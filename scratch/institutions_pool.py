"""Pool for the famous-institutions re-decision: earlier review drops + auto proper-noun drops in the 30k window."""
import json, sys
from pathlib import Path
from frequer import filters, config
from frequer.merge import merge_counts
from frequer.ranking import build_rows
S = Path(sys.argv[1])
m = config.load_manifest('es')
res = merge_counts(Path('/home/user/data-base/es/counts'), m.parts, 200000)
w = {s.name: s.weight for s in m.sources}
flt = filters.apply(m, res.merged, w)
kept = 0; win = []
for r in flt.routed:
    win.append(r); kept += r.action in ('keep', 'review-keep', 'pending', 'pending-names')
    if kept >= 30000: break
rev = flt.review.decisions
out = []
for r in win:
    if r.action in ('propn-drop', 'review-drop'):
        st = res.merged.lemmas[r.lemma]
        forms = [f for f, _ in sorted(st.forms.items(), key=lambda kv: -kv[1])[:3]]
        why = rev[r.lemma][1] if r.action == 'review-drop' else 'auto: proper noun'
        out.append([r.lemma, r.rank, st.freq, ', '.join(forms), why])
json.dump(out, open(S / 'pool.json', 'w'), ensure_ascii=False)
print(len(win), 'window;', len(out), 'pool', sum(1 for o in out if o[4] != 'auto: proper noun'), 'review drops')
