# es review shard 14: report (round 15, cascade)

Base `b65e7ed`, whose `review/rules` already match `full-es` 75c5ee4 (the developer's second set of rulings). The
runtime, lemma wheel and corpus sample were reused from this session's shard 10 (same setup script, extractor and
wheel checksum). Every review.py line passed `--rules` and `--decisions keep,drop,merge`.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 558 |
| flagged with examples | 444 (79.6 %, **below the ~85 % mark**) |
| flagged: reviewers agreed / to adjudicator | 544 / 14 |
| flagged: queried at the gate | 2 |
| flagged final: agreed / adjudicated | 542 / 16 |
| **flagged final: keep / drop / merge** | **22 / 483 / 53** |
| unflagged screened | 610 (3 batches, 0 failed) |
| suspects (either screener / both) | 363 / 306 |
| suspects with examples | 297 (81.8 %, **below the ~85 % mark**) |
| unflagged: reviewers agreed / to adjudicator | 352 / 11 |
| unflagged: queried at the gate | 3 |
| unflagged final: agreed / adjudicated | 349 / 14 |
| **unflagged suspects final: keep / drop / merge** | **103 / 136 / 124** |
| unflagged not suspected (stay keep) | 247 |

Gate reading: every merge and keep in both rounds, both accent-merge files (flagged 2, unflagged 4), every
unflagged drop, and every flagged drop whose reason mentions a fragment, participle, plural, misspelling or
real-word share; forms checked in the queues for the doubtful ones.

## Queries and outcomes

Flagged (`s14-flagged/queries.tsv`):

| lemma | agreed | why queried | adjudicated |
|---|---|---|---|
| cerbero | keep | 77 of 91 forms are the capitalised myth/name | drop (common reading about 8 %) |
| pickl | drop | every form is pickles, a Latin American loan | merge:pickles |

Unflagged (`s14-unflagged/queries.tsv`):

| lemma | agreed | why queried | adjudicated |
|---|---|---|---|
| desplantar | merge:desplante | desplanta/desplantan/desplantar are the real verb | keep; noun forms split off |
| estrendo | merge:estrenar | "fue estrendo en cines" may be the noun estreno | merge:estreno |
| aplicadar | merge:aplicar | no examples; mostly capitalised Aplicada | merge:aplicar (confirmed) |

Split for the coordinator to write: **desplantar** (desplante/Desplante forms -> desplante). Plus any
`split by form` question lines below.

## Notes

* Both queues fell below the ~85 % example share (79.6 % flagged, 81.8 % suspects); carried on as the file says.
* Nothing failed: no failed screener batches or review calls, 0 undecided after adjudication.

## Question lines: flagged (69)

