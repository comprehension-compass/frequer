"""Count one cleaned shard through the runtime into a counts file and a co-occurrence file."""

from __future__ import annotations

import gzip
import resource
import time
from collections import Counter
from dataclasses import asdict
from itertools import groupby
from pathlib import Path
from typing import Any

from frequer import __version__
from frequer.config import Manifest
from frequer.cooc import CoocAccumulator
from frequer.counts import ShardAccumulator, write_shard
from frequer.runtime import Runtime, StageClock
from frequer.shards import ShardJob

_STATE: dict[str, Any] = {}


def init_worker(lang: str, manifest_root: str | None, lemma_dir: str | None,
                wheel: str | None) -> None:
    """Per-process setup: load the runtime once, reuse it for every shard."""
    from frequer.config import MANIFEST_DIR, load_manifest

    manifest = load_manifest(lang, Path(manifest_root) if manifest_root else MANIFEST_DIR)
    _STATE["manifest"] = manifest
    _STATE["runtime"] = Runtime(
        manifest.language,
        lemma_dir=Path(lemma_dir) if lemma_dir else None,
        wheel=Path(wheel) if wheel else None,
        fallback=manifest.language.fallback,
    )


def peak_rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def _read_rows(path: Path) -> list[tuple[int, int, str]]:
    rows: list[tuple[int, int, str]] = []
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        for raw in fp:
            doc, part, line = raw.rstrip("\n").split("\t", 2)
            rows.append((int(doc), int(part), line))
    return rows


def count_rows(
    rows: list[tuple[int, int, str]],
    runtime: Runtime,
    manifest: Manifest,
    clock: StageClock,
    cooc: CoocAccumulator | None = None,
) -> tuple[ShardAccumulator, dict[str, Any]]:
    """Run ``rows`` (doc, part, line) through the runtime and tally them."""
    lang = manifest.language
    acc = ShardAccumulator(manifest.parts)
    kinds: Counter[str] = Counter()
    sentences = host_tokens = skipped = 0
    for _doc, group in groupby(rows, key=lambda r: r[0]):
        batch = list(group)
        part = batch[0][1]
        local: Counter[str] = Counter()
        doc_units: set[str] = set()
        for _d, _p, line in batch:
            for sent in runtime.sentences(line, clock):
                sentences += 1
                t0 = time.perf_counter()
                for occ in sent.occurrences:
                    if occ.host:
                        host_tokens += 1
                        if lang.host_tokens == "skip":
                            continue
                    key = runtime.key(occ.lemma, occ.kind)
                    if key is None:
                        skipped += 1
                        continue
                    kinds[occ.kind] += 1
                    local[key] += 1
                    acc.kinds[(key, occ.kind)] += 1
                    acc.forms[(key, occ.surface.lower() if lang.lowercase_forms else occ.surface)] += 1
                    acc.pos[(key, occ.pos)] += 1
                    if lang.readings and occ.reading:
                        acc.readings[(key, occ.reading)] += 1
                        acc.reading_source.setdefault((key, occ.reading), occ.reading_source or "dictionary")
                for unit in sent.units or ():
                    name = f"{unit.type}\t{unit.lemma}"
                    acc.units.setdefault(name, [0, 0])[0] += 1
                    doc_units.add(name)
                clock("count", time.perf_counter() - t0)
                if cooc is not None:
                    t0 = time.perf_counter()
                    cooc.add_sentence(runtime.cooc_keys(sent), sent.upos, runtime.pair_spans(sent))
                    clock("cooc", time.perf_counter() - t0)
        for unit in doc_units:
            acc.units[unit][1] += 1
        acc.add_document(part, local)
        if cooc is not None:
            cooc.end_document()
    stats = {
        "sentences": sentences, "host_tokens": host_tokens, "occurrence_kinds": dict(kinds),
        "uncounted_occurrences": skipped,
    }
    return acc, stats


def count_shard(job: ShardJob) -> dict[str, Any]:
    """Worker entry point: count, write the counts and co-occurrence files, delete the shard file."""
    runtime: Runtime = _STATE["runtime"]
    manifest: Manifest = _STATE["manifest"]
    clock = StageClock()
    t_start = time.perf_counter()
    t0 = time.perf_counter()
    rows = _read_rows(job.path)
    clock("read_shard", time.perf_counter() - t0)
    cfg = manifest.cooc
    cooc = CoocAccumulator(cfg.n_min, cfg.n_max) if cfg.enabled else None
    acc, stats = count_rows(rows, runtime, manifest, clock, cooc)
    body = acc.to_dict()
    shard_id = f"{job.source}.{job.url_index:02d}.{job.shard_index:05d}"
    if cooc is not None:
        t0 = time.perf_counter()
        cooc.write(job.cooc_path, {"shard": shard_id, "lang": manifest.language.code,
                                   "lemma_sha256": runtime.info.lemma_sha256})
        clock("cooc_write", time.perf_counter() - t0)
        stats["cooc_items"] = len(cooc.f)
    meta = {
        "frequer": __version__, "lang": manifest.language.code, "config_hash": job.config,
        "runtime": asdict(runtime.info), "shard": shard_id,
        "source": job.source, "url_index": job.url_index, "shard_index": job.shard_index,
        "closed_by": job.closed_by, "raw_chars": job.raw_chars, "lines": job.lines,
        "hygiene_dropped": job.dropped,
        "stats": {**stats, "seconds": {**job.seconds, **clock.seconds,
                                       "total_count_worker": time.perf_counter() - t_start},
                  "worker_peak_rss_mb": peak_rss_mb()},
    }
    write_shard(job.counts_path, meta, body)
    job.path.unlink(missing_ok=True)
    return {"source": job.source, "shard": f"{job.url_index}.{job.shard_index}", "tokens": body["tokens"],
            "seconds": time.perf_counter() - t_start, "rss_mb": peak_rss_mb()}
