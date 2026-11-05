# es review shard 12: report

Branch `es-review-shard-12` (from `b65e7ed`). Every `review.py` line ran with `--rules` and `--decisions keep,drop,merge`. The rules at `b65e7ed` are identical to `origin/full-es` (`75c5ee4`, with the second-set rulings), and every stage used them.

The runtime, lemma wheel, uplift review scripts and corpus sample were reused from this session's shard 8 work directory through symlinks, and the setup script was rerun with `WORK=$HOME/es-review-12`. It verified the wheel's sha256, skipped the existing sample and wrote this shard's config and routed queue.

## Counts
| step | count |
|---|---|
| flagged queue | 526 (examples 432 = **82 %**, below the ~85 % mark) |
| flagged reviewers | 513 agreed (drop 448, merge 41, keep 24), 13 disagreements, 0 accent-only merges |
| flagged after adjudication | 505 agreed + 21 adjudicated (13 disagreements + 8 queries), 0 undecided |
| flagged final | keep 25, drop 454, merge 47 |
| unflagged screened | 642 (3 batches, 0 failed); candidates 314 (both screeners 269) |
| suspects examples | 261 / 314 = **83 %**, below the ~85 % mark |
| unflagged reviewers | 294 agreed (drop 156, merge 91, keep 47), 20 disagreements, 7 accent-only merges |
| unflagged after adjudication | 291 agreed + 23 adjudicated (20 + 3 queries), 0 undecided |
| unflagged final | keep 52, drop 167, merge 95 (unscreened unflagged lemmas stay keep) |

Both example shares are a little under 85 %. I carried on as the instructions say. Lemmas without an example were decided from frequency, forms and flags.

## My queries (gate) and outcomes

### s12-flagged

| lemma | why queried | adjudicated |
|---|---|---|
| rejón | agreed drop, but rejón is a real Spanish word (bullfighting lance; rejoneo); check whether the common word is a third or more of the examples | drop: surname and place dominate; the bullfighting word is about 16%, under a third |
| pingo | agreed drop, but pingo is a real Spanish word (rag; horse in the Southern Cone; colloquial uses); check the examples | drop: mostly a name; lowercase forms are about 19% and there are no examples showing the common reading |
| coqui | agreed drop, but it may be coquí (the Puerto Rican frog) without the accent, which would be merge:coquí; check the examples | drop: mostly a name or brand; the lowercase coquí reading is about 12%, with no examples |
| pochote | agreed drop, but pochote is a real Central American Spanish tree name; check whether the common word is a third or more | drop: mostly place and street names; the tree reading is about 14%, under a third |
| féliz | agreed drop, but it looks like a misspelt feliz (stray accent), which the rules merge; check the examples | drop: mostly a Dominican surname; the misspelt feliz is about 15%, under a third |
| ex-testigo | agreed drop, but ex-ministro in this round merged to exministro; check consistency (merge:extestigo?) | merge:extestigo: ex- prefix spelling Spanish writes solid, consistent with ex-ministro → exministro |
| fuegofuego | agreed drop, but the doubled-word artefacts enemigosenemigo and desiertodesierto in this round merged to their word; check consistency (merge:fuego?) | merge:fuego: doubled-word artefact with an obvious target, consistent with enemigosenemigo and desiertodesierto |
| palabrapalabra | agreed drop, but the doubled-word artefacts enemigosenemigo and desiertodesierto in this round merged to their word; check consistency (merge:palabra?) | merge:palabra: doubled-word artefact with an obvious target, consistent with enemigosenemigo and desiertodesierto |

### s12-unflagged

| lemma | why queried | adjudicated |
|---|---|---|
| sirgar | agreed merge:sirga, but sirgar (to tow a boat) is a real verb; check whether verb forms are a real share | merge:sirga: forms are the noun sirga/sirgas; at most 1 of 98 (sirgo) could be the verb, not a real share |
| incomodo | agreed merge:incómodo, but incomodo is also a real verb form (yo incomodo, from incomodar); check which reading the examples show | merge:incómodo: examples are the adjective incómodos without the accent; only 2 of 86 could be the verb |
| canalete | agreed drop, but canalete (paddle; small channel) is a real Spanish noun; check whether the common word is a third or more | drop: about 10 of 85 are the common word; the rest are the places Canalete and Canaletes, well below a third |

