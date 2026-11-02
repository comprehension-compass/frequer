"""Merge the counts once (cached), apply frequer's filters, write routed.tsv (no snapshot).

Run from the pinned Honeyeater backend with frequer and the lemma site on PYTHONPATH:
    python route.py <config.json>
"""

from __future__ import annotations

import copy
import json
import pickle
import sys
from collections import Counter
from pathlib import Path

from common import load

from frequer import filters, snapshot
from frequer.config import load_manifest
from frequer.merge import merge_counts

KEPT = ("keep", "review-keep", "pending", "pending-names")
cfg = load(sys.argv[1])
work: Path = cfg["work"]
m = load_manifest(cfg["lang"])
cache = work / "merged.pkl"
if cache.exists():
    result = pickle.loads(cache.read_bytes())
else:
    result = merge_counts(Path(cfg["counts"]), m.parts, m.language.top_n * 4)
    cache.write_bytes(pickle.dumps(result))
merged = copy.deepcopy(result.merged)
weights = {s.name: s.weight for s in m.sources}
flt = filters.apply(m, merged, weights, "frequency", Path(cfg["reference"]))
with (work / "routed.tsv").open("w", encoding="utf-8") as fp:
    fp.write("# rank\tlemma\taction\tfreq\tpos\tforms\tflags\tkept_position\n")
    kept = 0
    for r in flt.routed:
        st = merged.lemmas[r.lemma]
        kept += r.action in KEPT
        fp.write(f"{r.rank}\t{r.lemma}\t{r.action}\t{st.freq}\t{snapshot.majority(st.pos, 'X')}\t"
                 f"{json.dumps(dict(st.forms.most_common(5)), ensure_ascii=False)}\t"
                 + "; ".join(f"{a}: {b}" for a, b in r.flags) + f"\t{kept}\n")
window = []
for r in flt.routed:
    if sum(x.action in KEPT for x in window) >= cfg["window"]:
        break
    window.append(r)
print(json.dumps({"window": len(window), "actions": Counter(r.action for r in window), "merges": len(flt.merges),
                  "hits": Counter(f for r in window for f in {a for a, _ in r.flags}),
                  "number_check": flt.number_check}, ensure_ascii=False, indent=1))
