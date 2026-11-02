import gzip
from collections import Counter
from pathlib import Path

import pytest

from frequer import junk
from frequer.config import JunkConfig
from frequer.counts import LemmaStats


def _st(freq: int, forms: dict[str, int]) -> LemmaStats:
    return LemmaStats(freq=freq, forms=Counter(forms))


def test_accent_merges_are_unique_and_keep_enye() -> None:
    lemmas = {
        "sabiduría": _st(600, {"sabiduría": 600}), "sabiduria": _st(50, {"sabiduria": 50}),
        "recibir": _st(900, {"recibió": 700, "recibir": 200}), "recibio": _st(40, {"recibio": 40}),
        "campaña": _st(900, {"campaña": 900}), "campana": _st(100, {"campana": 100}),
        "papa": _st(500, {"papa": 500}), "papá": _st(600, {"papá": 600}),
    }
    merges = {m.source: m.target for m in junk.accent_merges(lemmas, 5)}
    assert merges == {"sabiduria": "sabiduría", "recibio": "recibir"}


def test_routing_by_flag_count() -> None:
    cfg = JunkConfig(rules=["citation", "shape"], fragment_finals="lnrdz", verb_citation_pattern="(ar|er|ir)$")
    cands = [junk.Candidate("casa", 100, "NOUN", {"casa": 100}, 90),
             junk.Candidate("jugabl", 50, "ADJ", {"jugable": 50}, 40),  # citation + shape: 2 flags
             junk.Candidate("wi-fi", 40, "NOUN", {"wi-fi": 40}, 35),    # shape only: review
             junk.Candidate("cantar", 30, "VERB", {"canto": 30}, 25)]   # verb-shaped: exempt
    flags = junk.compute_flags(cands, cfg, total_docs=1000, zipf=None, lang="es", kept=frozenset(), propn_share=None)
    routed = {r.lemma: r.action for r in junk.route([c.lemma for c in cands], flags, None, 10)}
    assert routed == {"casa": "keep", "jugabl": "drop", "wi-fi": "pending", "cantar": "keep"}


def test_dictionary_proper_noun_evidence() -> None:
    def v(entries: list[str], tagged: bool) -> str | None:
        got = junk.dictionary_verdict(entries, tagged)
        return got[0] if got else None

    assert v(["person", "person"], True) == "name"  # 田中
    assert v(["place", "person"], True) == "place"  # アメリカ: a place among all-proper entries
    assert v(["proper"], True) == "review"  # トヨタ, 平成: another proper noun
    assert v(["common"], True) == "review"  # 返品, メンズ: a PROPN tag the dictionary does not back
    assert v([], True) == "review"  # サムソナイト-like words the dictionary lacks
    assert v(["person", "common"], False) is None  # 誠: a common reading, not tagged PROPN
    assert v(["person"], False) == "review"  # お花, 数人: built from parts, the dictionary shows only a name
    assert v(["common"], False) is None


def test_places_are_pending_names_unless_reviewed() -> None:
    flags = junk.Flags(propn_place={"東京": "place", "京都": "place"}, propn_drop={"田中": "person"})
    flags.propn_drop["令和"] = "person"  # an era name the dictionary also lists as a given name
    review = junk.Review(None, "", {"京都": ("keep", ""), "令和": ("keep", "")})  # type: ignore[arg-type]
    actions = {r.lemma: r.action for r in junk.route(["東京", "京都", "田中", "令和", "猫"], flags, review, 10)}
    assert actions == {"東京": "pending-names", "京都": "review-keep", "田中": "propn-drop", "令和": "review-keep",
                       "猫": "keep"}


def test_citation_reads_token_separated_forms_and_exempts_units() -> None:
    cfg = JunkConfig(rules=["citation"])
    cands = [junk.Candidate("ので", 100, "SCONJ", {"の で": 100}, 90),         # written as two tokens
             junk.Candidate("〜として", 80, "X", {"と し て": 80}, 70, unit=True),  # a construction
             junk.Candidate("子供", 60, "NOUN", {"子ども": 60}, 50)]             # the spelling never written
    flags = junk.compute_flags(cands, cfg, total_docs=1000, zipf=None, lang="ja", kept=frozenset(), propn_share=None)
    assert set(flags.flags) == {"子供"}


def test_number_rule_drops_what_the_app_check_ignores() -> None:
    verdicts = {"二十": True, "百": True, "千九百九十八": False, "一つ": None}  # the app's check (lexicon.lemma_defaults)
    cands = [junk.Candidate(w, 10, "NUM", {w: 10}, 9) for w in verdicts]
    flags = junk.compute_flags(cands, JunkConfig(number_rule=True), total_docs=100, zipf=None, lang="ja",
                               kept=frozenset(), propn_share=None, number_check=verdicts.get)
    assert set(flags.number_drop) == {"千九百九十八"}
    review = junk.Review(None, "", {"千九百九十八": ("keep", "")})  # type: ignore[arg-type]
    actions = {r.lemma: r.action for r in junk.route([c.lemma for c in cands], flags, review, 10)}
    assert actions == {"二十": "keep", "百": "keep", "千九百九十八": "review-keep", "一つ": "keep"}


def test_final_names_list_resolves_pending_places() -> None:
    flags = junk.Flags(propn_place={"東京": "place", "桃園": "place"})
    review = junk.Review(None, "", {"小倉": ("pending-names", "")})  # type: ignore[arg-type]
    listed = {"東京", "小倉"}.__contains__
    actions = {r.lemma: r.action for r in junk.route(["東京", "桃園", "小倉"], flags, review, 10, learnable=listed)}
    assert actions == {"東京": "review-keep", "桃園": "place-drop", "小倉": "review-keep"}


