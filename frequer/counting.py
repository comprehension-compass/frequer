"""Count one cleaned shard through the runtime into a shard counts file."""

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
from frequer.counts import ShardAccumulator, write_shard
from frequer.runtime import AnalysedSentence, Runtime, StageClock
from frequer.shards import ShardJob
from frequer.units import NoUnits, UnitCounter

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
    )
    _STATE["units"] = NoUnits()


def peak_rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024


def _read_rows(path: Path) -> list[tuple[int, int, str]]:
    rows: list[tuple[int, int, str]] = []
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        for raw in fp:
            doc, part, line = raw.rstrip("\n").split("\t", 2)
            rows.append((int(doc), int(part), line))
    return rows


def _vote_pos(
    acc: ShardAccumulator, lemma: str, i: int, sent: AnalysedSentence, tags: list[str] | None,
    from_model: bool,
) -> None:
    if from_model:
        if tags is not None:
            acc.pos[(lemma, tags[i])] += 1
    elif not sent.host[i]:
        acc.pos[(lemma, sent.pos[i])] += 1


def count_rows(
    rows: list[tuple[int, int, str]],
    runtime: Runtime,
    manifest: Manifest,
    units: UnitCounter,
    clock: StageClock,
) -> tuple[ShardAccumulator, dict[str, Any]]:
    """Run ``rows`` (doc, part, line) through the runtime and tally them."""
    lang = manifest.language
    acc = ShardAccumulator(manifest.parts)
    prov: Counter[str] = Counter()
    sentences = host_tokens = mismatches = override_tokens = 0
    conflicts: Counter[tuple[str, str, str]] = Counter()
    from_model = lang.pos_source == "model"
    for _doc, group in groupby(rows, key=lambda r: r[0]):
        batch = list(group)
        part = batch[0][1]
        local: Counter[str] = Counter()
        doc_units: set[str] = set()
        for _d, _p, line in batch:
            for sent in runtime.sentences(line, clock):
                sentences += 1
                mismatches += sent.mismatch
                tags: list[str] | None = None
                if from_model and sentences % lang.pos_sample_every == 0:
                    t0 = time.perf_counter()
                    tags = runtime.tag(sent.words, sent.spaces)
                    clock("pos_model", time.perf_counter() - t0)
                t0 = time.perf_counter()
                for i, word in enumerate(sent.words):
                    key = None if sent.punct[i] else runtime.key(sent.lemmas[i])
                    if key is None:
                        continue
                    lemma = key
                    if sent.host[i]:
                        host_tokens += 1
                        if lang.host_tokens == "skip":
                            continue
                    prov[sent.provenance[i]] += 1
                    wanted = runtime.overrides.get(word.lower())
                    if wanted is not None and not sent.host[i]:
                        override_tokens += 1
                        if wanted != lemma:
                            conflicts[(word.lower(), wanted, lemma)] += 1
                    local[lemma] += 1
                    if not sent.host[i]:
                        acc.forms[(lemma, word.lower() if lang.lowercase_forms else word)] += 1
                    _vote_pos(acc, lemma, i, sent, tags, from_model)
                    cand = sent.candidates[i]
                    if lang.readings and cand is not None and cand.lemma == lemma and cand.reading:
                        acc.readings[(lemma, cand.reading)] += 1
                        source = cand.reading_source
                        acc.reading_source.setdefault(
                            (lemma, cand.reading), str(getattr(source, "value", source))
                        )
                for unit in units.units(sent):
                    acc.units.setdefault(unit, [0, 0])[0] += 1
                    doc_units.add(unit)
                clock("count", time.perf_counter() - t0)
        for unit in doc_units:
            acc.units[unit][1] += 1
        acc.add_document(part, local)
    stats = {
        "sentences": sentences, "host_tokens": host_tokens, "step_mismatch_sentences": mismatches,
        "token_provenance": dict(prov),
        # Where the override file names a lemma the lemma step did not emit (the step
        # prefers its list over the backend's overridden lemma): [surface, override, step, n].
        "override_tokens": override_tokens,
        "override_conflicts": [[*k, n] for k, n in conflicts.most_common(200)],
    }
    return acc, stats


def count_shard(job: ShardJob) -> dict[str, Any]:
    """Worker entry point: count, write the counts file, delete the shard file."""
    runtime: Runtime = _STATE["runtime"]
    manifest: Manifest = _STATE["manifest"]
    clock = StageClock()
    t_start = time.perf_counter()
    t0 = time.perf_counter()
    rows = _read_rows(job.path)
    clock("read_shard", time.perf_counter() - t0)
    acc, stats = count_rows(rows, runtime, manifest, _STATE["units"], clock)
    body = acc.to_dict()
    meta = {
        "frequer": __version__, "lang": manifest.language.code, "config_hash": job.config,
        "runtime": asdict(runtime.info),
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
