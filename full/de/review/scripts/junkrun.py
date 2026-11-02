"""Merge the de counts once (cached), then run frequer's filters and write every ranked lemma's flags/action."""
import pickle, sys, time
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
from frequer import filters, snapshot
CACHE = Path('/home/user/merged-de.pkl')
m = load_manifest('de')
if not CACHE.exists():
    t = time.time()
    r = merge_counts(Path('/home/user/data/de/counts'), m.parts, m.language.top_n * 4)
    pickle.dump(r, CACHE.open('wb'), protocol=5)
    print('merged in', time.time() - t)
r = pickle.load(CACHE.open('rb'))
weights = {s.name: s.weight for s in m.sources}
flt = filters.apply(m, r.merged, weights, root=Path('/home/user/he-c07c7015'),
                    cooc=Path('/home/user/data/de/cooc-merged.gz'))
out = Path(sys.argv[1])
st = r.merged.lemmas
with out.open('w') as fp:
    fp.write('rank\tlemma\tfreq\tpos\taction\tflags\n')
    for x in flt.routed:
        s = st[x.lemma]
        fp.write(f"{x.rank}\t{x.lemma}\t{s.freq}\t{snapshot.majority(s.pos, 'X')}\t{x.action}\t"
                 + " | ".join(f"{a}: {b}" for a, b in x.flags) + "\n")
with out.with_suffix('.merges.tsv').open('w') as fp:
    for mg in flt.merges:
        fp.write(f"{mg.source}\t{mg.target}\t{mg.source_freq}\t{mg.evidence}\n")
with out.with_suffix('.excluded.tsv').open('w') as fp:
    for x in flt.excluded:
        f = st[x.lemma].freq if x.lemma in st else ''
        fp.write(f"{x.rank}\t{x.lemma}\t{f}\t{x.cls}\t{x.reason}\n")
print('merges', len(flt.merges), 'kept', len(flt.ranked), 'excluded', len(flt.excluded))