def test_umlaut_fold_merges_both_plain_spellings_into_the_umlaut_lemma() -> None:
    lemmas = {"für": _st(1000, {"für": 1000}), "fur": _st(20, {"fur": 20}), "fuer": _st(10, {"fuer": 10}),
              "schon": _st(900, {"schon": 900}), "schön": _st(1000, {"schön": 1000})}
    maps = [{"ä": "a", "ö": "o", "ü": "u"}, {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}]
    got = {(m.source, m.target) for m in junk.accent_merges(lemmas, 5, maps)}
    assert got == {("fur", "für"), ("fuer", "für")}  # schon/schön: two words, not 5x apart


def test_a_dominant_plain_spelling_is_never_merged_into_an_old_one() -> None:
    lemmas = {"bewusst": _st(50_000, {"bewusst": 50_000}), "Bewusst": _st(600, {"bewusst": 600}),
              "bewußt": _st(4_000, {"bewußt": 4_000})}
    assert junk.accent_merges(lemmas, 5, [{"ß": "ss"}]) == []


def test_propn_usage_flags_every_proper_noun_for_review() -> None:
    cfg = JunkConfig(rules=["propn_usage"], review_top=10)
    cands = [junk.Candidate("Berlin", 100, "PROPN", {"Berlin": 100}, 90),
             junk.Candidate("Haus", 100, "PROPN", {"Haus": 100}, 90),
             junk.Candidate("Xyz", 5, "PROPN", {"Xyz": 5}, 5),
             junk.Candidate("gehen", 100, "VERB", {"gehen": 100}, 90)]
    usage = {"Berlin": 0.001, "Haus": 0.2}
    flags = junk.compute_flags(cands, cfg, total_docs=1000, zipf=None, lang="de", kept=frozenset(),
                               propn_share=None, propn_usage=lambda c: usage.get(c.lemma))
    assert set(flags.flags) == {"Berlin", "Haus", "Xyz"}
    assert "name-like" in flags.flags["Berlin"][0][1] and "common-noun-like" in flags.flags["Haus"][0][1]
    # Proper-noun flags go to review within the window even alongside a second flag.
    flags.add("Berlin", "shape", "x")
    actions = {r.lemma: r.action for r in junk.route(["Berlin", "Haus", "gehen"], flags, None, 10)}
    assert actions == {"Berlin": "pending", "Haus": "pending", "gehen": "keep"}


def test_propn_usage_reads_articles_and_adjectives_from_the_cooc_file(tmp_path: Path) -> None:
    from frequer import propn_usage

    rows = ["u\tberlin\t100\t9", "u\thaus\t100\t9", "t\tneu ADJ\t50\t9", "t\tein DET\t80\t9",
            "n\tein haus\t15\t9", "n\tneu haus\t5\t9", "n\tin berlin\t40\t9"]
    path = tmp_path / "cooc-merged.gz"
    with gzip.open(path, "wt", encoding="utf-8") as fp:
        fp.write("{}\n" + "\n".join(rows) + "\n")
    got = propn_usage.load(path, ["ein", "kein"], ["berlin", "haus", "missing"])
    assert got == {"berlin": 0.0, "haus": 0.2}


def test_reviewed_keep_overrides_propn_drop() -> None:
    # A famous institution capitalised in all running text (renfe) is kept when the review says keep.
    flags = junk.Flags()
    flags.propn_drop = {"renfe": "capitalised in 100% of running text", "acme": "capitalised in 100% of running text"}
    review = junk.Review(Path("r.tsv"), "", {"renfe": ("keep", "famous institution")})
    routed = {r.lemma: r.action for r in junk.route(["renfe", "acme"], flags, review, 10)}
    assert routed == {"renfe": "review-keep", "acme": "propn-drop"}


def test_split_moves_listed_forms_and_merges_the_rest() -> None:
    # halar holds the noun halo and the interjection Hala (developer ruling 2026-11-02).
    from frequer.counts import Merged

    merged = Merged(parts=1)
    merged.lemmas["halar"] = LemmaStats(freq=100, df=50, forms=Counter({"halo": 80, "Hala": 20}),
                                        pos=Counter({"NOUN": 80, "INTJ": 20}))
    review = junk.Review(Path("r.tsv"), "", {"halar": ("split:halo|hala=Hala", "")})
    done = junk.apply_splits(merged, review.splits())
    junk.apply_merges(merged, [junk.Merge("halar", t, 0, "") for t in review.merges().values()])
    assert [m.target for m in done] == ["hala"]
    assert merged.lemmas["hala"].freq == 20 and merged.lemmas["hala"].forms == Counter({"Hala": 20})
    assert merged.lemmas["halo"].freq == 80 and "halar" not in merged.lemmas


def test_review_file_accepts_splits_and_rejects_unknown_decisions(tmp_path: Path) -> None:
    (tmp_path / "review").mkdir()
    (tmp_path / "review" / "xx.tsv").write_text("# round 1\nhalar\tsplit:halo|hala=Hala\tr\nfoo\tkeep\t\n",
                                                encoding="utf-8")
    review = junk.load_review("xx", tmp_path)
    assert review is not None and review.merges() == {"halar": "halo"}
    (tmp_path / "review" / "xx.tsv").write_text("foo\tmaybe\t\n", encoding="utf-8")
    with pytest.raises(SystemExit):
        junk.load_review("xx", tmp_path)
