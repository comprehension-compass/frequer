"""From merged counts to the snapshot's ranking: merges, rank, the exclusion list, the proper-noun rule, the
junk-filter heuristics.

One place, used by ``build`` (the snapshot) and by the convergence checkpoints, so convergence is judged on
the list the snapshot will hold (developer direction, 2026-11-01). Ranks reported are those of the
ranking after the merges and before any filter.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path

from frequer import compare, exclude, junk, propn, propn_usage, snapshot
from frequer.config import Manifest
from frequer.counts import Merged
from frequer.ranking import Row, build_rows, rank_rows


def honeyeater_root() -> Path:
    """The pinned Honeyeater checkout (as ``runtime.Runtime`` finds it)."""
    if "HONEYEATER_ROOT" in os.environ:
        return Path(os.environ["HONEYEATER_ROOT"])
    import nlp

    return Path(nlp.__file__).resolve().parents[2]


@dataclass
class Filtered:
    ranked: list[Row]
    exclusions: exclude.Exclusions | None = None
    excluded: list[exclude.Dropped] = field(default_factory=list)
    learnable: propn.LearnableNames | None = None
    tally: propn.CaseTally | None = None
    propn_dropped: list[propn.Dropped] = field(default_factory=list)
    names_kept: list[tuple[int, str]] = field(default_factory=list)
    case_kept: list[propn.Dropped] = field(default_factory=list)
    review: junk.Review | None = None
    merges: list[junk.Merge] = field(default_factory=list)
    flags: junk.Flags | None = None
    routed: list[junk.Routed] = field(default_factory=list)


def apply(manifest: Manifest, merged: Merged, weights: Mapping[str, float], score: str = "frequency",
          root: Path | None = None, cooc: Path | None = None) -> Filtered:
    """Merge, rank and filter ``merged`` (merges change ``merged`` in place, so the snapshot reflects them)."""
    cfg = manifest.language
    jc = cfg.junk
    out = Filtered([])
    out.review = junk.load_review(cfg.code)
    def fold(target: str) -> str:  # keys are case-folded, so review targets are too
        return target.lower() if cfg.fold_case else target

    merges = [junk.Merge(s, fold(t), merged.lemmas[s].freq, "review: merge")
              for s, t in (out.review.merges() if out.review else {}).items() if s in merged.lemmas]
    if jc.accent_ratio:
        taken = {m.source for m in merges}
        vetoed = {k for k, (d, _r) in out.review.decisions.items() if d == "keep"} if out.review else set()
        merges += [m for m in junk.accent_merges(merged.lemmas, jc.accent_ratio, jc.fold_maps)
                   if m.source not in taken and m.source not in vetoed]
    out.merges = junk.apply_merges(merged, merges)

    ranked = rank_rows(build_rows(merged, weights), score)
    rank_of = {r.lemma: i for i, r in enumerate(ranked, start=1)}
    out.exclusions = exclude.load(cfg.code)
    ranked, out.excluded = exclude.apply(ranked, lambda r: r.lemma, out.exclusions)

    needs_case = cfg.propn_rule == "capitalised_mid_sentence" or "propn_band" in jc.rules
    if needs_case:
        out.learnable = propn.load_names(root or honeyeater_root(), cfg.code)
        out.tally = propn.load_case(cfg.code)
    if cfg.propn_rule == "capitalised_mid_sentence" and out.learnable and out.tally:
        ranked, out.propn_dropped, out.names_kept, out.case_kept = propn.apply(
            ranked, lambda r: r.lemma, lambda r: snapshot.majority(r.stats.pos, "X"), lambda r: r.stats.forms,
            out.learnable, out.tally, cfg.propn_capitalised_min, rank_of)

    if jc.rules:
        learnable, tally = out.learnable, out.tally

        def share(c: junk.Candidate) -> tuple[float | None, bool]:
            assert learnable is not None and tally is not None
            if propn.learnable(c.lemma, learnable):
                return None, True
            if junk.acronym_share(c.forms) >= 0.5:
                return None, False  # an all-capitals acronym: no case evidence either way
            return propn.mid_capitalised_share(c.forms, tally), False

        candidates = [junk.Candidate(r.lemma, r.stats.freq, snapshot.majority(r.stats.pos, "X"), r.stats.forms,
                                     r.stats.df) for r in ranked]
        usage_of: dict[str, float] | None = None
        if "propn_usage" in jc.rules and cooc is not None and cooc.exists():
            usage_of = propn_usage.load(cooc, jc.propn_usage_determiners,
                                        {junk.base_of(c.lemma).lower() for c in candidates if c.pos == "PROPN"})

        def usage(c: junk.Candidate) -> float | None:
            assert usage_of is not None
            return usage_of.get(junk.base_of(c.lemma).lower())

        out.flags = junk.compute_flags(
            candidates, jc, total_docs=merged.docs, zipf=compare.zipf_lookup(), lang=cfg.code,
            kept=out.exclusions.kept if out.exclusions else frozenset(),
            propn_share=share if needs_case else None, propn_usage=usage if usage_of is not None else None)
        out.routed = junk.route([r.lemma for r in ranked], out.flags, out.review, jc.review_top, jc.review_multi_flag)
        keep = {r.lemma for r in out.routed if r.action in ("keep", "review-keep", "pending", "pending-names")}
        ranked = [r for r in ranked if r.lemma in keep]
    out.ranked = ranked
    return out
