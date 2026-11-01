"""Take the convergence checkpoints that are due (:mod:`frequer.converge`) and apply the stopping rule."""

from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from frequer import converge, filters, snapshot
from frequer.config import Manifest
from frequer.converge import BANDS, KEEP, Ranked
from frequer.merge import MergeResult, merge_counts
from frequer.ranking import Row

CANDIDATE_FACTOR = 4


def ranked_of(rows: list[Row], tokens: int, shards: list[str]) -> Ranked:
    head = rows[:KEEP]
    return Ranked(tokens=tokens, shards=tuple(shards), lemmas=tuple(r.lemma for r in head),
                  freq=tuple(r.stats.freq for r in head), dp=tuple(r.scores["dp_adjusted"] for r in head))


def mix_of(manifest: Manifest, work_dir: Path, names: list[str]) -> str:
    """``full`` when the shards ``names`` hold every ``first`` source whole and every other
    source at least once; otherwise what is missing (``web only``: no ``first`` source yet)."""
    held: dict[tuple[str, int], int] = {}
    for name in names:
        src, url, _shard, *_ = name.split(".")
        held[(src, int(url))] = held.get((src, int(url)), 0) + 1
    missing: list[str] = []
    for source in manifest.sources:
        if source.first:
            for k in range(len(source.urls)):
                marker = work_dir / f"{source.name}.{k:02d}.done.json"
                cut = json.loads(marker.read_text(encoding="utf-8"))["shards"] if marker.exists() else None
                if cut is None or held.get((source.name, k), 0) < cut:
                    missing.append(source.name)
                    break
        elif not any(src == source.name for src, _k in held):
            missing.append(source.name)
    if not missing:
        return "full"
    firsts = {s.name for s in manifest.sources if s.first}
    if all(m in firsts for m in missing) and not any(src in firsts for src, _k in held):
        return "web only"
    return "partial (lacks " + ", ".join(missing) + ")"


def _rank(manifest: Manifest, counts_dir: Path, names: list[str]) -> tuple[MergeResult, list[Row]]:
    result = merge_counts(counts_dir, manifest.parts, manifest.language.top_n * CANDIDATE_FACTOR, only=set(names))
    weights = {s.name: s.weight for s in manifest.sources}
    # Convergence is judged on the list the snapshot holds: merges and every filter applied.
    return result, filters.apply(manifest, result.merged, weights).ranked


def _lemmas(manifest: Manifest, counts_dir: Path, names: list[str]) -> list[str]:
    if not names:
        return []
    _result, ranked = _rank(manifest, counts_dir, names)
    return [r.lemma for r in ranked[:KEEP]]


def row_of(r: Ranked, prev: Ranked | None, *, mix: str, sources: dict[str, int],
           half_a: list[str], half_b: list[str]) -> dict[str, Any]:
    """One convergence row (``converge`` module docstring)."""
    change = converge.compare(prev, r) if prev is not None else {}
    bands: dict[str, Any] = {}
    for n in BANDS:
        bands[str(n)] = {
            "change": change.get(str(n), {}).get("change"),
            "median_shift": change.get(str(n), {}).get("median_shift"),
            "freq_at_n": r.freq[n - 1] if len(r.freq) >= n else None,
            "split_half": converge.disagreement(half_a, half_b, n),
        }
    return {"tokens": r.tokens, "shards": len(r.shards), "sources": sources, "mix": mix, "bands": bands}


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
    done = {row["tokens"] for row in state["checkpoints"]}
    shards = converge.finished_shards(counts_dir, out_dir / "checkpoints" / converge.LEDGER)
    last: tuple[int, MergeResult, list[Row]] | None = None
    # Shards arriving together (from remote parts) make one checkpoint: the newest prefix.
    for tokens, names in converge.due(shards, done)[-1:]:
        result, ranked = _rank(manifest, counts_dir, names)
        r = ranked_of(ranked, result.merged.tokens, names)
        converge.save_ranked(out_dir / "checkpoints" / f"{tokens}.json.gz", r)
        prev = state["checkpoints"][-1] if state["checkpoints"] else None
        prev_r = converge.load_ranked(out_dir / "checkpoints" / f"{prev['tokens']}.json.gz") if prev else None
        a, b = converge.split_halves(names)
        row = row_of(r, prev_r, mix=mix_of(manifest, counts_dir.parent / "work", names),
                     sources={name: t.tokens for name, t in result.sources.items()},
                     half_a=_lemmas(manifest, counts_dir, a), half_b=_lemmas(manifest, counts_dir, b))
        state["checkpoints"].append(row)
        row["passes"] = converge.run_length(state["checkpoints"])
        if row["passes"] >= converge.STOP_RUN and state.get("decision") != "stop":
            state["decision"] = "stop"
            state["stopped_at"] = row["tokens"]
        log(f"checkpoint {row['tokens']:,} ({row['mix']}): split-half "
            + ", ".join(f"{int(n) // 1000}k {converge._pct(v['split_half'])}" for n, v in row["bands"].items())
            + f"; stop {row['passes']}/{converge.STOP_RUN}")
        last = (tokens, result, ranked)
        converge.write_state(out_dir, state)
    if last is not None and write_snapshot:
        tokens, result, ranked = last
        citation = None
        if cfg.readings:
            from frequer.runtime import Runtime

            citation = Runtime(cfg, lemma_dir=lemma_dir, wheel=wheel, fallback=cfg.fallback).backend.lemma_citation
        weights = {s.name: s.weight for s in manifest.sources}
        head = snapshot.header(result, manifest, "frequency", weights, f"checkpoint-{tokens}")
        entries = snapshot.build_entries(ranked[: cfg.top_n], result.merged, manifest, citation)
        dest = out_dir / f"checkpoint-{tokens}"
        snapshot.write_snapshot(dest / f"{cfg.code}.json", head, entries)
        converge.prune_snapshots(out_dir, dest)
        log(f"checkpoint snapshot: {dest / f'{cfg.code}.json'} ({len(entries):,} entries)")
    return state


def final_record(out_dir: Path, ranked: list[Row], tokens: int, *, mix: str) -> dict[str, Any] | None:
    """Record the final list and calibrate: each checkpoint's top N against the final top N."""
    state = converge.load_state(out_dir)
    if not state["checkpoints"]:
        return None
    final = [r.lemma for r in ranked[:KEEP]]
    for row in state["checkpoints"]:
        lemmas = converge.load_ranked(out_dir / "checkpoints" / f"{row['tokens']}.json.gz").lemmas
        for n in BANDS:
            row["bands"][str(n)]["vs_final"] = converge.disagreement(lemmas, final, n)
    state["final"] = {"tokens": tokens, "mix": mix}
    if state.get("decision") != "stop":
        state["decision"] = "built from everything counted (stopping rule not met)"
        state["stopped_at"] = tokens
    converge.write_state(out_dir, state)
    return state
