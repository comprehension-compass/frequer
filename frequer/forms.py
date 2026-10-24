"""The form inventory: word-token counts per surface form, with document and site spread.

Tokenizer-only. A cleaned shard (see :mod:`frequer.shards`, inventory mode) goes through the
segmentation-free tokenizer, never the lemma step, and each form is tallied with its total count,
the documents it occurs in and the sites those documents came from. Lines repeated across
documents (menus, cookie banners, footers) are removed first: a normalised line seen in
``REPEAT_DOCS`` or more different documents is dropped everywhere.

Pure cores here (``is_word``, ``repeated_keys``, :class:`ShardForms`, the shard file format and
:func:`merge_forms`); :mod:`frequer.forms_run` orchestrates.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from array import array
from collections import Counter
from collections.abc import Callable, Iterable, Iterator, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np
import numpy.typing as npt

from frequer.config import LanguageConfig, Manifest

#: A normalised line in this many different documents is boilerplate.
REPEAT_DOCS = 3

Tokenize = Callable[[str], list[str]]
U64 = npt.NDArray[np.uint64]


def is_word(text: str) -> bool:
    """A word token has at least one letter: punctuation, spaces and pure digits are not words."""
    return any(ch.isalpha() for ch in text) and not any(ch.isspace() for ch in text)


def site_tag(site: str) -> int:
    """A stable 32-bit id for a site (host or pseudo-document), small enough to store per row."""
    return int.from_bytes(hashlib.blake2b(site.encode(), digest_size=4).digest(), "big")


# -- tokenizers -----------------------------------------------------------------------------------


def spacy_blank_tokenizer(code: str) -> Tokenize:
    """``spacy.blank(code).tokenizer``: the rule-based tokens the app's spaCy backends produce."""
    import spacy

    tokenizer = spacy.blank(code).tokenizer

    def tokens(line: str) -> list[str]:
        return [t.text for t in tokenizer(line) if is_word(t.text)]

    return tokens


def backend_tokenizer(language: LanguageConfig) -> Tokenize:
    """The Honeyeater backend's own segment + tokenize (Sudachi for ja), no lemma step."""
    from frequer.runtime import setup_django

    setup_django()
    from nlp import registry

    registry.register_defaults()
    backend: Any = registry.create(language.tokenizer)

    def tokens(line: str) -> list[str]:
        out: list[str] = []
        for sentence in backend.segment(line, paragraph_index=0, char_offset=0):
            out.extend(t.text for t in backend.tokenize(sentence) if not t.is_space and is_word(t.text))
        return out

    return tokens


def make_tokenizer(manifest: Manifest) -> Tokenize:
    forms = manifest.forms
    if forms is None:
        raise SystemExit(f"{manifest.language.code}: the manifest has no forms: block")
    if forms.tokenizer == "spacy_blank":
        return spacy_blank_tokenizer(manifest.language.code)
    return backend_tokenizer(manifest.language)


# -- repeated lines -------------------------------------------------------------------------------


def repeated_keys(keys: Sequence[int] | U64, docs: Sequence[int] | U64, min_docs: int = REPEAT_DOCS) -> U64:
    """Sorted line keys that occur in at least ``min_docs`` different documents.

    ``keys[i]`` is the normalised-line key of one occurrence, ``docs[i]`` the document it was in
    (unique across the whole run). Repeats inside one document count once. Bounded memory: two
    machine words per occurrence, however many lines there are.
    """
    k = np.asarray(keys, dtype=np.uint64)
    d = np.asarray(docs, dtype=np.uint64)
    if not k.size:
        return np.empty(0, dtype=np.uint64)
    order = np.lexsort((d, k))
    k, d = k[order], d[order]
    fresh = np.ones(k.size, dtype=bool)
    fresh[1:] = (k[1:] != k[:-1]) | (d[1:] != d[:-1])  # first occurrence of each (key, doc)
    unique_keys, per_key = np.unique(k[fresh], return_counts=True)
    result: U64 = unique_keys[per_key >= min_docs]
    return result


# -- one shard's tally ----------------------------------------------------------------------------


