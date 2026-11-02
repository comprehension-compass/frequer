import gzip
import json
from pathlib import Path

from frequer import propn


def test_case_test_drops_names_and_keeps_common_nouns(tmp_path: Path) -> None:
    (tmp_path / "reference" / "learnable-names").mkdir(parents=True)
    (tmp_path / "reference" / "learnable-names" / "es.json").write_text(
        json.dumps({"schema_version": 1, "names": ["España"]}), encoding="utf-8")
    (tmp_path / "case").mkdir()
    (tmp_path / "case" / "es.tsv.gz").write_bytes(gzip.compress(
        "# surface\tinitial\trunning\ttitle\nKayak\t60\t20\t20\nTom\t10\t90\t0\nEspaña\t5\t95\t0\n".encode()))
    names = propn.load_names(tmp_path, "es")
    tally = propn.load_case("es", tmp_path)
    rows = [
        ("de", "ADP", {"de": 100}),
        ("españa", "PROPN", {"España": 50}),
        # 100 Kayak (20 % in running text) against 60 kayak: 25 % capitalised in running text; KAYAK is no evidence.
        ("kayak", "PROPN", {"Kayak": 100, "kayak": 60, "KAYAK": 500}),
        ("tom", "PROPN", {"Tom": 100, "tom": 2}),
    ]
    rank_of = {r[0]: i for i, r in enumerate(rows, start=1)}
    kept, dropped, names_kept, case_kept = propn.apply(
        rows, lambda r: r[0], lambda r: r[1], lambda r: r[2], names, tally, 0.5, rank_of)
    assert [r[0] for r in kept] == ["de", "españa", "kayak"]
    assert [(d.rank, d.lemma) for d in dropped] == [(4, "tom")]
    assert names_kept == [(2, "españa")]
    assert case_kept[0].lemma == "kayak" and case_kept[0].share is not None and abs(case_kept[0].share - 0.25) < 1e-9


def test_uncounted_names_split_three_ways(tmp_path: Path) -> None:
    # Developer ruling 2026-11-02: one-word names with no occurrences get bare entries; a spelling the
    # release files under another lemma is reported, not appended; multi-word names wait for a unit.
    from collections import Counter

    from frequer.counts import LemmaStats
    f = tmp_path / "es.json"
    f.write_text(json.dumps({"names": ["España", "Amárico", "Avar", "Abu Dabi"]}), encoding="utf-8")
    names = propn.LearnableNames(f, "", frozenset(n.casefold() for n in json.loads(f.read_text())["names"]))
    lemmas = {"españa": LemmaStats(freq=9, forms=Counter({"España": 9})),
              "ávaro": LemmaStats(freq=3, forms=Counter({"avar": 3}))}
    unc = propn.uncounted_names(names, lemmas)
    assert unc.bare == ["amárico"] and unc.filed_under == {"avar": "ávaro"} and unc.multiword == ["Abu Dabi"]
