# es review shard 2: report

Branch `es-review-shard-2`, based on `c4aacac`. Rules: `review/rules/es-flagged-final.md` (flagged) and
`review/rules/es-unflagged-final.md` (suspects), for both the reviewers and the adjudicator. Every step's calls
finished: no failed batches and nothing left undecided.

**Adjudication rerun.** The first adjudication ran without `--rules`, so it used the config's default (uplift's
older prompts, where places go to `pending-names` and there is no institutions rule). At the coordinator's request
(fixed commands on `full-es` f117a3a) I moved each round's `adjudication/` aside and reran stage 1 from its cache
to restore the stage-1 `questions.txt`. Agreed, disagreement and query rows came out the same and no new reviewer
calls were made. I then reran both adjudications with the final rules and the same `queries.tsv`. All files in
`out/` are from the rerun.

## Counts

| step | count |
|---|---:|
| flagged queue (action `pending`) | 933 |
| flagged with an example | 840 (90 %) |
| unflagged pool (`keep`, no flag) | 4,986 |
| screened (3 learnable names left out by the screener) | 4,983 |
| suspects (union of both screeners) | 741 (521 marked by both) |
| suspects with an example | 670 (90 %) |

| round | agreed | adjudicated (of which queried) | keep | drop | merge |
|---|---:|---:|---:|---:|---:|
| s2-flagged | 909 | 24 (3) | 84 | 782 | 67 |
| s2-unflagged | 683 | 58 (16) | 331 | 223 | 187 |

Stage 1 agreement before queries: flagged 912 agreed / 21 disagreements; unflagged 699 agreed / 42 disagreements.
No `pending-names` decisions remain.

## Gate and queries

I read every agreed merge, `accent-merges.txt` (3 flagged, 10 unflagged, all fine: plain missing or stray
accents/ñ, and ole/olé is one word), every agreed drop (both rounds) and all unflagged keeps. Queried rows are in
each round's `queries.tsv`. Outcomes under the final rules:

**s2-flagged (3):**
- `quite`: stays merge:quitar.
- `joule`: changed to **keep** (the unit; merging into julio would mix it with the month).
- `tejidas`: changed to **merge:tejer**.

I considered and did not query `vigesimosegundo` (agreed drop; written as a word 2 times in 578, so the rule on
ordinals written as digits applies) and `omnium` (mostly the brand Plastic Omnium).

**s2-unflagged (16):**
- Possible second word behind a merge: `inserto`, `lustrar` and `vuelto` became **keep**. `comisar`, `fajar`,
  `piar`, `ámplia` and `alicatar` were upheld (the adjudicator judged the second word a minor share).
- Possible real word behind a drop: `morar`, `diaporama`, `pocito`, `vivar`, `hmmm`, `transmilenio` and
  `paulista` became **keep**; `mensa` became **merge:menso**.

## Changes made by the rerun (old rules → final rules)

- s2-flagged: canyoning drop→keep, cibel pending-names→drop, haka keep→drop, joule drop→keep, namaste drop→keep,
  pisano drop→keep, post-entrenamiento drop→merge:postentrenamiento, voile keep→drop.
- s2-unflagged: formo drop→merge:forma, hahaha drop→merge:jaja, hmmm drop→keep, inserto merge:insertar→keep,
  lustrar merge:lustre→keep, mensa drop→merge:menso, originación drop→keep, rooteado drop→merge:rootear,
  sardinero pending-names→keep, sencillísimo merge:sencillo→keep, siquiatra merge:psiquiatra→keep,
  solita merge:solo→merge:solito, ten merge:tener→drop, transmilenio drop→keep, vivar drop→keep.

## Things to check

- `vuelto` had no examples in the sample, so its keep assumes the remaining forms are the noun *el vuelto*.
- Several of the new keeps (pocito, vivar, sardinero, paulista) rest on "a real common word stays" even though
  90 %+ of the hits are names. The adjudicator asks whether there is a minimum share (see questions).
- `out/` matches a generic `out/` line in `.gitignore`, so I committed the outputs with `git add -f`. I did not
  edit `.gitignore`.
- The lemma `en` (rank 3) is in the flagged queue as `pending` (flag `shape: length 2`). The reviewers kept it.

