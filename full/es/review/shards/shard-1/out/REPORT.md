# es review shard 1: report

Branch `es-review-shard-1` (from `c4aacac`). Rules: stage 1 and adjudication both with
`review/rules/es-flagged-final.md` (flagged) and `review/rules/es-unflagged-final.md` (unflagged).

## Counts

| step | count |
|---|---|
| flagged queue (action `pending`) | 938 |
| flagged with an example | 816 (87.0 %) |
| unflagged screened (2 screeners, 20 batches, none failed) | 4,981 |
| suspects (union) | 777 (604 by both screeners) |
| suspects with an example | 693 (89.2 %) |

| round | reviewers agreed | disagreements | coordinator queries | final agreed / adjudicated | keep | drop | merge |
|---|---|---|---|---|---|---|---|
| s1-flagged | 915 | 23 | 7 | 908 / 30 | 74 | 803 | 61 |
| s1-unflagged | 730 | 47 | 29 | 701 / 76 | 350 | 242 | 185 |

No undecided lemmas in either round. Reviewer agreed split before adjudication: flagged keep 68 / drop 794 /
merge 53 (3 accent-only merges); unflagged keep 327 / drop 223 / merge 180 (8 accent-only merges).

## What went wrong: adjudication fell back to the old rules

The `--adjudicate` commands in `shard-1.md` don't pass `--rules`, so `review.py` falls back to config `rules`:
uplift's `prompts/es/rules-flagged.md`, the old rules (places → `pending-names`, no institutions rule, no
lemmatiser-conventions section). The first flagged adjudication ran that way; the adjudicator noticed ("the
coordinator cites an institutions ruling that is not in the binding rules I have"). I moved that adjudication
aside (kept locally, not committed), restored the stage-1 `questions.txt` and reran with
`--rules review/rules/es-flagged-final.md`. Six of the 30 decisions changed: asegurémono → merge:asegurarse,
dirigiéndono → merge:dirigirse (pronominal convention), etecsa drop → keep (institution), padrespadr drop →
merge:padre, papo drop → keep, chlamydia merge:clamidia → drop. The unflagged adjudication ran with
`--rules review/rules/es-unflagged-final.md` from the start. The coordinator was told, since every shard is affected.

A related point: `review.py`'s default `--decisions` still offers `pending-names` in the answer format,
though the final rules don't define it. The flagged adjudicator asked about it and didn't use it. Neither
round has a `pending-names` decision.

## Queries (gate)

I read every agreed merge, every agreed keep, every agreed drop (the full lists, not a sample) and the
accent-merge lists. I queried agreed decisions that may hide a second real word: a real verb or adjective merged
into a related noun, a wrong merge target, an accent merge of a verb form, or a real word dropped.

### s1-flagged

| lemma | agreed | after adjudication | why queried |
|---|---|---|---|
| hotelera | merge:hotelero | merge:hotelero | agreed merge:hotelero, but hotelera is also a feminine noun in its own right (a hotel company, 'la hotelera'); check whether a second real word hides behind the merge |
| pagada | merge:pagado | merge:pagar (changed) | agreed merge:pagado; the reviewers' questions note it could equally be the participle of pagar (merge:pagar); check the target |
| cabrio | drop | keep (changed) | agreed drop as a car-model name, but cabrio is an ordinary Spanish noun for a convertible car, and cabrío (macho cabrío) is a real adjective; check for a common-word reading |
| metrobus | drop | merge:metrobús (changed) | agreed drop as a transit brand, but metrobús is a common noun in several countries (a bus rapid transit line); possible merge:metrobús |
| kleenex | drop | keep (changed) | agreed drop as a brand, but kleenex is widely used generically in Spanish for a paper tissue ('un kleenex'); check whether that counts as an ordinary word |
| clínic | drop | drop | agreed drop as a Catalan hospital name; Hospital Clínic de Barcelona may count as a nationally famous public institution under the institutions ruling |
| jora | drop | drop | agreed drop as mostly a name, but jora is a real Andean Spanish word (chicha de jora, fermented maize); check whether the common word is a minority reading |

### s1-unflagged

| lemma | agreed | after adjudication | why queried |
|---|---|---|---|
| córneo | merge:córnea | keep (changed) | agreed merge:córnea, but córneo is a real adjective (capa córnea, tejido córneo) distinct from the eye noun córnea |
| esponjar | merge:esponja | keep (changed) | agreed merge:esponja, but esponjar is a real verb (to fluff up); a merge into the noun may hide it |
| amarar | merge:amar | merge:amar | agreed merge:amar, but amarar is a real verb (to land on water); check the forms |
| simultanear | merge:simultáneo | keep (changed) | agreed merge:simultáneo, but simultanear is a real verb (to do at the same time) |
| hibridar | merge:híbrido | merge:híbrido | agreed merge:híbrido, but hibridar is a real verb (to hybridise) |
| trozar | merge:troza | merge:troza | agreed merge:troza, but trozar is a real verb (to cut into pieces or logs) |
| decrementar | merge:decremento | keep (changed) | agreed merge:decremento, but decrementar is a real verb in use (opposite of incrementar) |
| cornear | merge:córnea | keep (changed) | agreed merge:córnea, but cornear is a real verb (to gore, of a bull); the target looks wrong |
| adujar | merge:aducir | merge:aducir | agreed merge:aducir; adujar is also a real nautical verb (to coil rope), though adujo is a form of aducir; check which reading the forms show |
| ripiar | merge:ripio | merge:ripio | agreed merge:ripio, but ripiar is a real (Caribbean) verb (to shred) |
| chinchar | merge:chinche | keep (changed) | agreed merge:chinche, but chinchar is a common colloquial verb (to annoy: no me chinches) |
| jabonar | merge:jabón | merge:jabón | agreed merge:jabón, but jabonar is a real verb (to soap) |
| rutilar | merge:rutilo | merge:rutilo | agreed merge:rutilo, but rutilar is a real verb (to shine); rutilo is a mineral |
| esclerótico | merge:esclerótica | merge:esclerótica | agreed merge:esclerótica, but esclerótico is a real adjective (sclerotic), distinct from the eye noun |
| precisa | merge:preciso | merge:preciso | agreed merge:preciso, but precisa is also the 3sg of precisar (to need/specify); check whether the verb reading is the majority |
| pruebo | merge:prueba | merge:prueba | agreed merge:prueba, but pruebo is the 1sg of probar; the target looks wrong (merge:probar?) |
| tesorer | merge:tesorería | merge:tesorería | agreed merge:tesorería; a cut-off tesorer could equally be tesorero (or tesorera); check the forms |
| contenidor | merge:contenido | merge:contenido | agreed merge:contenido, but contenidor looks like a misspelling of contenedor (or Catalan for container); check the target |
| valorarse | merge:valorar | merge:valorar | agreed merge:valorar; the lemmatiser convention keeps pronominal verbs as their own lemma (hacerse, quedarse) |
| hacero | merge:hacer | merge:hacer | agreed merge:hacer, but hacero may be a misspelling of acero (steel); check the forms |
| fregón | merge:fregona | merge:fregona | agreed merge:fregona, but fregón is a real adjective (Mexican colloquial: skilled, or annoying) |
| olográfica | merge:holográfico | merge:holográfico | agreed merge:holográfico, but ológrafo/ológrafa is a distinct real word (testamento ológrafo); check the target |
| circulo | merge:círculo | merge:círculo | agreed accent merge:círculo, but circulo is also the 1sg of circular; check whether the verb reading matters |
| rever | drop | keep (changed) | agreed drop, but rever is a real Spanish verb (to see again, to review) |
| changar | drop | drop | agreed drop, but changar is a real Latin American verb (to do odd jobs) |
| noticiar | drop | drop | agreed drop, but noticiar is a real (if rare) Spanish verb (to give news of) |
| ponible | drop | keep (changed) | agreed drop, but ponible is a Spanish adjective in real use (tecnología ponible, wearable) |
| brear | merge:brea | merge:brea | agreed merge:brea, but brear is a real verb (to tar; to pester) |
| despechar | merge:despecho | keep (changed) | agreed merge:despecho, but despechar is a real verb (to spite; to wean) |

## Questions

Every `# question` line, as the reviewers and the adjudicator wrote them (also in each round's `questions.txt`).
The adjudicator's lines come last in each list; they are grouped questions for the developer.

### s1-flagged (110 lines)

```
# question antiaging: an English cosmetics loan, written as one word, with no clear Spanish form (antiedad); kept as established, but borderline
# question antiaging: could count as an established marketing loan (anti-aging), but I judged it not established enough and dropped it
# question aparthotels: the academy spells it apartahotel but people also write aparthotel; merged to the academy form
# question aquilea: mostly a place or brand in the examples, but "aquilea" is also a real Spanish plant name, so I kept it as the common word.
# question aster: mostly a firm name in the examples, but the botanical noun is real Spanish, so kept
# question aster: the flower is a real Spanish word, but examples show only the company name
# question biociencias: could also be kept as a plural-only noun, but biociencia is the clear singular lemma
# question bonoloto: a famous Spanish state lottery game, but a product name; dropped as a product rather than kept as an institution.
# question bonoloto: state lottery game could count as a famous public institution, but treated as a product
# question borderline: the English word is used in Spanish psychiatry, but most examples are a bar name
# question bule: Spanish regional common word (calabash) possible, but the examples show a proper name
# question by-pass: the academy writes "baipás" and people write "bypass"; merged to the form people write.
# question cazacarro: lemma is written only as cazacarros (invariable); unsure whether the intended lemma is cazacarros or cazacarro, merged to cazacarros as the written form
# question cazacarro: lemma looks like singular but the word is invariable in the text (cazacarros singular); I chose merge:cazacarros to match the written form
# question cepe: acronym reading (CEPE) is the majority, but the common word cepe exists
# question cepe: the examples are mostly the UN commission acronym CEPE, but the real Spanish word cepe exists; kept as the common word
# question chanson: French loan for a music genre; unclear whether it is established enough in Spanish to keep
# question chanson: it is used as a music genre label in Spanish text, but I judged it not established enough for a learner and dropped it.
# question chlamydia: could merge to clamidia, but the examples are almost all the Latin binomial, so I dropped it
# question cide: CIDE is nationally known in Mexico but less famous than UNAM, so whether it counts as a famous institution is unclear
# question cide: a nationally known Mexican research institution but not a household name like UNAM; kept as a famous institution.
# question clad: it is an intergovernmental centre, but not a famous international body, so I dropped it
# question costo-efectiva: this is a calque of the English "cost-effective"; I dropped it as a hyphenated compound rather than merging it into a lemma such as costoefectivo, since no obvious Spanish lemma exists.
# question counseling: mostly English-phrase examples, but the term is used as a loan in Spanish psychology; kept as a borderline case.
# question cucos: all-caps website name; the real plural of "cuco" is a minority reading, so I dropped it.
# question dedicándono: the lemmatiser's pronominal convention suggests dedicarse, but plain dedicar is also possible; I chose dedicarse because the examples all use the "-nos" reflexive form.
# question dobra: examples mix the São Tomé currency with names and a Portuguese festival word; kept as the currency
# question dogecoin: cryptocurrency name could count as an established term or as a product/brand; dropped as a brand.
# question duvet: used as a shop term in some regions, but edredón is the usual word; dropped as not established
# question duvet: used in some Spanish regions for a quilt, but no examples were available, so I dropped it
# question ecdc: an EU agency that is not a place and is known mainly to specialists; kept as a famous international body on the AIEA/OMS model, but it could be judged a specialist acronym
# question echinacea: examples are mostly Latin binomials (Echinacea purpurea), but the plant name is real Spanish, so I merged it
# question eirl: Peruvian legal-form abbreviation, could count as an ordinary acronym, but treated as an organisation acronym
# question eirl: a legal-form abbreviation (like SL or SA) used in Peru; dropped as a specialist or organisation acronym
# question eoi: Escuela de Negocios EOI vs. Escuela Oficial de Idiomas; unclear whether it is a nationally famous public body, dropped as an ordinary organisation
# question etecsa: a state telecom company rather than a ministry or broadcaster; kept as nationally famous in Cuba, but it could count as a company brand
# question frangipani: it is a real word for the flower, but may be seen as a foreign term not fully adapted (Spanish also has franchipán)
# question gilet: a French loan that is used in cycling and fashion, but most examples are product names or a place, so I dropped it.
# question go-go: hyphenated, but not a compound of two listed words; kept as an established loan.
# question humilladero: most examples are the place name (Humilladero), but it is also a real common word; kept under the common-word rule.
# question hybris: hýbris may be a real Spanish word, but the examples are overwhelmingly the SAP product, so dropped
# question hybris: the Greek-origin word is a real concept (Spanish hibris), but the examples are the SAP company, so dropped rather than merged.
# question ieca: ordinary word in Spanish medicine (drug class) but only specialists use it; I decided drop
# question infanto-juvenil: could be kept as written instead if the hyphenated form is the one people write
# question infanto-juvenil: hyphenated but a standard Spanish adjective, not a compound of two listed words; kept
# question inpe: Peruvian prison institute or Brazilian space institute; neither is clearly famous enough, so dropped
# question inpe: two different national bodies share the acronym; unclear it is famous enough to keep
# question iptabl: the written form "iptables" is a real loan in sysadmin Spanish, but specialist only; dropped rather than merged.
# question isofix: standard/brand term that parents do use in Spanish; kept as an established technical term
# question ixil: Ixil is a Mayan people/language name (lowercase adjective ixil is used in Spanish); dropped as a proper noun, but could be kept as an ethnonym.
# question ixil: ethnic group and language of Guatemala, not a place; dropped as an ordinary proper name, but could be kept like maya
# question jaxa: a foreign national space agency, not a Spanish-world body or a listed international body; dropped as an ordinary organisation
# question lda: "Lda." can abbreviate "licenciada", but the examples show the technical acronym LDA and a company name; dropped.
# question lda: Lda can abbreviate licenciada, but the examples show LDA mostly as a technical acronym or company name; dropped.
# question lgbtqi: a variant of LGBT, which may merge into it if that lemma is on the list
# question lgbtqi: variant of the established LGBT; kept as an ordinary-use acronym but could be merged into LGBT if that is the listed form
# question litchi: DLE standard is lichi but litchi is also common; merged to lichi under the spelling rule
# question marathi: English spelling of the Spanish language name maratí; examples mostly come from English-language text
# question marathi: maratí is the academy form, but the counted text is mostly English-language context
# question maritima: most examples are place or proper-noun uses ("Stazione Maritima"), so the common-word reading may be a minority; merged because the lemma is a missing-accent form.
# question maritima: some examples are Italian place names (Stazione Maritima), but the lemma is mostly the unaccented adjective
# question mayday: loan used mostly in emergency-procedure texts; kept as an established distress call
# question mineco: a ministry-name acronym of a former ministry; kept as a famous public body
# question mirabel: mirabel is a rare plant name in Spanish, but the examples are hotel and place names, so dropped
# question mobil-home: French loan used for campsites; Spanish may write "mobil home", but the rules say hyphenated compounds drop
# question mobil-home: hyphenated French-origin loan used in Spanish camping contexts; unclear whether it counts as established or a hyphenated spelling to normalise
# question mutis: examples show only the surname (José Celestino Mutis, Red Universitaria Mutis), but "mutis" is a real Spanish word, so I kept it under the common-word rule.
# question mutis: the examples are mostly the surname Mutis, but mutis is a real Spanish word, so I kept it under the common-word rule.
# question pagada: could also be merge:pagar or an adjective lemma pagado; chose pagado
# question pagada: could be merge:pagar (participle) or pagado; chose pagado
# question papo: real but rare word, and the examples are almost all brand or name uses
# question paranaense: a demonym adjective derived from a place name, kept as a common adjective, though most uses are in team or region names.
# question paranaense: gentilic derived from a place name; kept as an ordinary adjective
# question picón: most examples are surnames, but picón is a real Spanish word; kept as a common word
# question picón: most occurrences are a surname, but the word picón is real Spanish, so kept under the common-word rule.
# question punjabi: panyabí is the academy form, but unsure how the list spells it; merged to panyabí.
# question punjabi: the Spanish form could be panyabí or punyabí; I chose punyabí.
# question rummy: card game name used in Spanish, but the examples are mostly app and brand titles
# question rummy: mostly "Gin Rummy" product names, but the game name is used in Spanish
# question salat: Islamic prayer term that appears in Spanish religious texts; unclear whether it counts as established
# question salat: transliterated religious term, could count as foreign
# question sandal: mixed English "sandal" and Spanish-looking "sandales"; dropped as mostly brand or English, but sandalia is the Spanish word
# question sedena: a Mexican ministry, kept as a famous institution, though it is mostly known by its acronym
# question sgm: abbreviation of "Segunda Guerra Mundial", a phrase and not a single listed lemma, so I dropped it instead of merging.
# question souq: Arabic loan with Spanish equivalent zoco, but occurrences are mostly in place names; dropped.
# question spritz: tagged ADJ and may be borderline loan, kept as established drink name
# question spritz: tagged ADJ but is a noun for the drink; kept as established loan
# question tadalafil: a generic drug name that is a real word in Spanish, but specialist and mostly spam context; dropped.
# question tadalafil: it may be too specialist for a learner's list; merged into the Spanish spelling.
# question tarahumara: an ethnonym is not a place, but the rules do not say whether people-group names count as common words; I kept it.
# question tarpon: Spanish has tarpón for the fish, but the counted uses are mostly brand and place, so dropped.
# question tic-tac: hyphenated, but it is a single onomatopoeic noun rather than a compound of two listed words, so kept
# question tic-tac: the academy writes "tictac", but people write the hyphenated form, so I kept the form as given
# question tomahawk: it is an established loan, but all sampled uses are names
# question tota: no examples available; "tota" may be Catalan or a name, dropped on the minority-reading rule
# question travelling: kept as an established film-camera term; the examples are mixed with English web text
# question uit-d: could merge into UIT if that entry is listed, but the "-D" sector code is not a separate word
# question ukiyo-e: an established art term in Spanish, but hyphenated and foreign
# question ukiyo-e: hyphenated but a single established art-term loan; keep vs drop is unclear under the rules
# question vaisnava: religious term from Sanskrit, adapted to Spanish spelling; kept, but it is niche vocabulary
# question vaisnava: specialist religious term, kept because it is written as a Spanish common noun
# question vtt: Spanish "VTT" (vehículo todo terreno) appears in two of three examples, but the Finnish institute reading also occurs; dropped as unsettled.
# question wayúu: it is a capitalised ethnonym, and the rules do not say whether ethnic-group names count as common words or as proper nouns; I kept it.
# question wenge: Spanish usually writes the wood as wengué, but the examples mix wood and place or brand uses; kept as written.
# question wenge: the academy writes wengué, but people write wenge, so I kept it as written.
# question clínic: do famous single hospitals (Hospital Clínic, La Paz, Gregorio Marañón) count as institutions to keep, or as places to drop?
# question etecsa, inpe: how famous must a body be in a smaller country (Cuba, Peru) to count as nationally famous, and what applies when one acronym names bodies in two countries?
# question go-go: merge into the academy's gogó when most hits are written go-go and many are names (go-go boyz, Go-Go Babyz)?
# question kleenex: brand names used generically when the academy has an adapted spelling (clínex): keep the brand spelling people write, merge into the academy form, or drop as a brand?
# question pending-names: this decision is offered in the answer format but not defined in the rules; I did not use it
```

### s1-unflagged (144 lines)

```
# question acollador: a real nautical word, but the examples are product spam where it mistranslates "lanyard"; dropped on that basis
# question ajar: forms are mostly "Aja"/"aja" (about 205 of 382), probably a name or interjection, while ajado/ajada are the real verb; kept for the verb reading
# question ajar: the examples are mostly the interjection or name "Aja"; it is kept for the real verb ajar (ajado)
# question akáshico: real derived adjective but esoteric; dropped as not useful to a learner
# question all-star: English hyphenated term, but it might count as an established loan in sports contexts
# question all-star: mostly English event and team names, but all-star is also used as a sports loan; dropped because the examples are proper names
# question altcoin: established loan or crypto-specialist jargon?
# question amadísimo: same superlative issue; merged to amado
# question antidesgaste: not in dictionaries, but it is a regular prefixed compound; kept
# question antidesgaste: transparent anti- compound that is common in industrial Spanish; dropped as not a dictionary word
# question arrobar: most forms are the noun arroba, so the lemma may belong to arroba; I kept it because arrobar is a real verb.
# question bizona: no examples were available, so I could not check the reading
# question bocinar: forms are mostly the noun bocina; kept because bocinar is a real verb
# question brea: the forms mix brea (tar), the name Brea and English "bread"; I merged to brea as the only clear Spanish word
# question carport: a regional loan, borderline for a learner's list; I kept it
# question carport: loan may be established enough in Spanish real-estate text to keep
# question catolica: the feminine católica or the masculine católico as the lemma; chose católico
# question changar: mixed English "change" and Spanish chango/changa, so the real-word reading is unclear
# question changar: mixed English "change", Spanish "chango" (monkey), and "changa"; no single obvious lemma, so dropped
# question chinchar: the verb exists, but the examples are the noun chinche; merged to the noun
# question choro: real Chilean noun but many examples are names; kept
# question clorella: kept as the form people write, though the academy form may be clorela.
# question coffeeshops: unclear whether coffeeshop is established enough in Spanish to keep; I merged on the assumption that it is
# question completísima: superlative merged to completo on the reading that it is an inflected form, though it could be read as a derived word
# question contendor: contendor is a real Spanish word, but the examples are typos of contenedor; I merged on the evidence of the examples.
# question contendor: contendor is also a valid Spanish word (contender), but the examples are mostly misspellings of contenedor
# question contenidor: the counted forms are mostly contenidos (contenido), but the lemma looks like Catalan or a misspelt contenedor.
# question coñito: I kept it as a real word and did not merge it into coño, because the diminutive is not clearly a broken lemma
# question crumble: some occurrences are a company name, but the food sense seems the majority
# question customizado: could be an English-derived adaptation of customizar (merge:customizar); judged nonstandard and dropped
# question customizado: could merge into personalizado, but that is a synonym rather than a spelling variant; dropped.
# question customizados: customizar is an anglicism; the rules don't say whether to merge or drop it.
# question córneo: córneo is a real adjective (horny), but the forms are overwhelmingly the noun córnea, so merged
# question córneo: córneo is a real adjective, but nearly all examples are the noun córnea, so I merged
# question daimyo: historical Japanese loan, unclear whether established enough in Spanish; dropped
# question dashboards: merged to dashboard, though dashboard itself may not count as an established loan.
# question dashboards: unclear whether the English loan dashboard is established enough to keep, so I merged it to the singular
# question datasets: "dataset" is a technical loan that may not be established enough; merged because the plural is filed as a lemma.
# question datasets: unclear whether dataset is established enough as a loan; merged on the assumption that it is
# question dronabinol: generic drug name, treated as specialist vocabulary
# question encoders: could instead merge into encoder if the technical loan counts as established
# question encoders: encoder is a technical loan and may not be wanted at all; I merged it to the singular.
# question encontro: Portuguese "Encontro(s)" is a minority of the examples; merged on the Spanish reading
# question encontro: could be a missing-accent "encontró" or a Portuguese noun, so the lemma is unclear
# question espectroscopio: a real word, but the examples are mostly espectroscopia; merged since the lemma looks conflated
# question espectroscopio: most forms are espectroscopia, a separate real word; kept without merging, but the lemma may be mismatched.
# question fluconazol: generic drug names (also oxicodona, lisinopril, salmeterol) are not covered by the rules; kept as ordinary Spanish medical nouns, but they could count as specialist vocabulary.
# question fluconazol: rules don't say whether generic drug names count as specialist vocabulary; dropped all drug names (fluconazol, oxicodona, lisinopril, salmeterol)
# question fluoxetina: drug name kept as widely known, unlike trastuzumab and bevacizumab; the rules don't say where everyday drug names stop
# question fluoxetina: no rule covers generic drug names; it is kept as a household medicine, unlike the INN biologics
# question foul: attested mostly in baseball text, so it may be too narrow for a general learner's list
# question gazebo: it may count as a foreign word not yet established
# question geocaching: English hobby term that may be a brand; I kept it as an established loan
# question guar: could be the real word guar (gum or plant) but no examples to check
# question haggis: well-known dish, but not established in Spanish; dropped
# question hutí: Spanish news uses it regularly, but it is a group name, so dropped under the proper-noun rule
# question hutí: ethnonym or group name versus an established common word in Spanish news; kept
# question imipramina: a specialist drug name, but a genuine Spanish word with a Spanish spelling
# question imipramina: a specialist drug name; kept as a real Spanish word, but it may count as too technical.
# question interesar: tagged ADJ and the forms are mostly the participle interesado, but the verb lemma is real, so kept rather than merged
# question jebuseo: biblical gentilic of an ancient people. Gentilics like yemení are kept, but this one is almost only Bible text and of little use to a learner.
# question jebuseo: lowercase gentilic of an ancient people (like cananeo), not a place, so rules on names versus real words don't clearly settle it
# question linebacker: established sports loan or specialist English term? Dropped as not established.
# question linebacker: sports loan might be established in Spanish sports press; judged not established enough for learners
# question loque: "loque" is also a real Spanish noun (a bee disease), but the PRON tag suggests most uses are "lo que" misspelt, and there are no examples to check; "lo que" as a merge target is a multiword phrase, not a clean lemma.
# question loque: "loque" is also a real word (a bee disease, "loque americana"), but the screener's note suggests the examples are mostly "lo que" typos, and no examples were available to check.
# question morphing: borderline between an established loan and a specialist term
# question morphing: unclear whether it is established in Spanish or just a software term.
# question multicloud: it is used in Spanish IT writing, so it might count as an established loan, but I judged it a specialist term.
# question murta: most examples are place names, but murta is a real Spanish plant word, so kept per the common-word rule
# question nivolumab: drug name kept like zidovudina would be consistent, but it is an INN used only by specialists
# question nivolumab: unadapted INN drug name; dropped as specialist, though zidovudina was kept as it is Spanish-adapted
# question numerosísimo: the rules cover plurals and conjugated forms but not superlatives; merged to the base adjective numeroso, though keeping it is arguable.
# question okra: not in the academy dictionary (quimbombó is the usual word), but used as a plain Spanish noun in the examples; kept
# question omnichannel: could be kept as an English marketing loan like marketing, but omnicanal is the Spanish form
# question omnichannel: merged to omnicanal on the assumption that omnicanal is the Spanish form; it could instead be kept as an established marketing loan.
# question orisha: established in Spanish religious and cultural writing, but niche; kept
# question orisha: religious term used in Spanish but borderline for being an established loan
# question oxandrolone: English spelling merged into oxandrolona, but a drug name only specialists use could also be dropped
# question oxandrolone: this is an English spelling of a drug name; I merged it into oxandrolona, but it could also be dropped as specialist vocabulary.
# question palear: most occurrences are "paleo" (diet), a clipped prefix form, but I kept the real verb palear
# question palear: paleo (diet) is the majority of the examples while the lemma is the verb palear
# question peplum: Latin/English-origin fashion term; kept as established in Spanish fashion usage
# question peplum: fashion term used in Spanish retail text, but also a Latin or French film-genre word; unclear whether established enough
# question perizita: could count as a proper name (ancient people) and drop
# question pitar: forms are mostly the nouns pita/pito, but the verb is real; kept as the verb rather than merging
# question playita: Las Playitas is a place name in many examples, but the common diminutive stays
# question prepa: clipping of preparatoria; kept as an established colloquial word instead of merging
# question prepa: kept as an established clipping, but the rules would merge an abbreviation of a listed word if preparatoria is listed
# question presidium: Latin/Russian loan, kept because dictionaries list presídium, but examples are mostly Russian-institution contexts
# question presidium: Latin/Russian-origin word that mostly refers to Soviet or Russian bodies; kept as established in Spanish
# question proméxico: government agency that is not a place, but unclear whether it is famous enough to count as a national institution; dropped
# question pruebo: the written form is always "prueba" (noun), so merged to prueba rather than probar
# question raeliano: demonym-like common word or movement name? Dropped as niche.
# question rever: the real verb is a minority of the forms against English "reverse"; dropped under the minority-reading rule
# question rifampicina: the rules don't say whether common drug names (rifampicina, alprazolam, sofosbuvir) count as specialist terms; I dropped them
# question rifampicina: the rules don't say whether drug names count as specialist terms; I kept them (also alprazolam, sofosbuvir, pantenol) but dropped the chemical-compound terms docosahexaenoico and enantato
# question rutilar: rutilado forms (29) may be a participle of rutilar, a real verb, rather than of rutilo; merged to rutilo as the majority form
# question rutilar: rutilar is also a real verb (to shine), but the examples are all about the mineral rutilo.
# question saz: no examples; saz is a rare real Spanish word (willow), but the counted forms look mostly like names/acronyms
# question scalping: English trading term; unclear whether it is established enough in Spanish finance to keep
# question scalping: a finance loan Spanish traders do use, but specialist; dropped
# question seder: a Jewish ritual term that Spanish does use (seder de Pésaj), but it is not clearly established enough to keep.
# question seder: foreign ritual term; kept because Spanish writes about the Pésaj seder, but could be treated as a specialist foreign word
# question shinto: Spanish also uses "shinto" itself, and "sintoísmo" names the religion; merged on the spelling rule.
# question sobreentender: the academy prefers sobrentender, but people write sobreentender, so I kept it
# question sobreentender: the academy prefers sobrentender, but sobreentender is the form people write, so I kept it
# question solapar: forms are mostly the noun solapa, which may need its own entry; kept because solapar is a real verb
# question stablecoin: the loan is newer and mostly used in crypto texts; kept as established in news Spanish
# question start-up: the target spelling startup is a guess; keep may be better if the list holds the hyphenated form
# question suscripto: variant of suscrito; kept as a written Rioplatense form rather than merged
# question taxa: could merge into taxón if read as the Latin plural, but examples use it as a singular, so I dropped it as a specialist term.
# question tealight: English product term; Spanish usually says "vela de té" or "velita"; dropped
# question telegrafiar: the verb is real, but most forms are the noun telegrafía; merged to the noun
# question ticks: the examples mix trading ticks (English loan) and nervous tics (Spanish tic); I merged to tic, but tick may be the intended lemma.
# question toppings: topping itself may not be established enough; merged on the assumption that it is
# question trackbacks: could be merge:trackback if web loans like blog count; dropped as specialist jargon.
# question trackbacks: merged to trackback, whose own keep/drop depends on whether it counts as an established web loan
# question transcendencia: RAE accepts both spellings; merged as a variant spelling
# question trascripción: RAE-accepted variant of transcripción, but it is what people write; kept rather than merged
# question trascripción: accepted variant of transcripción, so kept rather than merged; merge is arguable.
# question ultranza: kept as a word, but it only occurs in the phrase "a ultranza"; merge:a ultranza is the alternative.
# question ultranza: only occurs inside "a ultranza"; merged to the phrase, but a one-word keep could also be defended
# question valiosísimo: superlatives in -ísimo may count as their own lemma under the lemmatiser's conventions; I merged them as inflected forms (same for amadísimo)
# question valiosísimo: superlatives may count as conventions that stand (keep) rather than broken lemmas
# question veracruzana: demonym adjective, merged to masculine, though often part of the name Universidad Veracruzana
# question veracruzana: demonym derived from a place name; I merged the feminine adjective into veracruzano rather than treating it as an own-entry feminine
# question vestibilidad: calque from English "wearability", but it is a real Spanish word in common fashion use; kept
# question vestibilidad: possibly a calque of English "fit", but widely used in Spanish fashion retail, so kept
# question wargame: English hobby term that may be semi-established, but it is mostly product-listing text; dropped
# question wargame: established hobby loan or too specialist?
# question zoledrónico: the rules don't say whether drug names (zoledrónico, aripiprazol, verapamil) count as words a learner wants; I dropped them as specialist terms.
# question antidesgaste: are solid-written prefixed technical adjectives (anti-, multi-) keep or drop when the base word is listed?
# question chinchar, telegrafiar: I kept the real verb lemma while most counted forms belong to another word (chinche, telegrafía). Should these counts be split, or should keep imply moving them?
# question córneo, esponjar, desajustar, decrementar, despechar, simultanear (vs trozar, hibridar, fregón, ripiar): when a lemma is a real word but most forms belong to another listed word, should it be kept or merged? I kept it when the lemma's own forms are well attested and it is a word a learner meets.
# question haggis: should foreign culture-specific words with no Spanish equivalent (dish names and the like) count as established loans?
# question hutí: should lowercase ethnonyms or movement names used as common nouns (hutíes, talibanes) be kept, or dropped as organisation names?
# question numerosísimo: should -ísimo superlatives stay as their own lemmas, or merge into the base adjective (numeroso)?
# question rifampicina, pantenol, sofosbuvir, alprazolam, fluconazol, oxicodona, lisinopril: the rules don't cover generic drug and ingredient names. I kept those the general public knows and dropped prescription or clinical ones; please set a rule.
# question salmeterol, dronabinol: generic drug names (INNs) aren't covered by the rules; I dropped them as specialist terms. Should they always drop?
# question seder: foreign religious terms used in Spanish with no Spanish equivalent (séder, kosher, sabbat): established loan or drop?
# question transplante, vinil: should accepted variant spellings of a listed word (trasplante, vinilo) be kept as separate entries or merged?
# question ultranza: words that occur only inside a fixed phrase (a ultranza, de antemano): keep the word, or create a multiword entry like the split-loan rule?
# question zoledrónico, aripiprazol, verapamil, akáshico: the rules only drop specialist acronyms; please confirm that real but specialist or esoteric full words (drug names, New Age jargon) also drop
```
