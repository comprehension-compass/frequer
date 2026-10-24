"""Merging shard counts is addition: any split of the documents gives the same totals."""

from __future__ import annotations

from collections import Counter
from typing import Any

import pytest

from frequer.counts import Merged, ShardAccumulator, merge_shard, tally_frequencies, top_candidates

PARTS = 4
# (part, {lemma: count}) per document.
DOCS: list[tuple[int, dict[str, int]]] = [
    (0, {"casa": 3, "ser": 5}),
    (1, {"casa": 1, "perro": 2}),
    (1, {"ser": 2}),
    (3, {"casa": 2, "perro": 1, "ser": 1}),
    (2, {"raro": 1}),
]


def shard_of(docs: list[tuple[int, dict[str, int]]]) -> dict[str, Any]:
    acc = ShardAccumulator(PARTS)
    for part, counts in docs:
        acc.add_document(part, Counter(counts))
        for lemma, n in counts.items():
            acc.forms[(lemma, lemma.upper())] += n
            acc.pos[(lemma, "NOUN")] += n
    if any("casa" in counts for _, counts in docs):
        acc.readings[("casa", "かさ")] += 1
        acc.reading_source[("casa", "かさ")] = "curated"
    return acc.to_dict()


def merged_of(*shards: dict[str, Any], keep: set[str] | None = None) -> Merged:
    merged = Merged(parts=PARTS)
    for i, shard in enumerate(shards):
        merge_shard(merged, shard, "web" if i % 2 == 0 else "chat", keep)
    return merged


def test_any_split_merges_to_the_same_counts() -> None:
    whole = merged_of(shard_of(DOCS))
    split = merged_of(shard_of(DOCS[:2]), shard_of(DOCS[2:4]), shard_of(DOCS[4:]))
    assert split.tokens == whole.tokens == 18
    assert split.docs == whole.docs == 5
    assert split.part_tokens == whole.part_tokens == [8, 5, 1, 4]
    for lemma, stats in whole.lemmas.items():
        other = split.lemmas[lemma]
        assert (other.freq, other.df, dict(other.parts), dict(other.forms)) == (
            stats.freq, stats.df, dict(stats.parts), dict(stats.forms))
    assert whole.lemmas["casa"].freq == 6
    assert whole.lemmas["casa"].df == 3  # documents, not shards
    assert dict(whole.lemmas["casa"].parts) == {0: 3, 1: 1, 3: 2}


def test_source_attribution_follows_the_shard() -> None:
    merged = merged_of(shard_of(DOCS[:3]), shard_of(DOCS[3:]))
    assert merged.lemmas["ser"].by_source == Counter({"web": 7, "chat": 1})
    assert merged.tokens_by_source == Counter({"web": 13, "chat": 4 + 1})


def test_keep_limits_detail_but_not_totals() -> None:
    merged = merged_of(shard_of(DOCS), keep={"casa"})
    assert set(merged.lemmas) == {"casa"}
    assert merged.tokens == 18
    assert merged.part_tokens == [8, 5, 1, 4]


def test_readings_and_their_source_survive_the_merge() -> None:
    merged = merged_of(shard_of(DOCS), shard_of(DOCS))
    assert merged.lemmas["casa"].readings["かさ"] == 2
    assert merged.lemmas["casa"].reading_source["かさ"] == "curated"


def test_candidate_selection_takes_the_most_frequent() -> None:
    totals = tally_frequencies([shard_of(DOCS)])
    assert top_candidates(totals, 2) == {"ser", "casa"}


def test_shards_with_different_part_counts_are_refused() -> None:
    acc = ShardAccumulator(PARTS + 1)
    with pytest.raises(ValueError, match="parts"):
        merge_shard(Merged(parts=PARTS), acc.to_dict(), "web")
