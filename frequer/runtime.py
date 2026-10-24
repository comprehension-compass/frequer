"""The Honeyeater runtime, loaded outside the app: the one counting path.

Segment and tokenize come from the production backend; the lemma is
``LemmaRelease.lemmatise`` over the installed ``honeyeater-lemma-<lang>`` wheel
and the backend's own lemma (override file applied). Nothing here lemmatises on
its own. Run from ``honeyeater/backend`` with ``PYTHONPATH=.``.
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
from collections.abc import Callable, Iterator, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer.config import LanguageConfig, sha256_file

HOST = "<="
SKIP_LEMMAS = frozenset({"_", "~"})


@dataclass(frozen=True)
class RuntimeInfo:
    """Everything a snapshot header must record about how it was counted."""

    tokenizer: str
    lemma_package: str
    lemma_version: str
    lemma_sha256: str
    wheel_sha256: str | None
    honeyeater_commit: str
    honeyeater_dirty: bool
    overrides_path: str
    overrides_sha256: str
    theta: float


@dataclass
class AnalysedSentence:
    """One sentence, tokens aligned across every list."""

    words: list[str]
    spaces: list[bool]
    #: The backend's own pos per token (``X`` for a backend that tags nothing).
    pos: list[str]
    candidates: list[Any]
    lemmas: list[str]
    #: True where the lemma step resolved the token to its host's lemma.
    host: list[bool]
    #: How each lemma was decided: ``table``, ``backend`` or ``model``.
    provenance: list[str]
    punct: list[bool]
    mismatch: bool = False


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


class Runtime:
    """Backend + lemma release + override file for one language."""

    def __init__(
        self,
        language: LanguageConfig,
        *,
        lemma_dir: Path | None = None,
        wheel: Path | None = None,
    ) -> None:
        setup_django()
        from nlp import registry
        from nlp.lemma_step import load_release
        from nlp.sentence_stage import apply_override

        registry.register_defaults()
        self.language = language
        self._pattern = re.compile(language.lemma_pattern)
        self.backend: Any = registry.create(language.tokenizer)
        self._apply_override = apply_override
        release_dir = find_release_dir(language.lemma_package, lemma_dir)
        base = load_release(release_dir)
        self.release: Any = _traced(base)
        import nlp

        self.root = Path(os.environ.get("HONEYEATER_ROOT", Path(nlp.__file__).resolve().parents[2]))
        override_file = self.root / "reference" / "lemma-overrides" / f"{language.code}.json"
        self.overrides: dict[str, str] = json.loads(override_file.read_text(encoding="utf-8"))
        commit, dirty = git_head(self.root)
        meta = json.loads((release_dir / "release.json").read_text(encoding="utf-8"))
        self.info = RuntimeInfo(
            tokenizer=language.tokenizer,
            lemma_package=language.lemma_package,
            lemma_version=base.version,
            lemma_sha256=tree_sha256(release_dir),
            wheel_sha256=sha256_file(wheel) if wheel else None,
            honeyeater_commit=commit,
            honeyeater_dirty=dirty,
            overrides_path=f"reference/lemma-overrides/{language.code}.json",
            overrides_sha256=sha256_file(override_file),
            theta=float(meta["theta"]),
        )

    # -- analysis ---------------------------------------------------------

    def sentences(self, text: str, clock: Callable[[str, float], None] | None = None) -> Iterator[AnalysedSentence]:
        """Segment, tokenize and lemmatise ``text`` the way the pipeline does."""
        tick = clock or (lambda _stage, _secs: None)
        t0 = time.perf_counter()
        segments = self.backend.segment(text, paragraph_index=0, char_offset=0)
        tick("segment", time.perf_counter() - t0)
        for sentence in segments:
            t0 = time.perf_counter()
            tokens = [t for t in self.backend.tokenize(sentence) if not t.is_space]
            tick("tokenize", time.perf_counter() - t0)
            if not tokens:
                continue
            t0 = time.perf_counter()
            candidates = [None if t.is_punct else self.backend.lemmatize(t) for t in tokens]
            candidates = [self._apply_override(c, self.overrides) if c else None for c in candidates]
            tick("backend_lemma", time.perf_counter() - t0)
            words = [t.text for t in tokens]
            spaces = [
                i + 1 < len(tokens) and tokens[i + 1].char_offset > t.char_offset + len(t.text)
                for i, t in enumerate(tokens)
            ]
            backend_lemmas = [c.lemma if c else None for c in candidates]
            t0 = time.perf_counter()
            lemmas = self.release.lemmatise(words, spaces, backend_lemmas)
            tick("lemma_step", time.perf_counter() - t0)
            raw = self.release.last_raw
            host, provenance, mismatch = trace(self.release.lookup, words, backend_lemmas, raw, lemmas)
            yield AnalysedSentence(
                words=words, spaces=spaces, pos=[t.pos for t in tokens], candidates=candidates,
                lemmas=lemmas, host=host, provenance=provenance,
                punct=[bool(t.is_punct) for t in tokens], mismatch=mismatch,
            )

    def tag(self, words: Sequence[str], spaces: Sequence[bool]) -> list[str]:
        """The lemma model's POS per token (the morphologizer), for backends that tag nothing."""
        tags: list[str] = self.release.tag(words, spaces)
        return tags

    def key(self, lemma: str) -> str | None:
        """The snapshot key a lemma is counted under, or None when it is not counted."""
        if lemma in SKIP_LEMMAS:
            return None
        if self.language.fold_case:
            lemma = lemma.lower()
        return lemma if self._pattern.match(lemma) else None

    def lemma_of_word(self, word: str) -> str | None:
        """The counted key of ``word`` analysed alone (for the review checks)."""
        for sentence in self.sentences(word):
            for text, lemma, punct in zip(sentence.words, sentence.lemmas, sentence.punct, strict=True):
                if text == word and not punct:
                    return self.key(lemma)
        return None


