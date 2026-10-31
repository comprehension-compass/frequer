"""Comparisons the review report makes: against the live snapshot, wordfreq, and alternative scores."""

from __future__ import annotations

import json
import math
from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

from frequer.ranking import SCORES, Row, rank_rows


def spearman(xs: Sequence[float], ys: Sequence[float]) -> float:
    """Spearman rank correlation (average ranks for ties); nan under two points."""
    n = len(xs)
    if n < 2:
        return math.nan

    def ranks(vals: Sequence[float]) -> list[float]:
        order = sorted(range(n), key=lambda i: vals[i])
        out = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            for k in range(i, j + 1):
                out[order[k]] = (i + j) / 2 + 1
            i = j + 1
        return out

    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry, strict=True))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else math.nan


@dataclass
class Mover:
    lemma: str
    old_rank: int
    new_rank: int


@dataclass
class LiveShift:
    live_size: int
    new_size: int
    shared: int
    overlap: dict[int, float]
    spearman: float
    median_log_ratio: float
    up: list[Mover]
    down: list[Mover]
    new_in_top: list[Mover]
    lost_from_top: list[Mover]


def load_live_ranks(path: Path) -> dict[str, int]:
    """Lemma -> 1-based rank, from the live snapshot's entry order."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return {lemma: i for i, lemma in enumerate(data["lemmas"], start=1)}


def live_shift(
    live: Mapping[str, int], new_order: Sequence[str], *, window: int = 5000, movers: int = 15
) -> LiveShift:
    new = {lemma: i for i, lemma in enumerate(new_order, start=1)}
    shared = [lemma for lemma in new if lemma in live]
    overlap = {
        k: len(set(new_order[:k]) & {lm for lm, r in live.items() if r <= k}) / k
        for k in (1000, 5000, 20000) if k <= len(live)
    }
    rho = spearman([live[lm] for lm in shared], [new[lm] for lm in shared])
    ratios = sorted(abs(math.log(new[lm] / live[lm])) for lm in shared)
    median = ratios[len(ratios) // 2] if ratios else math.nan
    pool = [Mover(lm, live[lm], new[lm]) for lm in shared if min(live[lm], new[lm]) <= window]
    pool.sort(key=lambda m: m.new_rank - m.old_rank)
    up, down = pool[:movers], pool[::-1][:movers]
    entered = [Mover(lm, live.get(lm, 0), r) for lm, r in new.items() if r <= window and live.get(lm, 10**9) > window]
    left = [Mover(lm, r, new.get(lm, 0)) for lm, r in live.items() if r <= window and new.get(lm, 10**9) > window]
    return LiveShift(len(live), len(new), len(shared), overlap, rho, math.exp(median) if ratios else math.nan,
                     up, down, entered[:movers], sorted(left, key=lambda m: m.old_rank)[:movers])


@dataclass
class AltRanking:
    score: str
    overlap_with_default: float
    spearman: float
    risers: list[tuple[Row, int, int]]
    fallers: list[tuple[Row, int, int]]


def alternative_rankings(
    rows: Sequence[Row], default: str, *, window: int = 5000, show: int = 5
) -> list[AltRanking]:
    """How each other score reorders the default's top ``window``."""
    base = rank_rows(list(rows), default)
    base_rank = {r.lemma: i for i, r in enumerate(base, start=1)}
    out: list[AltRanking] = []
    for score in SCORES:
        if score == default:
            continue
        alt = rank_rows(list(rows), score)
        alt_rank = {r.lemma: i for i, r in enumerate(alt, start=1)}
        top_base = {r.lemma for r in base[:window]}
        top_alt = {r.lemma for r in alt[:window]}
        both = [lm for lm in top_base | top_alt]
        rho = spearman([base_rank[lm] for lm in both], [alt_rank[lm] for lm in both])
        by_lemma = {r.lemma: r for r in rows}
        moves = sorted(both, key=lambda lm: alt_rank[lm] - base_rank[lm])
        out.append(AltRanking(
            score, len(top_base & top_alt) / window, rho,
            [(by_lemma[lm], base_rank[lm], alt_rank[lm]) for lm in moves[:show]],
            [(by_lemma[lm], base_rank[lm], alt_rank[lm]) for lm in moves[::-1][:show]],
        ))
    return out


@dataclass
class WordfreqComparison:
    top_n: int
    overlap: int
    only_ours: list[str]
    only_wordfreq: list[str]


def wordfreq_comparison(
    ours: Sequence[str], wf_code: str, lemma_of_word: Callable[[str], str | None], top_n: int = 1000
) -> WordfreqComparison | None:
    """Our top ``top_n`` lemmas against wordfreq's, after lemmatising its forms.

    Returns None when ``wordfreq`` is not installed or has no list for the language.
    """
    try:
        from wordfreq import get_frequency_dict

        freqs = get_frequency_dict(wf_code, wordlist="best")
    except (ImportError, LookupError, ValueError):
        return None
    summed: dict[str, float] = defaultdict(float)
    for form, f in sorted(freqs.items(), key=lambda kv: -kv[1])[: top_n * 5]:
        lemma = lemma_of_word(form)
        if lemma:
            summed[lemma] += f
    theirs = [lm for lm, _ in sorted(summed.items(), key=lambda kv: -kv[1])[:top_n]]
    mine = list(ours[:top_n])
    # wordfreq's forms are lower-cased, so a German noun met alone comes back lower-case:
    # compare without case (and without a homograph key).
    def fold(lemma: str) -> str:
        at = lemma.find("#", 1)
        return (lemma if at < 0 else lemma[:at]).lower()

    folded = {fold(t) for t in theirs}
    mine_folded = {fold(m) for m in mine}
    both = {m for m in mine if fold(m) in folded} | {t for t in theirs if fold(t) in mine_folded}
    shared = sum(1 for m in mine if fold(m) in folded)
    return WordfreqComparison(top_n, shared, [m for m in mine if m not in both][:25],
                              [t for t in theirs if t not in both][:25])


def zipf_lookup() -> Callable[[str, str], float] | None:
    try:
        from wordfreq import zipf_frequency
    except ImportError:
        return None

    def zipf(word: str, lang: str) -> float:
        try:
            return float(zipf_frequency(word, lang))
        except Exception:
            return 0.0

    return zipf
