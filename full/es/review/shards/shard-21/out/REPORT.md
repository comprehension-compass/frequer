# es review shard 21 (round 17): report

Branch `es-review-shard-21` from `ae73f55`; rules `review/rules/es-{flagged,unflagged}-final.md` (unchanged; same as
full-es eb2aea4). Runtime, lemma wheel and corpus sample reused from the shard 9 work directory; the setup script and
`review/scripts/examples10.py` are unchanged. Every `review.py` call passed `--rules` and `--decisions keep,drop,merge`.

The coordinator's diminutive call (regular diminutives merge into the base; lexicalised ones keep) is in
`full/es/junk-review.md` and the shard file, not in the rules files the reviewers and adjudicator read, so I applied it
at the gate. No agreed keep in either round was a regular diminutive (`bosquete` is lexicalised), so it needed no query.

## Counts

| step | lemmas | result |
|---|---:|---|
| flagged: examples | 260 | 192 with examples (**74 %, under the ~85 % bar**) |
| flagged: two reviewers | 260 | 254 agreed (drop 225, merge 22, keep 7), 6 disagreements; 1 accent-only merge |
| flagged: adjudication | 6 | 6 disagreements, no queries; 0 undecided |
| **flagged final** | **260** | **keep 8, drop 229, merge 23** (254 agreed, 6 adjudicated) |
| unflagged: screening | 311 | 2 batches, 0 failed; 196 suspects (143 by both screeners) |
| suspects: examples | 196 | 166 with examples (85 %) |
| suspects: two reviewers | 196 | 183 agreed (drop 77, merge 57, keep 49), 13 disagreements; 5 accent-only merges |
| suspects: adjudication | 15 | 13 disagreements + 2 queries; 0 undecided |
| **suspects final** | **196** | **keep 55, drop 82, merge 59** (181 agreed, 15 adjudicated) |

## Queries (the gate) and outcomes

I read every agreed merge and keep, every accent-only merge, and all agreed drops in both rounds.

Flagged: no queries. The merges are plain fixes; the drops with a real-word reading (sabot, serreta) are under a third.

