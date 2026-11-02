# es handoff: scratch scripts, commands, failure modes

These are working copies from the es session, as run, with hard-coded paths. Generalise; don't run as-is. The
procedure and plumbing that is already generic is on `full-es`: `review/` (README, prompt templates verbatim,
rules, `scripts/examples.py`, `scripts/round.py`) and `full/es/steps.md` (ordered log).

## scratch/

| file | step | what it does |
|---|---|---|
| `case_tally.py` (`case_dump.py`) | proper nouns | tallies each surface form's sentence-initial / running / title-case occurrences over Tatoeba + ParaCrawl head → `corpora/case/es.tsv.gz` (committed as `tally_es.py`'s output) |
| `exclusion_cands.py`, `exclusion_criterion.md` | exclusion list | candidate English/boilerplate lemmas and units for the reviewed exclusion list, and the criterion the reviewers had |
| `drops_forms.py` | review | commonest surface forms for drop candidates (reviewer input column) |
| `halves.py` | convergence | split-half lists on the filtered ranking (odd/even shards) for the band agreement numbers |
| `clump.py` | junk: diversity | the documents-reached / expected ratio per lemma, to calibrate the 0.6 threshold |
| `bands.py` | band report / cut | walks `filters.apply(...).routed` counting actions per list band and listing the kept lemmas (`band-report.md`) |
| `full30.py` | cut | the routed 30k list with actions, for sampling |
| `triage_union.py` | unflagged review | union of screener suspects minus units / homograph keys / learnable names (now `review/scripts/round.py union`) |
| `institutions_pool.py` | institutions | review drops + proper-noun drops among the ranked lemmas that fill the top 30k |

Inline steps that never became files (now in `round.py`): agree (two reviewer outputs → agreed + disagreements),
apply (append decisions), reviewer input files. Place-name re-decision and the rulings were one-off edits of
`corpora/review/es.tsv` (rules in `review/README.md` §Place names and `full/es/junk-review.md`).

## shell/

* `env2.sh`: environment for builds (pinned honeyeater worktree `he-c07c701`, wheel site, `$LEMMA` flags).
* `restart-ext.sh`: restarts the extended count (`count --part 0/5`), its `coordinate` and the convergence pusher
  after a worker restart.
* `pushconv-ext.sh`: commits `out/es-ext/convergence.*` to `full-es` whenever they change (own clone, so the
  working tree never moves under a running process).
* `run-pc.sh`: the earlier single-machine count wrapper.

## Commands, count to snapshot

```bash
source env2.sh        # cd honeyeater/backend; PYTHONPATH=.:frequer:wheel-site; $PY; $LEMMA
$PY -m frequer count es --data-dir data --workers 3 $LEMMA         # resumable; checkpoints + stop rule
$PY -m frequer count es --data-dir data --workers 2 --part 0/5 $LEMMA   # distributed extension, one part here
$PY -m frequer coordinate es --data-dir data --repo coord-repo --parts 5 --out-dir out/es-ext --local-pid $P $LEMMA
HONEYEATER_ROOT=he-c07c701 FREQUER_REFERENCE_ROOT=he-766 \
  $PY -m frequer build es --data-dir data-base --out-dir out/es-30f --score frequency $LEMMA
#   interim list: add --top-n 10000 --leave-out-pending-names
cd honeyeater/backend && pg_ctlcluster 16 main start && \
  .venv/bin/python manage.py load_lemmas es --path out/es-30f/es.json --dry-run
```

## Failure modes and workarounds

* **Wheel hash mismatch**: the wheel embeds git HEAD; rebuild at the release commit's parent with its files
  checked out (README §Rebuilding the wheel).
* **Worker restarts kill background processes** (count, coordinator, pusher): several times. Counting is
  resumable: rerun `restart-ext.sh`. Pass the coordinator the real python PID (`pgrep -f "^.venv/bin/python -m
  frequer count es"`), not the wrapper shell's.
* **`pkill -f` / `pgrep -f | kill` matched the calling shell** and killed it (exit 144). Kill exact PIDs.
* **Working tree changed under a running coordinator**: run long processes from a frozen worktree (`fq-ext`)
  and push from a separate clone (`push-repo`).
* **Restamping the runtime**: after the equivalence proof (`runtime-equivalence.md`) shards were restamped to
  `c07c7015`. The old commit goes in a top-level `restamped_from`, not inside `runtime`, or merge equality breaks.
* **Agents stopped part-way**: one screener stopped after 1,399 of 4,769 rows (safety classifier). Restart a
  fresh agent on the unscreened remainder only; don't resend the same chunk.
* **Agents that say they used only Read/Write but can't count**: check every output with `round.py` (it refuses
  missing or extra lemmas) rather than trusting the reported counts.
* **Junk-rule false positives** found by reading flags: Tatoeba-heavy words in the diversity tail (fixed: absolute
  clumping ratio), participles under citation (fixed: global surface attestation, verb-shaped exempt), -mente
  reduplication and loans under shape, correlated flags dropping acronyms (fixed: the proper-noun middle band
  always goes to review), ñ stripped by accent merges (campana → campaña; fixed, plus a review keep vetoes).
* **Loader skips** from merge targets missing / capitalised / multi-word (fixed: rename, fold case, compound).
* **Drops cascade**: each drop pulls the next lemma into the window; review with a margin and repeat.
* **Number rule** needs Honeyeater's newer `lexicon` than the pinned runtime: it runs in a subprocess
  (`frequer/numbers.py`), with `django.setup()` and `config.settings.test`.

## Rulings

All developer rulings so far are in `full/es/junk-review.md` (questions per round, §Later rounds, §Developer
rulings 2026-11-02) and in `review/rules/` (the institutions ruling is in `es-unflagged.md` and the
institutions rules). Not yet written there: none.
