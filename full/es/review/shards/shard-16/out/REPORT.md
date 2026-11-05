# es review shard 16: report

Branch `es-review-shard-16` (from `ee1d9e0`). Every `review.py` line ran with `--rules` and `--decisions keep,drop,merge`. The rules at `ee1d9e0` are identical to `origin/full-es` (`34c1e92`), and every stage used them. The runtime, wheel, review scripts and sample were reused from this session's shard 8 work directory through symlinks, and the setup script was rerun with `WORK=$HOME/es-review-16`.

## Counts
| step | count |
|---|---|
| flagged queue | 365 (examples 290 = **79 %**, below the ~85 % mark) |
| flagged reviewers | 350 agreed (drop 302, merge 34, keep 14), 15 disagreements, 0 accent-only merges |
| flagged after adjudication | 345 agreed + 20 adjudicated (15 disagreements + 5 queries), 0 undecided |
| flagged final | keep 15, drop 307, merge 43 |
| unflagged screened | 397 (2 batches, 0 failed); candidates 218 (both screeners 183) |
| suspects examples | 178 / 218 = **82 %**, below the ~85 % mark |
| unflagged reviewers | 204 agreed (drop 91, merge 74, keep 39), 14 disagreements, 6 accent-only merges |
| unflagged after adjudication | 199 agreed + 19 adjudicated (14 + 5 queries), 0 undecided |
| unflagged final | keep 44, drop 95, merge 79 (unscreened unflagged lemmas stay keep) |

Both example shares are under 85 %. I carried on as the instructions say.

## My queries (gate) and outcomes

### s16-flagged

| lemma | why queried | adjudicated |
|---|---|---|
| macá | agreed drop, but macá (maká) is a lowercase Paraguayan ethnonym, which the second-set rulings keep; check whether that reading is a third or more | drop: mostly the biblical place; the lowercase reading (ethnonym or bird) is 16%, below a third |
| nawa | agreed drop, but it may be the Nahua/nawa people noun (lowercase ethnonym, possibly merge:nahua); check the examples | drop: no examples; lowercase only 14%, so the nahua ethnonym reading is well below a third and the rest is names or the NAWA acronym |
| escoto | agreed drop, but escoto is a real Spanish gentilic (Scot, as in the ancient Scoti); check whether the common word is a third or more | drop: mostly a surname (Duns Escoto); the Scot gentilic reading (escotos, 18%) is below a third |
| anti-arañazo | agreed drop, but this round merges hyphenated prefix spellings (anti-héroe → antihéroe, multi-núcleo → multinúcleo); check consistency (merge:antiarañazos?) | merge:antiarañazos: hyphenated prefix spelling; consistent with multi-núcleo → multinúcleo; invariable form antiarañazos |
| multi-pantalla | agreed drop, but multi-núcleo in this round merged to multinúcleo; check consistency (merge:multipantalla?) | merge:multipantalla: hyphenated prefix spelling; consistent with multi-núcleo → multinúcleo |

### s16-unflagged

| lemma | why queried | adjudicated |
|---|---|---|
| cochinita | agreed merge:cochinita pibil as a split dish name, but cochinita is also a real diminutive noun (little pig, cochina); check whether the halves only occur together | merge:cochinita pibil: All the examples are the dish name; little sign of the standalone diminutive |
| cuartar | agreed drop, but cuartar (to quarter; to plough a fourth time) is a real Spanish verb; check whether that reading is a third or more | drop: Mostly the place name Cuarte; verb forms (cuarte, cuartada, cuartes, cuartar) are at most about 29%, below a third |
| gladio | agreed drop, but gladio (short sword; gladiolus) is a real Spanish noun; check whether the common word is a third or more | drop: Mostly the game character or name Gladio; lowercase gladio is 3 of 79 |
| blocar | agreed drop, but blocar (to block, in sport) is a real Spanish verb; check the examples | drop: Mostly Portuguese bloco; clear verb forms (blocar, bloca) are about 19 to 31%, and the examples are all bloco |
| taaaan | agreed drop, but it is an elongated "tan" with an obvious target; laughter variants were merged in earlier rounds (jajaj → jaja); check merge:tan | merge:tan: Elongated spelling with an obvious target, as with jajaj → jaja |

How I picked them: I read every merge, every keep, every drop lemma and the accent-merges files. I queried agreed decisions that might hide a second real word or a lowercase ethnonym, and drops that didn't match a merge in the same round or in earlier rounds. All the accent-only merges looked right. The queries changed anti-arañazo → antiarañazos, multi-pantalla → multipantalla and taaaan → tan. The real-word checks all stayed as decided.

## What went wrong
* Nothing failed. Every stage finished on its first run.
* The example shares are below 85 % (see above).
* For the coordinator: `cochinita → cochinita pibil` and `taaaan → tan` are judgement calls (a split dish name and a noisy word). The ex- prefix disagreement `ex-jefe` was adjudicated with the others; see decisions.tsv.

