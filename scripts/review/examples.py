"""Example sentences for a review queue: candidate lines by surface form in the re-streamed sample, each
confirmed by the runtime (the production sentence stage must file that lemma in that sentence).

    python examples.py <config.json> <queue.tsv> [--actions pending] [--only a,b | --only-file F] [--notes F]

Run from the pinned Honeyeater backend (PYTHONPATH as for route.py). Queue: routed.tsv lemmas with one of
``--actions`` within the window, or exactly the ``--only`` / ``--only-file`` lemmas (one per line: screen.py's
candidates.txt, audit.py's sample). ``--notes`` (screen.py's candidates.tsv) puts the screeners' notes in the
flags column. Output: a queue TSV (common.QUEUE_COLUMNS; up to 3 examples per lemma). Check the share of lemmas
with an example: under ~85 % means the sample is too small or the forms do not match.
"""

from __future__ import annotations

import argparse
import bisect
import gzip
import json
from collections import defaultdict
from pathlib import Path

from common import load, read_tsv, routed_rows, write_queue

from frequer.config import load_manifest
from frequer.runtime import Runtime

ap = argparse.ArgumentParser()
ap.add_argument("config")
ap.add_argument("out")
ap.add_argument("--actions", default="pending")
ap.add_argument("--only")
ap.add_argument("--only-file", type=Path)
ap.add_argument("--notes", type=Path)
args = ap.parse_args()
cfg = load(args.config)
actions = set(args.actions.split(","))
only = set(args.only.split(",")) if args.only else None
if args.only_file:
    only = {line.strip() for line in args.only_file.read_text(encoding="utf-8").splitlines() if line.strip()}
notes = {r["lemma"]: r["notes"] for r in read_tsv(args.notes, ("lemma", "screeners", "notes"))} if args.notes else {}
queue = []
for rank, lemma, action, freq, pos, forms, flags, kept in routed_rows(cfg):
    if (lemma in only) if only else (action in actions and int(kept) <= cfg["window"]):
        queue.append({"rank": int(rank), "lemma": lemma, "freq": int(freq), "pos": pos,
                      "forms": json.loads(forms),
                      "flags": f"screeners: {notes[lemma]}" if lemma in notes else flags, "action": action})
lines: list[str] = []
docs: list[str] = []
for p in sorted((cfg["work"] / "sample/work").glob("*.tsv.gz")):
    with gzip.open(p, "rt", encoding="utf-8") as fp:
        for raw in fp:
            doc, _part, text = raw.rstrip("\n").split("\t", 2)
            lines.append(text)
            docs.append(f"{p.name}:{doc}")
text = "\n".join(lines)
# A language that lower-cases its forms (de) must be searched in lower case too, or a capitalised noun never matches.
if load_manifest(cfg["lang"]).language.lowercase_forms:
    text = text.lower()
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
for q in queue:
    q["examples"] = found.get(q["lemma"], [])
write_queue(Path(args.out), queue)
print(f"queue {len(queue)}; with examples {sum(1 for q in queue if q['examples'])}")
