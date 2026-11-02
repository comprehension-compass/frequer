import json, gzip
from pathlib import Path
from frequer.config import load_manifest
from frequer.counts import iter_counts
from frequer.merge import merge_counts
from frequer import filters
m = load_manifest('es')
cd = Path('/home/user/data-base/es/counts')
names = sorted(p.name for _s, p in iter_counts(cd))
by_src = {}
for n in names: by_src.setdefault(n.split('.')[0], []).append(n)
A, B = set(), set()
for src, ns in by_src.items():
    for i, n in enumerate(ns): (A if i % 2 == 0 else B).add(n)
w = {s.name: s.weight for s in m.sources}
out = {}
for label, half in (('A', A), ('B', B)):
    res = merge_counts(cd, m.parts, 160_000, only=half)
    flt = filters.apply(m, res.merged, w)
    out[label] = [(r.lemma, r.stats.freq) for r in flt.ranked[:45000]]
    print(label, res.merged.tokens, len(flt.ranked), flush=True)
json.dump(out, gzip.open('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/halves.json.gz', 'wt'))
