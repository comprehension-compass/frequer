"""Example sentences for a review queue: candidate lines by surface form in the re-streamed sample, each
confirmed by the runtime (the production sentence stage must file that lemma in that sentence).

    python examples.py <config.json> <out.jsonl> [--actions pending] [--only lemma,lemma,...]

Run from the pinned Honeyeater backend (PYTHONPATH as for route.py). Queue: routed.tsv lemmas with one of
``--actions`` within the window, or exactly the ``--only`` lemmas. Output: one JSON object per lemma
(rank, lemma, freq, pos, forms, flags, action, examples: up to 3 sentences).
"""

from __future__ import annotations

import argparse
import bisect
import gzip
import json
from collections import defaultdict
from pathlib import Path

from common import load, routed_rows

from frequer.config import load_manifest
from frequer.runtime import Runtime

ap = argparse.ArgumentParser()
ap.add_argument("config")
ap.add_argument("out")
ap.add_argument("--actions", default="pending")
ap.add_argument("--only")
args = ap.parse_args()
cfg = load(args.config)
actions, only = set(args.actions.split(",")), set(args.only.split(",")) if args.only else None
queue = []
for rank, lemma, action, freq, pos, forms, flags, kept in routed_rows(cfg):
    if (lemma in only) if only else (action in actions and int(kept) <= cfg["window"]):
        queue.append({"rank": int(rank), "lemma": lemma, "freq": int(freq), "pos": pos,
                      "forms": json.loads(forms), "flags": flags, "action": action})
lines: list[str] = []
docs: list[str] = []
for p in sorted((cfg["work"] / "sample/work").glob("*.tsv.gz")):
    with gzip.open(p, "rt", encoding="utf-8") as fp:
        for raw in fp:
            doc, _part, text = raw.rstrip("\n").split("\t", 2)
            lines.append(text)
            docs.append(f"{p.name}:{doc}")
text = "\n".join(lines)
starts, pos_ = [], 0
for ln in lines:
    starts.append(pos_)
    pos_ += len(ln) + 1
cand: dict[int, set[str]] = defaultdict(set)
for q in queue:  # up to 12 candidate lines per lemma, each from a different document
    seen, n = set(), 0
    for form in sorted(q["forms"], key=lambda f: -q["forms"][f]):
        f = form.replace(" ", "")
        i = text.find(f)
        while i >= 0 and n < 12:
            li = bisect.bisect_right(starts, i) - 1
            if docs[li] not in seen and len(lines[li]) <= 300:
                seen.add(docs[li])
                cand[li].add(q["lemma"])
                n += 1
            i = text.find(f, starts[li] + len(lines[li]) + 1) if li + 1 < len(starts) else -1
rt = Runtime(load_manifest(cfg["lang"]).language, lemma_dir=Path(cfg["lemma_dir"]), wheel=Path(cfg["wheel"]))
found: dict[str, list[str]] = defaultdict(list)
for li, sent in rt.sentences_many((li, lines[li]) for li in sorted(cand)):
    got = {rt.key(o.lemma, o.kind) for o in sent.occurrences}
    for lemma in cand[li] & got:
        s = cfg.get("join", " ").join(sent.words)  # "" for a language written without spaces (ja)
        if len(found[lemma]) < 3 and s not in found[lemma]:
            found[lemma].append(s[:160])
with open(args.out, "w", encoding="utf-8") as fp:
    for q in queue:
        q["examples"] = found.get(q["lemma"], [])
        fp.write(json.dumps(q, ensure_ascii=False) + "\n")
print(f"queue {len(queue)}; with examples {sum(1 for q in queue if q['examples'])}")
