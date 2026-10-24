"""Per-shard counts and the merge of many shards: the pure cores of the build.

A shard file holds, for every lemma, its frequency, the number of documents it
occurs in, its surface forms, its POS votes and its per-part counts (a *part*
is a hash bucket of documents, the unit dispersion is measured over). Merging
only adds, so shards can be counted in any order and a lost one is recounted
alone. Nothing here touches the runtime or the network.
"""

from __future__ import annotations

import gzip
import json
from collections import Counter
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

FORMAT = 1


class ShardAccumulator:
    """The worker's running totals for one shard (flat counters, cheap per token)."""

    def __init__(self, parts: int) -> None:
        self.parts = parts
        self.tokens = 0
        self.docs = 0
        self.part_tokens = [0] * parts
        self.freq: Counter[str] = Counter()
        self.df: Counter[str] = Counter()
        self.forms: Counter[tuple[str, str]] = Counter()
        self.pos: Counter[tuple[str, str]] = Counter()
        self.part: Counter[tuple[str, int]] = Counter()
        self.readings: Counter[tuple[str, str]] = Counter()
        self.reading_source: dict[tuple[str, str], str] = {}
        #: Hook for unit counts (reflexive/separable verbs, set phrases): unit key -> [frequency, documents].
        self.units: dict[str, list[int]] = {}

    def add_document(self, part: int, lemma_counts: Counter[str]) -> None:
        """Fold one document's lemma counts in: frequency, document frequency, part."""
        self.docs += 1
        self.part_tokens[part] += sum(lemma_counts.values())
        for lemma, n in lemma_counts.items():
            self.freq[lemma] += n
            self.df[lemma] += 1
            self.part[(lemma, part)] += n

    def to_dict(self) -> dict[str, Any]:
        entries: dict[str, dict[str, Any]] = {
            lemma: {"f": f, "d": self.df[lemma], "p": {}, "w": {}, "s": {}}
            for lemma, f in self.freq.items()
        }
        for (lemma, pos), n in self.pos.items():
            entries[lemma]["p"][pos] = n
        for (lemma, form), n in self.forms.items():
            entries[lemma]["w"][form] = n
        for (lemma, part), n in self.part.items():
            entries[lemma]["s"][str(part)] = n
        for (lemma, reading), n in self.readings.items():
            entry = entries[lemma]
            entry.setdefault("r", {})[reading] = n
            entry.setdefault("rs", {})[reading] = self.reading_source[(lemma, reading)]
        return {
            "tokens": sum(self.freq.values()),
            "docs": self.docs,
            "part_tokens": self.part_tokens,
            "lemmas": entries,
            "units": self.units,
        }


def write_shard(path: Path, meta: dict[str, Any], body: dict[str, Any]) -> None:
    tmp = path.with_suffix(".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=3) as fp:
        json.dump({"format": FORMAT, **meta, **body}, fp, ensure_ascii=False, separators=(",", ":"))
    tmp.replace(path)


def read_shard(path: Path) -> dict[str, Any]:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        data: dict[str, Any] = json.load(fp)
    if data.get("format") != FORMAT:
        raise ValueError(f"{path}: shard format {data.get('format')} != {FORMAT}")
    return data


@dataclass
class LemmaStats:
    freq: int = 0
    df: int = 0
    by_source: Counter[str] = field(default_factory=Counter)
    pos: Counter[str] = field(default_factory=Counter)
    forms: Counter[str] = field(default_factory=Counter)
    parts: Counter[int] = field(default_factory=Counter)
    readings: Counter[str] = field(default_factory=Counter)
    reading_source: dict[str, str] = field(default_factory=dict)


@dataclass
class Merged:
    parts: int
    tokens: int = 0
    docs: int = 0
    part_tokens: list[int] = field(default_factory=list)
    tokens_by_source: Counter[str] = field(default_factory=Counter)
    docs_by_source: Counter[str] = field(default_factory=Counter)
    shards: int = 0
    lemmas: dict[str, LemmaStats] = field(default_factory=dict)
    units: dict[str, list[int]] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.part_tokens:
            self.part_tokens = [0] * self.parts


def merge_shard(
    merged: Merged, shard: dict[str, Any], source: str, keep: set[str] | None = None
) -> None:
    """Add one shard into ``merged``; with ``keep``, only those lemmas' detail.

    Totals (tokens, documents, part sizes) always include every lemma, so rates
    and dispersion stay correct for the kept ones.
    """
    if len(shard["part_tokens"]) != merged.parts:
        raise ValueError("shard was counted with a different number of parts")
    merged.shards += 1
    merged.tokens += shard["tokens"]
    merged.docs += shard["docs"]
    merged.tokens_by_source[source] += shard["tokens"]
    merged.docs_by_source[source] += shard["docs"]
    for i, n in enumerate(shard["part_tokens"]):
        merged.part_tokens[i] += n
    for lemma, entry in shard["lemmas"].items():
        if keep is not None and lemma not in keep:
            continue
        stats = merged.lemmas.get(lemma)
        if stats is None:
            stats = merged.lemmas[lemma] = LemmaStats()
        stats.freq += entry["f"]
        stats.df += entry["d"]
        stats.by_source[source] += entry["f"]
        stats.pos.update(entry["p"])
        stats.forms.update(entry["w"])
        for part, n in entry["s"].items():
            stats.parts[int(part)] += n
        for reading, n in entry.get("r", {}).items():
            stats.readings[reading] += n
            stats.reading_source.setdefault(reading, entry["rs"][reading])
    for unit, (f, d) in shard.get("units", {}).items():
        acc = merged.units.setdefault(unit, [0, 0])
        acc[0] += f
        acc[1] += d


def tally_frequencies(shards: Iterable[dict[str, Any]]) -> Counter[str]:
    """Pass one of the merge: raw frequency per lemma, to pick the candidates cheaply."""
    totals: Counter[str] = Counter()
    for shard in shards:
        for lemma, entry in shard["lemmas"].items():
            totals[lemma] += entry["f"]
    return totals


def top_candidates(totals: Counter[str], n: int) -> set[str]:
    return {lemma for lemma, _ in totals.most_common(n)}


def iter_counts(counts_dir: Path) -> Iterator[tuple[str, Path]]:
    """``(source, path)`` of every finished shard file, in name order."""
    for path in sorted(counts_dir.glob("*.json.gz")):
        yield path.name.split(".", 1)[0], path
