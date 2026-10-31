"""The co-occurrence build: merge, score, the shipped table and the labelling queue.

- **Compaction** (during ``count``): finished shard files fold into one running
  file, ``cooc-acc.gz``, which records the shards it holds, so disk keeps one
  merged file plus a few shards and a resumed run never adds a shard twice.
- **Merge + prune**: every shard file and the running file merge into
  ``cooc-merged.gz``, items below ``min_count`` dropped.
- **Score** (:mod:`frequer.assoc`) and ship ``<lang>.cooc.tsv.gz``: the
  positively associated items (``g2_min`` >= 10.83, p < 0.001; ``pmi_min`` > 0;
  at least ``ship_min_docs`` documents), at most ``ship_rows`` of them by
  ``g2_min``, for the unit detector to read as a feature.
- **The labelling queue** ``<lang>.cooc-queue.tsv``: the top combinations the
  release's unit list does not hold (:class:`UnitList`), ranked by ``g2_min``
  among those with ``npmi_min`` >= ``queue_min_npmi``, dropping n-grams of
  function words only, n-grams with a ``queue_edge_ban`` UPOS at either edge
  (a determiner or conjunction at the edge is a fragment: *el mejor*, *tener
  uno*), an auxiliary with a reflexive (the impersonal *se ha*), a pair seen
  inside a release unit at least half the time (*se utiliza* is the listed
  *se + verbo* construction), and n-grams that
  are mostly the inside of a longer queued one. UPOS is each key's majority vote.
"""

from __future__ import annotations

import gzip
import json
import math
from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer import assoc
from frequer.cooc import FREE_PAIR, PAIR, bare_key, merge_files, read_items, read_meta

ACC = "cooc-acc.gz"
MERGED = "cooc-merged.gz"
#: UPOS that make an n-gram "function words only" when every member has one.
FUNCTION_UPOS = frozenset({"ADP", "AUX", "CCONJ", "DET", "PART", "PRON", "SCONJ", "NUM", "PUNCT", "SYM"})


def shard_files(counts_dir: Path) -> list[Path]:
    """Finished shard co-occurrence files: those whose counts file (the done marker) exists."""
    out = []
    for path in sorted(counts_dir.glob("*.cooc.gz")):
        if path.name == ACC:
            continue
        if path.with_name(path.name.removesuffix(".cooc.gz") + ".json.gz").exists():
            out.append(path)
    return out


def _absorbed(acc: Path) -> set[str]:
    return set(read_meta(acc)["shards"]) if acc.exists() else set()


def compact(counts_dir: Path, *, at_least: int = 1) -> int:
    """Fold finished shard files into the running file; returns how many were folded."""
    acc = counts_dir / ACC
    held = _absorbed(acc)
    fresh: list[Path] = []
    for path in shard_files(counts_dir):
        if read_meta(path)["shard"] in held:
            path.unlink()  # folded already (a crash after the fold, before the delete)
        else:
            fresh.append(path)
    if len(fresh) < at_least or not fresh:
        return 0
    tmp = counts_dir / (ACC + ".new")
    merge_files([acc, *fresh] if acc.exists() else fresh, tmp)
    tmp.replace(acc)
    for path in fresh:
        path.unlink()
    return len(fresh)


def merge_all(counts_dir: Path, out: Path, min_count: int) -> dict[str, Any]:
    """The final merge: the running file and every unfolded shard file, pruned."""
    acc = counts_dir / ACC
    held = _absorbed(acc)
    inputs = [p for p in shard_files(counts_dir) if read_meta(p)["shard"] not in held]
    if acc.exists():
        inputs.insert(0, acc)
    if not inputs:
        raise SystemExit(f"no co-occurrence files in {counts_dir}")
    return merge_files(inputs, out, min_count)