Unflagged (merges between two standard academy spellings, as shard 9's trasposición):
- `trasmutar` (`merge:transmutar`): adjudicated `keep`.
- `ácimo` (`merge:ázimo`): adjudicated `keep`.

## Points for the coordinator

Questions the adjudicator raised:
- `postesar`: should specialist ordinary words (construction, engineering) drop like specialist acronyms and drugs?
  (adjudicated drop; earlier shards' adjudicators also dropped such words, e.g. coloproctología in shard 17)
- `pintacarita`: invariable -s compounds filed under a back-formed singular merge into the -s form (adjudicated
  `merge:pintacaritas`, as portacoche → portacoches in shard 13); confirm this holds for all such compounds.

Split requests (for the coordinator to write): `canana` (cananita -> cananeo; the lemma itself dropped), `miniar`
(minio -> minio), `verdear` (verdeo -> verdeo).

## What went wrong

- The flagged queue's example share is 74 %, below the ~85 % bar; carried on as the instructions say.
- Nothing else: no failed calls or batches in any step.

## Every `# question` line

### Flagged round (`s21-flagged/questions.txt`)

```
# question alfa-bloqueador: unclear whether alfabloqueador or alfabloqueante is the standard Spanish form
# question auto-sanación: I merged it into autosanación on the assumption that this is the standard spelling, but I'm not sure it is already a listed lemma.
# question auto-sanación: autosanación is not clearly an established word; merge assumes the solid spelling is the list form
# question autocares: plural of autocar filed as a lemma, but the examples are company names, so dropped rather than merged
# question comedor-salón: hyphenated compound dropped per rule; could alternatively be considered a real-estate unit.
# question fruncido: tagged PROPN with little evidence, kept as the ordinary participle/adjective
# question hinayana: Buddhist doctrinal term found in Spanish dictionaries; dropped as too specialist, but a keep would also be defensible.
# question hinayana: Buddhist term used in Spanish texts but specialist and mostly capitalised; dropped as specialist
# question hualapai: lowercase ethnonyms keep, but 85% of uses are capitalised names (and Hualapai Ranch), so I dropped it.
# question hualapai: rules keep lowercase ethnonyms, but this is a non-Spanish tribe name mostly capitalised and also a place; dropped
# question israelo-palestino: hyphenated compound of israelo + palestino; kept as an established single adjective, but could be dropped under the hyphenated-compound rule.
# question israelo-palestino: hyphenated compound of two gentilics; rule says hyphenated compounds of two listed words drop, but this is a single established adjective, so kept.
# question martiro: lemma is a name fragment (Martiros Saryan), not the real word mártir; there is no obvious merge target, so the merge target given is unclear and drop may be better.
# question meseni: Mecanismo Especial de Seguimiento para Nicaragua is an IACHR body; I dropped it as too minor, but the international-bodies rule could cover it.
# question meseni: could be kept as an international body (CIDH mechanism), but it is a temporary mission, so dropped
# question no-dualidad: could instead merge into a single-word form (nodualidad), but I dropped it as a hyphenated compound.
# question pre-grabadas: no rule on whether pregrabado is the form written without a hyphen; merged assuming standard spelling pregrabado
# question serreta: Spanish serreta (a toothed tool or horse noseband) is a real word, but the examples are mostly place names, so I dropped it. Check if a corpus sample shows a larger real-word share.
# question serreta: serreta is a real Spanish word (noseband, small saw, a type of key) but most examples are place names; dropped because the real reading looks under a third.
# question sugo: Italian loan with uncertain establishment in Spanish; kept as a sauce word
# question sugo: capitalised in 80% of the examples and the only example reads like a menu item, so the common-word reading may be under a third; kept as the Argentine/Uruguayan word for pasta sauce.
# question terminados: merged into terminado, but the capitalised heading uses may be a separate noun sense.
# question titano: mix of Monte Titano (place), titanio variant (aleación de titano) and mythological titan; kept as the common word, real reading may be below a third
# question twas: international academy of sciences, but not a household name like Unesco; dropped as an ordinary organisation.
# question txotx: Basque loan; kept because it is widely used in Spain for the cider season and ritual, though it is regional.
```

### Unflagged round (`s21-unflagged/questions.txt`)

```
# question adaptante: could be merged to adaptar/adaptador; no clear target, dropped
# question adaptante: not sure it is a dictionary word (adaptativo may be intended); kept as a real adjective since the examples read as genuine Spanish.
# question canana: real Spanish noun, but the counts are dominated by "Montana Canana" and the unrelated cananita; the real reading looks under a third, so I dropped it.
# question canana: split by form: cananita -> cananeo
# question coligar: lemma holds forms coligado/coligada as participles; kept as the verb
# question dentofacial: specialist but a real word; the rules don't cover specialist non-acronym terms, so I kept it.
# question despresurización: the lemma and the suggested target are identical, so no real merge is possible; should be keep.
# question díada: the lemma díada is itself a valid academy spelling (díada/diada both exist), so merging into diada is debatable; the rules say variant spellings merge into the standard one.
# question escolano: the common word (escolano, choirboy) is a small share of examples; dropped as mostly surname
# question evolucionarias: the base adjective evolucionario is rare, merged on the assumption it is obvious
# question fotocroma: rare specialist term; kept as a real word, drop if specialist terms are unwanted
# question isciii: Instituto de Salud Carlos III is a national public body, but I judged it not a household name; dropped.
# question jacarandá: both jacarandá and jacaranda are listed; kept as its own entry, so the coordinator should check whether jacaranda is a separate lemma
# question malditamente: not in dictionaries but a productive, attested adverb; kept.
# question miniar: split by form: minio -> minio
# question parlamentar: forms Parlamente/parlamentares suggest a mix of the verb, the adjective and a Portuguese or name fragment; the examples show only one case, so the share of the verb reading is unclear.
# question parlamentar: lemma mixes the verb parlamentar, the adjective parlamentar, and Parlamente (Portuguese or misparsed); kept for the Spanish verb/adjective reading
# question pintacarita: lemma is a plural-based form (pintacaras is usual); kept as a real word, unsure of the standard singular spelling
# question pintacarita: pintacaras is a real term but the lemma is mostly the plural and partly a proper name; dropped.
# question postesar: lemma is the verb but the forms are mostly the participle postesado; kept as a technical term, a split or merge into postesado is possible
# question postesar: postesado is a real civil engineering term (post-tensioned concrete), so it may merit keep if the rules treat it as established.
# question qualia: philosophical term that is plural-looking Latin used as singular; kept as an established loan
# question rengo: no examples; the Argentine/Chilean adjective reading versus the Rengo name (the Chilean town, the Japanese union) is unclear, so kept
# question sphagnum: the adapted form esfagno exists; dropped as a raw Latin taxon, but merge:esfagno is defensible
# question trasportó: trasportar is an accepted variant of transportar; merged because the form is a conjugation filed as lemma
# question trasportó: trasportar is an accepted variant, but I merged into transportar as the standard lemma.
# question verdear: split by form: verdeo -> verdeo
# question pintacarita: an invariable compound noun ending in -s (pintacaritas) was filed under a back-formed singular; is merging into the -s form the intended handling for all such compounds?
# question postesar: the rules settle specialist acronyms and drugs but not specialist ordinary words (construction or engineering terms); should these drop like specialist acronyms?
```
