"""Per-band report of a junk review (no snapshot): routed.tsv and the review rounds' decisions -> band-report.md.

    python report.py <config.json>
"""
import json, random, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import load  # noqa: E402

cfg = load(sys.argv[1])
R = cfg["work"]
BANDS = [tuple(b) for b in cfg.get("bands", [(0, 10000), (10000, 20000), (20000, 25000), (25000, 30000)])]
KEPT = {"keep", "review-keep", "pending", "pending-names"}
rows = [l.rstrip("\n").split("\t") for l in open(R / "routed.tsv", encoding="utf-8") if not l.startswith("#")]
how, why = {}, {}
for rnd in sorted((p for p in R.glob("review/*/decisions.tsv") if not p.parent.name.startswith("audit")),
                  key=lambda p: p.stat().st_mtime):
    for l in open(rnd, encoding="utf-8"):
        k, d, w, h, rank = l.rstrip("\n").split("\t")
        how[k], why[k] = (h, rnd.parent.name), (d, w)
merges = {k: v for k, v in why.items() if v[0].startswith("merge:")}


def band_of(kept):
    for lo, hi in BANDS:
        if lo < kept <= hi:
            return f"{lo // 1000}-{hi // 1000}k"
    return None


per = defaultdict(Counter)
rule_hits = defaultdict(Counter)
drops, keeps_at = [], defaultdict(list)
for rank, lemma, action, freq, pos, forms, flags, kept in rows:
    b = band_of(max(int(kept), 1))
    if b is None:
        break
    per[b][action] += 1
    for f in {x.split(":")[0].strip() for x in flags.split("; ") if x}:
        rule_hits[b][f] += 1
    if action in ("review-drop", "propn-drop"):
        drops.append((int(rank), lemma, action, flags, why.get(lemma, ("", ""))[1]))
    if action in KEPT:
        for target in (25000, 30000):
            if abs(int(kept) - target) <= 150:
                keeps_at[target].append((int(kept), lemma, action, pos, freq))
import bisect
ranks = [int(r[0]) for r in rows]; kepts = [int(r[7]) for r in rows]
mrank = {}
for rnd in sorted((p for p in R.glob("review/*/decisions.tsv") if not p.parent.name.startswith("audit")),
                  key=lambda p: p.stat().st_mtime):
    for l in open(rnd, encoding="utf-8"):
        k, d, w, h, rank = l.rstrip("\n").split("\t")
        if d.startswith("merge:"):
            mrank[k] = int(rank)
for k, rank in mrank.items():  # merged lemmas left the ranking: count them where they stood
    i = min(bisect.bisect_left(ranks, rank), len(kepts) - 1)
    b = band_of(max(kepts[i], 1))
    if b:
        per[b]["merge"] += 1
out = [f"# {cfg['lang']} junk review: per-band report (no snapshot built)", ""]
out += ["Bands are positions in the cleaned list (the kept count), so a band holds what the developer would cut at.",
        "Actions: `keep` (no flag), `review-keep`, `pending-names` (place names awaiting the learnable-names list), "
        "`review-drop`, `propn-drop` (every Sudachi entry a person/organisation name). Merged lemmas leave the ranking "
        "(their counts join the target).", ""]
out += ["| band | entries | keep (no flag) | review-keep | pending-names | review-drop | dictionary name drop | "
        "merged | kept share | real lemmas among reviewed (keep + merge) |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
for lo, hi in BANDS:
    b = f"{lo // 1000}-{hi // 1000}k"; c = per[b]; n = sum(v for a, v in c.items() if a != "merge")
    kept = c["keep"] + c["review-keep"] + c["pending-names"] + c["pending"]
    rev = c["review-keep"] + c["review-drop"] + c["merge"]
    out.append(f"| {b} | {n:,} | {c['keep']:,} | {c['review-keep']:,} | {c['pending-names']:,} | {c['review-drop']:,} | "
               f"{c['propn-drop']:,} | {c['merge']:,} | {kept / n:.1%} | {(c['review-keep'] + c['merge']) / rev:.1%} of {rev:,} |")
    if c["pending"]:
        out.append(f"| {b} (unreviewed pending) | {c['pending']:,} | | | | | | | |")
out += ["", "## Rule hits per band", "", "| band | " + " | ".join(("diversity", "citation", "shape", "propn_band")) + " |",
        "|---|---:|---:|---:|---:|"]
for lo, hi in BANDS:
    b = f"{lo // 1000}-{hi // 1000}k"
    out.append(f"| {b} | " + " | ".join(f"{rule_hits[b][r]:,}" for r in ("diversity", "citation", "shape", "propn_band")) + " |")
random.seed(11)
for target in (25000, 30000):
    sel = sorted(random.sample(keeps_at[target], min(30, len(keeps_at[target]))))
    out += ["", f"## 30 keeps around {target:,}", "", "| list position | lemma | action | POS | frequency |", "|---:|---|---|---|---:|"]
    out += [f"| {k:,} | {l} | {a} | {p} | {int(f):,} |" for k, l, a, p, f in sel]
out += ["", "## 50 random drops", "", "| rank | lemma | how | flags | reviewers' reason |", "|---:|---|---|---|---|"]
for r in sorted(random.sample(drops, min(50, len(drops)))):
    out.append(f"| {r[0]:,} | {r[1]} | {r[2]} | {r[3][:80]} | {r[4][:80]} |")
out += ["", f"## Merges ({len(merges)})", "", "| lemma | into | reason | decided |", "|---|---|---|---|"]
out += [f"| {k} | {d[6:]} | {w[:80]} | {how[k][0]} ({how[k][1]}) |" for k, (d, w) in sorted(merges.items())]
qs = []
for p in sorted(p for p in R.glob("review/*/questions.txt") if not p.parent.name.startswith("audit")):
    qs += [l.strip() for l in open(p, encoding="utf-8") if l.strip()]
import re as _re
byl = {}
for q in qs:
    m = _re.match(r"# question ([^:：]+)", q)
    byl.setdefault(m.group(1).strip() if m else q, q)
out += ["", f"## Questions ({len(byl)} lemmas; first question per lemma)", ""] + list(byl.values())
(R / "band-report.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(len(out))
