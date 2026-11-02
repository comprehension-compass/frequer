"""File plumbing for one review round (review/README.md). Copies, merges and checks only: no decisions.

  round.py triage-chunks <round> <ranked.tsv> --chunks 2        screener inputs: <round>/t{A,B}<i>/input.tsv
  round.py union <round> --snapshot es.json --names <he>/reference/learnable-names/es.json
                                                                 triage outputs -> <round>/cands.json
  round.py inputs <round> --chunks 4                             reviewer inputs: <round>/r{A,B}<i>/input.tsv
  round.py agree <round>                                         -> merged.json, adj/disagreements.tsv, adj/questions.txt
  round.py apply <round> <corpora/review/xx.tsv> --label "..."   agreed + adj/decisions.tsv -> appended to the review file

A ranked.tsv for triage has a header line and the columns: lemma, list position, frequency, pos, commonest forms.
Every output file is `lemma<TAB>decision<TAB>reason`, plus `# question <lemma>: ...` lines.
"""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

TRIAGE_HEAD = "# lemma\tlist position\tfrequency\tpos\tcommonest surface forms\n"
REVIEW_HEAD = ("# lemma\tlist position\tfrequency\tpos\tcommonest forms\tscreeners' notes\t"
               'examples from the counted text (" || " between)\n')


