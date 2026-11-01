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
import subprocess
import sys
import time
from collections.abc import Callable, Iterable, Iterator
from concurrent.futures import FIRST_COMPLETED, Future, ProcessPoolExecutor, wait
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any

from frequer import combos, counting
from frequer.config import Manifest
from frequer.hygiene import make_classifier
from frequer.shards import Limits, ShardJob, produce_shards

#: Shards a worker counts before it is replaced by a fresh process (bounded memory on long runs).
RECYCLE_AFTER = 12


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


def parse_part(text: str) -> tuple[int, int]:
    """``i/N`` -> ``(i, N)``: this machine counts the URLs ``k`` with ``k % N == i`` of every
    source, and part 0 also counts every ``first`` source. Disjoint, deterministic, and each
    shard's name (source, URL, shard index) is the same whichever machine cuts it."""
    i, n = (int(x) for x in text.split("/"))
    if not 0 <= i < n:
        raise SystemExit(f"--part {text}: need 0 <= i < N")
    return i, n


def _url_indices(urls: list[str], limits: Limits) -> list[int]:
    count = min(len(urls), limits.max_urls) if limits.max_urls else len(urls)
    return [k for k in range(count) if limits.url_indices is None or k in limits.url_indices]


def _round_robin(streams: Iterable[Iterator[ShardJob]]) -> Iterator[ShardJob]:
    """One shard from each URL in turn, so a run stopped early holds every URL's share.

    Each URL's stream stays open between its turns (a dropped connection resumes with
    a ``Range`` request, :class:`frequer.sources.HttpStream`).
    """
    active = list(streams)
    while active:
        still: list[Iterator[ShardJob]] = []
        for stream in active:
            job = next(stream, None)
            if job is not None:
                yield job
                still.append(stream)
        active = still


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
    checkpoints_out: Path | None = None,
    part: tuple[int, int] | None = None,
    log: Callable[[str], None] = print,
) -> dict[str, Any]:
    """Count every unfinished shard; returns a run summary (also written to ``run-<ts>.json``)."""
    dirs.make()
    lang = manifest.language.code
    init_args = (lang, str(manifest_root) if manifest_root else None,
                 str(lemma_dir) if lemma_dir else None, str(wheel) if wheel else None, manifest.cooc.enabled)
    classify = make_classifier()
    started = time.time()
    results: list[dict[str, Any]] = []
    url_stats: dict[str, dict[str, object]] = {}
    pending: set[Future[dict[str, Any]]] = set()
    stopped = False

    def checkpoint() -> bool:
        """Take the due convergence checkpoints in a child process; True when the list has converged."""
        if checkpoints_out is None:
            return False
        cmd = [sys.executable, "-m", "frequer", "checkpoint", lang, "--data-dir", str(dirs.root.parent),
               "--out-dir", str(checkpoints_out)]
        if lemma_dir:
            cmd += ["--lemma-dir", str(lemma_dir)]
        if wheel:
            cmd += ["--wheel", str(wheel)]
        done = subprocess.run(cmd, capture_output=True, text=True)
        if done.returncode != 0:
            log(f"checkpoint failed (counting goes on): {done.stderr[-2000:]}")
            return False
        for line in done.stdout.splitlines():
            if line.startswith("checkpoint"):
                log(line)
        state = json.loads((checkpoints_out / "convergence.json").read_text(encoding="utf-8")) \
            if (checkpoints_out / "convergence.json").exists() else {}
        return bool(state.get("decision") == "stop")

    def drain(block: bool) -> None:
        nonlocal pending, stopped
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
        if done and not stopped and checkpoint():
            stopped = True
            log("converged: stopping (build the final snapshot from what was counted)")

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
            # A worker's spaCy string stores and memos grow with every shard: start a fresh one now and then.
            max_tasks_per_child=RECYCLE_AFTER,
        )
    else:
        counting.init_worker(*init_args)
    try:
        # Small ``first`` sources (Tatoeba) before the web, so every checkpoint holds them whole.
        for source in sorted(manifest.sources, key=lambda s: not s.first):
            if stopped:
                break
            if sources and source.name not in sources:
                continue
            if part is not None and source.first and part[0] != 0:
                continue  # the first sources are part 0's (the coordinator's)
            if shard_chars:
                source = source.model_copy(update={"shard_chars": shard_chars})
            lim = limits(source.name)
            jobs = _round_robin(
                produce_shards(
                    lang=lang, source=source, hygiene=manifest.hygiene_for(source),
                    parts=manifest.parts, work_dir=dirs.work, counts_dir=dirs.counts,
                    limits=replace(lim, url_indices=(k,)), classify=classify, url_stats=url_stats,
                )
                for k in _url_indices(source.urls, lim)
                if part is None or source.first or k % part[1] == part[0]
            )
            for job in jobs:
                if stopped:
                    break
                log(f"cut {job.source} {job.url_index}.{job.shard_index}: {job.lines:,} lines, "
                    f"{job.docs:,} docs, {job.raw_chars / 1e6:.1f}M raw chars, dropped {job.dropped}")
                if pool is None:
                    results.append(counting.count_shard(job))
                    continue
                pending.add(pool.submit(counting.count_shard, job))
                while len(pending) > workers and not stopped:
                    drain(block=True)
        while pending and not stopped:
            drain(block=True)
        fold(1)
    finally:
        if pool is not None:
            if stopped:
                # Converged: shards still in flight are not needed; their workers are stopped.
                procs = list(getattr(pool, "_processes", {}).values())
                pool.shutdown(wait=False, cancel_futures=True)
                for proc in procs:
                    proc.terminate()
            else:
                pool.shutdown(wait=True, cancel_futures=True)
    summary = {
        "language": lang, "workers": workers, "started": started, "wall_seconds": time.time() - started,
        "main_peak_rss_mb": counting.peak_rss_mb(), "shards_counted": len(results), "urls": url_stats,
        "stopped_by": "convergence" if stopped else None,
    }
    (dirs.root / f"run-{int(started)}.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    return summary

