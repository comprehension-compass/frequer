"""The reviewed exclusion list: lemmas dropped from the ranking at snapshot build.

``corpora/exclude/<lang>.tsv`` holds tab-separated ``lemma, class, reason`` rows (``#`` lines are
comments). A row whose class starts with ``exclude`` drops that snapshot key from the ranking, and
every lower rank moves up. A unit headword (it has a space) also drops when every one of its member
words is excluded, unless the file lists the headword itself with a ``keep`` class. The counts are
untouched, so the list can change and the snapshot be rebuilt without recounting. The file's sha256
goes into the snapshot header and the report.
"""

from __future__ import annotations

import hashlib
from collections import Counter
from collections.abc import Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer.config import MANIFEST_DIR


@dataclass(frozen=True)
class Exclusions:
    path: Path
    sha256: str
    #: snapshot key -> (class, reason) for the excluded keys.
    excluded: dict[str, tuple[str, str]]
    #: keys the file lists with a ``keep`` class (they override the unit rule).
    kept: frozenset[str] = field(default_factory=frozenset)


@dataclass(frozen=True)
class Dropped:
    rank: int
    lemma: str
    cls: str
    reason: str


def exclusion_path(lang: str, root: Path = MANIFEST_DIR) -> Path:
    return root / "exclude" / f"{lang}.tsv"


def load(lang: str, root: Path = MANIFEST_DIR) -> Exclusions | None:
    path = exclusion_path(lang, root)
    if not path.exists():
        return None
    raw = path.read_bytes()
    excluded: dict[str, tuple[str, str]] = {}
    kept: set[str] = set()
    for n, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            raise SystemExit(f"{path}:{n}: expected lemma<TAB>class<TAB>reason")
        lemma, cls = parts[0], parts[1].strip()
        reason = parts[2].strip() if len(parts) > 2 else ""
        if cls.startswith("exclude"):
            excluded[lemma] = (cls, reason)
        elif cls.startswith("keep"):
            kept.add(lemma)
        else:
            raise SystemExit(f"{path}:{n}: class {cls!r} is neither exclude-* nor keep-*")
    return Exclusions(path, hashlib.sha256(raw).hexdigest(), excluded, frozenset(kept))


def _members(headword: str) -> list[str]:
    return [w for w in headword.split() if any(c.isalpha() for c in w)]


def reason_for(lemma: str, ex: Exclusions) -> tuple[str, str] | None:
    """Why ``lemma`` is excluded, or None."""
    if lemma in ex.excluded:
        return ex.excluded[lemma]
    if " " in lemma and lemma not in ex.kept:
        bases = {k.split("#")[0].lower() for k in ex.excluded}
        members = _members(lemma)
        if members and all(m.lower() in bases for m in members):
            return "exclude-unit", "every member word is excluded"
    return None


def apply[T](ranked: Sequence[T], lemma_of: Any, ex: Exclusions | None) -> tuple[list[T], list[Dropped]]:
    """``ranked`` without the excluded lemmas, and what was dropped (with its rank before exclusion)."""
    if ex is None:
        return list(ranked), []
    kept: list[T] = []
    dropped: list[Dropped] = []
    for rank, row in enumerate(ranked, start=1):
        lemma = lemma_of(row)
        why = reason_for(lemma, ex)
        if why is None:
            kept.append(row)
        else:
            dropped.append(Dropped(rank, lemma, why[0], why[1]))
    return kept, dropped


def header_entry(ex: Exclusions | None, dropped: Sequence[Dropped], top_n: int, root: Path) -> dict[str, Any] | None:
    if ex is None:
        return None
    try:
        rel = str(ex.path.relative_to(root))
    except ValueError:
        rel = str(ex.path)
    return {
        "file": rel, "sha256": ex.sha256, "listed": len(ex.excluded),
        "dropped_from_top_n": sum(1 for d in dropped if d.rank <= top_n),
        "by_class": dict(Counter(d.cls for d in dropped if d.rank <= top_n)),
        "rule": "excluded keys and unit headwords made only of excluded words are dropped; lower ranks move up",
    }


def render(ex: Exclusions | None, dropped: Sequence[Dropped], top_n: int) -> list[str]:
    if ex is None:
        return []
    inside = [d for d in dropped if d.rank <= top_n]
    by = Counter(d.cls for d in inside)
    out = ["## Excluded lemmas", "",
           f"`{ex.path.name}` (sha256 `{ex.sha256[:16]}`) lists {len(ex.excluded):,} exclusions; "
           f"{len(inside):,} lemmas were dropped from the top {top_n:,} before cutting it "
           "(" + ", ".join(f"{k} {v:,}" for k, v in sorted(by.items())) + "). Lower ranks moved up.", "",
           "| rank before | lemma | class | reason |", "|---|---|---|---|"]
    out += [f"| {d.rank} | `{d.lemma}` | {d.cls} | {d.reason} |" for d in inside[:60]]
    if len(inside) > 60:
        out.append(f"\n_{len(inside) - 60:,} more in the exclusion file._")
    return [*out, ""]
