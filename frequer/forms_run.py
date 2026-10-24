"""``frequer forms``: stream the sources, clean, drop repeated lines, tokenize, tally forms.

Three stages, each resumable per shard, with the worker count never above ``--workers``:

1. **Fetch.** One worker per (source, URL) streams it through the shared fetch, hygiene (line
   length, alphabetic ratio, stripped-link gap, py3langid per line) and shard code, and keeps the
   cleaned shard (a few MB gzipped; the raw stream is never stored). Lines language ID rejected
   are kept beside it, only to measure what the filter removed.
2. **Repeated lines.** Every shard's normalised line keys are collected; a key seen in three or
   more different documents is boilerplate (:func:`frequer.forms.repeated_keys`).
3. **Tokenize.** Workers tokenize each shard minus the repeated lines and write its forms.

The merge then writes ``forms-<lang>.tsv`` with a JSON header.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import multiprocessing
import shutil
import time
from collections import Counter
from collections.abc import Callable, Iterator
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from itertools import groupby
from pathlib import Path
from typing import Any

import numpy as np

from frequer import __version__
from frequer.config import MANIFEST_DIR, Manifest, load_manifest
from frequer.forms import (
    REPEAT_DOCS,
    U64,
    ShardForms,
    Tokenize,
    make_tokenizer,
    merge_forms,
    read_forms_meta,
    repeated_keys,
    site_tag,
    write_forms,
    write_forms_tsv,
)
from frequer.hygiene import make_classifier, near_key
from frequer.shards import CutMode, Limits, marker_path, produce_shards

#: Raw characters per shard in the inventory: small, so a crash costs little and resume is fine-grained.
SHARD_CHARS = 10_000_000


@dataclass(frozen=True)
class Dirs:
    root: Path

    @property
    def shards(self) -> Path:
        return self.root / "shards"

    @property
    def counts(self) -> Path:
        return self.root / "counts"

    @property
    def work(self) -> Path:
        return self.root / "work"

    def make(self) -> None:
        for d in (self.shards, self.counts, self.work):
            d.mkdir(parents=True, exist_ok=True)


@dataclass(frozen=True)
class UrlTask:
    lang: str
    source: str
    url_index: int
    cap: int | None
    stride: int
    root: str
    manifest_root: str | None


def plan_tasks(manifest: Manifest, tokens: int, root: Path, manifest_root: Path | None) -> list[UrlTask]:
    """One task per source URL. A strided source reads its whole file; the others get a character
    cap per URL: its share of the token budget, split evenly, times the calibrated chars per token."""
    forms = manifest.forms
    if forms is None:
        raise SystemExit(f"{manifest.language.code}: the manifest has no forms: block")
    tasks: list[UrlTask] = []
    for source in manifest.sources:
        cfg = forms.sources.get(source.name)
        if cfg is None:
            continue
        cap = None if cfg.stride > 1 else int(tokens * cfg.share / len(source.urls) * cfg.raw_chars_per_token)
        tasks += [
            UrlTask(manifest.language.code, source.name, i, cap, cfg.stride, str(root),
                    str(manifest_root) if manifest_root else None)
            for i in range(len(source.urls))
        ]
    return tasks


def fetch_url(task: UrlTask) -> dict[str, Any]:
    """Worker: stream one URL into cleaned inventory shards (skipping finished ones)."""
    manifest = load_manifest(task.lang, Path(task.manifest_root) if task.manifest_root else MANIFEST_DIR)
    dirs = Dirs(Path(task.root))
    source = manifest.source(task.source).model_copy(
        update={"shard_chars": SHARD_CHARS, "max_chars_per_url": task.cap}
    )
    mode = CutMode(dedup=False, keep_dir=dirs.shards, tag=lambda d: site_tag(d.site or d.doc_id))
    stats: dict[str, dict[str, object]] = {}
    t0 = time.time()
    for job in produce_shards(
        lang=task.lang, source=source, hygiene=manifest.hygiene_for(source), parts=manifest.parts,
        work_dir=dirs.work, counts_dir=dirs.counts, classify=make_classifier(), url_stats=stats,
        limits=Limits(max_chars=task.cap, url_indices=(task.url_index,), stride=task.stride), mode=mode,
    ):
        print(f"cut {job.source}.{job.url_index:02d}.{job.shard_index:05d}: {job.lines:,} lines, "
              f"{job.docs:,} docs, {job.raw_chars / 1e6:.1f}M raw chars, rejected {job.rejected:,}, "
              f"dropped {job.dropped}", flush=True)
    return {"task": f"{task.source}.{task.url_index:02d}", "seconds": time.time() - t0}


# -- stage 2 --------------------------------------------------------------------------------------


def read_rows(path: Path) -> Iterator[tuple[int, int, str]]:
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        for raw in fp:
            doc, tag, line = raw.rstrip("\n").split("\t", 2)
            yield int(doc), int(tag), line


def shard_paths(shards: Path) -> list[Path]:
    return sorted(p for p in shards.glob("*.tsv.gz") if not p.name.endswith(".rej.tsv.gz"))


def shard_keys(job: tuple[Path, int]) -> tuple[U64, U64]:
    """Worker: (line keys, global document ids) of one shard; ``ordinal`` makes ids unique across shards."""
    path, ordinal = job
    keys: list[int] = []
    docs: list[int] = []
    for doc, _tag, line in read_rows(path):
        keys.append(near_key(line))
        docs.append((ordinal << 32) | doc)
    return np.array(keys, dtype=np.uint64), np.array(docs, dtype=np.uint64)


def find_repeats(paths: list[Path], pool: ProcessPoolExecutor) -> U64:
    parts = list(pool.map(shard_keys, [(p, i) for i, p in enumerate(paths)]))
    if not parts:
        return np.empty(0, dtype=np.uint64)
    return repeated_keys(np.concatenate([k for k, _ in parts]), np.concatenate([d for _, d in parts]))


# -- stage 3 --------------------------------------------------------------------------------------

_STATE: dict[str, Any] = {}


def init_counter(lang: str, manifest_root: str | None, repeats_path: str) -> None:
    manifest = load_manifest(lang, Path(manifest_root) if manifest_root else MANIFEST_DIR)
    _STATE["tokenize"] = make_tokenizer(manifest)
    _STATE["repeats"] = frozenset(int(k) for k in np.load(repeats_path))
    _STATE["repeat_sha"] = hashlib.sha256(Path(repeats_path).read_bytes()).hexdigest()[:16]


def count_one(job: tuple[Path, Path]) -> dict[str, Any]:
    """Worker: tokenize one shard minus its repeated lines; write its forms and what was removed."""
    path, counts_dir = job
    tokenize: Tokenize = _STATE["tokenize"]
    repeats: frozenset[int] = _STATE["repeats"]
    stem = path.name.removesuffix(".tsv.gz")
    t0 = time.time()
    forms = ShardForms()
    removed_repeat: Counter[str] = Counter()
    removed_langid: Counter[str] = Counter()
    lines = repeat_lines = docs = 0
    for _doc, group in groupby(read_rows(path), key=lambda r: r[0]):
        batch = list(group)
        site = batch[0][1]
        kept: list[str] = []
        for _d, _s, line in batch:
            if near_key(line) in repeats:
                repeat_lines += 1
                removed_repeat.update(tokenize(line))
            else:
                kept.extend(tokenize(line))
                lines += 1
        if kept:
            forms.add_document(site, kept)
            docs += 1
    rej = path.with_name(stem + ".rej.tsv.gz")
    rejected_lines = 0
    for _doc, _s, line in read_rows(rej):
        rejected_lines += 1
        removed_langid.update(tokenize(line))
    source_meta = json.loads(path.with_name(stem + ".meta.json").read_text(encoding="utf-8"))
    meta = {
        "shard": stem, "source": source_meta["source"], "tokens": sum(forms.counts.values()), "forms": len(forms.counts),
        "docs": docs, "lines": lines, "repeat_lines": repeat_lines, "langid_lines": rejected_lines,
        "raw_chars": source_meta["raw_chars"], "dropped": source_meta["dropped"],
        "repeat_sha": _STATE["repeat_sha"], "seconds": time.time() - t0,
    }
    removed = counts_dir / f"{stem}.removed.json.gz"
    with gzip.open(removed, "wt", encoding="utf-8") as fp:
        json.dump({"repeat": removed_repeat, "langid": removed_langid}, fp, ensure_ascii=False)
    write_forms(counts_dir / f"{stem}.forms.gz", meta, forms)  # last: its presence marks the shard done
    return meta


# -- the run --------------------------------------------------------------------------------------


def _counted(dirs: Dirs, path: Path, repeat_sha: str) -> bool:
    out = dirs.counts / (path.name.removesuffix(".tsv.gz") + ".forms.gz")
    return out.exists() and read_forms_meta(out).get("repeat_sha") == repeat_sha


def _removed_summary(dirs: Dirs, final: set[str]) -> dict[str, Any]:
    """What the two line filters took out: lines, tokens, and forms found *only* in removed lines.

    Attribution is sequential, as the filters run: a form counts as removed by language ID when it
    occurs in no kept and no repeated line, and as removed by the repeated-line filter when it
    occurs in no kept line.
    """
    repeat: Counter[str] = Counter()
    langid: Counter[str] = Counter()
    for path in dirs.counts.glob("*.removed.json.gz"):
        with gzip.open(path, "rt", encoding="utf-8") as fp:
            data = json.load(fp)
        repeat.update(data["repeat"])
        langid.update(data["langid"])
    only_repeat = {f: n for f, n in repeat.items() if f not in final}
    only_langid = {f: n for f, n in langid.items() if f not in final and f not in repeat}

    def summary(all_tokens: Counter[str], only: dict[str, int]) -> dict[str, int]:
        return {"tokens": sum(all_tokens.values()), "forms_only_in_removed_lines": len(only),
                "tokens_of_those_forms": sum(only.values()),
                "forms_only_in_removed_lines_5plus": sum(1 for n in only.values() if n >= 5)}

    return {"repeated_lines": summary(repeat, only_repeat), "langid": summary(langid, only_langid)}


def run_forms(
    manifest: Manifest, *, data_dir: Path, out_dir: Path, tokens: int, workers: int,
    manifest_root: Path | None = None, keep_shards: bool = False,
    log: Callable[[str], None] = lambda s: print(s, flush=True),
) -> dict[str, Any]:
    lang = manifest.language.code
    dirs = Dirs(data_dir / f"forms-{lang}")
    dirs.make()
    out_dir.mkdir(parents=True, exist_ok=True)
    ctx = multiprocessing.get_context("spawn")
    started = time.time()
    seconds: dict[str, float] = {}
    tasks = plan_tasks(manifest, tokens, dirs.root, manifest_root)
    log(f"{lang}: {len(tasks)} URLs, caps {sorted({t.cap for t in tasks}, key=lambda c: c or 0)}")

    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
        for res in pool.map(fetch_url, tasks):
            log(f"fetched {res['task']} in {res['seconds']:.0f}s")
    seconds["fetch_clean"] = time.time() - t0

    paths = shard_paths(dirs.shards)
    t0 = time.time()
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx) as pool:
        repeats = find_repeats(paths, pool)
    repeats_path = dirs.work / "repeats.npy"
    np.save(repeats_path, repeats)
    repeat_sha = hashlib.sha256(repeats_path.read_bytes()).hexdigest()[:16]
    seconds["repeated_lines"] = time.time() - t0
    log(f"{lang}: {len(paths)} shards, {len(repeats):,} repeated line keys (>= {REPEAT_DOCS} documents)")

    t0 = time.time()
    todo = [p for p in paths if not _counted(dirs, p, repeat_sha)]
    with ProcessPoolExecutor(max_workers=workers, mp_context=ctx, initializer=init_counter,
                             initargs=(lang, str(manifest_root) if manifest_root else None,
                                       str(repeats_path))) as pool:
        for meta in pool.map(count_one, [(p, dirs.counts) for p in todo]):
            log(f"tokenized {meta['shard']}: {meta['tokens']:,} tokens, {meta['forms']:,} forms, "
                f"{meta['repeat_lines']:,} repeated lines dropped, {meta['seconds']:.0f}s")
    seconds["tokenize"] = time.time() - t0

    t0 = time.time()
    forms_files = sorted(dirs.counts.glob("*.forms.gz"))
    merged = merge_forms(forms_files)
    metas = [read_forms_meta(p) for p in forms_files]
    seconds["merge"] = time.time() - t0
    header = build_header(manifest, tasks, dirs, metas, merged.forms, int(merged.counts.sum()), tokens, seconds, started)
    header["removed"] = _removed_summary(dirs, set(merged.forms))
    write_forms_tsv(out_dir / f"forms-{lang}.tsv", header, merged)
    if not keep_shards:
        shutil.rmtree(dirs.shards)
    return header


def build_header(
    manifest: Manifest, tasks: list[UrlTask], dirs: Dirs, metas: list[dict[str, Any]], forms: list[str],
    total: int, requested: int, seconds: dict[str, float], started: float,
) -> dict[str, Any]:
    sources: dict[str, dict[str, Any]] = {}
    for src in manifest.sources:
        mine = [t for t in tasks if t.source == src.name]
        if not mine:
            continue
        shards = [m for m in metas if m["source"] == src.name]
        markers = [json.loads(marker_path(dirs.work, src.name, t.url_index).read_text(encoding="utf-8"))
                   for t in mine]
        dropped: Counter[str] = Counter()
        for m in shards:
            dropped.update(m["dropped"])
        sources[src.name] = {
            "urls": len(mine), "url_cap_chars": mine[0].cap, "stride": mine[0].stride,
            "shards": len(shards), "tokens": sum(m["tokens"] for m in shards),
            "docs": sum(m["docs"] for m in shards), "lines": sum(m["lines"] for m in shards),
            "raw_chars_read": sum(m["raw_chars"] for m in markers),
            "compressed_bytes_read": sum(m["compressed_bytes_read"] for m in markers),
            "hygiene_dropped": dict(dropped),
            "lines_dropped_repeated": sum(m["repeat_lines"] for m in shards),
            "lines_dropped_langid": sum(m["langid_lines"] for m in shards),
            "url_list": [src.urls[t.url_index] for t in mine],
        }
    return {
        "language": manifest.language.code, "frequer": __version__,
        "date": time.strftime("%Y-%m-%d", time.gmtime(started)),
        "tokenizer": manifest.forms.tokenizer if manifest.forms else "",
        "tokens_requested": requested, "tokens": total, "forms": len(forms),
        "documents": sum(m["docs"] for m in metas), "lines": sum(m["lines"] for m in metas),
        "repeat_filter": {"min_documents": REPEAT_DOCS, "normalisation": "frequer.hygiene.near_key"},
        "seconds": {k: round(v, 1) for k, v in seconds.items()}, "sources": sources,
    }
