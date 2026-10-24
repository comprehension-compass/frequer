"""Cut a source stream into fixed-size, independently countable shards.

A shard is a run of whole documents totalling at least ``shard_chars`` raw
characters, so its boundaries depend only on the stream, never on hygiene or on
how many workers ran. Each cleaned shard is written to a small temporary file
for a worker to count and delete; its counts land in ``counts/``. A shard whose
counts file exists is skipped, and a URL whose stream was fully cut is recorded
in a ``.done.json`` marker so a rerun does not download it again.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import time
from collections.abc import Iterator
from dataclasses import dataclass, field
from pathlib import Path

from frequer.config import Hygiene, SourceConfig
from frequer.hygiene import Classifier, LineFilter
from frequer.sources import RawDoc, decompress, iter_docs, open_raw

FORMAT = 1


@dataclass(frozen=True)
class Limits:
    """Per-URL caps; None reads to the end of the stream."""

    max_chars: int | None = None
    max_urls: int | None = None


@dataclass
class ShardJob:
    source: str
    url_index: int
    shard_index: int
    path: Path
    counts_path: Path
    closed_by: str
    raw_chars: int
    docs: int
    lines: int
    dropped: dict[str, int]
    config: str
    seconds: dict[str, float] = field(default_factory=dict)


def part_of(doc_id: str, parts: int) -> int:
    """The corpus part (hash bucket) a document belongs to; stable across processes."""
    return int.from_bytes(hashlib.blake2b(doc_id.encode(), digest_size=8).digest(), "big") % parts


def config_hash(source: SourceConfig, hygiene: Hygiene, parts: int, lang: str) -> str:
    """Identity of everything that decides a shard's content; counts from another config never mix."""
    payload = json.dumps(
        [FORMAT, lang, source.name, source.shard_chars, source.pseudo_doc_lines, source.column,
         source.segment_lang, hygiene.model_dump(), parts],
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode()).hexdigest()[:16]


def counts_path(counts_dir: Path, source: str, url_index: int, shard_index: int) -> Path:
    return counts_dir / f"{source}.{url_index:02d}.{shard_index:05d}.json.gz"


def marker_path(work_dir: Path, source: str, url_index: int) -> Path:
    return work_dir / f"{source}.{url_index:02d}.done.json"


class _Timed:
    """Wraps a classifier, accumulating the seconds it takes."""

    def __init__(self, inner: Classifier) -> None:
        self.inner, self.seconds = inner, 0.0

    def __call__(self, line: str) -> tuple[str, float]:
        t0 = time.perf_counter()
        out = self.inner(line)
        self.seconds += time.perf_counter() - t0
        return out


def _write_shard(path: Path, rows: list[tuple[int, int, str]]) -> None:
    tmp = path.with_suffix(".tmp")
    with gzip.open(tmp, "wt", encoding="utf-8", compresslevel=3) as fp:
        for doc, part, line in rows:
            fp.write(f"{doc}\t{part}\t{line}\n")
    tmp.replace(path)


class _UrlCutter:
    """State of cutting one URL's documents into shards."""

    def __init__(self, *, lang: str, source: SourceConfig, hygiene: Hygiene, parts: int, url_index: int,
                 work_dir: Path, counts_dir: Path, chash: str, classify: Classifier) -> None:
        self.lang, self.source, self.hygiene, self.parts = lang, source, hygiene, parts
        self.url_index, self.work_dir, self.counts_dir, self.chash = url_index, work_dir, counts_dir, chash
        self.timed = _Timed(classify)
        self.shard_index = 0
        self.shard_raw = 0
        self._reset()

    def _reset(self) -> None:
        self.rows: list[tuple[int, int, str]] = []
        self.doc_no = 0
        self.fetch_s = 0.0
        self.hygiene_s = 0.0
        self.langid_before = self.timed.seconds
        self.line_filter = LineFilter(self.hygiene, self.lang, self.timed)
        self.shard_raw = 0

    @property
    def target(self) -> Path:
        return counts_path(self.counts_dir, self.source.name, self.url_index, self.shard_index)

    def add(self, doc: RawDoc) -> None:
        """Clean one document into the open shard (or just count its size when the shard is done)."""
        self.shard_raw += sum(len(line) for line in doc.lines)
        if self.target.exists():
            return
        t0 = time.perf_counter()
        part = part_of(doc.doc_id, self.parts)
        kept = [c for line in doc.lines if (c := self.line_filter.accept(line)) is not None]
        if kept:
            self.rows.extend((self.doc_no, part, c) for c in kept)
            self.doc_no += 1
        self.hygiene_s += time.perf_counter() - t0

    def close(self, reason: str) -> ShardJob | None:
        """End the open shard; returns a job unless its counts already exist."""
        job: ShardJob | None = None
        if not self.target.exists():
            path = self.work_dir / f"{self.source.name}.{self.url_index:02d}.{self.shard_index:05d}.tsv.gz"
            _write_shard(path, self.rows)
            langid = self.timed.seconds - self.langid_before
            job = ShardJob(
                source=self.source.name, url_index=self.url_index, shard_index=self.shard_index, path=path,
                counts_path=self.target, closed_by=reason, raw_chars=self.shard_raw, docs=self.doc_no,
                lines=len(self.rows), dropped=dict(self.line_filter.dropped), config=self.chash,
                seconds={"fetch_decode": self.fetch_s, "hygiene": self.hygiene_s - langid, "langid": langid},
            )
        self.shard_index += 1
        self._reset()
        return job


