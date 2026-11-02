# Review runner (scripts/review)

The list-cleaning pass after a full count, for any language. frequer's junk rules flag lemmas and route them
(`frequer/junk.py`); model reviewers decide what is routed to them; the decisions land in
`corpora/review/<lang>.tsv`, which every build applies. **The scripts copy, merge and check; they never decide.**
Every decision comes from two independent reviewers and an adjudicator, and anything new goes to the developer as
a `# question` line. This is a tool the orchestrating agent runs one step at a time and inspects between steps,
not an autopilot: `docs/PLAYBOOK.md` §5-§8 says what to look at after each step and when to stop and ask.

Reviewers are headless `claude -p` calls with no tools and no MCP servers, run from an empty directory, so a
reviewer sees only its prompt. Every answer is cached under the work directory: a rerun resumes. The session
running these must be allowed to run `claude` and `python` without a permission prompt (PLAYBOOK §Sessions).

## Configuration

One JSON file per language run (`common.py` has an example): the language, the work directory, the counts, the
pinned Honeyeater checkout (the runtime the counts were made with), the reference checkout (learnable names, the
number check), the lemma wheel, the window (30,000), the corpus sample for examples, the prompt files, and the
models (`sonnet` for screeners and reviewers, `opus` for the adjudicator; `claude` CLI aliases).

## Prompts are versioned files

| file | what |
|---|---|
| `prompts/common/reviewer.md`, `adjudicator.md`, `system.md` | the wrappers: lemma entries, answer format, `{placeholders}` |
| `prompts/<lang>/rules-flagged.md` | the binding rules for flagged rounds (es, de, ja) |
| `prompts/<lang>/rules-unflagged.md` | the rules for screened suspects (es) |
| `prompts/<lang>/screener.md` | triage of unflagged keeps (es, ja) |
| `prompts/<lang>/institutions-screen.md`, `institutions-review.md` | the institutions re-decision (es) |
| `prompts/TEMPLATE/` | a new language's starting point, with the cross-language rulings folded in |

