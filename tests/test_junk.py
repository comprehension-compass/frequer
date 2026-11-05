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


def test_reviewed_keep_overrides_propn_drop() -> None:
    # A famous institution capitalised in all running text (renfe) is kept when the review says keep.
    from pathlib import Path
    flags = junk.Flags()
    flags.propn_drop = {"renfe": "capitalised in 100% of running text", "acme": "capitalised in 100% of running text"}
    review = junk.Review(Path("r.tsv"), "", {"renfe": ("keep", "famous institution")})
    routed = {r.lemma: r.action for r in junk.route(["renfe", "acme"], flags, review, 10)}
    assert routed == {"renfe": "review-keep", "acme": "propn-drop"}


def test_split_moves_listed_forms_and_merges_the_rest() -> None:
    # halar holds the noun halo and the interjection Hala (developer ruling 2026-11-01).
    from pathlib import Path

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


def test_half_merge_counts_a_doubled_phrase_once() -> None:
    # cous cous: both tokens are "cous", so the phrase counts twice; merge:cuscús|half moves half (ruling 2026-11-02).
    from pathlib import Path
    review = junk.Review(Path("r.tsv"), "", {"cous": ("merge:cuscús|half", "")})
    assert review.merges() == {"cous": "cuscús"} and review.halves() == {"cous"}
    st = LemmaStats(freq=10, df=4, forms=Counter({"cous": 10}))
    junk.halve(st)
    assert st.freq == 5 and st.forms == Counter({"cous": 5}) and st.df == 2


def test_split_with_dash_drops_the_rest() -> None:
    # hoster: the hostería forms go to hostería; the English hosting term drops.
    from pathlib import Path

    from frequer.counts import Merged
    review = junk.Review(Path("r.tsv"), "", {"hoster": ("split:-|hostería=hostería", "")})
    merged = Merged(parts=1)
    merged.lemmas["hoster"] = LemmaStats(freq=50, forms=Counter({"hostería": 30, "hosters": 20}))
    junk.apply_splits(merged, review.splits())
    assert review.merges() == {} and merged.lemmas["hostería"].freq == 30
    routed = {r.lemma: r.action for r in junk.route(["hoster", "hostería"], junk.Flags(), review, 10)}
    assert routed["hoster"] == "review-drop"
