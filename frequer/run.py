"""Orchestrate fetch -> hygiene -> shard -> count across worker processes.

The main process streams each source and cuts shards (one core: decompress,
hygiene, langid); workers each load the runtime once and count shards one at a
time. At most ``workers + 1`` cut shards wait on disk, so disk use stays at a
few shard files regardless of corpus size. A shard whose counts file exists is
skipped; rerun the same command to resume.
"""

from __future__ import annotations

import json
import multiprocessing
import time
from collections.abc import Callable
from concurrent.futures import FIRST_COMPLETED, Future, ProcessPoolExecutor, wait
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from frequer import combos, counting
from frequer.config import Manifest
from frequer.hygiene import make_classifier
from frequer.shards import Limits, produce_shards


@dataclass(frozen=True)
class RunDirs:
    root: Path

    @property
    def work(self) -> Path:
        return self.root / "work"

    @property
    def counts(self) -> Path:
        return self.root / "counts"

    def make(self) -> None:
        self.work.mkdir(parents=True, exist_ok=True)
        self.counts.mkdir(parents=True, exist_ok=True)


def count_language(
    manifest: Manifest,
    dirs: RunDirs,
    *,
    workers: int,
    limits: Callable[[str], Limits],
    shard_chars: int | None = None,
    sources: list[str] | None = None,
    manifest_root: Path | None = None,
    lemma_dir: Path | None = None,
    wheel: Path | None = None,
    log: Callable[[str], None] = print,
) -> dict[str, Any]:
    """Count every unfinished shard; returns a run summary (also written to ``run-<ts>.json``)."""
    dirs.make()
    lang = manifest.language.code
    init_args = (lang, str(manifest_root) if manifest_root else None,
                 str(lemma_dir) if lemma_dir else None, str(wheel) if wheel else None)
    classify = make_classifier()
    started = time.time()
    results: list[dict[str, Any]] = []
    url_stats: dict[str, dict[str, object]] = {}
    pending: set[Future[dict[str, Any]]] = set()

    def drain(block: bool) -> None:
        nonlocal pending
        if not pending:
            return
        done, pending = wait(pending, return_when=FIRST_COMPLETED,
                             timeout=None if block else 0)
        for fut in done:
            res = fut.result()
            results.append(res)
            log(f"counted {res['source']} {res['shard']}: {res['tokens']:,} tokens in "
                f"{res['seconds']:.0f}s (worker peak {res['rss_mb']:.0f} MB)")
        fold(manifest.cooc.compact_every)

    def fold(at_least: int) -> None:
        if manifest.cooc.enabled:
            t0 = time.time()
            folded = combos.compact(dirs.counts, at_least=at_least)
            if folded:
                log(f"folded {folded} co-occurrence shard files into {combos.ACC} in {time.time() - t0:.0f}s")

    pool: ProcessPoolExecutor | None = None
    if workers > 0:
        pool = ProcessPoolExecutor(
            max_workers=workers, mp_context=multiprocessing.get_context("spawn"),
            initializer=counting.init_worker, initargs=init_args,
        )
    else:
        counting.init_worker(*init_args)
    try:
        for source in manifest.sources:
            if sources and source.name not in sources:
                continue
            if shard_chars:
                source = source.model_copy(update={"shard_chars": shard_chars})
            jobs = produce_shards(
                lang=lang, source=source, hygiene=manifest.hygiene_for(source),
                parts=manifest.parts, work_dir=dirs.work, counts_dir=dirs.counts,
                limits=limits(source.name), classify=classify, url_stats=url_stats,
            )
            for job in jobs:
                log(f"cut {job.source} {job.url_index}.{job.shard_index}: {job.lines:,} lines, "
                    f"{job.docs:,} docs, {job.raw_chars / 1e6:.1f}M raw chars, dropped {job.dropped}")
                if pool is None:
                    results.append(counting.count_shard(job))
                    continue
                pending.add(pool.submit(counting.count_shard, job))
                while len(pending) > workers:
                    drain(block=True)
        while pending:
            drain(block=True)
        fold(1)
    finally:
        if pool is not None:
            pool.shutdown(wait=True, cancel_futures=True)
    summary = {
        "language": lang, "workers": workers, "started": started, "wall_seconds": time.time() - started,
        "main_peak_rss_mb": counting.peak_rss_mb(), "shards_counted": len(results), "urls": url_stats,
    }
    (dirs.root / f"run-{int(started)}.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    return summary

