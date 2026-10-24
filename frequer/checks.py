"""The review checks ported from the 2025 post-processor, over the new counts.

Each check returns plain rows for the markdown report. Checks that ask "what
would the pipeline do with this word alone" go through ``lemma_of_word``, a
callable supplied by the caller (the runtime in a build, a stub in tests), so
this module never lemmatises on its own. Per-language parameters (plural
suffixes, thresholds) come from the manifest.
"""

from __future__ import annotations

import statistics
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from frequer.config import ChecksConfig
from frequer.ranking import Row

LemmaOf = Callable[[str], str | None]


@dataclass
class Flag:
    rank: int
    lemma: str
    frequency: int
    detail: str


def form_ratio_outliers(ranked: Sequence[Row], threshold: float) -> list[Flag]:
    """Forms far more frequent than the lemma's median form: a hint of a mis-filed form."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        forms = row.stats.forms
        if len(forms) < 2:
            continue
        median = statistics.median(forms.values())
        if median <= 0:
            continue
        top = [(f, n) for f, n in forms.most_common() if n / median > threshold]
        if top:
            shown = ", ".join(f"`{f}` {n:,} ({n / median:.0f}x)" for f, n in top[:4])
            flags.append(Flag(rank, row.lemma, row.stats.freq, f"median form {median:g}; {shown}"))
    return flags


def plural_mismatches(
    ranked: Sequence[Row], suffixes: Sequence[str], lemma_of_word: LemmaOf, known: Mapping[str, int]
) -> list[Flag]:
    """Lemmas that look like a plural whose stripped form lemmatises to a different, listed lemma."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        lemma = row.lemma
        if len(lemma) < 3:
            continue
        for suffix in suffixes:
            if not lemma.endswith(suffix) or len(lemma) - len(suffix) < 2:
                continue
            stem = lemma[: -len(suffix)]
            target = lemma_of_word(stem)
            if target and target != lemma and target in known:
                flags.append(Flag(rank, lemma, row.stats.freq,
                                  f"`{stem}` lemmatises to `{target}` (rank {known[target]:,})"))
    return flags


def lemma_inconsistencies(ranked: Sequence[Row], lemma_of_word: LemmaOf, known: Mapping[str, int]) -> list[Flag]:
    """Lemmas that, met alone, lemmatise to some other listed lemma."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        if len(row.lemma) < 2:
            continue
        target = lemma_of_word(row.lemma)
        if target and target != row.lemma and target in known:
            flags.append(Flag(rank, row.lemma, row.stats.freq,
                              f"alone, `{row.lemma}` lemmatises to `{target}` (rank {known[target]:,})"))
    return flags


def short_lemmas(ranked: Sequence[Row], max_len: int, lemma_of_word: LemmaOf) -> list[Flag]:
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        if len(row.lemma) > max_len:
            continue
        shown = ", ".join(f"`{f}` -> `{lemma_of_word(f) or '?'}`" for f in list(row.stats.forms)[:5])
        flags.append(Flag(rank, row.lemma, row.stats.freq, shown or "no forms"))
    return flags


def case_merges(ranked: Sequence[Row], known: Mapping[str, int], freqs: Mapping[str, int]) -> list[Flag]:
    """Non-lowercase lemmas worth a look: a listed lowercase twin (a merge candidate), or a
    capitalised lemma that is not mostly a noun/proper noun (so not German's POS-cased nouns)."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        lower = row.lemma.lower()
        if lower == row.lemma:
            continue
        twin = known.get(lower)
        nouns = sum(row.stats.pos.get(p, 0) for p in ("NOUN", "PROPN"))
        voted = sum(row.stats.pos.values())
        if twin:
            flags.append(Flag(rank, row.lemma, row.stats.freq,
                              f"lowercase `{lower}` is rank {twin:,} ({freqs[lower]:,}): merge candidate"))
        elif voted and nouns / voted < 0.5:
            top = max(row.stats.pos, key=lambda p: row.stats.pos[p])
            flags.append(Flag(rank, row.lemma, row.stats.freq, f"capitalised but mostly {top}; no lowercase twin"))
    return flags


def proper_noun_candidates(
    ranked: Sequence[Row], *, propn_share: float = 0.5, capital_share: float = 0.9
) -> list[Flag]:
    """Lemmas voted PROPN, or almost always met capitalised (where forms keep their case)."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        stats = row.stats
        pos_total = sum(stats.pos.values())
        form_total = sum(stats.forms.values())
        propn = stats.pos.get("PROPN", 0) / pos_total if pos_total else 0.0
        capital = sum(n for f, n in stats.forms.items() if f[:1].isupper()) / form_total if form_total else 0.0
        if propn >= propn_share or capital >= capital_share:
            flags.append(Flag(rank, row.lemma, stats.freq, f"PROPN {propn:.0%}, capitalised forms {capital:.0%}"))
    return flags


def foreign_candidates(
    ranked: Sequence[Row], lang: str, classify: Callable[[str], tuple[str, float]],
    zipf: Callable[[str, str], float] | None,
) -> list[Flag]:
    """Lemmas that look like another language's word: English-leaning wordfreq, or langid disagrees."""
    flags: list[Flag] = []
    for rank, row in enumerate(ranked, start=1):
        signals: list[str] = []
        if zipf is not None:
            en, own = zipf(row.lemma, "en"), zipf(row.lemma, lang)
            if en >= 2.5 and en > own + 1.0:
                signals.append(f"wordfreq zipf en {en:.1f} vs {lang} {own:.1f}")
        guess, prob = classify(row.lemma)
        if guess != lang and prob >= 0.95:
            signals.append(f"langid {guess} {prob:.2f}")
        if signals:
            flags.append(Flag(rank, row.lemma, row.stats.freq, "; ".join(signals)))
    return flags


def run_checks(
    ranked: Sequence[Row], cfg: ChecksConfig, lemma_of_word: LemmaOf,
) -> dict[str, list[Flag]]:
    """The four lemmatisation checks plus case merges, over the review window."""
    window = list(ranked[: cfg.review_top_n])
    known = {row.lemma: i for i, row in enumerate(ranked, start=1)}
    freqs = {row.lemma: row.stats.freq for row in ranked}
    out: dict[str, Any] = {
        "form_ratio": form_ratio_outliers(window, cfg.form_ratio_threshold),
        "plural": plural_mismatches(window, cfg.plural_suffixes, lemma_of_word, known)
        if cfg.plural_suffixes else [],
        "consistency": lemma_inconsistencies(window, lemma_of_word, known),
        "short": short_lemmas(window, cfg.short_lemma_max_len, lemma_of_word),
        "case": case_merges(window, known, freqs),
    }
    return out
