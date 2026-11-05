# es review shard 24: report

Branch `es-review-shard-24` (from `543d45d`). Every `review.py` line ran with `--rules` and `--decisions keep,drop,merge`. The rules files at `543d45d` are identical to `origin/full-es` (`2d4e2c1`) and include the diminutive call; every stage used them. The runtime, wheel, review scripts and sample were reused from this session's shard 8 work directory through symlinks, and the setup script was rerun with `WORK=$HOME/es-review-24`.

## Counts
| step | count |
|---|---|
| flagged queue | 182 (examples 141 = **77 %**, below the ~85 % mark) |
| flagged reviewers | 176 agreed (drop 156, merge 12, keep 8), 6 disagreements, 0 accent-only merges |
| flagged after adjudication | 173 agreed + 9 adjudicated (6 disagreements + 3 queries), 0 undecided |
| flagged final | keep 8, drop 156, merge 18 |
| unflagged screened | 203 (1 batch, 0 failed); candidates 154 (both screeners 132) |
| suspects examples | 131 / 154 = 85 % |
| unflagged reviewers | 145 agreed (drop 52, merge 51, keep 42), 9 disagreements, 2 accent-only merges |
| unflagged after adjudication | 144 agreed + 10 adjudicated (9 + 1 query), 0 undecided |
| unflagged final | keep 44, drop 56, merge 54 (unscreened unflagged lemmas stay keep) |

The flagged example share is below 85 %. I carried on as the instructions say. No regular diminutive came up in either round: no keep looks like one, and no decision cites the diminutive rule.

## My queries (gate) and outcomes

### s24-flagged

| lemma | why queried | adjudicated |
|---|---|---|
| calicanto | agreed drop, but calicanto (stone-and-lime masonry) is a real Spanish noun; check whether the common word is a third or more | drop: lowercase masonry sense is about 14/68 (≈21%), below a third; the rest is the station name |
| pampero | agreed drop, but pampero (the pampas wind; of the pampas) is a real Spanish word; check whether that reading is a third or more | drop: mostly the company Grúas Pampero; the wind/pampas sense is about 12%, below a third |
| anti-austeridad | agreed drop, but hyphenated prefix spellings merge into the solid form (anti-héroe → antihéroe, anti-arañazo → antiarañazos in earlier rounds); check merge:antiausteridad | merge:antiausteridad: anti- is a prefix, not a listed word; hyphenated prefix spellings merge into the solid form |

### s24-unflagged

| lemma | why queried | adjudicated |
|---|---|---|
| seise | agreed merge:seis, but seise is a real Spanish noun (the Seville cathedral choirboys, los seises); check whether the examples are that word or the plural of seis | merge:seis: the only example is the plural of the number ("seises y sietes y nueves"), not the Seville choirboys |

How I picked them: I read every merge, every keep, every drop lemma and the accent-merges files. I queried agreed decisions that might hide a second real word, and one drop that didn't match the prefix-hyphen pattern. All the accent-only merges looked right. The queries changed only anti-austeridad → antiausteridad.

## What went wrong
* Nothing failed. Every stage finished on its first run.
* The flagged example share is 77 %.

## Every `# question` line

### s24-flagged