def _skippable(marker: Path, chash: str, cap: int | None, source: str, url_index: int,
               counts_dir: Path) -> bool:
    """True when this URL was fully cut under the same configuration and every shard is counted."""
    if not marker.exists():
        return False
    info = json.loads(marker.read_text(encoding="utf-8"))
    if info["config"] == chash and info["cap"] == cap and all(
        counts_path(counts_dir, source, url_index, k).exists() for k in range(info["shards"])
    ):
        return True
    if info["config"] == chash and info["closed_by"] == "cap" and info["shards"]:
        # The last shard was cut short by a cap that has since changed: recount it.
        counts_path(counts_dir, source, url_index, info["shards"] - 1).unlink(missing_ok=True)
    marker.unlink()
    return False


def produce_shards(
    *,
    lang: str,
    source: SourceConfig,
    hygiene: Hygiene,
    parts: int,
    work_dir: Path,
    counts_dir: Path,
    limits: Limits,
    classify: Classifier,
    url_stats: dict[str, dict[str, object]],
) -> Iterator[ShardJob]:
    """Yield a :class:`ShardJob` for every shard of ``source`` that still needs counting."""
    chash = config_hash(source, hygiene, parts, lang)
    urls = source.urls[: limits.max_urls] if limits.max_urls else source.urls
    cap = limits.max_chars if limits.max_chars is not None else source.max_chars_per_url
    for url_index, url in enumerate(urls):
        marker = marker_path(work_dir, source.name, url_index)
        if _skippable(marker, chash, cap, source.name, url_index, counts_dir):
            continue
        raw = open_raw(url)
        stream = decompress(raw, url)
        cutter = _UrlCutter(lang=lang, source=source, hygiene=hygiene, parts=parts, url_index=url_index,
                            work_dir=work_dir, counts_dir=counts_dir, chash=chash, classify=classify)
        docs = iter(iter_docs(source, url_index, stream))
        raw_total = 0
        closed_by = "eof"
        while True:
            t0 = time.perf_counter()
            doc = next(docs, None)
            cutter.fetch_s += time.perf_counter() - t0
            if doc is None:
                break
            raw_total += sum(len(line) for line in doc.lines)
            cutter.add(doc)
            if cutter.shard_raw >= source.shard_chars:
                job = cutter.close("size")
                if job:
                    yield job
            if cap is not None and raw_total >= cap:
                closed_by = "cap"
                break
        if cutter.shard_raw:
            job = cutter.close(closed_by)
            if job:
                yield job
        sha = raw.digest.hexdigest() if raw.eof else None
        expected = source.sha256.get(url)
        if sha and expected and sha != expected:
            raise ValueError(f"{url}: sha256 {sha} != manifest {expected}")
        stream.close()
        raw.close()
        marker.write_text(
            json.dumps({"config": chash, "cap": cap, "shards": cutter.shard_index, "closed_by": closed_by,
                        "raw_chars": raw_total, "compressed_bytes_read": raw.pos, "sha256": sha}),
            encoding="utf-8",
        )
        url_stats[f"{source.name}.{url_index:02d}"] = {
            "url": url, "raw_chars": raw_total, "compressed_bytes_read": raw.pos,
            "closed_by": closed_by, "sha256": sha,
        }
