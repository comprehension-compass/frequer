"""Convergence checkpoints and the stopping rule (developer spec, 2026-11-01).

A list good enough for pre-generation does not need the whole corpus manifest:
counting stops once the list is stable. After **every counted shard** the shards
counted so far (in the order they finished) are merged into a checkpoint, which
gets one row in ``convergence.md`` / ``convergence.json``: total tokens, tokens
per source, the source mix, and per band N in 5k / 10k / 20k / 50k:

- ``change``: the share of the top N that was not in the previous checkpoint's top N;
- ``median_shift``: median absolute rank shift of the lemmas in both top-N lists;
- ``freq_at_n``: the raw frequency of the lemma at rank N;
- ``split_half``: 1 - overlap of the top N ranked from half A against half B, the
  shards split alternately into A and B within each source (both halves have the
  same source mix; a source with an odd count leaves its newest shard out).

**Stopping rule:** stop when three consecutive full-mix checkpoints give split-half
disagreement <= 5 % at top 20k and <= 10 % at top 50k, then build the final
snapshot from everything counted. Two independent halves differ about twice as
much as either differs from the converged list, so split-half disagreement
estimates (twice) the change the rest of the corpus would still make; the
**calibration** table (each checkpoint against the final list) checks that.

Each checkpoint's ranking (top ``KEEP``) is kept in ``checkpoints/<tokens>.json.gz``;
the latest checkpoint snapshot (the loader's format) is ``checkpoint-<tokens>/<lang>.json``.
"""

from __future__ import annotations

import gzip
import json
import shutil
import statistics
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer.counts import iter_counts, read_shard

BANDS = (5_000, 10_000, 20_000, 50_000)
#: Lemmas kept per checkpoint ranking (the widest band).
KEEP = max(BANDS)
#: Split-half disagreement ceilings for a passing checkpoint.
STOP_SPLIT = {20_000: 0.05, 50_000: 0.10}
#: Consecutive passing full-mix checkpoints that stop the run.
STOP_RUN = 3
LEDGER = "ledger.json"


@dataclass(frozen=True)
class Ranked:
    """One ranking's head: lemma, raw frequency, dispersion-adjusted score."""

    tokens: int
    shards: tuple[str, ...]
    lemmas: tuple[str, ...]
    freq: tuple[int, ...]
    dp: tuple[float, ...]


def disagreement(a: Sequence[str], b: Sequence[str], n: int) -> float | None:
    """Share of ``b``'s top ``n`` not in ``a``'s top ``n`` (None when either is shorter than ``n``)."""
    if len(a) < n or len(b) < n:
        return None
    top = set(a[:n])
    return sum(1 for x in b[:n] if x not in top) / n


def compare(prev: Ranked, cur: Ranked, bands: Sequence[int] = BANDS) -> dict[str, Any]:
    """``cur`` against the previous checkpoint, per band."""
    out: dict[str, Any] = {}
    for n in bands:
        a = {lemma: i for i, lemma in enumerate(prev.lemmas[:n])}
        shifts = [abs(a[x] - i) for i, x in enumerate(cur.lemmas[:n]) if x in a]
        out[str(n)] = {
            "change": disagreement(prev.lemmas, cur.lemmas, n),
            "median_shift": statistics.median(shifts) if shifts else None,
        }
    return out


def split_halves(names: Sequence[str]) -> tuple[list[str], list[str]]:
    """Shards (in finishing order) dealt alternately into halves A and B within each source;
    a source with an odd count leaves its newest shard out."""
    by_source: dict[str, list[str]] = {}
    for name in names:
        by_source.setdefault(name.split(".", 1)[0], []).append(name)
    a: list[str] = []
    b: list[str] = []
    for shards in by_source.values():
        even = shards[: len(shards) - len(shards) % 2]
        a += even[0::2]
        b += even[1::2]
    return a, b


def passes(row: dict[str, Any]) -> bool:
    """One checkpoint passes: full mix and split-half disagreement under every ceiling."""
    if row.get("mix") != "full":
        return False
    for n, ceiling in STOP_SPLIT.items():
        value = row["bands"].get(str(n), {}).get("split_half")
        if value is None or value > ceiling:
            return False
    return True


def run_length(rows: Sequence[dict[str, Any]]) -> int:
    """Consecutive passing checkpoints at the end of ``rows``."""
    k = 0
    for row in reversed(rows):
        if not passes(row):
            break
        k += 1
    return k


