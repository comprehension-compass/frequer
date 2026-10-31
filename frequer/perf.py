"""Throughput and memory per stage, from the numbers the shards recorded."""

from __future__ import annotations

from typing import Any

from frequer.merge import MergeResult

#: Stage name -> what it covers. Order is pipeline order.
STAGES = {
    "fetch_decode": "download, decompress, parse (main process)",
    "hygiene": "length/alpha/GAP/dedup filters (main process)",
    "langid": "py3langid (main process)",
    "read_shard": "read the cleaned shard file (worker)",
    "segment": "backend sentence segmentation (worker; German: the full parse)",
    "sentence_stage": "analyse_sentence minus the release: tokenize, candidates, numbers, unit merge (worker)",
    "lemma_step": "the release's lemma + UPOS (model on every sentence) (worker)",
    "units": "the release's unit step: list candidates, spancat, parts list, splitter (worker)",
    "count": "tally lemmas, forms, POS, readings, units (worker)",
    "cooc": "co-occurrence n-grams, pairs, marginals (worker)",
    "cooc_write": "write the sorted co-occurrence file (worker)",
}


def stage_table(result: MergeResult) -> list[dict[str, Any]]:
    """Per stage: core-seconds and counted tokens per core-second."""
    tokens = result.merged.tokens
    rows: list[dict[str, Any]] = []
    for stage, what in STAGES.items():
        secs = result.seconds.get(stage, 0.0)
        if secs <= 0:
            continue
        rows.append({"stage": stage, "what": what, "core_seconds": round(secs, 2),
                     "tokens_per_second": round(tokens / secs)})
    worker = result.seconds.get("total_count_worker", 0.0)
    if worker > 0:
        rows.append({"stage": "worker_total", "what": "everything a worker does per shard",
                     "core_seconds": round(worker, 2), "tokens_per_second": round(tokens / worker)})
    return rows
