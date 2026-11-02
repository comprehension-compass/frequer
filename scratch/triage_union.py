"""Union of 0-10k triage suspects -> cands.json (minus units, homograph keys, learnable names)."""
import collections, json, sys
sys.path[:0] = ['/home/user/frequer', '/home/user/he-c07c701/backend']
from pathlib import Path
from frequer import propn

T = Path('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/tri10')
snap = json.load(open('/home/user/out/es-30r/es.json'))['lemmas']
names = propn.load_names(Path('/home/user/he-c07c701'), 'es')
inp = {}
for d in ('tA1', 'tA2'):
    for l in open(T / d / 'input.tsv', encoding='utf-8'):
        if l.startswith('#'):
            continue
        p = l.rstrip('\n').split('\t')
        inp[p[0]] = p
seen = collections.Counter()
sus = collections.defaultdict(list)
for d in ('tA1', 'tA1b', 'tA2', 'tB1', 'tB2'):
    for l in open(T / d / 'output.tsv', encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 2 or p[0] not in inp:
            continue
        seen[p[0]] += 1
        if p[1].strip() == 'suspect':
            sus[p[0]].append(p[2] if len(p) > 2 else '')
missing = [k for k in inp if seen[k] < 2]
skip = collections.Counter()
out = []
for k, p in inp.items():
    if k not in sus:
        continue
    e = snap.get(k, {})
    if e.get('unit'):
        skip['unit'] += 1; continue
    if '#' in k:
        skip['homograph key'] += 1; continue
    if propn.learnable(k, names):
        skip['learnable name'] += 1; continue
    out.append({'lemma': k, 'rank': int(p[1]), 'freq': int(p[2]), 'pos': p[3],
                'forms': [f.strip() for f in p[4].split(',')], 'unit': None,
                'flags': 'screeners: ' + ' / '.join(r for r in sus[k] if r) or 'screeners: suspect',
                'both': len(sus[k]) == 2})
json.dump(out, open(Path(__file__).parent / 'cands.json', 'w'), ensure_ascii=False)
print(len(inp), 'inputs;', len(missing), 'not screened twice;', len(sus), 'suspects;', dict(skip), '->', len(out),
      'to review (both screeners:', sum(c['both'] for c in out), ')')