@dataclass
class UnitList:
    """The release's unit list as key sequences, for "is this combination listed?"."""

    #: Fixed-key sequences (homograph keys off) of every entry.
    seqs: set[tuple[str, ...]] = field(default_factory=set)
    #: Every contiguous piece (two keys or more) of a listed sequence of two keys or more.
    pieces: dict[tuple[str, ...], str] = field(default_factory=dict)
    #: Listed sequences of two keys or more, by length, for containment.
    long: dict[tuple[str, ...], str] = field(default_factory=dict)
    #: Lower-cased headwords of the unit list and the parts list.
    headwords: set[str] = field(default_factory=set)
    #: Sorted fixed keys of each entry (a pair matches whatever its order in text).
    bags: set[tuple[str, ...]] = field(default_factory=set)

    @classmethod
    def from_release(cls, release_dir: Path) -> UnitList:
        units = release_dir / "units"
        found = cls()
        if not (units / "list.json").exists():
            return found
        for row in json.loads((units / "list.json").read_text(encoding="utf-8")):
            seq = tuple(bare_key(k) for k in row["seq"])
            found.seqs.add(seq)
            found.bags.add(tuple(sorted(seq)))
            found.headwords.add(row["lemma"].lower())
            for _forms, head in row.get("by_forms") or ():
                found.headwords.add(str(head).lower())
            if len(seq) > 1:
                found.long.setdefault(seq, row["lemma"])
                for i in range(len(seq)):
                    for j in range(i + 2, len(seq) + 1):
                        found.pieces.setdefault(seq[i:j], row["lemma"])
        parts = json.loads((units / "parts.json").read_text(encoding="utf-8"))
        found.headwords.update(h.lower() for h in parts.get("heads", {}))
        return found

    def ngram_status(self, parts: Sequence[str]) -> tuple[bool, str]:
        """``(listed, contained)``: listed (or inside a listed unit), and the listed
        unit it extends, if any."""
        seq = tuple(parts)
        if seq in self.seqs or seq in self.pieces:
            return True, ""
        for i in range(len(seq)):
            for j in range(i + 2, len(seq) + 1):
                if seq[i:j] in self.long:
                    return False, self.long[seq[i:j]]
        return False, ""

    def pair_listed(self, parts: Sequence[str], head: str) -> bool:
        return head.lower() in self.headwords or tuple(sorted(parts)) in self.bags


@dataclass(frozen=True)
class Queued:
    row: assoc.Scored
    head: str
    contains: str
    #: For a pair: its occurrences where no member was a token of a release unit.
    free: int = 0


def queue(
    rows: Sequence[assoc.Scored],
    units: UnitList,
    tags: dict[str, str],
    heads: dict[str, str],
    *,
    min_npmi: float,
    top: int,
    edge_ban: frozenset[str] = frozenset(),
    free: dict[str, int] | None = None,
) -> list[Queued]:
    """The labelling queue (module docstring), best first."""
    picked: list[Queued] = []
    for row in rows:
        if math.isnan(row.npmi_min) or row.npmi_min < min_npmi:
            continue
        parts = row.keys.split(" ")
        if row.kind == PAIR:
            head = heads.get(row.keys, "")
            # An auxiliary with a reflexive is the impersonal se/sich (se ha, se puede), not a verb.
            unexplained = (free or {}).get(row.keys, 0)
            if tags.get(parts[0]) == "AUX" or units.pair_listed(parts, head):
                continue
            # Mostly inside a unit the release already found (se utiliza: se + verbo): not new.
            if free is not None and unexplained < 0.5 * row.f:
                continue
            picked.append(Queued(row, head, "", unexplained))
            continue
        if all(tags.get(p, "X") in FUNCTION_UPOS for p in parts):
            continue
        if tags.get(parts[0], "X") in edge_ban or tags.get(parts[-1], "X") in edge_ban:
            continue
        listed, contains = units.ngram_status(parts)
        if not listed:
            picked.append(Queued(row, "", contains))
    picked.sort(key=lambda q: (-q.row.g2_min, q.row.keys))
    # An n-gram that is mostly the inside of a longer queued one is that one's part.
    inside: dict[str, int] = {}
    for q in picked:
        if q.row.kind == PAIR:
            continue
        parts = q.row.keys.split(" ")
        for i in range(len(parts)):
            for j in range(i + 2, len(parts) + 1):
                if j - i < len(parts):
                    piece = " ".join(parts[i:j])
                    inside[piece] = max(inside.get(piece, 0), q.row.f)
    kept = [q for q in picked if q.row.kind == PAIR or inside.get(q.row.keys, 0) < 0.8 * q.row.f]
    return kept[:top]


