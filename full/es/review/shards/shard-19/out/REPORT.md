# es review shard 19: report (round 17, cascade)

Branch `es-review-shard-19`, created from `origin/full-es` at `ae73f55`. The rules files are unchanged since
0095cdd. I reused shard 15's runtime, wheel and sample, copied into `$HOME/es-review-19`, and reran the setup
script there for the config and `routed.tsv`. All `review.py` lines passed `--rules` and
`--decisions keep,drop,merge`. There were no failed calls and nothing was rerun.

**Diminutives:** the coordinator's new call (regular diminutives merge into the base) is recorded in
`full/es/junk-review.md` but is not in the binding rules files given to reviewers and adjudicator, and I don't
edit those. So the decisions here follow the rules files alone. The diminutive-shaped lemmas are listed below for
the coordinator to apply its call at collection.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 272 |
| flagged with an example | 207 (76.1%: **under the ~85% mark**) |
| flagged reviewers agreed | 267 (drop 228, merge 21, keep 18); 5 sent to the adjudicator; 0 accent-only merges |
| flagged queried at the gate | 1 |
| flagged adjudicated (5 disagreements + 1 query) | 6 (drop 3, merge 3) |
| **flagged final** | **keep 17, drop 231, merge 24** |
| unflagged screened | 300 (2 batches, 0 failed) |
| suspects (either screener) | 192 (158 marked by both) |
| suspects with an example | 160 (83.3%: **under the ~85% mark**) |
| unflagged reviewers agreed | 183 (drop 87, merge 63, keep 33); 9 sent to the adjudicator; 7 accent-only merges |
| unflagged queried at the gate | 0 (`queries.tsv` is empty) |
| unflagged adjudicated (9 disagreements) | 9 (keep 4, drop 3, merge 2) |
| **unflagged final** (suspects only; the 108 non-suspects stay keep) | **keep 37, drop 90, merge 65** |

## Gate

I read every agreed merge and keep in both rounds and all the agreed drops (lemma and reason). I checked forms
where a drop might hide a real word (repón, negocia, celos, decora, princip, llam, pánfilo, chacho, universiada);
each is a capitalised name, brand or event, with the real reading a small minority, so those decisions hold. The
accent-only merges (vacaciónes, nucléico, mísil, polícia, cristaleria, impérial, avaluo) are plain misspellings.

Flagged query → adjudicator:
- unidroit (agreed keep as an international body) → **drop** (specialist institute; consistent with ORECE,
  FEOGA and SICOFAA).

## Things for the coordinator

- Example coverage is under ~85% in both queues (76.1% and 83.3%). Per the instructions I noted it and carried on.
- **Diminutive-shaped lemmas, for the coordinator's diminutive call:**
  - cestita **keep** and cremita **keep** (unflagged): regular diminutives of cesta and crema, so under the
    call they would be merge:cesta and merge:crema;
  - hornito **keep** (flagged): the examples are mostly the volcanic formation (hornitos y jameos), which reads
    as lexicalised;
  - peñoncillo **drop** (unflagged): a place name.
- Split-by-form questions (ruling 2), which the coordinator writes: escorzar (escorzo, escorzado, escorzada,
  escorzadas → escorzo), faldear (faldeo → faldeo).
- Possible new classes of question:
  - regional-language cultural terms common in Spanish text but not in the academy dictionary (caganer);
  - rival adaptations with different suffixes (milénico vs milenial);
  - Latin American calques missing from the dictionary (retaliación);
  - whether the adapted spelling (tuitear) or the commoner written one (twitear) is the target;
  - another obscure international body dropped (unece).

## Every `# question` line

The question lines are in `s19-flagged/questions.txt` (33 lines) and `s19-unflagged/questions.txt` (31 lines),
reproduced below.

