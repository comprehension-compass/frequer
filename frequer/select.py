"""``frequer select``: the most frequent forms the lemmatiser's labels lack.

Reads a ``forms-<lang>.tsv`` (see :mod:`frequer.forms_run`) and writes ``candidates-<lang>.tsv``
(``rank, form, count, docs, sites, score``). A form is dropped when it is

* **already listed**: a key of the release's ``lookup.json`` or the first column of the curated
  TSV; with ``case_fold``, also a capitalised form whose lower-case form (all lower case, or the
  first letter lowered) is listed;
* **ignored by default by rule**: the classes Honeyeater's ``lexicon.lemma_defaults`` ignores
  without a human (not language, number, foreign script, acronym), using its own helpers, plus
  URLs and e-mail addresses;
* too narrow: fewer than ``min_docs`` documents or ``MIN_SITES`` sites.

The rest are ranked by a **dispersion-weighted frequency**, ``count * docs / (docs + 20)``: a
form's count, discounted when it comes from few documents. ``DAMPING`` (20) is the number of
documents at which half the count is kept, so a form repeated inside a handful of pages ranks
below a rarer one spread over hundreds.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from collections.abc import Callable, Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer.forms import read_forms_tsv

MIN_SITES = 3
DAMPING = 20.0

URL_OR_EMAIL = re.compile(
    r"(?i)(?:^[a-z][a-z0-9+.\-]*://|^www\.|\S@\S|\S\.(?:com|org|net|edu|gov|info|biz|io|de|es|jp|co|eu|ru|uk|fr)(?:/|$))"
)


def score(count: int, docs: int) -> float:
    """Dispersion-weighted frequency: ``count * docs / (docs + DAMPING)``."""
    return count * docs / (docs + DAMPING)


@dataclass(frozen=True)
class IgnoreRules:
    """Honeyeater's default-ignore helpers, injected so the selection is testable without Django."""

    script: str
    is_language: Callable[[str], bool]
    number: Callable[[str], bool | None]
    has_script_letter: Callable[[str, str], bool]
    is_acronym: Callable[[str], bool]


def honeyeater_rules(script: str) -> IgnoreRules:
    """The real helpers from ``lexicon.lemma_defaults`` (needs ``honeyeater/backend`` on the path)."""
    from frequer.runtime import setup_django

    setup_django()
    from lexicon import lemma_defaults as ld

    return IgnoreRules(script, ld._is_language, ld._number_is_learnable, ld.has_script_letter, ld.is_acronym)


def ignore_reason(form: str, rules: IgnoreRules) -> str | None:
    """Why ``form`` starts ignored by rule, or None. The order mirrors ``lemma_defaults.classify``."""
    if URL_OR_EMAIL.search(form):
        return "url_email"
    number = rules.number(form)
    if not rules.is_language(form) and number is None:
        return "non_language"
    if number is not None:
        return "number"
    if not rules.has_script_letter(form, rules.script):
        return "foreign_script"
    if rules.is_acronym(form):
        return "acronym"
    return None


def load_listed(lookup: Path, curated: Path | None) -> set[str]:
    """Lookup keys plus the curated TSV's first column (``#`` lines are comments)."""
    listed: set[str] = set(json.loads(lookup.read_text(encoding="utf-8")))
    if curated is not None:
        for raw in curated.read_text(encoding="utf-8").splitlines():
            if raw.strip() and not raw.startswith("#"):
                listed.add(raw.split("\t", 1)[0])
    return listed


def lowered_variants(form: str) -> set[str]:
    """All lower case, and the first letter lowered; neither includes ``form`` itself."""
    return {form.lower(), form[:1].lower() + form[1:]} - {form}


def is_listed(form: str, listed: set[str], case_fold: bool) -> str | None:
    """``"listed"``, ``"case_variant"`` or None."""
    if form in listed:
        return "listed"
    if case_fold and not listed.isdisjoint(lowered_variants(form)):
        return "case_variant"
    return None


@dataclass(frozen=True)
class Candidate:
    form: str
    count: int
    docs: int
    sites: int
    score: float


def select_candidates(
    rows: Iterable[tuple[str, int, int, int]], listed: set[str], rules: IgnoreRules, *,
    case_fold: bool, min_docs: int, min_sites: int = MIN_SITES,
) -> tuple[list[Candidate], dict[str, Any]]:
    """Every eligible candidate (best first) and the token mass each exclusion took."""
    mass: Counter[str] = Counter()
    pool: list[Candidate] = []
    for form, count, docs, sites in rows:
        mass["all"] += count
        status = is_listed(form, listed, case_fold)
        if status:
            mass[status] += count
            continue
        reason = ignore_reason(form, rules)
        if reason:
            mass["ignored_" + reason] += count
            continue
        mass["eligible_pool"] += count
        if docs >= min_docs and sites >= min_sites:
            pool.append(Candidate(form, count, docs, sites, score(count, docs)))
    pool.sort(key=lambda c: (-c.score, -c.count, c.form))
    return pool, dict(mass)


def coverage(pool: list[Candidate], mass: dict[str, int], top: int) -> dict[str, float]:
    """Share of the missing-form token mass the first ``top`` candidates account for.

    ``of_unlisted``: all word tokens of forms absent from the lists (before case folding or the
    ignore rules; the plan's 'missing mass'). ``of_eligible``: after both exclusions.
    """
    covered = sum(c.count for c in pool[:top])
    ignored = sum(v for k, v in mass.items() if k.startswith("ignored_"))
    unlisted = mass.get("eligible_pool", 0) + ignored + mass.get("case_variant", 0)
    eligible = mass.get("eligible_pool", 0)
    return {
        "of_unlisted_incl_case_variants": covered / unlisted if unlisted else 0.0,
        "of_unlisted_excl_case_variants": covered / (unlisted - mass.get("case_variant", 0))
        if unlisted > mass.get("case_variant", 0) else 0.0,
        "of_eligible": covered / eligible if eligible else 0.0,
    }


def write_candidates(path: Path, pool: list[Candidate], top: int) -> None:
    with path.open("w", encoding="utf-8") as fp:
        for rank, c in enumerate(pool[:top], 1):
            fp.write(f"{rank}\t{c.form}\t{c.count}\t{c.docs}\t{c.sites}\t{c.score:.1f}\n")


def run_select(
    lang: str, *, forms: Path, lookup: Path, curated: Path | None, case_fold: bool, top: int,
    min_docs: int, script: str, out_dir: Path, rules: IgnoreRules | None = None,
) -> dict[str, Any]:
    header, rows = read_forms_tsv(forms)
    listed = load_listed(lookup, curated)
    pool, mass = select_candidates(rows, listed, rules or honeyeater_rules(script),
                                   case_fold=case_fold, min_docs=min_docs)
    write_candidates(out_dir / f"candidates-{lang}.tsv", pool, top)
    stats = {
        "language": lang, "forms_file": forms.name, "forms_tokens": header.get("tokens"),
        "listed_forms": len(listed), "case_fold": case_fold, "min_docs": min_docs, "min_sites": MIN_SITES,
        "top": top, "eligible_candidates": len(pool), "mass": mass,
        "mass_share": {k: round(v / mass["all"], 4) for k, v in mass.items()},
        "coverage": {str(k): coverage(pool, mass, k) for k in (100, 500, top, 2000, 5000) if k <= len(pool)},
    }
    (out_dir / f"candidates-{lang}.json").write_text(json.dumps(stats, indent=1), encoding="utf-8")
    return stats