## `# question` lines

These are the reviewers' and adjudicator's own lines, copied without changes from each round's `questions.txt`.
The adjudicator's grouped questions are at the end of each list.

### s2-flagged
```
# question artemisia: "artemisia" is a variant of "artemisa", but the examples are mostly the Latin genus and a personal name
# question artero: examples show only the brand (Artero combs); kept as the real adjective "artero", but the evidence is thin
# question autism: English spelling of autismo, but the examples are English titles and organisation names, so I dropped it instead of merging.
# question avt: Asociación Víctimas del Terrorismo is well known in Spain but is a private association; treated as an ordinary organisation.
# question avt: it is a nationally known victims' association, but not a public body, so treated as an ordinary organisation
# question añol: no examples; likely a fragment of "español" split in uppercase text, but not clear enough to merge
# question bato: Mexican slang "bato" (guy) is a real word, but the evidence is mostly capitalised/all-caps names and no examples were available; dropped.
# question bato: slang "bato" (Mexican, "guy") versus the name Bato; no examples to confirm, though lowercase "batos" (118) suggests the slang
# question boletus: the Spanish mushroom term is boleto, but "Boletus" appears as the genus name and as a company name; I treated the real-word reading as the minority.
# question bufo: the Spanish adjective bufo/bufa (comic, buffoon) is real, but most occurrences are the toad genus Bufo, so I dropped it
# question bulevard: examples are mostly hotel and shopping-centre names, but the lowercase uses are a misspelling of bulevar, so it was merged
# question bulevard: most examples are proper names (hotel, shopping centre), so drop is also defensible; merged because 28 lowercase uses look like the common noun
# question canyoning: Spanish usually says barranquismo; kept as an established tourism loan, but borderline.
# question canyoning: widely used in Spanish tourism texts, but the rules don't say whether it counts as an established loan; dropped because barranquismo is the Spanish word
# question cesce: state-backed company rather than a ministry or public body; kept as a nationally known institution
# question cibel: Cibeles is a place (fountain and plaza) and may already be on the place list, in which case the merge just joins that entry.
# question cibel: the occurrences are almost all "Cibeles", the Madrid plaza and fountain (a place, dropped), but also the goddess Cibeles (a common noun, possibly merge:Cibeles)
# question cornejo: most occurrences are the surname, but the common noun exists, so I applied the rule that a common word stays.
# question coxsackie: the virus name is a real medical term, but most examples are the place name, so dropped.
# question cubrebotas: an invariable noun, so the real lemma may be cubrebotas itself; merged because the filed spelling "cubrebota" is never written
# question decanter: used for wine decanters and centrifuges in Spanish, but examples are mostly brand or technical
# question ecstasy: examples are titles, but the drug name is a possible established loan (éxtasis)
# question epso: EU recruitment office, not clearly a "famous international body" like ONU or UE; dropped
# question fixture: Mostly English product text in examples, but fixture is established for sports schedules in parts of Latin America.
# question fixture: examples are English product use, but the Río de la Plata Spanish sense is established
# question frob: a Spanish public body, but only moderately famous; kept as a public body people name, could be dropped as minor
# question haka: examples are mostly business names, but the word is established in Spanish sports coverage
# question icaic: is a Cuban state film institute a "famous institution" like RTVE, or an ordinary organisation?
# question iea: IEA is the English form of the International Energy Agency (Spanish AIE); a famous international body would be kept, but the form is English and the examples are unclear
# question iea: the examples are too thin to tell whether it is the energy agency (not a Spanish-named body) or something else; dropped
# question ifrc: a famous international body by the rules, but the Spanish acronym is FICR; dropped as an English-language form
# question ifrc: an international body but not on the rule's example list; kept as a famous international body
# question incoterm: could count as a specialist term (drop) or an established business word (keep)
# question incoterm: established trade term but specialist
# question insarag: a UN-linked international body, but only rescue specialists know it, so I treated it as a technical acronym and dropped it
# question insarag: it is an international UN-backed body, but a specialist one; I treated it as not famous enough to keep.
# question instagramers: it is unclear whether instagramer is established enough in Spanish to be a lemma; if not, drop it instead of merging.
# question jaca: real common word but most occurrences are the town of Jaca; kept under the rule that a real common word stays
# question jaca: the examples are mostly the town, but the word is also a common noun, so I kept it
# question jamboree: scout-event word used in Spanish, but the examples are mostly company and event names, so I dropped it
# question jife: international body but far less famous than ONU/OMS, so keeping it is a judgement call
# question jife: international drug-control body, a famous international body only to a minority of learners; kept under the international-bodies rule
# question joule: Spanish uses both julio and joule, and merging into julio risks mixing it with the month
# question joule: the examples include the surname Joule, and Spanish text may keep "joule" for the unit, so merge:julio is uncertain
# question kettlebells: kettlebell is established in fitness contexts, but Spanish also uses "pesa rusa"; merged to the singular
# question lamela: most occurrences are the surname or place, but the common word lamela is real; kept as the common word
# question lamela: the examples show a place name and a botanical term; kept as a common word, but the evidence is thin
# question lgbtt: could be merged into a listed LGBT lemma as a variant spelling; kept as an ordinary-word acronym
# question lgbtt: kept as an ordinary-use acronym; unclear whether it should merge into a listed lgbt form.
# question machina: "deus ex machina" is the first-half/second-half pattern, but the first halves (deus, ex) are not clearly in this batch; I dropped machina as the second half.
# question majlis: could count as an established loan from Arabic, but it is mostly a proper-noun use, so I dropped it
# question matapalo: real common word, but the examples are mostly the place name Matapalo; kept under the "real word stays" rule
# question mazuelo: a grape variety (Rioja) found mostly in wine-product text; kept as a real common noun, but it could be read as a specialist or brand term
# question mazuelo: kept as a grape-variety common noun, but occurrences are mostly in wine labels
# question meco: could be a real Spanish word (meco, a colloquial term) but the examples are mostly the town and names; dropped.
# question minsa: Peruvian ministry; unclear whether it is nationally famous enough
# question minsa: a Peruvian ministry acronym, famous only in Peru; kept as a national public body
# question neoprene: Spanish writes neopreno; merged on the English-spelling rule, though some examples are brand uses.
# question no-proliferación: could instead be merged into the open spelling "no proliferación"
# question oua: Organización de la Unidad Africana is a famous body but defunct, and the airport-code reading mixes in; dropped
# question oua: the defunct Organización para la Unidad Africana would count as a famous international body, but nearly all occurrences are the airport code
# question paso-a-paso: hyphenated form of the listed phrase "paso a paso"; dropped under the hyphenated-compounds rule rather than merged
# question pay-per-view: hyphenated English compound; kept as an established TV loan, but the rules' "hyphenated compounds of two listed words drop" could apply
# question pay-per-view: hyphenated three-word English loan; kept as an established TV term, though Spanish also says "pago por visión".
# question pisano: a real gentilicio, but the occurrences are mostly surnames, so I dropped it
# question playón: mostly place names (Pueblo Madero, Playón Chico) but also a real common word
# question playón: real Latin American common word, but most examples are place names
# question pochette: French loan for a small bag, but examples mostly brand model names; dropped
# question poppers: established drug-slang loan vs. product name; kept.
# question poppers: established loan or drug-brand term; kept because it is used as a common noun
# question post-entrenamiento: unclear whether the prefix form is a hyphenated compound (drop) or an adapted spelling of "postentrenamiento" (merge)
# question post-sinodal: the academy's form postsinodal is assumed, but hyphenated forms may be intended to stay as written
# question post-tratamiento: Spanish writes the prefix variously (postratamiento, post-tratamiento, postratamiento); the merge target is a best guess.
# question post-tratamiento: the academy writes postratamiento, but it is unclear whether that form is listed or the hyphenated form should simply drop
# question pre-final: prefinal is not clearly listed; merged as the obvious unhyphenated form.
# question proporcionada: participle could go to proporcionado or proporcionar; chose the verb.
# question qibla: the academy forms (alquibla/quibla) are my best guess for the right lemma.
# question quizzes: "quiz" is used in Spanish, but these examples are English or product context, so dropped rather than merged into quiz.
# question retamar: Real RAE word (retamar, a place of retama bushes) but most examples are a place or surname; kept under the common-word rule.
# question retamar: a place and surname name mostly, but also a real common word (retamar, retamares); kept under the common-word rule
# question sabbat: Spanish does use "sabbat", but the examples are many religious and neo-pagan uses; kept as an established loan
# question sabbat: Spanish usually writes sabat or sábado for the Jewish Sabbath, so this could be a merge; the examples are mixed, so I kept it as an established spelling.
# question sambo: martial-art sense is real, but many examples are place names
# question satsuma: also a fruit (mandarina satsuma), but the examples are all the Japanese domain, so I dropped it
# question secofi: Defunct Mexican ministry, so it is unclear whether it still counts as a famous public body.
# question secofi: a defunct Mexican ministry (now Secretaría de Economía), so it is unclear whether it is still famous enough to keep
# question semi-profesional: the academy writes semiprofesional (one word); I assumed that is the form on the list
# question silonita: a lowercase demonym that is a real Spanish word, but it occurs only in biblical text; kept out as too rare for a learner
# question silonita: a real demonym but only in biblical text; dropped as a name.
# question sras: it is mostly SARS, but it is also an abbreviation of "señoras" (Sras.), and I kept it as the majority reading
# question sriracha: could count as a foreign brand name, but kept as an established sauce name.
# question sriracha: sauce name, brand origin but generic usage; kept as an established loan
# question stepper: the loan is common in Spanish fitness vocabulary, but whether it counts as established is unclear
# question stop-motion: hyphenated loan; could instead merge into "stop motion" if that is the listed spelling
# question sub-páginas: merged into subpágina, which may not be a listed lemma; drop is the alternative under the hyphenated-compound rule
# question titi: no examples were shown, and most uses are likely names; kept as a real Spanish word.
# question tonka: 41% capitalised, but the examples show "haba tonka" as a common ingredient; kept
# question tonka: also a toy brand, but the majority of examples are the haba tonka ingredient
# question trans: Spanish adjective and noun (persona trans) but also a prefix or fragment in the examples; kept as the real-word reading, though the evidence is thin
# question uanl: counted as a famous university by name, but it is regional rather than national like UNAM
# question ucv: could be Universidad Central de Venezuela (a famous institution), but examples show a Spanish university and a file extension, so I dropped it
# question ufm: Universidad Francisco Marroquín is well known in Guatemala but probably not nationally famous across the Spanish-speaking world, so dropped
# question unitar: UN institute, not obviously as famous as ONU or Unesco; dropped as not clearly on the list of famous international bodies
# question unitar: UN-affiliated body, but not famous enough to count as a famous international body; dropped
# question videowall: technical loan, unclear whether learners need it
# question voile: the French fabric term is used in Spanish textiles, but the examples are mostly from translated catalogues
# question yankee: the English spelling could merge into "yanqui", but the examples are almost all names (Daddy Yankee, the Yankees), so I dropped it
# question canyoning: should a loan that Spanish text really uses but that has a standard native equivalent (barranquismo) stay, or drop in favour of the native word?
# question joule: when an English unit spelling's adapted Spanish form is a homograph (julio, the month), should it be kept separately as here, or merged anyway?
# question pending-names: the answer format allows this decision, but the rules never define it, so it was not used.
# question quite: should a lemma that is a real but rarer noun (quite, "estar al quite") still merge into the verb when nearly all its occurrences are verb forms?
# question tejidas, proporcionada: should participial adjectives merge into the verb (applied here) or into a -do adjective lemma?
```

