"""The Honeyeater runtime, loaded outside the app: the one counting path.

Every sentence goes through the production sentence stage,
:func:`nlp.sentence_stage.analysed_sentences` — the batched core the article pipeline
runs (each model once per batch of sentences): tokenize, the backend's candidates, the language's lemma release
(lemma + UPOS for every token, and its units), numbers spelled out, the
release's units merged into occurrences. frequer supplies only the release:
the app fetches the pinned wheel from R2 (:func:`nlp.lemma_releases.lemmatiser_for`),
frequer hands the stage a :class:`nlp.lemma_releases.SentenceLemmatiser` over a
locally installed wheel instead, so a release can be counted before it is
pinned. Nothing here lemmatises on its own. Run from ``honeyeater/backend``
(a pinned checkout) with ``PYTHONPATH=.``.

What a count takes from each sentence (:class:`AnalysedSentence`):

- **occurrences**, as the app's inventory has them: one per word token, one per
  multi-token compound (a compound is a word: *me llamo* is one *llamarse*), and
  for a **combination** (phrase or construction: not a word, counted apart in
  the app) one occurrence of the combination *next to* its member words, so
  *poder + infinitivo* ranks as itself without taking *poder*'s count;
- the release's own per-token **lemmas, UPOS and units**, for the co-occurrence
  pass and the unit table.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import logging
import os
import re
import subprocess
import time
from collections.abc import Callable, Iterable, Iterator, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer.config import LanguageConfig, sha256_file

SKIP_LEMMAS = frozenset({"_", "~", ""})
#: Unit types the app counts apart from words (plan §3.6: "combinations").
COMBINATIONS = frozenset({"phrase", "construction"})
#: Sentences per batch of the sentence stage (each model runs once per batch).
BATCH_SIZE = 64


@dataclass(frozen=True)
class RuntimeInfo:
    """Everything a snapshot header must record about how it was counted."""

    tokenizer: str
    lemma_package: str
    lemma_version: str
    lemma_sha256: str
    wheel_sha256: str | None
    #: The unseen-form fallback the release ran with (``spacy-list`` or ``backend``).
    fallback: str
    units: bool
    honeyeater_commit: str
    honeyeater_dirty: bool
    #: The override file feeds only the ``backend`` fallback under a release
    #: (``SentenceLemmatiser.fallback``); its hash is recorded either way.
    overrides_path: str
    overrides_sha256: str
    theta: float


@dataclass(frozen=True)
class Occurrence:
    """One counted occurrence: a word, a compound, or a combination."""

    lemma: str
    #: ``word``; ``compound1`` (one-token compound); ``compound`` (multi-token);
    #: ``phrase`` / ``construction`` (combinations); ``multi`` (a merged phrase
    #: of a release without units: the MWE table or the backend's long units).
    kind: str
    surface: str
    pos: str
    #: Token indices (into ``AnalysedSentence.words``).
    tokens: tuple[int, ...]
    reading: str = ""
    reading_source: str = ""
    #: A Japanese ending that took its host's lemma (``host_tokens`` decides).
    host: bool = False


@dataclass
class AnalysedSentence:
    """One sentence: every non-space token, the release's view, and the occurrences."""

    words: list[str]
    #: The release's lemma (homograph key kept) and UPOS per token.
    lemmas: list[str]
    upos: list[str]
    #: The release's units (``nlp.units.Unit``), or None for a release without them.
    units: list[Any] | None
    occurrences: list[Occurrence] = field(default_factory=list)


def tree_sha256(root: Path) -> str:
    """Content hash of an installed release directory (names and bytes, sorted)."""
    digest = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def git_head(repo: Path) -> tuple[str, bool]:
    def run(*args: str) -> str:
        return subprocess.run(
            ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
        ).stdout.strip()

    return run("rev-parse", "HEAD"), bool(run("status", "--porcelain", "--untracked-files=no"))


def find_release_dir(package: str, explicit: Path | None) -> Path:
    if explicit is not None:
        return explicit
    spec = importlib.util.find_spec(package)
    if spec is None or not spec.submodule_search_locations:
        raise SystemExit(f"{package} is not installed; pass --lemma-dir or add its site dir to PYTHONPATH")
    return Path(next(iter(spec.submodule_search_locations)))


def setup_django() -> None:
    """Bring up Django from ``honeyeater/backend`` so ``nlp.*`` and ``lexicon.*`` import."""
    logging.disable(logging.WARNING)  # the backend and procrastinate log JSON at INFO
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test")
    import django

    django.setup()


@dataclass
class StageClock:
    """Seconds per named stage."""

    seconds: dict[str, float] = field(default_factory=dict)

    def __call__(self, stage: str, secs: float) -> None:
        self.seconds[stage] = self.seconds.get(stage, 0.0) + secs


