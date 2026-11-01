from collections import Counter

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
