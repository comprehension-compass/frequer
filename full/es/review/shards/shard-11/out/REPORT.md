# es review shard 11: report (round 15, cascade)

Branch `es-review-shard-11`, created from `origin/full-es` at `b65e7ed`. The rules files are unchanged since
0095cdd. The container had been replaced since shard 7, so I ran the setup script fresh into `$HOME/es-review-11`.
All `review.py` lines passed `--rules` and `--decisions keep,drop,merge`. There were no failed calls and nothing
was rerun.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 537 |
| flagged with an example | 446 (83.1%: **under the ~85% mark**) |
| flagged reviewers agreed | 516 (drop 445, merge 47, keep 24); 21 sent to the adjudicator; 1 accent-only merge (borax → bórax) |
| flagged queried at the gate | 2 |
| flagged adjudicated (21 disagreements + 2 queries) | 23 (keep 5, drop 13, merge 5) |
| **flagged final** | **keep 27, drop 458, merge 52** |
| unflagged screened | 632 (3 batches, 0 failed) |
| suspects (either screener) | 354 (297 marked by both) |
| suspects with an example | 299 (84.5%: **just under the ~85% mark**) |
| unflagged reviewers agreed | 335 (drop 163, merge 100, keep 72); 19 sent to the adjudicator; 8 accent-only merges |
| unflagged queried at the gate | 6 |
| unflagged adjudicated (19 disagreements + 6 queries) | 25 (keep 5, drop 13, merge 7) |
| **unflagged final** (suspects only; the 278 non-suspects stay keep) | **keep 77, drop 172, merge 105** |

## Gate

I read every agreed merge and keep in both rounds and all the agreed drops (lemma and reason). I checked forms
where a drop or merge might hide a real word (bozo, orito, multiplica, seleccione, paternoster, chachapoya,
desagradecer, escofinar, trimar, ajuarar, bumer, mueso, cuera, ...); those decisions hold. The accent-only merges
(flúido, carácteristica, genetica, edifício, télefono, ...) are plain misspellings.

Flagged queries → adjudicator:
- mollar (agreed keep; only ~10% lowercase, the rest place names) → **drop**.
- orece (agreed keep as an international body; ORECE = BEREC) → **drop** (specialist EU agency).

Unflagged queries → adjudicator:
- bazucar (agreed merge:bazuca; 15 of 84 are bazuco, the drug) → **merge:bazuca**, with a split question bazuco → bazuco.
- afgani (agreed merge:afgano; afgani is also the currency) → **merge:afgano** (the currency reading is well under a third).
- enmarcación (agreed drop as a calque) → **keep** (ordinary Spanish for framing).
- antipasto (agreed drop as Italian) → **keep** (established culinary loan, Spanish plural).
- gratu, edifi (agreed drop; cut-off fragments) → **drop** (several merge targets fit, so none is obvious).

## Things for the coordinator

- Example coverage is under ~85% in both queues (83.1% and 84.5%). Per the instructions I noted it and carried on.
- Split-by-form questions (ruling 2), which the coordinator writes: bazucar (bazuco → bazuco), mahonés
  (mahonesa → mahonesa); emplomar also holds the noun emplomado.
- Possible new classes of question:
  - diminutives that have their own lemma (arquita, huequito, bebito): keep, or merge into the base?
  - a brand used as a common noun but lowercase only ~14% (scalextric): does the one-third ruling apply?
  - where the line between common and specialist generic drugs falls (ketorolac, esomeprazole, apixaban,
    nitrofurantoin, valaciclovir, pantoprazol);
  - English business phrases as multi-word units (in-company).
- Two -os clitic forms again: dirigíos → dirigirse, hacédmelo → hacer (see shard 7 on ofreceros).

## Every `# question` line

The question lines are in `s11-flagged/questions.txt` (65 lines) and `s11-unflagged/questions.txt` (58 lines),
reproduced below.

