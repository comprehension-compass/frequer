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
    "segment": "backend sentence segmentation (worker)",
    "tokenize": "backend tokenization (worker)",
    "backend_lemma": "backend lemmatize + override file (worker)",
    "lemma_step": "LemmaRelease.lemmatise, incl. model where needed (worker)",
    "pos_model": "model POS on sampled sentences (worker)",
    "count": "tally lemmas, forms, POS, readings (worker)",
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
