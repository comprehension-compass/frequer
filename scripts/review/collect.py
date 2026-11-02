"""Apply one finished review round to frequer's ``corpora/review/<lang>.tsv``.

    python collect.py <config.json> <round> [--label "round 3 (pulled in by round 2)"] [--redecide] [--dry-run]

Append-only by default: a lemma that already has a line keeps it (an earlier decision stands), and a differing
decision from this round is reported as a conflict for the orchestrator to look at. ``--redecide`` is for a round
run under a new developer ruling (institutions, a rule change): it replaces those lines in place and keeps the old
decision in the reason. A round with an undecided lemma is refused; an ``audit*`` round estimates and is never
applied. Explicit developer rulings are edits to the review file itself, with the ruling in the reason.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import apply_round, load, read_tsv

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config")
ap.add_argument("round")
ap.add_argument("--label", help="the '# ...' header line for the appended block (default: the round name)")
ap.add_argument("--redecide", action="store_true")
ap.add_argument("--dry-run", action="store_true")
args = ap.parse_args()
cfg = load(args.config)
if args.round.startswith("audit"):
    raise SystemExit("an audit round estimates; it is never applied (report.py reads it)")
rows = read_tsv(cfg["work"] / "review" / args.round / "decisions.tsv", ("lemma", "decision", "reason", "how", "rank"))
dest = Path(__file__).resolve().parents[2] / "corpora" / "review" / f"{cfg['lang']}.tsv"
before = dest.read_text(encoding="utf-8") if dest.exists() else (
    f"# {cfg['lang']} junk review: two independent reviewers, an adjudicator for disagreements (scripts/review).\n"
    "# lemma<TAB>decision<TAB>reason\n")
after, stats = apply_round(before, ((r["lemma"], r["decision"], r["reason"]) for r in rows),
                           args.label or args.round, args.redecide)
if not args.dry_run:
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(after, encoding="utf-8")
print(json.dumps({"round": args.round, "file": str(dest), "dry_run": args.dry_run, **stats}, indent=1))
if stats["conflict"]:
    print("conflicts: earlier decisions stood; rerun with --redecide only if a developer ruling covers them")
