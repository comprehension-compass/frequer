import json
from pathlib import Path
from frequer.config import load_manifest
from frequer.merge import merge_counts
W = "muell personalizabl ofrecerl dobl encuentr brindarl puzl descargabl prorock-perforación enseñarl proporcionarl multipl azafr increibl mostrarl coleccionabl start-ups al-tec psiquiatr".split()
m = load_manifest('es')
res = merge_counts(Path('/home/user/data-base/es/counts'), m.parts, 160_000)
out = {w: dict(res.merged.lemmas[w].forms.most_common(4)) for w in W if w in res.merged.lemmas}
json.dump(out, open('/tmp/claude-0/-home-user-frequer/0d494a33-43f2-555c-9abe-5ddab495db09/scratchpad/drops/forms.json', 'w'), ensure_ascii=False)
print(json.dumps(out, ensure_ascii=False))
