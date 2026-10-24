"""The form inventory's pure cores: the repeated-line filter, the shard merge, the selection."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from frequer.forms import ShardForms, is_word, merge_forms, repeated_keys, write_forms
from frequer.select import (
    IgnoreRules,
    ignore_reason,
    load_listed,
    score,
    select_candidates,
)


def keys(result: object) -> list[int]:
    return [int(k) for k in np.asarray(result)]


def test_line_in_three_documents_is_dropped() -> None:
    # key 7 in documents 1, 2, 3; key 8 in two; key 9 many times but in one document
    k = [7, 7, 7, 8, 8, 9, 9, 9, 9]
    d = [1, 2, 3, 1, 2, 5, 5, 5, 5]
    assert keys(repeated_keys(k, d)) == [7]


def test_repeats_inside_one_document_count_once() -> None:
    assert keys(repeated_keys([4, 4, 4, 4], [1, 1, 2, 2])) == []
    assert keys(repeated_keys([4, 4, 4, 4], [1, 1, 2, 3])) == [4]


def test_repeat_threshold_is_configurable_and_empty_input_is_fine() -> None:
    assert keys(repeated_keys([4, 4], [1, 2], min_docs=2)) == [4]
    assert keys(repeated_keys([], [])) == []


def test_word_tokens_need_a_letter() -> None:
    assert is_word("casa") and is_word("COVID-19") and is_word("日本語") and is_word("ー") is True
    assert not any(is_word(t) for t in ["2024", "12,5", "—", "...", " ", "", "a b"])


def test_merge_adds_documents_and_unions_sites(tmp_path: Path) -> None:
    a, b = ShardForms(), ShardForms()
    a.add_document(site=1, tokens=["der", "der", "Haus"])
    a.add_document(site=2, tokens=["der"])
    b.add_document(site=2, tokens=["der", "Haus"])  # site 2 again, in another shard
    b.add_document(site=3, tokens=["der"])
    paths = []
    for i, shard in enumerate((a, b)):
        path = tmp_path / f"s{i}.forms.gz"
        write_forms(path, {"shard": i}, shard)
        paths.append(path)
    rows = {form: (n, d, s) for form, n, d, s in merge_forms(paths).rows()}
    assert rows["der"] == (5, 4, 3)  # 5 tokens, 4 documents, sites {1, 2, 3}
    assert rows["Haus"] == (2, 2, 2)  # sites {1, 2}


def rules(*, number: frozenset[str] = frozenset(), acronym: frozenset[str] = frozenset()) -> IgnoreRules:
    """Stand-ins for Honeyeater's helpers: letters, hyphens and apostrophes are language."""
    return IgnoreRules(
        script="latin",
        is_language=lambda t: bool(t) and all(c.isalpha() or c in "-'" for c in t),
        number=lambda t: True if t in number else None,
        has_script_letter=lambda t, _s: any((c.isascii() and c.isalpha()) or c in "áéíóúñ" for c in t),
        is_acronym=lambda t: t in acronym,
    )


def test_listed_forms_curated_forms_and_case_variants_are_excluded(tmp_path: Path) -> None:
    lookup = tmp_path / "lookup.json"
    lookup.write_text(json.dumps({"casa": {"casa": 3}, "Rosa": {"rosa": 1}}), encoding="utf-8")
    curated = tmp_path / "curated.tsv"
    curated.write_text("# surface\tlemma\nabismo\tabismo\tonly\n\nacepta\taceptar\n", encoding="utf-8")
    listed = load_listed(lookup, curated)
    assert listed == {"casa", "Rosa", "abismo", "acepta"}
    rows = [("casa", 900, 90, 50), ("Casa", 800, 80, 40), ("CASA", 700, 70, 30), ("Abismo", 600, 60, 20),
            ("rosa", 500, 50, 20), ("Acepta", 400, 40, 20), ("nuevo", 300, 30, 20)]
    folded, _ = select_candidates(rows, listed, rules(), case_fold=True, min_docs=5)
    assert [c.form for c in folded] == ["rosa", "nuevo"]  # rosa: only the capitalised Rosa is listed
    exact, _ = select_candidates(rows, listed, rules(), case_fold=False, min_docs=5)
    assert [c.form for c in exact] == ["Casa", "CASA", "Abismo", "rosa", "Acepta", "nuevo"]


def test_default_ignore_classes_and_urls_are_excluded() -> None:
    r = rules(number=frozenset({"mil"}), acronym=frozenset({"USA"}))
    assert ignore_reason("www.hotel.com", r) == "url_email"
    assert ignore_reason("info@hotel.es", r) == "url_email"
    assert ignore_reason("https://x.org/a", r) == "url_email"
    assert ignore_reason("12:30", r) == "non_language"
    assert ignore_reason("mil", r) == "number"
    assert ignore_reason("Привет", r) == "foreign_script"
    assert ignore_reason("USA", r) == "acronym"
    assert ignore_reason("hotel", r) is None


def test_ranking_needs_docs_and_sites_and_discounts_concentrated_forms() -> None:
    rows = [
        ("concentrated", 1000, 6, 5),  # frequent but from six pages
        ("spread", 400, 300, 200),
        ("onesite", 5000, 400, 2),  # fails the site floor
        ("thin", 900, 4, 4),  # fails the document floor
    ]
    pool, mass = select_candidates(rows, set(), rules(), case_fold=False, min_docs=5)
    assert [c.form for c in pool] == ["spread", "concentrated"]
    assert mass["eligible_pool"] == sum(n for _f, n, _d, _s in rows)
    assert score(400, 300) > score(1000, 6) and score(100, 0) == 0.0
