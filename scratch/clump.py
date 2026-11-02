import json, math, gzip
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
from frequer.snapshot import majority
m = load_manifest('es')
res = merge_counts(Path('/home/user/data-base/es/counts'), m.parts, 80_000)
N = res.merged.docs
rows = sorted(res.merged.lemmas.items(), key=lambda kv: -kv[1].freq)
out = []
for i, (l, st) in enumerate(rows, 1):
    exp = N * (1 - math.exp(-st.freq / N))
    out.append((i, l, st.freq, st.df, round(st.df / exp, 3), majority(st.pos, 'X'), round(st.by_source.get('tatoeba-spa', 0) / st.freq, 3)))
json.dump({'N': N, 'rows': out}, gzip.open('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/clump.json.gz', 'wt'))
print(N, len(out))
