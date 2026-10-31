"""Merge, rank, write the snapshot and sidecar, run the review checks, write the report."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer import checks, combos, compare, perf, report, snapshot
from frequer.config import Manifest
from frequer.counting import peak_rss_mb
from frequer.hygiene import make_classifier
from frequer.merge import merge_counts
from frequer.ranking import SCORES, build_rows, rank_rows
from frequer.runtime import Runtime

#: wordfreq's code for each language is the manifest's own code.
CANDIDATE_FACTOR = 4


@dataclass(frozen=True)
class BuildOptions:
    score: str = "frequency"
    top_n: int | None = None
    candidates: int | None = None
    scope: str = "full"
    lemma_dir: Path | None = None
    wheel: Path | None = None
    live_snapshot: Path | None = None
    write_snapshot: bool = True


def build_language(manifest: Manifest, counts_dir: Path, out_dir: Path, opts: BuildOptions) -> dict[str, Any]:
    if opts.score not in SCORES:
        raise SystemExit(f"unknown score {opts.score!r}; choose from {SCORES}")
    cfg = manifest.language
    top_n = opts.top_n or cfg.top_n
    timings: dict[str, float] = {}

    t0 = time.perf_counter()
    result = merge_counts(counts_dir, manifest.parts, opts.candidates or top_n * CANDIDATE_FACTOR)
    timings["merge"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    weights = {s.name: s.weight for s in manifest.sources}
    rows = build_rows(result.merged, weights)
    ranked = rank_rows(rows, opts.score)
    timings["rank"] = time.perf_counter() - t0

    runtime = Runtime(cfg, lemma_dir=opts.lemma_dir, wheel=opts.wheel, fallback=cfg.fallback)
    for key in ("lemma_sha256", "fallback", "honeyeater_commit"):
        if getattr(runtime.info, key) != result.runtime[key]:
            raise SystemExit(f"the installed runtime's {key} differs from the one the shards were counted with")

    t0 = time.perf_counter()
    head = snapshot.header(result, manifest, opts.score, weights, opts.scope)
    citation = runtime.backend.lemma_citation if cfg.readings else None
    entries = snapshot.build_entries(ranked[:top_n], result.merged, manifest, citation)
    out_dir.mkdir(parents=True, exist_ok=True)
    if opts.write_snapshot:
        snapshot.write_snapshot(out_dir / f"{cfg.code}.json", head, entries)
        snapshot.write_sidecar(out_dir / f"{cfg.code}.dispersion.json.gz", head, ranked, result.merged, top_n)
    timings["snapshot"] = time.perf_counter() - t0

    cooc: combos.CoocResult | None = None
    if manifest.cooc.enabled:
        t0 = time.perf_counter()
        cooc = combos.build_cooc(
            counts_dir, out_dir, lang=cfg.code, cfg=manifest.cooc, release_dir=runtime.release_dir,
            pair_windows=runtime.pair_windows(), pair_head=runtime.pair_headword,
            header={k: head[k] for k in ("source", "corpus", "built", "lemma_release", "honeyeater")},
        )
        timings["cooc"] = time.perf_counter() - t0

    t0 = time.perf_counter()
    live_path = opts.live_snapshot or runtime.root / "reference" / "lemmas" / f"{cfg.code}.json"
    live = compare.load_live_ranks(live_path) if live_path.exists() else None
    shift = compare.live_shift(live, [r.lemma for r in ranked]) if live else None
    found = checks.run_checks(ranked, manifest.checks, runtime.lemma_of_word)
    zipf = compare.zipf_lookup()
    window = ranked[: manifest.checks.review_top_n]
    classify = make_classifier()
    foreign = checks.foreign_candidates(window, cfg.code, classify, zipf)
    foreign.sort(key=lambda f: -f.frequency)
    proper = checks.proper_noun_candidates(window)
    proper.sort(key=lambda f: -f.frequency)
    wf = compare.wordfreq_comparison([r.lemma for r in ranked], cfg.code, runtime.lemma_of_word)
    note = ("wordfreq is not installed in this environment (install it into FREQUER_DEPS)."
            if zipf is None else f"wordfreq has no usable list for `{cfg.code}`.")
    alts = compare.alternative_rankings(rows, opts.score)
    text = report.render(
        lang=cfg.code, scope=opts.scope, head=head, result=result, ranked=ranked, shift=shift, checks=found,
        wf=wf, wordfreq_note=note, foreign=foreign, proper=proper, alts=alts, cooc=cooc,
        live_label=f"the live snapshot (`reference/lemmas/{cfg.code}.json`)",
    )
    report.write(out_dir / "report.md", text)
    timings["report"] = time.perf_counter() - t0

    summary = {
        "language": cfg.code, "scope": opts.scope, "tokens": result.merged.tokens,
        "documents": result.merged.docs, "lemma_types_ranked": len(ranked), "snapshot_entries": len(entries),
        "stages": perf.stage_table(result), "build_seconds": {k: round(v, 2) for k, v in timings.items()},
        "worker_peak_rss_mb": round(result.peak_rss_mb), "build_process_peak_rss_mb": round(peak_rss_mb()),
        "host_tokens": result.host_tokens, "occurrence_kinds": dict(result.occurrence_kinds),
        "uncounted_occurrences": result.uncounted_occurrences, "sentences": result.sentences,
        "units_found": len(result.merged.units),
        "cooc": None if cooc is None else {
            "merged_rows_at_min_count": cooc.merged_rows, "scored": cooc.scored, "by_kind": cooc.by_kind,
            "shipped_rows": len(cooc.shipped), "table_bytes": cooc.table_bytes, "queue_rows": len(cooc.queue),
        },
        "checks": {k: len(v) for k, v in found.items()},
    }
    (out_dir / "perf.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    return summary

