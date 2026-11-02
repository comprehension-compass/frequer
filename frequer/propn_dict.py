"""Proper-noun evidence from a dictionary, for a script without case (``JunkConfig.propn_evidence: dictionary``).

A provider returns, for a word, the proper-noun class of each of its dictionary entries: ``person``,
``organization``, ``place``, ``proper`` (another proper noun: a brand, product, era) or ``common`` (any entry
that is not a proper noun). :func:`frequer.junk.dictionary_verdict` reads them. The evidence is the dictionary's,
not a guess from the text, so a name with no common reading can drop on it.

``sudachi``: SudachiPy's core dictionary (the one the Japanese backend analyses with), every entry whose
surface is the lemma (``Dictionary.lookup``); 名詞-固有名詞-人名 / 組織名 / 地名 / 一般.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import cache

SUDACHI_CLASSES = {"人名": "person", "組織名": "organization", "地名": "place"}


def provider(name: str) -> Callable[[str], list[str]]:
    if name == "sudachi":
        return _sudachi()
    raise SystemExit(f"unknown proper-noun dictionary {name!r}")


def _sudachi() -> Callable[[str], list[str]]:
    from sudachipy import Dictionary  # type: ignore[import-untyped]

    dictionary = Dictionary(dict="core")

    @cache
    def classes(word: str) -> list[str]:
        out: list[str] = []
        for m in dictionary.lookup(word):
            pos = m.part_of_speech()
            out.append(SUDACHI_CLASSES.get(pos[2], "proper") if pos[1] == "固有名詞" else "common")
        return out

    return classes
