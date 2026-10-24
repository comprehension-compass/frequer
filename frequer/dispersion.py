"""Dispersion measures over equal-size corpus parts (pure functions).

``counts`` is sparse: ``{part: occurrences}`` of one lemma; parts absent from it
hold zero. ``sizes`` is every part's size in tokens. Parts are hash buckets of
documents, so they are near-equal in size; both measures below use the real
sizes anyway.

* Gries' DP (2008): half the summed absolute difference between each part's
  share of the lemma and its share of the corpus; 0 = even, ``1 - min(s)`` = all
  in one part. ``dp_norm`` divides by that maximum so it spans [0, 1].
* Juilland's D (1970): ``1 - V / sqrt(n - 1)`` with ``V`` the coefficient of
  variation of the per-part *rates* (size-normalised); 1 = even, 0 = all in one part.

Juilland's D is biased low for rare lemmas even when they are scattered at
random: ``n`` parts and ``f`` tokens placed uniformly give an expected
``E[D] = 1 - 1/sqrt(f)`` (derivation in the docstring of
:func:`expected_juilland_d`). ``juilland_d_corrected`` divides by that so a
lemma is judged against chance, not against an unreachable ideal.
"""

from __future__ import annotations

import math
from collections.abc import Mapping, Sequence


def gries_dp(counts: Mapping[int, int], sizes: Sequence[int]) -> tuple[float, float]:
    """``(DP, DP_norm)``; ``(nan, nan)`` for a lemma that never occurs."""
    total = sum(counts.values())
    corpus = sum(sizes)
    if total <= 0 or corpus <= 0:
        return math.nan, math.nan
    # Parts the lemma misses contribute |0 - s_i| = s_i; fold them in via the complement.
    present_share = sum(sizes[i] for i in counts) / corpus
    diff = sum(abs(n / total - sizes[i] / corpus) for i, n in counts.items())
    dp = 0.5 * (diff + (1.0 - present_share))
    smallest = min(s for s in sizes if s > 0) / corpus
    ceiling = 1.0 - smallest
    return dp, (dp / ceiling if ceiling > 0 else 0.0)


def juilland_d(counts: Mapping[int, int], sizes: Sequence[int]) -> float:
    """Juilland's D over size-normalised rates; nan for a lemma that never occurs."""
    n = len(sizes)
    if n < 2 or not counts:
        return math.nan
    rates = [c / sizes[i] for i, c in counts.items() if sizes[i] > 0]
    if not rates:
        return math.nan
    mean = sum(rates) / n
    mean_sq = sum(r * r for r in rates) / n
    variance = max(mean_sq - mean * mean, 0.0)
    cv = math.sqrt(variance) / mean
    return 1.0 - cv / math.sqrt(n - 1)


def expected_juilland_d(frequency: int) -> float:
    """Juilland's D expected when ``frequency`` tokens fall uniformly over equal parts.

    With counts ~ Multinomial(f, 1/n): ``E[sum c_i^2] = f + f(f-1)/n``, so
    ``V^2 = n * sum(c^2) / f^2 - 1`` has expectation ``(n - 1) / f`` and
    ``D = 1 - V / sqrt(n - 1)`` has expectation ``1 - 1/sqrt(f)`` (to first order).
    """
    return 1.0 - 1.0 / math.sqrt(frequency) if frequency > 0 else math.nan


def juilland_d_corrected(d: float, frequency: int) -> float:
    """D divided by its chance level, capped at 1; nan where undefined (f < 2)."""
    if frequency < 2 or math.isnan(d):
        return math.nan
    return min(1.0, max(d, 0.0) / expected_juilland_d(frequency))
