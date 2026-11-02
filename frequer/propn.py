"""The snapshot's proper-noun rule, configured per language (``language.propn_rule``).

Developer direction (2026-11-01): routinely remove proper nouns that don't meet the requirements for
non-default-ignore (countries, well-known cities). A learnable name stays always: its case-folded text
(the homograph key removed) is in Honeyeater's ``reference/learnable-names/<code>.json`` (CLDR territories,
ISO 639-1 language names, time-zone exemplar cities; the app's default-writer list,
``backend/lexicon/learnable_names.py``), read from the pinned checkout.

``capitalised_mid_sentence`` (es): a PROPN-majority lemma drops only when its occurrences are mostly
capitalised **mid-sentence**, so a common noun the tagger often calls PROPN (*kayak*, *rock*, *máster*)
stays. The counts keep every surface form with its case but not its position. A per-language **case
tally** (``corpora/case/<code>.tsv.gz``, re-read from the counted sample by ``corpora/case/tally_<code>.py``)
gives each capitalised surface form's occurrences sentence-initially, mid-sentence in running text, and
mid-sentence in a title-case line (a heading or menu where most longer words are capitalised, so its
capitals say nothing about the word). A lemma's capitalised share in running text is then

    cap / (cap + sum(c_f for lower-case forms f)),  cap = sum(c_f * running_f / (initial_f + running_f + title_f))

with ``c_f`` the counted occurrences of form ``f``. An all-capitals form (``ROCK``) carries no case evidence
and is left out of both sides. A camel-case form (``iPhone``, ``eBay``) counts as capitalised. A
capitalised form the tally never saw counts as running text. A lemma with
no mid-sentence evidence at all drops, since the tag is the only evidence.

``none`` (de, ja): no rule. German capitalises every noun and Japanese has no case, so the test cannot work
there.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer.config import MANIFEST_DIR
from frequer.counts import LemmaStats

PROPN = "PROPN"


@dataclass(frozen=True)
class LearnableNames:
    path: Path
    sha256: str
    names: frozenset[str]


@dataclass(frozen=True)
class CaseTally:
    path: Path
    sha256: str
    #: capitalised surface form -> (sentence-initial, mid-sentence running text, mid-sentence title-case line)
    positions: dict[str, tuple[int, int, int]]


@dataclass(frozen=True)
class Dropped:
    rank: int
    lemma: str
    share: float | None


def load_names(honeyeater_root: Path, lang: str) -> LearnableNames:
    path = honeyeater_root / "reference" / "learnable-names" / f"{lang}.json"
    if not path.exists():
        raise SystemExit(f"{path}: no learnable-names file; the proper-noun rule needs one")
    raw = path.read_bytes()
    names = frozenset(str(n).casefold() for n in json.loads(raw)["names"])
    return LearnableNames(path, hashlib.sha256(raw).hexdigest(), names)


def case_path(lang: str, root: Path = MANIFEST_DIR) -> Path:
    return root / "case" / f"{lang}.tsv.gz"


def load_case(lang: str, root: Path = MANIFEST_DIR) -> CaseTally:
    path = case_path(lang, root)
    if not path.exists():
        raise SystemExit(f"{path}: no case tally; the capitalised_mid_sentence rule needs one")
    raw = path.read_bytes()
    positions: dict[str, tuple[int, int, int]] = {}
    for line in gzip.decompress(raw).decode("utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        form, initial, running, title = line.split("\t")
        positions[form] = (int(initial), int(running), int(title))
    return CaseTally(path, hashlib.sha256(raw).hexdigest(), positions)


def learnable(lemma: str, names: LearnableNames) -> bool:
    return lemma.split("#")[0].casefold() in names.names


def mid_capitalised_share(forms: Mapping[str, int], tally: CaseTally) -> float | None:
    """Share of a lemma's mid-sentence occurrences that are capitalised (module docstring); None without evidence."""
    cap = low = 0.0
    for form, count in forms.items():
        if not form[:1].isalpha():
            continue
        if len(form) > 1 and form.isupper():
            continue
        if form[:1].isupper() or any(c.isupper() for c in form[1:]):
            initial, running, title = tally.positions.get(form, (0, 1, 0))
            cap += count * running / (initial + running + title) if initial + running + title else count
        else:
            low += count
    return cap / (cap + low) if cap + low > 0 else None


def apply[T](
    ranked: Sequence[T], lemma_of: Callable[[T], str], pos_of: Callable[[T], str],
    forms_of: Callable[[T], Mapping[str, int]], names: LearnableNames, tally: CaseTally, threshold: float,
    rank_of: Mapping[str, int],
) -> tuple[list[T], list[Dropped], list[tuple[int, str]], list[Dropped]]:
    """Returns: kept rows, dropped proper nouns, learnable names kept, PROPN lemmas kept by the case test."""
    kept: list[T] = []
    dropped: list[Dropped] = []
    names_kept: list[tuple[int, str]] = []
    case_kept: list[Dropped] = []
    for row in ranked:
        lemma = lemma_of(row)
        if pos_of(row) != PROPN:
            kept.append(row)
            continue
        if learnable(lemma, names):
            kept.append(row)
            names_kept.append((rank_of[lemma], lemma))
            continue
        share = mid_capitalised_share(forms_of(row), tally)
        if share is None or share >= threshold:
            dropped.append(Dropped(rank_of[lemma], lemma, share))
        else:
            kept.append(row)
            case_kept.append(Dropped(rank_of[lemma], lemma, share))
    return kept, dropped, names_kept, case_kept