class Runtime:
    """Backend + lemma release for one language, wired into the production sentence stage."""

    def __init__(
        self,
        language: LanguageConfig,
        *,
        lemma_dir: Path | None = None,
        wheel: Path | None = None,
        fallback: str | None = None,
    ) -> None:
        setup_django()
        import nlp
        import nlp.sentence_stage as stage
        from nlp import registry
        from nlp.lemma_releases import Pin, pin_for
        from nlp.lemma_step import load_release

        registry.register_defaults()
        self.language = language
        self._pattern = re.compile(language.lemma_pattern)
        self.backend: Any = registry.create(language.tokenizer)
        release_dir = find_release_dir(language.lemma_package, lemma_dir)
        release = load_release(release_dir)
        if getattr(release.lookup, "word_rules", None) is not None and hasattr(release.lookup, "registered"):
            # The registry guard (Honeyeater #820, nlp.lemma_releases._lemmatiser): the release learns the
            # language's homograph registry when it is loaded for a language; do the same here.
            import dataclasses

            from lexicon.homographs import registered_keys

            release = dataclasses.replace(
                release, lookup=dataclasses.replace(release.lookup, registered=registered_keys(language.code)))
        self.root = Path(os.environ.get("HONEYEATER_ROOT", Path(nlp.__file__).resolve().parents[2]))
        pinned = pin_for(language.code)
        chosen = fallback or (pinned.fallback if pinned else "backend")
        wheel_sha = sha256_file(wheel) if wheel else None
        pin = Pin(
            version=release.version,
            wheel=wheel.name if wheel else f"{language.lemma_package}-{release.version}",
            sha256=wheel_sha or "",
            fallback=chosen,
            units=release.units is not None,
        )
        self.lemmatiser = _recording(language.code, pin, release)
        self.units_release: Any = release.units
        # The stage asks ``lemmatiser_for(code)`` for the release, and a backend whose
        # release cuts its tokens (Japanese, ``segmenter_for``) asks the module's own
        # ``lemmatiser_for``: answer both with ours.
        import nlp.lemma_releases as releases

        def ours(code: str) -> Any:
            return self.lemmatiser if code == language.code else None

        stage.lemmatiser_for = ours
        releases.lemmatiser_for = ours
        override_file = self.root / "reference" / "lemma-overrides" / f"{language.code}.json"
        commit, dirty = git_head(self.root)
        meta = json.loads((release_dir / "release.json").read_text(encoding="utf-8"))
        self.release_dir = release_dir
        self.info = RuntimeInfo(
            tokenizer=language.tokenizer,
            lemma_package=language.lemma_package,
            lemma_version=release.version,
            lemma_sha256=tree_sha256(release_dir),
            wheel_sha256=wheel_sha,
            fallback=chosen,
            units=release.units is not None,
            honeyeater_commit=commit,
            honeyeater_dirty=dirty,
            overrides_path=f"reference/lemma-overrides/{language.code}.json",
            overrides_sha256=sha256_file(override_file) if override_file.exists() else "absent",  # zh has none
            theta=float(meta["theta"]),
        )

    # -- analysis ---------------------------------------------------------

    def sentences(self, text: str, clock: Callable[[str, float], None] | None = None) -> Iterator[AnalysedSentence]:
        """Segment ``text`` and run each sentence through the production sentence stage."""
        return (sentence for _key, sentence in self.sentences_many([(0, text)], clock))

    def sentences_many[K](
        self,
        items: Iterable[tuple[K, str]],
        clock: Callable[[str, float], None] | None = None,
        *,
        batch_size: int = BATCH_SIZE,
    ) -> Iterator[tuple[K, AnalysedSentence]]:
        """Each ``(key, text)`` segmented and analysed through the batched sentence stage.

        The texts' sentences are one lazy stream (memory is one batch), so a batch spans
        lines and documents; a sentence's analysis never depends on its batch
        (``nlp.sentence_stage.analysed_sentences``). Yields ``(key, sentence)`` in order,
        a sentence per result, none for a sentence the release did not answer.
        """
        import nlp.sentence_stage as stage

        tick = clock or (lambda _stage, _secs: None)
        rec = self.lemmatiser
        segment_secs = 0.0

        def stream() -> Iterator[tuple[K, Any]]:
            nonlocal segment_secs
            for key, text in items:
                t0 = time.perf_counter()
                segments = self.backend.segment(text, paragraph_index=0, char_offset=0)
                segment_secs += time.perf_counter() - t0
                for sentence in segments:
                    yield key, sentence

        results = stage.analysed_sentences(self.backend, stream(), batch_size=batch_size)
        while True:
            lemma0, units0, segment0 = rec.seconds, rec.unit_seconds, segment_secs
            t0 = time.perf_counter()
            found = next(results, None)
            total = time.perf_counter() - t0
            units = rec.unit_seconds - units0
            lemma = rec.seconds - lemma0 - units
            segment = segment_secs - segment0
            if found is None:
                break
            key, analysis = found
            t1 = time.perf_counter()
            sentence = self._record(analysis)
            total += time.perf_counter() - t1
            tick("segment", segment)
            tick("sentence_stage", total - segment - lemma - units)
            tick("lemma_step", lemma)
            tick("units", units)
            if sentence is not None:
                yield key, sentence

    def _record(self, analysis: Any) -> AnalysedSentence | None:
        """One analysed sentence as the counting view; None when it has no release answer."""
        import nlp.sentence_stage as stage

        if analysis.release is None:
            return None
        out: list[Any] = []
        inventory: dict[str, Any] = {}
        keys: dict[tuple[int, str, int], str] = {}
        groups: dict[tuple[int, str, int], tuple[int, ...]] = {}
        stage.record_sentence(
            analysis, sentence_out=out, text_key=(0, ""), overrides={}, inventory=inventory,
            token_keys=keys, token_readings={}, position_base=0, phrase_groups=groups,
        )
        if not out:
            return None
        words = [t.text for t in analysis.tokens if not t.is_space]
        return self._assemble(out[0].tokens, inventory, keys, groups, (words, analysis.release))

    def _assemble(
        self,
        tokens: Sequence[Any],  # content.structure.StructureToken
        inventory: dict[str, Any],
        keys: dict[tuple[int, str, int], str],
        groups: dict[tuple[int, str, int], tuple[int, ...]],
        last: tuple[list[str], Any],
    ) -> AnalysedSentence:
        from nlp.lemma_step import split_key

        words, analysis = last
        offsets = [t.offset for t in tokens]
        if [t.text for t in tokens] != words:
            raise RuntimeError("the release saw different tokens than the sentence stage kept")
        index = {offset: k for k, offset in enumerate(offsets)}
        lemmas = [lemma for lemma, _upos in analysis.tagged]
        upos = [tag for _lemma, tag in analysis.tagged]
        sent = AnalysedSentence(words=words, lemmas=lemmas, upos=upos, units=analysis.units)
        # Which release unit (if any) an occurrence is: its lemma, at its tokens.
        by_token: dict[int, list[Any]] = {}
        for unit in analysis.units or ():
            for t in unit.tokens:
                by_token.setdefault(t, []).append(unit)
        members = {o for offs in groups.values() for o in offs[1:]}
        pos_of = {t.offset: t.pos or "X" for t in tokens}
        # Only a release that keys endings by their form (``host_keys``: Japanese) has host tokens:
        # an ending carries its host's lemma (会い|まし|た, 勉強し|て). It is part of that word
        # however the host was counted (alone, or inside a compound such as 勉強する), so it never
        # adds a second occurrence of the host's lemma.
        endings = bool(self.units_release and self.units_release.settings.candidates.host_keys)

        def is_ending(k: int) -> bool:
            return endings and k > 0 and lemmas[k] == lemmas[k - 1] and words[k] != lemmas[k]
        for (_p, _s, offset), lemma in sorted(keys.items(), key=lambda kv: index[kv[0][2]]):
            if offset in members:
                continue
            offs = groups.get((0, "", offset), (offset,))
            idx = tuple(sorted(index[o] for o in offs))
            unit = next((u for u in by_token.get(idx[0], ()) if u.lemma == lemma and set(idx) <= set(u.tokens)), None)
            if unit is None:
                kind = "multi" if len(idx) > 1 else "word"
            elif unit.type == "compound":
                kind = "compound1" if len(unit.tokens) == 1 else "compound"
            else:
                kind = unit.type
            entry = inventory.get(lemma)
            reading = str(getattr(entry, "reading", "") or "")
            source = getattr(entry, "reading_source", "")
            k = idx[0]
            host = len(idx) == 1 and lemma == lemmas[k] and is_ending(k)
            sent.occurrences.append(Occurrence(
                lemma=lemma, kind=kind, surface=" ".join(words[i] for i in idx), pos=pos_of[offset],
                tokens=idx, reading=reading, reading_source=str(getattr(source, "value", source) or ""),
                host=host,
            ))
            if kind in COMBINATIONS:
                # The combination counts next to its member words, not instead of them.
                for i in idx:
                    following = words[i + 1] if i + 1 < len(words) else ""
                    spelled = self.backend.spell_number(words[i], following=following)
                    word = spelled.lemma if spelled is not None else lemmas[i]
                    if split_key(word)[0] in SKIP_LEMMAS:
                        continue
                    sent.occurrences.append(Occurrence(
                        lemma=word, kind="word", surface=words[i], pos=upos[i], tokens=(i,),
                        host=spelled is None and is_ending(i),
                    ))
        return sent

    def key(self, lemma: str, kind: str = "word") -> str | None:
        """The snapshot key an occurrence is counted under, or None when it is not counted.

        A word's bare lemma (homograph key off) must match the language's
        ``lemma_pattern``; the key keeps the homograph key (``See#Fem``), which
        is the lemma's identity. A unit headword (spaces, slot labels) only
        needs a letter.
        """
        from nlp.lemma_step import split_key

        bare, homograph = split_key(lemma)
        if bare in SKIP_LEMMAS:
            return None
        if self.language.fold_case:
            bare = bare.lower()
        if kind in ("word", "compound1"):
            if not self._pattern.match(bare):
                return None
        elif not any(ch.isalpha() for ch in bare):
            return None
        return f"{bare}#{homograph}" if homograph else bare

    def cooc_keys(self, sent: AnalysedSentence) -> list[str]:
        """The unit detector's token keys (``nlp.units.token_keys``), homograph keys off."""
        from nlp.units import token_keys

        from frequer.cooc import bare_key

        host_keys = bool(self.units_release and self.units_release.settings.candidates.host_keys)
        return [bare_key(k) for k in token_keys(sent.words, sent.lemmas, host_keys=host_keys)]

    def pair_spans(self, sent: AnalysedSentence) -> list[tuple[int, ...]]:
        """The release's off-list verb-pair candidates (``open_spans`` source ``pair``)."""
        if self.units_release is None:
            return []
        from nlp.unit_rules import open_spans

        cand = self.units_release.settings.candidates
        if cand.reflexive is None and not cand.particle_pairs:
            return []
        return [tokens for source, tokens in open_spans(cand, sent.lemmas, sent.upos) if source == "pair"]

    @staticmethod
    def unit_tokens(sent: AnalysedSentence) -> frozenset[int]:
        """Every token (fixed or slot) of a unit the release found in ``sent``."""
        return frozenset(t for unit in sent.units or () for t in unit.members)

    def pair_windows(self) -> dict[int, float]:
        """Window size per pair length, for the expected frequency (``assoc``)."""
        if self.units_release is None:
            return {}
        cand = self.units_release.settings.candidates
        return pair_windows(cand.reflexive_reach, cand.particle_pairs)

    def pair_headword(self, key: str) -> str:
        """The headword the release's rule would give a pair key (``nlp.unit_rules.headword_rule``)."""
        if self.units_release is None:
            return ""
        from nlp.unit_rules import headword_rule

        settings = self.units_release.settings
        parts = key.split(" ")
        upos = ["VERB"] + ["PRON" if p == settings.candidates.reflexive else "ADP" for p in parts[1:]]
        # The rule reads text order; the verb's place does not change its output.
        head = headword_rule(settings.headword_rule, settings.candidates, parts, parts, upos,
                             tuple(range(len(parts))), name=False)
        return head or ""

    def splits(self, text: str) -> bool:
        """Whether ``text`` analysed alone is cut into several tokens that no single occurrence (a word or a
        unit) covers whole: the reader would never carry it as one lemma."""
        for sentence in self.sentences(text):
            return len(sentence.words) > 1 and not any(len(o.tokens) == len(sentence.words)
                                                       for o in sentence.occurrences)
        return False

    def lemma_of_word(self, word: str) -> str | None:
        """The counted key of ``word`` analysed alone (for the review checks)."""
        for sentence in self.sentences(word):
            for occ in sentence.occurrences:
                if occ.kind == "word" and occ.surface == word:
                    return self.key(occ.lemma)
        return None


