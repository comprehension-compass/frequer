# es review shard 7 (round 14: the cascade after shards 1-6)

First-pass review work for Honeyeater's Spanish list, rebuilt on the extended counts (1.38B tokens). The coordinating
session is **session_01YCC7brLFG4FC7xFoHpjkcD**: it re-checks your output, adjudicates anything it queries, collects
every shard and builds. Your job is the first pass only.

## Ground rules

* **Branch:** work on `es-review-shard-7` in `comprehension-compass/frequer`, created from `origin/full-es` at
  `04d1ada`. **Never push to `full-es`, `uplift` or `main`.**
* **Binding rules** (read them; they are the developer's): `review/rules/es-flagged-final.md` (flagged queue) and
  `review/rules/es-unflagged-final.md` (screened suspects). Rulings and their history: `full/es/junk-review.md`.
  The screener prompt is uplift's `scripts/review/prompts/es/screener.md`. Don't edit any of these.
* **Questions go to the coordinator, not into your decisions.** Anything the rules don't settle: decide anyway,
  keep the `# question ...` lines the reviewers and adjudicator write, and list them in your report. Never write a
  new rule or edit `corpora/review/es.tsv`.
* **Models:** screeners and reviewers `sonnet`, adjudicator `opus` (the config does this).
* Commit messages end with:
  ```
  Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
  Claude-Session: <your session URL>
  ```
  No model names or identifiers anywhere in commits or files. Never commit corpus text other than the queue files'
  example column (≤3 short sentences per lemma), and never the sample.

## Your queues

`full/es/review/shards/shard-7/`:

* `routed.tsv`: your lemmas in the review runner's routed format (rank, lemma, action, frequency, POS, forms,
  flags, kept position in the 40k window):
  * **flagged:** 878 lemmas with action `pending`. These are newly entering the 40k window on the
    rebuilt counts and are flagged by a junk rule. Full protocol with `es-flagged-final.md`.
  * **unflagged:** 978 lemmas with action `keep` and no flag, never screened before (kept positions 33,184–40,000, every 4th). Screen them first; suspects get the full protocol with `es-unflagged-final.md`.

## Steps

Every `review.py` line passes `--rules` (the adjudicate lines too) and `--decisions keep,drop,merge` (places drop: the
names list is final). The repository `.gitignore` matches `out/`: commit outputs with `git add -f`.

```bash
# 0. sessions: add the honeyeater repository (comprehension-compass/honeyeater) and clone it; then
git -C frequer fetch origin full-es && git -C frequer checkout -b es-review-shard-7 04d1ada
HONEYEATER=$PWD/honeyeater frequer/scripts/review-shard-setup.sh 7       # ~15 min; prints WORK, PY, PYTHONPATH
export WORK=$HOME/es-review-7 PY=$WORK/he/backend/.venv/bin/python
export PYTHONPATH=.:$PWD/frequer:$WORK/site:$WORK/up/scripts/review
FQ=$PWD/frequer; R=$WORK/up/scripts/review; cd $WORK/he/backend

# 1. flagged queue: examples (fixed extractor: forms with >= 10 % of the lemma's count), two reviewers
$PY $R/examples10.py $WORK/config.json $WORK/flagged.tsv --actions pending
$PY $R/review.py $WORK/config.json $WORK/flagged.tsv s7-flagged --rules $FQ/review/rules/es-flagged-final.md --decisions keep,drop,merge

# 2. unflagged: two screeners over every unflagged lemma, then examples for the suspects, two reviewers
$PY $R/screen.py $WORK/config.json s7-screen
$PY $R/examples10.py $WORK/config.json $WORK/suspects.tsv --only-file $WORK/s7-screen/candidates.txt \
    --notes $WORK/s7-screen/candidates.tsv
$PY $R/review.py $WORK/config.json $WORK/suspects.tsv s7-unflagged --rules $FQ/review/rules/es-unflagged-final.md --decisions keep,drop,merge

# 3. the gate (README §A round): read each round's agreed.tsv (every merge, a sample of drops) and
#    accent-merges.txt; write queries.tsv (lemma<TAB>why) for agreed decisions that may hide a second real word
#    (comisaria / comisaría, clara, vaya), then adjudicate
$PY $R/review.py $WORK/config.json $WORK/flagged.tsv s7-flagged --adjudicate --queries $WORK/review/s7-flagged/queries.tsv --rules $FQ/review/rules/es-flagged-final.md --decisions keep,drop,merge
$PY $R/review.py $WORK/config.json $WORK/suspects.tsv s7-unflagged --adjudicate --queries $WORK/review/s7-unflagged/queries.tsv --rules $FQ/review/rules/es-unflagged-final.md --decisions keep,drop,merge
```

Each step prints a JSON summary. Read it. A step with failed calls is rerun; finished calls are cached. If
fewer than ~85 % of lemmas get an example, say so in your report but carry on.

## Outputs (commit on `es-review-shard-7`)

`full/es/review/shards/shard-7/out/`:
* `flagged.tsv`, `suspects.tsv`: the queues as reviewed, with examples;
* `s7-screen/candidates.tsv`;
* for each round, `s7-flagged/` and `s7-unflagged/`: `decisions.tsv`, `agreed.tsv`, `disagreements.tsv`,
  `queries.tsv`, `questions.txt` (the batch caches stay out);
* `REPORT.md`: counts per step (screened, suspects, examples share, agreed / adjudicated, keep / drop / merge),
  your queries and why, every `# question` line, and anything that went wrong.

Then push the branch and **message the coordinator** with `send_message` (session
`session_01YCC7brLFG4FC7xFoHpjkcD`): the branch, the commit and the counts. Don't run `collect.py`; the coordinator
collects.
