# es review shard 20: report

Branch `es-review-shard-20` (from `ae73f55`). Every `review.py` line ran with `--rules` and `--decisions keep,drop,merge`. The rules files at `ae73f55` are identical to `origin/full-es` (`eb2aea4`), and every stage used them. The runtime, wheel, review scripts and sample were reused from this session's shard 8 work directory through symlinks, and the setup script was rerun with `WORK=$HOME/es-review-20`.

**Diminutive call** (coordinator, 2026-11-05, in `full/es/junk-review.md`: regular diminutives merge into the base word, lexicalised ones keep). The call isn't in the binding rules files the reviewers read, and I didn't edit those. Instead I checked every keep in both rounds for a regular diminutive, ready to query any I found. There were none: a suffix check (-ito/-illo/-cito and variants) matched only `adulamita`, which is a biblical gentilic, not a diminutive.

## Counts
| step | count |
|---|---|
| flagged queue | 271 (examples 214 = **79 %**, below the ~85 % mark) |
| flagged reviewers | 255 agreed (drop 220, merge 27, keep 8), 16 disagreements, 0 accent-only merges |
| flagged after adjudication | 251 agreed + 20 adjudicated (16 disagreements + 4 queries), 0 undecided |
| flagged final | keep 12, drop 223, merge 36 |
| unflagged screened | 301 (2 batches, 0 failed); candidates 203 (both screeners 171) |
| suspects examples | 168 / 203 = **83 %**, below the ~85 % mark |
| unflagged reviewers | 194 agreed (drop 89, merge 53, keep 52), 9 disagreements, 2 accent-only merges |
| unflagged after adjudication | 187 agreed + 16 adjudicated (9 + 7 queries), 0 undecided |
| unflagged final | keep 55, drop 91, merge 57 (unscreened unflagged lemmas stay keep) |

Both example shares are under 85 %. I carried on as the instructions say.

## My queries (gate) and outcomes

### s20-flagged

| lemma | why queried | adjudicated |
|---|---|---|
| hijahija | agreed drop, but doubled-word artefacts with an obvious target were merged in earlier rounds (fuegofuego → fuego, palabrapalabra → palabra); check merge:hija | merge:hija: doubled-word artefact with an obvious target, consistent with fuegofuego → fuego |
| insula | agreed drop, but it may be ínsula without the accent (a real Spanish word; also the anatomical ínsula); check whether that reading is a third or more | drop: lowercase ínsula reading is only about 16% of occurrences; capitalised name uses dominate |
| huanca | agreed drop, but huanca is a lowercase Peruvian ethnonym (los huancas), which the second-set rulings keep; check the examples | drop: mostly surname or place; the lowercase ethnonym is about 13%, under a third |
| post-ciclo | agreed drop, but this round merges hyphenated prefix spellings (post-colonial → poscolonial); check consistency (merge:posciclo?) | merge:posciclo: hyphenated prefix spelling, merged for consistency with this round |

### s20-unflagged

| lemma | why queried | adjudicated |
|---|---|---|
| recomer | agreed merge:recomendar, but recomer (recomerse, to be eaten up by worry) is a real verb; check whether its forms are a real share | merge:recomendar: recomendo and recomen dominate; real recomer forms (recome, recomida) are about 8 of 68, under a third |
| nooo | agreed drop, but stretched spellings with an obvious target merge (ufff → uf in this round, taaaan → tan earlier); check merge:no | merge:no: stretched spelling of no; same treatment as ufff → uf and taaaan → tan |
| quasi | agreed drop, but it may be the Latin spelling of cuasi, which Spanish writes with c; check merge:cuasi | drop: the only example is Italian and the capitalised forms look like names; no evidence of Spanish writers using it for cuasi |
| idus | agreed drop, but idus is a real Spanish word (los idus de marzo); check whether that reading is a third or more | keep: about 48 of 73 forms are not the idUS repository acronym, so los idus de marzo is plausibly a third or more |
| dormit | agreed drop, but it may be a cut-off of dormitorio (domitorio → dormitorio merged in this round); check for an obvious merge target | drop: Catalan participle; no examples to support a dormitorio cut-off |
| limpiaza | agreed drop, but it looks like a misspelt limpieza, which the rules merge; check the examples | drop: no examples, and 73 of 74 forms are capitalised, which points to a name rather than a misspelt limpieza |
| papudo | agreed drop, but papudo is a real Spanish adjective (double-chinned; Chilean place name too); check whether the common word is a third or more | drop: all forms are capitalised and the examples show only the Chilean town; common-adjective reading is well under a third |

How I picked them: I read every merge, every keep, every drop lemma and the accent-merges files. I queried agreed decisions that might hide a second real word or a lowercase ethnonym, and drops that didn't match the patterns already applied (doubled words, prefix hyphens, stretched spellings, misspellings). All the accent-only merges looked right. The queries changed hijahija → hija, post-ciclo → posciclo, nooo → no and idus → keep.

## What went wrong
* Nothing failed. Every stage finished on its first run.
* The example shares are below 85 % (see above).

## Every `# question` line

### s20-flagged

