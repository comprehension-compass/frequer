"""Junk-filter heuristics: per-lemma flags with evidence, accent merges, routing by flag count.

Developer direction (2026-11-01). Standing build rules, configured per language
(``language.junk``; none run unless listed). They read the existing counts, so changing them never needs a
recount. Each rule writes a flag with its evidence:

``diversity``  Low contextual diversity *for the lemma's frequency*: the documents it occurs in, divided by
               the documents ``f`` occurrences would reach if scattered at random (``N (1 - e^(-f/N))``, ``N``
               documents). Under ``diversity_max_clumping`` flags a lemma concentrated in few documents
               (Tatoeba's *Tom*, template spellings). The ratio already allows for frequency, and the report
               shows each log2-frequency band's 2nd percentile for comparison. The ranking stays raw frequency.
``citation``   The lemma's own spelling is (almost) never written as a word, under any lemma: under
               ``citation_max_share`` of its occurrences (*jugabl*, *notificarno*, *hijoshijo*). *dispuesto* is
               fine even though its masculine form is lemmatised to *disponer*. Units, numerals and verb-shaped
               lemmas (an infinitive, perhaps reflexive, which can be rarer than the inflected forms) are exempt.
``foreign``    wordfreq English zipf >= ``foreign_en_min`` and above the language's own by >= ``foreign_margin``.
               The exclusion list's ``keep-*`` rows (the reviewed loans) are exempt from this and from ``shape``.
``shape``      A hyphen, a digit, a whole-word reduplication (*señorseñor*, *hijoshijo*), a consonant followed by a
               word-final l/n/r/d/z the language does not combine (a fragment cut mid-word: *jugabl*, *facilitarl*),
               or a length extreme (*-mente* adverbs exempt).
``propn_band`` Proper nouns. With ``propn_evidence: case``, from the case tally (``frequer/propn.py``). A PROPN-majority lemma that is not a
               learnable name is capitalised in running text in at least ``propn_drop`` of its occurrences:
               dropped (acts alone). At most ``propn_keep``: kept, no flag. Between the two, or with no case
               evidence (an all-capitals acronym): flagged. With ``propn_evidence: dictionary`` (a script without
               case: ja), from the dictionary's proper-noun subtags (:func:`dictionary_verdict`): every entry a
               person or organisation name drops; every entry a proper noun with a place among them is
               ``pending-names`` (the learnable-names list decides); a PROPN tag without a proper-noun entry, or
               another proper noun (brand, era), is a flag.

``accent`` (``accent_ratio``) merges rather than flags. An unaccented spelling whose accented spelling is at least
``accent_ratio`` times as frequent moves its counts into the lemma that owns the accented spelling: the
accented lemma itself (*sabiduria* -> *sabiduría*), or the lemma of the accented form (*recibio* -> *recibir*).
It applies only when exactly one lemma owns the accented spellings, and never to a lemma the review file
marks ``keep`` (two real words: *secretaria* / *secretaría*). ñ is a letter, not an accent.

**Routing.** A lemma with 2+ flags is dropped (or, with ``review_multi_flag``, reviewed within ``review_top``). One with exactly 1 flag goes to review if it ranks within
``review_top``, and so does any lemma in the proper-noun middle band whatever its other flags. English
acronyms and names collect correlated flags (foreign, shape, proper noun), so those flags are not independent
evidence. The reviewed decision is committed in ``corpora/review/<code>.tsv`` (``lemma, decision,
reason``; decision ``keep``, ``drop``, ``merge:<lemma>`` or ``pending-names``: a place name left to the
learnable-names list, kept until it arrives) and applied by the build; a merge target counts as reviewed. An unreviewed single flag
is kept and reported as pending. A ``merge:`` decision moves the counts like an accent merge.
"""

from __future__ import annotations

import hashlib
import math
import re
import unicodedata
from collections import Counter, defaultdict
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer.config import MANIFEST_DIR, JunkConfig
from frequer.counts import LemmaStats, Merged
from frequer.snapshot import unit_kind

