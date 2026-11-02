# es review shard 6: report

Base `c4aacac` (`origin/full-es`), runner uplift `f8c8a67` with `review/scripts/examples10.py`, rules
`review/rules/es-flagged-final.md` and `es-unflagged-final.md`. Reviewers and adjudicator used those rules through
`--rules`; both adjudications were rerun on the corrected commands in `f117a3a` (see below). Screeners and reviewers
ran on the sonnet alias and the adjudicator on the opus alias, as the config sets. No step had failed calls or
failed batches.

## Counts

| step | count |
|---|---|
| flagged queue (`pending`) | 944 |
| flagged with examples | 826 (87.5 %) |
| unflagged screened | 4,974 (20 batches, 0 failed) |
| screen candidates | 966 (690 named by both screeners) |
| suspects with examples | 847 (87.7 %) |

| round | lemmas | reviewers agreed | to adjudicator (disagreements + queries) | keep | drop | merge | pending-names |
|---|---|---|---|---|---|---|---|
| s6-flagged | 944 | 919 (910 after queries) | 34 (25 + 9) | 82 | 779 | 83 | 0 |
| s6-unflagged | 966 | 924 (903 after queries) | 63 (42 + 21) | 506 | 240 | 220 | 0 |

Undecided: 0 in both rounds. Accent-only agreed merges: 5 (flagged), 13 (unflagged).

## Gate: my queries and outcomes

I read every agreed merge and keep in both rounds and every agreed drop lemma, then queried the decisions that might
hide a second real word, a missing-accent word or a misspelling. The outcomes below are from the final adjudication
under the final rules.

**s6-flagged (9)**
- `diagnostico` (merge:diagnóstico; also yo diagnostico): merge stands.
- `decima` (merge:décima; also a verb form): merge stands.
- `sangr` (merge:sangría; could be sangre/sangrar): merge stands.
- `pio` (merge:pío; mostly the name): merge stands.
- `satan` (drop; missing-accent Satán?): drop stands.
- `prez` (drop; prez/preces are real words): **changed to keep**.
- `mistica` (drop; missing-accent mística?): **changed to merge:mística**.
- `ffaa` (keep; abbreviation of fuerzas armadas, merge?): keep stands.
- `glbt` (keep; variant of LGBT): **changed to merge:LGBT**.

**s6-unflagged (21)**
- Noun-form merges that absorb a real verb or word: `mediar` **changed to keep**; the `pontificar`, `almidonar`,
  `sisar`, `trovar` and `maño` merges stand.
- Agreed keeps:
  - `transtorno` **changed to merge:trastorno**.
  - `eternalmente` **changed to merge:eternamente**.
  - `xacobeo` **changed to drop**.
  - `trasparencia`, `reusar` and `purina` stay keep.
- Agreed drops:
  - `sitar`, `capar` and `avocar` **changed to keep**.
  - `vertir` **changed to merge:verter**.
  - `tambi` **changed to merge:también**.
  - `agio`, `trigésimo`, `decimoctavo` and `vigesimoctavo` stay drop. The ordinals' counted forms are all digits, and
    the adjudicator asked about this.

## Things to know

- **The adjudication was rerun.** The first adjudication of both rounds ran without `--rules` (the step-3 commands
  before `f117a3a`), so the adjudicator saw the config's older uplift rules (`prompts/es/rules-*.md`). That is why
  it gave `aliaga` a `pending-names` decision. On the coordinator's instruction I set the first adjudication aside
  and reran both with `--rules`. The reviewer stage already had the final rules and was not rerun.
- **24 decisions changed between the two adjudications**, all of them lemmas the adjudicator saw.
  - s6-flagged (11, old → new):
    - aliaga: pending-names → keep
    - hibiscus: merge:hibisco → drop
    - maitre: merge:maître → drop
    - millo: drop → keep
    - mistica: drop → merge:mística
    - multiplicao: merge:multiplicar → merge:multiplicarse
    - prez: drop → keep
    - satan: merge:satán → drop
    - sci-fi: keep → drop
    - tato: drop → keep
    - tragus: drop → merge:trago
  - s6-unflagged (13, old → new):
    - asóciese: merge:asociar → merge:asociarse
    - boolean: drop → merge:booleano
    - choker: keep → drop
    - comuníquense: merge:comunicar → merge:comunicarse
    - gurdo: drop → merge:gurda
    - imaginaos: merge:imaginar → merge:imaginarse
    - inserir: merge:insertar → drop
    - intarsia: drop → keep
    - mesar: drop → keep
    - proclama: merge:proclamar → keep
    - shells: drop → merge:shell
    - tambi: drop → merge:también
    - trasparencia: merge:transparencia → keep
  - Only some of these follow from the rules text: the old rules had `pending-names`, and the final rules' Spellings
    and Split loans paragraphs are new. Others (satan, prez, tato, trasparencia, choker) look like run-to-run variance
    on borderline cases. You may want to spot-check them. The first adjudication isn't committed; it's kept on the
    shard machine.
