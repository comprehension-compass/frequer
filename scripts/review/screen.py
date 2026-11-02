"""Screening: two independent screeners list candidates for the full protocol (README §Triage, §Institutions).

    python screen.py <config.json> <name> [--pool keep|drops] [--prompt FILE] [--from N] [--to N]

``--pool keep`` (default): the unflagged keeps (action keep, no flags) within the window, positions --from..--to
(default the whole window), screened with config ``screener``: anything either screener lists is a suspect.
``--pool drops``: every review-drop and automatic propn-drop among the ranked lemmas that fill the window,
screened with config ``institutions_screen`` (positive selection: list what might be a famous institution).

Batches of 250 (lemma, POS, top written forms; no examples) go to screeners A and B. The release's own entries
(units, homograph keys, learnable names) are left out of the candidates: screeners flag them, but they are not
junk. Writes <work>/<name>/{A,B}/batch-NNN.txt, candidates.tsv (lemma, screeners, notes) and candidates.txt
(one lemma per line, for ``examples.py --only-file``). Read a sample of candidates.tsv before reviewing them.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from common import KEPT, claude, learnable_names, load, release_entry, routed_rows, write_tsv

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config")
ap.add_argument("name")
ap.add_argument("--pool", choices=("keep", "drops"), default="keep")
ap.add_argument("--prompt")
ap.add_argument("--from", dest="lo", type=int, default=0, help="first kept position (exclusive)")
ap.add_argument("--to", dest="hi", type=int, help="last kept position (default: the window)")
args = ap.parse_args()
cfg = load(args.config)
hi = args.hi or cfg["window"]
out = cfg["work"] / args.name
key = "screener" if args.pool == "keep" else "institutions_screen"
if not args.prompt and key not in cfg:
    raise SystemExit(f"config has no {key!r} prompt; pass --prompt")
PROMPT = Path(args.prompt or cfg[key]).read_text(encoding="utf-8")
names = learnable_names(cfg)
items, left_out = [], Counter()
for _rank, lemma, action, _freq, pos, forms, flags, kept in routed_rows(cfg):
    position = int(kept)
    if action in KEPT and position > hi:
        break
    wanted = (action == "keep" and not flags and position > args.lo) if args.pool == "keep" \
        else action in ("review-drop", "propn-drop")
    if not wanted:
        continue
    why = release_entry(lemma, names) if args.pool == "keep" else None
    if why:
        left_out[why] += 1
        continue
    written = ", ".join(f.replace(" ", cfg.get("join", " ")) for f in list(json.loads(forms))[:3])
    items.append(f"{lemma}\t{pos}\t{written}")
batches = [items[i:i + 250] for i in range(0, len(items), 250)]
known = {x.split("\t")[0] for x in items}
jobs = [(w, i) for i in range(len(batches)) for w in ("A", "B")]
with ThreadPoolExecutor(cfg["parallel"]) as ex:
    res = list(ex.map(lambda j: claude(cfg, cfg["reviewer_model"], PROMPT + "\n\n" + "\n".join(batches[j[1]]),
                                       out / j[0] / f"batch-{j[1]:03d}.txt"), jobs))
failed = [f"{w}{i}" for (w, i), text in zip(jobs, res, strict=True) if not text]
seen: Counter[str] = Counter()
notes: dict[str, list[str]] = defaultdict(list)
for text in res:
    for line in text.splitlines():
        parts = line.strip().strip("`").split("\t")
        if parts[0].strip() in known:
            seen[parts[0].strip()] += 1
            if len(parts) > 1 and parts[1].strip():
                notes[parts[0].strip()].append(parts[1].strip())
order = [x.split("\t")[0] for x in items if x.split("\t")[0] in seen]
write_tsv(out / "candidates.tsv", ("lemma", "screeners", "notes"),
          ({"lemma": k, "screeners": seen[k], "notes": " / ".join(notes[k])} for k in order))
(out / "candidates.txt").write_text("".join(f"{k}\n" for k in order), encoding="utf-8")
print(json.dumps({"pool": args.pool, "screened": len(items), "batches": len(batches), "failed_batches": failed,
                  "candidates": len(order), "both": sum(1 for k in order if seen[k] >= 2),
                  "left_out_release_entries": dict(left_out)}, ensure_ascii=False, indent=1))
if failed:
    print("some screener calls failed: rerun (finished calls are cached) before using candidates.txt")
