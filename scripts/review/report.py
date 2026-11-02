"""The per-band report the developer reads to choose the cutoff: routed.tsv, the review rounds and any audit.

    python report.py <config.json>         -> <work>/band-report.md

Bands (config ``bands``, default 0-10k, 10-20k, 20-25k, 25-30k) are positions in the cleaned list (the kept
count), so a band holds what a cut there would keep. Per band: actions, kept share, the share of reviewed
lemmas that were real (keep or merge), rule hits; then the audit estimates (``audit*`` rounds: the share of
sampled keeps that are real lemmas, the share of sampled drops the reviewers would keep), 30 random keeps at
each band's upper edge, 50 random drops, every merge and the questions for the developer. The report states
evidence; the cutoff is the developer's choice.
"""

from __future__ import annotations

import bisect
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KEPT, load, read_tsv

DECISION_COLUMNS = ("lemma", "decision", "reason", "how", "rank")
DROPS = ("review-drop", "propn-drop", "number-drop", "place-drop", "drop")
ACTIONS = ("keep", "review-keep", "pending", "pending-names", *DROPS)

cfg = load(sys.argv[1])
R = cfg["work"]
BANDS = [tuple(b) for b in cfg.get("bands", [(0, 10000), (10000, 20000), (20000, 25000), (25000, 30000)])]
rows = [line.split("\t") for line in (R / "routed.tsv").read_text(encoding="utf-8").splitlines()
        if not line.startswith("#")]


def rounds(audit: bool) -> list[Path]:
    paths = [p for p in R.glob("review/*/decisions.tsv") if p.parent.name.startswith("audit") == audit]
    return sorted(paths, key=lambda p: p.stat().st_mtime)


how: dict[str, tuple[str, str]] = {}
why: dict[str, tuple[str, str]] = {}
merge_rank: dict[str, int] = {}
for rnd in rounds(audit=False):
    for r in read_tsv(rnd, DECISION_COLUMNS):
        how[r["lemma"]], why[r["lemma"]] = (r["how"], rnd.parent.name), (r["decision"], r["reason"])
        if r["decision"].startswith("merge:"):
            merge_rank[r["lemma"]] = int(r["rank"] or 0)
audit: dict[str, str] = {}
for rnd in rounds(audit=True):
    for r in read_tsv(rnd, DECISION_COLUMNS):
        audit[r["lemma"]] = r["decision"]
merges = {k: v for k, v in why.items() if v[0].startswith("merge:")}


def label(lo: int, hi: int) -> str:
    return f"{lo / 1000:g}-{hi / 1000:g}k"


def band_of(kept: int) -> str | None:
    for lo, hi in BANDS:
        if lo < kept <= hi:
            return label(lo, hi)
    return None


per: dict[str, Counter[str]] = defaultdict(Counter)
rule_hits: dict[str, Counter[str]] = defaultdict(Counter)
audit_keep: dict[str, Counter[str]] = defaultdict(Counter)
audit_drop: dict[str, Counter[str]] = defaultdict(Counter)
drops, at_edge = [], defaultdict(list)
edges = [hi for _lo, hi in BANDS]
for rank, lemma, action, freq, pos, _forms, flags, kept in rows:
    b = band_of(max(int(kept), 1))
    if b is None:
        break
    per[b][action] += 1
    for f in {x.split(":")[0].strip() for x in flags.split("; ") if x}:
        rule_hits[b][f] += 1
    if action in DROPS:
        drops.append((int(rank), lemma, action, flags, why.get(lemma, ("", ""))[1]))
    if action in KEPT:
        for edge in edges:
            if abs(int(kept) - edge) <= 150:
                at_edge[edge].append((int(kept), lemma, action, pos, freq))
    if lemma in audit:
        real = audit[lemma] == "keep" or audit[lemma].startswith("merge:")
        if action in ("keep", "review-keep"):
            audit_keep[b]["real" if real else "junk"] += 1
        elif action in DROPS:
            audit_drop[b]["would keep" if real else "drop"] += 1
ranks, kepts = [int(r[0]) for r in rows], [int(r[7]) for r in rows]
for rank in merge_rank.values():  # merged lemmas left the ranking: count them where they stood
    i = min(bisect.bisect_left(ranks, rank), len(kepts) - 1)
    b = band_of(max(kepts[i], 1))
    if b:
        per[b]["merge"] += 1

