"""Convergence checkpoints and the stopping rule (developer direction, 2026-11-01).

A list that is good enough for pre-generation does not need the whole corpus
manifest: counting can stop once more text no longer moves the list. So, at
cumulative token counts of 10M, 25M, 50M, 100M and every 50M after, the shards
counted so far (in the order they finished) are merged into a **checkpoint**,
and each checkpoint is compared with the one before it, per band N in
5k / 10k / 20k / 50k:

- ``overlap``: the share of the previous top N still in the top N;
- ``spearman`` and ``median_shift``: rank stability of the lemmas in both top-N
  lists (Spearman on their ranks; median absolute rank shift);
- ``freq_at_n`` / ``dp_at_n``: the raw frequency and the dispersion-adjusted
  score (``f x (1 - DP_norm)``) of the lemma at rank N.

**Stopping rule:** stop once two consecutive comparisons both give top-20k
overlap >= 98 % and top-50k overlap >= 95 % (or when the manifest runs out),
then build the final snapshot from what was counted.

A checkpoint's ranking (top ``KEEP`` lemmas) is kept under
``<out>/checkpoints/<tokens>.json.gz`` so later comparisons need no re-merge;
``<out>/convergence.json`` holds every comparison and the decision, and the
latest checkpoint snapshot (the loader's format) is
``<out>/checkpoint-<tokens>/<lang>.json``; older checkpoint snapshots are removed.
"""

from __future__ import annotations

import gzip
import json
import shutil
import statistics
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer.counts import iter_counts, read_shard

BANDS = (5_000, 10_000, 20_000, 50_000)
#: Lemmas kept per checkpoint ranking (the widest band).
KEEP = max(BANDS)
FIRST = (10_000_000, 25_000_000, 50_000_000, 100_000_000)
STEP = 50_000_000
#: Stop when this many consecutive comparisons all meet every threshold.
STOP_RUN = 2
STOP_OVERLAP = {20_000: 0.98, 50_000: 0.95}
LEDGER = "ledger.json"


def schedule() -> Iterator[int]:
    """Checkpoint targets in tokens: 10M, 25M, 50M, 100M, 150M, 200M, ..."""
    yield from FIRST
    t = FIRST[-1]
    while True:
        t += STEP
        yield t


@dataclass(frozen=True)
class Ranked:
    """One checkpoint's ranking: lemma, raw frequency, dispersion-adjusted score."""

    tokens: int
    shards: tuple[str, ...]
    lemmas: tuple[str, ...]
    freq: tuple[int, ...]
    dp: tuple[float, ...]


def spearman(xs: Sequence[float], ys: Sequence[float]) -> float | None:
    """Spearman's rho of two equal-length sequences of distinct ranks."""
    n = len(xs)
    if n < 2:
        return None

    def ranks(v: Sequence[float]) -> list[int]:
        order = sorted(range(n), key=lambda i: v[i])
        out = [0] * n
        for r, i in enumerate(order):
            out[i] = r
        return out

    rx, ry = ranks(xs), ranks(ys)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry, strict=True))
    return 1.0 - 6.0 * d2 / (n * (n * n - 1))


def compare(prev: Ranked, cur: Ranked, bands: Sequence[int] = BANDS) -> dict[str, Any]:
    """The band metrics of ``cur`` against ``prev`` (module docstring)."""
    out: dict[str, Any] = {"tokens": cur.tokens, "previous_tokens": prev.tokens, "bands": {}}
    for n in bands:
        a = {lemma: i for i, lemma in enumerate(prev.lemmas[:n])}
        b = {lemma: i for i, lemma in enumerate(cur.lemmas[:n])}
        common = [lemma for lemma in a if lemma in b]
        size = min(n, len(prev.lemmas))
        band: dict[str, Any] = {
            "overlap": len(common) / size if size else None,
            "spearman": spearman([a[x] for x in common], [b[x] for x in common]),
            "median_shift": statistics.median(abs(a[x] - b[x]) for x in common) if common else None,
            "freq_at_n": cur.freq[n - 1] if len(cur.freq) >= n else None,
            "dp_at_n": round(cur.dp[n - 1], 2) if len(cur.dp) >= n else None,
            "complete": len(prev.lemmas) >= n and len(cur.lemmas) >= n,
        }
        out["bands"][str(n)] = band
    return out


def meets(comparison: dict[str, Any]) -> bool:
    """True when one comparison passes every stopping threshold."""
    for n, floor in STOP_OVERLAP.items():
        band = comparison["bands"].get(str(n))
        if band is None or not band["complete"] or band["overlap"] is None or band["overlap"] < floor:
            return False
    return True


def should_stop(comparisons: Sequence[dict[str, Any]]) -> bool:
    """The stopping rule: the last ``STOP_RUN`` comparisons all pass."""
    return len(comparisons) >= STOP_RUN and all(meets(c) for c in comparisons[-STOP_RUN:])


