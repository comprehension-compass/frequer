"""The co-occurrence core: what counts as an n-gram or a pair, and the shard merge."""

from __future__ import annotations

import math
from pathlib import Path

import pytest

from frequer import assoc
from frequer.combos import ACC, UnitList, compact, merge_all
from frequer.cooc import CoocAccumulator, merge_files, ngrams, pair_key, read_items, read_meta


def test_ngrams_stop_at_punctuation_and_figures() -> None:
    keys = ["sin", "embargo", "_", "el", "2024", "año", "pasado", "ir"]
    grams = list(ngrams(keys, 2, 4))
    assert "sin embargo" in grams
    assert not any("_" in g or "2024" in g for g in grams)
    assert "embargo el" not in grams and "el año" not in grams  # never across a boundary
    assert {"año pasado", "pasado ir", "año pasado ir"} <= set(grams)


def test_pair_key_puts_the_verb_first_and_stays_in_the_clause() -> None:
    keys = ["er", "freuen", "sich", "_", "sich"]
    upos = ["PRON", "VERB", "PRON", "PUNCT", "PRON"]
    assert pair_key(keys, upos, (1, 2)) == "freuen sich"
    assert pair_key(["sich", "freuen"], ["PRON", "VERB"], (0, 1)) == "freuen sich"
    assert pair_key(keys, upos, (1, 4)) is None  # across punctuation
    assert pair_key(["kommen", "morgen", "an"], ["VERB", "ADV", "ADP"], (0, 2)) == "kommen an"


def _shard(tmp: Path, name: str, docs: list[list[str]]) -> Path:
    acc = CoocAccumulator(2, 3)
    for doc in docs:
        for sentence in doc:
            keys = sentence.split()
            acc.add_sentence(keys, ["X"] * len(keys))
        acc.end_document()
    path = tmp / f"{name}.cooc.gz"
    acc.write(path, {"shard": name})
    (tmp / f"{name}.json.gz").write_bytes(b"")  # the done marker
    return path


def test_merge_sums_counts_and_documents_and_prunes(tmp_path: Path) -> None:
    a = _shard(tmp_path, "s.00.00000", [["a b c", "a b"], ["a b"]])
    b = _shard(tmp_path, "s.00.00001", [["a b d"]])
    out = tmp_path / "merged.gz"
    meta = merge_files([a, b], out, min_count=2)
    rows = {item: (f, d) for item, f, d in read_items(out)}
    assert rows["n\ta b"] == (4, 3)  # three in shard a over two documents, one in b
    assert rows["u\ta"] == (4, 3)
    assert "n\tb c" not in rows  # seen once: pruned
    assert meta["tokens"] == 10 and meta["shards"] == ["s.00.00000", "s.00.00001"]


def test_compaction_never_adds_a_shard_twice(tmp_path: Path) -> None:
    _shard(tmp_path, "s.00.00000", [["a b"]])
    assert compact(tmp_path) == 1
    # A crash after the fold but before the delete leaves the shard file behind.
    _shard(tmp_path, "s.00.00000", [["a b"]])
    _shard(tmp_path, "s.00.00001", [["a b"]])
    assert compact(tmp_path) == 1  # the stale copy is dropped, the new shard folded
    assert read_meta(tmp_path / ACC)["shards"] == ["s.00.00000", "s.00.00001"]
    _shard(tmp_path, "s.00.00002", [["a b"]])
    merge_all(tmp_path, tmp_path / "m.gz", 1)
    assert dict((i, f) for i, f, _d in read_items(tmp_path / "m.gz"))["n\ta b"] == 3


def test_unit_list_listed_pieces_and_extensions(tmp_path: Path) -> None:
    units = UnitList(seqs={("a", "través", "de")}, long={("a", "través", "de"): "a través de"},
                     pieces={("a", "través"): "a través de", ("través", "de"): "a través de",
                             ("a", "través", "de"): "a través de"},
                     headwords={"llamarse"}, bags={("llamar", "se")})
    assert units.ngram_status(["través", "de"]) == (True, "")
    assert units.ngram_status(["a", "través", "de", "el"]) == (False, "a través de")
    assert units.ngram_status(["sin", "embargo"]) == (False, "")
    assert units.pair_listed(["llamar", "se"], "")
    assert not units.pair_listed(["ir", "se"], "irse")


def test_measures_match_a_hand_worked_table() -> None:
    # Evert 2005-style 2x2: O11=30, R1=100, C1=200, N=10,000 -> E11=2.
    pmi, npmi, g2 = assoc.measures(30, 100, 200, 10_000)
    assert pmi == pytest.approx(math.log2(15))
    assert npmi == pytest.approx(math.log2(15) / -math.log2(30 / 10_000))
    cells = [(30, 2.0), (70, 98.0), (170, 198.0), (9730, 9702.0)]
    assert g2 == pytest.approx(2 * sum(o * math.log(o / e) for o, e in cells))
    assert assoc.signed_g2(1, 100, 200, 10_000) < 0  # observed below expected: repelled
    # A window multiplies the chance of meeting: the same counts are less surprising.
    assert assoc.measures(30, 100, 200, 10_000, span=4)[0] == pytest.approx(math.log2(15 / 4))


def test_trigram_takes_the_weakest_split(tmp_path: Path) -> None:
    items = [("u\ta", 100, 1), ("u\tb", 100, 1), ("u\tc", 1000, 1), ("n\ta b", 50, 1),
             ("n\tb c", 60, 1), ("n\ta b c", 40, 1)]
    marginals = assoc.Marginals.load(items)
    (row,) = list(assoc.score_items([items[-1]], marginals, 10_000, {}))
    left = assoc.measures(40, 100, 60, 10_000)  # a | b c
    right = assoc.measures(40, 50, 1000, 10_000)  # a b | c
    assert row.pmi_min == pytest.approx(min(left[0], right[0]))
    assert row.g2_min == pytest.approx(min(left[2], right[2]))
    assert row.pmi == pytest.approx(math.log2(40 * 10_000**2 / (100 * 100 * 1000)))
