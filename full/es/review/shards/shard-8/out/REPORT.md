# es review shard 8: report

Branch `es-review-shard-8` (from `04d1ada`). Every `review.py` line ran with `--rules` and `--decisions keep,drop,merge`.

## Rules versions
* **s8-flagged reviewers** ran on the rules at `04d1ada`. The coordinator's message about the second-set rulings came in while this stage was running, and I didn't rerun it, as instructed.
* Before every later stage I checked out `review/rules` from `origin/full-es` (`ad5eb4e`, with the "Developer rulings (second set)" block). That covers the **s8-flagged adjudication**, the **s8-unflagged reviewers** and the **s8-unflagged adjudication**. I didn't commit the rules files on this branch.

## Counts
| step | count |
|---|---|
| flagged queue | 874 (examples 770 = 88 %) |
| flagged reviewers | 855 agreed (drop 755, merge 61, keep 39), 19 disagreements, 3 accent-only merges |
| flagged after adjudication | 841 agreed + 33 adjudicated (19 disagreements + 14 queries), 0 undecided |
| flagged final | keep 41, drop 760, merge 73 |
| unflagged screened | 982 (4 batches, 0 failed); candidates 484 (both screeners 415) |
| suspects examples | 432 / 484 = 89 % |
| unflagged reviewers | 457 agreed (drop 224, merge 142, keep 91), 27 disagreements, 13 accent-only merges |
| unflagged after adjudication | 445 agreed + 39 adjudicated (27 + 12 queries), 0 undecided |
| unflagged final | keep 98, drop 236, merge 150 (unscreened unflagged lemmas stay keep) |

Both example shares are above 85 %.

## My queries (gate) and outcomes
### s8-flagged

| lemma | why queried | adjudicated |
|---|---|---|
| lato | agreed drop, but lato is a real Spanish adjective ("en sentido lato"); check whether the real reading is a third or more of the examples | drop: Overwhelmingly the Lato font; the adjective reading is far below a third |
| hena | agreed drop, but hena (henna, alheña) is a real Spanish noun; check the examples for the common word | drop: Nearly all uses are a name; the common noun is about 5% (Spanish usually writes henna or alheña) |
| minka | agreed drop, but minka/minga (Andean communal work) is a real word in Andean Spanish; check the examples | drop: The only example is a personal name; the Andean common word is about 8%, below a third |
| amhara | agreed drop as a name, but the second-set rulings keep lowercase ethnonyms; check whether this is the people/language noun | drop: Mostly the region; the lowercase people/language noun is about 9% |
| kiowa | agreed drop as a name, but the second-set rulings keep lowercase ethnonyms; check whether this is the people noun | drop: Mostly a product and place name; lowercase ethnonym is about 17% of uses, well under a third |
| ogoni | agreed drop as a name, but the second-set rulings keep lowercase ethnonyms; check whether this is the people noun | keep: Lowercase ethnonym (the Ogoni people) in about 27% of written forms and in the examples; the ruling keeps lowercase ethnonyms |
| khoi | agreed drop as a name, but the second-set rulings keep lowercase ethnonyms; check whether this is the people noun | keep: Lowercase ethnonym (the Khoi people) in 2 of 3 examples; the ruling keeps lowercase ethnonyms |
| toraja | agreed drop as a name, but the second-set rulings keep lowercase ethnonyms; check whether this is the people noun | drop: Mostly the Toraja region; the lowercase ethnonym is about 13% |
| negativos | agreed keep, but it is a plural filed as a lemma, which the rules merge (merge:negativo) | merge:negativo: Plural filed as a lemma |
| jejejeje | agreed drop, but interjections keep and variant spellings merge into the standard one (jeje / jejeje?) | merge:jeje: Laughter interjection; a variant spelling merges into the standard form |
| aprenda | agreed drop, but a conjugated form filed as a lemma is merge:aprender under the rules | merge:aprender: Conjugated form filed as a lemma |
| acción penal | agreed drop as multiword, but the second-set rulings allow two-word lemmas; decide whether it is a lexical unit | drop: transparent legal collocation of two listed words, not a lexical unit like palo santo or alter ego; caps come from headings |
| ex-director | agreed drop, but ex-novio in the same round merged to exnovio; check consistency (merge:exdirector?) | merge:exdirector: hyphenated spelling of exdirector (RAE writes ex- joined to single words); consistent with ex-novio → exnovio |
| horas-hombre | agreed drop as a hyphenated compound, but hora-hombre / horas hombre is an established unit; check keep or merge | merge:hora hombre: Established unit; this is the plural form, merged into the multi-word singular |