# -- bookkeeping -------------------------------------------------------------


def finished_shards(counts_dir: Path, ledger_path: Path) -> list[tuple[str, int, float]]:
    """``(name, tokens, mtime)`` of every counted shard, in the order they finished (tokens cached)."""
    ledger: dict[str, list[float]] = {}
    if ledger_path.exists():
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    out: list[tuple[str, int, float]] = []
    changed = False
    for _source, path in iter_counts(counts_dir):
        mtime = path.stat().st_mtime
        cached = ledger.get(path.name)
        if cached is None or cached[1] != mtime:
            cached = [float(read_shard(path)["tokens"]), mtime]
            ledger[path.name] = cached
            changed = True
        out.append((path.name, int(cached[0]), mtime))
    if changed:
        ledger_path.parent.mkdir(parents=True, exist_ok=True)
        ledger_path.write_text(json.dumps(ledger, indent=0), encoding="utf-8")
    out.sort(key=lambda t: (t[2], t[0]))
    return out


def due(shards: Sequence[tuple[str, int, float]], done: set[int]) -> list[tuple[int, list[str]]]:
    """Checkpoints not yet taken, one after every finished shard: ``(cumulative tokens, shard names)``."""
    out: list[tuple[int, list[str]]] = []
    cum = 0
    names: list[str] = []
    for name, tokens, _mtime in shards:
        cum += tokens
        names.append(name)
        if cum not in done:
            out.append((cum, list(names)))
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


def _pct(x: Any) -> str:
    return "-" if x is None else f"{x:.1%}"


def _num(x: Any) -> str:
    return "-" if x is None else f"{x:,.0f}"


def render_table(state: dict[str, Any]) -> list[str]:
    """The convergence section: one row per checkpoint, then the calibration table if built."""
    out = ["## Convergence", "",
           "One row per counted shard: the shards counted so far, in the order they finished. Per band N: "
           "**chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| "
           "of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement "
           "(1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each "
           "source; a source with an odd count leaves its newest shard out). Stopping rule: "
           f"{STOP_RUN} consecutive full-mix checkpoints with split <= {STOP_SPLIT[20_000]:.0%} at 20k and "
           f"<= {STOP_SPLIT[50_000]:.0%} at 50k.", ""]
    cols = ["tokens", "per source", "mix"]
    for n in BANDS:
        k = f"{n // 1000}k"
        cols += [f"{k} chg", f"{k} shift", f"f@{k}", f"{k} split"]
    cols.append("stop")
    out += ["| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]
    for row in state["checkpoints"]:
        cells = [f"{row['tokens']:,}", ", ".join(f"{k} {v:,}" for k, v in row["sources"].items()), row["mix"]]
        for n in BANDS:
            band = row["bands"].get(str(n), {})
            cells += [_pct(band.get("change")), _num(band.get("median_shift")),
                      _num(band.get("freq_at_n")), _pct(band.get("split_half"))]
        cells.append(f"{row['passes']}/{STOP_RUN}")
        out.append("| " + " | ".join(cells) + " |")
    final = state.get("final")
    out += ["", f"Decision: **{state.get('decision', 'continue')}**"
            + (f" at {state['stopped_at']:,} tokens." if state.get("stopped_at") else ".")]
    if final:
        out += [f"Final list: {final['tokens']:,} tokens ({final['mix']}).", "",
                "### Calibration", "",
                "Each checkpoint's full-data top N against the final list's top N (**vs final**: share of the "
                "final top N not in the checkpoint's), next to its split-half disagreement. If split-half "
                "estimates the remaining change, split ~ 2 x vs final.", ""]
        cols = ["tokens"]
        for n in BANDS:
            k = f"{n // 1000}k"
            cols += [f"{k} split", f"{k} vs final", f"{k} ratio"]
        out += ["| " + " | ".join(cols) + " |", "|" + " --- |" * len(cols)]
        for row in state["checkpoints"]:
            cells = [f"{row['tokens']:,}"]
            for n in BANDS:
                band = row["bands"].get(str(n), {})
                split, vs = band.get("split_half"), band.get("vs_final")
                cells += [_pct(split), _pct(vs), "-" if not split or not vs else f"{split / vs:.2f}"]
            out.append("| " + " | ".join(cells) + " |")
    out.append("")
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
