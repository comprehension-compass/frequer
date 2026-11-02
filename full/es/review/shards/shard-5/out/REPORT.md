# es review shard 5: report

Branch `es-review-shard-5` (from `c4aacac`). Runtime `c07c701`, lemma wheel 1.5.0 (sha256 checked), review runner
uplift `f8c8a67` with the fixed example extractor; reviewers and screeners sonnet, adjudicator opus (config).

## Counts

| step | count |
|---|---:|
| routed lemmas | 5,918 (962 pending flagged, 4,956 unflagged keeps) |
| screened (unflagged) | 4,954 (2 learnable names left out as release entries), 20 batches, 0 failed |
| suspects | 911 (636 listed by both screeners) |
| flagged with an example | 850 / 962 (88.4 %) |
| suspects with an example | 828 / 911 (90.9 %) |

| round | lemmas | reviewers agreed | to adjudicator (disagreements + queries) | final agreed | adjudicated | undecided | keep | drop | merge |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| s5-flagged | 962 | 931 | 31 + 6 | 925 | 37 | 0 | 94 | 791 | 77 |
| s5-unflagged | 911 | 868 | 43 + 8 | 860 | 51 | 0 | 487 | 215 | 209 |

Every step reported no failed calls; nothing needed a rerun.

## Gate (my queries, and what the adjudicator decided)

I read every agreed merge and the accent-only merges (flagged: practico, rectángular, factoria; unflagged: 11, all
plain missing or misplaced accents), all agreed keeps and drops by lemma, and queried agreed decisions that could
hide a second real word, plus one misspelling kept as a lemma.

### s5-flagged

| lemma | why |
|---|---|
| practico | agreed merge:práctico, but the forms also hold the verb form practico (yo practico, from practicar); is práctico right for the bulk, or should the verb share go to practicar? |
| chama | agreed drop; chama/chamas is real Venezuelan and Colombian colloquial Spanish (girl); check whether the common word is a real share or a minority |
| anis | agreed drop; lowercase anis (33) may be anís (anise) without its accent: merge:anís if that reading holds |
| pua | agreed drop; lowercase pua/puas may be púa without its accent: merge:púa if that reading holds |
| jiji | agreed drop; jiji (87 lowercase) is a common written laugh interjection in Spanish; the interjection rule keeps such lemmas |
| marcona | agreed drop as a place, but almendra marcona is a real Spanish common noun (the almond variety); the common-word rule (granada, nevada) may keep it |

Outcome: practico → merge:práctico; chama → keep; anis → merge:anís; pua → merge:púa; jiji → keep; marcona → keep; 

### s5-unflagged

| lemma | why |
|---|---|
| capitular | agreed merge:capítulo, but capitular (423) and capitulares (237) are the real verb and adjective (sala capitular, capitular ante); merging them into capítulo hides a second real word |
| combar | agreed merge:combo, but combado/combada/combarse are the real verb combar (to bend); check whether the verb share is large enough to keep |
| enseriar | agreed merge:enserio, but enserio is a misspelling of the phrase en serio, not a Spanish lemma; target looks wrong (merge into serio, or drop) |
| pacer | agreed drop, but paciendo/pacían (233) are the real verb pacer (to graze); Pace/Pacer are names, the verb should keep |
| boj | agreed drop as BOJ (Bank of Japan), but lowercase boj (95) is the real Spanish noun boj (boxwood) |
| uro | agreed drop as the Uros people, but uro/uros is also the Spanish noun for the aurochs; check the lowercase share |
| híper | agreed drop, but híper is colloquial Spanish for hipermercado and a stand-alone prefix-word; examples only show one reading |
| neoyorkino | agreed keep, but Spanish writes neoyorquino; per the spelling rules a misspelling merges (merge:neoyorquino) unless neoyorkino is the form people write |

Outcome: capitular → keep; combar → merge:combo; enseriar → merge:serio; pacer → keep; boj → keep; uro → keep; híper → keep; neoyorkino → merge:neoyorquino; 