How I picked them: I read every merge, every keep, every drop lemma and the accent-merges files. I queried agreed decisions that might hide a second real word, and agreed drops that didn't match a merge in the same round (ex- prefixes; doubled-word artefacts). All the accent-only merges looked right. Only the consistency queries changed decisions: ex-testigo → extestigo, fuegofuego → fuego, palabrapalabra → palabra.

## What went wrong
* Nothing failed. Every stage finished on its first run with no failed calls.
* The example shares are below 85 % (see above).
* For the coordinator: `jajaj → jaja` (unflagged) matches shard 8's `jajajajaja → jaja`. It only works if jaja is on the list.

## Every `# question` line

### s12-flagged

```
# question afro-descendiente: merge target spelled afrodescendiente, which is the form I expect people to write; confirm the list's spelling
# question ayto: examples show Aytos as the Bulgarian city (place name) for a large share; merged for the abbreviation reading
# question babesia: genus name used in Spanish (babesiosis); dropped as a raw taxon, but it could count as an adapted organism name
# question babesia: kept as adapted organism name but capitalised 67% of the time, which may mean Latin genus use
# question boho-chic: hyphenated loan not made of two listed Spanish words; kept as an established fashion loan, may need a call on its spelling (boho chic)
# question boho-chic: hyphenated loan of two foreign words; kept as one established loan, not a compound of listed words
# question brujita: diminutive of bruja; kept because it is a real common word, though the lemmatiser might prefer bruja
# question buitrero: buitrera is a real word (vulture nesting site) but the examples are the place name Pico La Buitrera; dropped on the minority-reading rule.
# question bussiness: misspelling of business; merged assuming business is on the list as an established loan.
# question caravela: merged into carabela, but some examples are a hotel or place name
# question cbu: a household banking term in Argentina, but the examples show only cement/company uses, so I dropped it.
# question conidio: lemma holds conidios and conidias; the feminine form is a variant, split by form: conidias -> conidia
# question conidio: real word but specialist mycology vocabulary; kept because the lemma is correct, and conidias is the feminine form of conidia
# question cou: COU is a defunct Spanish schooling stage, still known to Spanish speakers; kept as an ordinary Spanish acronym, but could be judged specialist
# question cou: historical Spanish school term (COU), not a current course; kept as an established acronym, but the example is thin.
# question dhikr: borderline Arabic religious term; dropped as not established in general Spanish
# question dinka: capitalised in 64% of text and one example is a game-mod name; kept as an ethnonym under the lowercase-ethnonym ruling
# question dragster: established loan, though the tag is PROPN and many examples are product names
# question ex-ministro: target exministro assumed; unsure whether list writes it as ex-ministro, exministro or ex ministro
# question ex-ministro: the target exministro is the standard unhyphenated form, but "ex ministro" is also written.
# question fixing: financial "fixing" is a loan in Spanish, but most examples are the magazine or product name, so dropped
# question fundidora: common noun "fundidora" (foundry) is possibly near a third of the examples; the capitalised uses are the Monterrey park/foundry name
# question geis: GEI (gases de efecto invernadero) plural filed as geis; dropped as specialist acronym, could merge:GEI if the list keeps it
# question geis: mixes the acronym GEI (gases de efecto invernadero) with the company GEIS; dropped because the evidence is mixed and the acronym is specialist
# question helicoide: real geometric word, but the examples mostly refer to the Caracas building; the share of the common reading is unclear
# question helicoide: the real-word reading (helicoide, helicoides) is only about a third of the examples; the rest are the Caracas building El Helicoide. Kept as borderline.
# question incorporada: could instead be dropped as mostly part of a proper phrase (Zona No Incorporada); merged to participle adjective
# question incorporada: could instead merge into the verb incorporar; chose the adjective incorporado because the examples use it as an adjective.
# question lambrusco: a wine type rather than a brand, so kept; check whether the list wants wine names
# question log-in: target spelling assumed to be "login" (could also be "log in" or "inicio de sesión"), please confirm
# question log-in: unsure whether "login" is on the list under that spelling; merged on the assumption that it is (or should be) the standard form.
# question minc: MINC is the Ministry of Culture in several countries (here the Dominican Republic); kept as a ministry acronym, but it could also be read as a minor abbreviation.
# question minc: acronym used by several countries' culture ministries (Dominican Republic and others); kept as a national ministry, but no single country is clear
# question montelukast: a common asthma drug but a specific prescription one, so I treated it as specialist and dropped it; the generic-drug ruling could arguably cover it
# question nawal: spelling variant of nahual; unclear whether to merge into nahual, kept for now as the Maya spelling
# question nawal: variant spelling of nahual, but most examples are the personal name; dropped under the one-third rule
# question no-residente: "no residente" is a real unit, but the hyphenated-compound rule says drop
# question odor: the example is English ("Nuisance Odor") and 72 of 91 hits are capitalised, so the Spanish reading may be under a third; kept because it is a common Spanish word.
# question odor: the only example is English ("Nuisance Odor"), but odor is a real Spanish word; dropped because lowercase Spanish use is only about 16% of occurrences.
# question pepo: pepo is a real Spanish word (a gourd-type fruit), but the examples are a name and the taxon C. pepo; dropped on the one-third rule
# question pingo: pingo is a real Spanish word (Rioplatense horse, rascal) but the examples are mostly capitalised names; dropped because the real reading is under a third
# question pingo: real word (Latin American slang) vs name is close to the one-third threshold; I counted lowercase as about 19% and dropped it.
# question puffs: merged into puf, assuming the list writes it "puf"; the Super Puffs brand uses are a minority
# question puffs: only about a third of the examples are the common-noun reading, so it sits near the cutoff; merged into puf.
# question rah: mixed reading, mostly the place Reethi Rah, with RAH (Real Academia de la Historia) a minority, so dropped
# question rah: split between Real Academia de la Historia (RAH) and Reethi Rah resort; dropped because neither reading is clearly dominant
# question recuérdel: recuérdeles is imperative + clitic of recordar; merged to plain verb since recordar is not pronominal here
# question shilling: examples are the English "Uganda Shilling", so chelín is the Spanish form but the reading may be mostly English
# question siriano: examples refer to aliens from Sirius rather than Syrians; kept as a lowercase ethnonym
# question siriano: the examples refer to inhabitants of Sirius, not Syrians; dropped, but a gentilic merge to sirio could be argued.
# question tabl: forms are mostly English "tables" plus a cut-off "tabl"; dropped, though merge:tabla is possible
# question troje: Spanish troj/troje is real but most examples are place or hotel names; kept on the third-of-examples rule from the sample
# question uabc: a state university in Baja California; dropped as not nationally famous like UNAM
# question uabc: regional state university rather than a national one; kept as a household name in Mexico
# question ucn: two readings (Unión del Centro Nacional, a Chilean party, and Universidad Católica del Norte); treated as an ordinary organisation and dropped.
# question unitaid: international body, kept under the international-bodies rule, though less famous than ONU or OMS
# question utn: it names several Latin American universities (Argentina, Ecuador), but the examples show the Argentine one, so I kept it as a national institution
# question veronés: the lowercase gentilic reading is about 38% of the examples, the rest being the painter Veronés; I kept it on the one-third rule, but it is borderline.
# question ayto: when the sample examples show only a homonymous place (Aytos) but the written-form counts point to an abbreviation, should the written forms decide?
# question post-rock: should music-genre loans with a Fundéu-adapted form (posrock) merge into that form, or drop as niche when they are uncommon?
```