## Every `# question` line

### s16-flagged

```
# question allopurinol: alopurinol is a common generic drug, so merged into the Spanish spelling
# question allopurinol: merged to alopurinol as a common generic drug; drop instead if the developer treats it as specialist
# question animándono: rule says -nos clitic fragments merge into pronominal verb if common in own right; animarse is common, so merge:animarse may be preferable
# question animándono: the rule points to the pronominal animarse where common, but the example reads as plain animar, so merged there
# question asiático-americano: the rules say hyphenated compounds of two listed words drop, but this is a gentilic that people write as one unit; I merged it into the unspaced "asiático americano", so please confirm that is the intended target or whether it should be dropped.
# question csce: historical name of the OSCE; kept as an international body, but the coordinator may prefer merging it into OSCE if that is listed.
# question escoto: lemma mixes surname Escoto with plural escotos (escote); split by form: escotos -> escote
# question ex-jefe: merged to exjefe as the Spanish spelling; if hyphenated ex- compounds count as "two listed words", it would drop instead
# question gamut: capitalised 48% and tagged PROPN; kept as established colour/music term, but may be mostly technical use
# question gamut: could count as an established loan in colour and music contexts; dropped as technical
# question gremlin: lowercase use is about 31% of examples, borderline for the one-third rule; dropped because the sample shows mainly product and game names
# question higiénico-sanitarias: target higiénico-sanitario is a hyphenated compound which the rules would otherwise drop; merge chosen as the plural is a broken lemma
# question inspirándono: the example uses plain "inspirar" (inspiring us), though inspirarse is also a common verb; I chose the plain verb.
# question instragram: misspelling of the brand Instagram; dropped because the brand itself would drop.
# question irgc: Iranian national body, not Spanish-speaking, but frequent in Spanish news; dropped as a foreign institution.
# question jarilla: lowercase use is about 31%, borderline; kept as a real plant word although some capitalised uses are names
# question longboards: unsure longboard is established enough in Spanish; merged into the singular rather than dropped
# question macá: real Spanish bird name but examples show the biblical place; dropped as a minority reading
# question macá: real bird-name reading (macá, a grebe) seems a minority versus the biblical place Macá; dropped on that basis
# question mandeno: could also be a Mandé ethnonym (mandeno/mandenos) but examples show the imperative
# question mncars: Museo Reina Sofía is a famous national museum, but it is a place-like single institution; dropped as not a body people name like RENFE
# question mncars: a single national museum (Reina Sofía) could count as a famous institution; dropped by analogy with single hospitals
# question multi-pantalla: could merge to "multipantalla" if that form is on the list; I dropped it as a hyphenated compound.
# question nereido: nereida is the base, mythological plural; confirm the merge target should be nereida rather than a separate nereido entry
# question pro-capitalista: merged to procapitalista as an obvious spelling fix, though the rule on hyphenated compounds could also drop it
# question rajput: capitalised in 73% of uses, but the ethnonym rule says lowercase ethnonyms keep; kept on that basis
# question rajput: no examples seen; kept as ethnonym, could be a proper-noun caste name
# question restaurativa: the examples show only an institute name, but "restaurativa" (as in justicia restaurativa) is a real adjective; merged to restaurativo would be an alternative if more common-word examples exist
# question safar: the verb safarse (safarse, safaron, safarme) is real, but under a third of examples, so dropped
# question santoku: no brand-only evidence beyond one example; kept as established loan for the knife type
# question satana: merge target Satanás is a proper name, but the list may treat it as a common word, so check the capitalisation
# question semi-privada: target "semiprivado" assumed as the standard unhyphenated spelling; confirm it is on the list
# question senad: Paraguay's anti-drug secretariat, but half the examples are a personal name; dropped.
# question senad: could be Paraguay's national anti-drug body, but the examples are mostly the first name; dropped
# question serrapeptase: could be dropped as a specialist drug, but kept as a merge into the adapted spelling
# question serrapeptase: could be kept as a generic supplement ingredient (serrapeptasa), but judged specialist.
# question sharpie: brand used as a common noun, no adapted spelling known; merge to itself is meaningless, should be keep or drop
# question sinac: national body of Costa Rica; unclear whether it is a household name beyond Costa Rica, kept as a national conservation body.
# question spei: Mexico's payment system run by Banxico; kept as a national body that is a household name, but it could be read as a product
# question tvg: Televisión de Galicia is a regional broadcaster, but most examples are a file extension or betting site, so dropped.
# question tvg: the examples mix a file extension, a betting company and Televisión de Galicia (a regional broadcaster that would keep); dropped because the broadcaster reading looks like a minority
# question unag: kept as a national body of Nicaragua; unclear whether it is a household name.
# question upb: could be Universidad Pontificia Bolivariana, a known university but regional, dropped
# question vud: Spanish "vehículo utilitario deportivo" (SUV) is used in rental sites, but it is a niche acronym; I treated it as a technical acronym and dropped it.
# question vud: Spanish for SUV but mostly a rental-category label; dropped as a specialist acronym
# question web-site: merge target could instead be "sitio web" if "website" is not on the list
# question ío: Spanish name of Jupiter's moon, a real Spanish form; dropped as a proper noun that is not a place a learner needs, but it could be kept
# question ío: Spanish spelling of Jupiter's moon Io; dropped as a place-like proper name, but it may merit a keep as astronomy vocabulary.
# question pre-seleccionados: when a participle is used adjectivally or nominally (preseleccionados), should it merge to the verb (preseleccionar) or to the masculine singular participle (preseleccionado)?
# question spei: national systems or services (not bodies) that are household names, such as SPEI or similar payment rails: keep like ETECSA, or drop as non-institution names?
```

