"""The standing proper-noun rule: drop proper nouns a learner does not learn from the snapshot.

Developer direction (2026-11-01): "We should be routinely removing proper nouns that don't meet the
specific requirements we set for non-default-ignore (countries, well known cities)." A snapshot lemma
whose majority tag is ``PROPN`` drops, unless its case-folded text (the homograph key removed) is in
Honeyeater's ``reference/learnable-names/<code>.json``. That file holds CLDR territory names, ISO 639-1
language names and time-zone exemplar cities, the same list the app's default writer uses
(``backend/lexicon/learnable_names.py``). It is read from the pinned Honeyeater checkout, and its
sha256 goes into the snapshot header. The rule matches the app, which default-ignores the same lemmas.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROPN = "PROPN"


@dataclass(frozen=True)
class LearnableNames:
    path: Path
    sha256: str
    names: frozenset[str]


def load(honeyeater_root: Path, lang: str) -> LearnableNames:
    path = honeyeater_root / "reference" / "learnable-names" / f"{lang}.json"
    if not path.exists():
        raise SystemExit(f"{path}: no learnable-names file; the proper-noun rule needs one")
    raw = path.read_bytes()
    names = frozenset(str(n).casefold() for n in json.loads(raw)["names"])
    return LearnableNames(path, hashlib.sha256(raw).hexdigest(), names)


def learnable(lemma: str, names: LearnableNames) -> bool:
    return lemma.split("#")[0].casefold() in names.names


def apply[T](
    ranked: Sequence[T], lemma_of: Callable[[T], str], pos_of: Callable[[T], str],
    names: LearnableNames, rank_of: Mapping[str, int],
) -> tuple[list[T], list[tuple[int, str]], list[tuple[int, str]]]:
    """``ranked`` without unlearnable proper nouns; the dropped and the kept learnable names, with their ranks."""
    kept: list[T] = []
    dropped: list[tuple[int, str]] = []
    names_kept: list[tuple[int, str]] = []
    for row in ranked:
        lemma = lemma_of(row)
        if pos_of(row) != PROPN:
            kept.append(row)
        elif learnable(lemma, names):
            kept.append(row)
            names_kept.append((rank_of[lemma], lemma))
        else:
            dropped.append((rank_of[lemma], lemma))
    return kept, dropped, names_kept


def header_entry(names: LearnableNames, dropped: Sequence[tuple[int, str]],
                 names_kept: Sequence[tuple[int, str]], top_n: int, root: Path) -> dict[str, Any]:
    try:
        rel = str(names.path.relative_to(root))
    except ValueError:
        rel = str(names.path)
    return {
        "learnable_names": rel, "sha256": names.sha256,
        "dropped_from_top_n": sum(1 for r, _ in dropped if r <= top_n),
        "learnable_names_kept": sum(1 for r, _ in names_kept if r <= top_n),
        "rule": "a lemma whose majority tag is PROPN is dropped unless its case-folded text is a learnable name",
    }


def render(names: LearnableNames, dropped: Sequence[tuple[int, str]],
           names_kept: Sequence[tuple[int, str]], top_n: int) -> list[str]:
    inside = [d for d in dropped if d[0] <= top_n]
    kept = [k for k in names_kept if k[0] <= top_n]
    return [
        "## Proper nouns", "",
        f"A lemma whose majority tag is PROPN is dropped unless it is a learnable name "
        f"(`reference/learnable-names/{names.path.stem}.json`, sha256 `{names.sha256[:16]}`: CLDR territories, "
        f"languages, exemplar cities). {len(inside):,} proper nouns were dropped from the top {top_n:,}, "
        f"and {len(kept):,} learnable names were kept.", "",
        "Kept (first 40): " + ", ".join(f"`{lemma}` ({r})" for r, lemma in kept[:40]), "",
        "Dropped (first 40): " + ", ".join(f"`{lemma}` ({r})" for r, lemma in inside[:40]), "",
    ]