A rules file is binding text: a change to it is a developer ruling, recorded in `docs/DECISIONS.md` and in the
language's `full/<lang>/junk-review.md`, in the same commit. The es, de and ja files are the texts those runs used
(es's triage rules were reworded only in their answer format, to list suspects rather than mark every row).

## Protocol

* **Rounds.** `route.py` writes `routed.tsv` (every ranked lemma: rank, action, frequency, POS, forms, flags,
  kept position). The `pending` lemmas in the window are the round. A drop or merge moves the window, so new
  flagged lemmas enter it: route, review, collect, route again, until nothing is pending.
* **Examples.** `sample.py` re-streams a cleaned corpus sample (the same hygiene and shard code as the count);
  `examples.py` finds candidate lines by surface form and keeps those in which the production sentence stage
  files that lemma (up to 3 per lemma, from different documents).
* **Two independent reviewers** (A and B) see the rules and batches of 40 lemmas, each with rank, frequency, POS,
  the flags with their evidence (or the screeners' notes), written forms and examples; never each other's
  answers. A lemma an answer skips or mangles is asked again once.
* **The gate between reviewers and adjudicator** (the es sanity pass). `review.py` stops after the reviewers. The
  orchestrator reads `agreed.tsv` (every merge, a sample of drops) and `accent-merges.txt` (agreed merges that
  differ from their target only by an accent or case, which can hide a second real word: es *comisaria* /
  *comisaría*, *clara*, *vaya*), and writes `queries.tsv` (`lemma<TAB>why`) for any agreed decision to re-examine.
* **The adjudicator** (`review.py --adjudicate`) decides every disagreement and every query, in batches of 30,
  and writes at most 5-6 grouped questions for the developer.
* **Apply.** `collect.py <round>` appends the round to `corpora/review/<lang>.tsv` under a `# <label>` header. An
  earlier decision stands unless the round is a re-decision under a new ruling (`--redecide`, which keeps the old
  decision in the reason). A round with an undecided lemma is refused.
* **Unflagged triage.** `screen.py` sends the unflagged keeps (batches of 250, no examples) to two screeners;
  anything either lists is a candidate, except the release's own entries (units, homograph keys, learnable names).
  Candidates then go through the full protocol with the unflagged rules.
* **Institutions** (positive selection). `screen.py --pool drops` over the review and proper-noun drops in the
  window with the institutions screen; picks go through review with `--decisions keep,drop --redecide`.
* **Audit** (an estimate, never applied). `audit.py` samples keeps and drops per band; they go through the full
  protocol as a round named `audit-*`; `report.py` turns it into per-band real-lemma and false-drop estimates.
* **Report and samples.** `report.py` writes `band-report.md` (audit estimates, drops, merges, questions);
  `band_samples.py` writes `band-samples.md`, the word samples per band and across languages that the developer
  chooses the cutoff from (ruling 2026-11-02).

## A round, step by step

```bash
cd <pinned honeyeater>/backend; export PYTHONPATH=.:<frequer>:<lemma site>     # route, sample, examples only
R=<frequer>/scripts/review; C=<config.json>
python $R/route.py $C                                  # routed.tsv; read the action counts it prints
python $R/sample.py $C                                 # once per language: the example sample
python $R/examples.py $C $W/r1.tsv --actions pending   # queue; check the share with examples (>~85 %)
python $R/review.py $C $W/r1.tsv round1                # stage 1: reviewers A and B, then STOP
#   read agreed.tsv, accent-merges.txt, disagreements.tsv; write $W/queries.tsv for agreed rows to re-examine
python $R/review.py $C $W/r1.tsv round1 --adjudicate --queries $W/queries.tsv
python $R/collect.py $C round1 --label "round 1 (window to 30k)"
#   send review/round1/questions.txt to the developer; a ruling edits the rules file and the affected lines
python $R/route.py $C                                  # new pending lemmas? round 2
```

Triage: `screen.py $C triage --to 10000`, read a sample of `triage/candidates.tsv`, then `examples.py $C
$W/t.tsv --only-file $W/triage/candidates.txt --notes $W/triage/candidates.tsv` and `review.py ... --rules
prompts/<lang>/rules-unflagged.md`. Audit: `audit.py $C a1`, then `examples.py --only-file $W/a1.txt`,
`review.py $C $W/a1.tsv audit-a1` (and `--adjudicate`), `report.py $C`.

## Files

| script | reads | writes |
|---|---|---|
| `route.py` | counts (merged once, cached `merged.pkl`), manifest, review file, reference checkout | `routed.tsv` |
| `sample.py` | manifest, config `sample` | `sample/work/*.tsv.gz` (cleaned lines) |
| `examples.py` | `routed.tsv`, the sample | a queue TSV (`common.QUEUE_COLUMNS`) |
| `review.py` | rules, a queue | `review/<round>/{A,B}/`, `A.tsv`, `B.tsv`, `agreed.tsv`, `disagreements.tsv`, `accent-merges.txt`, `questions.txt`; with `--adjudicate`: `adjudication/`, `decisions.tsv` |
| `screen.py` | `routed.tsv`, a screener prompt | `<name>/{A,B}/`, `candidates.tsv`, `candidates.txt` |
| `audit.py` | `routed.tsv` | `<name>.txt` (sampled lemmas) |
| `collect.py` | a round's `decisions.tsv` | `corpora/review/<lang>.tsv` |
| `report.py` | `routed.tsv`, rounds, audits, questions | `band-report.md` |
| `band_samples.py` | `routed.tsv` (and other languages' configs) | `band-samples.md`: words per band, at the cut, deeper, across languages; optional model-written glosses |

`route.py`, `sample.py` and `examples.py` run from the pinned Honeyeater checkout's `backend` with
`PYTHONPATH=.:<frequer>:<lemma site>` (as `frequer count`); the others need only Python and `claude`. The pure
helpers in `common.py` are tested (`tests/test_review.py`).

## What ran for ja (2026-11-01/02)

1. `route.py` (junk rules as in `corpora/ja.yaml`; the diversity threshold set to 0.2 after a first run flagged
   14,500 lemmas): 2,077 lemmas pending in the 30k window.
2. `sample.py`: HPLT files 2, 6, 11, 16, 19 to 25M characters each, plus Tatoeba (2.4M lines).
3. `examples.py` + `review.py` round1 (2,077: 1,950 agreed, 127 adjudicated), collect, route; rounds 2 and 3
   for what the window pulled in (90, 2).
4. Rule change (a dictionary name drops only with the tagger's PROPN), route, rounds 4 (643) and 5 (32).
5. Round 6: the era names (5) after a reviewed decision was made to outrank the automatic drop.
6. Audit: 100 random unflagged keeps per band, `report.py`.
7. Number rule on (the app's check), route, round 7 (107 pulled in).
8. Developer rulings (famous institutions keep; adult spam jargon drop; era names keep; lone bound kanji drop)
   folded into the rules; round 8 re-decided the affected lemmas (351).
9. `screen.py` over the unflagged keeps 0-30k, then the full protocol on the suspects (round 9).
10. `names_final` with the reviewed learnable-names list (the reference checkout), route; build at 30k with
    `--reference-root`, appended learnable names, `load_lemmas --dry-run`.

The es run used the same protocol through agent sessions reading and writing files (two screeners per chunk,
two reviewers per ~740-lemma chunk, one adjudicator per round; `full-es` `review/` and `full/es/steps.md`); de
used it with no screener stage (every flagged lemma in the window to two reviewers; `full/de/review/`). The
runner here is the generalised form of both.
