"""Stage 1 of the unflagged triage: two independent screeners mark suspects among the unflagged kept lemmas.

    python screen.py <config.json> <out-name>

Reads routed.tsv (action keep, no flags, kept position <= window), sends batches of 250 (lemma, POS, top
written forms; no examples) to two screeners with the prompt in config "screener", and writes
<work>/<out-name>/{A,B}/batch-NNN.txt and suspects.txt (lemma, how many screeners named it). Suspects then go
through the full protocol: examples.py --only, review.py.
"""

from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from common import claude, load, routed_rows

cfg = load(sys.argv[1])
out = cfg["work"] / sys.argv[2]
PROMPT = Path(cfg["screener"]).read_text(encoding="utf-8")
items = []
for _rank, lemma, action, _freq, pos, forms, flags, kept in routed_rows(cfg):
    if int(kept) > cfg["window"]:
        break
    if action == "keep" and not flags:
        written = ", ".join(f.replace(" ", "") for f in list(json.loads(forms))[:2])
        items.append(f"{lemma}\t{pos}\t{written}")
batches = [items[i:i + 250] for i in range(0, len(items), 250)]
known = {x.split("\t")[0] for x in items}
with ThreadPoolExecutor(cfg["parallel"]) as ex:
    res = list(ex.map(lambda a: claude(cfg, cfg["reviewer_model"], PROMPT + "\n" + "\n".join(batches[a[1]]),
                                       out / a[0] / f"batch-{a[1]:03d}.txt"),
                      [(w, i) for i in range(len(batches)) for w in ("A", "B")]))
sus: dict[str, int] = {}
for text in res:
    for line in text.splitlines():
        k = line.split("\t")[0].strip().strip("`")
        if k in known:
            sus[k] = sus.get(k, 0) + 1
(out / "suspects.txt").write_text("".join(f"{k}\t{n}\n" for k, n in sus.items()), encoding="utf-8")
print(json.dumps({"screened": len(items), "batches": len(batches), "suspects": len(sus),
                  "both": sum(1 for n in sus.values() if n >= 2)}))
