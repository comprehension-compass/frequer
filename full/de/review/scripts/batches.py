import json, sys
from pathlib import Path
S = Path(sys.argv[1]); size = int(sys.argv[2]); tag = sys.argv[3]
items = json.load(open(S / 'items.json')); ex = json.load(open(S / 'examples.json'))
order = sorted(items.values(), key=lambda x: int(x['rank']) if x['rank'] != '-' else 10**9)
d = S / f'review-{tag}'; d.mkdir(exist_ok=True)
for b in range(0, len(order), size):
    chunk = order[b:b + size]
    lines = [f"# Batch {b // size + 1:02d}: {len(chunk)} lemmas. One decision line per lemma, in this order.\n"]
    for x in chunk:
        lines.append(f"## {x['lemma']}\nrank {x['rank']}, frequency {x['freq']}, POS {x['pos'] or '-'}\n"
                     f"flags: {x['flags']}\nexamples:")
        for s in ex.get(x['lemma'], [])[:3]:
            lines.append(f"  - {s}")
        if not ex.get(x['lemma']):
            lines.append("  - (no example found in the sample)")
        lines.append("")
    (d / f"batch{b // size + 1:02d}.md").write_text("\n".join(lines), encoding='utf-8')
print(len(order), 'items in', (len(order) + size - 1) // size, 'batches')
