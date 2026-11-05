# es review shard 26: report (round 18, cascade)

Base `543d45d`, whose `review/rules` (now carrying the diminutive call) match `full-es` 2d4e2c1. The runtime, lemma
wheel and corpus sample were reused from this session's shard 10 (setup script and extractor unchanged). Every
review.py line passed `--rules` and `--decisions keep,drop,merge`.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 181 |
| flagged with examples | 143 (79.0 %, **below the ~85 % mark**) |
| flagged: reviewers agreed / to adjudicator | 170 / 11 |
| flagged: queried at the gate | 2 |
| flagged final: agreed / adjudicated | 168 / 13 |
| **flagged final: keep / drop / merge** | **10 / 147 / 24** |
| unflagged screened | 203 (1 batch, 0 failed) |
| suspects (either screener / both) | 112 / 81 |
| suspects with examples | 95 (84.8 %, just below the ~85 % mark) |
| unflagged: reviewers agreed / to adjudicator | 104 / 8 |
| unflagged: queried at the gate | 1 |
| unflagged final: agreed / adjudicated | 103 / 9 |
| **unflagged suspects final: keep / drop / merge** | **18 / 50 / 44** |
| unflagged not suspected (stay keep) | 91 |

Gate reading: every merge, keep and accent merge in both rounds (flagged 0, unflagged 1), every unflagged drop, and
every flagged drop whose reason mentions a fragment, doubled word, plural, misspelling or real-word share. No final
keep is a regular diminutive.

## Queries and outcomes

| round | lemma | agreed | why queried | adjudicated |
|---|---|---|---|---|
| flagged | diosesdiose | drop | earlier rounds merged doubled words with an obvious base (aguaagua -> agua) | merge:dios |
| flagged | mañanamañana | drop | same pattern | merge:mañana |
| unflagged | angelita | merge:ángel | reviewers note the examples are mostly a person's name | drop |

No splits requested beyond any `split by form` question lines below.

## Notes

* Both queues fell below the ~85 % example share (79.0 % flagged, 84.8 % suspects); carried on as the file says.
* Nothing failed: no failed screener batches or review calls, 0 undecided after adjudication.

## Question lines: flagged (25)

```
# question bodysuit: Merged into "body" as an English spelling of the adapted word; if "body" is not on the list, drop instead.
# question buap: kept as a nationally known Mexican state university on the UNAM model; confirm it counts as nationally famous.
# question cicpc: Venezuelan national investigative police; treated as a household-name national body, so keep
# question dabigatr: dabigatrán is a specific anticoagulant; merged as a generic drug, but drop if the coordinator treats it as specialist.
# question decamétrico: real Spanish technical adjective (ondas decamétricas) but of marginal learner value; kept because the lemma is sound.
# question eco-sostenible: merged to ecosostenible (standard spelling); if the rules treat eco- plus sostenible as a hyphenated compound of two listed words, it would drop instead.
# question gulet: borderline loan for a boat type; dropped as not established enough in Spanish
# question gulet: loan not in the academy dictionary, kept because the boat reading dominates, but it is a niche term
# question inba: Mexican INBA is a national body, but the examples mix Argentine and Hungarian uses, so I dropped it.
# question inba: the examples mix Mexican, Argentine and Hungarian bodies, so no single famous institution; dropped
# question inifap: Mexican national agricultural research institute; dropped as not a household name, but it could count as a national public body.
# question inifap: national research institute; kept as a public body, though less of a household name than UNAM or RENFE.
# question jatoba: Spanish may write it jatobá; kept as written in the list
# question mariage: only one example is a Spanish-context use (maridaje misspelt); the rest are French, so drop may be preferable
# question minero-medicinal: hyphenated compound of two listed words would normally drop, but it is a fixed term for spa waters; kept as one unit
# question oh-oh: hyphenated interjection variant; kept, could instead merge into a plain "oh" entry if one exists
# question onusal: UN mission, could count as an international body; dropped because it ended in 1995
# question platanito: lowercase platanitos is the diminutive of plátano, but many hits are the Platanitos brand/site
# question sapele: Nigerian city name appears in some examples; kept for the wood reading (about two thirds of examples)
# question toril: Capitalised "Toril" (51) is likely a place or surname, so I dropped it by the one-third rule; if those are mostly sentence-initial uses of the bullring word, it should be kept.
# question utpl: Single regional university; kept as a nationally known Ecuadorian university, but it is borderline against the "single institution" rule.
# question utpl: nationally known Ecuadorian private university; kept as a famous institution, but borderline
# question voice-over: used by Spanish-language professionals, but the usual Spanish term is "voz en off"; dropped as not established
# question platanito: lowercase "platanitos" may be the lexicalised plantain-chip snack (Peru, Ecuador); if so, it should be keep, not merged into plátano
# question toril: no examples in the sample; capitalised Toril/Toriles could partly be the bull-pen word (e.g. "Puerta de Toriles"), which might lift the real reading above a third
```

## Question lines: unflagged (25)

```
# question abeliano: derived from the name Abel but a standard mathematical adjective; kept
# question alejándote: clitic -te merged to pronominal verb alejarse by the developer ruling.
# question angelita: examples are mostly the personal name Angelita, real diminutive reading may be under a third; merged by the diminutive rule but drop is arguable
# question angelita: examples are the personal name Angelita; merged to ángel by the diminutive rule, but drop is possible if name dominates.
# question autoabastecer: most forms are autoabastecerse; kept the lemma as given
# question caloroso: no examples; assumed a variant of caluroso rather than Portuguese or Italian text.
# question caloroso: the DRAE does list caloroso, but these hits look like Portuguese/Italian; merged into caluroso
# question dominatrices: Spanish normally uses the loan dominatrix; plural dominatrices merged to it.
# question folklor: folclor and folclore are both academy-accepted; chose folclore as the more written form
# question hazar: the lemma mixes hazara (ethnonym) with Hazar (lake/name); decided for the hazara reading
# question hazar: the majority reading is the ethnonym hazara, but Hazar (30) is a name, so the lemma is mixed; merged to hazara.
# question iniciante: kept as a RAE entry, though the examples may show Portuguese influence and principiante is the usual word.
# question orgón: Reich's term, but not a general learner word; dropped as specialist.
# question orgón: real Spanish noun but a niche Reich pseudoscience term; kept since it is a genuine word
# question platforma: about half the hits are the capitalised organisation PLATFORMA; merged as the misspelling reading, drop is defensible
# question platforma: many occurrences are the organisation PLATFORMA; merged to plataforma anyway.
# question primea: examples mix a misspelt primera and a hotel brand; decided drop as unclear
# question primea: misspelling of primera vs. hotel brand; dropped as unclear.
# question rebufar: lemma filed as verb but forms are mostly the noun rebufo; kept as is, maybe merge:rebufo.
# question reventazón: examples shown are all the Reventazón river/project, so the common noun reading may be under a third; kept on the assumption of real word use, check.
# question swimrun: sport name, borderline loan; dropped as not yet established.
# question torreña: torreña could be Torrevieja/Torre-town gentilic of several places; merged to torreño as the obvious masculine
# question zakaah: the Spanish target could be zakat or azaque; chose zakat as the form people write
# question autoabastecer: split by form: autoabastecerse, autoabastecernos, autoabastecerte -> autoabastecerse
# question folklor: confirm the target is folclore (the academy's main form) and not folclor or folklore, if one of those is the spelling the list already uses
```
