"""Sentence-position case tally for capitalised surface forms of PROPN-majority lemmas.
Re-reads the counted sample (ParaCrawl en-es, Spanish column, stride 28 offset 0, the first
~700M kept characters = the 35 counted shards; Tatoeba spa whole). Tokenizer only, no lemmatiser."""
import bz2, gzip, json, re, subprocess, sys, collections
rank = json.load(gzip.open('ranking.json.gz', 'rt', encoding='utf-8'))
watch = set()
for o in rank:
    if o['forms']:
        for f in o['forms']:
            if f[:1].isupper() and ' ' not in f:
                watch.add(f)
print(len(watch), 'watched forms', flush=True)
WORD = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
END = set('.!?…:;')
tally = collections.defaultdict(lambda: [0, 0, 0])  # surface -> [initial, mid in running text, mid in a title-case line]
def titlecase(line):
    words = [w for w in WORD.findall(line) if len(w) > 3]
    return len(words) >= 2 and sum(w[:1].isupper() for w in words) >= 0.6 * len(words)
def scan(line):
    title = titlecase(line)
    prev_end = 0
    initial = True
    for m in WORD.finditer(line):
        gap = line[prev_end:m.start()]
        if prev_end and any(c in END for c in gap):
            initial = True
        w = m.group()
        if w in watch:
            tally[w][0 if initial else (2 if title else 1)] += 1
        initial = False
        prev_end = m.end()
# Tatoeba
t = subprocess.run(['curl', '-sS', 'https://downloads.tatoeba.org/exports/per_language/spa/spa_sentences.tsv.bz2'], capture_output=True).stdout
for line in bz2.decompress(t).decode('utf-8', 'replace').splitlines():
    p = line.split('\t')
    if len(p) >= 3: scan(p[2])
print('tatoeba done', flush=True)
p = subprocess.Popen(['curl', '-sS', 'https://web-language-models.s3.amazonaws.com/paracrawl/release9/en-es/en-es.txt.gz'], stdout=subprocess.PIPE)
g = gzip.GzipFile(fileobj=p.stdout)
kept = 0; BUDGET = 35 * 20_000_000
for n, raw in enumerate(g):
    if (n // 50) % 28:
        continue
    cols = raw.decode('utf-8', 'replace').rstrip('\n').split('\t')
    if len(cols) < 2: continue
    s = cols[1]; kept += len(s); scan(s)
    if kept >= BUDGET: break
    if n % 20_000_000 == 0: print(n, kept, flush=True)
p.kill()
with gzip.open('case-tally2.tsv.gz', 'wt', encoding='utf-8') as f:
    f.write(f'# surface\tsentence_initial\tmid_sentence_running_text\tmid_sentence_title_case_line  (ParaCrawl stride 28 offset 0, {kept:,} chars; Tatoeba spa)\n')
    for w, (a, b, c) in sorted(tally.items()):
        f.write(f'{w}\t{a}\t{b}\t{c}\n')
print('done', n, kept, len(tally))
