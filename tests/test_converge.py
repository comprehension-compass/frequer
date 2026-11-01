"""The convergence checkpoints' pure core: band comparison, split halves, mix, stopping rule."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from frequer.checkpoint import mix_of
from frequer.config import load_manifest
from frequer.converge import Ranked, compare, disagreement, due, run_length, split_halves


def ranked(lemmas: list[str]) -> Ranked:
    n = len(lemmas)
    return Ranked(1, (), tuple(lemmas), tuple(range(n, 0, -1)), tuple(float(x) for x in range(n, 0, -1)))


def test_change_and_rank_shift_against_the_previous_checkpoint() -> None:
    c = compare(ranked(["a", "b", "c", "d"]), ranked(["b", "a", "c", "e"]), bands=(2, 4))
    assert c["2"]["change"] == 0.0
    assert c["4"]["change"] == 0.25  # e is new to the top 4
    assert c["4"]["median_shift"] == 1  # shifts 1, 1, 0
    assert disagreement(["a"], ["a"], 2) is None  # a band wider than the list is undecided


def test_split_halves_deal_alternately_within_each_source_and_drop_an_odd_newest() -> None:
    names = ["w.00.0", "t.00.0", "w.01.0", "w.02.0", "w.03.0", "w.04.0", "t.00.1"]
    a, b = split_halves(names)
    assert a == ["w.00.0", "w.02.0", "t.00.0"]
    assert b == ["w.01.0", "w.03.0", "t.00.1"]  # w.04.0, the newest of an odd five, is left out


def test_stop_needs_three_consecutive_full_mix_passes() -> None:
    def row(mix: str, s20: float | None, s50: float | None) -> dict[str, Any]:
        return {"mix": mix, "bands": {"20000": {"split_half": s20}, "50000": {"split_half": s50}}}

    good, weak = row("full", 0.04, 0.09), row("full", 0.04, 0.11)
    assert run_length([good, good]) == 2
    assert run_length([good, good, good]) == 3
    assert run_length([good, good, weak]) == 0
    assert run_length([row("web only", 0.01, 0.01), good, good]) == 2
    assert run_length([good, row("full", 0.04, None)]) == 0  # fewer than 50k lemmas per half


def test_due_takes_a_checkpoint_after_every_shard() -> None:
    shards = [("s1", 6, 1.0), ("s2", 6, 2.0), ("s3", 30, 3.0)]
    assert due(shards, done=set()) == [(6, ["s1"]), (12, ["s1", "s2"]), (42, ["s1", "s2", "s3"])]
    assert due(shards, done={6, 12}) == [(42, ["s1", "s2", "s3"])]
    assert due(shards, done={12}) == [(42, ["s1", "s2", "s3"])]  # never back-fills behind the last


def test_mix_needs_every_first_source_whole_and_every_other_source(tmp_path: Path) -> None:
    manifest = load_manifest("ja")
    web = ["hplt-v2-ja.00.00000.json.gz", "hplt-v2-ja.01.00000.json.gz"]
    assert mix_of(manifest, tmp_path, web) == "web only"
    (tmp_path / "tatoeba-jpn.00.done.json").write_text(json.dumps({"shards": 2}))
    one = [*web, "tatoeba-jpn.00.00000.json.gz"]
    assert mix_of(manifest, tmp_path, one).startswith("partial")
    assert mix_of(manifest, tmp_path, [*one, "tatoeba-jpn.00.00001.json.gz"]) == "full"
    assert mix_of(manifest, tmp_path, ["tatoeba-jpn.00.00000.json.gz", "tatoeba-jpn.00.00001.json.gz"]) \
        == "partial (lacks hplt-v2-ja)"
