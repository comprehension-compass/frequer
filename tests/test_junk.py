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


def test_umlaut_fold_merges_both_plain_spellings_into_the_umlaut_lemma() -> None:
    from frequer.counts import LemmaStats
    from frequer.junk import accent_merges

    lemmas = {"für": LemmaStats(freq=1000, forms=Counter({"für": 1000})),
              "fur": LemmaStats(freq=20, forms=Counter({"fur": 20})),
              "fuer": LemmaStats(freq=10, forms=Counter({"fuer": 10})),
              "schon": LemmaStats(freq=900, forms=Counter({"schon": 900})),
              "schön": LemmaStats(freq=1000, forms=Counter({"schön": 1000}))}
    maps = [{"ä": "a", "ö": "o", "ü": "u"}, {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}]
    got = {(m.source, m.target) for m in accent_merges(lemmas, 5, maps)}
    assert got == {("fur", "für"), ("fuer", "für")}  # schon/schön: two words, not 5x apart
