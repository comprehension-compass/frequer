# es review shard 4: report

Branch `es-review-shard-4` from `c4aacac`. Setup by `scripts/review-shard-setup.sh 4` (honeyeater `c07c701`,
lemma wheel 1.5.0 checksum ok, uplift `f8c8a67`, fixed extractor `examples10.py`). Screeners and reviewers
sonnet-class, adjudicator opus-class (config). No failed batches or calls in any step; nothing was rerun.

## Counts

| step | lemmas | result |
|---|---:|---|
| flagged queue (action `pending`) | 956 | examples for 850 (88.9 %) |
| unflagged screen (two screeners) | 4,959 screened | 652 suspects (506 listed by both); 3 learnable names left out as release entries |
| suspects queue | 652 | examples for 588 (90.2 %) |

The routed pool has 4,962 unflagged lemmas; 4,959 were screened and 3 were set aside as learnable names (the release's own entries).

| round | lemmas | agreed | adjudicated (disagreements + queries) | queried | keep | drop | merge |
|---|---:|---:|---:|---:|---:|---:|---:|
| s4-flagged | 956 | 933 | 23 (11 + 12) | 12 | 84 | 815 | 57 |
| s4-unflagged | 652 | 602 | 50 (33 + 17) | 17 | 233 | 212 | 207 |
| **total** | **1,608** | **1,535** | **73** | **29** | **317** | **1,027** | **264** |

Reviewers before the gate: s4-flagged 945 agreed (87 keep / 805 drop / 53 merge), 4 accent-only merges;
s4-unflagged 619 agreed (219 keep / 208 drop / 192 merge), 18 accent-only merges.

## Gate: queries and outcomes

I read every agreed merge, every agreed keep, the whole agreed drop list for s4-unflagged and a sample of 70
for s4-flagged, all accent-only merges and the disagreements. The accent-only merges hide no second word, except
liquido (checked: all forms are líquido). Queries (lemma: why → adjudicator's decision):

### s4-flagged (12 queried, 6 changed)
* **prospera** (agreed `merge:prosperar` → `merge:prosperar`): agreed merge:prosperar, but 93% capitalised and one example is a brand (Prospera massager); also could be próspera (adj. without accent): verb, adjective or brand?
* **messiah** (agreed `merge:mesías` → `drop`): agreed merge:mesías, but the only example is an English name ("YAHUSHUA Messiah"); a non-Spanish token whose Spanish reading is a minority drops
* **cous** (agreed `merge:cuscús` → `merge:cuscús`): agreed merge:cuscús as first half of split loan "cous cous", but both halves are the same token "cous": merging all occurrences counts each "cous cous" twice
* **afro-americana** (agreed `merge:afroamericana` → `merge:afroamericano`): agreed merge:afroamericana: target is the feminine form; the adjective lemma is presumably afroamericano (cf. judeo-cristiana -> judeocristiano)
* **restaura** (agreed `merge:restaurar` → `merge:restaurar`): agreed merge:restaurar with no examples; 93% capitalised (Restaura), may be a brand or company name
* **maxima** (agreed `drop` → `drop`): agreed drop as brand, but may hide máxima (feminine of máximo / noun "maxim") written without accent
* **afghani** (agreed `drop` → `drop`): agreed drop as foreign, but it is a currency (Afghan afgani); earlier rulings keep currency names (rand, leu, birr kept here)
* **vnu** (agreed `keep` → `drop`): agreed keep as UN Volunteers; is a minor UN programme a famous international body under the institutions rule?
* **fnuos** (agreed `keep` → `drop`): agreed keep as UN observer force (UNDOF); specialised UN mission, is it famous?
* **ciemat** (agreed `keep` → `drop`): agreed keep as national research body; specialised public body, nationally famous?
* **músculo-esquelético** (agreed `keep` → `merge:musculoesquelético`): agreed keep, but the spelling rule merges hyphenated spellings of a word Spanish writes as one (musculoesquelético)
* **checkin** (agreed `keep` → `keep`): agreed keep, but the written form is check-in; English spelling merge under the spellings rule?

### s4-unflagged (17 queried, 11 changed)
* **habeis** (agreed `merge:habéis` → `merge:haber`): agreed merge:habéis, but the target is a conjugated form; the lemma is haber (cf. teneis -> tener)
* **podreis** (agreed `merge:podréis` → `merge:poder`): agreed merge:podréis, but the target is a conjugated form; the lemma is poder
* **dinamo** (agreed `merge:dínamo` → `keep`): agreed merge:dínamo, but most forms are the club name Dinamo (488 of ~710); dinamo is also an accepted spelling: merge, keep or drop?
* **liquido** (agreed `merge:líquido` → `merge:líquido`): accent-only merge:líquido; check the hidden verb form liquido (liquidar); examples look like líquido
* **diezmar** (agreed `merge:diezmo` → `keep`): agreed merge:diezmo, but diezmar is a real verb and its forms (diezmar 300, diezmado 219, diezmada 161, diezmando 132) are verb uses: keep the verb?
* **opacar** (agreed `merge:opaco` → `keep`): agreed merge:opaco, but opacar is a real verb with verb forms (opacar 182, opacado 127, opacada 81) next to opaco/opaca
* **cascar** (agreed `merge:cascada` → `merge:cascada`): agreed merge:cascada, but forms include cascara/cascaras (360 = cáscara without accent): two words under one broken lemma
* **jalear** (agreed `merge:jalea` → `merge:jalea`): agreed merge:jalea, but forms include jaleo/Jaleo (326), a separate real noun: two words under one lemma
* **murar** (agreed `merge:morir` → `merge:morir`): agreed merge:morir (muramos, muráis), but Mures (419) is a name: does the name share go with it?
* **molesta** (agreed `merge:molestar` → `merge:molesto`): agreed merge:molestar with no examples; could be the adjective molesto (fem.) rather than the verb
* **sunitas** (agreed `merge:suní` → `merge:sunita`): agreed merge:suní; the written singular is sunita (people write sunita/sunitas): spelling rule says the form people write
* **pacificar** (agreed `drop` → `keep`): agreed drop because examples are the name Pacifica, but pacificar is a real verb; a real common word stays even if many occurrences are a name
* **humanar** (agreed `drop` → `drop`): agreed drop (mostly a plant/name), but humanar is a real verb: is the real-word share a minority?
* **chontal** (agreed `drop` → `keep`): agreed drop as place name, but chontal is also an indigenous people/language (cf. wayuu, purépecha kept)
* **grappa** (agreed `drop` → `drop`): agreed drop, but grappa is a liqueur name used in Spanish like amaretto (kept in s4-flagged)
* **cedeao** (agreed `keep` → `drop`): agreed keep (ECOWAS); a regional body: famous international body under the institutions rule, or regional like OEA (dropped earlier)?
* **rimel** (agreed `keep` → `merge:rímel`): agreed keep, but Spanish writes rímel (s4-flagged merges rimmel -> rímel): merge:rímel?

## Things to know

* **Two words under one lemma.** cascar (cascada and cáscara without its accent, 360) and jalear (jalea plus jaleo,
  326) were merged into the majority word, so the hidden word's counts go with it. opacar and diezmar
  were kept as verbs, though opaco/opaca (3.5k) sits under opacar. The adjudicator asks whether these should be
  split by form, the way halar/hala was (question below). This is a new class, so I left it to the coordinator.
* **cous → cuscús**: both halves of "cous cous" are the same token, so the merge counts each phrase twice
  (question below).
* **Outputs ignored by git.** The repository's `.gitignore` has a generic `out/` rule, so the files under
  `shard-4/out/` were added with `git add -f`.
* Nothing else went wrong: no failed calls, no undecided lemmas.

## Every `# question` line

### s4-flagged
# question alfa-linolénico: a real chemistry term, but a hyphenated compound with no standard fused spelling; dropped.
# question alfa-linolénico: it is a real chemistry term, but I applied the hyphenated-compound drop rule. I am unsure whether "linolénico" is itself listed.
# question aosis: international body of small island states, but not among the famous bodies listed; dropped as specialist acronym
# question aosis: international body, but a specialist UN grouping, so dropped rather than kept like ONU
# question batista: real fabric word, but most uses are the surname
# question belladonna: Spanish word is belladona, but examples are mostly a person's name and English text; merged on the spelling rule.
# question berrocal: most occurrences are surnames or place names, but it is a real common word, so kept
# question betta: a real pet-fish name used in Spanish, but evidence is mixed with proper-noun uses; dropped.
# question betta: the examples are mixed between the fish name and a place or other name. I kept it because the fish reading looks like the majority.
# question birr: flagged as a possible cut-off, but it is the Ethiopian currency, so kept
# question birr: the examples mix the town Birr (a place, which would drop) with the Ethiopian currency; I kept it as the currency.
# question brassica: could merge to brásica, but the examples are mostly the Latin genus name, so I dropped it.
# question broadcaster: English term used in tech and media Spanish, but not established enough to keep as a loan
# question carrasco: real common word, but most uses are the Montevideo place and surnames
# question ccrvma: international body (Antarctic marine resources commission) but not famous like ONU or OMS; dropped as a niche body
# question ccrvma: international body, but not famous like the UN bodies on the list
# question ciemat: a national public research body, but not clearly as famous as the examples in the rules
# question ciemat: a public research body, but unclear whether it is nationally famous enough to keep
# question cmts: also the informal abbreviation of centímetros in some examples, but the CMTS (cable modem) reading dominates, so dropped rather than merged into centímetros
# question cmts: majority is the cable-modem acronym, but some uses are the abbreviation of centímetros. Dropped rather than merged.
# question croton: croton is also a plant name, but the examples show only the company, so I dropped it.
# question croton: the plant word is crotón in Spanish, but the examples are company uses, so I dropped it rather than merging.
# question cupa: rare Spanish word (cuba) exists, but the examples are overwhelmingly the brand, so dropped.
# question divemaster: it could count as an established loan among divers, but I treated it as a certification title and dropped it.
# question divemaster: specialist diving term used in Spanish dive courses; dropped as not established for general learners
# question durbar: could be a common noun for a historical court assembly, but the examples are mostly names
# question e-scooter: could be an established loan, but I judged it a hyphenated English spelling and dropped it
# question fnuos: UN peacekeeping force (UNDOF); unclear whether it counts as a famous international body like ONU/OTAN
# question fnuos: is the UN Golan observer force (UNDOF) a "famous international body" in the same sense as ONU or OTAN? I kept it.
# question glitch: a gaming loan that may not be established enough, but it is common in Spanish gaming text, so I kept it.
# question glitch: capitalised in only 24% of running text, so the loan reading is plausible, but it is a niche gaming term.
# question horde: a game faction name, though "horda" is a real word; I judged that most uses are the name and dropped it.
# question horqueta: many occurrences are place names, but it is a real common word, so kept
# question iccat: An international body but specialist, not clearly in the famous-bodies class; dropped.
# question iccat: international body, but a specialist one; dropped as a technical acronym
# question indonesa: demonym filed under the feminine; merged into indonesio, though the rules could also read it as a separate feminine entry
# question indonesa: merge to indonesio assumes the feminine adjective isn't a separate entry; keep if the lemmatiser treats it as one
# question inkas: could be a spelling of incas, but the examples show a hotel/brand name, so dropped
# question inkas: examples show a hotel name, so the inca reading may be a minority
# question junker: Spanish history texts use "junker(s)" for Prussian aristocrats, but examples are mixed with a company name; kept as a historical term.
# question katakana: foreign script name; kept as a word learners meet, but could be treated as a foreign term
# question kola: brand (Inca Kola) dominates examples; kept as the real word
# question lobería: most examples are place or hotel names, but the common noun exists, so I kept it
# question lobería: mostly place and hotel names, but it is also a real common word, so kept
# question macroinvertebrado: only plural forms are written; kept as lemma because the singular is a valid Spanish word, though specialist.
# question malvarrosa: most examples are the Valencia beach (a place name), but malvarrosa is also a real Spanish plant word; I kept it as the common word.
# question malvarrosa: most examples are the place or a business name; kept as the real flower word under the common-word rule
# question marshmallow: English loan for the sweet vs. Android/brand name; the name uses dominate, so dropped
# question messiah: examples read like a name (YAHUSHUA Messiah) in English text; merged into mesías on the English-spelling rule
# question messiah: examples show a religious-name use (YAHUSHUA Messiah), which may be a title rather than the common word
# question micro-sd: merge into microSD or keep as written? The rules treat it as a hyphenated spelling of an adapted tech term.
# question mini-nevera: unsure whether Spanish writes this as mininevera or mini nevera, or whether "mini" counts as a listed word that would make it a droppable hyphenated compound.
# question músculo-esquelético: hyphenated compound of two parts, may be dropped as hyphenated compound; kept since músculo-esquelético is not two listed words in this sense
# question nearshore: business jargon used in Spanish IT text, so it could count as an established loan like "online"
# question nearshore: business jargon used in Spanish IT text; may count as an established loan
# question nidal: capitalised Nidal (a name) is over half the occurrences, but the real Spanish noun is established, so I kept it.
# question noodl: "noodles" is sometimes used in Spanish food writing; I dropped it as not established enough
# question noodl: noodles is only a gloss for fideos in most examples, so it is not clearly an established loan. I merged it rather than dropped it.
# question norad: is NORAD a famous international body like OTAN, or a regional agency name (also used for the Norwegian Norad)? Dropped.
# question pacho: "pacha" is also a real word, but most hits are the name Pacho, so I dropped it
# question pacho: Pacha/pacha (a la pacha, relaxed) is a real word but is filed under a mostly-name lemma; dropped
# question paho: famous international body, but written in its English form rather than Spanish OPS
# question paho: international body (PAHO = OPS) but the English acronym is not the Spanish form, so dropped
# question plo: could count as a famous international body, but it is not an established Spanish acronym
# question plo: the PLO is an international body but not on the listed famous bodies; I dropped it.
# question policias: most examples are a forum name, but the word is a real plural missing its accent, so I merged it
# question pre-construcción: could merge to "preconstrucción", but that form is rare and not clearly a Spanish lemma, so dropped
# question rondón: most examples are a surname, but the common word (de rondón) exists, so I kept it under the common-word rule.
# question rondón: mostly a surname (86% capitalised), but "de rondón" is a real Spanish idiom, so I kept it.
# question salema: salema is also a Spanish fish name, but the examples are overwhelmingly the Algarve beach/town; dropped as a place.
# question salema: salema is also a Spanish fish name, but the examples are the Algarve place, so dropped.
# question sambuca: also a liqueur and a place name in the examples; kept as the instrument word, which appears in Spanish text.
# question sambuca: place name Sambuca di Sicilia appears, but the instrument/liqueur reading is a real common word, so kept.
# question sanfermin: the Sanfermines festival is famous, but the rules say events drop; dropped.
# question sanfermin: the rules drop events, but Sanfermines is a very familiar Spanish festival word; I dropped it, though a plural-only merge:sanfermines is arguable.
# question seguidme: imperative plus clitic; merged into seguir though lemmatiser might keep such forms.
# question shabbat: Spanish usually writes shabat, but the counted form is shabbat; kept as written.
# question shabbat: Spanish usually writes shabat, but the counted text overwhelmingly has Shabbat, so kept as written
# question sil: rare real word (ochre pigment), but nearly all uses are an organisation acronym
# question sil: rare real word (ochre) vs. dominant organisation acronym; dropped
# question songo: a real Cuban music term, but the examples are mostly a name
# question start-stop: the car start-stop system might count as an established loan, but dropped as a hyphenated technical term
# question tabata: it is named after a person, but it is used as a common noun for a workout style, so I kept it.
# question tabata: named after a person, but used as a common noun for a workout method; kept as an established loan, though it could be argued either way.
# question taino: whether the ethnonym is better kept as a lemma than merged into the accented spelling
# question takeaway: could count as an established loan, but examples are business names
# question takeaway: the Spanish usage is borderline, since examples are English business names; I dropped it.
# question teppanyaki: restaurant-menu loan, so it is borderline in how established it is. I kept it.
# question tofo: Place name (Tofo, Mozambique) is the majority, but "tofo" (gout nodule) is a real Spanish word; kept as the common word.
# question tofo: place name is the majority of occurrences, but the real word tofo exists; kept as the common word
# question trillo: the lemma is a surname/place in the examples, but the plural trillos (187) suggests the common noun; kept
# question ulpgc: A university acronym, but regional rather than nationally famous; dropped.
# question ulpgc: a public university, but only regionally known; dropped
# question valium: a trademark that is often used as a generic noun; dropped under the brand rule
# question valium: brand, but used generically in Spanish; kept as a common word.
# question varona: examples are mostly the biblical word or a surname; I kept it as the feminine entry of varón.
# question vinca: Spanish "vinca" is a plant (pervinca), but the examples are mostly a company name and a drug name, so I dropped it.
# question vinca: vinca is a real Spanish plant name but most examples are a company name, so dropped
# question visco: ambiguous between the real word and name or prefix uses; no examples seen, kept
# question visco: could be the Spanish prefix or word "visco" (birdlime), but the examples are unavailable and a brand reading seems likely
# question vnu: Spanish acronym for UN Volunteers programme; kept as international body, though minor
# question vnu: Spanish acronym of UN Volunteers (Voluntarios de las Naciones Unidas); kept as an international body, but could be seen as too specialised.
# question wafer: English loan; kept as established in Spanish (confectionery/chip)
# question wafer: kept as loan, but many examples are watch model names.
# question wayuu: ethnic group name, could count as a proper noun; kept as a common noun
# question zepa: Spanish protected-area acronym common in Spanish text, but possibly specialist-only
# question zepa: ordinary Spanish term for a protected-area designation, but the acronym is technical, so dropped
# question checkin: the English loan is usually written check-in. Should unhyphenated checkin merge into check-in, even though the tokenizer may never produce a check-in lemma?
# question ciemat: how famous must a national public body be to stay (CIEMAT, INTA, ICEX versus CSIC)? The same question applies to minor UN programmes and missions (VNU, FNUOS).
# question cous: both halves of "cous cous" are the same token, so a merge counts each phrase twice. Should the frequency be halved, or should the second half be stripped some other way?
# question valium: should brand names that have become common words (valium, aspirina-type cases) be kept, or do all brands drop?

### s4-unflagged
# question alegadamente: calque of English "allegedly" that is not in the DLE but is common in news writing; kept as established usage
# question amicus: "amicus curiae" is a Latin legal phrase used in Spanish; dropped as specialist
# question avellano: the second example sentence has no visible avellano form and may be a place or proper-name use. Even so, the common-word reading is the clear majority, so it stays.
# question cantilever: technical design term, kept as an established loan, but it could count as specialist
# question capitoné: French-origin upholstery term; borderline between established loan and foreign word
# question capitoné: French-origin upholstery term; kept as established in Spanish decor vocabulary
# question cedeao: it is a regional African body (ECOWAS), not clearly "famous" in the sense of the rule; kept as an international body
# question cedeao: not sure whether a West African regional bloc counts as a famous international body, which the rules list only by example (ONU, UE, OTAN, OMS)
# question chenille: chenilla is the Spanish form, but these hits are mostly product listings
# question chontal: mostly the Nicaraguan department Chontales, but also an ethnonym/adjective; I chose drop as the place reading is the majority.
# question chontal: the forms are mostly "Chontales" (a Nicaraguan department), but "chontal" is also a common ethnonym; I treated it as a place name and dropped it.
# question chorrillo: the real common word is a minority of the occurrences and most are the place Chorrillos
# question claretiano: derived from a religious order's name; I treated it as an ordinary adjective and kept it
# question computerizada: the right target is unclear between computarizado and computerizado; I chose the verb computarizar.
# question computerizada: unclear whether the right lemma is computarizado or computerizado; I chose the adapted spelling computarizado
# question creatura: could be merged into criatura as a variant, but the RAE lists it as a word in its own right
# question cristino: mixed between the place Isla Cristina and misspelt cristianas; I dropped it as the majority is the place
# question cristino: the main form cristina is the Isla Cristina place name or a given name, while cristinas in the examples is a misspelling of cristianas; I dropped it rather than merging into cristiano.
# question customización: borderline anglicism (from customizar); kept as a Spanish-formed derivative
# question datum: used in Spanish geodesy/GIS, but only specialists use it; dropped as technical
# question descriminalización: it is a misspelling-flagged but widely attested Spanish variant; merging into despenalización is the alternative.
# question descriminalización: it is attested in Latin American Spanish, so keep is arguable; I merged it into despenalización, though decriminalización is the other candidate
# question dinamo: most examples are club names (Dinamo); I merged to the common word dínamo.
# question encostrar: real but rare verb; the inflected forms look unusual, so it may be a lemmatiser artefact
# question entregabilidad: calque of English "deliverability", kept as a real Spanish formation
# question entregabilidad: calque of English "deliverability", real Spanish formation but narrow email-marketing jargon; kept
# question exagente: ex- compounds are normally written solid in news text but the academy prefers a separate ex; kept as a real word
# question exagente: the rules say nothing on ex- compounds; I dropped it as a prefix compound, but a merge to "agente" or a keep for "ex agente" could also be argued.
# question facelift: car-trade loan used in Spanish listings, but all examples are model-spec strings, so I dropped it
# question facelift: only seen in car listings, so it may be too niche to count as established
# question fobos: Fobos is the Spanish name for the moon Phobos, which could count as a place name (drop) or a name for a body in space; I dropped it either way.
# question gadita: biblical demonym only (Gad tribe), borderline for a learner list, kept as a real word
# question grappa: grappa is also an established Italian spirit, but nearly all examples are the place name, so I dropped it
# question gravísimo: it is unclear whether a superlative counts as a broken lemma; I merged it into grave
# question habitacio: no examples were available, so I assumed Catalan or a cut-off form; if it is mostly an accent-less habitación it should merge:habitación.
# question hase: majority of examples are archaic "ha+se" with some spam/name uses; merged to haber though a drop is defensible
# question hmm: an English-style spelling of a hesitation interjection (Spanish usually writes "mmm"), so whether it counts as established is unclear
# question impeachment: loan, though Spanish also uses "juicio político"; kept as an established loan
# question jitter: could count as an established technical loan, but treated as specialist
# question kayac: kayac is the adapted spelling, but kayak is the more common form people write; merged
# question kulak: borderline historical Russian loan; kept as used in Spanish historical texts
# question lamivudine: same doubt as sumatriptan; merged into lamivudina, though dropping could be argued.
# question lamivudine: same issue as sumatriptan. I merged it to lamivudina as an English spelling of an adapted word, but it could be a specialist term to drop.
# question lidio: lidio is a real adjective (Lydian), but most forms are lidia, so I merged
# question malls: established in Latin American Spanish but not in all varieties; I merged to mall rather than dropping it.
# question malls: mall is a loan mainly in Latin America; merged the plural to mall rather than dropping.
# question mapeados: merged to the verb mapear, though mapeado (participle/adjective) is also plausible
# question mirrorless: a photography loan that may only be specialist; I kept it as widely used in Spanish camera text
# question mirrorless: the term is used in Spanish camera writing but may be too specialist for a learner list.
# question molesta: could be the feminine of the adjective molesto or a form of molestar; the examples were unavailable
# question montesino: the real adjective is rare and most occurrences are the surname or place Montesinos, so keep is borderline
# question mortem: "post" is not in this batch, so I dropped it as the second half of the split loan "post mortem"
# question moño: most counted forms are "monos" (mono), so the lemma may be mis-assigned, but moño itself is a real word and is kept
# question notariado: forms mix the noun notariado and the participle notariada; I kept the noun lemma
# question nylon: the academy spells it nailon, but the counted text almost always writes nylon; I kept it as the form people write rather than merging into nailon.
# question opacar: forms are mostly the adjective opaco; I merged it, though opacar is also a real verb
# question orear: lemma is a real verb, but the counts are dominated by the Oreo brand
# question orear: the forms are mostly the Oreo brand, but orear is a real verb, so I kept it under the common-word rule
# question pachinko: unclear whether it is established enough in Spanish to count as a loan
# question pachinko: well-known Japanese game, but not established in Spanish; dropped
# question pacificar: forms are mostly the name Pacifica and pacifico, so unclear whether to merge into pacífico or drop; chose drop.
# question pacificar: real verb exists, but most forms are the name Pacifica or the misspelling pacifico, so I dropped it
# question pallar: the capitalised Pallas/Pallares/Palla are probably names, which may outnumber the real bean word
# question politburó: could be read as an institution name, but treated as a common noun
# question predeterminadamente: real-sounding adverb used for "by default" but not a standard dictionary form; dropped as dubious
# question qubit: a specialist term; I kept it as an established loan, but it could be read as technical vocabulary only specialists use.
# question qubit: could count as a specialist term; kept because it is the established Spanish form in general science writing
# question rapidísima: unclear whether a superlative should merge into rapidísimo or rápido; chose rapidísimo
# question rapidísima: unclear whether the lemma should be rápido or rapidísimo
# question realize: some of the 169 occurrences may be English, but all three examples are Spanish misspellings of "realice", so I merged it.
# question rectar: almost all the occurrences are recta, which is a noun in its own right and also the feminine of recto; I merged to recta, but recto is also defensible.
# question responsivo: calque from English "responsive", but common enough in Spanish web writing that I kept it
# question responsivo: calque of English "responsive" but widely used in Spanish web-design text; I kept it.
# question roadbook: the examples are mostly product listings, but it is the standard rally term in Spanish, so I kept it.
# question roadbook: this is a niche rally term; I kept it as an established loan
# question rosáceo: the noun rosácea dominates; I kept the lemma instead of merging it to rosácea.
# question salita: a diminutive that could merge into sala, but it is not a broken lemma, so I kept it
# question siquiátrico: it is an accepted academy spelling, so I kept it rather than merging it into psiquiátrico.
# question siquiátrico: kept as an accepted variant; merging into psiquiátrico is possible if one spelling is preferred.
# question subsiguientemente: adverb of real subsiguiente, used in legal/formal text, but not clearly established; dropped
# question sumatriptan: drug generic names may be too specialist for a learner list; I merged them into the Spanish spelling.
# question sumatriptan: the rules don't say whether generic drug names belong on a learner's list. I merged it as a missing-accent form, but it could be a specialist term to drop.
# question telf: the abbreviation of teléfono is a minority of occurrences versus the town Telfs, so I dropped it rather than merging into teléfono
# question trimado: nautical term, kept as real Spanish, but all examples are product/technical text
# question trimado: nautical/technical sense only; kept as real Spanish word
# question ultimadamente: a calque but widely written in Spanish web text; I chose drop because it is not standard.
# question ultimadamente: it is a calque of English "ultimately" and is not obviously a misspelling, so I dropped it rather than merging it into "finalmente".
# question upyd: a political party is neither a listed famous institution nor an ordinary organisation; dropped as a party acronym
# question valsartán: drug generic names aren't covered by the technical-acronym rule, so it could be a specialist term
# question valsartán: real generic drug name, but possibly too specialist for a learner list; kept as a common noun
# question velour: unclear if velour is established enough to keep as written or should merge into velur
# question vicenciano: real but niche religious adjective, so keep is borderline
# question zapar: zapa is also a distinct word (sap/spade) but most occurrences are zapas (shoes), so merged to zapa.
# question zapar: zapa/zapas could be the real word zapa (spade/sap) rather than the clipping of zapatilla; the examples shown are all sneakers, so I merged to zapatilla.
# question zucchini: Spanish texts do use it, so it may be an established loan, but calabacín is the standard word; I dropped it.
# question zucchini: it may be established in some regions, but calabacín is the standard Spanish word
# question cedeao: should regional international bodies (CEDEAO, OEA) count as famous international bodies under the institutions rule? OEA in particular seems learner-relevant.
# question gadita: are demonyms of biblical tribes and peoples (gaditas, rubenitas, manasitas) common words to keep or names to drop?
# question molesta, habitacio: no examples in the sample; molesta could be the verb molestar, and habitacio could be Catalan habitació rather than cut-off habitación.
# question opacar, diezmar, cascar, jalear: two real words are filed under one lemma (opaco, cáscara and jaleo are hidden); should the hidden word be split out into its own entry, or is one decision per lemma final?
# question rapidísima: should -ísimo superlatives merge into the base adjective (rápido) or into a masculine superlative lemma (rapidísimo)?
