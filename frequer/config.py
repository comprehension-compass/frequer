"""Typed corpus manifests (``corpora/<lang>.yaml``).

One file per language holds everything that differs between languages as
*data*: the tokenizer id, the lemma-key pattern, hygiene bounds, review-check
parameters and the corpus sources. Shared code never branches on a language
code; it reads these models.
"""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_DIR = REPO_ROOT / "corpora"


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Hygiene(Strict):
    """Line-level filters applied before counting (see :mod:`frequer.hygiene`)."""

    min_chars: int = 12
    max_chars: int = 1000
    min_alpha_ratio: float = 0.5
    #: Drop lines the wikitext/HTML cleaning left a stripped-link gap in
    #: (the lemmatiser sampler's ``GAP``).
    gap_filter: bool = True
    #: Minimum py3langid probability for the target language; 0 skips the filter
    #: (a source that is already human-labelled by language).
    langid_min_prob: float = 0.5


class LanguageConfig(Strict):
    code: str
    #: Honeyeater backend registry id (``nlp.registry.create``).
    tokenizer: str
    #: Importable package name of the installed ``honeyeater-lemma-<lang>`` wheel.
    lemma_package: str
    #: A lemma key must match this (the loader's ``lemma_pattern``) to be counted.
    lemma_pattern: str
    #: Lower-case lemma keys, summing on collapse (the Spanish snapshot's convention).
    fold_case: bool = False
    #: Lower-case surface forms before counting them (the German snapshot's convention).
    lowercase_forms: bool = False
    #: Emit hiragana readings derived exactly as ``build_ja_snapshot.py`` does.
    readings: bool = False
    #: Tokens the lemma step resolves to their host's lemma (a Japanese ending):
    #: ``skip`` (decided 2026-10-24) leaves them out, so 行っ|た counts 行く once;
    #: ``count`` would add each ending to its host and inflate verbs.
    host_tokens: Literal["count", "skip"] = "skip"
    #: The release's unseen-form fallback (``spacy-list`` or ``backend``); None
    #: takes the pinned checkout's ``reference/lemma-releases.json`` entry.
    fallback: Literal["spacy-list", "backend"] | None = None
    top_n: int = 50_000
    forms_kept: int = 5


class ChecksConfig(Strict):
    """Parameters of the ported review checks (:mod:`frequer.checks`)."""

    review_top_n: int = 10_000
    form_ratio_threshold: float = 100.0
    #: Suffixes tried by the singular/plural check; empty skips it.
    plural_suffixes: list[str] = Field(default_factory=list)
    short_lemma_max_len: int = 2


class SourceConfig(Strict):
    name: str
    #: ``hplt`` = JSONL documents; ``tsv`` = one sentence per line in a column.
    kind: Literal["hplt", "tsv"]
    urls: list[str]
    licence: str
    licence_url: str = ""
    notes: str = ""
    #: Expected sha256 of the *compressed* file per URL, where known.
    sha256: dict[str, str] = Field(default_factory=dict)
    #: ``hplt``: the ``seg_langs`` code to keep (e.g. ``deu_Latn``).
    segment_lang: str = ""
    #: ``tsv``: zero-based column holding the target-language text.
    column: int = 0
    #: ``tsv``: consecutive lines grouped into one pseudo-document (a corpus of
    #: isolated sentences has no document boundaries; dispersion needs some).
    pseudo_doc_lines: int = 50
    #: Raw (pre-hygiene) characters per shard; fixed so shards are reproducible.
    shard_chars: int = 20_000_000
    #: Full-run cap on raw characters read from each URL (None reads to the end).
    max_chars_per_url: int | None = None
    #: Full run: keep every ``stride``-th document (pseudo-document for TSV), so a cap
    #: spreads over the whole file instead of its first crawl.
    stride: int = 1
    #: Weight of this source's frequency in ranking scores (the blend knob).
    weight: float = 1.0
    hygiene: Hygiene | None = None


class PilotConfig(Strict):
    """Caps for ``frequer pilot``: a small slice, never the full corpus."""

    shard_chars: int
    #: Raw characters read from each of the first ``urls`` URLs of a source.
    max_chars_per_url: dict[str, int]
    urls: dict[str, int] = Field(default_factory=dict)