@dataclass
class CoocResult:
    meta: dict[str, Any]
    scored: int
    by_kind: dict[str, int]
    shipped: list[assoc.Scored]
    queue: list[Queued]
    table_path: Path
    table_bytes: int
    queue_path: Path
    merged_rows: int


def build_cooc(
    counts_dir: Path,
    out_dir: Path,
    *,
    lang: str,
    cfg: Any,  # frequer.config.CoocConfig
    release_dir: Path,
    pair_windows: dict[int, float],
    pair_head: Callable[[str], str],
    header: dict[str, Any],
) -> CoocResult:
    merged = counts_dir.parent / MERGED
    meta = merge_all(counts_dir, merged, cfg.min_count)
    shipped, scored, by_kind = assoc.build_table(
        merged, min_count=cfg.min_count, pair_spans=pair_windows, keep=cfg.ship_rows,
        min_docs=cfg.ship_min_docs,
    )
    tags = assoc.tag_majority(read_items(merged))
    heads = {r.keys: pair_head(r.keys) for r in shipped if r.kind == PAIR}
    out_dir.mkdir(parents=True, exist_ok=True)
    table = out_dir / f"{lang}.cooc.tsv.gz"
    head = {
        **header, "tokens": meta["tokens"], "sentences": meta["sentences"], "shards": len(meta["shards"]),
        "min_count": cfg.min_count, "ship": {"rows": len(shipped), "max_rows": cfg.ship_rows,
                                             "min_docs": cfg.ship_min_docs, "g2_min_at_least": assoc.G2_P001,
                                             "pmi_min_above": 0},
        "columns": {
            "kind": "n = contiguous lemma n-gram in a sentence; p = verb pair in a clause (verb first)",
            "keys": "the unit detector's token keys (lower-cased lemma, homograph key off), space-joined",
            "f": "frequency", "d": "documents",
            "pmi": "log2 PMI against independence of all members",
            "pmi_min": "minimum PMI over binary splits (= pmi for two members)",
            "npmi_min": "normalised PMI of that split (Bouma 2009)",
            "g2_min": "signed log-likelihood G2 (Dunning 1993), minimum over binary splits",
            "head": "for a pair: the headword the release's rule gives it",
        },
    }
    with gzip.open(table, "wt", encoding="utf-8", compresslevel=9) as fp:
        fp.write("# " + json.dumps(head, ensure_ascii=False, separators=(",", ":")) + "\n")
        for line in assoc.table_lines(shipped, heads):
            fp.write(line + "\n")
    units = UnitList.from_release(release_dir)
    free = {item.split("\t", 1)[1]: f for item, f, _d in read_items(merged) if item[0] == FREE_PAIR}
    # Counts from before the unit-free pair count carry none: no filter then.
    free_or_none = free or None
    picked = queue(shipped, units, tags, heads, min_npmi=cfg.queue_min_npmi, top=cfg.queue_rows,
                   edge_ban=frozenset(cfg.queue_edge_ban), free=free_or_none)
    qpath = out_dir / f"{lang}.cooc-queue.tsv"
    write_queue(qpath, picked, tags)
    return CoocResult(meta, scored, by_kind, shipped, picked, table, table.stat().st_size, qpath,
                      int(meta.get("rows", 0)))


def write_queue(path: Path, picked: Iterable[Queued], tags: dict[str, str]) -> None:
    cols = ["rank", "kind", "keys", "upos", "head", "f", "d", "pmi_min", "npmi_min", "g2_min", "extends_listed",
            "pair_outside_units"]
    with path.open("w", encoding="utf-8") as fp:
        fp.write("\t".join(cols) + "\n")
        for k, q in enumerate(picked, start=1):
            r = q.row
            upos = " ".join(tags.get(p, "X") for p in r.keys.split(" "))
            fp.write("\t".join([str(k), r.kind, r.keys, upos, q.head, str(r.f), str(r.d), assoc.fmt(r.pmi_min),
                                assoc.fmt(r.npmi_min), f"{r.g2_min:.1f}", q.contains,
                                str(q.free) if r.kind == PAIR else ""]) + "\n")
