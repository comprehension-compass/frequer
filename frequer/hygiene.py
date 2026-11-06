"""Line hygiene before counting: bounds, junk, duplicates, language ID.

The same filters the lemmatiser sampler uses (including its stripped-link
``GAP``) plus the web-corpus hygiene HPLT needs. Everything here is per shard:
the dedup sets are discarded with the shard, so a shard's output depends only on
its own input and a lost worker costs exactly one shard.
"""

from __future__ import annotations

import hashlib
import re
from collections import Counter
from collections.abc import Callable

from frequer.config import Hygiene

#: Link text that wikitext/HTML cleaning lost ("word  , word"): honeyeater-lemmatiser
#: ``scripts/sample.py`` ``GAP`` (v3.22).
GAP = re.compile(r"\S {2,}\S| [,.;:)]")
_SPACE = re.compile(r"\s+")
_DIGITS = re.compile(r"\d+")
_NON_WORD = re.compile(r"[\W_]+")

Classifier = Callable[[str], tuple[str, float]]

#: Reasons a line is dropped, in the order they are tested.
REASONS = ("length", "alpha", "gap", "exact_dup", "near_dup", "traditional", "langid", "traditional_doc")
#: Hygiene fields added after the es/de/ja counts: left out of a shard's config hash while at their default,
#: so those counts keep their identity.
LATE_DEFAULTS: dict[str, object] = {"simplified_only": False, "traditional_doc_share": 0.2, "langid_aliases": []}


def clean_line(line: str) -> str:
    """Collapse whitespace (tabs and newlines included) to single spaces."""
    return _SPACE.sub(" ", line).strip()


def near_key(line: str) -> int:
    """Hash of the line with case, digits, punctuation and spacing erased.

    Two lines that differ only in a number, a separator or capitalisation
    ("Page 3 of 12" / "page 4 of 12") collide: that is the boilerplate HPLT repeats.
    """
    folded = _NON_WORD.sub("", _DIGITS.sub("0", line.casefold()))
    return int.from_bytes(hashlib.blake2b(folded.encode(), digest_size=8).digest(), "big")


def exact_key(line: str) -> int:
    return int.from_bytes(hashlib.blake2b(line.encode(), digest_size=8).digest(), "big")


def alpha_ratio(line: str) -> float:
    return sum(ch.isalpha() for ch in line) / len(line) if line else 0.0


def make_classifier() -> Classifier:
    """py3langid with normalised probabilities, on a line's first 300 characters."""
    from py3langid.langid import MODEL_FILE, LanguageIdentifier

    identifier = LanguageIdentifier.from_model_file(MODEL_FILE, norm_probs=True)

    def classify(line: str) -> tuple[str, float]:
        lang, prob = identifier.classify(line[:300])
        return str(lang), float(prob)

    return classify


class LineFilter:
    """One shard's filter. ``accept`` returns the cleaned line, or None when dropped.

    ``dedup=False`` skips the exact and near-duplicate tests: the form inventory counts, per
    line, the documents it occurs in, so it removes repeated lines itself after the whole run.
    """

    def __init__(self, cfg: Hygiene, lang: str, classify: Classifier, *, dedup: bool = True) -> None:
        self.cfg, self.lang, self._classify, self._dedup = cfg, lang, classify, dedup
        #: The last dropped line's reason and cleaned text (the inventory keeps langid rejects).
        self.last_drop: tuple[str, str] | None = None
        self._exact: set[int] = set()
        self._near: set[int] = set()
        self.dropped: Counter[str] = Counter()
        self.kept = 0
        self._t2s: Callable[[str], str] | None = None
        if cfg.simplified_only:
            import opencc  # opencc-python-reimplemented, a Honeyeater backend dependency

            self._t2s = opencc.OpenCC("t2s").convert

    def accept(self, raw: str) -> str | None:
        line = clean_line(raw)
        self.last_drop = None
        cfg = self.cfg
        if not cfg.min_chars <= len(line) <= cfg.max_chars:
            return self._drop("length", line)
        if alpha_ratio(line) < cfg.min_alpha_ratio:
            return self._drop("alpha", line)
        if cfg.gap_filter and GAP.search(line):
            return self._drop("gap", line)
        if self._dedup:
            exact = exact_key(line)
            if exact in self._exact:
                return self._drop("exact_dup", line)
            self._exact.add(exact)
            near = near_key(line)
            if near in self._near:
                return self._drop("near_dup", line)
            self._near.add(near)
        if self._t2s is not None and self._t2s(line) != line:
            return self._drop("traditional", line)
        if cfg.langid_min_prob > 0:  # 0 trusts the source's own language label (Tatoeba)
            lang, prob = self._classify(line)
            if (lang != self.lang and lang not in cfg.langid_aliases) or prob < cfg.langid_min_prob:
                return self._drop("langid", line)
        self.kept += 1
        return line

    def drop_kept(self, n: int, reason: str) -> None:
        """Take back ``n`` accepted lines (a document dropped whole after its lines were tested)."""
        self.kept -= n
        self.dropped[reason] += n

    def _drop(self, reason: str, line: str) -> str | None:
        self.dropped[reason] += 1
        self.last_drop = (reason, line)
        return None