def trace(
    lookup: Any,  # nlp.lemma_step.Lookup
    words: Sequence[str],
    backend: Sequence[str | None],
    model_raw: Sequence[str] | None,
    final: Sequence[str],
) -> tuple[list[bool], list[str], bool]:
    """Which layer decided each token, and which tokens took their host's lemma.

    Replays the step's choice (table; model for an ambiguous form; the
    unseen-form rule between backend and model) only to
    *attribute* tokens; the lemmas themselves always come from
    ``LemmaRelease.lemmatise``. If the replay disagrees with it the runtime has
    changed under us, and the third value says so (counted per shard).
    """
    host: list[bool] = []
    provenance: list[str] = []
    resolved: list[str] = []
    for i, word in enumerate(words):
        guess = model_raw[i] if model_raw is not None else None
        key = lookup.key(word)
        if key is not None and lookup.table[key] is not None:
            raw, layer = lookup.table[key], "table"
        elif guess is None:  # the step needed the model but the trace saw no run
            return [False] * len(words), ["model"] * len(words), True
        elif key is not None:
            raw, layer = guess, "model"
        else:
            raw = lookup.unseen(word, backend[i], guess)
            layer = "model" if raw == guess else "backend"
        is_host = raw == HOST
        host.append(is_host)
        provenance.append(layer)
        resolved.append(resolved[-1] if is_host and resolved else raw)
    return host, provenance, list(final) != resolved


def _traced(base: Any) -> Any:
    """``base`` with ``model_lemmas`` recording its raw output and a ``tag`` method added."""
    from nlp.lemma_step import LemmaRelease

    class Traced(LemmaRelease):  # type: ignore[misc]  # nlp.* is untyped from here
        last_raw: list[str] | None = None

        def model_lemmas(self, words: Sequence[str], spaces: Sequence[bool]) -> list[str]:
            raw: list[str] = super().model_lemmas(words, spaces)
            object.__setattr__(self, "last_raw", raw)
            return raw

        def lemmatise(
            self, words: Sequence[str], spaces: Sequence[bool], backend: Sequence[str | None]
        ) -> list[str]:
            object.__setattr__(self, "last_raw", None)
            out: list[str] = super().lemmatise(words, spaces, backend)
            return out

        def tag(self, words: Sequence[str], spaces: Sequence[bool]) -> list[str]:
            from spacy.tokens import Doc

            doc = Doc(self.pipeline.vocab, words=list(words), spaces=list(spaces))
            for _name, proc in self.pipeline.pipeline:
                doc = proc(doc)
            return [token.pos_ for token in doc]

    return Traced(version=base.version, lookup=base.lookup, pipeline=base.pipeline)


@dataclass
class StageClock:
    """Seconds and calls per named stage."""

    seconds: dict[str, float] = field(default_factory=dict)

    def __call__(self, stage: str, secs: float) -> None:
        self.seconds[stage] = self.seconds.get(stage, 0.0) + secs
