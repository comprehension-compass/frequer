"""Rank lemmas by a configurable score.

The default is raw frequency, so a snapshot is comparable with the ones already
live. The alternatives trade frequency against how widely a lemma is spread, so
that a name from one news story or a term from one manual does not outrank a
word that is everywhere. Every score is computed for every candidate so the
review report can show how each would reorder the list.
"""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass, field

from frequer.counts import LemmaStats, Merged
from frequer.dispersion import gries_dp, juilland_d, juilland_d_corrected

SCORES = (
    "frequency",
    "document_frequency",
    "juilland_u",
    "juilland_u_corrected",
    "dp_adjusted",
    "cd_blend",
)


@dataclass
class Row:
    lemma: str
    stats: LemmaStats
    #: Source-weighted frequency (equals ``stats.freq`` when every weight is 1).
    weighted: float
    dp: float
    dp_norm: float
    juilland_d: float
    juilland_d_corrected: float
    scores: dict[str, float] = field(default_factory=dict)


def _finite(x: float, default: float = 0.0) -> float:
    return default if math.isnan(x) else x


def score_row(name: str, row: Row) -> float:
    """The named score of one row; larger ranks higher."""
    f = row.weighted
    if name == "frequency":
        return f
    if name == "document_frequency":
        return float(row.stats.df)
    if name == "juilland_u":  # Juilland's usage coefficient: f * D
        return f * max(_finite(row.juilland_d), 0.0)
    if name == "juilland_u_corrected":  # f * D judged against chance
        return f * _finite(row.juilland_d_corrected)
    if name == "dp_adjusted":  # f * (1 - DP_norm)
        return f * (1.0 - _finite(row.dp_norm, 1.0))
    if name == "cd_blend":  # geometric mean of frequency and document frequency
        return math.sqrt(f * row.stats.df)
    raise KeyError(f"unknown ranking score {name!r}; choose from {SCORES}")


def build_rows(merged: Merged, weights: Mapping[str, float]) -> list[Row]:
    """A :class:`Row` per merged lemma with dispersion and every score filled in."""
    rows: list[Row] = []
    for lemma, stats in merged.lemmas.items():
        dp, dp_norm = gries_dp(stats.parts, merged.part_tokens)
        d = juilland_d(stats.parts, merged.part_tokens)
        weighted = sum(n * weights.get(src, 1.0) for src, n in stats.by_source.items())
        row = Row(lemma, stats, weighted, dp, dp_norm, d, juilland_d_corrected(d, stats.freq))
        row.scores = {name: score_row(name, row) for name in SCORES}
        rows.append(row)
    return rows


def rank_rows(rows: list[Row], score: str) -> list[Row]:
    """Rows by descending ``score``; ties broken by raw frequency, then lemma, so output is stable."""
    return sorted(rows, key=lambda r: (-r.scores[score], -r.stats.freq, r.lemma))
