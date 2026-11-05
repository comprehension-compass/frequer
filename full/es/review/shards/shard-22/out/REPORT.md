# es review shard 22: report (round 17, cascade)

Base `ae73f55`, whose `review/rules` match `full-es` eb2aea4. The runtime, lemma wheel and corpus sample were reused
from this session's shard 10 (setup script and extractor unchanged). Every review.py line passed `--rules` and
`--decisions keep,drop,merge`.

The coordinator's diminutive call (regular diminutives merge into the base; lexicalised ones keep) is in
`full/es/junk-review.md`, not in the rules files the reviewers read, so I applied it at the gate: every final keep
that looks like a diminutive was checked, and the one candidate (chivito) was queried under the call.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 266 |
| flagged with examples | 221 (83.1 %, **below the ~85 % mark**) |
| flagged: reviewers agreed / to adjudicator | 255 / 11 |
| flagged: queried at the gate | 1 |
| flagged final: agreed / adjudicated | 254 / 12 |
| **flagged final: keep / drop / merge** | **9 / 229 / 28** |
| unflagged screened | 305 (2 batches, 0 failed) |
| suspects (either screener / both) | 168 / 142 |
| suspects with examples | 135 (80.4 %, **below the ~85 % mark**) |
| unflagged: reviewers agreed / to adjudicator | 163 / 5 |
| unflagged: queried at the gate | 1 |
| unflagged final: agreed / adjudicated | 162 / 6 |
| **unflagged suspects final: keep / drop / merge** | **35 / 81 / 52** |
| unflagged not suspected (stay keep) | 137 |

Gate reading: every merge, keep and accent merge in both rounds (flagged 1, unflagged 4), every unflagged drop, and
every flagged drop whose reason mentions a fragment, plural, misspelling or real-word share.

## Queries and outcomes

| round | lemma | agreed | why queried | adjudicated |
|---|---|---|---|---|
| flagged | meze | drop | only 2 of 73 forms are 'mezes'; most may be the dish | drop (not an established loan; mostly names) |
| unflagged | chivito | keep | diminutive call: regular diminutive of chivo, or lexicalised? | keep (lexicalised: kid goat, Uruguayan dish) |

No splits requested beyond any `split by form` question lines below.

## Notes

* Both queues fell below the ~85 % example share (83.1 % flagged, 80.4 % suspects); carried on as the file says.
* Nothing failed: no failed screener batches or review calls, 0 undecided after adjudication.

## Question lines: flagged (31)

```
# question acompáñe: acompañar is the plain verb but the -nos form could also be argued as acompañarse; chose plain verb
# question alv: Mexican slang abbreviation (a la verga); dropped as an abbreviation not suited to a learner list
# question anti-cáncer: anticancerígeno is an alternative target, but anticáncer is the closer spelling.
# question anti-cáncer: dropped as a hyphenated compound, though anticáncer is arguably the standard spelling
# question chippendale: also an established furniture style and a dance troupe name; dropped because most uses are place or brand names
# question cuqui: lowercase uses are only about a third of the examples, so the real-word reading is borderline; kept.
# question cuqui: real adjective reading (lowercase) is about 32% against nickname Cuqui, borderline for the one-third threshold
# question espaciadora: feminine adjective filed as its own lemma and used almost only in "barra espaciadora"; merged into espaciador, but "barra espaciadora" could also be kept as a unit.
# question espaciadora: feminine adjective occurring only in "barra espaciadora"; kept as is, but could be merged to espaciador or to the compound barra espaciadora
# question facho: Spanish colloquial "facho" (fascist) exists, but the examples are mostly Monte Facho and a surname, so I dropped it.
# question facho: most of the 69 occurrences are the place name Monte Facho or a surname; the common word facho (fascist) looks under a third, so drop may be the correct call
# question formé: tagged PROPN but examples are the verb formar (1st person preterite), so merged rather than dropped
# question gram-positivas: target spelling grampositivo chosen, though "gram positivo" is also written
# question hebreos: only the Bible book title occurs; if a learner entry is wanted it would be hebreo, but the title reading was dropped
# question hebreos: the examples are mostly the Bible book title (which would drop), but the ethnonym reading is merged into hebreo
# question hippocampus: could be merge:hipocampo if the brain reading dominates, but no examples were available
# question hippocampus: could be the Latin taxon (drop) but examples are unseen; merged to hipocampo as the English/Latin spelling of the adapted word
# question kairós: Greek concept word, but the example reads as a name; dropped
# question kairós: a real philosophical and theological term, but the examples read as a name, so dropped.
# question kameez: garment loan from Urdu, mostly in "shalwar kameez" product text; dropped as not established enough
# question meze: loan is used on Spanish menus, but the examples are mostly a misspelling of "meses", so dropped
# question mype: acronym of Peruvian usage (micro y pequeña empresa) treated as an ordinary word; could instead be seen as regional specialist term
# question mype: kept as an ordinary-word acronym in Peruvian Spanish, though it is also a regional administrative term
# question no-nacido: merged into the two-word unit "no nacido"; drop is the alternative if hyphenated forms are treated as compounds of two listed words.
# question omep: international education NGO rather than a famous body like ONU or OMS; dropped as a specialist acronym.
# question pilsener: the beer-style sense (pilsen) could be a common word, but the examples and capitalisation point mainly to the Ecuadorian brand, so it was dropped.
# question power-up: hyphenated gaming loan, kept as established but could be seen as marginal
# question tembleque: real-word reading is about a third (36%), the rest are the town; borderline.
# question unmiss: a UN body, but a single peacekeeping mission rather than a famous international body, so dropped
# question espaciadora: should feminine adjective forms filed as lemmas merge into the masculine, as feminine gentilics do, or keep their own entry like feminine nouns?
# question no-nacido, forma-de-vida: should hyphenated spellings of established multi-word noun units (los no nacidos, forma de vida) merge into the spaced unit instead of dropping?
```

