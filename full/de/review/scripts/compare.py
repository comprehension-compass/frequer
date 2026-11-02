import json, re, sys
from pathlib import Path
S = Path(sys.argv[1]); tag = sys.argv[2]; size = int(sys.argv[3])
d = S / f'review-{tag}'
def load(p):
    out, qs = {}, []
    for line in p.read_text(encoding='utf-8').splitlines():
        if line.startswith('#'):
            if 'question' in line: qs.append(line)
            continue
        parts = line.split('\t')
        if len(parts) >= 2 and parts[0].strip():
            out[parts[0].strip()] = (parts[1].strip(), parts[2].strip() if len(parts) > 2 else '')
    return out, qs
items = json.load(open(S / 'items.json')); ex = json.load(open(S / 'examples.json'))
agreed, dis, qa, missing = {}, [], [], []
for bf in sorted(d.glob('batch*.md')):
    names = re.findall(r'^## (.+)$', bf.read_text(encoding='utf-8'), re.M)
    a, qa1 = load(d / 'A' / (bf.stem + '.tsv')); b, qb1 = load(d / 'B' / (bf.stem + '.tsv'))
    qa += qa1 + qb1
    for n in names:
        if n not in a or n not in b:
            missing.append((bf.stem, n, n in a, n in b)); continue
        if a[n][0] == b[n][0]:
            agreed[n] = a[n]
        else:
            dis.append((n, a[n], b[n]))
print('agreed', len(agreed), 'disagree', len(dis), 'missing', len(missing))
json.dump({'agreed': agreed, 'dis': dis, 'questions': qa, 'missing': missing}, open(d / 'compare.json', 'w'), ensure_ascii=False)
adj = d / 'adjudicate'; adj.mkdir(exist_ok=True)
for i in range(0, len(dis), size):
    lines = []
    for n, x, y in dis[i:i + size]:
        it = items[n]
        lines.append(f"## {n}\nrank {it['rank']}, frequency {it['freq']}, POS {it['pos'] or '-'}\nflags: {it['flags']}\n"
                     f"reviewer 1: {x[0]} ({x[1]})\nreviewer 2: {y[0]} ({y[1]})\nexamples:")
        lines += [f"  - {s}" for s in ex.get(n, [])[:3]] or ["  - (none)"]
        lines.append("")
    (adj / f"adj{i // size + 1:02d}.md").write_text("\n".join(lines), encoding='utf-8')
print('adjudication files', (len(dis) + size - 1) // size)