### s11-flagged
```
# question adhan: Spanish more often writes "adhán" or "azán"; kept as written, the rules do not settle the standard spelling.
# question adhan: could be treated as a specialist religious term; kept as an established loan
# question anti-gay: could merge to antigay if the list wants that spelling; dropped as hyphenated
# question audior: lemma is a bogus verb; the form written is "Audio", so merge into the noun/adjective audio
# question auh: Argentine national program (Asignación Universal por Hijo) versus airport code; dropped as a program, not a body
# question avo: could be the Spanish fractional noun (avos), but the evidence is mostly capitalised names and no examples were shown
# question avo: no examples shown; kept as the fraction suffix noun (dieciseisavo), but the capitalised "Avo/Avos" forms may be names
# question beta-sitosterol: dropped as a specialist ingredient; it could count as a common supplement ingredient (keep).
# question beta-sitosterol: hyphenated form of a specialist-ish compound; kept as a common supplement ingredient, but could be a specialist term to drop or a merge to "betasitosterol".
# question bribri: a people and language name rather than a lowercase ethnonym; kept as an ethnonym but capitalised 72% of the time.
# question chachapoya: ethnonym/ancient culture; capitalised 78% so treated as proper noun, but lowercase ethnonyms keep could apply
# question chachapoya: historical people (Chachapoyas) also a place/region; dropped as proper noun, though lowercase ethnonyms keep (could be keep if treated as ethnonym)
# question clematis: only one example shown, plant reading appears to be the majority (38% lowercase), kept; the lemma could also be filed as clemátide in Spanish.
# question co-estrella: coestrella is the usual Spanish spelling, but "co-estrella" may be rare; confirm the target exists
# question co-estrella: target coestrella chosen as the standard closed spelling; confirm it is the preferred form.
# question cocef: binational US-Mexico body, so it may count as an international body; judged not a household name and dropped.
# question conaculta: defunct national body, kept as a household-name public body
# question conaculta: defunct since 2015 and only borderline a household name; kept as a national public body
# question contra-ángulo: hyphenated; could be seen as a compound of two listed words (contra + ángulo) and dropped, or merged to "contraángulo"; kept as a distinct dental term.
# question creepypasta: borderline between an established loan and a niche internet term; kept because it takes Spanish plural creepypastas
# question creepypasta: kept as an established internet loan, but most examples come from a wiki name.
# question escooter: possibly an adapted loan for electric scooter (escúter); dropped as mostly product names.
# question ex-empleado: the hyphenated-compound drop rule might apply, but ex- is a prefix and exempleado is the standard spelling, so I merged it
# question ex-post: merge target "ex post" assumed to be the standard written form; "ex ante" would be its pair.
# question ex-post: rules say hyphenated compounds of two listed words drop, but this is a Latin phrase variant; kept, coordinator may want to merge into a multi-word target "ex post".
# question fnmt: FNMT (Fábrica Nacional de Moneda y Timbre) is a national Spanish body and might count as a household-name institution; dropped as less widely referred to by name.
# question full-duplex: could be a unit "full dúplex"; dropped as a specialist networking term.
# question go-kart: assumed the list's standard form is kart; if the list uses karting or go-kart as a unit, adjust.
# question go-kart: target kart assumed to be the listed standard form; could instead be go-kart/kárting
# question hihat: could instead merge into the hyphenated spelling hi-hat if that is the list's standard form; kept as written
# question hihat: loan used by drummers, borderline established; dropped as a specialist term.
# question in-company: borderline loan; kept as established in Spanish business-training usage
# question incaa: kept as a national body, ruled by analogy with ETECSA
# question lobelia: capitalised in 60% of examples with the sole example being a place name; kept since lowercase plant reading is about 40%.
# question mesolítico: tagged PROPN but a normal adjective/noun; kept as common word.
# question metalcore: borderline loan for a learner; kept as an established genre name
# question metalcore: genre name, borderline loan; kept as established music term
# question mollar: real adjective mollar (granada mollar) is only part of the examples; the other examples are place names and a surname, so kept on the one-third rule
# question nsfw: kept as a common internet acronym; it could also be treated as a specialist acronym.
# question olmeda: common noun (elm grove) is a minority of examples; dropped as the place/villa name
# question paternoster: real word paternóster (prayer) is a small minority of the examples, so dropped.
# question pre-incas: target preinca is uncertain; preincaico may be the more common adjective
# question razia: no example sentences show the common-noun reading; kept only on the lowercase share (razia and razias)
# question razia: razias (14 of 83) is a real Spanish word (raid, roundup), but it falls below a third of the examples; dropped.
# question romanesco: mixed readings (dialect, adjective, vegetable); kept because the adjective/dialect reading is a large share of examples
# question room-service: the target "room service" assumes Spanish writes it as two words; the hyphenated form could instead be treated as a hyphenated compound and dropped.
# question scalextric: a brand, but "un scalextric" is a common noun for a slot-car set in Spain; kept on that basis, drop if the rule is brand-only.
# question scalextric: brand that is used as a common noun for slot-car sets in Spain; dropped as a brand, but could be kept if the developer treats it like kleenex (clínex).
# question seleccione: all-caps UI imperative; dropped rather than merged to seleccionar as it is a conjugated form filed as a lemma, merge:seleccionar could also apply
# question seleccione: all-caps imperative of seleccionar, a real verb form filed as lemma; could be merge:seleccionar
# question shhh: no clear Spanish lemma for this interjection; I guessed chsss, but if the list has no such entry, drop or keep as its own entry (shh) may be better
# question shibari: it could be an established loan for a learner, but it is a niche term, so I dropped it.
# question súper-tierra: the target "supertierra" may not exist as a lemma; if it does not, drop is the alternative.
# question tawhid: established Islamic term in Spanish texts, but mostly capitalised in names; dropped
# question tawhid: religious term mixed with a militant group's name; kept as an established loan
# question teórico-prácticas: could merge to teórico-práctico, but the rule says hyphenated compounds of listed words drop
# question thermos: brand and also generic, merged to termo as an adapted-spelling common noun
# question thermos: brand used as common noun; merged to termo (adapted spelling) though many examples are the brand Thermos
# question u-boat: hyphenated, mostly capitalised; Spanish also uses U-Boot, so it is unclear whether the loan is established enough to keep
# question uniéndono: merge target unirse chosen because unirse is the common pronominal verb; the examples (uniéndonos a él) fit it, though plain unir is also possible.
# question uniéndono: unirse chosen as pronominal verb since "uniéndonos" is mostly reflexive/with a (unirse a)
# question yupi: examples look partly like a site name/yuppies; kept for the interjection reading
# question yupi: the examples mix the interjection, "yuppies" and a game-site brand; kept on the interjection reading
# question in-company: should established English business phrases written unhyphenated in Spanish (in company) become a multi-word unit, or drop as not established for a learner?
# question scalextric: brand used generically in Spain but lowercase only ~14%; does the one-third ruling apply to brand-as-common-noun cases where capitalised uses may still be generic, and is there an adapted spelling (escalextric) to merge into?
```

