# de cleaning pass: per-band report (four review rounds and the developer's rulings of 2026-11-02 applied)

Bands by position in the cleaned list (kept rank). A lemma counts in the band where it would have sat. "Kept" includes unreviewed lemmas with no flag and reviewed keeps; "dropped" is every lemma removed from that stretch of the raw ranking (review drops, the number rule, 2+-flag drops).

| band | raw ranks | kept | of which reviewed keep | dropped | review drop | English exclusion | number rule | other drop | kept share | f at band end |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0-10,000 | 1-10892 | 10,000 | 1,040 | 1,082 | 671 | 190 | 221 | 0 | 90.2% | 2215 |
| 10,000-20,000 | 10893-22430 | 10,000 | 811 | 1,962 | 1,323 | 423 | 215 | 1 | 83.6% | 821 |
| 20,000-25,000 | 22431-28285 | 5,000 | 365 | 1,118 | 747 | 263 | 108 | 0 | 81.7% | 598 |
| 25,000-30,000 | 28286-34135 | 5,000 | 341 | 1,096 | 758 | 246 | 92 | 0 | 82.0% | 462 |

Pending (flagged, not yet reviewed) inside the 30k: 19

## Real-lemma share of the kept list (sample, drawn before round 4)

100 random kept lemmas per band, judged by one independent reviewer (real, correctly spelt dictionary lemma a learner wants: yes/no). The misses are mostly lemmatiser output no rule flags (a wrong citation form, a clipped stem), which only a lemmatiser fix or a wider review would catch.