## Question lines: unflagged (25)

```
# question capacítese: capacitar and capacitarse are both common; merged into the pronominal verb per the clitic ruling
# question cienta: fragment of -cientas numerals (doscientas, trescientas); no single obvious target lemma, so dropped
# question colpa: Peruvian Spanish "colpa" (clay lick) is real, but the sampled examples are tourism-specific; dropped as marginal.
# question crep: no examples shown; merged into crepe on the strength of the written forms (creps, Crepes).
# question enoxaparin: enoxaparina is a fairly specialist drug; I merged it under the rule for English spellings of adapted names, but it may belong in drop.
# question framerate: a technical loan; I kept it because of gaming use, but it is borderline with specialist vocabulary.
# question framerate: tech loan; borderline between established and jargon, kept
# question hehehe: laughter spelling, not covered by the interjection rule (vaya, hala); dropped as an artefact
# question kudzu: Japanese-origin plant name; kept as an established common noun, but a specialist term, so could go either way
# question kudzu: plant name used in Spanish text but of Japanese origin; kept as a common organism name
# question macla: MACLA is also an arts organisation (27 of 72), but the common-word reading is over a third, so kept.
# question macla: lowercase mineral sense is about half the examples, the rest is the organisation MACLA; kept for the common word
# question nuraga: Spanish also writes nuraghe; I kept the form people write here.
# question nuraga: Spanish also writes nuraje or nurague; kept the form found in the counted text
# question ortopeda: ortopedista is the more usual form; kept because ortopeda is a real word
# question perindopril: specialist vs common drug; kept as a widely prescribed generic ACE inhibitor, may be judged specialist.
# question querosén: the list writes the form people write, and querosén is the common Latin American spelling; the rule says to merge to the standard form, but if querosén is the form people write it may deserve its own entry.
# question querosén: the rules say both "use the form people write" and "variant spellings merge into the standard one"; I kept querosén because it is the attested regional form, but merge:queroseno is defensible.
# question reichsführer: German SS rank appearing in Spanish historical texts; treated as a title and dropped.
# question sobrero: examples show a surname and a typo for sombrero; the bullfighting sense (toro sobrero) is not clearly attested.
# question sobrero: the examples mix a surname, a typo for sombrero and a rare bullfighting term; I dropped it without being able to measure the shares.
# question splatter: borderline loan; kept as an established film-genre term, though niche
# question splatter: no examples to check; kept as the established film-genre loan.
# question wáter: the screener calls it a variant of váter; kept as wáter because it is the form people write, so a merge into váter may be wanted instead.
# question wáter: váter is the other spelling; kept wáter as the dominant written form, merge into váter if the coordinator prefers the academy form.
```
