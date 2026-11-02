"""Example sentences for review: stream HPLT de + Tatoeba, keep up to K sentences per wanted lemma.

The wanted forms must be only those carrying a real share of the lemma (>= 10 % of its occurrences): matching a
rare form with equal weight made German *Ofen* sentences the examples for the English lemma *of* (2026-11-02).

argv: wanted.json ({lemma: [lower-case forms]}), out.json, chars_per_url. Never committed (web text).
"""
import json, re, sys, random
from frequer.config import load_manifest
from frequer.sources import open_raw, decompress, iter_docs
K = 3
wanted = json.load(open(sys.argv[1]))
cap = int(sys.argv[3])
form2lem = {}
for lem, forms in wanted.items():
    for f in forms:
        form2lem.setdefault(f, set()).add(lem)
out = {lem: [] for lem in wanted}
seen_docs = {lem: set() for lem in wanted}
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ"„])')
WORD = re.compile(r"[\wäöüÄÖÜß]+(?:-[\wäöüÄÖÜß]+)*")
m = load_manifest('de')
srcs = {s.name: s for s in m.sources}
plan = [('tatoeba-deu', 0, 40_000_000)] + [('hplt-v2-de', k, cap) for k in (1, 6, 11, 16, 3, 8, 13)]
for name, k, limit in plan:
    src = srcs[name]
    url = src.urls[k]
    raw = open_raw(url); stream = decompress(raw, url)
    read = 0
    for doc in iter_docs(src, k, stream):
        for line in doc.lines:
            read += len(line)
            for sent in SENT.split(line):
                if not 25 <= len(sent) <= 220:
                    continue
                for w in set(WORD.findall(sent.lower())):
                    for lem in form2lem.get(w, ()):
                        if len(out[lem]) < K and doc.doc_id not in seen_docs[lem]:
                            out[lem].append(sent.strip()); seen_docs[lem].add(doc.doc_id)
        if read >= limit:
            break
    stream.close(); raw.close()
    full = sum(1 for v in out.values() if len(v) >= K)
    print(name, k, read, 'lemmas with', K, ':', full, 'of', len(out), flush=True)
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False)
