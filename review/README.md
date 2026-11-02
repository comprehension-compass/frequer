# Reviewed cleanup of a frequency list

How the es list was reviewed (2026-11-01/02), written so it can be repeated for another language. The build
applies the decisions; this directory holds the procedure, the rules the agents had, the prompt templates
(`prompts/templates.md`) and the file plumbing (`scripts/`). Scripts only copy, merge and check: every decision
comes from a reviewer or the adjudicator.

## Where decisions live

* `corpora/review/<lang>.tsv`: one line per lemma, `lemma<TAB>decision<TAB>reason`. Decisions: `keep`, `drop`,
  `merge:<lemma>`, `pending-names` (a place, until the learnable-names list decides it), and
  `split:<lemma>|<other>=<form>,...` (the listed forms go to `<other>`, the rest merge into `<lemma>`). `#` lines
  head each round. The build (`frequer/filters.py`, `frequer/junk.py`) applies them: splits, then review merges
  (targets folded to lower case; a missing target is created; a multi-word target becomes a compound), accent
  merges (vetoed by a `keep`), ranking, the exclusion list, the junk rules, then routing. A reviewed `keep`
  overrides every automatic drop; a merge target counts as reviewed.
* `corpora/exclude/<lang>.tsv`: the exclusion list (English, boilerplate, abbreviations), reviewed separately.
* `full/<lang>/junk-review.md`: per-round counts, the developer's questions and rulings.

## The two kinds of round

**Flagged rounds** review what the junk rules flag (`frequer/junk.py`): a single flag, or the proper-noun middle
band, within `review_top`. Two flags drop unless `review_multi_flag` sends them to review. Drops pull new lemmas
into the window, so review with a margin (es: 1,500 ranks past the cut, by raising `review_top` to list them,
then restoring it) and repeat until no lemma in the list is `pending`.

**Unflagged rounds** check the lemmas no rule flagged, in two stages, because a blind sample found a few per cent
junk there (`full/<lang>/band-report.md`):

1. *Triage.* Write the unflagged keeps of a band to a ranked TSV, then `round.py triage-chunks`. Two screeners
   read every row (rules `<lang>-triage.md`) and mark it `ok` or `suspect`, with "when in doubt, suspect".
2. *Union.* `round.py union` takes every lemma either screener suspects. It leaves out the release's own
   entries: units, homograph keys and learnable names (screeners flag `a pesar de`, `hacerse`, `parte#Fem`).
3. *Full review*, as below, with rules `<lang>-unflagged.md`. These rules add that the lemmatiser's
   conventions stand (function words, gendered nouns with their own entry, pronominal verbs).

## A review round, step by step

1. `cands.json`: `[{lemma, rank, freq, pos, forms, flags}]` (flagged rounds: from the flags sidecar
   `<lang>.flags.tsv`; unflagged rounds: from `round.py union`).
2. `scripts/examples.py <round> <tatoeba-code> <paracrawl-pair>`: 1 Tatoeba and up to 3 ParaCrawl sentences per
   lemma, matched on its surface forms (about 10 minutes; nothing committed).
3. `round.py inputs <round> --chunks N`: reviewer files `r{A,B}<i>/input.tsv`, about 740 lemmas each.
4. Two independent reviewers per chunk (A and B), started fresh and in parallel, each seeing only the rules and
   its chunk (`prompts/templates.md`). Neither sees the other's output.
5. `round.py agree <round>`: the agreed decisions (same decision and same merge target), the disagreements and the
   pooled `# question` lines.
6. **Sanity pass** (the coordinator, before adjudication): read the agreed merges and a sample of agreed drops.
   Send to the adjudicator, as queried rows, any agreed merge that may hide a second real word (es: *clara* the
   egg white, *vaya* the interjection, *comisaria* the feminine noun beside *comisaría*). One way to find them:
   list the merges whose source and target differ only by an accent, and read them.
7. One adjudicator (the stronger model tier) decides every disagreement and query, and writes at most 5-6 grouped
   questions for the developer.
8. `round.py apply <round> corpora/review/<lang>.tsv --label "round N (...)"`: appends the decisions.
9. Rebuild, check `load_lemmas <lang> --path ... --dry-run` reports 0 skipped, and send the questions to the
   developer. A ruling becomes a line in `junk-review.md` and an edit to the affected review lines.

## Institutions re-decision (developer ruling: famous institutions that aren't places are kept)

1. Pool: every `review-drop` and automatic `propn-drop` among the ranked lemmas that fill the top N (es: 23,842 =
   7,286 + 16,556 in the 30k window), each with its commonest forms and why it was dropped. Build it by running
   `filters.apply` on the counts and walking `routed` until N lemmas are kept.
2. Screen, positive selection: 4 screeners, one per quarter of the pool (rules `<lang>-institutions-screen.md`),
   list anything that is or might be such an institution ("be generous"): es 754 picks.
3. Examples for the picks, then two reviewers (`keep`/`drop`, rules `<lang>-institutions-review.md`) and an
   adjudicator on their disagreements (es: 685 agreed, 69 adjudicated, 158 keeps).
4. Write the keeps: replace an earlier review `drop` line with `keep` (keeping the old decision in the reason);
   add a `keep` line for an automatic drop. `junk.route` lets a reviewed `keep` beat the proper-noun drop.

## Place names

Places get `pending-names` in review, never a decision, until Honeyeater's reviewed learnable-names list
(`reference/learnable-names/<lang>.json`) is final. Then: a pending place in the list becomes `keep`, the others
`drop`; earlier keeps of places not in the list drop; listed places that were dropped or merged become `keep`.
With `append_learnable_names: true`, learnable names outside the top N follow it in the snapshot.
`FREQUER_REFERENCE_ROOT` points the build at a Honeyeater checkout whose reference data (the names list, the number
rule) is newer than the pinned runtime's; the header records its commit.
An interim list built before the names are final uses `--leave-out-pending-names`.

## Scale and cost (es)

| stage | rows | agents |
|---|---:|---|
| triage 0-10k | 9,538 x 2 | 4 screeners (+1 for a remainder) |
| triage 10k-30k | 18,744 x 2 | 8 screeners |
| full review (rounds 1-9) | 2,635 / 587 / 660 / ... / 307 / 2,946 | 2 reviewers per ~740-lemma chunk, 1 adjudicator per round |
| institutions | 23,842 screened, 754 reviewed | 4 screeners, 2 reviewers, 1 adjudicator |
