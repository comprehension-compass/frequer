"""Take the convergence checkpoints that are due (:mod:`frequer.converge`) and apply the stopping rule."""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from frequer import converge, snapshot
from frequer.config import Manifest
from frequer.converge import KEEP, Ranked
from frequer.merge import merge_counts
from frequer.ranking import Row, build_rows, rank_rows

CANDIDATE_FACTOR = 4


def ranked_of(rows: list[Row], tokens: int, shards: list[str]) -> Ranked:
    head = rows[:KEEP]
    return Ranked(tokens=tokens, shards=tuple(shards), lemmas=tuple(r.lemma for r in head),
                  freq=tuple(r.stats.freq for r in head), dp=tuple(r.scores["dp_adjusted"] for r in head))


def record(target: int | str, r: Ranked, prev: Ranked | None) -> dict[str, Any]:
    return {
        "target": target, "tokens": r.tokens, "shards": len(r.shards),
        "freq_at": {str(n): r.freq[n - 1] for n in converge.BANDS if len(r.freq) >= n},
        "dp_at": {str(n): round(r.dp[n - 1], 2) for n in converge.BANDS if len(r.dp) >= n},
        "comparison": converge.compare(prev, r) if prev is not None else None,
    }


def previous(out_dir: Path, state: dict[str, Any]) -> Ranked | None:
    numbered = [c for c in state["checkpoints"] if isinstance(c["target"], int)]
    if not numbered:
        return None
    return converge.load_ranked(out_dir / "checkpoints" / f"{numbered[-1]['target']}.json.gz")


def decide(state: dict[str, Any]) -> None:
    comparisons = [c["comparison"] for c in state["checkpoints"]
                   if isinstance(c["target"], int) and c["comparison"]]
    if converge.should_stop(comparisons) and state.get("decision") != "stop":
        state["decision"] = "stop"
        state["stopped_at"] = state["checkpoints"][-1]["tokens"]


def run_checkpoints(
    manifest: Manifest,
    counts_dir: Path,
    out_dir: Path,
    *,
    lemma_dir: Path | None = None,
    wheel: Path | None = None,
    write_snapshot: bool = True,
    log: Callable[[str], None] = print,
) -> dict[str, Any]:
    """Take every due checkpoint; returns the convergence state (``decision`` is ``stop`` or ``continue``)."""
    cfg = manifest.language
    state = converge.load_state(out_dir)
    done = {c["target"] for c in state["checkpoints"] if isinstance(c["target"], int)}
    shards = converge.finished_shards(counts_dir, out_dir / "checkpoints" / converge.LEDGER)
    pending = converge.due(shards, done)
    weights = {s.name: s.weight for s in manifest.sources}
    last: tuple[int, Any, list[Row]] | None = None
    for target, names in pending:
        result = merge_counts(counts_dir, manifest.parts, cfg.top_n * CANDIDATE_FACTOR, only=set(names))
        ranked = rank_rows(build_rows(result.merged, weights), "frequency")
        r = ranked_of(ranked, result.merged.tokens, names)
        converge.save_ranked(out_dir / "checkpoints" / f"{target}.json.gz", r)
        rec = record(target, r, previous(out_dir, state))
        state["checkpoints"].append(rec)
        overlap = (rec["comparison"] or {}).get("bands", {})
        log(f"checkpoint {target:,}: {r.tokens:,} tokens, {len(names)} shards; overlap "
            + ", ".join(f"{int(n) // 1000}k {b['overlap']:.1%}" for n, b in overlap.items() if b["overlap"] is not None))
        last = (target, result, ranked)
        decide(state)
        converge.write_state(out_dir, state)
    if last is not None and write_snapshot:
        target, result, ranked = last
        citation = None
        if cfg.readings:
            from frequer.runtime import Runtime

            citation = Runtime(cfg, lemma_dir=lemma_dir, wheel=wheel, fallback=cfg.fallback).backend.lemma_citation
        head = snapshot.header(result, manifest, "frequency", weights, f"checkpoint-{result.merged.tokens}")
        entries = snapshot.build_entries(ranked[: cfg.top_n], result.merged, manifest, citation)
        dest = out_dir / f"checkpoint-{target}"
        snapshot.write_snapshot(dest / f"{cfg.code}.json", head, entries)
        converge.prune_snapshots(out_dir, dest)
        log(f"checkpoint snapshot: {dest / f'{cfg.code}.json'} ({len(entries):,} entries)")
    return state


def final_record(out_dir: Path, ranked: list[Row], tokens: int, shards: list[str]) -> dict[str, Any] | None:
    """Add the final build to the convergence table (compared with the last checkpoint)."""
    state = converge.load_state(out_dir)
    if not state["checkpoints"]:
        return None
    state["checkpoints"] = [c for c in state["checkpoints"] if c["target"] != "final"]
    prev = previous(out_dir, state)
    if prev is not None and prev.tokens == tokens:
        converge.write_state(out_dir, state)
        return state
    state["checkpoints"].append(record("final", ranked_of(ranked, tokens, shards), prev))
    if state.get("decision") != "stop":
        state["decision"] = "built from everything counted (stopping rule not met)"
        state["stopped_at"] = tokens
    converge.write_state(out_dir, state)
    return state