- Two of my queries cited a rule loosely:
  - The `pio` query mentioned a "minority rule". The binding minority rule covers only non-Spanish tokens.
  - The `ffaa` query said "an abbreviation of a listed word merges". The rules list that as a case of a broken
    lemma, but the adjudicator kept FFAA as an acronym used as a word.
  The decisions are the adjudicator's.
- `full/es/review/shards/shard-6/out/` matches the repo's `.gitignore` line `out/`, so I force-added it as the shard
  file asks.
- I ran the flagged reviewers and the unflagged screen at the same time. The worker restarted once, after the
  unflagged reviewers had finished, and nothing was lost.
- Recurring question themes, which probably need one ruling each:
  - Mixed lemmas that hold two real words (mediar/mediados, tato/tata, millo/milla).
  - Whether -ísimo superlatives get their own lemma.
  - Pronominal -se in merge targets (the two adjudications disagreed on asociar/asociarse and similar).
  - Ordinals that are words but are counted only as digits.
  - How established a jargon or fandom loan must be.
  - Real words whose counts are inflated by English homographs (capar, avocar, sitar, mugir).

## Question lines

All `# question` lines (reviewers, and the final adjudication) are in `s6-flagged/questions.txt` (132 lines) and
`s6-unflagged/questions.txt` (159 lines). They're reproduced in full below.

