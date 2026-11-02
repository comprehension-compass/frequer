"""Word samples per band, for the developer's cutoff decision (ruling 2026-11-02): ``band-samples.md``.

    python band_samples.py <config.json> [--compare other.json ...] [--gloss] [--per-band 40] [--cut 30000]
                           [--deeper 35000] [--seed 11]

The developer chooses the cutoff from words, not from a real-word percentage (the list is filtered anyway). From
routed.tsv (kept positions: keep, review-keep, pending-names, pending), it writes <work>/band-samples.md with:

* per band (config ``bands``): ``--per-band`` random kept words with POS and frequency;
* **just above the cut**: the last 60 kept words before ``--cut``;
* **what a deeper cut adds**: ``--per-band`` random kept words between ``--cut`` and ``--deeper``;
* **across languages**: 15 words around each band edge for this language and every ``--compare`` config, side
  by side, so the same position can be compared.

``--gloss`` adds a short English gloss per word, written by the reviewer model (headless ``claude -p``, cached
under <work>/glosses/). Glosses are an aid for reading the samples, marked as model-written; they decide nothing.
Copy the result to ``full/<code>/band-samples.md`` on the build branch with the developer's ruling.
"""

from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Any

from common import KEPT, claude, load, routed_rows

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config")
ap.add_argument("--compare", nargs="*", default=[], help="other languages' configs (their routed.tsv)")
ap.add_argument("--gloss", action="store_true")
ap.add_argument("--per-band", type=int, default=40)
ap.add_argument("--cut", type=int, default=30000)
ap.add_argument("--deeper", type=int, default=35000)
ap.add_argument("--seed", type=int, default=11)
args = ap.parse_args()
cfg = load(args.config)
others = [load(c) for c in args.compare]
bands = [tuple(b) for b in cfg.get("bands", [(0, 10000), (10000, 20000), (20000, 25000), (25000, 30000)])]
rng = random.Random(args.seed)


def kept_words(c: dict[str, Any]) -> list[tuple[int, str, str, int]]:
    """(kept position, lemma, POS, frequency) for every kept lemma, in list order."""
    return [(int(kept), lemma, pos, int(freq)) for _r, lemma, action, freq, pos, _f, _fl, kept in routed_rows(c)
            if action in KEPT]


def gloss_map(c: dict[str, Any], words: list[tuple[int, str, str, int]]) -> dict[str, str]:
    if not args.gloss:
        return {}
    todo = sorted({(w, pos) for _k, w, pos, _f in words})
    out: dict[str, str] = {}
    for i in range(0, len(todo), 200):
        batch = todo[i:i + 200]
        prompt = (f"Give a short English gloss (2-5 words) for each {c['language_name']} word below, as a learner's "
                  "dictionary would; for a name, say what it names. Answer one line per word, exactly "
                  "`<word>\\t<gloss>`, the word copied exactly, nothing else.\n\n"
                  + "\n".join(f"{w}\t{pos}" for w, pos in batch))
        text = claude(c, c["reviewer_model"], prompt, c["work"] / "glosses" / f"{len(todo)}-{i:05d}.txt")
        wanted = {w for w, _p in batch}
        for line in text.splitlines():
            parts = line.strip().strip("`").split("\t")
            if len(parts) >= 2 and parts[0] in wanted:
                out[parts[0]] = parts[1].strip()
    return out


def table(rows: list[tuple[int, str, str, int]], gl: dict[str, str]) -> list[str]:
    head = "| position | word | POS | frequency |" + (" gloss (model-written) |" if args.gloss else "")
    out = [head, "|---:|---|---|---:|" + ("---|" if args.gloss else "")]
    for k, w, pos, f in rows:
        out.append(f"| {k:,} | {w} | {pos} | {f:,} |" + (f" {gl.get(w, '')} |" if args.gloss else ""))
    return out


mine = kept_words(cfg)
picks: dict[str, list[tuple[int, str, str, int]]] = {}
for lo, hi in bands:
    pool = [w for w in mine if lo < w[0] <= hi]
    picks[f"{lo:,}-{hi:,}"] = sorted(rng.sample(pool, min(args.per_band, len(pool))))
above = [w for w in mine if args.cut - 60 < w[0] <= args.cut]
deeper_pool = [w for w in mine if args.cut < w[0] <= args.deeper]
deeper = sorted(rng.sample(deeper_pool, min(args.per_band, len(deeper_pool))))
edges = [hi for _lo, hi in bands]


def around(words: list[tuple[int, str, str, int]], edge: int) -> list[tuple[int, str, str, int]]:
    return [w for w in words if edge - 7 <= w[0] <= edge + 7]


shown = [w for v in picks.values() for w in v] + above + deeper + [w for e in edges for w in around(mine, e)]
gl = gloss_map(cfg, shown)
out = [f"# {cfg['lang']}: word samples per band, for the cutoff", "",
       "Positions are places in the cleaned list (kept lemmas only). The developer chooses the cutoff from these "
       "words and the comparison across languages; this file decides nothing."
       + (" Glosses are written by a model as a reading aid." if args.gloss else ""), ""]
for name, rows in picks.items():
    out += [f"## Band {name}: {len(rows)} random words", "", *table(rows, gl), ""]
out += [f"## Just above the cut ({args.cut:,}): the last {len(above)} words", "", *table(above, gl), ""]
out += [f"## What a cut at {args.deeper:,} adds: {len(deeper)} random words of {len(deeper_pool):,}", "",
        *table(deeper, gl), ""]
langs = [(cfg, mine, gl)]
for o in others:
    words = kept_words(o)
    langs.append((o, words, gloss_map(o, [x for e in edges for x in around(words, e)])))
if others:
    out += ["## Across languages at the same positions", ""]
    for e in edges:
        out += [f"### Around {e:,}", "", "| position | " + " | ".join(c["lang"] for c, _w, _g in langs) + " |",
                "|---:|" + "---|" * len(langs)]
        cols = [{w[0]: w[1] + (f" ({g[w[1]]})" if w[1] in g else "") for w in around(words, e)}
                for _c, words, g in langs]
        for k in range(e - 7, e + 8):
            out.append(f"| {k:,} | " + " | ".join(col.get(k, "") for col in cols) + " |")
        out.append("")
path = Path(cfg["work"]) / "band-samples.md"
path.write_text("\n".join(out) + "\n", encoding="utf-8")
print(path, len(out), "lines")
