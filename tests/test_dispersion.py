"""Dispersion measures: known limits, agreement with a dense reference, chance level."""

from __future__ import annotations

import math
import random

import pytest

from frequer.dispersion import (
    expected_juilland_d,
    gries_dp,
    juilland_d,
    juilland_d_corrected,
)

SIZES = [100] * 10


def dense_dp(counts: list[int], sizes: list[int]) -> float:
    total, corpus = sum(counts), sum(sizes)
    return 0.5 * sum(abs(c / total - s / corpus) for c, s in zip(counts, sizes, strict=True))


def dense_d(counts: list[int], sizes: list[int]) -> float:
    rates = [c / s for c, s in zip(counts, sizes, strict=True)]
    mean = sum(rates) / len(rates)
    sd = math.sqrt(sum((r - mean) ** 2 for r in rates) / len(rates))
    return 1 - (sd / mean) / math.sqrt(len(rates) - 1)


def test_even_spread_is_perfect() -> None:
    counts = {i: 5 for i in range(10)}
    dp, dp_norm = gries_dp(counts, SIZES)
    assert dp == pytest.approx(0.0, abs=1e-12)
    assert dp_norm == pytest.approx(0.0, abs=1e-12)
    assert juilland_d(counts, SIZES) == pytest.approx(1.0)


def test_all_in_one_part_is_worst() -> None:
    dp, dp_norm = gries_dp({3: 40}, SIZES)
    assert dp == pytest.approx(0.9)  # 1 - min share
    assert dp_norm == pytest.approx(1.0)
    assert juilland_d({3: 40}, SIZES) == pytest.approx(0.0)


def test_unequal_sizes_match_dense_reference() -> None:
    sizes = [50, 80, 120, 100, 150, 90, 110, 60, 140, 100]
    counts = {0: 3, 2: 7, 5: 1, 9: 4}
    dense = [counts.get(i, 0) for i in range(10)]
    assert gries_dp(counts, sizes)[0] == pytest.approx(dense_dp(dense, sizes))
    assert juilland_d(counts, sizes) == pytest.approx(dense_d(dense, sizes))


def test_absent_lemma_is_undefined() -> None:
    assert math.isnan(gries_dp({}, SIZES)[0])
    assert math.isnan(juilland_d({}, SIZES))


def test_random_scatter_sits_near_chance_level() -> None:
    rng = random.Random(7)
    f, n = 60, 100
    ds = []
    for _ in range(300):
        counts: dict[int, int] = {}
        for _ in range(f):
            part = rng.randrange(n)
            counts[part] = counts.get(part, 0) + 1
        ds.append(juilland_d(counts, [1000] * n))
    assert sum(ds) / len(ds) == pytest.approx(expected_juilland_d(f), abs=0.03)
    assert juilland_d_corrected(sum(ds) / len(ds), f) == pytest.approx(1.0, abs=0.05)


def test_corrected_d_is_capped_and_undefined_for_singletons() -> None:
    assert juilland_d_corrected(0.99, 2) == 1.0
    assert math.isnan(juilland_d_corrected(0.5, 1))