### s6-flagged
# question aire-acondicionado: it is a hyphenated compound of two listed words (which would drop), but I merged it into the one-noun entry "aire acondicionado".
# question aire-acondicionado: the rule drops hyphenated compounds, but the unhyphenated phrase aire acondicionado is a common noun a learner would want.
# question aliaga: a real Spanish plant name, but the sample is mostly the place name and a surname; I kept it as a common word.
# question ampersand: English-looking and examples are mostly cake toppers and company names, but Spanish does use the loan for the symbol.
# question anticiparno: "anticiparnos" could be anticipar + nos or reflexive anticiparse; I chose anticiparse.
# question arra: "arras" is Spanish, but ARRA (91 uses) is probably a US-law acronym, so the merge covers only part of the evidence
# question aupair: could be treated as a split loan or a spelling merge; both give "au pair".
# question auto-renovación: the academy prefers autorrenovación, but it is rare, so the merge target is a judgement call.
# question bacopa: a plant name that is a real Spanish word, but most examples are supplements and aquarium plants
# question basset: it is capitalised as a breed name in most hits, but it is used in Spanish as a common noun for the breed
# question basándonos: the lemma is a conjugated form; I merged it into basarse as the likely pronominal lemma, but basar could also be argued.
# question bbdd: "base de datos" is a phrase, so merging into it may not fit the lemma conventions; drop is the alternative.
# question bidegorri: it is a real Basque-Spanish word for a cycle lane, but the examples are mostly a shop name, so I dropped it.
# question bodies: examples mix the Spanish baby-clothing plural (bodies → body) with the English exhibition title "Human Bodies"; I merged on the assumption that the Spanish use is the majority
# question bodies: the examples mix the Spanish clothing sense with English titles; I treated the clothing sense as the real word
# question carina: mostly person and place names, but kept as a real common word.
# question cerrito: often a place name (El Cerrito, Cerritos), but it is also a real diminutive, so I kept it.
# question coam: it is a regional professional body, so I treated it as an ordinary organisation rather than a famous institution
# question compressor: English spelling of compresor, but the examples are English product names, so dropped rather than merged
# question conicyt: it is a national public body, but known mainly in Chile, so whether it counts as nationally famous is unclear
# question conicyt: it is nationally famous in Chile, but the other uses (Nicaragua) are marginal
# question controlling: an English loan used in Spanish business, but possibly only specialist jargon; I kept it.
# question controlling: an English-origin business term; it is unclear whether it is established enough in Spanish
# question cplp: Community of Portuguese Language Countries could count as a famous international body, but it is little known in Spanish
# question cplp: it is an international body, but a lusophone one that is rarely referred to in Spanish, so the "famous international bodies" rule may not cover it
# question decima: examples are mixed between décima and a Decima MAS proper name; I chose the common word.
# question decima: examples show only the name "Decima MAS", but lowercase decima/decimas plausibly stand for décima(s), so I merged it.
# question e-wallet: may be an established loan in fintech Spanish; judged not established enough
# question egb: Spanish school-level acronym many learners may meet, but examples are mixed with other uses, so dropped
# question egb: examples are mixed (file extension, strep B, schooling); kept on the strength of the Spanish education meaning
# question enfocándono: the examples show "enfocándonos en", so I chose the pronominal enfocarse; plain enfocar is arguable.
# question euskaldún: most occurrences are the Euskalduna palace, but the word is a real Spanish adjective, so I kept it
# question fenix: most examples are business names, but the spelling is a plain missing accent of fénix, so I merged it.
# question fluo: mostly a brand fragment ("LV Fluo"), but the colloquial abbreviation of fluorescente is real, so I merged it.
# question frac: the lowercase "frac" could be the Spanish garment or an abbreviation, and no examples were available to check
# question full-hd: "Full HD" is an established tech term, but the hyphenated shape dropped it; a merge into "full HD" was not obvious.
# question ganoderma: the fungus genus is a real term, but the uses seen are product and brand names
# question glbt: a variant spelling of LGBT; kept as an ordinary acronym rather than merged into LGBT.
# question glbt: it is a variant of LGBT, which is probably its own entry; I kept it as an ordinary acronym.
# question gueshe: a Buddhist title (like lama) used in Spanish texts; I treated it as a title and dropped it.
# question gueshe: a Spanish-adapted spelling of a Tibetan Buddhist teacher title, but it is mostly used inside a person's name, so it was dropped as a title or name
# question guijo: a real common word, but nearly all examples are place names (El Guijo, Guijo de Ávila); I applied the common-word rule.
# question guijo: the examples are almost all place names, but guijo is a real common word, so I kept it
# question handball: kept as a regional loan, though balonmano is the standard Spanish word.
# question hech: no examples shown; assumed the Biblical abbreviation "Hech." for Hechos, merged into hecho
# question hech: probably the abbreviation of Hechos (Bible book), but merging to a lemma is not obvious
# question hibiscus: unclear whether the Latin genus name or hotel names dominate, so the merge to hibisco is uncertain
# question hitn: Spanish-language US broadcaster rather than a Spanish-world national body; dropped as an ordinary organisation.
# question igic: regional (Canary Islands) tax acronym; treated as an ordinary-word acronym like IVA, but it is less nationally known
# question inia: public research body in several countries, but not clearly nationally famous, so dropped
# question ipbes: an international intergovernmental body, but a specialist one; unclear whether it counts as "famous international body"
# question jatropha: Spanish has jatrofa, but the examples are mostly Latin or English usage, so I dropped it
# question jokers: joker is only marginally established in Spanish; merged to singular rather than dropped
# question kasbah: casba is the Spanish form, but the examples are almost all hotel and place names, so I dropped it rather than merged it.
# question lacar: Capitalised usage is mostly the Lago Lacar place name, but lacar is a real verb with lowercase and inflected forms, so I kept it under the common-word rule.
# question laso: "laso" is a rare real Spanish adjective, but the examples are surnames and a "lasso" tool; I dropped it as mostly a name.
# question laso: majority of occurrences are a surname or the English "lasso" tool, but laso is a real Spanish adjective.
# question luengo: most occurrences are the surname, but luengo/luenga is a real archaic Spanish adjective
# question luengo: the surname reading dominates, but the archaic adjective is real Spanish, so I kept it under the common-word rule.
# question mahjongg: assumed "mahjong" is the established Spanish spelling; the academy also lists "mahjong", so confirm the target form.
# question maitre: "maître" as a restaurant term is Spanish, but most examples are a French name or title; I merged it to the accented form.
# question millo: millo is a real Spanish word (sorghum or maize), but the counted forms are mostly the name Millo and milla; I dropped it and the examples are missing.
# question millo: mostly written as a name (Millo 116 of 168), no examples; kept as a real regional word, but milla (38) is mixed in.
# question minusma: it is a UN mission, which could count as an international body, but I judged it specialist.
# question mistica: it could be a missing-accent form of "mística", but the evidence is mostly the MISTICA project name; I dropped it.
# question mol: mol is a real unit, but it is filed with mola and the MOL company, so it might be better split than dropped.
# question multi-idioma: the rules don't say whether a hyphenated prefix compound merges into a solid spelling or is simply dropped; merged to multiidioma
# question multi-idioma: the rules don't say whether a hyphenated prefix compound merges into its solid spelling or drops as a hyphenated compound; I merged it.
# question multiroom: it could count as an established tech loan, but the evidence is mostly product names
# question multiroom: possibly an established loan in audio/tech, but examples are mostly product names
# question ninjutsu: a Japanese martial-arts term used in Spanish for anime and games; unclear whether it counts as an established loan.
# question ninjutsu: a martial-art loan mostly from anime and games; it is unclear whether it counts as established in Spanish.
# question noma: mixed readings (brand NoMa/Noma, "nomas" as "no más"), and no examples were given
# question noma: the Spanish "nomás" reading is a minority of the occurrences, so I dropped it, though the lemma could be filed under "nomás" instead
# question oif: not on the rule's example list of international bodies, but similar in standing to AIEA, so kept
# question oif: the rules do not say whether this is a famous international body like ONU or a minor organisation; I decided it is minor and dropped it
# question onboard: "cámaras onboard" is used in Spanish motorsport commentary, but I judged it not established enough to keep.
# question onboard: the examples mix the motorsport loan with the English "onboard" in hardware text; I kept it.
# question pcus: the Soviet Communist Party is a famous body, but not one of the Spanish-speaking institutions the rules list as kept.
# question pcus: the Soviet Communist Party is neither a place nor a famous Spanish-world institution, so I treated it as an ordinary organisation.
# question pio: mostly the name Pio/PIO, but pío is a real word, so I merged it.
# question pio: the real word pío is rare here and most uses are names (Pio XII and the like); merged by the missing-accent rule.
# question piracetam: a generic drug name is not clearly covered by the rules; kept as an ordinary medical noun
# question post-secundaria: no clear single listed lemma; merged to the solid prefix form "postsecundaria", but drop is defensible if that form isn't on the list.
# question practicum: Spanish writes prácticum, but the examples are mostly the unaccented form and some are the Practicum Script brand name.
# question pre-kinder: Chilean usage; the established spelling (prekinder vs prekínder) is unsettled, so I chose prekínder.
# question pre-kinder: Merged into the unhyphenated Latin American form prekínder; the accent and spelling may need checking against how the list writes it.
# question prez: "prez" and "preces" are mixed under one lemma; the name reading dominates, so I dropped it, though preces (plural of "prez") could be a separate entry.
# question quidditch: fictional proper noun, but it works as a common noun for the sport in Spanish text
# question quidditch: fictional sport from a book; kept as a common noun, but it could be read as a title/event
# question rgdp: merging into RGPD assumes RGPD counts as an acronym used as an ordinary word in Spanish
# question rollerball: pen type, possibly an established loan in Spanish product text, but examples are mostly brand listings; dropped.
# question ruc: RUC is a tax-ID term in Peru/Ecuador, but there are no examples to confirm the reading
# question ruc: no examples were shown. I kept it as an ordinary tax-registry term, but it could be seen as a technical acronym.
# question sci-fi: could instead be kept as an established loan; I treated it as an abbreviation of ciencia ficción
# question sci-fi: it is an established English abbreviation, but Spanish writes "ciencia ficción", so I dropped it instead of merging.
# question sebin: it is a national intelligence service, not an obviously "famous institution" like those listed, so I treated it as a public body
# question shoji: mixed between the common word (screen) and a person's name, but the common reading may be a minority
# question shonen: manga term used by Spanish fans; unclear whether it is established enough for a general learner list
# question shonen: manga-fan loan, could count as established; judged too niche
# question shoppers: "personal shopper" is used in Spanish, but the examples are mixed and the lemma is a plural English form
# question sigatoka: "sigatoka negra" is a Spanish banana-disease term, but it is specialist and the word is also a Fiji place name.
# question sorrentino: "sorrentinos" (Argentine pasta) is a real common noun, but only about 13% of uses, so I dropped it as a surname.
# question taichi: Spanish usually writes "tai chi" or "taichí"; I kept the one-token form as written by people.
# question taichi: Spanish usually writes "tai chi" or "taichí"; kept as written.
# question tato: mostly a pet or person name, but the real word tata (nanny) is present, so merged
# question terminals: could be merge:terminal as an English plural, but most uses are the company name APM Terminals; I dropped it.
# question timeout: established computing loan, but the examples are technical and Spanish also has "tiempo muerto"; kept.
# question timeout: mostly computing contexts; kept as an established loan (sports "tiempo muerto" sense too)
# question toxoplasma: it is a genus name, but the examples use it as an ordinary Spanish noun for the parasite, so I kept it.
# question tragus: most examples are English jewellery listings; merged to trago on the assumption that the anatomical reading is the real word
# question tragus: the Spanish word is trago, but the examples are all piercing-product English, so I dropped it
# question técnico-científico: a real adjective, but I applied the hyphenated-compound drop rule.
# question unifem: the body was folded into ONU Mujeres in 2011; I kept it as a famous international body.
# question unirno: the examples read as the pronominal verb, so I merged to unirse rather than unir.
# question vtc: Spanish "VTC" (vehículo de transporte con conductor) is an ordinary word, but most examples are machine models, so dropped
# question vtc: it is a real Spanish term for ride-hailing cars, but the examples are mostly machine models, so dropped
# question warez: it could count as an established jargon loan, but I judged it not established in Spanish
# question ylang-ylang: it is a hyphenated loan, so I kept it as established, though the academy writes ilang-ilang.
# question óblast: a common noun in Spanish, but the examples are mostly place names; kept as the common word.
# question ffaa, sci-fi: the queries assume "an abbreviation of a listed word merges", but the binding rules have no such rule; can merge targets be multiword lemmas (fuerzas armadas, ciencia ficción)?
# question lacar: when a real common word shares its spelling with a frequent place name, should its rank be corrected for the place-name occurrences, or kept as counted?
# question pio: the query cites a "minority rule" that is not in the binding rules; is there a threshold below which the common-word reading of a name-dominated lemma drops?
# question post-consumo: should prefixed words be merged to the RAE-preferred pos- form (posconsumo) or to the post- form common in Latin American usage (postconsumo)?
# question satan: are religious and figurative names that act as words (Satán, Satanás) kept, or dropped as personal names?
# question sci-fi, shonen, onboard: how established must a fandom or jargon loan be to count as established?
# question tato, millo, prez, laso: these junk lemmas also hold forms of a different real word (tata, milla, preces, lasa); should those forms be moved to their own lemma when this one is dropped?
# question ffaa: should abbreviations of institutions merge into a multi-word expansion (fuerzas armadas), or stay as acronyms like ONU?
# question glbt: should variant-order acronyms (GLBT, LGTB) merge into one form, and which form is canonical, LGBT or Spain's LGTB?
# question millo, prez, tato: a second real word's forms are filed under the lemma (milla, preces, tata); should those forms be split out to their own lemmas rather than staying here?
# question post-consumo: both posconsumo and postconsumo are widely written; should the list prefer the academy's pos- form or the more frequent web form for pos(t)- prefixes?
# question tragus: when Spanish uses the Latin form for a specialist sense (the tragus piercing), should it merge into the native word (trago) or drop as specialist?

