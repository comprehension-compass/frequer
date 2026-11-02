"""Assemble corpora/review/de.tsv and corpora/exclude/de.tsv from the review rounds."""
import json, sys
from pathlib import Path
S = Path(sys.argv[1]); rounds = sys.argv[2].split(','); repo = Path('/home/user/frequer')
dec, src = {}, {}
for lem in json.load(open(S / 'auto-keep.json')):
    dec[lem] = ('keep', 'learnable-names list (Honeyeater reference/learnable-names/de.json @ 1bf77f0)'); src[lem] = 'list'
items = {}
for tag in rounds:
    d = S / f'review-{tag}'
    c = json.load(open(d / 'compare.json'))
    for k, (x, r) in c['agreed'].items():
        dec[k] = (x, f'agreed: {r}'); src[k] = tag
    for f in sorted((d / 'adjudicate').glob('adj*.tsv')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.startswith('#') or not line.strip():
                continue
            p = line.split('\t')
            dec[p[0].strip()] = (p[1].strip(), f'adjudicated: {p[2].strip() if len(p) > 2 else ""}'); src[p[0].strip()] = tag
    items.update(json.load(open(S / f'items-{tag}.json')))
bad = [k for k, (x, _r) in dec.items() if not (x in ('keep', 'drop') or x.startswith('merge:'))]
assert not bad, bad[:20]
lines = ["# German junk-filter review (frequer/junk.py): lemma<TAB>decision<TAB>reason. 2026-11-02.",
         "# Two independent reviewers per lemma (example sentences from the counted sources), disagreements",
         "# adjudicated; learnable place names from Honeyeater's reviewed list. full/de/junk-review.md has the rules."]
lines += [f"{k}\t{x}\t{r}" for k, (x, r) in sorted(dec.items())]
(repo / 'corpora/review').mkdir(exist_ok=True)
(repo / 'corpora/review/de.tsv').write_text("\n".join(lines) + "\n", encoding='utf-8')
ex = ["# German exclusion list (frequer/exclude.py): lemma<TAB>class<TAB>reason. 2026-11-02.",
      "# The foreign-flagged lemmas of the junk review, under the es criterion: drop English leakage, keep loans",
      "# an English-speaking learner would want to know German uses. keep-loan rows exempt a lemma from the",
      "# foreign and shape rules."]
for k, (x, r) in sorted(dec.items()):
    it = items.get(k)
    if not it or 'foreign:' not in it['flags']:
        continue
    if x == 'drop':
        ex.append(f"{k}\texclude-english\t{r}")
    elif x == 'keep':
        ex.append(f"{k}\tkeep-loan\t{r}")
(repo / 'corpora/exclude').mkdir(exist_ok=True)
(repo / 'corpora/exclude/de.tsv').write_text("\n".join(ex) + "\n", encoding='utf-8')
print('decisions', len(dec), 'exclusion rows', len(ex) - 4)
