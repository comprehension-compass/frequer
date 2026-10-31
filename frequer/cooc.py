"""Co-occurrence counts per shard, and their merge: the pure core of the association pass.

Counted in the same pass as the lemma frequencies, over the **release's own
word lemmas** (``ReleaseAnalysis.tagged``: a unit's members keep their own
lemmas, as in the text), each keyed exactly as the unit detector keys a token
(:func:`nlp.units.token_keys`: the lower-cased lemma) with the homograph key
taken off (``See#Fem`` -> ``see``). Per sentence:

- ``n``: contiguous key n-grams, ``n_min``..``n_max`` (2-4). A *boundary* token
  (punctuation, a key with no letter: figures, symbols) is never a member and
  an n-gram never reaches across one, so n-grams stay inside a stretch of
  words between punctuation;
- ``p``: verb pairs within a clause, exactly the release's own off-list pair
  candidates (:func:`nlp.unit_rules.open_spans`, source ``pair``: a verb with
  the release's reflexive pronoun, *se* / *sich*; a verb with a separated
  particle, *kommt ... an*), keeping those with no boundary token between the
  members. The key puts the verb first, then the other members in text order
  (``freuen sich``, ``kommen an``, ``setzen sich auseinander``); ``q`` counts the
  same pair again where no member is a token of a unit the release found (the
  passive *se utiliza* is the listed *se + verbo* construction, not a new verb);
- ``u``: every non-boundary key once (the marginals), and ``t``: its UPOS votes
  (``key UPOS``), so a report can tell function words from content words.

Each item also gets a document frequency. A shard writes its items sorted, one
``item<TAB>f<TAB>d`` line each under a JSON meta line, so any number of shard
files merge in one streaming pass (:func:`merge_files`) in constant memory, and
a lost shard is recounted alone. Nothing here touches the runtime.
"""

from __future__ import annotations

import gzip
import heapq
import json
from collections import Counter
from collections.abc import Iterable, Iterator, Sequence
from pathlib import Path
from typing import Any

FORMAT = 1
#: Item kinds: n-gram, verb pair, verb pair no release unit covers, unigram marginal, unigram UPOS vote.
NGRAM, PAIR, FREE_PAIR, UNIGRAM, TAG = "n", "p", "q", "u", "t"
VERBS = frozenset({"VERB", "AUX"})


def is_boundary(key: str) -> bool:
    """A token no co-occurrence item may hold or reach across."""
    return key == "_" or not any(ch.isalpha() for ch in key) or any(ch.isspace() for ch in key)


def bare_key(key: str) -> str:
    """``key`` without its homograph key (``see#fem`` -> ``see``), as ``nlp.lemma_step.split_key``."""
    at = key.find("#", 1)
    return key if at < 0 else key[:at]


def runs(keys: Sequence[str]) -> list[list[str]]:
    """Maximal stretches of non-boundary keys."""
    out: list[list[str]] = [[]]
    for key in keys:
        if is_boundary(key):
            if out[-1]:
                out.append([])
        else:
            out[-1].append(key)
    return [run for run in out if run]


def ngrams(keys: Sequence[str], n_min: int = 2, n_max: int = 4) -> Iterator[str]:
    """Every contiguous n-gram (``n_min``..``n_max``) inside a run, space-joined."""
    for run in runs(keys):
        for n in range(n_min, n_max + 1):
            for i in range(len(run) - n + 1):
                yield " ".join(run[i : i + n])


def pair_key(keys: Sequence[str], upos: Sequence[str], tokens: Sequence[int]) -> str | None:
    """A verb pair's key (verb first, then the rest in text order), or None if a
    boundary token lies between its members or it holds no verb."""
    lo, hi = min(tokens), max(tokens)
    if any(is_boundary(keys[t]) for t in tokens) or any(is_boundary(keys[k]) for k in range(lo + 1, hi)):
        return None
    verb = next((t for t in sorted(tokens) if upos[t] in VERBS), None)
    if verb is None:
        return None
    return " ".join([keys[verb], *(keys[t] for t in sorted(tokens) if t != verb)])


