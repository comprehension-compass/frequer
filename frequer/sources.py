"""Streaming readers for the corpus sources: nothing is stored whole.

``open_raw`` yields the compressed bytes of a URL (or local path) as a
resumable stream: a dropped connection reconnects with a ``Range`` header at the
byte it reached, so a 60 GB shard survives a network blip. ``iter_docs`` decodes
that into :class:`RawDoc` records (a document id plus its lines). HPLT carries
real document boundaries; sentence corpora are grouped into pseudo-documents
because dispersion needs *some* unit larger than a sentence.
"""

from __future__ import annotations

import bz2
import gzip
import hashlib
import io
import json
import time
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import IO, TYPE_CHECKING
from urllib.parse import urlsplit

from frequer.config import SourceConfig

if TYPE_CHECKING:
    import requests

RETRIES = 8
CONNECT_TIMEOUT = 30
READ_TIMEOUT = 90


@dataclass(frozen=True)
class RawDoc:
    doc_id: str
    lines: list[str]
    #: The site the document came from (the HPLT record's URL host); a pseudo-document is its own site.
    site: str = ""


class HttpStream(io.RawIOBase):
    """A read-only, resumable HTTP body that hashes what it hands out."""

    def __init__(self, url: str) -> None:
        super().__init__()
        import requests

        self.url = url
        self.pos = 0
        self.digest = hashlib.sha256()
        self.eof = False
        self._session = requests.Session()
        self._resp: requests.Response | None = None

    def readable(self) -> bool:
        return True

    def _connect(self) -> None:
        headers = {"Range": f"bytes={self.pos}-"} if self.pos else {}
        resp = self._session.get(
            self.url, headers=headers, stream=True, timeout=(CONNECT_TIMEOUT, READ_TIMEOUT)
        )
        resp.raise_for_status()
        if self.pos and resp.status_code != 206:
            raise OSError(f"{self.url}: server ignored Range at byte {self.pos}")
        self._resp = resp

    def readinto(self, buffer: bytearray | memoryview) -> int:  # type: ignore[override]
        if self.eof:
            return 0
        for attempt in range(RETRIES):
            try:
                if self._resp is None:
                    self._connect()
                assert self._resp is not None
                chunk: bytes = self._resp.raw.read(len(buffer))
                break
            except Exception:
                self._resp = None
                if attempt == RETRIES - 1:
                    raise
                time.sleep(min(2**attempt, 30))
        if not chunk:
            self.eof = True
            return 0
        buffer[: len(chunk)] = chunk
        self.pos += len(chunk)
        self.digest.update(chunk)
        return len(chunk)

    def close(self) -> None:
        if self._resp is not None:
            self._resp.close()
            self._resp = None
        self._session.close()
        super().close()


class FileStream(io.RawIOBase):
    """The same interface over a local file (tests, offline reruns)."""

    def __init__(self, path: Path) -> None:
        super().__init__()
        self._fp = path.open("rb")
        self.digest = hashlib.sha256()
        self.pos = 0
        self.eof = False

    def readable(self) -> bool:
        return True

    def readinto(self, buffer: bytearray | memoryview) -> int:  # type: ignore[override]
        n = self._fp.readinto(buffer)
        if not n:
            self.eof = True
            return 0
        self.digest.update(bytes(buffer[:n]))
        self.pos += n
        return n

    def close(self) -> None:
        self._fp.close()
        super().close()


def open_raw(url: str) -> HttpStream | FileStream:
    if url.startswith(("http://", "https://")):
        return HttpStream(url)
    return FileStream(Path(url.removeprefix("file://")))


def decompress(raw: io.RawIOBase, url: str) -> IO[bytes]:
    """The decompressed byte stream, chosen by the URL's suffix."""
    buffered = io.BufferedReader(raw, buffer_size=1 << 20)
    suffix = url.rsplit(".", 1)[-1]
    if suffix == "zst":
        import zstandard

        reader: IO[bytes] = zstandard.ZstdDecompressor().stream_reader(buffered, read_across_frames=True)
        return reader
    if suffix == "gz":
        return gzip.GzipFile(fileobj=buffered)  # type: ignore[return-value]
    if suffix == "bz2":
        return bz2.BZ2File(buffered)
    return buffered


def site_of(url: str) -> str:
    """The host of a document URL, without a leading ``www.``; empty when it has none."""
    try:
        host = urlsplit(url).hostname or ""
    except ValueError:
        return ""
    return host.lower().removeprefix("www.")


def _hplt_docs(lines: Iterator[str], source: SourceConfig, stride: int) -> Iterator[RawDoc]:
    for n, raw in enumerate(lines):
        if stride > 1 and n % stride:
            continue
        try:
            doc = json.loads(raw)
        except ValueError:
            continue
        if doc.get("filter", "keep") != "keep":
            continue
        text = doc.get("text") or ""
        segments = text.split("\n")
        langs = doc.get("seg_langs") or []
        if source.segment_lang and len(langs) == len(segments):
            segments = [s for s, lang in zip(segments, langs, strict=True) if lang == source.segment_lang]
        if segments:
            doc_id = str(doc.get("id", ""))
            yield RawDoc(doc_id, segments, site_of(str(doc.get("u") or "")) or doc_id)


def _tsv_docs(lines: Iterator[bytes], source: SourceConfig, url_index: int, stride: int) -> Iterator[RawDoc]:
    """Pseudo-documents of ``pseudo_doc_lines`` consecutive lines; a stride skips whole groups unparsed."""
    group: list[str] = []
    index = 0
    size = source.pseudo_doc_lines
    for n, raw in enumerate(lines):
        if stride > 1 and (n // size) % stride:
            continue
        cols = raw.decode("utf-8", errors="replace").rstrip("\n").split("\t")
        if len(cols) <= source.column:
            continue
        group.append(cols[source.column])
        if len(group) >= size:
            doc_id = f"{source.name}:{url_index}:{index}"
            yield RawDoc(doc_id, group, doc_id)
            group, index = [], index + 1
    if group:
        doc_id = f"{source.name}:{url_index}:{index}"
        yield RawDoc(doc_id, group, doc_id)


def iter_docs(
    source: SourceConfig, url_index: int, stream: IO[bytes], stride: int = 1
) -> Iterator[RawDoc]:
    """Documents of one decompressed source stream, in file order.

    ``stride`` keeps every ``stride``-th document (HPLT) or pseudo-document (TSV), so a
    whole file can be sampled evenly without reading the rest of the pipeline.
    """
    if source.kind == "hplt":
        text = io.TextIOWrapper(stream, encoding="utf-8", errors="replace", newline="\n")
        yield from _hplt_docs(iter(text), source, stride)
    else:
        yield from _tsv_docs(iter(stream), source, url_index, stride)