### s8-unflagged

| lemma | why queried | adjudicated |
|---|---|---|
| asechar | agreed merge:acechar, but asechar (to lay snares; asechanza) is a separate real verb; check whether the examples are that verb | merge:acechar: no examples; asecha/asechan on the web are overwhelmingly misspelt acechar; the rare snare verb isn't learner vocabulary |
| macero | agreed merge:macerar, but macero (mace-bearer) is a real noun; check whether any examples are the noun | merge:macerar: bulk is macera/maceras of macerar; the mace-bearer noun (Macero, maceros) is a small, largely surname share |
| chapuzar | agreed merge:chapuza, but chapuzar (to dunk) is a real verb; check the forms | merge:chapuza: 116 of 123 are chapuza(s); verb forms (chapuzó, chapuzar) are a negligible share |
| nimbar | agreed merge:nimbo, but nimbar (to surround with a halo) is a real verb; check the forms | merge:nimbo: about 95 of 105 are the noun nimbo; nimbado forms are about 10 |
| taquigrafiar | agreed merge:taquigrafía, but taquigrafiar is a real verb; check whether verb forms are a real share | merge:taquigrafía: 109 of 113 are the noun; verb forms are only 4 |
| patón | agreed drop, but patón is a real Spanish word (big-footed; Bigfoot); check the real reading's share | drop: mostly the place Patones and a surname; real patón/patona is about 13 of 119, well under a third |
| ceto | agreed drop, but ceto is used as a Spanish clipping in "dieta ceto" (keto); check the examples | drop: no examples; looks mostly like the Greek name, CETO and a prefix fragment |
| tias | agreed drop, but it may be tías without the accent (plural, merge:tía); check the examples | drop: mostly the place name Tías; the unaccented tías reading is a small minority |
| jajajajaja | agreed drop, but in the flagged round jejejeje was adjudicated merge:jeje (interjection variant); check consistency (merge:jaja?) | merge:jaja: laughter variant, consistent with jejejeje → jeje |
| eskimo | agreed drop, but it may be the English spelling of esquimal, which the rules merge; check the examples | drop: examples are a yarn brand and a band, not the ethnonym, so no esquimal merge |
| niñ | agreed drop, but it may be a cut niñ@s/niñ*s inclusive form (amigxs was merged to amigo in this round); merge:niño? | merge:niño: cut inclusive form niñ@s/niñ*s, consistent with amigxs → amigo |
| cocin | agreed drop, but it may be a cut fragment of cocina/cocinar with an obvious merge target | drop: cut fragment with no single obvious target (cocina/cocinar/cocinero) |

How I picked them: I read every merge, every keep, every drop lemma and the accent-merges files. I queried agreed decisions that might hide a second real word (lato, hena, asechar, macero and the like), lowercase ethnonyms that the second-set rulings now keep, and decisions that went against a clear rule or against another call in the same shard (plural or conjugated forms kept or dropped instead of merged; ex- prefixes; laughter variants). All the accent-only merges looked right.

## What went wrong
* The first flagged `--adjudicate` call failed because my `queries.tsv` had a `lemma<TAB>why` header line, which the runner reads as a lemma. I removed the header and reran. No other failures.
* Possible inconsistencies the coordinator may want to check at collection:
  * `jejejeje → jeje` and `jajajajaja → jaja` assume that jeje and jaja are on the list.
  * `horas-hombre → hora hombre` is a multi-word target.
  * The clitic merges in the flagged round (aproximarno → aproximar, esforcémo → esforzarse, and so on) were decided on the old rules, before the second-set clitic-target ruling.

