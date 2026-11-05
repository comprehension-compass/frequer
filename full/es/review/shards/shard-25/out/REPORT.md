# es review shard 25 (round 18): report

Branch `es-review-shard-25` from `543d45d`; rules `review/rules/es-{flagged,unflagged}-final.md` as at 543d45d (now
with the diminutive call; same as full-es 2d4e2c1). Runtime, lemma wheel and corpus sample reused from the shard 9 work
directory; the setup script and `review/scripts/examples10.py` are unchanged. Every `review.py` call passed `--rules`
and `--decisions keep,drop,merge`.

## Counts

| step | lemmas | result |
|---|---:|---|
| flagged: examples | 182 | 138 with examples (**76 %, under the ~85 % bar**) |
| flagged: two reviewers | 182 | 181 agreed (drop 154, merge 24, keep 3), 1 disagreement; 3 accent-only merges |
| flagged: adjudication | 2 | 1 disagreement + 1 query; 0 undecided |
| **flagged final** | **182** | **keep 3, drop 154, merge 25** (180 agreed, 2 adjudicated) |
| unflagged: screening | 202 | 1 batch, 0 failed; 109 suspects (87 by both screeners) |
| suspects: examples | 109 | 77 with examples (**71 %, under the ~85 % bar**) |
| suspects: two reviewers | 109 | 100 agreed (drop 59, merge 27, keep 14), 9 disagreements; 1 accent-only merge |
| suspects: adjudication | 10 | 9 disagreements + 1 query; 0 undecided |
| **suspects final** | **109** | **keep 18, drop 62, merge 29** (99 agreed, 10 adjudicated) |

## Queries (the gate) and outcomes

I read every agreed merge and keep, every accent-only merge, and all agreed drops in both rounds.

- Flagged: `practica` (agreed `merge:práctica`): could equally be the verb practicar; all 68 occurrences are PRACTICA.
  Adjudicated `merge:práctica` (the examples include the noun), with a question (below).
- Unflagged: `harmónico` (agreed `merge:armónico`): an accepted academy variant, like trasposición, trasmutar and
  ácimo, which were kept as written. Adjudicated `merge:armónico`, as the minority variant: armónico is the form people
  write. (The earlier keeps were spellings that were the written majority; this one is not.)

The reviewers applied the diminutive rule themselves (`movidito` → `movido`).

## Points for the coordinator

Questions the adjudicator raised:
- `practica`: when every occurrence is one all-caps form with a dropped accent (PRACTICA: práctica or practicar), a
  split by form can't separate the readings. Split by context, or send it all to the majority reading?
- `itinere`: the split-loan rule merges the first half, but here the first half ("in") is generic, so the distinctive
  second half carries the merge (`merge:in itinere`). Confirm this handling.
- `compuester`: no examples; chose `merge:componer` from the VERB tag; the lexicalised compuesto is the other option.

Split request (for the coordinator to write): `emplastar` (emplasto, Emplasto, emplaste, Emplaste -> emplasto).

## What went wrong

- Example shares are 76 % (flagged) and 71 % (suspects), both below the ~85 % bar; carried on as the instructions say.
- Nothing else: no failed calls or batches in any step.

## Every `# question` line

### Flagged round (`s25-flagged/questions.txt`)

```
# question diece: the form dieces has no examples, so the merge into diez is assumed to be a plural of diez
# question fuac: unclear which body this is (possibly Colombian air force, Fuerza Aérea); the example is too sparse, so I dropped it.
# question hotdog: merging into the two-word "hot dog" assumes that is the standard written form; "perro caliente" is the native alternative.
# question hotdog: the established Spanish form could also be the loan "hot dog" (two words); I chose perrito caliente, but the coordinator may prefer merge:hot dog.
# question inea: could be the Mexican national adult-education institute (INEA), a household name there; I dropped it because the examples are unavailable to confirm.
# question practica: examples mix a site name, the verb practica and the noun práctica without accent; merged to práctica as the main real reading
# question practica: the examples mix a brand (PRACTICA ESPAÑOL), the verb practica (→ practicar) and the noun práctica; I chose práctica
# question vozvoz: merged into voz as an obvious doubled-word artefact; drop would also be defensible.
# question practica: all 68 occurrences are the single form PRACTICA, so a split by form cannot separate práctica from practicar; should all-caps tokens with a missing accent be split by context, or go wholly to the majority reading?
```

### Unflagged round (`s25-unflagged/questions.txt`)

```
# question ajustamiento: rare and often a calque of "adjustment", where ajuste would be normal; kept because it is a valid DLE word and not clearly broken
# question bouclé: the DLE adaptation buclé is assumed; if buclé is not on the list, keep bouclé as an established textile term
# question bouclé: used in Spanish fashion copy but not established in dictionaries; chose drop.
# question bugambilia: Both bugambilia and buganvilia are accepted; I kept bugambilia as the form people write, so merging into buganvilia would also be defensible.
# question compuester: Text form is compuesto, which is also a real adjective/noun; I merged to the verb componer because the lemma is tagged VERB.
# question elementaria: unsure whether this school-level noun (calque of "elementary") should merge into elemental or drop; chose merge.
# question emplastar: split by form: emplasto, emplaste, Emplasto, Emplaste -> emplasto
# question itinere: Latin phrase "in itinere" is established in Spanish labour law, but "in" is not a listed lemma, so I applied the split-loan rule and dropped it. The coordinator may prefer to keep it as the compound "in itinere".
# question memória: Looks like Portuguese text, so I dropped it, but a merge to memoria is arguable if some uses are accent typos in Spanish.
# question shoyu: not in the academy dictionary, but common in Spanish cooking text; chose keep.
# question temporáneo: could be a cut-off form of contemporáneo/extemporáneo or the rare real word "temporáneo"; no examples to check, dropped
# question temporáneo: the lemma could be a real rare adjective or a cut-off fragment of contemporáneo/extemporáneo; no examples were available, so I dropped it.
# question compuester: merge target could be componer (participle) or the lexicalised noun/adjective compuesto; with no examples I chose componer from the VERB tag
# question emplastar: split by form: emplasto, Emplasto, emplaste, Emplaste -> emplasto (emplaste is either the subjunctive of emplastar or the noun variant)
# question itinere: the split-loan rule assumes the first half occurs only in the compound; here the first half "in" is generic, so should the distinctive second half carry the merge, as done here?
```
