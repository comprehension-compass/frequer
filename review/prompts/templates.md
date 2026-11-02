# Prompt templates

The exact prompts the es review used, with the round's paths and numbers as `{placeholders}`. Each agent is
started fresh (no shared context) and reads only the files named. Screeners and reviewers: the cheaper model
tier; adjudicators: the stronger one. Rules files: `review/rules/<lang>-*.md`.

## Screener (triage of unflagged keeps)

> Screen a {Language} word list. Work alone. Read ONLY {rules: <lang>-triage.md} and {round}/t{A|B}{i}/input.tsv
> (read it in parts; it is long). Use only Read and Write; no web; your own knowledge of {Language}. For EVERY
> lemma in input.tsv, in order, write `lemma<TAB>ok|suspect<TAB>reason` (reason only for suspects) to
> {round}/t{A|B}{i}/output.tsv. Build the file in several passes (rewrite the whole file each time with all lines
> so far) and make sure every lemma is present. Reply only with the counts of ok and suspect.

Chunks of ~4,700 rows ran to completion in one agent; one screener was stopped part-way. In that case, write the
unscreened rows to a new chunk (`t{A}{i}b`) and start a fresh screener on just that remainder.

## Reviewer

> You are an independent reviewer for a {Language} learner frequency list. Work alone. Read ONLY: {rules} (binding
> rules) and {round}/r{A|B}{i}/input.tsv ({n} lemmas from list positions {from}–{to}, with example sentences; read
> it in parts). No web; your own knowledge of {Language}.
>
> For EVERY lemma, in order, decide exactly one of `keep`, `drop`, `merge:<lemma>`, `pending-names`, with a short
> reason; add `# question <lemma>: ...` lines where genuinely unclear. Write {round}/r{A|B}{i}/output.tsv
> (`lemma<TAB>decision<TAB>reason`, lemma copied exactly), building it in passes. Make sure every lemma is in
> the file. Reply only with the counts.

For flagged rounds the rules were `<lang>-flagged.md`, and the prompt also restated the settled lines (place
names → `pending-names`; other names drop; a real common word stays even if many occurrences are a name; a
non-native token whose real-word reading is a minority drops; adapted spellings merge into the dictionary form;
abbreviations merge into the full word; cut-off lemmas merge; specialist acronyms drop; digit-only ordinals drop;
hyphenated compounds of two listed words drop). Chunks: ~740 lemmas.

## Adjudicator

> You are the adjudicator for a reviewed cleanup of Honeyeater's {Language} learner frequency list ({what the
> lemmas are and where they sit}). Read ONLY: {rules} (binding rules), {round}/adj/disagreements.tsv and
> {round}/adj/questions.txt. No web; your own knowledge of {Language}.
>
> disagreements.tsv holds {n} lemmas where two independent reviewers disagree ({m} of them are merges to
> different targets: pick the right target), then {q} where they agreed but the coordinator queries the decision
> (a merge can hide a second real word: a lemma whose own reading is a real word a learner meets should be
> `keep`). Use the examples and commonest forms as evidence.
>
> Decide `keep`, `drop`, `merge:<lemma>` or `pending-names` for each, with a one-line reason. Write
> {round}/adj/decisions.tsv (`lemma<TAB>decision<TAB>reason`, lemma copied exactly, all {n+q}) and
> {round}/adj/questions-final.txt (at most 5-6 grouped `# question ...` lines, only for anything genuinely new that
> the rules don't settle and the developer should rule on). Reply with the counts.

Coordinator queries come from reading the agreed decisions before adjudication (README §Sanity pass).

## Institutions screen (positive selection)

> Screen a list of dropped {Language}-list names. Work alone. Read ONLY {rules: <lang>-institutions-screen.md} and
> {round}/s{i}/input.tsv ({n} lemmas; read it in parts). No web; your own knowledge. Write your picks to
> {round}/s{i}/output.tsv (`lemma<TAB>institution`, lemma copied exactly), appending as you go. Go through every
> line. Reply with the number of picks.

The institution reviewers and adjudicator use the reviewer and adjudicator templates above, with
`<lang>-institutions-review.md`. Their decisions are `keep` or `drop` only.