## Things to know

* **The adjudicate commands were run with `--rules`** pointing at the binding `review/rules/es-*-final.md`. The
  shard file's step 3 lines omit `--rules`, which would have made the adjudicator use the config's default
  (uplift's `prompts/es/rules-flagged.md`) rather than the final rules the reviewers saw.
* `out/` is matched by a generic `.gitignore` rule (`out/`, line 178), so the output files were added with
  `git add -f`. The batch caches, A/B side files and adjudication batches are not committed.
* Many questions overlap (both reviewers often raise the same one). Recurring classes: generic drug names
  (keep vs specialist drop: reviewers split, e.g. gabapentina, ketoconazol, emtricitabina); verb lemmas whose
  forms are mostly a related noun (alarmar, desmadrar, zanjar, capitular, cimbrar, parvo: keep vs merge vs split);
  feminine gentilic lemmas (kazaja, kirguisa); multiword merge targets (palo santo, post mortem, alter ego,
  open source); regional or Catalan institutions (govern, síndic, ecofin, tsj, segib); accepted variant spellings
  (iodo/yodo, neoyorkino/neoyorquino, vermú/vermut).

## Every `# question` line

### s5-flagged (reviewers, then adjudicator)

```
# question alef: kept as a Spanish letter name (álef), but the list form may need an accent
# question anis: no examples; lowercase "anis" might be anís without accent, but name reading is the majority
# question anis: the lowercase 33 may be anís missing its accent, but the majority are names
# question apartament: could be read as a cut-off or misspelt apartamento, but the examples are missing and it looks like another language, so I dropped it.
# question apartament: no examples were shown, so I can't tell whether it is a truncated apartamento or Catalan/Romanian text; I merged it.
# question arriendos: no examples shown; merged to arriendo on the assumption it is the plural of the common noun, not a business name
# question asociarno: "asociarnos con" is pronominal (asociarse), but "asociarnos a ella" could be plain asociar; chose asociarse.
# question avant-garde: established loan in Spanish arts writing, or foreign word?
# question bde: BdE (Banco de España) would be a keep if it were the majority reading, but the examples show a format code and the counts are mixed
# question beamer: Spanish "beamer" (projector) exists in some regions, but most examples are brand/LaTeX uses, so dropped
# question beamer: the Spanish "projector" sense exists in some regions, but most examples are LaTeX or a car brand, so I dropped it
# question beta-alanina: real Spanish noun but hyphenated and specialist; dropped
# question blitzkrieg: also a game title in many examples, but the historical loan is established in Spanish
# question bluegrass: Music genre loan, but about half the uses are the Kentucky region name. I kept it as the genre.
# question bluegrass: a music-genre loan, but about half the uses are the Kentucky region name
# question cfdi: widely known in Mexico as a tax-invoice term, but treated as a technical acronym and dropped
# question cfdi: widely used in Mexico for electronic invoices, but I treated it as a specialist acronym
# question chama: Venezuelan and Colombian slang "chama" is real, but nearly all occurrences are capitalised names, and there are no examples to check
# question chama: Venezuelan slang "chama" (girl) is a real word, but the capitalisation and the plural Chamas suggest names; no examples were available.
# question chambray: it may be established in Spanish fashion vocabulary, but the examples are product listings, so I dropped it.
# question chiffon: assumed the adapted form is "chifón"; the rules don't say whether chiffon is established as a loan
# question ciudadciudad: rule says doubled words drop, but the merge to ciudad is obvious
# question congr: forms are mostly "Congres" (Catalan or English "Congress"), so merge:congreso is not obvious; dropped.
# question créeme: merged to creer as a conjugated form, though pronominal-verb conventions might argue otherwise.
# question d-os: assumed the list's lemma for Dios is lowercase "dios"
# question d-os: the lemma form of dios (lower or upper case) is not specified.
# question doge: the examples show hotel names and the DOGE acronym alongside the ruler sense; kept as a real common word.
# question durian: RAE prefers "durión"; I kept the form used in the text.
# question e-bici: hyphenated compound of "e" and "bici" (an established word for e-bike); dropped under the hyphenated-compound rule, but a learner might want it.
# question e-bici: it may be a real word, but the rules drop hyphenated compounds, so I dropped it.
# question e-visa: hyphenated, with no adapted Spanish spelling; kept as a useful established term.
# question eco-lodge: could merge into "ecolodge" if that is a listed loan, but no such lemma is shown, so dropped.
# question ecofin: EU Council body could count as a famous international body, but it is little known to learners; dropped.
# question ecofin: EU Council configuration, not clearly a famous international body like ONU or UE; kept as one.
# question enea: most examples are the names Enea and Eneas, but the common word (the plant) exists, so kept
# question furano: capitalised place-name uses outnumber the chemical noun, but the plural "furanos" is a real word
# question furano: the city name is the majority of occurrences, but the chemical term furanos is a real common word, so kept.
# question govern: Catalan regional government could count as a public body, but it is not a Spanish word and not nationally famous, so dropped
# question govern: Catalan word for a regional government (Govern Balear); kept as a public body, but it could be read as a foreign word.
# question higuerón: examples are mostly place names, but higuerón is a real Spanish tree name, so I kept it.
# question higuerón: examples are mostly the place name, but higuerón is also a real tree name; kept as the common word
# question holi: could be the colloquial Spanish greeting "holi", but the examples are the festival and brand names
# question holi: no examples were available; kept on the strength of the lowercase greeting use, but the festival name may dominate.
# question huesa: kept as the common word (grave); most examples are surname or company uses
# question iau: international body but a specialist astronomy acronym, so dropped as not famous enough
# question idae: a Spanish public energy agency, but possibly not famous enough to count as a national institution
# question inec: Ecuador's national statistics institute could count as a public body, but the examples include an Irish venue; dropped.
# question jiji: laughter "jiji" is a real informal Spanish interjection, but it is under half of occurrences and the capitalised ones are names; dropped
# question jipijapa: also a real word for the straw used in Panama hats, but the examples are mostly the Ecuadorian town, so dropped.
# question jipijapa: most examples are the town, but it is also a common word (the hat and its fibre); kept under the common-word rule
# question kalashnikov: common noun (rifle) versus a person's surname; merged to the Spanish form
# question kalashnikov: many occurrences are the surname, but the rifle sense is an established common noun, so I kept it.
# question lavalier: established term for a clip-on microphone, but only specialists use it; dropped.
# question lavalier: many examples are the Rode product, but the word is also a common noun for the microphone, so I kept it.
# question lehendakari: could count as a title (drop), but it is an established common noun in Spanish press, so kept
# question marcona: almendra marcona is a real Spanish common noun (variety), but most examples are the Peruvian place; dropped on majority place-name reading
# question marcona: it is also an almond variety (almendra Marcona), but the place-name examples dominate; dropped.
# question marengo: mix of colour word and surname/farm name; colour reading seems the majority, so kept.
# question masterplan: used in Spanish architecture text, so it may count as an established loan, but dropped as mostly English or proper-name use
# question monusco: UN mission rather than a body like ONU; dropped as too specialist, could be argued keep
# question monusco: UN peacekeeping mission; dropped as specialist rather than a famous international body
# question morra: most examples are surnames or place names, with only the Mexican slang reading as a real word
# question mullah: Spanish writes "mulá", but the examples are mostly names or junk, so dropped instead of merged
# question mungo: "frijol mungo" is a real Spanish term, but most occurrences are the name Mungo
# question nini: most running text is a name, but nini is also a real Spanish word, so I kept it.
# question no-ficción: "no ficción" is a real term, but the rules drop hyphenated compounds of two listed words
# question no-ficción: rules say hyphenated compounds of two listed words drop, but "no ficción" is the standard spelling, so I merged it.
# question oacnudh: UN human rights office in Colombia; dropped as specialist, could count as an international body
# question oacnudh: UN office, kept as an international body, but it is quite specialist
# question open-source: hyphenated English loan; kept as an established loan, but it may belong under a spaced form "open source" instead
# question open-source: the loan "open source" may not be on the list as its own entry; merged on the spelling rule
# question pavlova: examples mix the dessert and a place name; kept as the common word
# question pichi: no examples available; kept as the Spanish dress word, but it may be mostly a name
# question pilsner: English-origin beer style used in Spanish; kept as an established loan but borderline
# question popo: Colloquial in Mexico and elsewhere, but the single example shows only one reading; kept as a common word.
# question post-mortem: Spanish writes "post mortem" or "postmortem"; I merged to the spaced form, but it could be kept as a loan instead.
# question practico: Mixed: the verb form (I practise) in "Practico a diario" and the unaccented adjective in "practicos". I merged to práctico because of the adjective count.
# question practico: the examples mix the verb form "practico" (practicar) with "practicos" for práctico, so the merge target is uncertain
# question pre-reserva: it could merge into prerreserva, but that form is not clearly on the list, so I dropped it.
# question pua: lowercase "puas" may be the real word "púa" without its accent, but PUA the acronym dominates
# question ranchito: most examples are business or place names, but the common noun is real Spanish, so I kept it.
# question samu: no examples; could be the public emergency service (SAMU), but dropped as an ordinary organisation
# question satori: Japanese loan with some Spanish use, but most examples are names, so dropped.
# question satori: examples mix the Buddhist term with company and product names; kept as an established loan.
# question savana: it is a misspelling of sabana, but the examples are mostly brand names, so I dropped it rather than merging.
# question savana: the real word is sabana, but the examples are almost all the brand name
# question screensaver: English loan that may be established in Spanish computing, but the examples are mostly product names.
# question segib: SEGIB is an international body but regional; kept as a famous international institution, which may be a stretch.
# question self-service: could be kept as an established loan, but hyphenated English spelling with a Spanish equivalent, so dropped.
# question self-service: it could count as an established loan, but I judged it a hyphenated English spelling with a Spanish equivalent.
# question semi-estructurada: the lemma is filed in the feminine; I merged to the masculine adjective lemma semiestructurado.
# question shaders: specialist loan, but common in Spanish game-dev text, so I kept it
# question sico: no examples; could be a fragment of a psico- word
# question snooze: used in Spanish text about alarms and apps, but I judged it not established enough to keep.
# question síndic: Catalan/Andorran public office title, dropped as a title; "síndico" would be the Spanish word
# question síndic: it could be treated as an institution title, but it is Catalan and a title; dropped.
# question taiko: the lowercase instrument sense (79 uses) might count as an established loan
# question trackball: technical loan, kept as established but marginal
# question trifolio: all examples refer to the Adidas logo; I kept it as a real, rare Spanish word.
# question trifolio: it is a real but rare word, and most occurrences are the Adidas logo, so I kept it as a common word.
# question tsj: acronym used for Spanish regional courts and Venezuela's supreme court; treated as a famous public body.
# question tsj: the examples are Venezuelan (Tribunal Supremo de Justicia); I judged it a nationally famous public body, but it may be too country-specific.
# question tvn: Chilean public broadcaster TVN would be keep, but the Korean tvN, a parts catalogue and logo uses may be the majority.
# question tvn: TVN is Chile's national broadcaster, which would be a keep, but the examples mix it with Korean tvN and a parts code, so I dropped it.
# question unhcr: the rules don't say whether the English acronym of a famous international body should merge into the Spanish ACNUR; dropped as a foreign-language form
# question vatio-hora: a real unit term, but the rules drop hyphenated compounds of two listed words
# question webhosting: the examples are product names, but the term is a general tech loan
# question yoes: the "yoes" of esoteric (Gurdjieff-style) texts is a noun use of "yo"; merge assumes the pronoun lemma "yo" is the right target.
# question ypfb: state company rather than a ministry; kept as a national public body
# question zambra: the capitalised author surname Zambra dominates, but the common word (the dance) is clearly real, so I kept it.
# question zeitgeist: established loan or foreign word? Two of three examples are the real word, so I kept it.
# question zeitgeist: the word is used in Spanish cultural writing (distopías example), but most occurrences are a forum or film name, so I dropped it.
# question zouk: music-genre loan might be wanted, but the examples are mostly place and brand names
# question zouk: some examples are the place Zouk Mikayel, but the genre reading is the majority
# question ecofin: do EU Council configurations (Ecofin, JAI) count as famous international bodies like UE and OTAN?
# question govern: Catalan institution names used in Spanish media (Govern, Generalitat-type bodies): should they count as famous institutions when the lemma is a Catalan common noun?
# question holi: are cute/informal greeting variants (holi) with a non-Spanish majority reading (the festival) kept under the interjection rule, as jiji is?
# question open-source: is "open source" established enough in Spanish to be a list entry (Spanish also says "código abierto")? If not, this should drop rather than merge.
# question practico: when a lemma mixes a missing-accent adjective (prácticos) with a correct verb form (practico), is the majority merge enough, or should the verb share go to practicar?
```

### s5-unflagged (reviewers, then adjudicator)

```
# question acerca: it is nearly always "acerca de"; kept as a word, but the learner may want the phrase entry.
# question acerca: it mostly occurs in "acerca de", but it is a real word, so I kept it rather than treating it as a fragment.
# question afinar: many forms counted are "afines" (adjective afín), so the lemma is mixed, but afinar itself is valid.
# question alarmar: about 70% of forms are the noun alarmas, so merge:alarma is arguable; I kept it because alarmar is a real verb.
# question alarmar: most occurrences are the noun alarma(s), so a separate alarma entry may be needed; I kept the verb lemma
# question aneto: nearly every example is the Pyrenean peak, but aneto is a real word for dill, so I applied the granada rule
# question ashram: loan from Sanskrit/Hindi, borderline for "established in Spanish"; kept
# question boldenona: generic drug name; could count as an ordinary word, dropped as specialist
# question boldenona: it is a real Spanish drug name, but only specialists use it, so I dropped it.
# question carboplatino: same as gabapentina, generic drug name
# question changelog: it could count as an established tech loan like blog or chat; dropped because it is specialist web vocabulary.
# question chilaquil: the forms are almost all plural (chilaquiles); I kept the singular lemma instead of merging it into the plural.
# question ciar: the real verb ciar is rare and the data is mostly the colour cian, so I merged it into cian, but Cíes and Ciara are mixed in
# question ciar: the real verb ciar is rare and the forms are mostly the colour cian, so I merged into cian; drop is also defensible because of the Cíes and Ciara noise
# question cimbrar: the forms are mostly the noun cimbra, but cimbrar is itself a real verb, so kept rather than merged
# question confi: could be a clipped form of "confianza" or of a name like "Confi", but the evidence is unclear, so I dropped it.
# question contribuidor: calque of "contributor", but attested and not the same as contribuyente, so kept
# question crimpado: English-derived technical term; kept because the Spanish technical use is widespread.
# question crimpado: it is real technical Spanish from English crimp, but I treated it as specialist jargon and dropped it.
# question customizadas: customizar is an anglicism and personalizado is the standard Spanish word; merged to the participle customizado
# question darma: the Spanish academy writes "dharma", but the list uses the form people write, so I kept darma as the real word rather than merging.
# question deejay: dj vs deejay as the listed form; chose dj as the usual Spanish spelling
# question deejay: the rules don't say whether it stays as its own entry or merges into DJ (which Spanish also writes); I kept it as an established loan.
# question desenfocar: forms are mostly the noun desenfoque, but the verb is real so I kept it
# question desenfocar: the forms are mostly the noun desenfoque, but the verb is real and the participles belong to it, so I kept it
# question desmadrar: forms are mostly the noun desmadre, but the verb is real too; kept rather than merged
# question desmadrar: the noun desmadre dominates the counts, so merge:desmadre is arguable; I kept the lemma because desmadrar is a real verb.
# question desta: archaic contraction of "de esta" with no clean single lemma to merge into; dropped rather than merged.
# question diligenciar: most forms are the noun diligencia, so merge:diligencia is arguable; I kept it because diligenciar is a real verb.
# question disturbar: DLE status is uncertain and many hits may be calques of English "disturb"; kept as a Spanish verb
# question dorio: most examples are the Italian place Dorio or the surname Doria, but dorios is the real adjective; I kept it.
# question efesio: the word is a real gentilicio (from Éfeso), but nearly all uses are the book title Efesios; I dropped it as a title
# question embragar: most counts are "embrago", a misspelling of "embargo", yet the verb embragar is real; kept.
# question embragar: most forms are embrago, which may be a typo for embargo or a misspelling of embrague, so the lemma is mixed; I kept it as the real verb.
# question empecinar: the dictionary form is empecinarse, but forms like empecinado are mostly participial adjectives; kept as given
# question empecinar: the dictionary form is empecinarse, but the pronominal convention and the participle adjective make keep acceptable
# question emtricitabina: no rule covers generic drug names; I kept them as common nouns (also atazanavir, enalapril)
# question emtricitabina: the rules don't say whether generic drug names belong on the list. I kept them as ordinary nouns (same for atazanavir and enalapril).
# question eolio: Eolio/eolia is also a real adjective (arpa eolia), but over 90% of the examples are the island name
# question eritreo: most occurrences are the place Eritrea; kept as the demonym
# question eritreo: most occurrences are the place name Eritrea, but eritreo is a real demonym, so kept
# question estacionarse: same as normalizarse; kept as pronominal, merge:estacionar is arguable
# question estilográfico: forms are mostly feminine (pluma estilográfica); kept because the lemma is not clearly broken
# question finisher: established enough in Spanish running/triathlon use to keep, or an unadapted English loan?
# question fucus: it could be read as a specialist Latin genus name rather than a Spanish noun.
# question fucus: the examples show only the algae genus; Spanish also has fuco, so it could be a merge:fuco
# question gabapentina: drug names are not covered by the rules; kept as ordinary medical vocabulary, same for carboplatino
# question gabapentina: generic drug names are not covered by the rules; dropped as specialist vocabulary
# question ganas: gana is mostly used in the plural (tener ganas), so keep is possible; I merged because it is a plural filed as lemma.
# question garantir: Portuguese-looking participles (garantida, garantido) may be Portuguese text, not Spanish misspellings; merged into garantizar anyway.
# question gravísima: could merge to gravísimo (the superlative) or to grave; chose grave
# question gravísima: merge target could be grave or gravísimo; I chose gravísimo as the superlative's own base.
# question guilloché: a French loan used in watchmaking; I judged it too specialist for a learner list
# question hacimiento: archaic and found mostly in biblical text (hacimiento de gracias); kept as a real dictionary word, but a learner may not need it.
# question hacimiento: archaic and found mostly in the Reina-Valera Bible, so it may not be useful to a learner
# question hygge: Danish loan with some use in Spanish lifestyle text; dropped as not yet established
# question híper: also colloquial for hipermercado, but the examples show the prefix use
# question indochino: Indochina forms (place name) are a minority, so I kept the adjective.
# question iodo: iodo is an accepted variant of yodo, not a clear error; I merged because the list uses the more common form.
# question iodo: valid academy variant of yodo, not clearly broken, so kept; merge:yodo is possible if the list prefers the common form
# question kazaja: gentilic adjectives with a feminine form are not clearly covered by the "own feminine entry" convention; I merged it into the masculine entry.
# question kazaja: the lemma is kazajo or kazako; I chose kazajo as the form the screener suggested
# question ketoconazol: generic drug names are not covered by the rules; dropped as specialist
# question kirguisa: feminine of kirguís, whether it counts as its own entry like hermana is unclear. Decided merge.
# question kirguisa: gentilic lemma could be kirguís or kirguiso; I chose kirguís per the screener note.
# question loguear: informal anglicism; kept as widely used in Latin American Spanish
# question macarons: the singular macaron may be rare in the text, but I merged because it is a plural filed as lemma.
# question mandrinado: specialist machining term, though still a real Spanish word
# question marketers: English plural of a person noun; "marketing" is established but "marketer" is doubtful
# question marketers: is marketer established enough in Spanish to merge into, or should it drop as an English word?
# question minut: Catalan plural dominates and the examples are missing; dropped as non-Spanish rather than merged into minuto.
# question multidominio: technical compound, kept as a real word on thin evidence
# question nakba: a historical event name that is also common in Spanish news, so it could count as a loan; I followed the "events drop" rule
# question nakba: the event name is a proper noun and drops under the events rule, but it is also used as a common noun in Spanish news
# question nefita: a group demonym used mostly in Mormon texts; I treated it as a proper name and dropped it
# question negrito: forms are mostly negrita (bold type), so merge:negrita is arguable, but negrito is a real word and I kept it
# question negrito: majority of occurrences are negrita (bold font), which might warrant its own entry rather than keeping negrito alone
# question nickname: the more established loan is nick; kept because it is common in Spanish web text.
# question normalizarse: forms are just "se + verb"; I kept it as a pronominal lemma, but merge:normalizar is arguable
# question obstante: it is nearly always "no obstante"; kept as a real word, but the phrase may be the better entry.
# question obstante: it occurs almost only in "no obstante", but it is a real word, so I kept it.
# question oud: Arabic loan with no examples; judged a foreign word, but it could count as an established loan.
# question oud: Oud is an Arabic loan that could be established (the instrument, also in perfumery), but most uses look like capitalised brand or perfume names, so I dropped it.
# question oxycodone: merged to oxicodona (adapted Spanish spelling) on the assumption that it counts as an adapted word
# question palmo: forms are mostly palmito, a different word; kept palmo but palmito may need its own entry
# question palmo: most forms are palmito, a different word; I kept palmo because the lemma itself is valid.
# question palosanto: merged to the two-word "palo santo", but some examples are the brand Palosanto, so drop is possible
# question palosanto: the RAE writes "palo santo" as two words, and PaloSanto is also a brand; I merged it on the strength of the tree-name reading.
# question pandear: forms are the noun pandeo, but pandear is also a real verb; I merged to the noun because the counted text is almost all noun use.
# question parvo: parvo (canine parvovirus) is a minority use; chose parva as the majority reading
# question patagón: the demonym is a real word, but most occurrences are the place Patagones
# question patagón: the mostly-place-name majority (Patagones) would drop, but the rule keeps real common words, so I kept it.
# question pirar: pira, piro and Pires are mixed; the verb pirar (slang) exists, but I merged to pira because it dominates the counts
# question pleyadiano: it could be read as a gentilic of a star cluster rather than a proper noun; I dropped it as lore-specific
# question pleyadiano: the word is used mostly for a fictional or esoteric group, so it is borderline between a common word and a name. I kept it as a derived common word.
# question posar: forms such as "posada" and "pose" may belong to other lemmas, but posar itself is valid.
# question punzonar: punzonado is a participle used as a noun; merged on the noun reading, but keeping the verb is also defensible
# question punzonar: punzonar is a real verb, but the forms are mostly the noun punzonado, so merged
# question quemarropa: merged to "a quemarropa" as a cut-off fragment of a fixed phrase, but it could be kept as a one-word adverbial entry
# question quemarropa: only occurs in "a quemarropa"; kept as the word, though could be a fragment of the locution
# question quipo: QUIPO (34) in capitals may be a brand rather than the quipu variant; no examples were available.
# question randomizado: could be dropped as a medical anglicism instead of merged to aleatorizado
# question randomizado: could be dropped as an anglicism instead of merged into aleatorizado.
# question recuérdese: could be recordarse if read as pronominal ("recuérdese de que"), but most uses are impersonal/passive "recuérdese que"
# question retrabajo: may be a calque of "rework" in technical text; kept as a Spanish word
# question rezonificación: the word is rare and may be a calque of English rezoning, but it is used in Spanish; I kept it.
# question rien: the Spanish reading "ríen" fits the first example but the second is the name Rien Poortvliet, and the split between them is unclear
# question rooteo: tech slang from English root; I dropped it as not established.
# question santificadora: the feminine form of an adjective filed as lemma; I merged it to santificador as a broken lemma rather than a separate feminine entry
# question sirolimus: specialist drug name, kept as a real word since the rules don't exclude non-acronym technical terms
# question softcore: established adult/gaming loan, or too niche? Decided drop.
# question softcore: hardcore is well established in Spanish, so softcore may deserve keep; dropped as less established.
# question systema: could merge to sistema if the Latin or old-spelling reading were the majority, but examples show mostly the martial art
# question tamari: Japanese soy sauce, could count as an established loan
# question tamari: it is sold in Spanish shops, so it might count as an established loan; no examples were available.
# question templar: counts are mostly the noun temple and English Temple/Templar, so merge:temple is possible; kept as the real verb
# question termolúdico: rare and tied to spa names (Caldea), but a regular compound adjective, so kept
# question termolúdico: real word or mostly the Caldea brand context?
# question toffee: DLE has the adapted form "tofe", but people write "toffee", so I kept it rather than merging.
# question toffee: mostly in English product or recipe names, but it is also a Spanish loan for the sweet
# question trancar: forms are mixed (tranca, tranque, and Tranco, a reservoir name); kept as the real verb
# question transm: abbreviation could stand for transmisión, transmitido or others, so no obvious merge target; dropped
# question uro: it is both an ethnic group and a place-linked name, so I dropped it as a proper noun
# question vajrayana: it is a Buddhist term that some Spanish texts use, but I treated it as a non-established Sanskrit word
# question vajrayana: it is a Buddhist tradition name (like budismo) written lowercase 32 times; I treated it as a specialist foreign term and dropped it.
# question vermú: vermut is the academy's main spelling and vermú is also accepted; I kept vermú as the form people write
# question zanjar: most forms are the noun zanja, so merge:zanja is arguable; I kept it because zanjar is a common verb (zanjar el debate).
# question capitular: the misfiled capitulo forms (~1,700) outnumber the real capitular forms (~780); should such entries be split rather than decided as a whole?
# question cimbrar, parvo: the lemma has absorbed forms of a separate real noun (cimbra, parva); should those forms be split into their own entry?
# question gabapentina, carboplatino: should generic drug names be kept when fairly common (gabapentina), or always dropped as specialist?
# question gravísima: should superlatives merge into their own masculine lemma (gravísimo) or into the base adjective (grave)?
# question híper: a real word (hipermercado) whose sample examples show only the detached prefix; should it be kept on the word reading, or dropped as a fragment?
# question iodo: should accepted Spanish variant spellings (iodo/yodo) merge into the more common form, or stay as their own entries?
# question neoyorkino: neoyorkino is widely written; does the "form people write" rule override the academy's neoyorquino here?
# question sonotrodo, multidominio: real but specialist non-acronym technical words; the rules only drop specialist acronyms, so should specialist words drop too?
# question unío, centrándome: when a clitic form's verb has both a base and a pronominal lemma (unir/unirse, centrar/centrarse), should the merge target the pronominal lemma?
```
