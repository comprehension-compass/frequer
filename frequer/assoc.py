"""Association measures over the merged co-occurrence counts, and the shipped table.

Every combination is scored as a 2x2 contingency table over the
**observed** frequency ``O11`` of the combination, the marginals ``R1`` and
``C1`` (the frequencies of its two sides, each a unigram or a shorter n-gram
counted in the same pass) and the sample size ``N`` (non-boundary tokens):
``E11 = R1 * C1 * span / N``, the expected frequency under independence
(Evert 2005, *The Statistics of Word Cooccurrences*, ch. 3-4; ``span`` is 1 for
adjacent combinations and the window size for verb pairs, Evert 2008,
"Corpora and collocations", §3).

- ``pmi``: pointwise mutual information ``log2(O11 / E11)`` (Church & Hanks
  1990). For an n-gram of ``n > 2`` words, ``pmi`` is taken against full
  independence of all ``n`` words (``log2(O * N^(n-1) / prod f_i)``).
- ``pmi_min``: for ``n > 2``, the minimum PMI over the binary splits
  ``w1..wk | wk+1..wn`` (every split must be associated, the weakest link;
  the split view of n-gram association follows da Silva & Lopes 1999, "A Local
  Maxima method and a Fair Dispersion Normalization for extracting multi-word
  units", and Pecina 2010, "Lexical association measures and collocation
  extraction", §3). For bigrams it equals ``pmi``.
- ``npmi_min``: normalised PMI (Bouma 2009), ``pmi / -log2(O11 / N)``, in
  [-1, 1] (bounded, so usable as a feature), minimum over the same splits.
- ``g2_min``: Dunning's (1993) log-likelihood ratio ``G2 = 2 sum O ln(O/E)``
  over the four cells, **signed** (negative when ``O11 < E11``, Evert 2005
  §3.1.4), minimum over the same splits.

Pecina (2010) compares 82 measures for collocation extraction and finds no
single best one; PMI favours rare combinations and G2 frequent ones, so the
table ships both and the labelling queue filters on one and ranks by the other.
"""

from __future__ import annotations

import heapq
import math
from array import array
from collections import Counter
from collections.abc import Iterable, Iterator, Sequence
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from frequer.cooc import NGRAM, PAIR, TAG, UNIGRAM, Item, read_items, read_meta

#: Marginals key prefix of a two-member pair (a side of a three-member pair's split).
PAIR_PREFIX = "p:"
#: Critical value of chi-squared with one degree of freedom at p = 0.001.
G2_P001 = 10.83


def measures(o11: float, r1: float, c1: float, n: float, span: float = 1.0) -> tuple[float, float, float]:
    """``(pmi, npmi, signed G2)`` of one 2x2 table (pure; see the module docstring)."""
    e11 = r1 * c1 * span / n
    pmi = math.log2(o11 / e11)
    npmi = pmi / -math.log2(o11 / n) if o11 < n else 1.0
    return pmi, npmi, signed_g2(o11, r1, c1, n, span)


def signed_g2(o11: float, r1: float, c1: float, n: float, span: float = 1.0) -> float:
    """Dunning's G2 over the 2x2 table, negative for a repelled pair."""
    n_eff = n * span
    obs = (o11, r1 - o11, c1 - o11, n_eff - r1 - c1 + o11)
    exp = (r1 * c1 / n_eff, r1 * (n_eff - c1) / n_eff, (n_eff - r1) * c1 / n_eff,
           (n_eff - r1) * (n_eff - c1) / n_eff)
    g2 = 2.0 * sum(o * math.log(o / e) for o, e in zip(obs, exp, strict=True) if o > 0 and e > 0)
    return g2 if o11 >= exp[0] else -g2


def _vec(o: np.ndarray, r: np.ndarray, c: np.ndarray, n: float, span: np.ndarray) -> tuple[np.ndarray, ...]:
    """Vectorised :func:`measures` (rows whose marginals are missing come back NaN)."""
    with np.errstate(divide="ignore", invalid="ignore"):
        n_eff = n * span
        e11 = r * c / n_eff
        pmi = np.log2(o / e11)
        npmi = np.where(o < n, pmi / -np.log2(o / n), 1.0)
        obs = (o, r - o, c - o, n_eff - r - c + o)
        exp = (e11, r * (n_eff - c) / n_eff, (n_eff - r) * c / n_eff, (n_eff - r) * (n_eff - c) / n_eff)
        g2 = np.zeros_like(o)
        for oo, ee in zip(obs, exp, strict=True):
            g2 += np.where((oo > 0) & (ee > 0), oo * np.log(np.where(oo > 0, oo, 1) / np.where(ee > 0, ee, 1)), 0.0)
        g2 = 2.0 * g2
        g2 = np.where(o >= e11, g2, -g2)
        bad = (r <= 0) | (c <= 0)
        return (np.where(bad, np.nan, pmi), np.where(bad, np.nan, npmi), np.where(bad, np.nan, g2))


