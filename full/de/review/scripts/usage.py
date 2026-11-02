import gzip, json, sys
from collections import Counter, defaultdict
snap = json.load(open('/home/user/frequer/out/de/de.json'))['lemmas']
keys = {}
for rank, (lem, e) in enumerate(snap.items(), 1):
    if rank > 35000: break
    keys.setdefault(lem.split('#')[0].lower(), (rank, lem, e.get('pos')))
DET = {'ein','eine','einen','einem','einer','eines','kein','keine','keinen','keinem','keiner','keines'}
u = Counter(); tvotes = defaultdict(Counter); det = Counter(); prev = defaultdict(Counter)
with gzip.open('/home/user/data/de/cooc-merged.gz','rt',encoding='utf-8') as fp:
    next(fp)
    for line in fp:
        kind, k, f, d = line.rstrip('\n').split('\t')
        f = int(f)
        if kind == 'u':
            if k in keys: u[k] = f
        elif kind == 't':
            key, upos = k.rsplit(' ', 1) if ' ' in k else (k, '')
            tvotes[key][upos] += f
        elif kind == 'n':
            parts = k.split(' ')
            if len(parts) == 2 and parts[1] in keys:
                if parts[0] in DET: det[parts[1]] += f
                prev[parts[1]][parts[0]] = f
adj = {k for k, c in tvotes.items() if c and c.most_common(1)[0][0] == 'ADJ'}
out = []
for k, (rank, lem, pos) in keys.items():
    if not u[k]: continue
    a = sum(f for w, f in prev[k].items() if w in adj)
    out.append((rank, lem, pos, u[k], det[k] / u[k], a / u[k]))
json.dump(out, open(sys.argv[1], 'w'))
