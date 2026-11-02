"""scripts/review plumbing: parsing answers, agreement, applying a round. Copies, merges and checks only."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "review"))
import common


def test_answers_keep_only_known_lemmas_and_valid_decisions() -> None:
    text = ("Here are my decisions:\n`casa\tkeep\treal word`\nperro\tmerge:perro\tsame\nxyz\tmaybe\t?\n"
            "unknown\tdrop\t\nhala\tmerge:\t\n# question casa: is it?\n")
    got, qs = common.parse_answer(text, {"casa", "perro", "xyz", "hala"})
    assert got == {"casa": ("keep", "real word"), "perro": ("merge:perro", "same")}
    assert qs == ["# question casa: is it?"]
    got, _ = common.parse_answer("renfe\tmerge:renfe\t\nunam\tkeep\t\n", {"renfe", "unam"}, ("keep", "drop"))
    assert got == {"unam": ("keep", "")}  # an institutions round allows keep and drop only


def test_agreement_needs_the_same_decision_and_target() -> None:
    a = {"x": ("keep", ""), "y": ("merge:a", ""), "z": ("drop", "")}
    b = {"x": ("keep", ""), "y": ("merge:b", "")}
    agreed, dis = common.agree(["x", "y", "z"], a, b)
    assert agreed == {"x": ("keep", "")} and dis == ["y", "z"]


def test_accent_only_merges_are_listed_for_the_coordinator() -> None:
    agreed = {"comisaria": ("merge:comisaría", ""), "fue": ("merge:ser", ""), "Hala": ("merge:hala", "")}
    assert common.accent_only_merges(agreed) == ["comisaria", "Hala"]


def test_applying_a_round_never_overwrites_without_redecide() -> None:
    before = "# head\ncasa\tkeep\tr1\nrenfe\tdrop\tname\n"
    after, stats = common.apply_round(before, [("casa", "keep", ""), ("renfe", "keep", "institution"),
                                               ("nuevo", "drop", "junk")], "round 2", redecide=False)
    assert after == before + "# round 2\nnuevo\tdrop\tjunk\n"
    assert stats == {"unchanged": 1, "conflict": 1, "added": 1}
    after, stats = common.apply_round(before, [("renfe", "keep", "institution")], "institutions", redecide=True)
    assert "renfe\tkeep\tinstitution (was drop: name)" in after and stats["redecided"] == 1
    with pytest.raises(SystemExit):
        common.apply_round(before, [("otro", "", "")], "r", redecide=False)


def test_release_entries_are_not_screening_candidates() -> None:
    names = frozenset({"parís"})
    assert common.release_entry("a pesar de", names) == "unit"
    assert common.release_entry("parte#Fem", names) == "homograph key"
    assert common.release_entry("París", names) == "learnable name"
    assert common.release_entry("casa", names) is None


def test_queue_round_trip(tmp_path: Path) -> None:
    q = [{"rank": 3, "lemma": "casa", "freq": 10, "pos": "NOUN", "forms": {"casa": 8, "casas": 2},
          "flags": "shape: x", "action": "pending", "examples": ["La casa\tazul.", "Mi casa."]}]
    common.write_queue(tmp_path / "q.tsv", q)
    back = common.read_queue(tmp_path / "q.tsv")
    assert back[0]["forms"] == {"casa": 8, "casas": 2} and back[0]["examples"] == ["La casa azul.", "Mi casa."]


def test_prompt_placeholders_must_all_be_filled() -> None:
    assert common.fill("{rules} / {decisions}", {"rules": "R", "decisions": "D"}) == "R / D"
    with pytest.raises(SystemExit):
        common.fill("{rules} {lemas}", {"rules": "R"})


def test_every_prompt_template_fills() -> None:
    for name in ("reviewer.md", "adjudicator.md", "system.md"):
        text = (common.PROMPTS / "common" / name).read_text(encoding="utf-8")
        common.fill(text, {"rules": "", "lemmas": "", "decisions": "", "language": "x"})
