import json, sys, unicodedata, collections
sys.path.append('/home/user/frequer-deps')
from wordfreq import zipf_frequency as z
s = json.load(open('/home/user/out/es/es.json'))
L = list(s['lemmas'].items())
rank = {k: i+1 for i, (k, v) in enumerate(L)}
def strip(w): return ''.join(c for c in unicodedata.normalize('NFD', w) if unicodedata.category(c) != 'Mn')
# foreign-word table from report (top 10k window)
report = [l.split('|')[2].strip().strip('`') for l in open('/home/user/out/es/report.md').read().split('## Foreign-word candidates')[1].split('## Proper')[0].splitlines() if l.startswith('| ') and l[2].isdigit()]
cands = {}
def add(k, why):
    cands.setdefault(k, []).append(why)
for k in report: add(k, 'report foreign table')
for k, v in L:
    base = k.split('#')[0]
    if ' ' in base or '+' in base: continue
    en, es = z(base, 'en'), z(base, 'es')
    if en >= 2.5 and en > es + 0.5 and (v['pos'] != 'PROPN' or en >= 4.0):
        add(k, f'wordfreq en {en:.1f} vs es {es:.1f}')
# unaccented template spellings
byplain = collections.defaultdict(list)
for k, v in L: byplain[strip(k.split('#')[0])].append(k)
for k, v in L:
    b = k.split('#')[0]
    if strip(b) != b: continue
    tw = [t for t in byplain[b] if t != k and strip(t.split('#')[0]) == b and t.split('#')[0] != b]
    tw = [t for t in tw if s['lemmas'][t]['frequency'] >= 3 * v['frequency']]
    if tw: add(k, 'unaccented spelling of ' + ', '.join(tw[:2]))
# units containing template tokens / English-only units
for k, v in L:
    if v.get('unit') and all((z(w,'en') > z(w,'es') + 0.5 and z(w,'en') >= 3) for w in k.split() if w.isalpha()) and any(w.isalpha() for w in k.split()):
        add(k, 'unit of English-leaning words')
for k in ('jetcost', 'aereo', 'aereos', 'tiquete', 'low cost'):
    if k in rank: add(k, 'flight-search template')
out = []
for k, why in cands.items():
    v = s['lemmas'][k]
    out.append({'lemma': k, 'rank': rank[k], 'freq': v['frequency'], 'pos': v['pos'], 'unit': v.get('unit'), 'forms': list(v['forms'])[:3], 'why': '; '.join(dict.fromkeys(why))})
out.sort(key=lambda r: r['rank'])
json.dump(out, open('cands.json', 'w'), ensure_ascii=False, indent=0)
c = collections.Counter(w.split(' ')[0] + ' ' + w.split(' ')[1] if w.startswith('wordfreq') else w.split(' of ')[0] for r in out for w in r['why'].split('; '))
print(len(out)); print(collections.Counter(r['pos'] for r in out).most_common(8))
for r in out[:60]: print(r['rank'], r['lemma'], r['pos'], r['why'])