### s11-unflagged
```
# question alisal: both place name and common word (alder grove); kept as common word.
# question arquita: biblical gentilic (arquitas) is most of the evidence; a diminutive of arca is possible, but I could not confirm it.
# question arquita: biblical gentilic that may be better handled as an ethnonym entry; kept as lowercase ethnonym
# question bazucar: bazuca (weapon) and bazuco (drug) are different words; I merged into bazuca as the majority form, and bazuco may need its own entry.
# question bazucar: split by form: bazuco -> bazuco
# question bebito: diminutives are not covered by the merge rules, so I kept it as a common word.
# question cigarillo: cigarillo is also a real word for a small cigar, but the examples use it as a variant of cigarrillo, so I merged it
# question corion: accent form córion is also attested; kept as the written form corion
# question directorado: rare and not clearly in the academy dictionary, kept as a real word; the developer may want it checked
# question dirigío: the source forms are dirigíos, which could be dirigir or dirigirse; chose the pronominal verb because the examples use "dirigíos al/a".
# question druid: capitalised Druid looks like a game class or name; merged to druida following the English-spelling rule.
# question emplomar: forms are all participles/emplomado noun; kept as verb lemma.
# question emplomar: lemma holds the verb and the noun emplomado (leading); kept as the lemma's own reading.
# question enmarcación: could merge:enmarque (standard word) but the web-sense "framing" is not clearly the same word; dropped
# question esomeprazole: merged to esomeprazol as a common generic drug; drop instead if the developer treats it as specialist.
# question fashionistas: unsure fashionista is established enough as a loan; merged on the assumption that it is
# question grañón: place names Grañón/Grañones vs. the common word grañón (cooked wheat); roughly half each, kept as the common word
# question hacédmelo: merged into hacer, but the clitic form hacédmelo saber could also be read as imperative of hacer only; chosen hacer as plain verb.
# question hacédmelo: vosotros imperative + clitic; merged to plain verb since hacerse-style pronominal reading does not apply.
# question huequito: diminutive kept as its own entry; the rules do not say whether diminutives merge into the base word (hueco)
# question influente: influyente is the standard Spanish form; confirm whether influente should instead merge:influyente
# question ketorolac: specialist-leaning drug; merged to the Spanish spelling as a common generic NSAID
# question laodicense: gentilic of a place name (Laodicea), not a place itself; kept as a lowercase ethnonym, mostly biblical use.
# question mahonés: forms are mostly mahonesa (the sauce, a separate common word); split by form: mahonesa, mahonesas -> mahonesa
# question mandarino: capitalised Mandarino (about 30%) may be a surname or the language name; kept as the lowercase common word.
# question mandarino: the examples are mostly the tree, but could also be a plural filed from mandarina; kept
# question ministre: the examples are Spanish subjunctive of ministrar, but the screener read it as Catalan or French; I merged it on the Spanish reading.
# question mousepad: it is an established loan, but the examples are mostly product listings, and Spanish also has alfombrilla de ratón.
# question nitrofurantoin: it may count as a specialist drug; I merged it on the basis that it is a common generic antibiotic.
# question pantoprazol: common generic drug or specialist? I kept it as widely prescribed, like omeprazol.
# question perdónenme: merged to perdonar, the plain verb.
# question perlante: could be an adjective for water-beading fabric, but it looks like French or Italian, and the evidence is one example.
# question portacable: could instead be a brand or fragment of portacables; kept as a technical compound
# question portacable: plural portacables is the usual dictionary form; kept as a real compound.
# question pragmáticamente: adverb tagged ADJ; kept as its own entry, though one could merge it into pragmático.
# question processo: examples are Spanish text with Portuguese or Italian spelling; dropped rather than merged to proceso.
# question purpurear: forms are mostly Echinacea purpurea (Latin taxon) rather than the adjective purpúreo; merge to purpúreo may be wrong, drop could be better
# question santifícalo: forms santifícalos/santifícalo are imperatives with clitic; santificar chosen as plain verb
# question seguiriya: the screener suggests merging into siguiriya, but seguiriya is the form written here and is the academy's main form, so I kept it.
# question setlist: borderline loan; kept as established in music contexts
# question setlist: kept as an established music loan, but the one example is English-like; the rules don't clearly settle it.
# question silesio: the lemma mixes the place Silesia with the gentilic silesio; the place reading is the majority, so I dropped it
# question snackbar: borderline loan; examples are mostly Dutch/camping contexts, so dropped
# question suavecito: many examples are the song or band name Suavecito; kept because the real diminutive reading looks like about a third of the examples
# question swatche: unsure swatch is established enough as a loan; merged on the assumption that it is
# question syllabus: could be merge:sílabo if the team wants an adapted spelling; dropped as not established in Spanish
# question syllabus: the Latin loan is used in academic Spanish, though Latin American usage prefers "sílabo"; I kept it.
# question tene: could be a name or a fragment as well as voseo tené; merged into tener as the most likely reading
# question tirio: could be argued as a place-related gentilic of Tiro, kept as lowercase ethnonym
# question transformante: kept as adjective though tagged ADV; participle-like adjective use is the real reading.
# question transformante: only ~1 example, but form is a real adjective; kept.
# question trimar: lemma holds trimarán (noun) and a minor verb trimar; decided by majority form
# question trolleys: merged into "trolley" (luggage sense, used in Spain); if the coordinator prefers an adapted spelling, adjust.
# question trolleys: merged into trolley (suitcase sense) on the assumption that trolley is itself a listed loan
# question urbanita: the base form may itself be unlisted; merge assumes urbanita is the target lemma.
# question arquita: do diminutives that have their own lemma (arquita < arca) keep, or merge into the base noun?
# question bazucar: split by form: bazuco -> bazuco
# question ketorolac/esomeprazole/apixaban/nitrofurantoin/valaciclovir: where is the line between a common generic drug and a specialist one? I treated widely prescribed drugs that are not household or OTC names (ketorolaco, esomeprazol) as specialist. Should regionally household drugs such as ketorolaco in Mexico keep under their Spanish spelling?
```