### s16-unflagged

```
# question antipasti: Italian food term used on Spanish menus; dropped as not established, but could be a keep as a loan
# question antipasti: an Italian plural that may merge into antipasto if the coordinator prefers
# question bielástico: real but rare technical-commercial adjective; kept as a Spanish word
# question cheka: historical Soviet institution, not a place; dropped as a foreign name, though Spanish also writes it "checa".
# question cochinita: the lemma may also be a plain diminutive of cochina, but nearly all examples are the dish cochinita pibil; the coordinator should check that the target "cochinita pibil" exists and that "pibil" is dropped.
# question correfoc: Catalan tradition widely named in Spanish texts in Catalonia; dropped as non-established, but could be a keep if the developer treats it as a cultural loan
# question curvador: same case as trillador; the examples are mostly curvadora (machine)
# question depositación: a real coating-technology term, or a mistaken form of deposición?
# question deslizadero: split by form: deslizadera, deslizaderas -> deslizadera
# question focu: unclear whether the target is "focus group" (a loan) or foco; the examples show "focus groups", so I chose the compound
# question frezar: the lemma mixes freza/frezar (real, spawning) with misspelt fresado and unrelated frece/frecen; kept for the real reading
# question horonita: lowercase demonym of Beth-horon, which could count as an ethnonym; dropped as a minor biblical gentilic
# question iboga: kept out as a specialist plant/drug, but it could count as an adapted organism name.
# question improviso: forms are mostly verb improvisa (improvisar) with only 4 occurrences of noun improviso; split by form: improvisa, Improvisa, improvisas -> improvisar
# question improviso: split by form: improvisa, improvisas -> improvisar (49+11 of 77 are verb forms; noun improviso only ~4 examples, below a third, so arguably drop or merge:improvisar)
# question midiéndose: medirse (try on) may be the better target than plain medir
# question midiéndose: the first example is medirse (try on) and the second is passive; filed under plain medir
# question níque: could be a cut-off níquel or a misspelling, with no examples to check; merged into níquel as the obvious candidate
# question placeholder: English IT term that may be established enough in Spanish tech writing; dropped as not clearly established
# question pleuritis: could instead be considered a specialist medical term; kept as common enough in Spanish
# question sertraline: a well-known generic antidepressant, treated as a common drug and merged to the Spanish spelling sertralina
# question solícitamente: Kept as a valid adverb, but it may fall under the rule for adverbs in -mente that merge to the adjective
# question substantivar: the forms are mostly "substantivo" (old spelling), so I merged to sustantivo rather than the verb sustantivar.
# question taconear: split by form: taconeo -> taconeo
# question tarjetita: plain diminutive; kept as its own lemma, but could merge into tarjeta if diminutives are to be folded
# question tarjetita: the rules do not say whether regular diminutives merge into the base noun or keep their own entry. I decided by analogy with the -ísimo ruling, and lexicalised diminutives (e.g. ventanilla) would be a separate matter.
# question tipsters: borderline loan; dropped as too niche, but could be merge:tipster if the list carries that entry
# question tipsters: tipster is an English betting term with doubtful establishment in Spanish; merged to singular tipster, but the coordinator may prefer drop.
# question todomisericordioso: Spanish compound used only as a divine epithet in Islamic texts; dropped as odd
# question trillador: lemma is the masculine form but the examples are mostly the feminine trilladora (machine); consider merge:trilladora
# question vapo: no examples; could be slang for vaporizador, dropped as unclear
# question cochinita: in Mexico "cochinita" alone also names the dish (tacos de cochinita); confirm that the split-loan merge still applies when the first half also occurs alone
# question deslizadero: split by form: deslizadera, deslizaderas, Deslizadera -> deslizadera (technical slider, mostly the slider in garment and machinery examples)
# question frezar: split by form: freza -> freza (spawning noun, about 43% of the examples); frezado is a misspelling of fresado
# question tarjetita: should regular diminutives (-ito/-ita) merge into their base like regular -ísimo superlatives, or keep their own entry?
# question trillador: split by form: trilladora, Trilladora, trilladoras, Trilladoras -> trilladora (machine noun with its own dictionary entry)
```
