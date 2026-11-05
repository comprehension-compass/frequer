# es review shard 18: report (round 16, cascade)

Base `ee1d9e0`, whose `review/rules` match `full-es` 34c1e92. The runtime, lemma wheel and corpus sample were reused
from this session's shard 10 (setup script and extractor unchanged). Every review.py line passed `--rules` and
`--decisions keep,drop,merge`.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 348 |
| flagged with examples | 279 (80.2 %, **below the ~85 % mark**) |
| flagged: reviewers agreed / to adjudicator | 345 / 3 |
| flagged: queried at the gate | 1 |
| flagged final: agreed / adjudicated | 344 / 4 |
| **flagged final: keep / drop / merge** | **18 / 300 / 30** |
| unflagged screened | 414 (2 batches, 0 failed) |
| suspects (either screener / both) | 204 / 183 |
| suspects with examples | 169 (82.8 %, **below the ~85 % mark**) |
| unflagged: reviewers agreed / to adjudicator | 198 / 6 |
| unflagged: queried at the gate | 0 |
| unflagged final: agreed / adjudicated | 198 / 6 |
| **unflagged suspects final: keep / drop / merge** | **27 / 95 / 82** |
| unflagged not suspected (stay keep) | 210 |

Gate reading: every merge, keep and accent merge in both rounds (flagged 1, unflagged 4), every unflagged drop, and
every flagged drop whose reason mentions a fragment, plural, misspelling or real-word share; forms checked in the
queues for the doubtful ones (dentellar, tizo, tremolar, angu, guardavida, pescaito all held up).

## Queries and outcomes

Flagged (`s18-flagged/queries.tsv`):

| lemma | agreed | why queried | adjudicated |
|---|---|---|---|
| palmas | drop | the rules keep palma even when many uses are a name; palmas (clapping) is common | merge:palma |

Unflagged: no queries (`s18-unflagged/queries.tsv` is empty).

No splits requested beyond any `split by form` question lines below.

## Notes

* Both queues fell below the ~85 % example share (80.2 % flagged, 82.8 % suspects); carried on as the file says.
* Nothing failed: no failed screener batches or review calls, 0 undecided after adjudication.

## Question lines: flagged (36)

```
# question butoh: a niche Japanese dance term; kept as an established loan, but a learner may not need it
# question cassava: I decided keep as the common word (yuca), but the examples show only the company name Cassava Enterprises; if the real-word reading is under a third, this should be drop.
# question dgrn: a Spanish state directorate (Registros y Notariado), but it is a sub-ministry body and not a household name, so dropped
# question e-cigs: could merge into "cigarrillo electrónico", but the target is not an obvious lemma, so dropped
# question e-cigs: it could merge into "cigarrillo electrónico", but that is not a clear one-word lemma, so it was dropped.
# question efemérid: the written form is always efemérides, which is both singular and plural; merged to efeméride, but the plural-only entry efemérides may be preferred.
# question eufrasia: lowercase (plant) reading is 22 of 76, just under a third; kept as borderline
# question eufrasia: the plant reading is about 29% of the examples, borderline for the "about a third" threshold; kept because the reading is real
# question filia: some examples are the Filia Hotel; kept because the common noun filia/filias is the majority
# question flip-flops: electronics term and sandals both occur; merged to the singular loan flip-flop
# question flip-flops: the examples are electronics (biestable); the sandal sense is also possible. Merged into flip-flop.
# question iffhs: international body but a specialist one, not a household name; dropped
# question junkie: yonqui is the adapted spelling I assumed; confirm it is the list's form.
# question kilovatio-hora: a real unit term, but the hyphenated-compound rule says drop; the coordinator may prefer merge:kilovatio hora
# question kilovatio-hora: a real unit, but the rules drop hyphenated compounds; the coordinator may want a "kilovatio hora" unit instead.
# question l-dopa: merged into levodopa as a common generic drug; drop if the developer considers it specialist
# question mikve: Hebrew loan with Spanish plural; unclear whether it is established enough, kept because the examples use it as a common noun
# question morito: lemma mixes the proper name, the diminutive of moro and the bird (glossy ibis); kept because lowercase forms are over a third, but it is borderline.
# question morito: the bird name is a real word, but many examples are a hotel or a personal name; kept because the bird reading is at least a third of the examples
# question ohada: kept as a regional international body, though less famous than OEA or CEDEAO
# question ohada: regional African legal-harmonisation body, kept under the "regional and international bodies" ruling, though it is not widely known to learners.
# question palmas: all sampled examples are the place name Las Palmas; the common word palma (clapping) may be elsewhere in the counts
# question ready-to-wear: the established Spanish form is prêt-à-porter, but the English form is not a clear variant spelling, so dropped rather than merged
# question semar: SEMAR is mostly the Mexican navy ministry (kept as a national body), but Semar is also a Javanese character name in some examples.
# question semi-auto: merged to semiautomático on the assumption that the abbreviation stands for it; could also be semiautomática's masculine form being the target.
# question sorprendiéndono: sorprenderse is also common, but the example is non-reflexive, so merged into the plain verb
# question sorprendiéndono: sorprenderse is common, but the examples are plain transitive "surprising us", so I merged into sorprender
# question superfoods: "superfood" is an increasingly used loan, but these examples are brand-led, so dropped
# question taijiquan: established enough as a loan? Spanish also uses taichí; kept as the full name of the art.
# question taijiquan: it is capitalised 70% of the time, but the word names the martial art itself and is not a proper name, so I kept it.
# question tshirt: English spelling of an adapted word? Spanish writes camiseta, and t-shirt is only partly established; dropped as non-Spanish.
# question whigs: it is a plural form of a foreign party term. I merged it into whig on the basis that lowercase use is about half the examples, but dropping would also be defensible.
# question yagua: Yagua is also a real Spanish word (a palm tree, and an Amazonian people), but the examples seen are place names, so I dropped it.
# question yagua: real common word (yagua) vs ethnonym/place (Yagua Cocha); the real reading is borderline at about a third of the examples
# question yatch: it may be a misspelling of yate, but the sample shows hotel and place names, so it was dropped rather than merged.
# question yatch: mostly a hotel name; the lowercase reading would be yate (misspelling), a minority of examples
```

