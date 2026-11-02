"""A distributed part's skip list: shards counted elsewhere are treated as finished."""

from __future__ import annotations

import json
from pathlib import Path

from frequer.shards import CutMode, _skippable, counts_path


def _marker(tmp: Path) -> Path:
    marker = tmp / "src.00.done.json"
    marker.write_text(json.dumps({"config": "c", "cap": 10, "shards": 2, "closed_by": "cap"}), encoding="utf-8")
    return marker


def test_skipped_shards_count_as_finished(tmp_path: Path) -> None:
    counts = tmp_path / "counts"
    counts.mkdir()
    counts_path(counts, "src", 0, 1).write_text("x", encoding="utf-8")
    skip = frozenset({counts_path(counts, "src", 0, 0).name})
    assert _skippable(_marker(tmp_path), "c", 10, "src", 0, counts, CutMode(), skip)


def test_without_the_skip_list_the_url_is_recut(tmp_path: Path) -> None:
    counts = tmp_path / "counts"
    counts.mkdir()
    last = counts_path(counts, "src", 0, 1)
    last.write_text("x", encoding="utf-8")
    assert not _skippable(_marker(tmp_path), "c", 10, "src", 0, counts, CutMode())
    assert not last.exists()  # a capped last shard is recounted (the behaviour the skip list must not trigger)
