"""Merge, rank, write the snapshot and sidecar, run the review checks, write the report."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer import (
    checks,
    combos,
    compare,
    converge,
    exclude,
    filters,
    junk_report,
    perf,
    propn,
    report,
    snapshot,
)
from frequer.checkpoint import final_record, mix_of
from frequer.config import REPO_ROOT, Manifest
from frequer.counting import peak_rss_mb
from frequer.counts import iter_counts
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
    #: an interim list: place names waiting for the learnable-names list are left out instead of kept
    leave_out_pending_names: bool = False


def build_language(manifest: Manifest, counts_dir: Path, out_dir: Path, opts: BuildOptions) -> dict[str, Any]:
    if opts.score not in SCORES:
        raise SystemExit(f"unknown score {opts.score!r}; choose from {SCORES}")
    cfg = manifest.language
    top_n = opts.top_n or cfg.top_n
    timings: dict[str, float] = {}

    t0 = time.perf_counter()
    result = merge_counts(counts_dir, manifest.parts, opts.candidates or top_n * CANDIDATE_FACTOR)
    timings["merge"] = time.perf_counter() - t0

    runtime = Runtime(cfg, lemma_dir=opts.lemma_dir, wheel=opts.wheel, fallback=cfg.fallback)
    for key in ("lemma_sha256", "fallback", "honeyeater_commit"):
        if getattr(runtime.info, key) != result.runtime[key]:
            raise SystemExit(f"the installed runtime's {key} differs from the one the shards were counted with")

    # Merges, rank, then the exclusion list, the proper-noun rule and the junk rules (frequer/filters.py).
    t0 = time.perf_counter()
    weights = {s.name: s.weight for s in manifest.sources}
    flt = filters.apply(manifest, result.merged, weights, opts.score, runtime.root)
    rows = build_rows(result.merged, weights)
    if opts.leave_out_pending_names:
        pending = {r.lemma for r in flt.routed if r.action == "pending-names"}
        flt.ranked = [r for r in flt.ranked if r.lemma not in pending]
    ranked, exclusions, dropped, propn_dropped = flt.ranked, flt.exclusions, flt.excluded, flt.propn_dropped
    timings["rank"] = time.perf_counter() - t0
    propn_head: dict[str, Any] = {"rule": "none"}
    propn_text: list[str] = []
    if cfg.propn_rule == "capitalised_mid_sentence" and flt.learnable is not None and flt.tally is not None:
        propn_head = propn.header_entry(flt.learnable, flt.tally, cfg.propn_capitalised_min, propn_dropped,
                                        flt.names_kept, flt.case_kept, top_n, runtime.root, REPO_ROOT)
        propn_text = propn.render(flt.learnable, flt.tally, cfg.propn_capitalised_min, propn_dropped,
                                  flt.names_kept, flt.case_kept, top_n)

    t0 = time.perf_counter()
    head = snapshot.header(result, manifest, opts.score, weights, opts.scope)
    excluded = exclude.header_entry(exclusions, dropped, top_n, REPO_ROOT)
    if excluded is not None:
        head["exclusions"] = excluded
    head["proper_nouns"] = propn_head
    if opts.leave_out_pending_names:
        head["pending_names"] = "left out (interim list; place names wait for the learnable-names list)"
    if flt.flags is not None:
        head["junk"] = junk_report.header_entry(manifest, flt, top_n, REPO_ROOT)
    citation = runtime.backend.lemma_citation if cfg.readings else None
    # Learnable names (Honeyeater reference/learnable-names) not in the top_n follow it, in frequency order.
    appended = []
    if flt.learnable is not None and cfg.append_learnable_names:
        top = {r.lemma for r in ranked[:top_n]}
        appended = [r for r in rank_rows(rows, opts.score)
                    if r.lemma not in top and propn.learnable(r.lemma, flt.learnable)]
        counted = {r.lemma.split("#")[0].casefold() for r in rows}
        head["learnable_names"] = {
            "file": str(flt.learnable.path), "sha256": flt.learnable.sha256, "names": len(flt.learnable.names),
            "in_top_n": sum(1 for lem in top if propn.learnable(lem, flt.learnable)),
            "appended_after_top_n": len(appended),
            "not_counted": sorted(n for n in flt.learnable.names if n not in counted)}
    entries = snapshot.build_entries(ranked[:top_n] + appended, result.merged, manifest, citation)
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
    # The word checks say nothing useful about a unit headword (*werden + Partizip II*).
    units = {r.lemma for r in ranked if snapshot.unit_kind(r.stats.kinds)}
    found = {name: [f for f in flags if f.lemma not in units] for name, flags in found.items()}
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
    text += "\n".join(exclude.render(exclusions, dropped, top_n))
    text += "\n" + "\n".join(propn_text)
    if flt.flags is not None:
        text += "\n" + "\n".join(junk_report.render(manifest, flt, top_n))
        junk_report.write_flags(out_dir / f"{cfg.code}.flags.tsv", flt)
    names = [p.name for _s, p in iter_counts(counts_dir)]
    state = final_record(out_dir, ranked, result.merged.tokens,
                         mix=mix_of(manifest, counts_dir.parent / "work", names))
    if state is not None:
        text += "\n" + "\n".join(converge.render_table(state)) + "\n"
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
        "excluded_from_top_n": sum(1 for d in dropped if d.rank <= top_n),
        "proper_nouns_dropped_from_top_n": sum(1 for d in propn_dropped if d.rank <= top_n),
    }
    (out_dir / "perf.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    return summary