### s19-flagged
```
# question anti-fatiga: could merge into antifatiga if that is on the list; dropped as a hyphenated compound
# question ayni: Andean reciprocity concept, possibly worth keeping, but no examples were shown and it is mostly capitalised, so dropped
# question carbonio: could be a deliberate Italian/product word, merged to carbono as the obvious Spanish lemma
# question cazadero: lowercase reading is about 31% of occurrences, borderline for the one-third rule, so kept
# question cazadero: lowercase use (~32%) is borderline against the "about a third" threshold; the capitalised use is mostly a place in California
# question celos: tagged PROPN with mostly all-caps evidence, so dropped; the real plural-only noun "celos" probably sits under another lemma.
# question co-creativa: cocreativo may not be on the list; if it isn't, drop is the alternative
# question co-creativa: cocreativo may not itself be on the list; merge target assumed
# question cryptocurrencie: English plural, not merged into criptomoneda since the text appears to be English.
# question doner: a loan from Turkish; kept as established food vocabulary, though some writers spell it döner or just kebab
# question doner: borderline loan; kept as an established food word (döner/kebab)
# question faba: Asturian/Spanish word for haba, but occurrences are mostly the protected bean name; dropped
# question faba: Faba is a real Spanish word (fabada, fabas) but most examples are the Asturian bean denomination; dropped as a name
# question feaga: Spanish national agricultural fund; dropped as not a household name, but the institution rule could arguably keep it.
# question feaga: national EU agricultural fund, borderline institution; dropped as specialist.
# question intermezzo: examples show a bar name and a drug brand, so the music reading may be under a third
# question kohen: Jewish priestly title; treated as a foreign term, not an established loan
# question lilis: possibly a plural of lili (flower), but most occurrences look like a name; dropped
# question métis: capitalised in 69% of examples; kept as an ethnonym, but it could be treated as a proper noun
# question métis: ethnonym of a Canadian people, kept under the lowercase-ethnonym ruling, though it is capitalised in 69% of the text
# question nance: the fruit nance is a real Spanish word, but the examples show only the place name
# question negocia: could be a conjugated form of negociar, but the counted forms are all capitalised brand-style, so dropped
# question no-oficial: could merge to "oficial" with a negation, but dropped as hyphenated compound of listed words
# question pre-embarque: merge target preembarque is assumed to be the standard spelling
# question repón: could be the imperative of reponer, but it is always capitalised and has no examples, so dropped as a name
# question repón: tagged PROPN with no examples, so the imperative of reponer cannot be confirmed
# question satay: borderline for how established it is in Spanish; kept because it appears on Spanish menus
# question unece: international body, but not clearly a household name in Spanish; dropped
# question unece: international body, but only in its English acronym (Spanish is CEPE) and not a household name, so dropped
# question unidroit: specialist intergovernmental body; kept as an international body, but it is not a household name
# question valenciana: the examples are company names in all-caps, so the common-word reading may be under a third; merged as the gentilic anyway.
# question vendr: forms are vendrán/vendrás/vendrá and also Vendres (Catalan Friday); decided for the venir reading
# question vendr: mixed with Catalan "vendres" (Friday); decided for the Spanish venir reading.
```

### s19-unflagged
```
# question amiodarone: the English form could merge to amiodarona, but dropped as a specialist drug
# question bodystocking: product-catalogue term (Milanoo); kept as an established lingerie loan, but could be seen as a rare product term
# question caganer: Catalan figure widely named in Spanish Christmas contexts, but not in Spanish dictionaries; dropped as not established.
# question caganer: Catalan, but Spanish texts use it as the usual name of the figure; kept as an established cultural loan
# question chacho: a real colloquial word, but the examples are mostly the name Chacho (well under a third); I dropped it.
# question chacho: real Spanish colloquial word (chacho/chacha) exists, but the examples shown are names; dropped on the one-third rule.
# question escorzar: split by form: escorzo -> escorzo
# question escorzar: split by form: escorzo, escorzado, escorzada, escorzadas -> escorzo
# question faldear: split by form: faldeo -> faldeo
# question famotidine: all examples are English drug-leaflet text; merged to the Spanish generic famotidina
# question homeschooling: borderline loan; kept as established in Spanish web text
# question milénico: milenial may be the preferred spelling; no rule settles which adapted form is the lemma
# question milénico: the examples use the word for the generation (millennials), not the "millennial" sense of milenario; the target milenial is my guess at the standard spelling
# question nuer: ethnonym split between lowercase and capitalised; kept as lowercase ethnonym, though nuerte and nuers look like noise
# question panderia: the merge to panadería is inferred from the contexts; the lemma could also be read as pandería, which seems far less likely
# question pentoxifilina: borderline between a common generic drug and a specialist one; dropped as specialist
# question pentoxifilina: generic drug with an adapted name, but only specialists use it; I judged it specialist and dropped it, so confirm if it should count as a common generic drug
# question perdicera: occurs almost only in "águila perdicera"; merged to perdicero, but could be dropped as specialist
# question radiónico: pseudoscientific specialist term; kept as an ordinary adjective, but it could be dropped as too specialist.
# question radiónico: real but niche pseudoscience term; dropped
# question retaliación: calque in Latin American legal and workplace Spanish with 77 uses; I dropped it as an anglicism, so confirm whether it should be kept as an established usage
# question retaliación: calque of English "retaliation" and absent from the academy's dictionary, but used in Latin American Spanish; kept, could instead merge to represalia
# question sampleado: could be a noun (sampleado = sampling) as well as a participle; merged to samplear on the participle reading.
# question sampleado: samplear is not clearly established as a Spanish lemma, so it may be better to drop; I merged it into the verb.
# question twitear: the rules favour the adapted spelling tuitear, but twitear is the commoner written form here; confirm which one the list should use.
# question universiada: a generic common noun for the games, but all occurrences are capitalised and refer to specific events; I dropped it.
# question universiada: lowercase common noun exists in Spanish, but all occurrences are capitalised event references; dropped as an event name.
# question webcomic: borderline loan, kept by analogy with web and blog
# question webcomic: borderline loan; kept because it is used as an ordinary noun in the examples
# question caganer: is a Catalan cultural term widely used in Spanish texts but absent from the DLE (also sardana-type words) established enough to keep, or should it be dropped as a non-Spanish token?
# question milénico: should a rival adaptation with a different suffix (milénico vs milenial) count as a variant to merge into the standard form, or keep its own entry?
```
