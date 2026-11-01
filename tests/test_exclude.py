from pathlib import Path

from frequer import exclude


def test_exclusions_drop_keys_and_all_excluded_units(tmp_path: Path) -> None:
    (tmp_path / "exclude").mkdir()
    (tmp_path / "exclude" / "es.tsv").write_text(
        "# lemma\tclass\treason\n"
        "the\texclude-english\tEnglish article\n"
        "low\texclude-english\ttemplate\n"
        "cost\texclude-english\ttemplate\n"
        "low cost\tkeep-loan\testablished in Spain\n"
        "beach\texclude-english\tnot used in Spanish\n",
        encoding="utf-8",
    )
    ex = exclude.load("es", tmp_path)
    assert ex is not None
    ranked = ["de", "the", "low cost", "beach resort", "beach house", "resort", "low"]
    kept, dropped = exclude.apply(ranked, lambda r: r, ex)
    # Listed keys go; a unit goes only when every member is excluded and it is not listed as a keep.
    assert kept == ["de", "low cost", "beach resort", "beach house", "resort"]
    assert [(d.rank, d.lemma, d.cls) for d in dropped] == [(2, "the", "exclude-english"), (7, "low", "exclude-english")]
    (tmp_path / "exclude" / "es.tsv").write_text("beach\texclude-english\t-\nhouse\texclude-english\t-\n",
                                               encoding="utf-8")
    ex2 = exclude.load("es", tmp_path)
    assert ex2 is not None
    kept, dropped = exclude.apply(ranked, lambda r: r, ex2)
    assert "beach house" not in kept and dropped[0].cls == "exclude-unit"
    assert exclude.load("de", tmp_path) is None