class CoocAccumulator:
    """One shard's co-occurrence counts (frequency and document frequency per item)."""

    def __init__(self, n_min: int = 2, n_max: int = 4) -> None:
        self.n_min, self.n_max = n_min, n_max
        self.f: Counter[str] = Counter()
        self.d: Counter[str] = Counter()
        self.tokens = 0
        self.sentences = 0
        self._doc: set[str] = set()

    def add_sentence(
        self, keys: Sequence[str], upos: Sequence[str], pairs: Iterable[Sequence[int]] = (),
        covered: frozenset[int] = frozenset(),
    ) -> None:
        """Count one sentence: ``keys``/``upos`` per token, ``pairs`` as token indices,
        ``covered`` the tokens of the release's units."""
        self.sentences += 1
        items: list[str] = []
        for key, tag in zip(keys, upos, strict=True):
            if not is_boundary(key):
                items.append(f"{UNIGRAM}\t{key}")
                items.append(f"{TAG}\t{key} {tag}")
        self.tokens += len(items) // 2
        items.extend(f"{NGRAM}\t{g}" for g in ngrams(keys, self.n_min, self.n_max))
        for tokens in pairs:
            pk = pair_key(keys, upos, tokens)
            if pk is not None:
                items.append(f"{PAIR}\t{pk}")
                if not covered.intersection(tokens):
                    items.append(f"{FREE_PAIR}\t{pk}")
        self.f.update(items)
        self._doc.update(items)

    def end_document(self) -> None:
        self.d.update(self._doc)
        self._doc.clear()

    def write(self, path: Path, meta: dict[str, Any]) -> None:
        self.end_document()
        head = {"format": FORMAT, "tokens": self.tokens, "sentences": self.sentences,
                "n_min": self.n_min, "n_max": self.n_max, **meta}
        write_items(path, head, ((item, self.f[item], self.d[item]) for item in sorted(self.f)))


Item = tuple[str, int, int]


def write_items(path: Path, meta: dict[str, Any], items: Iterable[Item]) -> int:
    """Write sorted ``(item, f, d)`` rows under a JSON meta line; returns the row count."""
    tmp = path.with_name(path.name + ".tmp")
    rows = 0
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=3) as fp:
        fp.write(json.dumps(meta, ensure_ascii=False, separators=(",", ":")) + "\n")
        for item, f, d in items:
            fp.write(f"{item}\t{f}\t{d}\n")
            rows += 1
    tmp.replace(path)
    return rows


def read_meta(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        meta: dict[str, Any] = json.loads(fp.readline())
    if meta.get("format") != FORMAT:
        raise ValueError(f"{path}: co-occurrence format {meta.get('format')} != {FORMAT}")
    return meta


def read_items(path: Path) -> Iterator[Item]:
    """Rows of one file, in its (sorted) order; the meta line is skipped."""
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        fp.readline()
        for line in fp:
            kind, rest = line.rstrip("\n").split("\t", 1)
            key, f, d = rest.rsplit("\t", 2)
            yield f"{kind}\t{key}", int(f), int(d)


def merge_items(streams: Sequence[Iterable[Item]], min_count: int = 1) -> Iterator[Item]:
    """Sum sorted streams item by item; drop items whose total is below ``min_count``."""
    current: str | None = None
    f = d = 0
    for item, fi, di in heapq.merge(*streams, key=lambda row: row[0]):
        if item != current:
            if current is not None and f >= min_count:
                yield current, f, d
            current, f, d = item, 0, 0
        f += fi
        d += di
    if current is not None and f >= min_count:
        yield current, f, d


def merge_files(paths: Sequence[Path], out: Path, min_count: int = 1, extra: dict[str, Any] | None = None) -> dict[str, Any]:
    """Merge shard (or already merged) files into ``out``; returns the meta written.

    Token and sentence totals add; ``shards`` lists every shard id merged so far
    (a compaction's output knows which shards it holds). ``min_count`` above 1
    prunes, so only a final merge may use it.
    """
    metas = [read_meta(p) for p in paths]
    if len({(m["n_min"], m["n_max"]) for m in metas}) > 1:
        raise ValueError("co-occurrence files counted with different n-gram orders")
    shards: list[str] = sorted({s for m in metas for s in m.get("shards", [m.get("shard", "")]) if s})
    meta = {
        "format": FORMAT, "n_min": metas[0]["n_min"], "n_max": metas[0]["n_max"],
        "tokens": sum(m["tokens"] for m in metas), "sentences": sum(m["sentences"] for m in metas),
        "shards": shards, "min_count": max([min_count, *(m.get("min_count", 1) for m in metas)]),
        **(extra or {}),
    }
    meta["rows"] = write_items(out, meta, merge_items([read_items(p) for p in paths], min_count))
    return meta