```
# question aiib: a regional/international body, but little known in the Spanish-speaking world; kept under the international-bodies rule.
# question aiib: international development bank, kept under the international-bodies rule, but it is less of a household name than the IMF.
# question anglo-estadounidense: a real Spanish compound adjective, but the rules say hyphenated compounds of two listed words drop; dropped on that basis.
# question aramid: could merge:aramida as an English spelling of an adapted word, but it is a specialist material term in product-listing text, so I dropped it.
# question aripo: kept as a regional body per the OEA/CEDEAO ruling, though less well known
# question aripo: same as kaiciid, an obscure regional body kept under the ruling
# question arna: no examples available; may be a real word (arna, moth) but evidence points to a name
# question arna: the real Spanish word (arna, moth/woodworm) may exist, but there are no examples and most uses look like names
# question asociándono: the verb could also be asociar, but asociarse fits the examples (asociándonos con) better.
# question baiano: Spanish gentilic is bahiano; I dropped as a Portuguese form, but merge:bahiano is arguable.
# question baiano: a Portuguese-origin demonym (from Bahía) that is only about half lowercase in the text
# question baud: baudio is a Spanish adapted form, but the text is mostly English "Baud Rate", so I dropped it rather than merging.
# question becquerel: Spanish unit lemma is becquerelio; lowercase unit uses are under a third of the examples, so dropped as a surname.
# question carm: Autonomous-community government of Murcia; the rules cover national, regional (supranational) and international bodies but not sub-national governments, so I dropped it.
# question cartón-yeso: it is a real Spanish term for drywall, but I followed the rule that hyphenated compounds of two listed words drop.
# question casbah: examples show it as a district name; merged to the adapted spelling casba
# question chilca: Andean plant (chilca) is a real Spanish word but is about a fifth of the examples against the place name; dropped under the one-third rule.
# question chilca: place use (Chilca, La Chilca) appears alongside the plant sense. I judged the plant to be about a third or more of the uses, since the lowercase and plural forms are frequent.
# question chor: the lemma mixes Chor (name) with chorlo and chores; split by form: chorlo, Chorlo -> chorlo
# question co-creativo: cocreativo is not a clear standard lemma, so I dropped it rather than merging.
# question co-creativo: cocreativo is not clearly a listed word, so this merge is a best guess; the alternative is drop
# question co-escrito: coescribir is rare; the participle coescrito might deserve its own entry instead.
# question conabio: Mexican national commission; unclear whether it counts as a household name
# question conabio: national body of Mexico; I judged it not a household name, so drop.
# question coya: real word (Inca queen, Collao people) is a minority of examples, dropped.
# question dari: language name, kept as lowercase Dari; 47% capitalised, so it could also be read as a name
# question dari: no examples were found; kept as the lowercase language name, but the majority of occurrences may be a surname or place name.
# question dracaena: genus name for a common houseplant; merged to the adapted spelling drácena, but the coordinator may prefer a drop if raw Latin taxon is read strictly.
# question dracaena: raw genus name vs adapted dracena; merged on the basis that the plant is commonly sold under this name.
# question enlatado: tagged PROPN only from sentence-initial/title use; kept as the real adjective/noun.
# question fomo: counted as an established loan; the rules don't say whether it counts as a technical acronym
# question fomo: slang acronym; unclear whether it counts as an ordinary word
# question goggl: goggles is an English loan used in Mexico, so it is uncertain it is established enough to keep; I merged into goggles on the assumption that it is.
# question goggl: goggles is an English loan used mainly in Mexico; if the team judges it not established enough, it should be dropped instead.
# question grog: real Spanish word, but examples are mostly names; dropped as under a third
# question grog: real word (grog) is about 28% of examples, just under a third; dropped
# question ideam: IDEAM is also Colombia's national meteorology institute (household name, would keep), but the examples show mostly a Spanish company, so I dropped it.
# question ideam: the name could be Colombia's national meteorological institute, but the examples show a Spanish company (IDEAM, S.A.), so I dropped it.
# question inai: INAI is a Mexican national body; whether it is a household name enough for the ETECSA-type ruling is a judgement call, so I kept it.
# question inai: a national Mexican body that is probably a household name; kept under the national-bodies ruling.
# question kaiciid: international body but not famous; kept under the regional/international bodies ruling
# question kaiciid: international dialogue centre, but not obviously a famous international body; dropped
# question mandorla: the art-history term mandorla may be a real word, but the evidence is mostly capitalised product use; dropped.
# question mixe: capitalised 42% so mostly lowercase ethnonym reading; kept per the lowercase-ethnonym ruling, but Mixe may also be a place/people name.
# question monokini: the academy may write monoquini; kept as the form people write, but a merge to monoquini is possible.
# question moonwalk: many examples are product listings (inflatables), but the dance reading is plausibly a third or more
# question méxico-americano: a real gentilic compound, but the rules say to drop hyphenated compounds; a single-word form such as "mexicoamericano" is not attested here.
# question oij: it could also be the Organización Iberoamericana de Juventud; kept as the Costa Rican body per the examples.
# question polder: lowercase and plural uses are only about a quarter of the examples, near the one-third line; merged to pólder as the real word.
# question polder: real Spanish word (pólder) but under a third of the examples are the common word; dropped.
# question ready-made: borderline art-term loan (Duchamp's "ready-made"); dropped as not established enough for a learner list.
# question ready-made: the Spanish form could be readymade or ready-made; I chose the unhyphenated form, but the item may be too niche to keep at all.
# question recién nacido: it is a multi-word lemma that reached the list only because of its capitalised headings; the rules do not say whether such units are kept.
# question reversi: game name, capitalised 88%; kept as an established name like ajedrez.
# question reversi: kept as a generic game name, but no examples were available to confirm the common-noun reading
# question rompetronco: only the capitalised plural Rompetroncos occurs, so it may be a name or product rather than a real word
# question semirrígido: assumed standard spelling is the unhyphenated semirrígido.
# question shekinah: Hebrew term used in Spanish religious texts, and the Spanish spelling (shejiná) is unclear; dropped
# question standup: mostly "Standup Paddle" (a sport name); the comedy loan "stand-up" may be worth its own entry
# question tbn: no examples; all-caps with 83 tokens suggests a network name rather than an abbreviation of "también"
# question user-agent: established in web terminology but only specialists use it; dropped as technical and hyphenated.
# question uvi: the one example is a university (Universidad Veracruzana Intercultural), but "uvi" is also the Spanish hospital unit (like UCI). Dropped on the evidence shown; the real-word share is not visible in the examples.
# question valkiria: standard Spanish spelling is valquiria; merge:valquiria may be preferred over keeping valkiria.
# question yin-yang: merge target "yin yang" vs "yin y yang"; unclear which form Spanish lists
# question zanu-pf: a national political party, not covered by the institution rules; dropped as an ordinary organisation.
# question zanu-pf: a ruling party is neither an institution nor an ordinary organisation under the rules; dropped as an ordinary organisation
# question chilca: "a real common word stays even if many occurrences are a name" seems to conflict with the one-third ruling for regional words like chilca. Does the one-third threshold override it?
# question chitosan: is quitosano a common ingredient (keep) or a specialist one (drop) under the drugs and ingredients ruling?
# question pickl: is pickles (Latin American loan, not in the DLE) established enough to keep as a merge target, or should it drop with the surname uses?
```