## Question lines: unflagged (26)

```
# question actividade: dropped as Galician/Portuguese; could alternatively merge:actividad if the text is judged a misspelling
# question atraidos: merged to the verb atraer, as with victimizado, but atraído could stand as an adjective lemma.
# question brusela: "bruselas" is also the common noun for Brussels sprouts (col de Bruselas); dropped as the place-name reading since the lemma "brusela" is a broken singular. Could instead be a merge to "col de Bruselas".
# question brusela: lemma is only from "col de Bruselas"; dropped as a place name, but a multi-word merge target (col de Bruselas) could be argued
# question busines: "business" is a possible established loan, but most examples are product or company names, so I dropped it
# question cañoner: cañonera is a noun (gunboat) with its own feminine entry; merged to cañonera rather than cañonero
# question dentellar: Dentelle/Dentelles (25 of 84) are French; I merged for the Spanish dentellada reading, but the coordinator may want the French forms excluded.
# question eclair: éclair the pastry is a real Spanish word, but the examples are all proper names; I judged the pastry reading under a third.
# question eclair: éclair the pastry is an established loan, but the examples are all names
# question honorem: second half of "ad honorem"; no first-half "ad" entry was shown to carry the merge, so dropped per split-loan rule
# question lansoprazole: lansoprazol is a fairly common generic but less of a household name than omeprazol; merged rather than dropped as specialist.
# question ligur: counts split between lowercase and capitalised; kept as ethnonym/adjective
# question pescaito: could be merged into pescadito as a variant spelling; kept as an established dialectal form
# question propo: could be a clipping of propósito or propuesta; no examples, dropped
# question sencillito: the rules don't say whether a regular diminutive merges into its base; kept because the lemma isn't broken (alternative merge:sencillo).
# question snowboarders: merge target snowboarder assumes the loan is established; the alternative is drop.
# question spreader: container-crane term seen only in industrial text; dropped as not established.
# question spreader: could be an established technical loan in port/crane context; dropped as specialist
# question stricto: examples not shown; assumed it occurs as "stricto sensu"
# question stricto: no examples shown; assumed to occur as "stricto sensu", so the first half merges into that compound.
# question transvasar: split by form: transvase, transvases -> transvase
# question tremolar: forms are mostly "tremolo" as a music or guitar term, and the target trémolo is my guess at the accented noun; confirm it is on the list
# question tremolar: lemma mixes the rare verb tremolar with the noun trémolo; decided for the noun reading, split by form: tremola, tremolando, tremolar -> tremolar
# question vermeil: specialist jewellery term; kept as established French loan, but a case for drop.
# question multitasking: is a loan that coexists with a recommended Spanish equivalent (multitarea) kept, or merged into the equivalent?
# question multivitamin: multivitamínico and multivitamina both exist as nouns; confirm which is the list's target
```
