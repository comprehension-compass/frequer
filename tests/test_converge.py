"""The convergence checkpoints' pure core: band comparison, schedule, stopping rule."""

from __future__ import annotations

import json
from pathlib import Path

from frequer.checkpoint import mix_of
from frequer.config import load_manifest
from frequer.converge import Ranked, compare, due, meets, should_stop


def ranked(lemmas: list[str], tokens: int = 1) -> Ranked:
    n = len(lemmas)
    return Ranked(tokens, (), tuple(lemmas), tuple(range(n, 0, -1)), tuple(float(x) for x in range(n, 0, -1)))


def test_compare_overlap_rank_stability_and_tail() -> None:
    prev = ranked(["a", "b", "c", "d"])
    cur = ranked(["b", "a", "c", "e"])
    band = compare(prev, cur, bands=(2, 4))["bands"]
    assert band["2"]["overlap"] == 1.0
    assert band["2"]["spearman"] == -1.0  # a and b swapped
    assert band["4"]["overlap"] == 0.75  # d left the top 4
    assert band["4"]["median_shift"] == 1  # shifts 1, 1, 0
    assert band["4"]["freq_at_n"] == 1 and band["4"]["complete"]


def test_band_wider_than_the_list_is_incomplete_and_never_passes() -> None:
    c = compare(ranked(["a"]), ranked(["a"]), bands=(20_000, 50_000))
    assert not c["bands"]["50000"]["complete"]
    assert not meets(c)


def test_stopping_rule_needs_two_consecutive_passes() -> None:
    def comparison(o20: float, o50: float) -> dict[str, object]:
        return {"bands": {"20000": {"overlap": o20, "complete": True},
                          "50000": {"overlap": o50, "complete": True}}}

    good, weak = comparison(0.985, 0.96), comparison(0.985, 0.94)
    assert not should_stop([good])
    assert not should_stop([good, weak])
    assert not should_stop([good, weak, good])
    assert should_stop([weak, good, good])


def test_due_takes_the_shortest_prefix_reaching_each_target() -> None:
    shards = [("s1", 6_000_000, 1.0), ("s2", 6_000_000, 2.0), ("s3", 30_000_000, 3.0)]
    got = due(shards, done=set())
    # 12M reaches 10M; 42M reaches 25M (not 50M).
    assert got == [(10_000_000, ["s1", "s2"]), (25_000_000, ["s1", "s2", "s3"])]
    assert due(shards, done={10_000_000}) == [(25_000_000, ["s1", "s2", "s3"])]


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