RULES = ("diversity", "citation", "foreign", "shape", "propn_band")
VOWELS = set("aeiouáéíóúüàèìòùâêîôûäëïöy")


def strip_accents(text: str) -> str:
    """Remove diacritics except the tilde of ñ (a letter of its own: *campana* is not *campaña*)."""
    kept = text.replace("ñ", "\0").replace("Ñ", "\1")
    plain = "".join(c for c in unicodedata.normalize("NFD", kept) if unicodedata.category(c) != "Mn")
    return plain.replace("\0", "ñ").replace("\1", "Ñ")


def base_of(lemma: str) -> str:
    return lemma.split("#")[0]


def is_unit(lemma: str) -> bool:
    return " " in lemma or "+" in lemma


# -- review decisions ---------------------------------------------------------


@dataclass(frozen=True)
class Review:
    path: Path
    sha256: str
    #: lemma -> (decision, reason); decision is keep, drop or merge:<lemma>
    decisions: dict[str, tuple[str, str]]

    def merges(self) -> dict[str, str]:
        return {k: d.split(":", 1)[1] for k, (d, _r) in self.decisions.items() if d.startswith("merge:")}


def review_path(lang: str, root: Path = MANIFEST_DIR) -> Path:
    return root / "review" / f"{lang}.tsv"


