"""Two independent reviewers per lemma, then an adjudicator: headless ``claude -p``, in two stages with a check by
the orchestrating agent between them (README §A round).

    python review.py <config.json> <queue.tsv> <round> [--rules FILE] [--decisions keep,drop,...]
        Stage 1. Reviewers A and B each see the rules and batches of lemmas (rank, frequency, POS, flags or
        screeners' notes, written forms, examples), never each other's answers. Writes
        <work>/review/<round>/{A,B}/batch-NNN.txt (cached: a rerun resumes), agreed.tsv, disagreements.tsv,
        questions.txt and accent-merges.txt (agreed merges that differ from their target only by an accent or
        case: read these). Then stops.

    python review.py <config.json> <queue.tsv> <round> --adjudicate [--queries queries.tsv]
        Stage 2, after the orchestrator has read agreed.tsv (a sample of drops, every merge, accent-merges.txt).
        The adjudicator (the stronger model) decides every disagreement, plus every agreed lemma the
        orchestrator queries in queries.tsv (``lemma<TAB>why``). Writes <round>/adjudication/, decisions.tsv
        (lemma, decision, reason, agreed|adjudicated|undecided, rank) and appends its questions to questions.txt.

The scripts never decide. collect.py applies decisions.tsv to corpora/review/<lang>.tsv once the round is
complete; the questions go to the developer.
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from common import (
    DECISIONS,
    PROMPTS,
    accent_only_merges,
    agree,
    claude,
    fill,
    load,
    parse_answer,
    read_queue,
    read_tsv,
    write_tsv,
)

BATCH, ADJ_BATCH = 40, 30
ROUND_COLUMNS = ("lemma", "decision", "reason")

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("config")
ap.add_argument("queue", type=Path)
ap.add_argument("round")
ap.add_argument("--rules", help="rules file (default: config 'rules'); e.g. the unflagged or institutions rules")
ap.add_argument("--decisions", default=",".join(DECISIONS),
                help="allowed decisions (institutions: keep,drop); 'merge' admits merge:<lemma>")
ap.add_argument("--adjudicate", action="store_true", help="stage 2: the adjudicator")
ap.add_argument("--queries", type=Path, help="stage 2: agreed lemmas the orchestrator queries (lemma<TAB>why)")
args = ap.parse_args()
cfg = load(args.config)
allowed = tuple(args.decisions.split(","))
shown = ", ".join("merge:<lemma>" if d == "merge" else d for d in allowed)
RULES = Path(args.rules or cfg["rules"]).read_text(encoding="utf-8")
SYSTEM = fill((PROMPTS / "common" / "system.md").read_text(encoding="utf-8"), {"language": cfg["language_name"]})
REVIEWER = (PROMPTS / "common" / "reviewer.md").read_text(encoding="utf-8")
ADJUDICATOR = (PROMPTS / "common" / "adjudicator.md").read_text(encoding="utf-8")
queue = read_queue(args.queue)
by = {q["lemma"]: q for q in queue}
rnd = cfg["work"] / "review" / args.round


def entry(q: dict[str, Any]) -> str:
    ex = "\n".join(f"  - {e}" for e in q["examples"]) or "  - (no example found in the sample)"
    forms = ", ".join(f"{f.replace(' ', cfg.get('join', ' '))} ({n:,})" for f, n in q["forms"].items())
    return (f"### {q['lemma']}\nrank {q['rank']:,}; frequency {q['freq']:,}; tagged {q['pos']}\n"
            f"flags: {q['flags'] or 'none'}\nwritten as: {forms}\nexamples:\n{ex}\n")


def ask(template: str, model: str, batch: list[dict[str, Any]], path: Path, extra: Any = None
        ) -> tuple[dict[str, tuple[str, str]], list[str]]:
    body = "\n".join(entry(q) + (extra(q) if extra else "") for q in batch)
    prompt = fill(template, {"rules": RULES, "lemmas": body, "decisions": shown})
    return parse_answer(claude(cfg, model, prompt, path, SYSTEM), {q["lemma"] for q in batch}, allowed)


def run(who: str, template: str, model: str, items: list[dict[str, Any]], size: int, extra: Any = None
        ) -> tuple[dict[str, tuple[str, str]], list[str]]:
    batches = [items[i:i + size] for i in range(0, len(items), size)]

    def one(i: int) -> tuple[dict[str, tuple[str, str]], list[str]]:
        got, qs = ask(template, model, batches[i], rnd / who / f"batch-{i:03d}.txt", extra)
        missing = [q for q in batches[i] if q["lemma"] not in got]
        if missing:  # ask again, once, for the lemmas the answer skipped or mangled
            more, qs2 = ask(template, model, missing, rnd / who / f"batch-{i:03d}-retry.txt", extra)
            got.update(more)
            qs += qs2
        return got, qs

    with ThreadPoolExecutor(cfg["parallel"]) as ex:
        res = list(ex.map(one, range(len(batches))))
    return {k: v for g, _ in res for k, v in g.items()}, [q for _, qs in res for q in qs]


def read_side(name: str) -> dict[str, tuple[str, str]]:
    return {r["lemma"]: (r["decision"], r["reason"]) for r in read_tsv(rnd / f"{name}.tsv", ROUND_COLUMNS)}


if not args.adjudicate:
    with ThreadPoolExecutor(2) as ex:  # A and B in parallel; neither sees the other
        fa = ex.submit(run, "A", REVIEWER, cfg["reviewer_model"], queue, BATCH)
        fb = ex.submit(run, "B", REVIEWER, cfg["reviewer_model"], queue, BATCH)
        (da, qa), (db, qb) = fa.result(), fb.result()
    agreed, dis = agree(by, da, db)
    for side, d in (("A", da), ("B", db)):
        write_tsv(rnd / f"{side}.tsv", ROUND_COLUMNS, ({"lemma": k, "decision": v[0], "reason": v[1]}
                                                       for k, v in d.items()))
    write_tsv(rnd / "agreed.tsv", ROUND_COLUMNS, ({"lemma": k, "decision": v[0], "reason": v[1]}
                                                  for k, v in agreed.items()))
    write_tsv(rnd / "disagreements.tsv", ("lemma", "A", "reason A", "B", "reason B"), (
        {"lemma": k, "A": da.get(k, ("(none)", ""))[0], "reason A": da.get(k, ("", ""))[1],
         "B": db.get(k, ("(none)", ""))[0], "reason B": db.get(k, ("", ""))[1]} for k in dis))
    (rnd / "questions.txt").write_text("\n".join(sorted(set(qa + qb))) + "\n", encoding="utf-8")
    (rnd / "accent-merges.txt").write_text("".join(f"{k}\t{agreed[k][0]}\n" for k in accent_only_merges(agreed)),
                                           encoding="utf-8")
    counts: dict[str, int] = {}
    for d, _r in agreed.values():
        counts[d.split(":")[0]] = counts.get(d.split(":")[0], 0) + 1
    print(json.dumps({"lemmas": len(by), "agreed": len(agreed), "agreed_by_decision": counts,
                      "to_adjudicator": len(dis), "accent_only_merges": len(accent_only_merges(agreed)),
                      "next": "read agreed.tsv and accent-merges.txt; write queries.tsv; rerun with --adjudicate"},
                     ensure_ascii=False, indent=1))
else:
    da, db, agreed = read_side("A"), read_side("B"), read_side("agreed")
    queries = {r["lemma"]: r["why"] for r in read_tsv(args.queries, ("lemma", "why"))} if args.queries else {}
    unknown = sorted(set(queries) - set(agreed))
    if unknown:
        raise SystemExit(f"queries for lemmas that are not agreed decisions of this round: {unknown[:10]}")
    todo = [by[k] for k in by if k not in agreed or k in queries]

    def both(q: dict[str, Any]) -> str:
        a, b = da.get(q["lemma"], ("(none)", "")), db.get(q["lemma"], ("(none)", ""))
        why = f"coordinator's query: {queries[q['lemma']]}\n" if q["lemma"] in queries else ""
        return f"reviewer 1: {a[0]} ({a[1]})\nreviewer 2: {b[0]} ({b[1]})\n{why}"

    adj, qadj = run("adjudication", ADJUDICATOR, cfg["adjudicator_model"], todo, ADJ_BATCH, both)
    rows = []
    for q in queue:
        k = q["lemma"]
        if k in adj:
            d, why, how = (*adj[k], "adjudicated")
        elif k in agreed:
            d, why, how = (*agreed[k], "agreed")
        else:
            d, why, how = "", "", "undecided"
        rows.append({"lemma": k, "decision": d, "reason": why, "how": how, "rank": q["rank"]})
    write_tsv(rnd / "decisions.tsv", ("lemma", "decision", "reason", "how", "rank"), rows)
    with (rnd / "questions.txt").open("a", encoding="utf-8") as fp:
        fp.write("".join(f"{line}\n" for line in sorted(set(qadj))))
    undecided = [r["lemma"] for r in rows if not r["decision"]]
    print(json.dumps({"lemmas": len(rows), "agreed": sum(r["how"] == "agreed" for r in rows),
                      "adjudicated": len(adj), "queried": len(queries), "undecided": len(undecided),
                      "first_undecided": undecided[:10]}, ensure_ascii=False, indent=1))