### s12-unflagged

```
# question apersonar: apersona/apersonas (23 of 92) look like typos of "a persona", but the real forms (apersonó, apersonaron, apersonarse) are the clear majority, so kept.
# question apersonar: some counted forms such as "apersonas" and "un apersona" are typos for "a persona", so the real verb forms are the majority but not all of the counts.
# question asgardiana: fictional gentilic; merged to asgardiano but drop is possible if the fictional term is judged not learner-relevant
# question bisacodyl: may be a specialist drug (drop) rather than common generic
# question bolear: split by form: boleo, Boleo -> boleo
# question bugfix: established enough as a loan? Kept because Spanish dev text uses it as-is.
# question bugfix: kept as an established software loan, but it is borderline (tagged PROPN, tech jargon)
# question camar: forms are mixed (camaron, Camares, Camará); camaron may be a misspelling of camarón but the capitalised ones are probably the singer's surname, so I dropped it
# question electroshock: RAE prefers electrochoque, but the English-style spelling is what people write; kept rather than merged
# question electroshock: Spanish also writes electrochoque; kept as the form people write, so confirm whether to merge:electrochoque
# question escalación: Latin American calque of escalada/escalamiento, unclear whether to merge
# question escalación: calque of English escalation, keep rests on real use in sports (alineación) which is not shown in the examples
# question fluídico: the academy may prefer fluídico/fluidico variants; kept as written
# question fungoide: a real DLE adjective but appears almost only in a medical term; kept as a real word
# question fungoide: real adjective, but only in the specialist term "micosis fungoide"; I dropped it as too narrow.
# question herid: "Herid" (50) may be a heading or name rather than the imperative; merged to herir on the strength of heridles/heridlos.
# question hongkonés: demonym derived from a place name; rules don't mention demonyms of places, so kept as an ordinary word
# question horita: diminutive filed as its own lemma; kept, but merge:hora is possible if diminutives should fold into the base
# question horita: diminutive of hora, mostly plural horitas; kept, could be merged into hora if diminutives should merge
# question hyperlinks: Spanish has hipervínculo and hiperenlace, so no single obvious merge target; dropped as English
# question hyperlinks: could also be dropped as an untranslated English token; merged into hipervínculo as the obvious Spanish word
# question jajaj: laughter variant; merged into jaja assuming jaja is kept as an interjection
# question jajaj: merge:jaja assumes jaja is on the list as a lemma; otherwise drop
# question kadete: all examples are the Russian Kadets party, so I dropped it rather than merging into cadete.
# question kadete: real word meaning Russian Kadet party member, which cadete does not cover, so merge was not used; drop is a judgement on its low learner value
# question leit: split by form: leit -> leitmotiv; no examples shown, assumed to come from "leit motiv" split
# question mandaloriana: Star Wars name-derived; merged to mandaloriano, but the masculine may itself be a drop.
# question mensajito: a regular diminutive. Kept as an everyday word, though merge:mensaje is arguable.
# question moldeadora: keep as own entry since máquina moldeadora is a noun use, but adjective use is only part of examples; coordinator may prefer merge:moldeador
# question papayo: split by form: papaya, papayas -> papaya
# question persignar: all forms are mostly pronominal (se persigna), so merge:persignarse could also be argued; kept the plain verb as the lemma
# question persignar: persignarse may be the better lemma, since most forms are reflexive. Kept persignar as a real verb in its own right.
# question pibil: occurs mostly in "cochinita/puerco pibil"; kept as a single word, could instead be merged into "cochinita pibil"
# question porcini: Italian mushroom name used in Spanish gastronomy; dropped as not established, could be keep
# question povera: only occurs in "arte povera", but "arte" is not a split-loan half in the usual sense; dropped rather than merged into "arte povera"
# question preterrenal: kept as a real word, though its usage is almost all LDS religious text
# question proficiente: examples look like an anglicism (proficient); kept because the RAE lists it
# question quetiapine: may be a specialist drug (drop) rather than common generic
# question raspadito: kept as a lottery-specific term; merging into raspado is the alternative if the sense is thought too narrow.
# question sarong: examples are trade-catalogue spam; kept as an established loan.
# question stablecoins: assumed stablecoin is established enough in Spanish crypto text to be a loan worth keeping
# question sulfametoxazol: common antibiotic ingredient (as in cotrimoxazol), but judged specialist; unclear whether it counts as a common generic drug
# question tampo: tampo is a rare real Spanish word, but the examples are all hobby usage (model-car decals), so I dropped it
# question truenosnoche: web artefact fused from "truenos" + "Noche"; dropped rather than merged to trueno
# question hyperlinks, hiperlinks: should English or hybrid spellings merge into a Spanish calque (hipervínculo) when there is no adapted spelling?
# question mandaloriana, asgardiana: should gentilics of fictional places drop like names, or merge into a masculine form (mandaloriano, asgardiano)?
# question papayo: split by form: papaya, papayas -> papaya
# question quetiapine, bisacodyl, epinephrine: where is the line between common and specialist drugs? (Prescription-only but widely used, like quetiapina, versus OTC ingredients, like bisacodilo.)
```
