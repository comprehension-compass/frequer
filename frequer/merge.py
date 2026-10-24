"""Merge finished shard files into one :class:`Merged`, checking they agree.

Shards counted under a different lemma release, override file, honeyeater
commit or hygiene configuration must not be mixed: the snapshot header records
one of each. The merge is two passes so memory is bounded by the candidate set,
not by every lemma type the corpus holds: pass one tallies raw frequency, pass
two keeps the full detail only for the top ``candidates`` lemmas.
"""

from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from frequer.counts import Merged, iter_counts, merge_shard, read_shard, tally_frequencies, top_candidates


@dataclass
class SourceTotals:
    shards: int = 0
    tokens: int = 0
    docs: int = 0
    lines: int = 0
    raw_chars: int = 0
    dropped: Counter[str] = field(default_factory=Counter)
    config_hash: str = ""


@dataclass
class MergeResult:
    merged: Merged
    runtime: dict[str, Any]
    lang: str
    sources: dict[str, SourceTotals]
    #: Summed stage seconds across shards, and the token total they cover.
    seconds: Counter[str]
    peak_rss_mb: float
    host_tokens: int
    step_mismatch_sentences: int
    sentences: int
    token_provenance: Counter[str]
    override_tokens: int
    override_conflicts: Counter[tuple[str, str, str]]


def merge_counts(counts_dir: Path, parts: int, candidates: int | None) -> MergeResult:
    files = list(iter_counts(counts_dir))
    if not files:
        raise SystemExit(f"no shard counts in {counts_dir}")
    keep: set[str] | None = None
    if candidates:
        keep = top_candidates(tally_frequencies(read_shard(p) for _s, p in files), candidates)
    merged = Merged(parts=parts)
    sources: dict[str, SourceTotals] = {}
    seconds: Counter[str] = Counter()
    provenance: Counter[str] = Counter()
    runtime: dict[str, Any] | None = None
    lang = ""
    peak = 0.0
    host = mismatch = sentences = override_tokens = 0
    conflicts: Counter[tuple[str, str, str]] = Counter()
    for source, path in files:
        shard = read_shard(path)
        if runtime is None:
            runtime, lang = shard["runtime"], shard["lang"]
        elif shard["runtime"] != runtime or shard["lang"] != lang:
            raise SystemExit(f"{path.name}: counted under a different runtime/language than the others")
        totals = sources.setdefault(source, SourceTotals(config_hash=shard["config_hash"]))
        if totals.config_hash != shard["config_hash"]:
            raise SystemExit(f"{path.name}: hygiene/shard configuration differs within source {source}")
        totals.shards += 1
        totals.tokens += shard["tokens"]
        totals.docs += shard["docs"]
        totals.lines += shard["lines"]
        totals.raw_chars += shard["raw_chars"]
        totals.dropped.update(shard["hygiene_dropped"])
        stats = shard["stats"]
        seconds.update(stats["seconds"])
        provenance.update(stats["token_provenance"])
        peak = max(peak, stats["worker_peak_rss_mb"])
        host += stats["host_tokens"]
        mismatch += stats["step_mismatch_sentences"]
        sentences += stats["sentences"]
        override_tokens += stats["override_tokens"]
        for surface, wanted, got, n in stats["override_conflicts"]:
            conflicts[(surface, wanted, got)] += n
        merge_shard(merged, shard, source, keep)
    assert runtime is not None
    return MergeResult(
        merged, runtime, lang, sources, seconds, peak, host, mismatch, sentences, provenance,
        override_tokens, conflicts,
    )


def dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