def load_review(lang: str, root: Path = MANIFEST_DIR) -> Review | None:
    path = review_path(lang, root)
    if not path.exists():
        return None
    raw = path.read_bytes()
    decisions: dict[str, tuple[str, str]] = {}
    for n, line in enumerate(raw.decode("utf-8").splitlines(), start=1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        decision = parts[1].strip() if len(parts) > 1 else ""
        if decision not in ("keep", "drop", "pending-names") and not decision.startswith("merge:"):
            raise SystemExit(f"{path}:{n}: decision {decision!r} is not keep, drop, pending-names or merge:<lemma>")
        decisions[parts[0]] = (decision, parts[2].strip() if len(parts) > 2 else "")
    return Review(path, hashlib.sha256(raw).hexdigest(), decisions)


# -- merges (accent rule and merge: decisions) ---------------------------------


@dataclass(frozen=True)
class Merge:
    source: str
    target: str
    source_freq: int
    evidence: str


def accent_merges(lemmas: Mapping[str, LemmaStats], ratio: float) -> list[Merge]:
    """Unaccented lemmas whose accented spelling is >= ``ratio`` times as frequent, owned by exactly one lemma."""
    owners: dict[str, Counter[str]] = defaultdict(Counter)  # accented spelling (lower) -> lemma -> count
    for lemma, st in lemmas.items():
        if is_unit(lemma):
            continue
        b = base_of(lemma)
        if strip_accents(b) != b:
            owners[b.lower()][lemma] += st.freq
        for form, n in st.forms.items():
            f = form.lower()
            if strip_accents(f) != f:
                owners[f][lemma] += n
    by_plain: dict[str, list[str]] = defaultdict(list)
    for spelling in owners:
        by_plain[strip_accents(spelling)].append(spelling)
    out: list[Merge] = []
    for lemma, st in lemmas.items():
        b = base_of(lemma)
        if is_unit(lemma) or strip_accents(b) != b or b.lower() not in by_plain:
            continue
        targets: Counter[str] = Counter()
        for spelling in by_plain[b.lower()]:
            targets.update(owners[spelling])
        targets.pop(lemma, None)
        if len(targets) != 1:
            continue
        (target, n), = targets.items()
        if n >= ratio * st.freq:
            out.append(Merge(lemma, target, st.freq, f"accented spelling {n:,} vs {st.freq:,}"))
    return sorted(out, key=lambda m: -m.source_freq)


def _merge_stats(into: LemmaStats, other: LemmaStats) -> None:
    into.freq += other.freq
    into.df += other.df  # an upper bound: a document holding both is counted twice
    into.by_source.update(other.by_source)
    into.pos.update(other.pos)
    into.forms.update(other.forms)
    into.parts.update(other.parts)
    into.readings.update(other.readings)
    into.kinds.update(other.kinds)


def apply_merges(merged: Merged, merges: Sequence[Merge]) -> list[Merge]:
    """Move each merge's counts into its target (in place); returns the merges applied."""
    done: list[Merge] = []
    for m in merges:
        src, dst = merged.lemmas.get(m.source), merged.lemmas.get(m.target)
        if src is None or m.source == m.target:
            continue
        if dst is None:  # the right lemma was never a candidate: the counts move under its name
            merged.lemmas[m.target] = dst = src
        else:
            _merge_stats(dst, src)
        if " " in m.target and not unit_kind(dst.kinds):
            dst.kinds = Counter({"compound": dst.freq})  # a multi-word lemma is a compound (README §Units)
        del merged.lemmas[m.source]
        done.append(m)
    return done


# -- flags -----------------------------------------------------------------------


@dataclass(frozen=True)
class Candidate:
    """What the rules need to know about one ranked lemma."""

    lemma: str
    freq: int
    pos: str
    forms: Mapping[str, int]
    docs: int
    #: Mostly met as a multi-token unit (a compound, phrase or construction): exempt from citation and shape,
    #: whatever its key looks like (ja keys have no spaces: 毎日新聞, 〜として).
    unit: bool = False


@dataclass
class Flags:
    #: lemma -> [(rule, evidence)]
    flags: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    #: proper nouns the band drops on its own: lemma -> evidence
    propn_drop: dict[str, str] = field(default_factory=dict)
    #: place names (dictionary evidence) the learnable-names list decides: lemma -> evidence
    propn_place: dict[str, str] = field(default_factory=dict)
    #: per log2-frequency band: its 2nd percentile of the clumping ratio (context for the fixed threshold)
    diversity_bands: dict[str, float] = field(default_factory=dict)

    def add(self, lemma: str, rule: str, evidence: str) -> None:
        self.flags.setdefault(lemma, []).append((rule, evidence))


_REDUP = re.compile(r"^(.{3,}?)[s-]?\1$")


def shape_evidence(b: str, cfg: JunkConfig, zipf_own: Callable[[str], float] | None) -> str | None:
    if "-" in b:
        return "hyphenated"
    if any(c.isdigit() for c in b):
        return "digit"
    if _REDUP.search(b):
        return "reduplication"
    letters = [c for c in b.lower() if c.isalpha()]
    if len(letters) >= 3 and letters[-1] in cfg.fragment_finals and letters[-2] not in VOWELS \
            and "".join(letters[-2:]) not in cfg.allowed_final_pairs:
        return f"ends in '{''.join(letters[-2:])}' (cut mid-word?)"
    if len(b) >= cfg.max_length and not b.endswith("mente"):
        return f"length {len(b)}"
    if len(b) <= cfg.short_max_length and (zipf_own is None or zipf_own(b) < cfg.short_zipf_min):
        return f"length {len(b)}"
    return None


#: A dictionary entry's proper-noun class (``frequer/propn_dict.py``): person, organization, place, proper
#: (another proper noun: a brand, product, era) or common (any entry that is not a proper noun).
NAME_CLASSES = ("person", "organization")


def dictionary_verdict(entries: Sequence[str], tagged_propn: bool) -> tuple[str, str] | None:
    """``(verdict, evidence)`` from a lemma's dictionary entries: ``name`` (drop), ``place`` (the learnable-names
    list decides), ``review`` (one flag), or None. Only a lemma whose every entry is a proper noun is a name (and
    then only if tagged PROPN) or a place; a PROPN tag the dictionary does not back (common-noun entries, or none) is a review flag, not a drop."""
    kinds = set(entries)
    shown = "/".join(sorted(kinds)) or "no entry"
    if kinds and "common" not in kinds:
        if "place" in kinds:
            return "place", f"dictionary: every entry a proper noun, a place among them ({shown})"
        if kinds & set(NAME_CLASSES):
            # Only with the tagger's agreement: the dictionary lacks words it builds from parts (お花 = お + 花,
            # 数人 = 数 + 人), so looked up whole they show only their name entry.
            if tagged_propn:
                return "name", f"dictionary: every entry a proper noun ({shown})"
            return "review", f"dictionary: every entry a name ({shown}), but not tagged PROPN"
        return "review", f"dictionary: proper noun, not a person or place ({shown})"
    if not tagged_propn:
        return None
    if kinds - {"common"}:
        return "review", f"tagged PROPN; dictionary has proper and common entries ({shown})"
    return "review", f"tagged PROPN; the dictionary {'has only common entries' if kinds else 'lacks it'}"


def compute_flags(
    candidates: Sequence[Candidate], cfg: JunkConfig, *, total_docs: int,
    zipf: Callable[[str, str], float] | None, lang: str, kept: frozenset[str],
    propn_share: Callable[[Candidate], tuple[float | None, bool]] | None,
    propn_dict: Callable[[Candidate], tuple[list[str], bool]] | None = None,
) -> Flags:
    """Every enabled rule over ``candidates`` (in rank order)."""
    out = Flags()
    on = set(cfg.rules)
    if "diversity" in on and total_docs:
        bands: dict[int, list[float]] = defaultdict(list)
        for c in candidates:
            if c.freq < cfg.diversity_min_freq:
                continue
            ratio = c.docs / (total_docs * (1 - math.exp(-c.freq / total_docs)))
            bands[int(math.log2(c.freq))].append(ratio)
            if ratio < cfg.diversity_max_clumping:
                out.add(c.lemma, "diversity", f"in {c.docs:,} documents, {ratio:.2f} of the {c.freq:,} occurrences' "
                                              f"random spread (threshold {cfg.diversity_max_clumping})")
        for band, ratios in bands.items():
            if len(ratios) >= cfg.diversity_min_band:
                ratios.sort()
                out.diversity_bands[f"{2 ** band}-{2 ** (band + 1) - 1}"] = round(ratios[int(0.02 * len(ratios))], 2)
    verb_shape = re.compile(cfg.verb_citation_pattern) if cfg.verb_citation_pattern else None
    own: Callable[[str], float] | None = (lambda w: zipf(w, lang)) if zipf is not None else None
    surface: Counter[str] = Counter()
    if "citation" in on:
        for c in candidates:
            for f, n in c.forms.items():
                surface[f.lower()] += n
                if " " in f:  # a multi-token form, as a language without word spaces writes it (の で: ので)
                    surface[f.replace(" ", "").lower()] += n
    for c in candidates:
        b = base_of(c.lemma)
        if "citation" in on and not is_unit(c.lemma) and not c.unit and c.pos not in ("NUM", "PROPN") \
                and not (verb_shape and verb_shape.search(b)):
            seen = surface[b.lower()]
            if seen < cfg.citation_max_share * c.freq:
                out.add(c.lemma, "citation", f"spelling written {seen:,} times as a word, against {c.freq:,} "
                                             "occurrences")
        if "foreign" in on and zipf is not None and not is_unit(c.lemma) and c.lemma not in kept:
            en, mine = zipf(b, "en"), zipf(b, lang)
            if en >= cfg.foreign_en_min and en - mine >= cfg.foreign_margin:
                out.add(c.lemma, "foreign", f"wordfreq zipf en {en:.1f} vs {lang} {mine:.1f}")
        if "shape" in on and not is_unit(c.lemma) and not c.unit and c.lemma not in kept:
            why = shape_evidence(b, cfg, own)
            if why:
                out.add(c.lemma, "shape", why)
        if "propn_band" in on and propn_dict is not None and c.pos != "NUM":  # 六十四 is also a given name
            entries, learnable = propn_dict(c)
            verdict = None if learnable else dictionary_verdict(entries, c.pos == "PROPN")
            if verdict is not None:
                kind, evidence = verdict
                if kind == "name":
                    out.propn_drop[c.lemma] = evidence
                elif kind == "place":
                    out.propn_place[c.lemma] = evidence
                else:
                    out.add(c.lemma, "propn_band", evidence)
        if "propn_band" in on and propn_share is not None and c.pos == "PROPN":
            share, learnable = propn_share(c)
            if learnable:
                continue
            if share is None:
                out.add(c.lemma, "propn_band", "proper noun with no case evidence (all-capitals or sentence-initial)")
            elif share >= cfg.propn_drop:
                out.propn_drop[c.lemma] = f"capitalised in {share:.0%} of running text"
            elif share > cfg.propn_keep:
                out.add(c.lemma, "propn_band", f"capitalised in {share:.0%} of running text")
    return out


def acronym_share(forms: Mapping[str, int]) -> float:
    tot = sum(forms.values())
    return sum(n for f, n in forms.items() if len(f) > 1 and f.isupper()) / tot if tot else 0.0


# -- routing ---------------------------------------------------------------------


@dataclass(frozen=True)
class Routed:
    lemma: str
    rank: int
    action: str  # keep, drop, review-keep, review-drop, pending, propn-drop
    flags: tuple[tuple[str, str], ...]


def route(ranked: Sequence[str], flags: Flags, review: Review | None, review_top: int,
          review_multi_flag: bool = False) -> list[Routed]:
    """The action for every ranked lemma (``ranked`` in rank order, after the exclusion list)."""
    decisions = review.decisions if review else {}
    # The lemma a reviewer merged something into was chosen by the review: it counts as reviewed.
    targets = {t.lower() for t in review.merges().values()} | set(review.merges().values()) if review else set()
    out: list[Routed] = []
    kept = 0
    for rank, lemma in enumerate(ranked, start=1):
        fl = tuple(flags.flags.get(lemma, ()))
        decision = decisions.get(lemma, ("", ""))[0]
        if lemma in flags.propn_drop:
            action = "propn-drop"
        elif decision == "drop":
            action = "review-drop"
        elif decision == "pending-names" or (lemma in flags.propn_place and not decision):
            action = "pending-names"  # a place name: decided by the learnable-names list, kept until then
        elif decision == "keep" or (lemma in targets and decision != "drop"):
            action = "review-keep"
        elif any(rule == "propn_band" for rule, _e in fl) or len(fl) == 1 or (review_multi_flag and fl):
            action = "pending" if kept < review_top else ("keep" if len(fl) == 1 else "drop")
        elif len(fl) >= 2:
            action = "drop"
        else:
            action = "keep"
        if action in ("keep", "review-keep", "pending", "pending-names"):
            kept += 1
        out.append(Routed(lemma, rank, action, fl))
    return out


def overlap(flags: Flags, lemmas: Sequence[str]) -> dict[str, dict[str, int]]:
    """How many of ``lemmas`` each pair of rules flags together (the diagonal: each rule's hits)."""
    m: dict[str, dict[str, int]] = {a: dict.fromkeys(RULES, 0) for a in RULES}
    for lemma in lemmas:
        rules = sorted({r for r, _e in flags.flags.get(lemma, ())})
        for a in rules:
            for b in rules:
                m[a][b] += 1
    return m


def summary(routed: Sequence[Routed], flags: Flags, merges: Sequence[Merge], review: Review | None,
            top_n: int) -> dict[str, Any]:
    kept_lemmas = [r.lemma for r in routed if r.action in ("keep", "review-keep", "pending")][:top_n]
    window = [r.lemma for r in routed[: top_n + sum(1 for r in routed[:top_n] if r.action not in (
        "keep", "review-keep", "pending"))]]
    return {
        "rules": list(RULES), "merges": len(merges),
        "actions": dict(Counter(r.action for r in routed[: len(window)])),
        "hits_in_window": {rule: sum(1 for lem in window if any(x == rule for x, _ in flags.flags.get(lem, ())))
                           for rule in RULES},
        "propn_drop_in_window": sum(1 for lem in window if lem in flags.propn_drop),
        "review_file_sha256": review.sha256 if review else None,
        "kept": len(kept_lemmas),
    }
