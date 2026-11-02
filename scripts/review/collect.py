"""Fold every review round's decisions into frequer's corpora/review/<lang>.tsv (a later round wins).

    python collect.py <config.json>
"""

from __future__ import annotations

import sys
from pathlib import Path

from common import load

cfg = load(sys.argv[1])
rows: dict[str, tuple[str, str]] = {}
# Later rounds win; a round directory named rulings* (explicit developer rulings) is applied last.
rounds = sorted((cfg["work"] / "review").glob("*/decisions.tsv"),
                key=lambda p: (p.parent.name.startswith("rulings"), p.stat().st_mtime))
for p in rounds:
    if p.parent.name.startswith("audit"):
        continue  # an audit estimates, it does not decide
    for line in open(p, encoding="utf-8"):
        k, d, w, _how, _rank = line.rstrip("\n").split("\t")
        if d:
            rows[k] = (d, w.replace("\t", " "))
dest = Path(__file__).resolve().parents[2] / "corpora" / "review" / f"{cfg['lang']}.tsv"
dest.parent.mkdir(parents=True, exist_ok=True)
with dest.open("w", encoding="utf-8") as f:
    f.write(f"# {cfg['lang']} junk review: two independent reviewers, an adjudicator for disagreements;\n"
            "# scripts/review. lemma<TAB>decision<TAB>reason\n")
    for k, (d, w) in rows.items():
        f.write(f"{k}\t{d}\t{w}\n")
print(f"{len(rows)} decisions from {len(rounds)} rounds -> {dest}")