def header_entry(names: LearnableNames, tally: CaseTally, threshold: float, dropped: Sequence[Dropped],
                 names_kept: Sequence[tuple[int, str]], case_kept: Sequence[Dropped], top_n: int,
                 root: Path, repo_root: Path) -> dict[str, Any]:
    def rel(p: Path, base: Path) -> str:
        try:
            return str(p.relative_to(base))
        except ValueError:
            return str(p)
    return {
        "rule": "capitalised_mid_sentence: a PROPN-majority lemma that is not a learnable name is dropped when "
                f"at least {threshold:.0%} of its mid-sentence occurrences are capitalised",
        "learnable_names": rel(names.path, root), "learnable_names_sha256": names.sha256,
        "case_tally": rel(tally.path, repo_root), "case_tally_sha256": tally.sha256,
        "dropped_from_top_n": sum(1 for d in dropped if d.rank <= top_n),
        "learnable_names_kept": sum(1 for r, _ in names_kept if r <= top_n),
        "kept_by_case_test": sum(1 for d in case_kept if d.rank <= top_n),
    }


def render(names: LearnableNames, tally: CaseTally, threshold: float, dropped: Sequence[Dropped],
           names_kept: Sequence[tuple[int, str]], case_kept: Sequence[Dropped], top_n: int) -> list[str]:
    inside = [d for d in dropped if d.rank <= top_n]
    kept = [k for k in names_kept if k[0] <= top_n]
    common = [d for d in case_kept if d.rank <= top_n]

    def fmt(d: Dropped) -> str:
        return f"`{d.lemma}` ({d.rank}, {'-' if d.share is None else format(d.share, '.0%')})"
    return [
        "## Proper nouns", "",
        f"A PROPN-majority lemma is dropped unless it is a learnable name (`{names.path.name}`, sha256 "
        f"`{names.sha256[:16]}`) or fewer than {threshold:.0%} of its mid-sentence occurrences are capitalised "
        f"(case tally `{tally.path.name}`, sha256 `{tally.sha256[:16]}`). Among the first build's top {top_n:,}: "
        f"{len(inside):,} dropped, {len(kept):,} learnable names kept, {len(common):,} kept as common nouns by "
        "the case test. In brackets: rank before filtering, then the mid-sentence capitalised share.", "",
        "Kept by the case test (first 60): " + ", ".join(fmt(d) for d in common[:60]), "",
        "Learnable names kept (first 40): " + ", ".join(f"`{lemma}` ({r})" for r, lemma in kept[:40]), "",
        "Dropped (first 40): " + ", ".join(fmt(d) for d in inside[:40]), "",
    ]


@dataclass
class Uncounted:
    """Learnable names no counted lemma carries (``build`` appends ``bare``; ``multiword`` waits for a release)."""

    bare: list[str]  # one-word names with no occurrences, as the list writes them (lower-cased when folded)
    filed_under: dict[str, str]  # one-word name -> the lemma whose forms hold its spelling
    multiword: list[str]


def uncounted_names(names: LearnableNames, lemmas: Mapping[str, LemmaStats], fold: bool = True) -> Uncounted:
    keys = {k.split("#")[0].casefold() for k in lemmas}
    holder: dict[str, str] = {}
    for lemma, st in lemmas.items():  # the commonest lemma holding each spelling
        for form in st.forms:
            f = form.casefold()
            if f not in holder or lemmas[holder[f]].freq < st.freq:
                holder[f] = lemma
    raw = json.loads(names.path.read_bytes())["names"]
    out = Uncounted([], {}, [])
    for name in dict.fromkeys(str(n) for n in raw):
        key = name.casefold()
        if key in keys:
            continue
        if " " in name.strip():
            if name.casefold() not in {m.casefold() for m in out.multiword}:
                out.multiword.append(name)
        elif key in holder:
            out.filed_under[key] = holder[key]
        elif key not in out.bare and name not in out.bare:
            out.bare.append(key if fold else name)
    return out


def write_multiword(path: Path, unc: Uncounted) -> None:
    with path.open("w", encoding="utf-8") as fp:
        fp.write("# name\ttokens\tnote\n")
        for name in sorted(unc.multiword, key=str.casefold):
            fp.write(f"{name}\t{len(name.split())}\tlearnable multi-word name; release 1.5.0 emits no unit for it, "
                     "so its parts are counted as separate words; to become a unit headword in lemma release 1.6\n")
