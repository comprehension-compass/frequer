import json, gzip, random, collections
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
from frequer import filters, snapshot
m = load_manifest('es')
res = merge_counts(Path('/home/user/data-base/es/counts'), m.parts, 120_000)
flt = filters.apply(m, res.merged, {s.name: s.weight for s in m.sources})
KEPT = ("keep", "review-keep", "pending", "pending-names")
pos = 0; bands = [(0,10000),(10000,20000),(20000,25000),(25000,30000)]
stat = {b: collections.Counter() for b in bands}
excl_ranks = sorted(d.rank for d in flt.excluded)
keeps = {b: [] for b in bands}
stats = {r.lemma: r.stats for r in flt.ranked}
for r in flt.routed:
    b = next((b for b in bands if b[0] <= pos < b[1]), None)
    if b is None: break
    stat[b][r.action] += 1
    if r.action in KEPT:
        pos += 1
        st = stats.get(r.lemma)
        keeps[b].append((pos, r.lemma, r.action, st.freq if st else None, snapshot.majority(st.pos, 'X') if st else '?'))
json.dump({'stat': {f"{a}-{b}": dict(v) for (a, b), v in stat.items()}, 'keeps': {f"{a}-{b}": v for (a, b), v in keeps.items()},
           'excluded_total': len(flt.excluded), 'merges': len(flt.merges)},
          open('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/bands.json', 'w'), ensure_ascii=False)
print('ok')
