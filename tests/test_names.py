"""Every learnable name gets an entry (developer ruling, 2026-11-02): frequer/names.py."""

from __future__ import annotations

from frequer import names


def test_each_listed_name_is_counted_filed_bare_or_multiword() -> None:
    spellings = {n.casefold(): n for n in
                 ["España", "Madrid", "Albacete", "Cuzco", "Nueva Zelanda", "Ciudad de México", "Granada", "Islandia"]}
    on_list = ["casa", "españa"]                                 # España already made the cut
    counted = ["casa", "españa", "madrid", "ciudad de méxico", "granada", "zzz"]   # rank order
    filed = {"Cuzco": "cusco", "Islandia": "islandia"}           # the release files Cuzco under cusco
    p = names.plan(spellings, on_list, counted, filed.get, fold_case=True)
    assert p.counted == ["madrid", "ciudad de méxico", "granada"]  # rank order, multiword unit included
    assert p.filed == [("Cuzco", "cusco")]
    assert p.bare == ["albacete", "cusco", "islandia"]           # uncounted singles, and the filed-under lemma
    assert p.multiword == ["Nueva Zelanda"]                      # no unit carries it: for release 1.6
    assert p.appended() == ["madrid", "ciudad de méxico", "granada", "albacete", "cusco", "islandia"]


def test_a_filed_under_lemma_already_listed_adds_nothing_and_case_is_kept_without_folding() -> None:
    spellings = {"köln": "Köln", "bayern": "Bayern"}
    p = names.plan(spellings, ["Cologne"], [], {"Köln": "Cologne"}.get, fold_case=False)
    assert p.filed == [("Köln", "Cologne")] and p.bare == ["Bayern"] and p.appended() == ["Bayern"]


def test_a_name_cut_into_tokens_no_unit_covers_is_multiword() -> None:
    spellings = {"近畿地方": "近畿地方", "京都": "京都"}
    p = names.plan(spellings, [], [], {"京都": "京都"}.get, fold_case=False, split={"近畿地方"}.__contains__)
    assert p.multiword == ["近畿地方"] and p.bare == ["京都"]
