"""Per-band report of the reviewed de list (kept-rank bands), from junkrun's output and the review file."""
import csv, json, random, sys
from collections import Counter
from pathlib import Path
flags_tsv, merges_tsv, review_tsv, questions, out = map(Path, sys.argv[1:6])
rows = list(csv.DictReader(flags_tsv.open(), delimiter='\t'))
exc = flags_tsv.with_suffix('.excluded.tsv')
if exc.exists():
    for line in exc.read_text(encoding='utf-8').splitlines():
        rk, lem, f, cls, reason = (line.split('\t') + ['', '', '', '', ''])[:5]
        rows.append({'rank': rk, 'lemma': lem, 'freq': f, 'pos': '', 'action': 'excluded:' + cls, 'flags': ''})
    rows.sort(key=lambda r: int(r['rank']))
review = {}
for line in review_tsv.read_text(encoding='utf-8').splitlines():
    if line.startswith('#') or not line.strip(): continue
    p = line.split('\t'); review[p[0]] = (p[1], p[2] if len(p) > 2 else '')
KEPT = ('keep', 'review-keep', 'pending', 'pending-names')
BANDS = [(0, 10000), (10000, 20000), (20000, 25000), (25000, 30000)]
kept = 0; band_of = {}
for r in rows:
    if r['action'] in KEPT:
        kept += 1
    b = next((i for i, (lo, hi) in enumerate(BANDS) if lo < max(kept, 1) <= hi), None)
    band_of[r['lemma']] = b
    r['kept_rank'] = kept if r['action'] in KEPT else ''
    if kept > 30000 and r['action'] in KEPT: break
def why(r):
    d = review.get(r['lemma'], ('', ''))
    if r['action'].startswith('excluded:'):
        return 'exclusion (English)' if 'english' in r['action'] else 'exclusion'
    if r['action'] == 'review-drop':
        return 'number rule' if d[1].startswith('number rule') else 'review drop'
    return r['action']
L = ["# de cleaning pass: per-band report (round 1 + round 2 applied)", "",
     "Bands by position in the cleaned list (kept rank). A lemma counts in the band where it would have sat. "
     "\"Kept\" includes unreviewed lemmas with no flag and reviewed keeps; \"dropped\" is every lemma removed from "
     "that stretch of the raw ranking (review drops, the number rule, 2+-flag drops).", "",
     "| band | raw ranks | kept | of which reviewed keep | dropped | review drop | English exclusion | number rule | other drop | kept share | f at band end |",
     "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
for i, (lo, hi) in enumerate(BANDS):
    rs = [r for r in rows if band_of.get(r['lemma']) == i]
    k = [r for r in rs if r['action'] in KEPT]; d = [r for r in rs if r['action'] not in KEPT]
    c = Counter(why(r) for r in d)
    last = k[-1] if k else None
    L.append(f"| {lo:,}-{hi:,} | {rs[0]['rank']}-{rs[-1]['rank']} | {len(k):,} | {sum(1 for r in k if r['action']=='review-keep'):,} | "
             f"{len(d):,} | {c['review drop']:,} | {c['exclusion (English)']:,} | {c['number rule']:,} | {sum(v for x, v in c.items() if x not in ('review drop','number rule','exclusion (English)')):,} | "
             f"{len(k) / max(1, len(rs)):.1%} | {last['freq'] if last else '-'} |")
L += ["", "Pending (flagged, not yet reviewed) inside the 30k: " + str(sum(1 for r in rows if r['action'] == 'pending' and r['kept_rank'] and int(r['kept_rank']) <= 30000)), ""]
# per-rule hits in window
win = [r for r in rows if band_of.get(r['lemma']) is not None]
hits = Counter(f.split(':')[0] for r in win for f in r['flags'].split(' | ') if f)
L += ["## Rule hits in the window", "", "| rule | hits | of which dropped |", "|---|---:|---:|"]
for rule, n in hits.most_common():
    dn = sum(1 for r in win if r['action'] not in KEPT and any(f.startswith(rule + ':') for f in r['flags'].split(' | ')))
    L.append(f"| {rule} | {n:,} | {dn:,} |")
L.append(f"| number rule (drops) | {sum(1 for r in win if why(r)=='number rule'):,} | |")
random.seed(7)
def sample_around(target):
    ks = [r for r in win if r['kept_rank'] and abs(int(r['kept_rank']) - target) <= 60]
    return random.sample(ks, min(15, len(ks)))
for t in (25000, 30000):
    L += ["", f"## Sample keeps around {t:,}", "", "| kept rank | raw rank | lemma | freq | POS | reviewed |", "|---:|---:|---|---:|---|---|"]
    for r in sorted(sample_around(t), key=lambda r: int(r['kept_rank'])):
        L.append(f"| {r['kept_rank']} | {r['rank']} | {r['lemma']} | {r['freq']} | {r['pos']} | {'yes' if r['action']=='review-keep' else ''} |")
drops = [r for r in win if r['action'] not in KEPT]
L += ["", "## Random 50 drops from the window", "", "| raw rank | lemma | freq | POS | why | reason |", "|---:|---|---:|---|---|---|"]
for r in sorted(random.sample(drops, min(50, len(drops))), key=lambda r: int(r['rank'])):
    L.append(f"| {r['rank']} | {r['lemma']} | {r['freq']} | {r['pos']} | {why(r)} | {review.get(r['lemma'], ('', ''))[1][:90]} |")
merges = [l.split('\t') for l in merges_tsv.read_text(encoding='utf-8').splitlines()]
rev = [m for m in merges if m[3].startswith('review')]; acc = [m for m in merges if not m[3].startswith('review')]
L += ["", f"## Merges: {len(merges):,} applied ({len(rev):,} from review, {len(acc):,} umlaut/ß folds)", "",
      "Largest review merges:", "", "| source | target | source freq |", "|---|---|---:|"]
L += [f"| {m[0]} | {m[1]} | {m[2]} |" for m in sorted(rev, key=lambda m: -int(m[2]))[:30]]
L += ["", "Largest umlaut/ß merges:", "", "| source | target | source freq | evidence |", "|---|---|---:|---|"]
L += [f"| {m[0]} | {m[1]} | {m[2]} | {m[3]} |" for m in sorted(acc, key=lambda m: -int(m[2]))[:20]]
L += ["", "## Reviewer and adjudicator questions", "", "```"] + questions.read_text(encoding='utf-8').splitlines() + ["```"]
out.write_text("\n".join(L) + "\n", encoding='utf-8')
print(out)