### s6-unflagged
# question abajar: dialectal/dated verb, kept since it is a real entry; no examples to check
# question adobar: the forms are mostly adobe (the material, plus the Adobe brand) and adobo, which are separate nouns; I kept the real verb lemma
# question agregado: it is also a real noun (attaché) and adjective, but the examples are mostly the participle used in web artefacts such as "Agregado el…", so I merged it
# question airfryer: it is a Philips brand name but is used generically; I kept it.
# question airfryer: it is a Philips trademark, but it may also be a generic loan for freidora de aire; I dropped it because most examples are brand use.
# question alar: alar is a real adjective, but about 85% of the forms are alado, so I merged it.
# question alar: also a real adjective and verb (alar), but alado forms dominate; merged into alado
# question amalecita: biblical gentilic; kept as a common noun, not a place or person name
# question autofoco: unclear whether it is established enough versus autoenfoque; kept
# question autofoto: a rare coinage next to the established selfie, so not clearly settled by the rules
# question autoprueba: rare compound, kept as a legitimate word
# question autoritativo: possible English calque of "authoritative", kept because it is in real use
# question autoritativo: possibly an English calque, but it is attested in theological and technical Spanish, so I kept it.
# question aventador: the real common word is a minority of the examples, which are mostly the Lamborghini; kept under the "common word stays" rule
# question azular: the real verb exists, but the counts are all azulado (adjective); I kept it by the lemmatiser's convention
# question bupropión: same drug-name issue, kept
# question cabezuela: most examples are place names, but the botanical common word exists
# question cappella: "a cappella" is an established loan, but the lemma here is mostly name occurrences, so I dropped it
# question cappella: only the second half of "a cappella"; the first half "a" has no merge target, so dropped
# question caramba: the carámbanos forms belong to carámbano, a different word, but caramba itself is clearly fine, so I kept it
# question cebollines: the form is common as a plural in Latin American recipes, so merge into cebollín versus keeping it as its own lemma is arguable
# question checkbox: UI loan commonly used in tech Spanish, but specialist; decided drop.
# question choker: fashion loan is common in Spanish shop text, but one example is the technical logging sense; kept as an established loan
# question clubber: borderline loan; kept as established enough in Spanish nightlife usage.
# question completísimo: the rules do not say whether a superlative counts as an inflected form; I merged it into completo.
# question conificado: a real word, but only specialists (cycling parts) use it; kept because the rules don't exclude niche vocabulary.
# question corintio: most occurrences are the biblical book "Corintios", but corintio is also a real common word, so I kept it.
# question corintio: most occurrences are the biblical book title "Corintios", but the word is also a real adjective, so I kept it
# question cultivación: rare calque of cultivo not in dictionaries; merged into cultivo rather than dropped
# question cámping: the academy writes cámping but camping may be the more common form on the list; merged to camping on the assumption it is listed
# question desacertar: desacierto (noun, 70) is a separate real word, but the adjective forms are the majority
# question desper: forms are mostly "despido" (me despido, despedirse), so merged to despedirse, but the noun despido is also possible
# question desper: mostly "despido" (despedir/despedirse), so the right lemma is not obvious; dropped.
# question dinamitar: most forms are the noun dinamita, but dinamitar is a real verb with its own uses, so I kept it.
# question disformidad: Spanish word that is rare outside the Warhammer "Warp" sense, so I kept it as a real word
# question disformidad: real but rare Spanish word, whose occurrences are mostly the Warhammer "Warp" term
# question doña: a title of address, which the rules drop, but also a common dictionary word; I kept it, though most examples are inside names (Hotel Doña Carlota).
# question dumper: the examples mix a software name, the construction vehicle, and a battery product; I kept it because the vehicle sense is an established loan.
# question encartar: mixed lemma with the Encarta brand (about a third of occurrences); kept as the real verb/noun encarte
# question experimentado: it could be merged to experimentar, but I kept it as a dictionary adjective meaning "experienced"
# question experimentado: it is a participle but also a real adjective ("experienced"); I kept it rather than merging into experimentar.
# question extramuros: most examples are place or district names, but it is also a real adverb
# question filum: could be argued as a technical loan, but Spanish uses "filo" for the biological sense
# question fintar: the lemma is a verb, but nearly all occurrences are the noun finta, so I merged it into finta.
# question flashear: could be seen as a technical anglicism, but it is also general slang, so I kept it
# question forestar: the forms are mostly foresta/Foresta (noun or name); I kept forestar because forestada and forestadas come from the verb.
# question galaadita: biblical gentilic may count as a common noun rather than a name
# question galaadita: biblical gentilic; I treated it as a common noun rather than a proper name
# question garriga: Catalan/Spanish common word for scrubland, but the evidence is mostly the surname and place names; dropped
# question gerir: DLE status unclear; dropped as Portuguese-like
# question gerir: no examples were available, and it may be a rare real verb rather than a Portuguese import
# question gurdo: Haitian currency "gurda" could be a real word, but the lemma form gurdo looks broken; dropped.
# question hidroclorotiazida: a common generic drug name, so a learner may meet it; I treated it as specialist vocabulary and dropped it.
# question hidroclorotiazida: a generic drug name that is not an acronym, which the rules do not cover; I kept it as a real common noun.
# question homogenización: variant of homogeneización, kept as an accepted form rather than merged
# question humbucker: a specialist loan, so I kept it because the examples show it used in Spanish sentences
# question importantísimos: lemma could be importante rather than importantísimo; chose to keep the superlative, consistent with sacratísimo
# question inscripta: the lemma could be the participle inscripto or the verb inscribir; I chose the verb
# question intarsia: Italian origin, but used as a knitting term; kept
# question intarsia: knitting term that may count as an established loan; dropped as specialist
# question jumpsuit: could count as an established fashion loan, but Spanish has mono
# question jumpsuit: used in Spanish fashion writing, so it may count as an established loan, but mono exists and examples are mostly product text
# question lasallista: derived from the name of an institution (La Salle); keep vs drop is not settled by the rules
# question levonorgestrel: generic drug names are not covered by the rules; kept as real Spanish nouns, not brands
# question lidocaine: examples are English text, so I dropped it rather than merging into lidocaína.
# question lidocaine: examples are largely English-language spam text, so drop is also defensible
# question manifold: Spanish diving and engineering texts use it as a loan, but many examples are software or product names, so I dropped it
# question mazut: Russian-origin loan with mostly trade-site use; I kept it as an established term for fuel oil.
# question mediar: the verb mediar is real, but the counted forms are almost all the plural-only "mediados"; I merged it into mediados, but keeping mediar is also defensible.
# question medo: ethnonym of an ancient people; kept as a common noun because the Spanish word medo is real
# question medo: ethnonym of an ancient people; kept as a dictionary word rather than a proper noun
# question mensurar: the counts mix the verb and the noun mensura; I kept the verb lemma as is.
# question menudear: the verb is real, but nearly all forms are the noun menudeo
# question mesar: forms meso and mese suggest a mixed lemma, but mesar is a real verb with its own forms
# question mesar: the verb is real, but most forms are meso/mese (prefix or name), so I dropped it
# question meteo: a clipping of meteorología that is common on weather sites, but the examples are missing and it is tagged PROPN. I dropped it as a brand or site name; merge:meteorología would be the alternative if that lemma is listed.
# question meteo: clipping of meteorología, but it may be established enough as its own word; merged under the abbreviation rule
# question mixes: could also be the ethnonym mixe or "mixtos"; merged into mix from the music-mix example
# question mixes: examples mix the ethnonym with the English "mixes" (music mixes), so the lemma is unclear
# question monomodo: a technical term, but a real Spanish word, so kept
# question monomodo: specialist fibre-optic term, kept as a real compound; could be seen as too technical
# question mugir: the verb is real and the Mugen brand dominates the counts; I dropped it per the minority-reading rule.
# question mulching: it is used in Spanish garden-machinery text but is probably too specialised for a learner list
# question mulching: possibly established in gardening-equipment Spanish; dropped as a specialist English term
# question multipar: multiparte is not clearly standard Spanish and the medical term is multípara, but most occurrences are multiparte
# question multipar: unsure whether multiparte is a standard Spanish word; the medical term is multípara
# question mískito: merged into miskito, assuming that is the standard spelling of the listed ethnonym
# question overclock: it is a loan used by PC users, but it is specialist; unclear whether it is established enough to keep.
# question pablista: niche political term, kept as a real derived word
# question panko: borderline whether a Japanese culinary loan is established enough for a learner list
# question panko: it is a Japanese loan used mainly in recipes, and whether it is established enough for a learner list is unclear
# question pavonar: pavonar is a real verb but forms split between the place name Pavones and the adjective pavonado, so dropped as a minority real-word reading
# question pegador: examples look like web spam, but the word is real Spanish, so I kept it
# question pegador: real Spanish word, but most examples are spam translations ("precios pegadores"); kept as a real word
# question pembrolizumab: a generic drug name, not an acronym or brand; the rules don't say whether rare generic drug names are kept, so I dropped it as specialist vocabulary.
# question pomeranio: forms mix the dog breed with the place Pomerania; kept because the breed is a common word.
# question pomeranio: the dog breed is a real word, but most examples are the place name; decided drop.
# question postratamiento: technical compound, kept as a real prefixed word; could be seen as too specialist
# question putter: English golf term, kept as an established sports loan; borderline
# question putter: a golf term that only specialists may use, but it is established in Spanish golf vocabulary, so I kept it.
# question quererse: "te quiero" is mostly plain querer with an object clitic, not the reflexive; I kept the pronominal lemma by convention
# question sandboard: it is unclear whether niche sport loans like sandboard and skatepark count as established enough; I kept both.
# question sandboarding: established enough as a loan is borderline
# question seleccionado: participle filed as lemma, but it can also be a plain adjective; I treated it as a participle to merge, unlike experimentado
# question shells: computing sense "shell" is a loan, but some examples are pistachio shells; I merged into shell on the computing majority.
# question shells: the computing sense (shell) is an established technical loan, but most examples are mixed with product names, so I dropped it.
# question shunt: established in Spanish medicine and electronics, but only specialists use it, so keep versus drop is a judgement call
# question shunt: established in medical and electrical Spanish, but could be read as a specialist foreign term
# question sinsajo: sinsajo is also a real word for a bird, but nearly all examples are the book title
# question sitar: the instrument is a real loan but the "site" forms dominate; I dropped it per the minority-reading rule.
# question stewards: Wikimedia role in the examples; the aviation loan steward might merit a merge
# question tacrolimus: same as levonorgestrel
# question timestamp: English IT term, kept as an established loan, but it is borderline.
# question timestamp: possibly an established IT loan, but dropped as specialist
# question tolar: examples mix the currency and the place Tolar Grande; kept as the currency.
# question tolar: the occurrences mix the currency with the place Tolar Grande, so kept as a currency
# question transtorno: academy-accepted variant of trastorno; kept rather than merged, but the list may prefer the commoner spelling
# question transtorno: accepted academy variant of trastorno, so kept rather than merged
# question trasparencia: accepted academy variant of transparencia, so kept rather than merged
# question trasparencia: same issue, accepted variant of transparencia
# question tuno: forms are mostly tuna/Las Tunas (a place); kept as the real word, though merge:tuna is possible
# question tuno: most examples are Las Tunas (a place); merged into the common word tuna
# question tupi: no clear rule for ethnonyms; merged into tupí as a common word rather than dropped as a name.
# question ucranio: most forms are lowercase ucrania, a misspelling of the place name; I kept ucranio as the real demonym.
# question ucranio: most forms are lowercase ucrania, probably the place name; I kept the demonym.
# question ummah: I am not sure the academy dictionary lists "umma", so the merge target may be wrong
# question ummah: Spanish may write it "umma"; dropped as not established
# question vemurafenib: generic drug names are not covered by the rules; kept as a common noun, but it is very specialist
# question vemurafenib: the rules have no clear line on generic drug names; I dropped it as too specialist but kept bupropión as better known.
# question vertir: could be a cut-off fragment of convertir/divertir/advertir, or rare verter; no obvious merge, so dropped
# question vertir: no example sentences; may be verter or a cut-off convertir, so dropped
# question viejita: a diminutive with its own entry; I kept it rather than merging into viejo.
# question vítae: "currículum vítae" is a split loan, but currículum also occurs alone; I assumed its own lemma is handled separately and only dropped vítae.
# question vítae: the first half "currículum" is not in this batch, so I can't check that it is merged to "currículum vítae"; I dropped vítae under the split-loan rule.
# question zafar: some occurrences are the surname or place Zafar
# question zoster: occurs only in "herpes zóster"; could be treated as a split loan or kept as is, I merged it to the accented form
# question ñoño: most forms are nona (a different word), which the lemmatiser conflated with ñoño; I kept ñoño as a real word.
# question ñoño: the forms are mostly nona, a different word; I kept ñoño because it is a real word.
# question airfryer: is a brand name that is becoming generic (Airfryer) kept as a loan or dropped as a brand?
# question capar, avocar: real Spanish lemmas whose counts are inflated by English homographs (Cape, avocado). Keep them at the inflated rank, or recount?
# question comuníquense: should pronominal forms merge into the bare infinitive (comunicar) or a separate -se lemma (comunicarse)? I used the bare infinitive.
# question desvivir, asóciese, imaginaos: should pronominal-only verbs be lemmatised with -se (desvivirse), or always as the base infinitive?
# question doña: the rules do not cover titles of address (don, doña); should they always be kept?
# question importantísimos, famosísimo: should -ísimo superlatives stay as their own lemmas or merge into the base adjective (importante, famoso)?
# question mediar, pontificar, almidonar, trovar, maño: a single decision cannot split a lemma that mixes two real words (mediar/mediados, almidonar/almidón, maño/maña); can these be split, and which should hold the frequency?
# question pomeranio: the breed noun pomerania shares its form with the place name Pomerania. Should the merged lemma stay on the list, or go to pending-names?
# question sitar, mugir: these are kept as real words, but their counts are mostly junk forms ("site", "Mugen"); should their frequency be recomputed?
# question trasparencia: should academy-accepted minor variants merge into the main spelling, or stay as separate lemmas?
# question trigésimo, decimoctavo, vigesimoctavo: should an ordinal that exists as a word be kept when all its counted tokens are digits?
# question airfryer: should a product name that is turning generic (airfryer) count as a brand or as an established loan?
# question capar, avocar: if a real Spanish lemma's occurrences are mostly a misattributed foreign token, should the lemma stay as keep (my reading) or drop?
# question galaadita: are gentilics of places not on the place list (biblical or minor) always drop?
# question importantísimos, famosísimo: should superlatives (-ísimo) keep their own lemma or merge into the base adjective (importante, famoso)? I treated them as their own lemma, as the rules list only plurals and conjugations as broken.
# question lasallista: should adjectives derived from the names of large but non-institutional organisations (religious orders, school networks) be kept like franquista-type words or dropped as name-derived?
# question mediar: keeping mediar leaves the far more frequent "mediados" (a mediados de) attached to it; should mediados get its own entry when a mislemmatised word dwarfs a real lemma?
# question sitar, mugir, mesar, agio, aventador: when the lemma string is a real Spanish word but most forms belong to a foreign word, brand or place, is there a share or frequency threshold for keep vs drop?
# question trasparencia: should academy-accepted minority variants (tras-/trans-, etc.) stay separate or merge into the majority spelling under the "form people write" rule?
# question trigésimo, decimoctavo, vigesimoctavo: should "only written as digits" be judged on this corpus's forms, especially when many digit forms are degrees rather than ordinals?
# question vemurafenib: the rules drop specialist acronyms but don't cover specialist non-acronym terms such as generic drug names; I treated them the same way (drop)
