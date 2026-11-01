"""The snapshot's filters, in order: the reviewed exclusion list, then the language's proper-noun rule.

One place, used by ``build`` (the snapshot) and by the convergence checkpoints, so convergence is judged on
the list the snapshot will hold (developer direction, 2026-11-01).
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

from frequer import exclude, propn, snapshot
from frequer.config import Manifest
from frequer.ranking import Row


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


def apply(manifest: Manifest, ranked: list[Row], root: Path | None = None) -> Filtered:
    """``ranked`` with the exclusion list and the proper-noun rule applied (ranks reported are the input's)."""
    cfg = manifest.language
    rank_of = {r.lemma: i for i, r in enumerate(ranked, start=1)}
    out = Filtered(ranked)
    out.exclusions = exclude.load(cfg.code)
    out.ranked, out.excluded = exclude.apply(ranked, lambda r: r.lemma, out.exclusions)
    if cfg.propn_rule == "capitalised_mid_sentence":
        out.learnable = propn.load_names(root or honeyeater_root(), cfg.code)
        out.tally = propn.load_case(cfg.code)
        out.ranked, out.propn_dropped, out.names_kept, out.case_kept = propn.apply(
            out.ranked, lambda r: r.lemma, lambda r: snapshot.majority(r.stats.pos, "X"), lambda r: r.stats.forms,
            out.learnable, out.tally, cfg.propn_capitalised_min, rank_of)
    return out
