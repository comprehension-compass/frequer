# German review shard 6: round `r7`

Developer request 2026-11-02: German is cleaned to kept rank 40,000, and the review rounds are split across sessions.
This shard is one self-contained round. **Orchestrator:** session `session_01YCC7buiq9WmneZ8sMFpxBq` (the de session;
it routes, collects and builds). Send `# question` lines and the "done" message there, with the claude-code-remote
`send_message` tool.

| | |
|---|---|
| what | systematic case-pair and plural candidates (developer rulings 2026-11-02: case and plural forms merge into the real lemma) (collected with --redecide: some are earlier keeps) |
| branch | `de-review-shard-6` (frequer); it holds the queue at `full/de/review/shards/queue-r7.tsv` |
| queue | `full/de/review/shards/queue-r7.tsv` (rank, lemma, frequency, POS, forms, flags or screeners' notes, action, up to 3 examples confirmed by the production sentence stage) |
| rules | `scripts/review/prompts/de/rules-unflagged.md` (unflagged rules; binding; includes every developer ruling to 2026-11-02) |
| prompts | `scripts/review/prompts/common/reviewer.md`, `adjudicator.md`, `system.md` (as on the branch) |
| models | reviewers `sonnet` (A and B, independent), adjudicator `opus` |
| output | commit `full/de/review/rounds/r7/` (the whole `<work>/review/r7/` directory) to `de-review-shard-6` and push |

The example extractor fix (examples only from forms carrying >= 10 % of a lemma, confirmed by the runtime) is already
applied: the queue's examples were made that way. Do not regenerate them.

## Steps

```bash
git clone https://github.com/comprehension-compass/frequer && cd frequer && git checkout de-review-shard-6
W=$HOME/derev-r7; mkdir -p $W
cat > $W/config.json <<CFG
{"lang": "de", "language_name": "German", "work": "$W", "rules": "prompts/de/rules-unflagged.md",
 "reviewer_model": "sonnet", "adjudicator_model": "opus", "parallel": 6}
CFG
cd scripts/review
python3 review.py $W/config.json ../../full/de/review/shards/queue-r7.tsv r7      # stage 1: reviewers A and B
```

Then **the gate** (README §The gate): read `$W/review/r7/agreed.tsv` (every `merge:` line and a sample of 50
drops) and `accent-merges.txt` (agreed merges that differ only by case or umlaut, which can hide a second real word:
*schon/schön*, *Masse/Maße*, a capitalised noun that is a word of its own such as *das Gute*). Write
`$W/queries.tsv` (`lemma<TAB>why`) for any agreed decision the adjudicator should re-examine, especially merges into
an English word's look-alike (a past error: *of -> Ofen*, *Red -> reden*, *not -> Note*: those are English, `drop`).

```bash
python3 review.py $W/config.json ../../full/de/review/shards/queue-r7.tsv r7 --adjudicate --queries $W/queries.tsv
mkdir -p ../../full/de/review/rounds && cp -r $W/review/r7 ../../full/de/review/rounds/r7
cp $W/queries.tsv ../../full/de/review/rounds/r7/ 2>/dev/null; cd ../.. && git add full/de/review/rounds/r7
git commit -m "de review round r7 (shard 6)" && git push -u origin de-review-shard-6
```

Check `decisions.tsv` has no `undecided` line (rerun the adjudicate step if so). Do **not** edit
`corpora/review/de.tsv`: the orchestrator collects with `collect.py` (append-only, --redecide).

Finally send the orchestrator one message: the branch and commit, the counts (agreed / adjudicated; keep / drop /
merge), and the `# question` lines from `questions.txt`.
