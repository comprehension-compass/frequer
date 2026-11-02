"""Spot audit: random keeps and drops per list band, for an estimate the developer reads (never applied).

    python audit.py <config.json> <name> [--keeps 100] [--drops 50] [--seed 11]

Writes <work>/<name>.txt (one lemma per line) from routed.tsv: per band (config ``bands``, kept positions), a
random sample of the kept lemmas (keep, review-keep) and of the dropped ones (any drop action). Then, with a
round name starting ``audit``:

    python examples.py <config.json> <work>/<name>.tsv --only-file <work>/<name>.txt
    python review.py   <config.json> <work>/<name>.tsv audit-<name>      (and --adjudicate)

``report.py`` turns the audit round into per-band estimates: the share of sampled keeps the reviewers call real
lemmas (keep or merge), and the share of sampled drops they would keep (false drops). ``collect.py`` refuses an
audit round: its decisions estimate, they do not decide.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import defaultdict

from common import KEPT, load, routed_rows

DEFAULT_BANDS = [(0, 10000), (10000, 20000), (20000, 25000), (25000, 30000)]
DROPS = ("drop", "review-drop", "propn-drop", "number-drop", "place-drop")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config")
ap.add_argument("name")
ap.add_argument("--keeps", type=int, default=100)
ap.add_argument("--drops", type=int, default=50)
ap.add_argument("--seed", type=int, default=11)
args = ap.parse_args()
cfg = load(args.config)
bands = [tuple(b) for b in cfg.get("bands", DEFAULT_BANDS)]
keeps: dict[tuple[int, int], list[str]] = defaultdict(list)
drops: dict[tuple[int, int], list[str]] = defaultdict(list)
top = max(hi for _lo, hi in bands)
for _rank, lemma, action, _freq, _pos, _forms, _flags, kept in routed_rows(cfg):
    position = max(int(kept), 1)
    if position > top:
        break
    band = next(b for b in bands if b[0] < position <= b[1])
    if action in ("keep", "review-keep"):
        keeps[band].append(lemma)
    elif action in DROPS:
        drops[band].append(lemma)
    elif action not in KEPT:
        raise SystemExit(f"unknown action {action!r} in routed.tsv")
rng = random.Random(args.seed)
picked: list[str] = []
summary = {}
for b in bands:
    k = rng.sample(keeps[b], min(args.keeps, len(keeps[b])))
    d = rng.sample(drops[b], min(args.drops, len(drops[b])))
    picked += k + d
    summary[f"{b[0]}-{b[1]}"] = {"keeps": len(k), "drops": len(d)}
(cfg["work"] / f"{args.name}.txt").write_text("".join(f"{x}\n" for x in picked), encoding="utf-8")
print(json.dumps(summary, indent=1))
