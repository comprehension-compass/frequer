# Junk review orchestration (scripts/review)

The list-cleaning pass after a full count: frequer's junk rules flag lemmas, model reviewers decide the
flagged ones in the review window, and the decisions land in `corpora/review/<lang>.tsv`, which the build
applies. These are the scripts the ja pass ran (2026-11-01/02), with every path and the language in one JSON
config (`common.py` has an example). Reviewers are headless `claude -p` calls with no tools, run from an empty
directory, each answer cached under the work directory so a rerun resumes.

## Protocol

* **Two independent reviewers** (`reviewer_model`, Sonnet) see the rules, the lemma, its rank, frequency, POS,
  flags with their evidence, its written forms and 2-3 example sentences, in batches of 40; never each other's
  answers. **An adjudicator** (`adjudicator_model`, Opus) sees both answers for every disagreement (batches
  of 30). Decisions: `keep`, `drop`, `merge:<lemma>`, `pending-names` (a place name: the learnable-names list
  decides); `# question <lemma>: ...` lines for what the rules don't settle.
* **Examples** come from a re-streamed corpus sample (the count deletes its cleaned shards): the same
  hygiene and shard code (`sample.py`), candidate lines found by surface form, each one confirmed by the
  runtime (the production sentence stage must file that lemma in that sentence; `examples.py`).
* **Rounds.** A drop or merge moves the window, so new flagged lemmas enter it: route, review the new
  `pending`, collect, route again, until none are pending.
* **Unflagged triage.** Two screeners (`screen.py`, batches of 250 without examples) list suspects among the
  unflagged keeps; every suspect named by either goes through the full protocol.
* **Audit** (an estimate, never applied): a random sample of unflagged keeps per band through the full
  protocol; a round directory named `audit*` is skipped by `collect.py` and `report.py`.

## Files

| script | reads | writes |
|---|---|---|
| `route.py` | counts (merged once, cached `merged.pkl`), manifest, `corpora/review/<lang>.tsv`, reference checkout | `routed.tsv`: rank, lemma, action, freq, POS, forms (JSON), flags, kept position |
| `sample.py` | manifest, config `sample` | `sample/work/*.tsv.gz` (cleaned lines: doc, part, text) |
| `examples.py` | `routed.tsv`, sample | a queue: one JSON object per lemma with `examples` |
| `review.py` | config `rules`, a queue | `review/<round>/{A,B,adjudication}/`, `decisions.tsv` (lemma, decision, reason, agreed/adjudicated/undecided, rank), `questions.txt` |
| `screen.py` | `routed.tsv`, config `screener` | `<name>/{A,B}/`, `suspects.txt` |
| `collect.py` | every round's `decisions.tsv` (later wins) | `corpora/review/<lang>.tsv` |
| `report.py` | `routed.tsv`, decisions, questions | `band-report.md` (per band: actions, kept share, rule hits, samples, drops, merges, questions) |

`route.py`, `sample.py` and `examples.py` run from the pinned Honeyeater checkout's `backend` with
`PYTHONPATH=.:<frequer>:<lemma site>` (as `frequer count`); the others need only Python and `claude`.
Prompts: `prompts/rules-<lang>.md` (the binding reviewer rules, with the developer's rulings folded in) and
`prompts/screener-<lang>.md`.

## What ran for ja, in order

1. `route.py` (junk rules as in `corpora/ja.yaml`; the diversity threshold set to 0.2 after a first run
   flagged 14,500 lemmas): 2,077 lemmas pending in the 30k window.
2. `sample.py`: HPLT files 2, 6, 11, 16, 19 to 25M characters each, plus Tatoeba (2.4M lines).
3. `examples.py` + `review.py` round1 (2,077: 1,950 agreed, 127 adjudicated), `collect.py`, `route.py`;
   rounds 2 and 3 for what the window pulled in (90, 2).
4. Rule change (a dictionary name drops only with the tagger's PROPN), `route.py`, round 4 (643) and 5 (32).
5. Round 6: the era names (5) after a reviewed decision was made to outrank the automatic drop.
6. Audit: 100 random unflagged keeps per band (`--only`), `report.py`.
7. Number rule on (the app's check), `route.py`, round 7 (107 pulled in).
8. Developer rulings (famous institutions keep; adult spam jargon drop; era names keep; lone bound kanji
   drop) folded into the rules; round 8 re-decided the affected lemmas (351).
9. `screen.py` over the unflagged keeps 0-30k, then the full protocol on the suspects (round 9).
10. `names_final` with the reviewed learnable-names list (the reference checkout), `route.py`; build at 30k
    with `--reference-root`, appended learnable names, `load_lemmas --dry-run`.