def _chunks(items: list[str], n: int) -> list[list[str]]:
    size = -(-len(items) // n)
    return [items[i * size:(i + 1) * size] for i in range(n)]


def triage_chunks(rnd: Path, ranked: Path, n: int) -> None:
    rows = [line for line in ranked.read_text(encoding="utf-8").splitlines(keepends=True) if not line.startswith("#")]
    for side in "AB":  # two independent screeners see every row
        for i, part in enumerate(_chunks(rows, n), start=1):
            d = rnd / f"t{side}{i}"
            d.mkdir(parents=True, exist_ok=True)
            (d / "input.tsv").write_text(TRIAGE_HEAD + "".join(part), encoding="utf-8")
    print(len(rows), "rows,", n, "chunks per screener")


def _read_decisions(paths: list[Path]) -> tuple[dict[str, tuple[str, str]], list[str]]:
    out: dict[str, tuple[str, str]] = {}
    questions: list[str] = []
    for p in paths:
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("#"):
                if "question" in line:
                    questions.append(line.strip())
                continue
            f = line.split("\t")
            if len(f) >= 2:
                out[f[0]] = (f[1].strip(), f[2].strip() if len(f) > 2 else "")
    return out, questions


def union(rnd: Path, snapshot: Path, names: Path) -> None:
    """Union of both screeners' suspects, minus the release's own entries (units, homograph keys, learnable names)."""
    lemmas = json.loads(snapshot.read_text())["lemmas"]
    learnable = {n.casefold() for n in json.loads(names.read_text())["names"]}
    inp: dict[str, list[str]] = {}
    for d in sorted(rnd.glob("tA*")):
        for line in (d / "input.tsv").read_text(encoding="utf-8").splitlines():
            if not line.startswith("#"):
                f = line.split("\t")
                inp[f[0]] = f
    seen: collections.Counter[str] = collections.Counter()
    notes: dict[str, list[str]] = collections.defaultdict(list)
    for d in sorted(rnd.glob("t[AB]*")):
        out, _q = _read_decisions([d / "output.tsv"])
        for k, (verdict, why) in out.items():
            if k in inp:
                seen[k] += 1
                if verdict == "suspect":
                    notes[k].append(why)
    missing = [k for k in inp if seen[k] < 2]
    if missing:
        raise SystemExit(f"{len(missing)} rows not screened twice (first: {missing[:5]}); finish the triage first")
    skip: collections.Counter[str] = collections.Counter()
    cands = []
    for k, f in inp.items():
        if k not in notes:
            continue
        if lemmas.get(k, {}).get("unit"):
            skip["unit"] += 1
        elif "#" in k:
            skip["homograph key"] += 1
        elif k.split("#")[0].casefold() in learnable:
            skip["learnable name"] += 1
        else:
            cands.append({"lemma": k, "rank": int(f[1]), "freq": int(f[2]), "pos": f[3],
                          "forms": [x.strip() for x in f[4].split(",")],
                          "flags": "screeners: " + " / ".join(n for n in notes[k] if n)})
    (rnd / "cands.json").write_text(json.dumps(cands, ensure_ascii=False))
    print(len(inp), "screened;", len(notes), "suspect;", dict(skip), "->", len(cands), "to review")


def inputs(rnd: Path, n: int) -> None:
    cands = json.loads((rnd / "cands.json").read_text())
    ex = json.loads((rnd / "examples.json").read_text())
    rows = ["\t".join([c["lemma"], str(c["rank"]), str(c["freq"]), c.get("pos", ""), ", ".join(c["forms"]),
                       c.get("flags", "").replace("\t", " "),
                       " || ".join(e.replace("\t", " ")[:300] for e in ex.get(c["lemma"], []))]) + "\n"
            for c in cands]
    for side in "AB":
        for i, part in enumerate(_chunks(rows, n), start=1):
            d = rnd / f"r{side}{i}"
            d.mkdir(parents=True, exist_ok=True)
            (d / "input.tsv").write_text(REVIEW_HEAD + "".join(part), encoding="utf-8")
    print(len(rows), "lemmas,", n, "chunks per reviewer")


def agree(rnd: Path) -> None:
    a, qa = _read_decisions(sorted(rnd.glob("rA*/output.tsv")))
    b, qb = _read_decisions(sorted(rnd.glob("rB*/output.tsv")))
    inp = {}
    for p in sorted(rnd.glob("rA*/input.tsv")):
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.startswith("#"):
                inp[line.split("\t")[0]] = line
    gaps = [k for k in inp if k not in a or k not in b]
    if gaps:
        raise SystemExit(f"{len(gaps)} lemmas lack a decision from a reviewer (first: {gaps[:5]})")
    agreed = {k: a[k] for k in inp if a[k][0] == b[k][0]}
    dis = [k for k in inp if k not in agreed]
    (rnd / "adj").mkdir(exist_ok=True)
    with (rnd / "adj" / "disagreements.tsv").open("w", encoding="utf-8") as fp:
        fp.write(REVIEW_HEAD.rstrip("\n") + "\treviewer 1\treason 1\treviewer 2\treason 2\n")
        for k in dis:
            fp.write(inp[k] + "\t" + "\t".join(a[k] + b[k]) + "\n")
    (rnd / "adj" / "questions.txt").write_text("\n".join(sorted(set(qa + qb))) + "\n", encoding="utf-8")
    (rnd / "merged.json").write_text(json.dumps({"A": a, "B": b, "agree": agreed}, ensure_ascii=False))
    print(len(agreed), "agreed", dict(collections.Counter(v[0].split(":")[0] for v in agreed.values())),
          len(dis), "to the adjudicator")


def apply(rnd: Path, review_file: Path, label: str) -> None:
    final = {k: tuple(v) for k, v in json.loads((rnd / "merged.json").read_text())["agree"].items()}
    adj, _q = _read_decisions([rnd / "adj" / "decisions.tsv"])
    final.update(adj)
    order = [c["lemma"] for c in json.loads((rnd / "cands.json").read_text())]
    if set(order) != set(final):
        raise SystemExit(f"decisions and candidates differ: {sorted(set(order) ^ set(final))[:10]}")
    have = {line.split("\t")[0] for line in review_file.read_text(encoding="utf-8").splitlines()
            if line and not line.startswith("#")}
    with review_file.open("a", encoding="utf-8") as fp:
        fp.write(f"# {label}\n")
        for k in order:
            if k not in have:  # an earlier decision stands; re-decide it by editing its line
                fp.write(f"{k}\t{final[k][0]}\t{final[k][1].replace(chr(9), ' ')}\n")
    print(dict(collections.Counter(v[0].split(":")[0] for v in final.values())), "appended to", review_file)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("triage-chunks")
    p.add_argument("round", type=Path)
    p.add_argument("ranked", type=Path)
    p.add_argument("--chunks", type=int, default=2)
    p = sub.add_parser("union")
    p.add_argument("round", type=Path)
    p.add_argument("--snapshot", type=Path, required=True)
    p.add_argument("--names", type=Path, required=True)
    p = sub.add_parser("inputs")
    p.add_argument("round", type=Path)
    p.add_argument("--chunks", type=int, default=1)
    p = sub.add_parser("agree")
    p.add_argument("round", type=Path)
    p = sub.add_parser("apply")
    p.add_argument("round", type=Path)
    p.add_argument("review_file", type=Path)
    p.add_argument("--label", required=True)
    a = ap.parse_args()
    if a.cmd == "triage-chunks":
        triage_chunks(a.round, a.ranked, a.chunks)
    elif a.cmd == "union":
        union(a.round, a.snapshot, a.names)
    elif a.cmd == "inputs":
        inputs(a.round, a.chunks)
    elif a.cmd == "agree":
        agree(a.round)
    else:
        apply(a.round, a.review_file, a.label)


if __name__ == "__main__":
    main()