seen_actions = [a for a in ACTIONS if any(per[b][a] for b in per)]
rules = sorted({r for b in rule_hits for r in rule_hits[b]})
out = [f"# {cfg['lang']}: per-band report", "",
       "Bands are positions in the cleaned list (the kept count), so a band holds what a cut there would keep. "
       "Merged lemmas leave the ranking (their counts join the target) and are counted where they stood. "
       "This report is evidence for the developer's cutoff decision; it does not make it.", ""]
out += ["| band | entries | " + " | ".join(seen_actions) + " | merged | kept share | real among reviewed |",
        "|---|---:|" + "---:|" * (len(seen_actions) + 3)]
for lo, hi in BANDS:
    b = label(lo, hi)
    c = per[b]
    n = sum(v for a, v in c.items() if a != "merge") or 1
    kept_n = sum(c[a] for a in KEPT)
    rev = c["review-keep"] + c["review-drop"] + c["merge"]
    real = f"{(c['review-keep'] + c['merge']) / rev:.1%} of {rev:,}" if rev else "-"
    out.append(f"| {b} | {n:,} | " + " | ".join(f"{c[a]:,}" for a in seen_actions)
               + f" | {c['merge']:,} | {kept_n / n:.1%} | {real} |")
if any(per[b]["pending"] for b in per):
    out += ["", "**Unreviewed pending lemmas remain**: review them before reading the bands as final."]
out += ["", "## Rule hits per band", "", "| band | " + " | ".join(rules) + " |", "|---|" + "---:|" * len(rules)]
for lo, hi in BANDS:
    b = label(lo, hi)
    out.append(f"| {b} | " + " | ".join(f"{rule_hits[b][r]:,}" for r in rules) + " |")
if audit:
    out += ["", "## Audit estimates (random samples, two reviewers and an adjudicator; not applied)", "",
            "| band | sampled keeps | real lemmas | sampled drops | the reviewers would keep |", "|---|---:|---:|---:|---:|"]
    for lo, hi in BANDS:
        b = label(lo, hi)
        k, d = audit_keep[b], audit_drop[b]
        nk, nd = sum(k.values()), sum(d.values())
        out.append(f"| {b} | {nk} | {k['real'] / nk:.0%} | {nd} | {d['would keep'] / nd:.0%} |" if nk and nd else
                   f"| {b} | {nk} | {k['real'] / nk:.0%} | {nd} | - |" if nk else f"| {b} | 0 | - | {nd} | - |")
rng = random.Random(11)
for edge in edges:
    sel = sorted(rng.sample(at_edge[edge], min(30, len(at_edge[edge]))))
    out += ["", f"## 30 keeps around {edge:,}", "", "| list position | lemma | action | POS | frequency |",
            "|---:|---|---|---|---:|"]
    out += [f"| {k:,} | {lemma} | {a} | {p} | {int(f):,} |" for k, lemma, a, p, f in sel]
out += ["", "## 50 random drops", "", "| rank | lemma | how | flags | reviewers' reason |", "|---:|---|---|---|---|"]
for r in sorted(rng.sample(drops, min(50, len(drops)))):
    out.append(f"| {r[0]:,} | {r[1]} | {r[2]} | {r[3][:80]} | {r[4][:80]} |")
out += ["", f"## Merges ({len(merges)})", "", "| lemma | into | reason | decided |", "|---|---|---|---|"]
out += [f"| {k} | {d[6:]} | {w[:80]} | {how[k][0]} ({how[k][1]}) |" for k, (d, w) in sorted(merges.items())]
questions: dict[str, str] = {}
for p in sorted(p for p in R.glob("review/*/questions.txt") if not p.parent.name.startswith("audit")):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            m = re.match(r"# question ([^:\uff1a]+)", line.strip())  # an ASCII or a full-width colon
            questions.setdefault(m.group(1).strip() if m else line.strip(), line.strip())
out += ["", f"## Questions for the developer ({len(questions)} lemmas; first question per lemma)", ""]
out += list(questions.values())
(R / "band-report.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(R / "band-report.md", len(out), "lines")
