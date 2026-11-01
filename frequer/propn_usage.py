"""Usage evidence for proper nouns where case says nothing (German): names rarely take an article or adjective.

For each wanted key, the share of its occurrences right after an indefinite or negative article (the manifest's
``propn_usage_determiners``) or after an ADJ-majority word, read from the merged co-occurrence file (bigrams and
UPOS votes counted in the same pass, keyed as the unit detector keys a token: the lower-cased lemma). That file
holds items seen at least ``cooc.min_count`` times, so a rare bigram is missing and the share is a lower bound;
a key with no unigram entry has no evidence (``None``).
"""

from __future__ import annotations

import gzip
from collections import Counter, defaultdict
from collections.abc import Iterable
from pathlib import Path


def load(path: Path, determiners: Iterable[str], keys: Iterable[str]) -> dict[str, float]:
    """``key -> share`` for every key in ``keys`` the file has a unigram count for."""
    wanted = set(keys)
    dets = set(determiners)
    uni: dict[str, int] = {}
    votes: dict[str, Counter[str]] = defaultdict(Counter)
    after_det: Counter[str] = Counter()
    before: dict[str, Counter[str]] = defaultdict(Counter)
    with gzip.open(path, "rt", encoding="utf-8") as fp:
        next(fp)  # the JSON meta line
        for line in fp:
            kind, item, f, _d = line.rstrip("\n").split("\t")
            if kind == "u":
                if item in wanted:
                    uni[item] = int(f)
            elif kind == "t":
                key, _, upos = item.rpartition(" ")
                votes[key][upos] += int(f)
            elif kind == "n":
                first, _, second = item.partition(" ")
                if second in wanted and " " not in second:
                    if first in dets:
                        after_det[second] += int(f)
                    else:
                        before[second][first] = int(f)
    adjectives = {k for k, c in votes.items() if c.most_common(1)[0][0] == "ADJ"}
    return {k: (after_det[k] + sum(n for w, n in before[k].items() if w in adjectives)) / n
            for k, n in uni.items() if n}