# -- the checkpoint runner -------------------------------------------------


def _shard_tokens(path: Path) -> int:
    return int(read_shard(path)["tokens"])


def finished_shards(counts_dir: Path, ledger_path: Path) -> list[tuple[str, int, float]]:
    """``(name, tokens, mtime)`` of every counted shard, in the order they finished.

    Token totals are cached in the ledger, so a shard file is read once.
    """
    ledger: dict[str, list[float]] = {}
    if ledger_path.exists():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    out: list[tuple[str, int, float]] = []
    changed = False
    for _source, path in iter_counts(counts_dir):
        mtime = path.stat().st_mtime
        cached = ledger.get(path.name)
        if cached is None or cached[1] != mtime:
            cached = [float(_shard_tokens(path)), mtime]
            ledger[path.name] = cached
            changed = True
        out.append((path.name, int(cached[0]), mtime))
    if changed:
        ledger_path.parent.mkdir(parents=True, exist_ok=True)
        ledger_path.write_text(json.dumps(ledger, indent=0), encoding="utf-8")
    out.sort(key=lambda t: (t[2], t[0]))
    return out


def due(shards: Sequence[tuple[str, int, float]], done: set[int]) -> list[tuple[int, list[str]]]:
    """Checkpoints not yet taken: ``(target, shard names)``, the shortest prefix reaching each target."""
    out: list[tuple[int, list[str]]] = []
    cum = 0
    names: list[str] = []
    targets = schedule()
    target = next(targets)
    for name, tokens, _mtime in shards:
        cum += tokens
        names.append(name)
        while cum >= target:
            if target not in done:
                out.append((target, list(names)))
            target = next(targets)
    return out


def save_ranked(path: Path, r: Ranked) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = {"tokens": r.tokens, "shards": list(r.shards), "lemmas": list(r.lemmas),
            "freq": list(r.freq), "dp": [round(x, 3) for x in r.dp]}
    with gzip.open(path, "wt", encoding="utf-8") as fp:
        json.dump(body, fp, ensure_ascii=False, separators=(",", ":"))


def load_ranked(path: Path) -> Ranked:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        b = json.load(fp)
    return Ranked(b["tokens"], tuple(b["shards"]), tuple(b["lemmas"]), tuple(b["freq"]), tuple(b["dp"]))


def render_table(state: dict[str, Any]) -> list[str]:
    """The convergence section of the build report."""
    out = ["## Convergence", "",
           "Each checkpoint merges the shards counted so far (in the order they finished) and is compared "
           "with the previous one. Overlap: share of the previous top N still in the top N; Spearman and "
           "median |rank shift| over the lemmas in both; f@N and dp@N: raw frequency and dispersion-adjusted "
           "score (`f x (1 - DP_norm)`) of the lemma at rank N. Stopping rule: two consecutive checkpoints with "
           f"top-20k overlap >= {STOP_OVERLAP[20_000]:.0%} and top-50k overlap >= {STOP_OVERLAP[50_000]:.0%}.", ""]
    cols = ["tokens"]
    for n in BANDS:
        k = f"{n // 1000}k"
        cols += [f"{k} overlap", f"{k} rho", f"{k} med shift", f"f@{k}", f"dp@{k}"]
    out += ["| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]

    def num(x: Any, fmt: str) -> str:
        return "-" if x is None else format(x, fmt)

    for ck in state["checkpoints"]:
        row = [f"{ck['tokens']:,}"]
        cmp_ = ck.get("comparison")
        for n in BANDS:
            band = (cmp_ or {}).get("bands", {}).get(str(n), {})
            row += [num(band.get("overlap"), ".1%"), num(band.get("spearman"), ".3f"),
                    num(band.get("median_shift"), ",.0f"),
                    num(ck["freq_at"].get(str(n)), ","), num(ck["dp_at"].get(str(n)), ",.1f")]
        out.append("| " + " | ".join(row) + " |")
    out += ["", f"Decision: **{state.get('decision', 'continue')}**"
            + (f" at {state['stopped_at']:,} tokens." if state.get("stopped_at") else "."), ""]
    return out


def write_state(out_dir: Path, state: dict[str, Any]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "convergence.json").write_text(json.dumps(state, indent=1), encoding="utf-8")
    (out_dir / "convergence.md").write_text("\n".join(render_table(state)) + "\n", encoding="utf-8")


def load_state(out_dir: Path) -> dict[str, Any]:
    path = out_dir / "convergence.json"
    if path.exists():
        state: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return state
    return {"checkpoints": [], "decision": "continue", "stopped_at": None}


def prune_snapshots(out_dir: Path, keep: Path) -> None:
    for old in out_dir.glob("checkpoint-*"):
        if old.is_dir() and old != keep:
            shutil.rmtree(old)