### s2-unflagged
```
# question acrilamida: borderline specialist chemical term; kept because it is well known from food-safety news
# question acrilamida: the rules say nothing about chemical terms; I kept it as a news-familiar word, and dropped dihidrotestosterona and propranolol as too specialist.
# question aqueste: archaic demonstrative that is a real Spanish word, but the rules do not say whether archaic forms are wanted by a learner
# question aqueste: it is archaic, but pronouns and determiners stay under the rules, so I kept it
# question aramida: borderline between everyday word and technical material term; kept because it is a standard Spanish noun
# question arpegiar: most forms are the noun arpegio, which is not a form of the verb; I kept the verb and arpegio may need its own entry.
# question atendimiento: it is used in Latin American Spanish but is not clearly a misspelling or a standard lemma; dropped rather than merged into atención
# question atendimiento: nonstandard or Portuguese-influenced; merge:atención may be preferable
# question avanafil: generic drug names (diazepam kept, avanafil and escitalopram dropped) are not clearly covered; I kept only the well-known one
# question bandeau: French fashion loan; kept because "bikini bandeau" is common in Spanish shopping text, but how established it is for a learner is unclear.
# question bandeau: French swimwear term used in Spanish fashion text; unclear if established enough to keep
# question barbechar: it is a real verb, but the evidence is almost entirely the noun barbecho; merged assuming barbecho is the intended learner entry.
# question bootloader: not sure whether it is established enough among computer users to count as a loan; dropped as specialist.
# question bootloader: technical loan, could count as specialist vocabulary; kept as common among phone users
# question brahmana: could merge into brahmán, but the examples are Sanskrit-religious text, so I dropped it
# question cacito: dialectal diminutive (of cazo) seen mainly in supplement text; kept as a real word.
# question cacito: diminutive of cazo/cacillo? Kept as the form actually used for protein-powder scoops
# question catarí: qatarí is the other common spelling; kept since catarí is the form written here
# question citalopram: generic drug names are not clearly covered; I kept both citalopram and tadalafilo
# question citalopram: generic drug names are not covered by the rules; kept as ordinary words, along with tadalafilo
# question cobot: technical loan, kept because it appears in general news; could be seen as specialist
# question colestipol: generic drug names are not covered by the rules, since they are neither brand names nor acronyms
# question colestipol: it is a generic drug name, not a brand, so the rules don't settle whether it counts as specialist vocabulary
# question collpa: Quechua loan used in Peruvian Spanish for clay licks; I judged it not established enough for the list
# question collpa: Quechua-origin word used in Peruvian Spanish for clay licks; unclear whether it counts as established regional Spanish or a specialist term.
# question comboniana: I dropped it as a minor religious order name, though comboniano could be a merge target.
# question comprehensivo: often an anglicism (comprehensive), but it is in the RAE; kept.
# question consellera: Catalan title used in Spanish press; kept as established usage, could be read as a foreign word or title
# question consellera: Catalan word, but used as a title in Spanish-language press
# question consellería: Galician/Valencian term; I kept it as a regional-body name used in Spanish texts
# question crawlers: the singular "crawler" might count as an established web loan; I dropped it as specialist.
# question cropped: fashion term common in Spanish retail text; unclear if established enough
# question culotte: Spanish also has culote; I kept culotte because that is the form people write for the cycling garment.
# question culotte: the RAE lists culote, but the cycling sense is often written culotte, so keep may also be defensible
# question cusqueña: feminine adjective form as lemma; I merged to cusqueño, but it could stay as a gentilic with its own feminine entry
# question cusqueña: the rules do not say whether a gentilic adjective's feminine form should merge into the masculine; I merged it to cusqueño, as with antineumocócica.
# question cyberbullying: English spelling might instead merge into an adapted form such as ciberbullying; kept as the established loan
# question cyberbullying: English spelling of a concept Spanish also writes as "ciberacoso"; kept as an established loan, not merged.
# question deriva: noun "deriva" and verb form of derivar share one surface; I kept it as the noun.
# question desasociar: DLE lacks it and disociar is a different sense, but it is widely used in tech Spanish; kept rather than merged
# question diazepam: generic drug names are not covered by the rules; kept as widely known, unlike avanafil and escitalopram which I dropped as specialist.
# question domótico: domótica is the main form; I kept the masculine adjective as its own entry.
# question domótico: the noun domótica dominates; I kept domótico as a real lemma rather than merging
# question doping: doping is widely used in Spanish, and the rules don't say whether to merge it into dopaje or keep it as an established loan
# question electrochapado: specialist term; kept as a real word, though it is only used in industrial text
# question escitalopram: same drug-name issue as avanafil
# question estimado: "Estimado" is mostly the letter salutation; merged into estimar per participle rule, but a learner may want the greeting kept as an adjective
# question estimado: tagged VERB and mostly the salutation "Estimado"; I kept it as an adjective rather than merging into estimar.
# question film: it could merge into filme as an adapted spelling, but film/films are established and widely written, so I kept it.
# question formo: the form could be merge:formar, but "forma" and capitalised "Formo" make it unclear
# question formo: the forms are mostly forma, which could be noun or verb; merged to forma but formar is possible
# question frambueso: forms are mostly frambuesa, which probably has its own entry; kept as the separate real word
# question gesso: Italian-origin craft term; kept as established because the Spanish text uses it consistently
# question gesso: Italian-origin craft term; kept because the examples use it as an ordinary Spanish noun
# question hahaha: laugh interjection; merged to jaja assuming that is the listed form
# question heurística: mostly used as an adjective, so merge:heurístico could also be argued; kept because heurística is a real noun
# question heurística: tagged ADJ and examples are adjectival, but heurística is also a real noun with its own entry; kept rather than merged into heurístico
# question hist: could be an abbreviation of historia, histórico or a medical prefix; no examples, so dropped
# question horcajada: the singular is a real noun but nearly all occurrences are "a horcajadas"; I chose the plural-only lemma horcajadas.
# question impeledor: rare technical calque; dropped, but merge:impulsor is possible
# question impeledor: rare variant of impulsor used in Latin American pump/engineering texts
# question izakaya: Japanese loan with frequent use in Spanish restaurant text; unclear if established enough
# question izar: "Ice" (English) is the largest form, but the verb izar is real and common in nautical use, so I kept it.
# question jjoo: abbreviation of a multi-word phrase with no single lemma to merge into; kept as an ordinary-use acronym
# question jjoo: could be kept as an ordinary-word acronym for Juegos Olímpicos; I dropped it as an abbreviation with no single lemma
# question kombu: niche food loan; kept as established in Spanish cooking text
# question limeño: demonyms are not covered explicitly by the place-name rule; kept as common adjectives (same for bernés, ghanés).
# question limeño: the rules say place names drop but don't settle gentilics; I kept limeño, bernés and ghanés as ordinary adjectives
# question lorquino: demonym of Lorca; the rules cover place names but not demonyms
# question lorquino: demonyms from place names are not covered by the rules; kept as an ordinary adjective
# question machar: maché occurs only in "papel maché", where papel is a separate word; I merged to maché, but drop is possible
# question malfuncionamiento: the screener called it nonstandard, but it is attested in Latin American Spanish, so I kept it rather than merging.
# question malfuncionamiento: the standard spelling may be "mal funcionamiento", but the one-word form is attested, so I kept it
# question manzanar: most occurrences are the place name Manzanares; I kept it under the common-word rule
# question mediopié: rare compound, kept as a real technical word
# question morar: it is a real verb, but most counts are English "more" or the colour morado/mora, so only about 1,476 occurrences are the verb. I dropped it, but morar itself might deserve a clean entry.
# question multibrazo: compound used only in the suspension sense; kept as an established technical term.
# question multiestación: rare technical compound; kept as a real noun
# question multilenguaje: could be kept as a software term; I judged it a dubious compound
# question niñxs: inclusive-x spelling could instead merge into niño; I dropped it as non-standard orthography
# question niñxs: inclusive-x spelling is not covered by the rules; merged into niño, but drop is arguable
# question originación: calque not in the dictionary, kept as an established finance term
# question originación: used in Spanish banking but looks like an English calque, so I dropped it
# question palier: a French-origin technical loan; I kept it as established in Spanish vehicle parts text, but it is borderline.
# question paulista: it is a real demonym, but the examples are mostly place and hotel names, so I dropped it.
# question pelet: the form to merge into is unclear (pélet, pellet); people also write pellet
# question piar: the cluster mixes pie, piara, pío and piar; I merged it into pie because pié/píe make up most of it.
# question pinto: most occurrences are the surname Pintos, but the common adjective is real, so I kept it
# question pipo: pipo may be a real colloquial word, but the examples are almost all names and a brand
# question propranolol: drug names are not covered by the rules; dropped as specialist vocabulary
# question qubits: the singular qubit may not be on the list, so the merge assumes it is a loan Spanish uses
# question registrante: not in the academy dictionary but common in Latin American legal and domain texts; kept
# question respondedor: mostly a calque of "first responder" and "non-responder"; kept as a regular Spanish formation
# question rooteado: merged to rootear, but the slang verb may not be wanted by learners
# question ruidera: real common word, but nearly all examples are the place Ruidera (Lagunas de Ruidera)
# question ruidera: the place name Ruidera dominates the examples, but ruidera is also a real Spanish common word, so I kept it under the common-word rule
# question sabana: many occurrences are an unaccented misspelling of sábanas or the place name Sabana; kept as the common word savanna
# question sabana: mixes sabana (savanna), the place name Sabana, and sábana misspelt without the accent; I kept it as the real word.
# question secoya: tree sense (secuoya variant) dominates, but the ethnonym also occurs; kept as the common word
# question sencillísimo: the rules don't settle whether a superlative form should merge into the base adjective or stay
# question sendo: the rules do not say whether to merge a plural-only form filed under a singular lemma into the plural lemma; merged into sendos
# question sicólogo: accepted variant of psicólogo; kept as the form people write
# question significantemente: rare non-standard adverb; merged to significativamente instead of keeping it as a real word
# question siquiatra: the rules treat the spelling as an accepted variant, not a misspelling, so I kept it instead of merging into psiquiatra
# question slipper: majority of occurrences are the shoe sense, but capitalised "Slipper" (66) may be product or proper-name uses; kept as an established fashion loan.
# question slipper: mix of footwear usage and a title ("Spur and Slipper"); kept as an established fashion loan, but borderline
# question snowpark: loan used in the ski sector; kept as an established loan, but it may be too niche.
# question snowpark: possibly an established ski loan; dropped as a niche English compound
# question squat: the Spanish word is sentadilla, but "squat" is common in gym Spanish; I kept it.
# question subartículo: real prefixed noun, but only in legal and technical text; dropped as specialist.
# question subtel: Chilean body, so I treated it as a nationally famous public institution; it could instead count as a minor organisation acronym
# question subtel: a Chilean body, so "nationally famous" is arguable, and some examples are product spam; kept as a public body.
# question temanita: a real gentilic, but it is biblical and obscure; I dropped it as a name or title.
# question temanita: biblical gentilic, kept as a common noun though it appears in religious text only
# question ten: could be voseo tenes of tener, but the examples point mostly to the river Tenes
# question texano: texano is an accepted variant of tejano; I kept it rather than merging because it is not broken.
# question tipster: a betting loan of modest establishment; I kept it, but it could be argued as unestablished English.
# question trasferencia: the academy accepts it, so I kept it, but it could be merged into transferencia.
# question ultimar: most surface forms are "ultimas" (missing accent for últimas); I kept the real verb lemma instead of merging to última
# question vacación: it could be merged into vacaciones, but singular use is real, so I kept it.
# question vouchers: merged into voucher, but it is unclear whether voucher itself is established enough for a learner list
# question vouchers: voucher is a travel-trade loan; I judged it established enough to keep, but it is borderline
# question wallets: crypto-context loan, borderline between an established loan and an unestablished foreign word
# question webapp: Spanish usually writes "aplicación web", so it is unclear whether it is established enough to keep
# question aqueste, temanita: should archaic or biblical-only words drop even when they are real Spanish words?
# question hmmm, hahaha: should spelling variants of sounds (hmmm/hmm/mmm, hahaha/jajaja) merge into one canonical interjection, and which forms are listed?
# question inserto, lustrar, alicatar: when a cluster mixes two real words, each with a real share, there is no split decision; I kept the lemma when its own reading is a learner word, otherwise merged to the majority. Should these be split?
# question machar: should "papel maché" become its own entry, given that papel is a real word that occurs alone?
# question niñxs: should inclusive spellings (-x, -e, -@) merge into the standard lemma or drop as non-standard?
# question paulista, sardinero, vivar, pocito: rare common words, gentilics and diminutives whose occurrences are 90%+ names were kept by the "real common word stays" rule. Is there a minimum share of the real reading below which they drop, and are diminutives wanted as separate entries?
# question transmilenio: do city-level public transit systems (TransMilenio, Metro de Madrid) count as famous public bodies under the institutions rule?
# question vacación, trasferencia: should accepted variants of an already-listed word (singular of a plural-only noun, tras-/trans- spellings) always merge into the dominant form?
# question vuelto: no examples in the sample, so the share of the noun (change) versus the participle is unverified.
```