## Every `# question` line

### s8-flagged

```
# question abat: Abat Oliba CEU is a university but only a fragment of its name appears, so dropped
# question acción penal: legal collocation that is real Spanish but multiword; dropped because lemmas are single words
# question aprenda: it is a real verb form (aprender) written in capitals in web headings; dropped as an artefact rather than merged to aprender
# question aprenda: real Spanish verb form (aprender) but tagged PROPN from all-caps web headings; dropped as a mis-filed form rather than merged
# question aproximarno: lemma is a cut-off of aproximarnos; merged into aproximar (aproximarse might be the intended pronominal lemma)
# question armagnac: mostly place/name uses, but armagnac (brandy, academy form armañac) is a real word; dropped because the lowercase reading is a minority
# question armagnac: the brandy is a real word, but most examples are the region or a noble house; kept as the common word.
# question armorial: real but rare Spanish word, used here as a website section label; kept
# question asignándol: lemma should be asignar, but rules say merge to the obvious Spanish lemma; clitic gerund filed wrongly
# question back-up: assumed backup is the listed form; unclear whether it is on the list
# question barraco: could be read as a rare common word, but the examples are mostly the place El Barraco, so dropped.
# question batmóvil: fictional vehicle name; kept as common noun since 14 lowercase uses and Spanish-adapted spelling
# question binador: binadora is a noun (a hoeing machine) and 'binadora' as lemma may be intended; merged to it as the obvious form
# question binador: lemma binador is a verb-tagged form of the noun binadora (agricultural cultivator); kept, but could be merge:binadora or drop as too specialist
# question bragado: mostly the Argentine town, but bragado is a real adjective, so I kept it under the common-word rule
# question broccoli: merged to brócoli as the accented adapted spelling; could be kept if the list prefers the English form
# question carmenere: grape variety kept as a common noun; unclear whether wine varieties count as products or names
# question cedi: a currency name, kept as a common noun although it is mostly seen in exchange-rate text
# question cefaclor: a drug name that may be too specialist for a learner list, but it is a generic noun written in Spanish, so I kept it
# question cnbv: a Mexican financial regulator is not as universally famous as UNAM or Hacienda, so I treated it as a public body people refer to by name.
# question cnbv: a Mexican regulator is a public body, but it is unclear whether it is famous enough for the institution rule; kept.
# question co-autora: lemma is feminine; I merged to coautora (the academy-preferred spelling), assuming the masculine/feminine pair is otherwise coautor/coautora.
# question comté: could be a cheese name a learner meets, but mostly place/hotel contexts; dropped
# question consecuenciales: merge target "consecuencial" is a rare adjective; it is only attested in all-caps legal boilerplate, so drop could also fit.
# question crue: Spanish rectors' conference is a public-ish body, but examples include Mötley Crüe, so dropped
# question crue: examples mix the Spanish rectors' conference with Mötley Crüe, kept because the all-caps CRUE majority is the Spanish body
# question d-pad: gaming loan may be established; dropped as niche jargon.
# question dala: real Spanish reading (da + la) is possible, but most uses are the name Dalas, so dropped.
# question dashcam: loan is common in product text but not clearly listed among established loans; kept as a learner-relevant loan
# question dashcam: loan is fairly established for a learner but not as common as chat/blog; kept
# question depa: it is a clipped form of departamento, which the rules would merge, but it is an established colloquial word, so I kept it.
# question dgii: Dominican tax authority is a national public body, but not obviously famous across the Spanish-speaking world; dropped
# question ex-compañero: the rules don't say whether ex- plus a noun is a hyphenated compound of two listed words (drop) or a spelling variant of excompañero (merge); I chose merge.
# question ex-jugador: merged to exjugador; the academy writes ex jugador as two words, so the target spelling is uncertain.
# question frame-rate: hyphenated English loan could be kept as "frame rate"; dropped under hyphenated-compound rule
# question grd: Spanish medical term (grupos relacionados con el diagnóstico) in some examples, but many are a company name, so I dropped it as a specialist acronym.
# question grindcore: genre loan; kept though used mainly by fans.
# question grizzlie: "grizzly" is a Spanish loan for the animal, but the team name dominates the examples (82% capitalised), so I dropped it
# question icbf: Colombian public body, but not as famous as the listed examples; I kept it as a national public body.
# question icbf: it is a national public body, but I'm not sure it is famous enough to count as nationally famous outside Colombia; I chose keep.
# question indh: Chile's national human rights institute is a public body, but not nationally famous enough per the examples; dropped
# question jejejeje: laughter interjection could be kept or merged into jejeje; dropped as a reduplicated variant
# question junquera: mostly La Junquera (a place), but junquera is a real noun, so I kept it under the common-word rule
# question kajal: a cosmetics loan, but nearly half the occurrences are capitalised and some are a personal name
# question kajal: loan for eyeliner, kept as an established cosmetic term, but the evidence is thin
# question latanoprost: a specialist drug name; kept as a common medical noun though only specialists may use it.
# question live-action: loan is hyphenated and Spanish may also write "live action"; kept as an established loan, but the merge-vs-keep call is unclear
# question manzanero: examples are mostly the surname Manzanero, kept as a real common word
# question maruja: mostly a name in the examples, but marujas is a real colloquial Spanish noun; kept as the common word
# question mcerl: educational acronym well known to Spanish learners but not a listed ordinary-word acronym.
# question mcerl: well known to language learners but still a specialist acronym; dropped.
# question michi: Latin American slang for "cat" exists, but 85% capitalised and no examples; dropped
# question minugua: UN verification mission in Guatemala, arguably a famous international body but defunct and little known; dropped
# question morbi-mortalidad: "morbi" is not a listed word, so I merged it into morbimortalidad instead of dropping it as a hyphenated compound.
# question mugs: mixed Spanish "los mugs" and English product-list uses; merged to mug as an established loan, but drop is defensible.
# question negativos: kept as the plural of the adjective/noun negativo, but the lemmatiser may intend negativo as the lemma; the examples are only product-title usage
# question negativos: tagged PROPN, but the evidence is title-cased product text, so treated as the common word.
# question neocon: "neocons" in Spanish prose is a real loan (RAE neocón), but the NeoCon event is the larger share, so I dropped it
# question nicotine: examples are mostly English text; merged to nicotina by the English-spelling rule, though drop is arguable.
# question oedt: OEDT is the Spanish acronym of the EU drugs observatory (EMCDDA); dropped as a specialist body, though it could count as an international body.
# question ofreciéndono: the lemma is a cut-off form of ofreciéndonos; merged to the verb ofrecer
# question olanzapine: a drug name seen only in English-language text; merged to the Spanish olanzapina by the English-spelling rule, though drop is arguable.
# question olanzapine: examples are English-language text; merged into the Spanish drug name olanzapina rather than dropped.
# question poinsettia: Spanish usually says flor de Pascua; dropped as English
# question post-doctoral: merged to posdoctoral, though postdoctoral is also accepted by the RAE
# question pre-pagada: merge target prepagada vs prepago; chose prepagada as the written adjective form, but the lemma might be prepagado
# question pre-selección: merged to preselección, assuming that is the spelling in the list
# question quereteo: a biblical gentilic (Cherethites), only written in the plural; I treated it as a name and dropped it, not as a common word to merge to quereteo.
# question quereteo: biblical gentilic (Kerethites) used as a common noun in the plural; dropped as a proper name, though it could be kept as a people-name noun.
# question remaster: loan established enough in Spanish is borderline; kept as gaming/music loan
# question remaster: loan is marginal; most occurrences are titles of games/product releases, kept as established media loan
# question reseda: most occurrences are the California place name, but the rules keep a real common word that doubles as a place name, so I kept it
# question sanctorum: Latin term in "Sancta Sanctorum" and "Santa Sanctorum"-type phrases; dropped as a fragment, not a standalone Spanish word
# question secam: TV standard acronym, could count as an ordinary technical word like PAL; dropped as specialist.
# question senan: Panama's aeronaval service is a public body, but it is not clearly famous across the Spanish-speaking world, so dropped.
# question sepd: Supervisor Europeo de Protección de Datos is an EU body, but not widely famous; dropped as a specialist acronym.
# question sepd: an EU body, but not a famous international body in the rules' sense; dropped.
# question siii: could be the elongated interjection "sííí" (yes), but examples mostly Samsung Galaxy SIII; dropped
# question slang: English word used as a gloss for "jerga"; could count as an established loan
# question slang: English-learning contexts dominate; unclear whether it counts as an established loan
# question slim-fit: "slim fit" is common in Spanish clothing text but may not count as established enough to keep, so I merged it into the two-word form.
# question slim-fit: hyphenated English fashion loan; kept as an established loan, but "slim fit" may not be on the list as a compound
# question softbox: established photography loan, but mostly product names, so dropped
# question speakeasy: borderline loan; kept since used with Spanish article and plural in examples
# question speakeasy: borderline whether established beyond tourism/bar contexts, kept as loan
# question tai-chi: Spanish writes both tai chi and taichí; chose tai chi as the common form
# question tai-chi: the target form (tai chi vs taichí) is unclear; chose the two-word form.
# question tapatío: demonym of Guadalajara (place-derived) kept as a common adjective
# question udlap: private Mexican university; unclear whether it is nationally famous enough to count as a famous institution, dropped as minor
# question udlap: well-known Mexican university, but private and regional, so dropped as not nationally famous
# question vtv: national broadcaster in Venezuela; kept as a famous broadcaster, though less widely known than RTVE.
# question websocket: technical loan, dropped as specialist vocabulary
# question wto: English acronym for the OMC; dropped rather than merged since the Spanish form is not obviously the same token.
# question zinfandel: a grape name used in Spanish wine writing, but could count as an established loan
# question zinfandel: grape name, borderline as an established loan; kept
# question crue: do national associations (like CRUE, the rectors' conference) count as famous public bodies, or as ordinary organisations?
# question depa: is a colloquial clipping (depa, profe, cole, boli) an "abbreviation of a listed word" to merge, or its own word to keep?
# question ex-director, ex-jugador: should every hyphenated ex- form merge into its joined form (exdirector, exjugador, exnovio)? Both reviewers read "ex" plus a listed word as a hyphenated compound to drop.
# question jejejeje: which laughter form is the standard lemma (je, jeje, jejeje), and should jaja-type variants follow the same target?
# question khoi, ogoni: does "lowercase ethnonyms keep" still apply to obscure ethnonyms when the lowercase share is under a third but the examples show the people reading?
```