## Question lines: unflagged (62)

```
# question aera: could be read as a misspelt área, but the examples are mostly names or acronyms, so dropped
# question anaquita: no examples; it may be a diminutive of anaquel, but the evidence is too thin, so it is dropped
# question anaquita: no examples; possibly a diminutive of a regional word, dropped for lack of evidence
# question bodhisatva: the academy spells it bodisatva; kept the form people write
# question bogey: golf jargon (birdie, green, approach) may be too specialist; I kept it as an established loan in sports text.
# question bronzer: cosmetics loan, borderline established; kept
# question bronzer: kept as an established cosmetics loan, but it may be too niche
# question cabar: forms are cabaré (75) vs cabar (4); cabaré is a real word, so merge into cabaré, though cabar could be a rare real verb reading
# question capacitadora: feminine of capacitador; kept under the own-feminine-entry convention, unclear whether capacitador is itself on the list.
# question chemise: French loan used for lingerie and in a hat model name; unclear how established it is.
# question chiclet: could instead merge into chicle; kept because "teclado chiclet" is a fixed term
# question chiclet: mixed brand (Chiclets) and keyboard-style use; kept as a common noun, could be dropped as a brand
# question cocal: cocales is a real word, but about 22 of 89 occurrences, below the third needed, so I dropped it
# question copito: no example sentences in the sample, and Copito is also a name (about half of the counts); I kept it on the one-third rule, but this rests on the written-form counts alone.
# question copito: no example sentences were available, so the share of occurrences that are the name Copito (de Nieve) versus the common noun (copo diminutive, "copitos de algodón") is estimated from the written forms only.
# question desplantar: split by form: desplante, Desplante -> desplante (verb forms desplanta, desplantar, desplantan are a minority)
# question dializar: forms are mostly the participle dializado; kept the verb as the lemma since dializarse/dializan are verb forms
# question embolar: forms embolo/embole/embolada/Embolo mix émbolo, embole (LatAm "fuss") and a surname; merged to émbolo as the main reading
# question embolar: split by form: embolo, Embolo -> émbolo
# question flapper: borderline loan, used in cultural-history texts, often in quotes.
# question flapper: kept as established loan; borderline since many occurrences are in cultural/academic text
# question geminar: forms are mostly the participle adjective, so merged into geminado; if geminar is kept as a verb lemma, this should be keep
# question geminar: lemma is really the adjective geminado; merged there
# question geocache: borderline loan; dropped because it is niche, though "geocaching" is known in Spanish
# question gintonic: the academy writes gin-tonic; I kept the form people write, but merge:gin-tonic may be preferred
# question gintonic: the target spelling is unclear (gin-tonic, gin tonic or gintonic); I chose gin-tonic, and it should be changed to whichever form the list standardises on.
# question gorgotear: split by form: gorgoteo -> gorgoteo
# question hebronita: biblical clan gentilic; kept as lowercase ethnonym, borderline for a learner list.
# question hete: archaic "hete aquí" fragment; dropped as no clear lemma, could instead be filed under "he".
# question hete: could instead merge into "he" (hete aquí) if the coordinator wants archaic presentatives kept
# question hibakusha: Japanese loan used in Spanish news; kept as established but borderline.
# question hibakusha: kept as a loan; borderline as it is a specialist term used in Spanish peace-movement writing
# question internodal: a specialist botanical term but a real adjective with ordinary derivation; kept
# question levofloxacin: dropped as a specialist drug; if the developer treats it as a common generic antibiotic, merge to levofloxacino
# question lotu: mostly the brand Lotus, dropped; the "loto" reading is minor.
# question luneto: lemma mixes luneto (vault) and luneta (rear window, monstrance); kept for luneto's own reading, so luneta forms may need splitting.
# question luneto: split by form: luneta -> luneta
# question mesurable: RAE lists mensurable; mesurable may be a minority variant, but the examples are ordinary Spanish use, so I merged it.
# question mesurable: RAE may list mesurable with a different sense; merged because the examples all mean "measurable"
# question monstruito: same diminutive question as rubiecita
# question moodboard: established enough as a Spanish design/marketing loan? Kept as borderline.
# question motilla: it is a real Spanish word (mound), but the examples are mostly names, so I dropped it
# question mímese: the verb is probably mimar/mimarse but there is no example to confirm
# question porfiriato: historical period name, kept as a common noun used in lowercase and in Spanish history discourse
# question postest: Anglicism/Latin form, kept as established in education research
# question preocues: the target could be preocupar or preocuparse; I chose the pronominal verb because it is the common use.
# question proinversión: Peruvian state investment agency; dropped as not a household name, but it could count as a national body
# question redimensionado: noun use of a participle-shaped word; kept, could merge to redimensionar
# question requintar: forms are mixed (requinto, requinte, requintado); requinte is Portuguese, so I merged into requinto, the Spanish word for the instrument
# question requintar: forms mix Spanish requinto with Portuguese requinte/requintado; merged into requinto as the only clear Spanish word
# question rubiecita: diminutive of rubia, kept as lexicalised; the rules do not say whether to merge diminutives
# question rubiecita: no rule on diminutives; kept as its own word
# question seudo: it is a valid variant spelling of the prefix pseudo-; dropped as a prefix fragment, so merge:pseudo may be wanted
# question transmitiéndose: the sample shows passive/reflexive se, so I merged into plain transmitir rather than transmitirse.
# question tweeters: the singular tweeter may be established in audio contexts; dropped as a specialist term
# question umpire: Anglicism but standard in Latin American baseball reporting; kept.
# question zanjón: lowercase forms are only about 29% of examples and the sample example is a river name; kept as borderline.
# question aplicadar: should participle-adjective forms go to the verb (aplicar) or to an adjective entry aplicado, if one exists?
# question desplantar: split by form: desplante, Desplante -> desplante
# question embolar: split by form: embolo, Embolo -> émbolo (embole may partly be the Rioplatense noun embole "bore")
# question estrendo: only one example; the 90 tokens could also be misspellings of estruendo or estrenado. Is merge:estreno safe, or should an unverifiable misspelling drop?
# question luneto: split by form: luneta -> luneta
```