def splits(parts: Sequence[str]) -> list[tuple[str, str]]:
    """Every binary split of an n-gram's keys into a left and right side."""
    return [(" ".join(parts[:k]), " ".join(parts[k:])) for k in range(1, len(parts))]


@dataclass(frozen=True)
class Scored:
    kind: str
    keys: str
    f: int
    d: int
    pmi: float
    pmi_min: float
    npmi_min: float
    g2_min: float

    @property
    def n(self) -> int:
        return self.keys.count(" ") + 1


class Marginals:
    """Frequencies of every unigram and n-gram (by hash), for looking up a split's sides.

    Held as sorted numpy arrays of 64-bit string hashes, so the merged table of a
    full-size corpus fits in memory (16 bytes per item). The hashes are Python's
    own, valid within one process only; nothing is written with them.
    """

    def __init__(self, hashes: np.ndarray, freqs: np.ndarray) -> None:
        order = np.argsort(hashes, kind="stable")
        self.hashes, self.freqs = hashes[order], freqs[order]

    @classmethod
    def load(cls, items: Iterable[Item]) -> Marginals:
        hs, fs = array("q"), array("q")
        for item, f, _d in items:
            kind, key = item.split("\t", 1)
            if kind in (UNIGRAM, NGRAM):
                hs.append(hash(key))
                fs.append(f)
        return cls(np.frombuffer(hs, dtype=np.int64).copy(), np.frombuffer(fs, dtype=np.int64).copy())

    def lookup(self, keys: Sequence[str]) -> np.ndarray:
        """Frequency per key (0 where it was pruned or never seen)."""
        h = np.fromiter((hash(k) for k in keys), dtype=np.int64, count=len(keys))
        if not len(self.hashes):
            return np.zeros(len(keys))
        at = np.searchsorted(self.hashes, h)
        at = np.minimum(at, len(self.hashes) - 1)
        hit = self.hashes[at] == h
        return np.where(hit, self.freqs[at], 0).astype(np.float64)


def score_items(
    items: Iterable[Item], marginals: Marginals, tokens: int, pair_spans: dict[int, float], chunk: int = 200_000
) -> Iterator[Scored]:
    """Score every n-gram and pair item (unigrams and UPOS votes are skipped).

    ``pair_spans[k]`` is the window size of a ``k``-member verb pair. A
    two-member pair is the verb against its reflexive or particle; a
    three-member pair (verb, reflexive, particle) is the (verb, particle) pair
    against the reflexive. A side pruned below the count floor leaves the
    split unscored (NaN).
    """
    batch: list[Item] = []
    for row in items:
        kind = row[0][0]
        if kind in (NGRAM, PAIR):
            batch.append(row)
            if len(batch) >= chunk:
                yield from _score_batch(batch, marginals, tokens, pair_spans)
                batch = []
    if batch:
        yield from _score_batch(batch, marginals, tokens, pair_spans)


def _score_batch(batch: list[Item], marginals: Marginals, tokens: int, pair_spans: dict[int, float]) -> Iterator[Scored]:
    rows: list[tuple[int, str, list[str]]] = []  # (row index, kind, parts)
    lefts: list[str] = []
    rights: list[str] = []
    owner: list[int] = []
    span: list[float] = []
    for i, (item, _f, _d) in enumerate(batch):
        kind, key = item.split("\t", 1)
        parts = key.split(" ")
        rows.append((i, kind, parts))
        if kind == NGRAM:
            for left, right in splits(parts):
                lefts.append(left)
                rights.append(right)
                owner.append(i)
                span.append(1.0)
        elif len(parts) == 2:  # the verb against the reflexive or particle
            lefts.append(parts[0])
            rights.append(parts[1])
            owner.append(i)
            span.append(pair_spans.get(2, 1.0))
        else:  # (verb, reflexive, particle): the (verb, particle) pair against the reflexive
            lefts.append(PAIR_PREFIX + f"{parts[0]} {parts[2]}")
            rights.append(parts[1])
            owner.append(i)
            span.append(pair_spans.get(len(parts), 1.0))
    left_f = marginals.lookup(lefts)
    right_f = marginals.lookup(rights)
    o = np.array([batch[k][1] for k in owner], dtype=np.float64)
    pmi, npmi, g2 = _vec(o, left_f, right_f, float(tokens), np.array(span))
    worst: dict[int, tuple[float, float, float]] = {}
    for j, k in enumerate(owner):
        if math.isnan(pmi[j]):
            worst[k] = (math.nan, math.nan, math.nan)  # a side was pruned: the split is unknown
        elif k not in worst:
            worst[k] = (float(pmi[j]), float(npmi[j]), float(g2[j]))
        else:
            a, b, c = worst[k]
            worst[k] = (min(a, float(pmi[j])), min(b, float(npmi[j])), min(c, float(g2[j])))
    uni = marginals.lookup([p for _i, kind, parts in rows if kind == NGRAM for p in parts])
    at = 0
    for i, kind, parts in rows:
        item, f, d = batch[i]
        w_pmi, w_npmi, w_g2 = worst.get(i, (math.nan, math.nan, math.nan))
        full = w_pmi
        if kind == NGRAM:
            fs = uni[at : at + len(parts)]
            at += len(parts)
            if len(parts) > 2 and np.all(fs > 0):
                full = math.log2(f) + (len(parts) - 1) * math.log2(tokens) - float(np.sum(np.log2(fs)))
        yield Scored(kind, item.split("\t", 1)[1], f, d, full, w_pmi, w_npmi, w_g2)