### s8-unflagged

```
# question acidular: acidular is also a real verb (acidulate); lemma tagged ADJ with forms acidulado, so merged
# question acidular: split by form: acidulado, acidulada, acidulados, aciduladas -> acidulado (the forms are really the adjective; the verb reading is rare)
# question agremiar: the verb is real, but nearly all forms are the participle/noun agremiado
# question ambo: no examples were available, so the suit reading could not be checked against place-name uses
# question amigxs: inclusive -x spelling isn't covered by the rules; I treated it as a variant spelling of amigo.
# question amigxs: no explicit rule for inclusive -x spellings; merged to amigo as a variant spelling
# question antifouling: specialist boating term; kept as an established loan
# question antifouling: used as-is by Spanish-speaking boaters but only a specialist term; dropped
# question asechar: asechar is a real but rare verb (poner asechanzas), but the forms here are mostly the Latin American use for acechar; no examples were available to check
# question asechar: the dictionary has a distinct verb asechar (poner asechanzas), but the examples read as acechar, so I merged it.
# question autoresponder: it may be an established marketing loan; dropped as web jargon
# question balayage: established enough as a loan is borderline; kept
# question biochar: English technical loan, kept because it takes Spanish plurals, but biocarbón is the alternative lemma
# question birdwatching: dropped because examples quote it as foreign, though tourism text uses it
# question brochado: tagged VERB as a participle of brochar, but all examples are the machining noun "brochado"; kept as a specialist but real technical word, drop could also be defended
# question calmo: lemma calmo tagged VERB but forms are adjective; kept as adjective
# question camita: split by form: camitas, Camita (ethnonym, Ham's descendants) -> camita (ethnonym); the diminutive of cama is the main use, so kept as is
# question casón: most examples are the Casón del Buen Retiro or a hotel name, so the common-word reading may be under a third; kept as a real DLE word
# question casón: real augmentative of casa, but most examples are the Madrid building
# question chapuzar: split by form: chapuzó, chapuzar -> chapuzar (verb, "to dip"); chapuza, chapuzas -> chapuza
# question conexionar: split by form: conexionado, Conexionado -> conexionado
# question conexionar: split by form: conexionado, conexionada -> conexionado
# question customizada: customizar is an anglicism; merged to the verb rather than dropped
# question desgobernar: split by form: desgobierno, Desgobierno -> desgobierno
# question embozar: split by form: embozo -> embozo
# question embozar: split by form: embozo, embozos -> embozo
# question encuenta: some examples are en cuenta and others are encuentra, so there is no single merge target
# question encuenta: some examples are really "encuentra" (se encuenta, Encuenta tu concesionario), so the target could instead be encontrar
# question frittata: Italian loan with no academy entry; kept as common on Spanish menus
# question habitu: habitus is Latin term used in sociology; target kept as its own entry, may deserve drop
# question habitu: habitus is a specialist Latin term in sociology; if the coordinator drops habitus, drop this too
# question hiperlink: could equally be dropped as a non-established hybrid
# question hiperlink: merge target could be hipervínculo or enlace; chose hipervínculo as the closest equivalent
# question holguinero: demonym of a place; rules cover place names and lowercase ethnonyms but not city demonyms, so drop is a judgment call.
# question holguinero: demonyms of places are not covered explicitly; decided drop as place-derived proper-ish adjective
# question iftar: could count as an established religious loan alongside Ramadán; I dropped it because it is not in the dictionary and appears mainly in news contexts.
# question ignifugar: split by form: ignifugo, ignifuga -> ignifugo
# question ignifugar: split by form: ignifugo, ignifuga, ignifugas -> ignífugo
# question jambalaya: dropped as an unestablished dish name; keep would be defensible if dish names count as loans
# question lacandón: also a place or region name, but the lowercase ethnonym is the main reading
# question lacandón: most forms are the place-linked "selva lacandona", so the ethnonym reading may be under half
# question laissez: merge target "laissez faire" assumed as multi-word unit
# question luciferino: split by form: luciferina, luciferinas -> luciferina
# question mayora: merged into mayoría based on the "mayora de" examples, though the feminine of mayor is the other possible reading
# question mayora: the examples show a cut-off "mayoría", so it is merged there rather than into mayor
# question memorabilia: mixed readings (Xenophon's title vs collectibles); kept as the collectibles loan
# question mucus: kept as an established medical Latinism; the usual Spanish equivalents are moco and mucosidad, so merge:mucosidad is possible if the coordinator disagrees
# question mucus: mucosidad or moco are both plausible targets; chose mucosidad as the register matching the health-text examples
# question muguet: Spanish medical texts use "muguet" for oral thrush, so a merge into "muguete" might be wanted; dropped as French
# question muguet: it is a French word, but it also occurs in Spanish medical text for oral thrush (RAE lists it); kept on that basis.
# question nimbar: split by form: nimbada, nimbado, nimbados -> nimbado
# question noticas: lemma is partly a typo and partly a section title; merged to noticia
# question omelet: not sure whether the list's standard spelling is omelette or the academy's omelé; chose omelette as the form people write
# question perfomance: target performance assumed to be on the list as a loan; if not, drop
# question performance: the merge target performance is not itself on the list as shown; confirm it exists as a lemma.
# question perseida: astronomical name, kept as a common noun for the meteor shower, but could be read as a proper-noun event
# question pingpong: RAE writes pimpón, but people write ping-pong; I merged into ping-pong following the list's usage rule.
# question pingpong: the academy spells it pimpón, but ping-pong is the common written form; merged to pimpón per the adapted-spelling rule
# question piroxicam: I wrote merge:piroxicam in error; it is a common generic drug so the decision should be keep.
# question pizcar: split by form: pizcas -> pizca
# question pizcar: split by form: pizcas, pizco -> pizca
# question plenum: the examples are HVAC/construction use, not the Spanish assembly sense; dropped as a technical loan
# question raki: could be kept as an established drink loan like other dish and drink words; dropped as too niche
# question respingar: split by form: respingo -> respingo
# question respingar: split by form: respingo, respingos -> respingo
# question roadtrip: "road trip" is a plausible established loan, but the merge target is a new two-word unit; drop if the coordinator thinks it is not established.
# question roadtrip: "road trip" is the usual spelling, but unsure it counts as an established loan
# question rodiano: Star Wars species name, so dropped; "rodiano" could also be read as a demonym of Rodas
# question salitral: place-name use also present (Salitral), but common word reading likely over a third
# question salmodiar: split by form: salmodia, salmodias -> salmodia
# question sectur: Mexican tourism ministry could count as a household-name national body (keep); I decided drop but the rules are unclear on ministry acronyms with this low profile.
# question sectur: Mexican tourism ministry is a national body; unclear if household name, decided drop
# question seleccio: could be a truncated selección, but the lowercase form is probably Catalan, so I dropped it.
# question sicotrópicas: merge target sicotrópico follows the variant spelling in the text; psicotrópico may be the preferred standard form
# question sinti: could be the Sinti people or a misspelling of "sentí"; examples missing, kept as the ethnonym
# question sinti: no examples; the lowercase forms may be the ethnonym or a stray "sentí" misspelling, so I kept it as an ethnonym
# question sobreexplotado: adjective-like participle; merged to the verb per the participle rule
# question solazar: split by form: solazo -> solazo
# question spammers: assumes spammer is a listed loan like spam; drop if it is not
# question spammers: merge target spammer assumed to exist as a listed loan
# question sudcoreano: both sudcoreano and surcoreano are in use; merged into the academy's surcoreano
# question sumergiéndote: sumergirse vs sumergir both plausible; chose pronominal since reflexive use here
# question telo: forms mix telos with telo/telas (Argentine slang telo for motel); merged to telos on the majority forms
# question tisbita: biblical gentilic (Elías tisbita) is not a place name, but it comes from a place and is only used in that fixed phrase; dropped
# question tranquillo: counted as a keep for the Spanish noun (coger el tranquillo); the other examples are the Italian/English-style adjective and may be a minority reading
# question trifecta: mixed examples (political and tech jargon); kept as an established loan, borderline
# question trifecta: the loan is used in some Latin American political and racing contexts, but the examples read as English; dropped
# question trídem: real Spanish trucking term, dropped as too specialist
# question whislist: merged to wishlist on the assumption that it is an established e-commerce loan; drop if it is not
# question agremiar: split by form: agremiados, agremiadas, agremiado -> agremiado (agremiado is used as a noun meaning union member; the lemma may hold two real words)
# question bloggera: please confirm that adapted feminine person nouns merge into their own feminine entry (bloguera), not the masculine (bloguero); only gentilics have a ruling.
# question ceto: no examples were sampled; if lowercase "ceto" is mostly the clipping in "dieta ceto" (keto), it would reach the one-third threshold and should be keep. Please pull a sample.
# question macero: please confirm the coordinator should split maceros/Macero -> macero, or let the noun's minor share follow macerar.
# question mucus: please rule on unadapted Latinisms with a Spanish equivalent (mucus vs moco/mucosidad): keep, or merge into the native word.
```
