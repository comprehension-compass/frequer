# Triage rules (screening only)

These lemmas are on Honeyeater's Spanish learner word list (positions 1-10,000) and passed every automatic
filter. A blind check found a few per cent of these are still junk. Your job is only to SCREEN:
mark each lemma `ok` or `suspect`. Suspects get a full review with example sentences later, so when in doubt,
mark `suspect`.

Mark `suspect` when the lemma looks like any of these:
- a word from another language (Italian, Catalan, Portuguese, French, English, Latin…) rather than Spanish or an
  established loan;
- an inflected or misspelt form filed as a lemma (a plural, a feminine, a conjugated verb, a superlative, a missing
  accent, a verb with a clitic attached), when the dictionary form differs;
- a name (person, brand, company, product, place) or a multi-word name;
- an abbreviation, code, fragment or web artefact;
- not a word at all.

Mark `ok` for a real Spanish word or established loan in its dictionary form, even if rare or specialised.

Output one line per lemma: `lemma<TAB>ok|suspect<TAB>few-word reason (suspects only)`.