def pair_marginals(items: Iterable[Item]) -> dict[str, int]:
    """Two-member pair frequencies, the (verb, particle) side of a three-member pair."""
    return {item.split("\t", 1)[1]: f for item, f, _d in items if item[0] == PAIR and item.count(" ") == 1}


def tag_majority(items: Iterable[Item]) -> dict[str, str]:
    """Each unigram key's majority UPOS from the ``t`` votes."""
    votes: dict[str, Counter[str]] = {}
    for item, f, _d in items:
        if item[0] == TAG:
            key, tag = item[2:].rsplit(" ", 1)
            votes.setdefault(key, Counter())[tag] += f
    return {k: min(c.items(), key=lambda kv: (-kv[1], kv[0]))[0] for k, c in votes.items()}


def build_table(
    merged: Path,
    *,
    min_count: int,
    pair_spans: dict[int, float],
    keep: int,
    min_docs: int = 1,
) -> tuple[list[Scored], int, dict[str, int]]:
    """Score every item of a merged file at or above ``min_count``.

    Returns the ``keep`` items with the highest ``g2_min`` among the positively
    associated ones (``g2_min >= G2_P001`` and ``pmi_min > 0``) seen in at least
    ``min_docs`` documents, the number scored, and the count per kind of
    everything scored.
    """
    meta = read_meta(merged)
    tokens = int(meta["tokens"])
    marginals = Marginals.load(r for r in read_items(merged) if r[1] >= min_count)
    pairs = pair_marginals(r for r in read_items(merged) if r[1] >= min_count)
    if pairs:  # a pair side that is itself a pair: add them to the lookup, prefixed
        extra_h = np.fromiter((hash(PAIR_PREFIX + k) for k in pairs), dtype=np.int64, count=len(pairs))
        extra_f = np.fromiter(pairs.values(), dtype=np.int64, count=len(pairs))
        marginals = Marginals(np.concatenate([marginals.hashes, extra_h]), np.concatenate([marginals.freqs, extra_f]))
    heap: list[tuple[float, str, Scored]] = []
    scored = 0
    by_kind: Counter[str] = Counter()
    for row in score_items((r for r in read_items(merged) if r[1] >= min_count), marginals, tokens, pair_spans):
        scored += 1
        by_kind[f"{row.kind}{row.n}"] += 1
        if math.isnan(row.g2_min) or row.g2_min < G2_P001 or not row.pmi_min > 0 or row.d < min_docs:
            continue
        entry = (row.g2_min, row.keys, row)
        if len(heap) < keep:
            heapq.heappush(heap, entry)
        elif entry > heap[0]:
            heapq.heapreplace(heap, entry)
    shipped = [e[2] for e in sorted(heap, reverse=True)]
    return shipped, scored, dict(by_kind)


def fmt(x: float) -> str:
    return "nan" if math.isnan(x) else f"{x:.3f}"


COLUMNS = ("kind", "n", "keys", "f", "d", "pmi", "pmi_min", "npmi_min", "g2_min", "head")


def table_lines(rows: Iterable[Scored], heads: dict[str, str]) -> Iterator[str]:
    yield "\t".join(COLUMNS)
    for r in rows:
        yield "\t".join([r.kind, str(r.n), r.keys, str(r.f), str(r.d), fmt(r.pmi), fmt(r.pmi_min),
                         fmt(r.npmi_min), f"{r.g2_min:.1f}", heads.get(r.keys, "") if r.kind == PAIR else ""])