```
# question apdo: examples show "APDO" used oddly as a device label (likely "apagado"); merged to apartado on the abbreviation reading.
# question apdo: examples show APDO as an equipment label (probably "apagado"), but the capitalised forms look like the postal-address abbreviation Apdo.; merged to apartado on the majority reading.
# question calicanto: also a real word (a masonry mortar), but the examples are about a station/place, so dropped.
# question involucrándo: split by form: involucrándolos -> involucrar
# question kokeshi: Japanese doll name; could count as an established loan, but dropped as a niche foreign word
# question norte-este: could merge into noreste as a variant spelling; I applied the hyphenated-compound drop rule instead
# question nuestr: cut-off fragment of nuestro, but variants (nuestres, nuestrs, nuestrás) make the target unclear; dropped.
# question pvpc: a regulated Spanish electricity tariff that many households know by name, so it could count as an ordinary-word acronym; I treated it as a technical acronym and dropped it
# question pvpc: tariff acronym seen on Spanish electricity bills; dropped as technical, but a learner in Spain might meet it.
# question pí: capitalised in 93% of uses with no example; may be a Catalan surname or a variant of "pi" (the number), so it is dropped
# question pí: no examples, mostly capitalised; may be Catalan "Pi" or a misspelling of "pi", so dropped as a name
# question rips: no example in sample; dropped as non-Spanish acronym/plural, unclear what it denotes
# question rips: no examples were available, so the reading is a guess from the written forms
# question sclc: no examples were available; judged as the medical acronym (small-cell lung cancer) from the form alone
# question sepla: a union, which the rules might class as an ordinary organisation; I kept it as a national body in the ETECSA sense
# question shel: no examples were available; judged a name or fragment from the form alone
# question surfhouse: could be an established loan like surf camp, but frequency and usage look like business-specific name
# question technyl: no examples were available; judged a brand name from the form alone
# question valiéndono: -nos fragment merged into the pronominal verb valerse (valiéndonos de), since "valerse" is common; plain "valer" would be the alternative
# question yinn: unsure whether a learner's list wants this loan; kept because the lowercase common-noun use dominates
# question buganvilia: buganvilia is widely written (esp. Mexico) alongside RAE buganvilla; confirm the variant rule beats "the form people write" here, and which of noreste/nordeste is the listed lemma for norte-este
# question involucrándo: split by form: involucrándolos -> involucrar
```

### s24-unflagged

```
# question aumentación: could be merged into aumento as a calque, but the sense is unclear, so dropped
# question aumentación: not a standard word; merged into aumento as a calque, though dropping is also defensible
# question aver: could be haber or a ver; merged to a ver as the commonest written error
# question aver: examples missing, and some forms (averá, AVer) may be a brand or other words; decided on the dominant misspelling reading of a ver.
# question batanar: split by form: batanes, batana, batanas -> batán
# question batanar: split by form: batanes, batanas, batán -> batán
# question desmemoriar: forms include noun "desmemoria" (35); merged to desmemoriado, but the noun may deserve a separate entry
# question desmemoriar: split by form: desmemoria -> desmemoria (noun); desmemoriado/desmemoriados/desmemoriada -> desmemoriado
# question despulpar: lemma mixes the verb with despulpe/despulpado forms; kept for the verb reading
# question empavesar: split by form: empavesado (noun, ship dressing/flags) vs empavesado (participle); merged to the noun/adjective form empavesado
# question frite: imperative of freír (Frite grupos...) vs French "frites" in "moules et frites"; I merged to freír, but the French reading may be a large share
# question garete: only occurs in "al garete"; kept as a real word, but the coordinator may prefer the phrase as the unit
# question guantero: guantera (glove compartment) is a different noun from guantero (glove maker); I merged to guantera since it dominates the forms
# question metilsulfonilmetano: MSM is a common supplement ingredient, but treated as a specialist chemical name rather than a common generic drug.
# question pastoralmente: regular -mente adverbs have no stated rule; kept as a real, attested word
# question posherpética: lemma is the feminine form and the base posherpético is not itself listed; merged to the masculine per the gentilic/feminine pattern.
# question postpago: pospago is the academy form but postpago is the form people write (and prepago pairs with it); kept as its own entry
# question postpago: pospago is the academy form, but postpago is the usual spelling in the text; merged per the variant-spelling rule.
# question seise: "seises" is also the Seville cathedral choirboys, a real noun; the only example is the number plural, so merged into seis.
# question tinidazol: a fairly common generic antibiotic, borderline between a common and a specialist drug; dropped
# question ufscar: Brazilian federal university (not Spanish-speaking world), dropped as not a household name for Spanish learners
# question upar: forms are mostly upa/upo (interjection or noise); no clear Spanish lemma, so dropped.
# question webdoc: could be an established loan for "documental web", but there are no examples and uppercase uses look like a brand; dropped
# question frite: merged into fritar, the verb these forms actually conjugate; if fritar isn't on the list, should regional verb variants merge into the standard verb (freír) instead?
# question seise: the 2 capitalised "Seise" could be the choirboys' noun, but there is no example to confirm; should a split by form (Seise -> seise) be written, or is 2 occurrences too few to matter?
```