def pair_windows(reflexive_reach: int, particle_pairs: bool) -> dict[int, float]:
    """A reflexive may sit ``reach`` tokens either side of its verb; a separated
    particle up to 14 tokens after it (``open_spans``)."""
    two = float(2 * reflexive_reach)
    if particle_pairs:
        two = max(two, 14.0)
    return {2: two, 3: two}


def _recording(code: str, pin: Any, release: Any) -> Any:
    """A ``SentenceLemmatiser`` that times its batches and, apart, its unit detector."""
    from nlp.lemma_releases import SentenceLemmatiser

    class Recording(SentenceLemmatiser):  # type: ignore[misc]  # nlp.* is untyped from here
        seconds = 0.0
        unit_seconds = 0.0

        def analyse_many(self, requests: Sequence[Any]) -> Any:
            t0 = time.perf_counter()
            try:
                return super().analyse_many(requests)
            finally:
                self.seconds += time.perf_counter() - t0

    rec = Recording(code, pin, release)
    units = release.units
    if units is not None:
        find_many = units.find_many

        def timed(sentences: Sequence[Any]) -> Any:
            t0 = time.perf_counter()
            try:
                return find_many(sentences)
            finally:
                rec.unit_seconds += time.perf_counter() - t0

        units.find_many = timed  # an instance attribute: the class's method is untouched
    return rec