Adjusted real share (units such as *es gibt* and homograph keys such as *Gericht#court* are the app's own conventions, counted as real): 0-10k 95%, 10-20k 85%, 20-25k 79%, 25-30k 84%.

| band | real | not | real share | the misses |
|---|---:|---:|---:|---|
| 0-10k | 89 | 11 | 89% | mEHR (miscapitalised fragment), weichen#yield (annotation artefact), Q (single letter), Preis-Leistungsverhältnis (misspelt, needs Leistungs-), es gibt (phrase not lemma), sich merken (reflexive phrase form), dating (English word), im Durchschnitt (phrase), Platz nehmen (phrase), ausgerichtet (inflected participle), Gericht#court (annotation artefact) |
| 10-20k | 83 | 17 | 83% | ups (English interjection), ie (fragment), Corona-Virus (should be Coronavirus), Ficht (should be Fichte), Ostukraine (minor region), Konstantin (personal name), Bohr (surname/fragment), si (fragment), Lanz (surname), sich finanzieren (reflexive phrase form), Gegentor#Neut (annotation artefact), pflegend (participle form), Programmier (cut-off fragment), Angeblich (miscapitalised adjective), jo (colloquial particle fragment), bett (fragment of Bett), Anschreibe (fragment) |
| 20-25k | 78 | 22 | 78% | wrde (cut-off wrde), beworben (inflected participle), Installer (English word), Haselnuß (old spelling Haselnuss), Knowhow (should be Know-how), umschlossen (inflected form), Fingerabdrücke (plural form), Wolter (surname), beschichtet (participle form), Enthalte (inflected fragment), Organisieren (capitalised verb form), Schenker (surname), Beende (imperative fragment), gebracht (inflected participle), So (miscapitalised So), Denise (personal name), Zusammengefasst (miscapitalised participle), gebräunt (inflected participle), HABEN (miscapitalised auxiliary), sich von etwas ernähren (phrase), Nachhaltig (miscapitalised adjective), Amazona (brand/name fragment) |
| 25-30k | 81 | 19 | 81% | dot (English word), Unity (brand/English), feat (abbreviation, not German), hälfte (fragment), Dinslaken (minor place), reCAPTCHA (brand), Angie (personal name), gespendet (inflected participle), oz (abbreviation, English), Sophos (company name), gesponsert (inflected participle), autofahren (should be Auto fahren), gesundheitsfördern (broken lemma), Staatlich (miscapitalised adjective), schmerz (cut-off fragment), im großen Stil (phrase), Sonnentag#day (annotation artefact), Schieb (fragment), Gewerkschaftsbund#Masc (annotation artefact) |

## Rule hits in the window

| rule | hits | of which dropped |
|---|---:|---:|
| propn_usage | 4,354 | 3,212 |
| shape | 539 | 248 |
| citation | 286 | 134 |
| diversity | 232 | 155 |
| foreign | 36 | 31 |
| number rule (drops) | 636 | |

## Sample keeps around 25,000

| kept rank | raw rank | lemma | freq | POS | reviewed |
|---:|---:|---|---:|---|---|
| 24946 | 28217 | Musikgeschichte | 600 | NOUN |  |
| 24947 | 28218 | Raumteiler | 600 | NOUN |  |
| 24949 | 28221 | Volksverhetzung | 600 | NOUN |  |
| 24952 | 28224 | Webprojekt | 600 | NOUN |  |
| 24959 | 28231 | äußere | 600 | ADJ |  |
| 24967 | 28242 | Glücksfall | 599 | NOUN |  |
| 24981 | 28258 | tiefe | 599 | ADJ |  |
| 24986 | 28264 | Betriebsart | 598 | NOUN |  |
| 24990 | 28271 | Mnner | 598 | NOUN |  |
| 25004 | 28289 | pokern | 598 | NOUN |  |
| 25008 | 28294 | Blättchen | 597 | NOUN |  |
| 25014 | 28300 | Multitasking | 597 | NOUN |  |
| 25023 | 28312 | einbürgern | 597 | VERB |  |
| 25045 | 28339 | pensionieren | 596 | ADJ |  |
| 25056 | 28355 | Schnäppchenpreis | 595 | NOUN |  |

## Sample keeps around 30,000

| kept rank | raw rank | lemma | freq | POS | reviewed |
|---:|---:|---|---:|---|---|
| 29942 | 34077 | Nagelstudio | 463 | NOUN |  |
| 29943 | 34078 | Nebenkostenabrechnung | 463 | NOUN |  |
| 29944 | 34079 | Pflasterstein | 463 | NOUN |  |
| 29945 | 34080 | Präposition | 463 | NOUN |  |
| 29947 | 34082 | Sammelbegriff | 463 | NOUN |  |
| 29954 | 34089 | USP | 463 | PROPN |  |
| 29955 | 34090 | Vorbau | 463 | NOUN |  |
| 29966 | 34101 | unterrichte | 463 | VERB |  |
| 29967 | 34102 | verwendung | 463 | ADJ |  |
| 29975 | 34110 | Buchverlag | 462 | NOUN |  |
| 29976 | 34111 | Civic | 462 | PROPN |  |
| 29980 | 34115 | Frontkamera | 462 | NOUN |  |
| 29987 | 34122 | Lizenzgeber | 462 | NOUN |  |
| 29998 | 34133 | STIHL | 462 | PROPN |  |
| 29999 | 34134 | Shenzhen | 462 | PROPN |  |

## Random 50 drops from the window

| raw rank | lemma | freq | POS | why | reason |
|---:|---|---:|---|---|---|
| 5876 | Carl | 5249 | PROPN | review drop | agreed: first name |
| 6055 | neunzehnhundertvierundachtzig | 5040 | NUM | number rule | number rule: lexicon.number_words.number_is_learnable(de) is False (Honeyeater 25ec0b1) |
| 6848 | Focus | 4245 | PROPN | review drop | coordinator correction: the surface forms are the English word or a name (top form 'focus' |
| 6993 | not | 4127 | ADJ | review drop | coordinator correction: the surface forms are the English word or a name (top form 'not'); |
| 7030 | neunzehnhundertfünfundsiebzig | 4098 | NUM | number rule | number rule: lexicon.number_words.number_is_learnable(de) is False (Honeyeater 25ec0b1) |
| 8072 | Nina | 3387 | PROPN | review drop | agreed: first name |
| 9029 | Basic | 2935 |  | exclusion (English) | agreed: English/programming language |
| 9287 | Toni | 2761 | PROPN | review drop | agreed: first name |
| 10100 | Guido | 2452 | PROPN | review drop | agreed: first name |
| 10944 | Spotify | 2202 | PROPN | review drop | agreed: brand |
| 11615 | Finance | 2087 |  | exclusion (English) | agreed: English |
| 13441 | hundertfünfzigtausend | 1664 | NUM | number rule | number rule: lexicon.number_words.number_is_learnable(de) is False (Honeyeater 25ec0b1) |
| 13486 | Adventure | 1655 | PROPN | review drop | agreed: English |
| 13963 | Quick | 1621 |  | exclusion (English) | agreed: English |
| 14870 | Launch | 1486 |  | exclusion (English) | agreed: English |
| 15615 | Horse | 1393 |  | exclusion (English) | agreed: English |
| 16631 | Impact | 1277 |  | exclusion (English) | agreed: English |
| 16796 | Lenin | 1216 | PROPN | review drop | agreed: person |
| 18756 | Haag | 1047 | PROPN | review drop | agreed: place name |
| 19298 | Engineer | 1043 |  | exclusion (English) | agreed: English |
| 19307 | FX | 1008 | PROPN | review drop | agreed: acronym |
| 19650 | Elmar | 982 | PROPN | review drop | agreed: first name |
| 19835 | Guy | 1007 |  | exclusion (English) | agreed: name |
| 21152 | Dobrindt | 891 | PROPN | review drop | agreed: surname |
| 21957 | CCC | 847 | PROPN | review drop | agreed: org |
| 22482 | Pennsylvania | 852 |  | exclusion (English) | agreed: US state |
| 23557 | Budot | 767 | NOUN | review drop | agreed: spam junk |
| 24516 | Buck | 727 | PROPN | review drop | agreed: name |
| 24885 | Lugano | 712 | PROPN | review drop | agreed: foreign city |
| 25693 | Dietz | 682 | PROPN | review drop | agreed: surname/publisher |
| 25874 | BU | 676 | PROPN | review drop | coordinator correction: the surface forms are the English word or a name (top form 'bu');  |
| 26374 | Djokovic | 657 | PROPN | review drop | agreed: person |
| 27752 | eg | 614 | PROPN | review drop | agreed: junk (EG) |
| 27808 | UX | 612 | PROPN | review drop | agreed: technical acronym |
| 28936 | TI | 579 | PROPN | review drop | agreed: abbreviation |
| 29231 | Ferguson | 570 | PROPN | review drop | agreed: surname |
| 29700 | Yellow | 584 |  | exclusion (English) | agreed: English |
| 29995 | Valentina | 550 | PROPN | review drop | agreed: first name |
| 30380 | Dylan | 540 | PROPN | review drop | agreed: person |
| 30513 | Beckham | 537 | PROPN | review drop | agreed: surname |
| 30681 | Neuhausen | 533 | PROPN | review drop | agreed: town |
| 30963 | Tabs | 527 | PROPN | review drop | agreed: English plural, tech |
| 30979 | siebzehnhundertfünfzig | 527 | NUM | number rule | number rule: lexicon.number_words.number_is_learnable(de) is False (Honeyeater 25ec0b1) |
| 31083 | dreihundertfünfzigtausend | 525 | NUM | number rule | number rule: lexicon.number_words.number_is_learnable(de) is False (Honeyeater 25ec0b1) |
| 31179 | Wowereit | 523 | PROPN | review drop | agreed: surname |
| 31352 | Geißler | 518 | PROPN | review drop | agreed: surname |
| 31405 | Gloss | 517 | PROPN | review drop | agreed: brand/English |
| 31497 | ICQ | 515 | PROPN | review drop | agreed: obsolete brand |
| 32960 | Wendler | 485 | PROPN | review drop | agreed: surname |
| 33939 | Sega | 466 | PROPN | review drop | agreed: company |

## Merges: 1,314 applied (877 from review, 437 umlaut/ß folds)

Largest review merges:

| source | target | source freq |
|---|---|---:|
| UND | und | 18465 |
| Schwarz | schwarz | 17192 |
| Services | Service | 16654 |
| DER | der | 16055 |
| International | international | 14854 |
| sex | Sex | 13382 |
| raum | Raum | 13047 |
| Onlin | online | 11775 |
| Digital | digital | 10953 |
| FÜR | für | 10861 |
| Smart | smart | 10852 |
| Global | global | 7407 |
| IN | in | 7390 |
| Jung | jung | 6877 |
| MIT | mit | 6629 |
| German | Germane | 6526 |
| Wild | wild | 6428 |
| TOP | Top | 6091 |
| Geweb | Gewebe | 6067 |
| alle | all | 6026 |
| Braun | braun | 5879 |
| Lange | lange | 5679 |
| HIER | hier | 5677 |
| Real | real | 5414 |
| Ausserdem | außerdem | 5382 |
| VON | von | 5272 |
| Extrem | extrem | 5109 |
| Sports | Sport | 4942 |
| teilweis | teilweise | 4817 |
| NEU | neu | 4675 |

Largest umlaut/ß merges:

| source | target | source freq | evidence |
|---|---|---:|---|
| Gunter | Günter | 691 | accented spelling 9,395 vs 691 |
| Gartner | Gärtner | 643 | accented spelling 6,048 vs 643 |
| Lucke | Lücke | 520 | accented spelling 12,605 vs 520 |
| Kohler | Köhler | 512 | accented spelling 3,870 vs 512 |
| Gunther | Günther | 483 | accented spelling 8,814 vs 483 |
| OVP | ÖVP | 433 | accented spelling 5,088 vs 433 |
| Gruner | grün | 431 | accented spelling 5,556 vs 431 |
| Bader | Bad | 409 | accented spelling 2,936 vs 409 |
| Giessen | gießen | 310 | accented spelling 19,402 vs 310 |
| massgeschneiderte | maßgeschneidert | 295 | accented spelling 3,949 vs 295 |
| beschworen | beschwören | 288 | accented spelling 1,942 vs 288 |
| anlassen | Anlaß | 277 | accented spelling 2,665 vs 277 |
| Grossmutter#mother | Großmutter | 277 | accented spelling 5,784 vs 277 |
| Tribune | Tribüne | 274 | accented spelling 2,362 vs 274 |
| gewahr | Gewähr | 273 | accented spelling 16,174 vs 273 |
| heissem | heiß | 261 | accented spelling 2,213 vs 261 |
| naechsten | nächst | 260 | accented spelling 101,314 vs 260 |
| Fussballspiel | Fußballspiel | 259 | accented spelling 2,409 vs 259 |
| mittelgross | mittelgroß | 254 | accented spelling 3,494 vs 254 |
| weissem | weiß | 252 | accented spelling 2,778 vs 252 |

## Reviewer and adjudicator questions

```
# question einunddreißigste: ordinals above 30 follow the cardinal rule? kept as it is a calendar date (31st)
# question Bundesrepublik Deutschland: multiword place/state name, kept as official state name
# question IT: kept as everyday acronym, examples mostly English "it"
# question zwanzigste: ordinals dreizehnte-zwanzigste and dreißigste kept, compound ordinals (einundzwanzigste etc.) dropped by analogy with the cardinal rule; confirm
# question IT: lemma mixes German acronym IT and English it; kept as the acronym
# question Telekom: company, but analogous to Deutsche Bahn; kept as nationally referenced.
# question Jesus Christus: religious figure, dropped as a person name under the rules.
# question US: examples are junk, kept as the USA abbreviation seen in US-compounds.
# question Jesus Christus: religious figure, dropped under people rule
# question Telekom: national company, dropped as company
# question zB: lowercase abbreviation of z. B.; kept as daily-read abbreviation, may duplicate zum Beispiel
# question Sowjetunion: country-like place name not on the reviewed list; kept as ordinary historical common noun
# question DB: ambiguous (Deutsche Bahn vs dB vs Datenbank); dropped
# question WDR: regional ARD broadcaster, nationally famous? dropped as minor organisation
# question Sowjetunion: historic state not on place list; kept as common noun-like
# question DB: kept as Deutsche Bahn but examples mix dB and Datenbank
# question Atlantik: ocean, which the rules say were already moved to the reviewed list, yet it appears here; kept as obviously learnable
# question Dublin: capital of Ireland; rule says any remaining place name drops, but capitals like Dublin, Budapest, Bangkok, Shanghai, Miami may deserve the reviewed list
# question Atlantik: rules say oceans were already removed from the batch, yet it appears; kept as an obviously learnable word
# question Amnesty International: multiword organisation name; dropped as not a single-word national institution
# question Fick: vulgar but real word; kept per the real-word rule
# question KfW: nationally famous state bank or company-like organisation? kept as famous institution
# question Korea: major country but it was still in the batch; dropped per rule, check it is on the places list
# question wieviel: kept as spelling variant; no merge target since wie viel is two words
# question CIA: foreign organisation acronym, dropped; EU/UNO/NATO kept
# question taz: newspapers (taz, Handelsblatt) dropped as brands; are national newspapers "nationally famous institutions"?
# question Greenpeace: dropped as NGO name; is a famous international NGO an institution to keep?
# question Potential: kept as accepted spelling of Potenzial; merge if Potenzial is already on the list?
# question taz: national newspaper, brand or institution?
# question Greenpeace: major NGO; kept as nationally famous organisation
# question sechzigste: ordinal form, no obvious dictionary lemma
# question Potential: variant of Potenzial, merged
# question Hamas: foreign organisation, not a German institution, but constant in news; kept
# question NABU: nationally known NGO; dropped as minor organisation like AWO
# question Dax: stock index, not an institution; kept as everyday news word
# question UEFA: international sports body, not a German institution; kept with DFB-Pokal and MDR as nationally known names
# question Auschwitz: widely meaningful place name but not on the place list; dropped per rule
# question Skandinavien: well-known region absent from place list; dropped per rule (same for Nordafrika)
# question Pazifik: ocean/region (Pazifik, Südostasien) kept although not on the place list; rule says drop any place seen
# question CVP: Swiss party kept as nationally famous; PKV kept as everyday insurance term, BKK dropped
# question Online-Händler: kept hyphenated Online- compounds as ordinary nouns but dropped jargon ones (Android-Smartphone, Session-Cookie, PDF-Format); boundary unclear
# question Steuereinnahme: plural-dominant noun; kept as dictionary lemma, merge to Steuereinnahmen not needed
# question Versicherungsbedingung: same plural-dominant case, kept
# question EKD: kept as nationally famous church body; could be judged minor organisation
# question Weißrussland: country not on the reviewed list per rules; dropped, but may deserve keep or merge into Belarus
# question Sahara: major region/geographic name seen despite rule; dropped
# question Arktis: major region, but place names still in batch are not on the reviewed list; dropped per rule
# question Sibirien: same as Arktis
# question Kanar: merged to Kanaren, a place name that may not be on the place list (then drop)
# question Hesse: inhabitant of Hessen (common noun) vs mostly Hermann Hesse; dropped
# question Arktis: place names not on the list drop by rule, but Arktis, Sibirien, Südfrankreich are well-known regions a learner may want
# question Kanar: merged-looking to Kanaren but place-name rule says drop; dropped
# question neunzigste: ordinal 90 lemma in inflected form; dropped as low value
# question weltgroß: weltgrößte/drittgrößte superlative compounds are common but have no clean lemma; dropped
# question Scree: merged to Screen (loan) which may not be on the list
# question Alb: Schwäbische Alb is a region name, dropped per place rule
# question Westdeutschland: major region name; rules say any place name still in batch is not on the reviewed list so dropped, though it is an everyday word
# question Pentagon: kept as a widely used institution word although it is not German
# question WWW: kept as an everyday acronym; examples are only URLs
# question Allahs: deity names (Allah, Zeus) are neither people nor common nouns; dropped both
# question ZB: abbreviation of zum Beispiel; kept as read daily, but lemma is the abbreviation not a word
# question CM: lemma is the unit cm; kept as an abbreviation read daily
# question MG: lemma is the unit mg; kept as an abbreviation read daily
# question ALG: dropped as bureaucratic abbreviation (Arbeitslosengeld), could be kept as everyday acronym
# question Tour de France: multiword event name, kept as nationally famous; confirm multiword lemmas are allowed
# question zweitgroß: lemma is a superlative-only stem (zweitgrößte); kept as is, same for zweithoch, weltgrößt, letztgenannt.
# question Hbf: kept as an everyday station abbreviation; QM and Mo-Fr dropped as comparable abbreviations, confirm policy.
# question Remote: dropped as not established German; could be kept like Team/Event if the developer disagrees.
# question zweitgroß: superlative-compound adjectives (zweitgroß, weltgrößt, zweithoch) occur only inflected; kept as lemmas, confirm convention
# question Mazedonien: country but not on reviewed place list; dropped per rule
# question LINZ: merged to Linz on the assumption it is a major Austrian city on the reviewed place list; drop if not
# question EU-Verordnung: kept the standard hyphenated compounds (EU-Verordnung, EU-Ausland, U-Bahn-Station, Software-Update, Web-Browser) and dropped tech/marketing/bureaucratic ones; rule on hyphenated compounds is not fully settled
# question BER: kept as nationally known airport abbreviation; could be seen as place name
# question Giessen: could be the verb giessen at sentence start or the city Gießen; treated as city
# question RAF: kept as famous German group but also Royal Air Force
# question DFL: kept as nationally known football body; borderline
# question (adjudicator) of: frequency far exceeds Ofen; most occurrences are likely English "of" — merging inflates Ofen (same concern for not, or, as, ten, has, back, fun, first, who, Turn, check)
# question (adjudicator) einundzwanzigste: rules keep ordinals but drop compound cardinals; unclear whether compound ordinals (incl. 31st) count as spelled-number compounds
# question (adjudicator) Telekom: unclear whether former state companies (Telekom) and private broadcasters (RTL) fall under nationally famous institutions
# question (adjudicator) CIA: unclear whether foreign/international organisations (CIA, NSA, Greenpeace, WWF, UEFA) count as famous institutions; NABU, AWO, BMBF dropped as minor
# question (adjudicator) Tokyo: foreign spelling of a list city (Tokio, Peking for Beijing) — drop per rule or merge into the listed German name?
# question (adjudicator) ZUM: should contractions zum/am be their own lemmas or merge into zu/an?
# question (adjudicator) Spambot: real compound but frequency is all template text
# question (adjudicator) Photovoltaik-Anlage: rules do not say whether valid hyphenated spelling variants (also Fitness-Studio, Web-Browser) should merge into the closed form to avoid duplicate list entries
# question (adjudicator) Tour de France: are nationally famous events treated like nationally famous institutions?
# question (adjudicator) Jehova: is a divine name in a fixed phrase (Zeugen Jehovas) a learnable term or a name to drop?
# question (adjudicator) QM: should a unit abbreviation merge to its abbreviation (qm) or to the full word (Quadratmeter)?
# question (adjudicator) Standart: common misspelling of Standard, but examples also show Standarte; merge:Standard if a dominant misspelling may be merged
# question SRG: Swiss national broadcaster; kept as nationally famous institution though not German
# question Software-Entwicklung: merged to Softwareentwicklung (standard closed spelling)
# question Hostingkunde: dropped as niche template text; could be kept as a plain compound noun
# question Programmierkenntnis, Witterungsbedingung: kept as singular lemmas of plural-dominant nouns
# question Anmeldedat, Bestelldate, Messdat, Reisedat: merged to plural *-daten* forms as the natural lemma
# question DW: Deutsche Welle is a national-ish broadcaster but acronym is 2 letters; kept as famous institution.
# question DLRG: kept as nationally famous; borderline vs minor organisation.
# question GDL: kept as nationally famous union in news; borderline.
# question Botswana: country shown in batch although not on the reviewed place list; dropped per rule
# question Punkto: merged to puncto, which may not be on the list
# question FED: kept as widely named foreign institution; drop if foreign central banks do not count
# question office: only Home Office/Oval Office usage, dropped as non-German standalone
# question Westjordanland: well-known region but rules say unlisted place names drop
# question Westjordanland: major region but not on the reviewed place list; dropped per rule
# question Paul-Ehrlich-Institut: kept as nationally known federal agency; hyphenated proper name
# question Lichtenstein: mostly a town/surname; Liechtenstein misspelling in one example, dropped
# question Burkina: fragment of Burkina Faso; if that country is on the place list, merge there
# question (adjudicator) US-Unternehmen: rules don't say whether transparent hyphenated news compounds (US-Unternehmen, EU-Ebene, Online-Ausgabe) are kept or dropped as hyphenated compounds
# question (adjudicator) Youtube-Kanal: brand + common noun compounds (Google-Suche, Youtube-Kanal) appear in everyday sentences; dropped as brand compounds, unsure
# question (adjudicator) DVB-T: line between consumer and specialist technical acronyms (DVB-T, HDTV) is not set
# question (adjudicator) FED: rules list international bodies (EU, UNO, NATO) but not foreign national institutions often named in German news (Fed)
# question (adjudicator) GDL: whether a union famous mainly through strikes counts as a nationally famous institution
# question (adjudicator) BewohnerInne: Binnen-I gender form covers both Bewohner and Bewohnerin; unclear which lemma it merges into
# question (adjudicator) nchst: list's citation form for superlative adjectives (nächst/nächste, allerbest/allerbeste) unclear
# question (adjudicator) Tara: rare common noun mostly outweighed by name usage; unclear whether to keep
# question Zeugen Jehovas: nationally known religious body or minor organisation? dropped as organisation name
# question EUROPA: uppercase variant of Europa, merged rather than dropped as place name; fine if Europa already on the place list
# question Backstag: Backstage merged as established loan; drop if Backstage is judged not established
# question Werbeeinnahme: kept as singular lemma though only plural Werbeeinnahmen occurs; could merge to the plural
# question (adjudicator) Frauenkirche: rules cover place names and famous institutions but not nationally famous landmarks/buildings; treated as a place name (drop)
# question (adjudicator) Software-Entwickler: should a valid hyphenated spelling of a compound merge into the solid form (Softwareentwickler) when both lemmas exist?
# question wallen: lemma is a real verb but all examples are the English Wallet; dropped
# question DS-GVO: nationally known acronym (DSGVO) but only template legal text here; dropped
# question zweitgroß: real forms are zweitgrößt-; kept the clipped lemma (and zweithoch) as written, merge to zweitgrößt/zweithöchst may be intended
# question (adjudicator) losen: examples show the adjective lose mis-lemmatised as losen; rules forbid merging different words, so kept, but the counts may belong to lose
# question (adjudicator) Satan: rules drop religious/cultural figures but Satan is also used as a common noun; is it a name or a word here?
# question (adjudicator) RSS-Feed: RSS is not on the specialist-acronym list (HTML, SEO, URL, CSS, SSL); does a compound on a specialist acronym drop with it?
# question (adjudicator) EU-DSGVO: DSGVO is widely known in German; are law/regulation abbreviations names (drop) or acronyms used as words (keep)?
```

## Learnable names (developer ruling 2026-11-02)

Honeyeater `reference/learnable-names/de.json` @ 25ec0b1, 761 names (with the developer's 12 added places): 370 already in
the cleaned top 30k. Single-token names not in the 30k: 168 counted below the cut (appended with their counts), 112 never
counted (appended as bare forms), 42 counted under another lemma (listed with that lemma; mostly case or plural:
*Armenisch* under *armenisch*, *Karpaten* under *Karpate*; a few owners are junk lemmas, *Anden* under *And*, *Ewe* under
*EWE*): `learnable-names-append.tsv`. 69 multiword names (19 already emitted as units by 1.5.1, e.g. *Europäische Union*
11,622; input for release 1.6): `learnable-multiword-names.tsv`.

## Round 4 (developer rulings of 2026-11-02)

165 hyphenated compounds dropped only for the hyphen were re-judged like any other word (97 now kept, e.g.
Android-Smartphone, PDF-Format); 317 review keeps whose earlier examples could have come from a rare form were re-checked
with the fixed extractor (5 now dropped, 2 merged). Rulings applied directly: the 12 places and 10 institutions kept,
ordinals from 31 up and 20 abbreviations dropped, superlative-only stems kept; number rule from Honeyeater 25ec0b1
(1,028 drops in the top 60k).