@dataclass
class ShardForms:
    """Forms of one shard: count, documents, and the sites they were seen on."""

    counts: Counter[str] = field(default_factory=Counter)
    docs: Counter[str] = field(default_factory=Counter)
    sites: dict[str, set[int]] = field(default_factory=dict)

    def add_document(self, site: int, tokens: Iterable[str]) -> None:
        seen: set[str] = set()
        for form in tokens:
            self.counts[form] += 1
            seen.add(form)
        for form in seen:
            self.docs[form] += 1
            self.sites.setdefault(form, set()).add(site)


def write_forms(path: Path, meta: dict[str, Any], forms: ShardForms) -> None:
    """``# <meta json>`` then ``form<TAB>count<TAB>docs<TAB>site,site,...`` (hex), gzip."""
    tmp = path.with_suffix(".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=3) as fp:
        fp.write("# " + json.dumps(meta, ensure_ascii=False) + "\n")
        for form, n in forms.counts.items():
            sites = ",".join(f"{s:x}" for s in forms.sites[form])
            fp.write(f"{form}\t{n}\t{forms.docs[form]}\t{sites}\n")
    tmp.replace(path)


def read_forms_meta(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        meta: dict[str, Any] = json.loads(fp.readline()[2:])
    return meta


def iter_forms(path: Path) -> Iterator[tuple[str, int, int, list[int]]]:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        fp.readline()
        for raw in fp:
            form, n, d, sites = raw.rstrip("\n").split("\t")
            yield form, int(n), int(d), [int(s, 16) for s in sites.split(",")]


# -- merge ----------------------------------------------------------------------------------------


@dataclass
class MergedForms:
    forms: list[str]
    counts: npt.NDArray[np.int64]
    docs: npt.NDArray[np.int64]
    sites: npt.NDArray[np.int64]

    def rows(self) -> Iterator[tuple[str, int, int, int]]:
        """Forms by descending count (ties by form)."""
        order = sorted(range(len(self.forms)), key=lambda i: (-int(self.counts[i]), self.forms[i]))
        for i in order:
            yield self.forms[i], int(self.counts[i]), int(self.docs[i]), int(self.sites[i])


def merge_forms(paths: Iterable[Path]) -> MergedForms:
    """Sum shard tallies. A document lives in one shard, so documents add; sites are unioned.

    The (form, site) pairs are kept as packed 64-bit words and de-duplicated once at the end, so
    memory is eight bytes per pair rather than a Python set per form.
    """
    ids: dict[str, int] = {}
    counts: list[int] = []
    docs: list[int] = []
    pairs = array("Q")
    for path in paths:
        for form, n, d, sites in iter_forms(path):
            i = ids.get(form)
            if i is None:
                i = ids[form] = len(counts)
                counts.append(0)
                docs.append(0)
            counts[i] += n
            docs[i] += d
            base = i << 32
            pairs.extend(base | s for s in sites)
    unique = np.unique(np.frombuffer(pairs, dtype=np.uint64)) if pairs else np.empty(0, dtype=np.uint64)
    sites_per = np.bincount((unique >> np.uint64(32)).astype(np.int64), minlength=len(counts))
    return MergedForms(list(ids), np.array(counts, dtype=np.int64), np.array(docs, dtype=np.int64),
                       sites_per.astype(np.int64))


# -- the output file ------------------------------------------------------------------------------

COLUMNS = "form\tcount\tdocs\tsites"


def write_forms_tsv(path: Path, header: dict[str, Any], merged: MergedForms) -> None:
    tmp = path.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as fp:
        fp.write("# " + json.dumps(header, ensure_ascii=False, sort_keys=True) + "\n" + COLUMNS + "\n")
        for form, n, d, s in merged.rows():
            fp.write(f"{form}\t{n}\t{d}\t{s}\n")
    tmp.replace(path)


def read_forms_tsv(path: Path) -> tuple[dict[str, Any], Iterator[tuple[str, int, int, int]]]:
    """The JSON header and a row iterator (``form, count, docs, sites``) of a ``forms-<lang>.tsv``."""
    fp = path.open(encoding="utf-8")
    header: dict[str, Any] = json.loads(fp.readline()[2:])
    if fp.readline().rstrip("\n") != COLUMNS:
        raise ValueError(f"{path}: not a forms file")

    def rows() -> Iterator[tuple[str, int, int, int]]:
        with fp:
            for raw in fp:
                form, n, d, s = raw.rstrip("\n").split("\t")
                yield form, int(n), int(d), int(s)

    return header, rows()
