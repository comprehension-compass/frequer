"""Example sentences for review candidates, from Tatoeba (whole) and the head of a ParaCrawl pair.

Usage: python review/scripts/examples.py <round-dir> <tatoeba-code> <paracrawl-pair> [--side 1]
  e.g. python review/scripts/examples.py work/r9 spa en-es

Reads <round-dir>/cands.json ([{lemma, forms}, ...]); writes <round-dir>/examples.json ({lemma: [sentence, ...]}):
one Tatoeba sentence and up to three ParaCrawl sentences per lemma (every 7th line of the first ~700 MB, compressed),
matched on any of the lemma's surface forms (lower-cased); a multi-word lemma matches as a substring. Nothing is
committed: the sentences go only into the reviewers' input files.
"""

import argparse
import bz2
import collections
import gzip
import json
import re
import subprocess
from pathlib import Path

TATOEBA = "https://downloads.tatoeba.org/exports/per_language/{code}/{code}_sentences.tsv.bz2"
PARACRAWL = "https://web-language-models.s3.amazonaws.com/paracrawl/release9/{pair}/{pair}.txt.gz"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("round_dir", type=Path)
    ap.add_argument("tatoeba_code")
    ap.add_argument("paracrawl_pair")
    ap.add_argument("--side", type=int, default=1, help="column of the target language in the ParaCrawl pair")
    ap.add_argument("--bytes", type=int, default=700_000_000)
    a = ap.parse_args()
    cands = json.loads((a.round_dir / "cands.json").read_text())
    want: dict[str, set[str]] = collections.defaultdict(set)
    for r in cands:
        for f in r.get("forms") or [r["lemma"]]:
            want[f.lower()].add(r["lemma"])
    multi = {r["lemma"]: r["lemma"].lower() for r in cands if " " in r["lemma"] and "+" not in r["lemma"]}
    ex: dict[str, list[str]] = collections.defaultdict(list)
    tok = re.compile(r"[\w'-]+", re.U)

    def scan(line: str, cap: int) -> None:
        if not 25 <= len(line) <= 300:
            return
        low = line.lower()
        seen: set[str] = set()
        for t in tok.findall(low):
            for lem in want.get(t, ()):
                if lem not in seen and len(ex[lem]) < cap and line not in ex[lem]:
                    ex[lem].append(line)
                    seen.add(lem)
        for lem, m in multi.items():
            if len(ex[lem]) < cap and m in low and line not in ex[lem]:
                ex[lem].append(line)

    raw = subprocess.run(["curl", "-sS", TATOEBA.format(code=a.tatoeba_code)], capture_output=True, check=True).stdout
    for line in bz2.decompress(raw).decode("utf-8", "replace").splitlines():
        p = line.split("\t")
        if len(p) >= 3:
            scan(p[2], 1)
    proc = subprocess.Popen(["curl", "-sS", "-r", f"0-{a.bytes}", PARACRAWL.format(pair=a.paracrawl_pair)],
                            stdout=subprocess.PIPE)
    n = 0
    try:
        for line_b in gzip.GzipFile(fileobj=proc.stdout):
            n += 1
            if n % 7:
                continue
            parts = line_b.decode("utf-8", "replace").rstrip("\n").split("\t")
            if len(parts) > a.side:
                scan(parts[a.side], 3)
    except (EOFError, OSError):
        pass  # the byte range ends mid-stream
    (a.round_dir / "examples.json").write_text(json.dumps(ex, ensure_ascii=False, indent=0))
    print(n, "lines;", sum(1 for r in cands if ex.get(r["lemma"])), "of", len(cands), "lemmas with examples")


if __name__ == "__main__":
    main()
