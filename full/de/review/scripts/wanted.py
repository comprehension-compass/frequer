"""wanted.json for examples.py: per lemma, the surface forms carrying >= 10 % of its occurrences (argv: items.json out.json)."""
import json, pickle, sys
L = pickle.load(open('/home/user/merged-de.pkl', 'rb')).merged.lemmas
items = json.load(open(sys.argv[1])); out = {}
for lem in items:
    st = L.get(lem)
    forms = [f for f, n in st.forms.most_common(5) if n >= 0.1 * st.freq] if st and st.forms else []
    b = lem.split('#')[0].lower()
    out[lem] = forms or ([b] if ' ' not in b else [])
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False)