class FormsSource(Strict):
    """How ``frequer forms`` reads one source (see :mod:`frequer.forms_run`)."""

    #: Fraction of ``--tokens`` this source supplies; split evenly over its URLs.
    share: float = 1.0
    #: Keep every ``stride``-th document (pseudo-document for TSV): a stride above 1 reads the
    #: whole file and spreads the sample over it, with no per-URL character cap.
    stride: int = 1
    #: Raw characters read per word token that survives hygiene (calibrated on a slice);
    #: turns a token budget into a per-URL character cap.
    raw_chars_per_token: float = 8.0


class FormsConfig(Strict):
    """The tokenizer-only form inventory: data, never a language branch."""

    #: ``lexicon.models.Script`` value the default-ignore rule checks forms against.
    script: str
    #: ``spacy_blank`` = ``spacy.blank(code).tokenizer``; ``backend`` = the registry backend's tokenize.
    tokenizer: Literal["spacy_blank", "backend"]
    sources: dict[str, FormsSource]


class CoocConfig(Strict):
    """The co-occurrence pass (:mod:`frequer.cooc`, :mod:`frequer.assoc`)."""

    enabled: bool = True
    n_min: int = 2
    n_max: int = 4
    #: Items below this merged count are dropped before scoring (Evert 2005 §4.1:
    #: association scores are unreliable for f < 3-5).
    min_count: int = 5
    #: Shipped table: at most this many rows, the highest ``g2_min`` among the
    #: positively associated (p < 0.001) ones with at least ``ship_min_docs`` documents.
    ship_rows: int = 400_000
    ship_min_docs: int = 3
    #: The labelling queue: this many top combinations not on the unit list.
    queue_rows: int = 2000
    #: ``npmi_min`` floor for the labelling queue (ranked by ``g2_min`` above it).
    queue_min_npmi: float = 0.25
    #: UPOS (a key's majority) that may not open or close a queued n-gram.
    queue_edge_ban: list[str] = Field(default_factory=lambda: ["DET", "CCONJ"])
    #: During ``count``, fold finished shard co-occurrence files into one running
    #: file every this many shards, so disk holds one merged file plus a few shards.
    compact_every: int = 8


class Observed(Strict):
    scope: str
    date: str
    tokens: int
    documents: int
    shards: int
    lines: int
    partial: bool = True


class Manifest(Strict):
    language: LanguageConfig
    hygiene: Hygiene = Field(default_factory=Hygiene)
    #: Number of equal-size corpus parts (hash buckets of documents) dispersion is measured over.
    parts: int = 100
    checks: ChecksConfig = Field(default_factory=ChecksConfig)
    sources: list[SourceConfig]
    pilot: PilotConfig
    forms: FormsConfig | None = None
    cooc: CoocConfig = Field(default_factory=CoocConfig)
    #: Token counts per source once fetched (``frequer sync-manifest``).
    observed: dict[str, list[Observed]] = Field(default_factory=dict)

    def hygiene_for(self, source: SourceConfig) -> Hygiene:
        return source.hygiene or self.hygiene

    def source(self, name: str) -> SourceConfig:
        for source in self.sources:
            if source.name == name:
                return source
        raise KeyError(name)


def manifest_path(lang: str, root: Path = MANIFEST_DIR) -> Path:
    return root / f"{lang}.yaml"


def load_manifest(lang: str, root: Path = MANIFEST_DIR) -> Manifest:
    data = yaml.safe_load(manifest_path(lang, root).read_text(encoding="utf-8"))
    return Manifest.model_validate(data)


OBSERVED_MARKER = "\nobserved:"


def write_observed(lang: str, observed: dict[str, list[Observed]], root: Path = MANIFEST_DIR) -> None:
    """Rewrite only the ``observed:`` tail of a manifest, keeping its comments."""
    path = manifest_path(lang, root)
    text = path.read_text(encoding="utf-8")
    head = text[: text.index(OBSERVED_MARKER)]
    body = {name: [o.model_dump() for o in runs] for name, runs in observed.items()}
    tail = yaml.safe_dump({"observed": body}, sort_keys=True, allow_unicode=True, width=100)
    path.write_text(head + "\n" + tail, encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fp:
        for block in iter(lambda: fp.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()
