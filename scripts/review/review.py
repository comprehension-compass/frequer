"""Two independent reviewers per lemma, then an adjudicator for their disagreements (headless claude -p).

    python review.py <config.json> <queue.jsonl> <round-name>

Each reviewer call sees the rules (config "rules") and a batch of lemmas, each with its rank, frequency,
POS, flags and evidence, written forms and examples; never the other reviewer's answers. The adjudicator sees
the rules, the lemma and both answers. Writes <work>/review/<round>/{A,B,adjudication}/batch-NNN.txt (cached:
a rerun resumes), decisions.tsv (lemma, decision, reason, agreed|adjudicated|undecided, rank) and
questions.txt. Decisions: keep, drop, pending-names, merge:<lemma>.
"""

from __future__ import annotations

import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from common import claude, load

cfg = load(sys.argv[1])
RULES = Path(cfg["rules"]).read_text(encoding="utf-8")
BATCH, ADJ_BATCH, PAR = 40, 30, cfg["parallel"]
SYSTEM = (f"You are a careful reviewer of a {cfg.get('language_name', cfg['lang'])} learner's frequency list. "
          "Follow the rules exactly and answer only in the format asked.")
DEC = re.compile(r"^(keep|drop|pending-names|merge:\S+)$")
FORMAT = ("\n\nAnswer with one line per lemma, in the order given, exactly `<lemma>\\t<decision>\\t<short reason>`, "
          "the lemma copied exactly as given after ###, the decision one of keep, drop, pending-names, "
          "merge:<lemma>. Then any `# question <lemma>: ...` lines. Nothing else: no preamble, no table.")
queue = [json.loads(line) for line in open(sys.argv[2], encoding="utf-8")]
rnd = cfg["work"] / "review" / sys.argv[3]


def entry(q: dict[str, Any]) -> str:
    ex = "\n".join(f"  - {e}" for e in q["examples"]) or "  - (no example found in the sample)"
    forms = ", ".join(f"{f.replace(' ', '')} ({n:,})" for f, n in q["forms"].items())
    return (f"### {q['lemma']}\nrank {q['rank']:,}; frequency {q['freq']:,}; tagged {q['pos']}\n"
            f"flags: {q['flags'] or 'none'}\nwritten as: {forms}\nexamples:\n{ex}\n")


def parse(text: str, lemmas: set[str]) -> tuple[dict[str, tuple[str, str]], list[str]]:
    got: dict[str, tuple[str, str]] = {}
    questions: list[str] = []
    for line in text.splitlines():
        line = line.strip().strip("`")
        if line.startswith("# question"):
            questions.append(line)
            continue
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0].strip() in lemmas and DEC.match(parts[1].strip()):
            got[parts[0].strip()] = (parts[1].strip(), parts[2].strip() if len(parts) > 2 else "")
    return got, questions


def ask(batch: list[dict[str, Any]], path: Path, head: str = "", extra: Any = None) -> tuple[dict, list]:
    body = "\n".join(entry(q) + (extra(q) if extra else "") for q in batch)
    return parse(claude(cfg, cfg["adjudicator_model"] if extra else cfg["reviewer_model"],
                        head + RULES + "\n\n# Lemmas\n\n" + body + FORMAT, path, SYSTEM), {q["lemma"] for q in batch})


def reviewer(who: str, batches: list[list[dict[str, Any]]]) -> tuple[dict, list]:
    def one(i: int) -> tuple[dict, list]:
        got, qs = ask(batches[i], rnd / who / f"batch-{i:03d}.txt")
        missing = [q for q in batches[i] if q["lemma"] not in got]
        if missing:  # ask again for the lemmas the answer skipped
            more, qs2 = ask(missing, rnd / who / f"batch-{i:03d}-retry.txt")
            got.update(more)
            qs += qs2
        return got, qs

    with ThreadPoolExecutor(PAR) as ex:
        res = list(ex.map(one, range(len(batches))))
    return {k: v for g, _ in res for k, v in g.items()}, [q for _, qs in res for q in qs]


batches = [queue[i:i + BATCH] for i in range(0, len(queue), BATCH)]
with ThreadPoolExecutor(2) as ex:
    fa, fb = ex.submit(reviewer, "A", batches), ex.submit(reviewer, "B", batches)
    (da, qa), (db, qb) = fa.result(), fb.result()
by = {q["lemma"]: q for q in queue}
agree = {k: da[k] for k in by if k in da and k in db and da[k][0] == db[k][0]}
dis = [by[k] for k in by if k not in agree]
HEAD = ("You are the adjudicator. Two independent reviewers disagreed on each lemma below. Apply the rules and "
        "settle each case.\n\n")


def both(q: dict[str, Any]) -> str:
    a, b = da.get(q["lemma"], ("(none)", "")), db.get(q["lemma"], ("(none)", ""))
    return f"reviewer 1: {a[0]} ({a[1]})\nreviewer 2: {b[0]} ({b[1]})\n"


ab = [dis[i:i + ADJ_BATCH] for i in range(0, len(dis), ADJ_BATCH)]
adj: dict[str, tuple[str, str]] = {}
qadj: list[str] = []
with ThreadPoolExecutor(PAR) as ex:
    for g, q in ex.map(lambda i: ask(ab[i], rnd / "adjudication" / f"batch-{i:03d}.txt", HEAD, both),
                       range(len(ab))):
        adj.update(g)
        qadj += q
with (rnd / "decisions.tsv").open("w", encoding="utf-8") as fp:
    for q in queue:
        k = q["lemma"]
        d, why, how = (*agree[k], "agreed") if k in agree else (*adj[k], "adjudicated") if k in adj \
            else ("", "", "undecided")
        fp.write(f"{k}\t{d}\t{why}\t{how}\t{q['rank']}\n")
(rnd / "questions.txt").write_text("\n".join(sorted(set(qa + qb + qadj))) + "\n", encoding="utf-8")
print(json.dumps({"lemmas": len(by), "agreed": len(agree), "adjudicated": len(adj),
                  "undecided": len(by) - len(agree) - len(adj)}))