```
# question amorita: lemma mixes the ethnonym (amoritas, lowercase) with the name Amorita (about half); kept for the ethnonym reading.
# question amorita: no examples; amorreo is my guess for the intended lemma and could instead be a brand or name.
# question balsamera: rare (biblical) word, keep is borderline for a learner list, but the lemma itself is correct
# question butternut: kept as an established loan for the squash; confirm vs. a drop for being a food-menu English word
# question campano: unclear how many examples are surnames/place names; kept as common word on a guess.
# question cenesex: a national Cuban body; kept as a household name there, but it is less famous than ETECSA.
# question comprimidos: the plural-form merge is clear, but examples are almost all drug labels; keep as comprimido if that counts as the real reading.
# question csnu: merge target is a guess; CSNU is the Spanish abbreviation of Consejo de Seguridad de las Naciones Unidas, and ONU may not be the right lemma (alternatively drop).
# question decidno: rules say clitic -nos fragments merge to plain verb or pronominal verb; merged to decidnos per surface form, probably should be merge:decir.
# question dormid: decided keep but it is a conjugated form; better merge:dormir.
# question fge: possibly Fiscalía General del Estado (a national body), but there are no examples and the casing FGe is odd; dropped.
# question fonca: national body, but only specialists in arts and culture may know it; kept as a household name in Mexico
# question fonca: treated as a national Mexican public body (Fondo Nacional para la Cultura y las Artes); confirm it counts as a household name
# question front-office: hyphenated English business term; dropped rather than merged into "front office", as it is not clearly established in Spanish
# question kfor: international force rather than a body proper; kept as a famous international body, could be judged a specialist acronym
# question kfor: international military mission; dropped as not a household name like OTAN
# question lavadora-secador: written lavadora-secadora, a real appliance word; dropped under the hyphenated-compound rule, but a merge to a closed spelling could be wanted
# question mistol: real Spanish tree and fruit word, but about 27% of examples; dropped as below a third
# question mistol: tree/fruit reading seems real but some examples are street names; kept on the common-word rule
# question paleoceno: the examples show mostly capitalised geological-period use; kept as a real common term, but it is specialist vocabulary
# question post-colonial: merged to poscolonial assuming the academy's simplified spelling is the standard form.
# question post-tensión: postensión is my best guess for the standard spelling; confirm
# question pre-factibilidad: merged into factibilidad assuming it is a listed lemma; if only "factibilidad" is absent, keep decision may differ.
# question rosetas: lemma holds the real plural of roseta (rosetas de maíz, popcorn, is also a common plural-only use), but the examples are mostly capitalised product text; merged into roseta.
# question rosetas: the examples are product names, but roseta is a real word, so merged to the singular
# question separarno: lemma tagged as -nos clitic form of separar; merged into pronominal separarse as the common verb (all examples are separarnos).
# question separarno: the -nos fragment rule names -nos/-te; applied to separarse as common pronominal verb, though separar is also plausible.
# question tapatía: tapatío is a demonym for Guadalajara; confirm it is on the list as a common word, otherwise drop.
# question uaa: UAA is a regional university, not clearly nationally famous; decided drop.
# question uaa: regional university, not a nationally famous institution, and many examples are a technical code
# question zafu: real Spanish-adjacent meaning (meditation cushion) may be a loan; decided drop as specialist.
# question balsamera: words found only in Bible text (Reina-Valera), with a correct lemma; keep as real words, or drop as archaic for learners?
# question butternut: food loans that occur mostly as a modifier after a Spanish noun (calabaza butternut); established enough to keep?
```

### s20-unflagged

```
# question adulamita: biblical gentilic kept under the lowercase-ethnonym ruling; very low learner value
# question adulamita: lowercase gentilic from the Bible; dropped because it is rare and tied to the place Adulam
# question algunxs: the rules do not cover inclusive-x forms; merged into alguno
# question canil: Portuguese-looking kennel word mixed with the Caniles place name; no examples were available, so the real-word share is unclear.
# question cocooning: the examples are mixed (product, spam, a trend adjective); kept as an established trend loan, but a reviewer may prefer drop.
# question electrolyte: examples are mostly English product names; merged to electrólito by the English-spelling rule
# question freerider: could be an established sport loan; dropped because the examples lean toward a product name
# question mockups: the examples are mostly the Balsamiq Mockups product name, but the generic design loan "mockup" also occurs; merged into mockup
# question netlabel: the term is established among music-scene users, but I judged it too niche for a learner's list
# question obsesor: rare esoteric term, dropped as too rare for a learner list
# question obsesor: real derived noun but used almost only in spiritist texts; dropped as rare
# question onigiri: could count as an established food loan like sushi; dropped because many examples are a game title
# question skibus: ski + bus is a generic compound, but examples are mostly the La Molina service; dropped.
# question sobrecomprado: participial adjective of rare verb sobrecomprar; kept as trading jargon, could instead merge to sobrecomprar
# question sobrecomprado: participial adjective that is mainly finance jargon; kept as an adjective, could instead merge into sobrecomprar
# question subpanel: hybrid sub- compound with technical use; kept as an ordinary derived noun
# question supercargar: real prefixed verb, but a calque of English "supercharge" and unnatural; dropped.
# question trichomonas: Spanish "tricomonas" is the adapted form, but the examples are all Latin binomials, so dropped rather than merged.
# question trimethoprim: examples are English drug lists inside Spanish text; merged to trimetoprima by the English-spelling rule, but could be a drop if the real reading is judged a minority
# question uvs: UV (ultravioleta) abbreviation versus the Uvs place name; dropped because it is mixed and not a clean merge
# question idus: no sample examples; keep assumes the lowercase and Idus forms are mostly the Roman date rather than more idUS repository hits
# question limpiaza: no sample examples; if the capitalised forms turn out to be headings misspelling Limpieza rather than a company name, it should be merge:limpieza
```
