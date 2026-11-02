import json, gzip
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
from frequer import filters, snapshot
m = load_manifest('es')
res = merge_counts(Path('/home/user/data-base/es/counts'), m.parts, 160_000)
flt = filters.apply(m, res.merged, {s.name: s.weight for s in m.sources})
act = {r.lemma: r.action for r in flt.routed}
rows = [(r.lemma, r.stats.freq, r.stats.df, snapshot.majority(r.stats.pos, 'X'), bool(snapshot.unit_kind(r.stats.kinds)), act.get(r.lemma), list(snapshot.top_forms(r.stats.forms, 3))) for r in flt.ranked[:40000]]
json.dump(rows, gzip.open('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/full30.json.gz', 'wt'), ensure_ascii=False)
print(len(flt.ranked), res.merged.docs)
