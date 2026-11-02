import json, gzip
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
from frequer.ranking import build_rows, rank_rows
from frequer.snapshot import majority
m = load_manifest('es')
res = merge_counts(Path('/home/user/data/es/counts'), m.parts, 200_000)
rows = rank_rows(build_rows(res.merged, {s.name: s.weight for s in m.sources}), 'frequency')
out = []
for i, r in enumerate(rows, 1):
    out.append({'rank': i, 'lemma': r.lemma, 'freq': r.stats.freq, 'pos': majority(r.stats.pos, 'X'),
                'forms': dict(r.stats.forms) if majority(r.stats.pos, 'X') == 'PROPN' else None})
with gzip.open('ranking.json.gz', 'wt', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False)
print(len(out), sum(1 for o in out if o['forms'] is not None))
