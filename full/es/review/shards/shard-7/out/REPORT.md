# es review shard 7: report (round 14, cascade)

Branch `es-review-shard-7`, created from `origin/full-es` at `04d1ada`. Before any review stage ran, I applied the
developer's second rulings set to `review/rules/` from full-es `0095cdd`, as the coordinator asked. All
`review.py` lines passed `--rules` and `--decisions keep,drop,merge`. The screener and reviewer calls had no
failures, so no stage was rerun.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 878 |
| flagged with an example | 737 (83.9%: **under the ~85% mark**) |
| flagged reviewers agreed | 851 (drop 751, merge 63, keep 37); 27 sent to the adjudicator |
| flagged queried at the gate | 7 |
| flagged adjudicated (27 disagreements + 7 queries) | 34 (keep 5, drop 18, merge 11) |
| **flagged final** | **keep 37, drop 768, merge 73** (844 agreed + 34 adjudicated) |
| unflagged screened | 978 (4 batches, 0 failed) |
| suspects (either screener) | 444 (364 marked by both) |
| suspects with an example | 393 (88.5%) |
| unflagged reviewers agreed | 419 (keep 95, merge 136, drop 188); 25 sent to the adjudicator; 12 accent-only merges |
| unflagged queried at the gate | 5 |
| unflagged adjudicated (25 disagreements + 5 queries) | 30 (keep 7, drop 15, merge 8) |
| **unflagged final** (suspects only; the 534 non-suspects stay keep) | **keep 101, drop 202, merge 141** |

## Gate

I read every agreed merge and keep in both rounds, all 751 + 188 agreed drops (lemma and reason, plus forms
where a drop might hide a real word), and both accent-merges files. The 12 accent-only merges (hidraúlico,
farmaceútico, líbido, dósis, senorita, ...) are all plain misspellings and I left them alone. Most drops of
possible real words were already well reasoned under the one-third ruling (ruca, lobito, gallero, palomero,
piolín, diabla, chichi), or the word was an event or company name (transfiere, totalisimo, gelida).

Flagged queries → adjudicator:
- varano (agreed keep; lowercase 29%, place Varano Borghi) → **keep** (about a third).
- energéctica (agreed merge:energético; all 122 uses capitalised) → **drop** (company or title name).
- recluta (agreed keep; 2 of 96 lowercase, no examples) → **drop**.
- uneac (agreed keep; Cuban writers' and artists' union) → **keep** (household-name national body, like ETECSA).
- rhc (agreed keep; Radio Habana Cuba) → **drop** (minor broadcaster).
- mise (agreed drop; 57 of 121 lowercase, possibly half of mise en place / mise en scène) → **drop** (no clean split target).
- clac (agreed keep; onomatopoeia 32% vs the CLAC acronym) → **keep**.

Unflagged queries → adjudicator:
- cuado (agreed merge:cuñado, no examples) → **drop** (cuando, cuñado or a name are all plausible).
- harmónica (agreed merge:armónico; might be the instrument armónica) → **merge:armónico** (examples are the adjective).
- yorkie (agreed drop; 40% lowercase breed noun) → **keep**.
- sultano (agreed keep; forms are sultana/sultanas) → **merge:sultana**.
- indiv (agreed merge:individual, no examples) → **drop** (individual or individuo).

## Things for the coordinator

- Flagged example coverage is 83.9%, just under the ~85% mark. Per the instructions I noted it and carried on.
- Several `# question` lines ask the coordinator to confirm a merge target exists: antiinmigración, antivaho,
  antivibración, semiesencial, grecocatólico, art déco, todo incluido, minipímer, pin-up, striptease/estriptis,
  nailon/nylon, gecko/geco.
- Lemma-split questions (developer ruling 2), which the coordinator writes: afijar → afijo, desparejar → desparejo,
  ufanar → ufano, empachar → empacho (unflagged), plus the chaga/chagas and geyser (water heater) lines in flagged.
  **entronar** asks for a *typo* split (entrono → entorno, about 70 of 121), which may be a new class of question.
- estós: unclear whether the target is merge:estos (own lemma, like los) or merge:este.
- -os clitic (ofreceros): the -nos/-te ruling doesn't name -os. The reviewers merged it into the plain verb
  ofrecer. This may be a new class of question.

## Every `# question` line

The question lines are in `s7-flagged/questions.txt` (100 lines) and `s7-unflagged/questions.txt` (69 lines),
reproduced below.

### s7-flagged
```
# question akelarre: a real Spanish word, but the lowercase share is only about 11%, so the rule drops it; the capitalised forms may be sentence-initial
# question anti-inmigración: Target spelling antiinmigración assumed (prefix anti- written solid); the lemma may not exist yet.
# question anti-inmigración: unclear whether antiinmigración is a listed lemma; if not, drop as a hyphenated prefix compound
# question anti-phishing: could be merged into "antiphishing" instead; dropped as a hyphenated compound with a foreign word.
# question anti-phishing: hyphenated anti- + loan; dropped as English technical term, but could merge into "antiphishing" if that is listed
# question anti-vaho: merge target antivaho assumed to be the standard spelling; confirm it is listed
# question anti-vibración: hyphenated "anti" + noun; merged to the closed spelling antivibración on the assumption that is the standard form.
# question art-deco: target art déco assumed as the multi-word standard spelling
# question assoc: no examples in the sample; may be an abbreviation of asociación (merge:asociación), but capitalised use looks English, so dropped
# question babia: "estar en Babia" is a common idiom, but every example here is the place or a name, so I dropped it as a place name.
# question babia: place name that is also the idiom "estar en Babia"; kept for the idiom, though most examples are the place
# question balla: could be a stray verb form (Catalan "balla") or a surname; no examples available, dropped.
# question bifida: merge target "espina bífida" is a multi-word unit; "bífida" alone would be a bare adjective.
# question biol: no examples; could abbreviate biología or biólogo, so no obvious merge target, dropped
# question bothan: fictional ethnonym in lowercase use; unclear whether the lowercase-ethnonym rule covers fiction
# question braco: capitalised uses are mostly hotel and surname, but the two examples of the dog breed suggest the real reading is near a third
# question bungy: Unsure whether bungee is already on the list; if not, drop would also fit.
# question campsa: historic state oil monopoly, now defunct and seen mainly in a restaurant guide; treated as a company name and dropped
# question cantv: a company rather than a public body; kept as a household-name national entity by analogy with ETECSA
# question caprese: its dish reading (about 40%) is borderline as an established loan
# question caprese: place-name reading (Caprese Michelangelo) versus food adjective; kept because lowercase is about 40%
# question carabinieri: foreign institution, not of a Spanish-speaking country; kept because Spanish uses it as a common lowercase noun (39 of 94 occurrences)
# question carabinieri: foreign national police body, not of the Spanish-speaking world; kept as an established loan used lowercase in Spanish text
# question catarinense: Spanish gentilic of Santa Catarina but examples are mostly a football league name; dropped
# question chaga: Chagas is the disease name but the lemma is mixed with chaga (mushroom); dropped, a merge to chagas may be wanted
# question chaga: written forms mix chaga/chagas (disease name); merge target chagas assumed as the standard lemma
# question churn: telecom/marketing jargon in Spanish; dropped because specialist and mixed with an unrelated machine name, but could be kept as a loan.
# question clac: onomatopoeia reading is about 32% (lowercase 30 of 95), borderline on the one-third threshold; kept, but could be dropped if lowercase uses are actually the CLAC acronym.
# question clac: the capitalised acronym (Fair Trade body) dominates the examples; the real onomatopoeia may be under a third, so drop is possible if the lowercase uses are also the acronym.
# question co-directora: the hyphenated feminine form has no masculine counterpart in the examples, so I merged it to the feminine codirectora; the coordinator may prefer codirector.
# question diabla: real feminine of diablo appears in only about a fifth of the examples (diabla, diablas, diablita); dropped under the one-third rule, but a coordinator may want to check whether diablo covers it
# question diabla: the feminine of diablo would keep, but all shown examples are names or brands, so I dropped it; a split may be needed if the real word is a third or more of the examples
# question energéctica: 122 occurrences all capitalised, possibly a company name rather than a misspelling of energética; merged on the misspelling reading
# question etcs: mixes the rail control system with a misspelling of ECTS, which is not itself listed; dropped
# question exopolítica: coined pseudo-scientific term, kept as a regular noun
# question fise: Peruvian energy-inclusion fund acronym; treated as a minor body rather than a household-name institution
# question gay-friendly: hyphenated loan kept as established; check against the hyphenated-compound rule
# question geckos: DLE lists geco, but the list uses the form people write, so I chose gecko
# question geyser: some examples are the Latin American water heater, which may deserve its own entry apart from géiser
# question greco-católica: the target grecocatólico is assumed as the standard spelling; the rules might instead drop it as a hyphenated compound.
# question guppy: about half the examples are brand or place names (Guppy baby carriers, Guppy Gulch Quarry), but the fish reading is likely over a third. Kept.
# question guppy: examples are mostly brand names and English plural guppies; kept as an established fish name, but may be below a third of real usage
# question hallelujah: the examples are mostly titles and names, but I merged it because aleluya is the adapted word
# question hi-hat: hyphenated loan; kept as an established drum-kit term, but the rules do not clearly cover hyphenated loans
# question hi-hat: specialist drum term, kept as an established loan; drop if the team thinks only drummers use it
# question horrocruxes: fictional-world term; merged to the singular rather than dropped as a title
# question hotspots: not sure hotspot is established enough to be a learner loan; I merged it as a WiFi term like web and chat
# question injector: examples look like English/IT usage, so drop is also defensible if the Spanish "inyector" reading is a minority
# question kaftan: many examples are names (a yacht, a character), but about 32% are the common noun, so merged
# question kannada: kept as language name; lowercase ethnonym/language reading is 40% of examples
# question kannada: most examples are foreign titles, but the lowercase language use is real; kept
# question karate-do: kept as a hyphenated loan; could alternatively merge into karate
# question kyat: a foreign currency name with no rule of its own; I treated it like forint and kept it.
# question laguito: real diminutive is about 25% of examples (lowercase), below a third, so dropped
# question laguito: real diminutive of lago is about a quarter of the examples, below a third, so dropped
# question lassi: the lowercase drink reading is about a third of examples, so it is borderline.
# question lipgloss: established enough in Spanish beauty vocabulary? kept; Spanish may also write "gloss"
# question lipgloss: it may be an established makeup loan, but the English spelling and the brand-like use led me to drop it.
# question maglev: mixed name (Shanghai Maglev) and generic term; kept as the generic loan.
# question marquise: the diamond-cut reading is about 28% of examples, under the one-third threshold, so I dropped it, but marquesa-style common use is possible
# question minipimer: the Spanish spelling with an accent (minipímer) is assumed to be the standard form
# question niceno: gentilic-type adjective derived from the place Nicea; kept as a real adjective in credo niceno
# question nylón: academy form is nailon; merged there, but "nylon" is the commoner written form, so the coordinator may prefer to keep it.
# question ofrecero: ofreceros is ofrecer + -os (not -nos/-te); merged into plain verb ofrecer, though ofrecerse is also a common verb
# question ofrecero: the form written is ofreceros (ofrecer + os); the rule on -nos/-te clitics does not name -os, merged into plain verb ofrecer since ofrecerse is less central here.
# question pinup: pin-up is an established loan in Spanish, but examples are mostly English-context uses; merged into pin-up
# question pinup: unsure whether the list spells the loan "pin-up" or "pinup"; merged into the academy spelling.
# question post-punk: hyphenated genre loan; could instead be written "postpunk", so the coordinator should check which spelling people use.
# question pre-pedido: no obvious Spanish target; merged to preventa as approximate, drop could also fit
# question publ: could be an abbreviation of "publicado", but the evidence is too thin for an obvious merge; dropped.
# question publ: probably an abbreviation of "publicado" or "publicación", but it is not obvious which, so I dropped it rather than merging
# question recluta: capitalised 88% and no examples were shown, so it may mostly be a name or heading. I kept it as the real word on the assumption that job-ad and military uses are at least a third of the occurrences.
# question recluta: capitalised in 88% of examples and none were shown, so it may be mostly a title or name; kept as a real common word on the assumption that about a third of uses are the noun.
# question rhc: Radio Habana Cuba is a state international broadcaster; unclear whether it counts as a household-name national body. Kept as a broadcaster.
# question rhc: kept as Radio Habana Cuba, but it appears as a news-agency tag and may be too specialised
# question sate: a minority of examples may be a real word (sate, from saciar), but the sample shows only the SATE acronym, so I dropped it
# question sate: the SATE reading (thermal insulation system) is the majority of examples; the common-word reading seems minor, so dropped.
# question scart: SCART is a technical connector acronym but widely written in Spanish TV text; dropped as technical, so keep if the developer wants it as a household term.
# question semi-esencial: could instead merge to "semiesencial" if the developer accepts that closed spelling, but it is not an established form
# question semi-esencial: merged to semiesencial on the assumption that the prefix spelling is standard; drop if the coordinator prefers the hyphenated-compound rule
# question shcp: a national ministry acronym that is less well known than Hacienda itself; I kept it as a household name in Mexico.
# question shh: mixed with the Sonic hedgehog gene abbreviation (SHH); kept for the interjection reading, which may be only about half of the uses
# question socio-laboral: merged to the academy spelling sociolaboral; confirm the target form if the list prefers the hyphenated spelling.
# question strip-tease: target estriptis is the academy form, but the list may prefer the spelling people write (striptease)
# question todo-incluido: the rule on hyphenated compounds of listed words says drop, but the variant-spelling ruling says merge; merged into "todo incluido" as a common unit.
# question torr: the pressure unit is real but the examples are missing and capitalisation suggests names; dropped as specialist
# question tuto: clipping of tutorial is colloquial, and some uses may be a nickname; kept because lowercase forms are about half the examples
# question tuto: lowercase "tuto"/"tutos" is only about 47% of the examples and no examples were available, so the real-word reading is unconfirmed
# question umu: a single regional university rather than a nationally famous one, kept under the university rule
# question usmp: Peruvian private university; unclear whether it counts as a nationally famous university, dropped
# question usmp: private university in Lima; unclear whether it counts as nationally famous, kept as a major Peruvian university
# question varano: lowercase reading is about 29%, slightly under a third, kept because the capitalised uses are mostly a place name
# question varano: real reading is about 29% of examples, just under a third, and the place name Varano Borghi is also present; kept as a borderline case
# question wiccan: examples are largely English or titles; merged to wiccano as an English spelling of the adapted word, but drop is arguable if the real reading is under a third.
# question wikiproyecto: could count as an established web term like wiki; dropped as mostly names of specific projects.
# question babia: idioms built on a capitalised place name ("estar en Babia") drop under the place rule; should the idiom be kept as a multi-word unit instead?
# question injector: if lowercase "injector" in Spanish text is just a misspelling of inyector, should those occurrences be split by form to inyector rather than dropped with the English names?
# question mise: lowercase uses are likely "mise en place" (cooking) or "mise en scène"; should either become a unit entry, and how should a first half shared by two compounds be handled?
# question recluta: is the common noun and verb reading counted under a separate NOUN or VERB entry? If not, dropping this PROPN-tagged bucket loses a learner word.
# question varano: does "about a third" in the one-third ruling cover shares near 29%, or is 33% a hard cutoff?
```

### s7-unflagged
```
# question abbá: biblical Aramaic term used in Spanish religious texts; dropped because of the Abbás/ABBA name mix.
# question afijar: split by form: afijar, afijaremos, afijará, afijen -> afijar (verb, a minority of the examples); I merged the lemma into afijo for its majority reading.
# question afijar: split by form: afijo -> afijo
# question alcántara: Alcantara is a brand-origin upholstery material used as a common noun, and the lemma is the fragment alcántar; dropped, but it may deserve a kept entry alcántara
# question alcántara: the word is partly a brand (Alcantara) used as a material name; merged as the common material.
# question amantadina: specialist antiviral/Parkinson's drug; dropped as not a common generic, but borderline.
# question anonimizador: rare but regular derived noun; kept
# question antialiasing: could count as an established tech loan; dropped as specialist
# question apartements: could also be treated as a foreign-language junk token and dropped; merged because it sits in lists beside apartamentos
# question atractividad: rare, and no merge target is clearly right (atractivo or atractivo's synonyms); dropped as a calque.
# question bacón: the academy prefers beicon, but the list uses the form people write, so I kept it; merge to beicon if you prefer the academy form.
# question budesonide: could merge:budesonida if the coordinator treats it as a common drug; I judged it specialist.
# question calicó: I kept it as an adapted loan found in Spanish text; the screener suspected Catalan, so please confirm it is established in Spanish.
# question campanita: no examples given, so the share of uses as the name (Tinker Bell) is unclear; kept because most occurrences are lowercase
# question capilariza: capilarizar is not clearly established in dictionaries; it appears only in sportswear marketing copy, so drop is also defensible.
# question clickeando: merged into clickear as the form people write; the academy's clicar (or clic per the spelling rule) could be the target instead
# question clickeando: merged to clicar following the click → clic convention; the coordinator may prefer clickear if the list keeps that verb form
# question cocotte: French cookware word, borderline between established loan and foreign word; kept
# question cocotte: no clear academy entry; kept for its cookware use in Spanish texts.
# question comeback: borderline loan; about a third of the examples are a phone model name
# question comeback: mixed product-name and fashion/K-pop uses; kept as an established loan, borderline
# question condoler: forms are mostly condolerse; kept as the pronominal verb, no merge target needed
# question cuado: cuñado is the likeliest reading, but no examples were shown; cuadro or a cut-off fragment is possible
# question cyclosporine: ciclosporina is an obvious Spanish form, but I judged it a specialist drug and dropped it rather than merging; a ruling on whether it counts as a common generic would settle it.
# question desparejar: forms are mostly the adjective desparejo/desparejado, so a lemma desparejo could fit better; kept since desparejar is a real verb.
# question diptera: dípteros is a Spanish word, but these forms are almost all the taxon label; dropped, and a lemma dípteros might need a separate entry.
# question empachar: split by form: empacho -> empacho
# question entronar: most examples are the typo "entrono" (entorno); dropped as the entronar reading is under a third
# question entronar: split by form: entrono -> entorno (misspelling, about 70 of 121 occurrences; the remainder is real entronar)
# question excluídos: merged into the verb excluir; the rules don't say whether a participle used as an adjective should go to excluido instead
# question extrudado: merge target extrudir is uncertain; the examples read mostly as a noun or adjective ("el extrudado"), so keep may fit better.
# question extrudado: no clear Spanish lemma (extrudar or extrusionar); dropped as an industrial technical term
# question glycol: could merge into glicol, but dropped because every example is an English chemical name
# question guatear: lemma may be better as the adjective guateado; kept because the verb guatear is plausible but its dictionary status is unclear
# question halloumi: cheese name that appears on Spanish menus, but the examples are from English contexts; dropped as not yet established
# question indiv: no examples; "individual" is a guess from the abbreviation
# question indiv: no examples; assumed to abbreviate individual
# question legenda: unclear whether the lowercase legenda/legendas forms are Spanish; about half are lowercase and the examples show only the name Lucilla Legenda, so I dropped it as foreign or a name
# question multieje: borderline specialist term; kept as an ordinary prefixed compound
# question multipack: it occurs mostly in commercial copy; keep assumes it counts as an established loan.
# question netofatita: gentilic of the biblical town Netofa; the rules cover ethnonyms but not biblical place-gentilics, so dropped.
# question netofatita: lowercase gentilic rule would suggest keep, but it is a biblical place-derived gentilic with no learner value; dropped
# question notica: some examples are typos of "noticias"; I kept it on the strength of the real diminutive reading.
# question notica: some occurrences may be typos of "noticias"; kept as a real colloquial diminutive.
# question pieta: the Italian art-work sense (Pietà) is not in the examples, so I dropped it
# question purito: puritos (small cigars) plus Purito as a nickname/name; the real-word reading is about a third (37 of 109), so I kept it.
# question purito: the real-word reading (puritos, small cigars) is about 33% of occurrences, right at the "about a third" line; the lemmatiser may also want it merged into puro as a diminutive.
# question rooting: Android jargon seen in Spanish tech text; I judged it not yet established enough to keep.
# question rooting: the English term is common in Android contexts, but Spanish usually says "rootear" or "root", so it is borderline as an established loan.
# question seah: biblical unit of measure that appears in Spanish Bible texts; dropped as not established for a learner's list
# question selegiline: could merge into the adapted spelling selegilina, but dropped because all examples are English drug lists and the drug is specialist
# question somatropina: generic drug but specialist hormone; dropped as specialist
# question sultano: most forms are sultana, which could be its own feminine entry; kept the lemma as a real word.
# question sultano: most occurrences are "La Sultana" as a place epithet or title, but sultano/sultana is a real word, so I kept it.
# question terroirs: terroir may not itself be on the list; merged target assumed to be the standard singular loan form
# question terroirs: the target lemma terroir is assumed to be on the list or to be kept as an established loan; if terroir is not itself kept, this should be drop.
# question teseracto: the lowercase real-word reading (the geometric tesseract) is about 13% of the examples, so I dropped it, but it may deserve a keep if the Marvel use is judged a common noun.
# question totoaba: a well-known animal in Mexico (the fish is regularly in news about the vaquita), so keep could be defended; I dropped it as a specialist organism name with no example sentences to check.
# question totoaba: tagged VERB is a tagger error (noun); no examples were available to confirm usage
# question trabe: real Spanish word (beam, trabe) exists, but the sample is dominated by the "a trabes de" misspelling and a brand; dropped, since the real reading is probably under a third
# question trabe: trabe is also a real but rare word (viga), and the examples are one brand name and two "a trabes" misspellings; merged to través as the majority reading.
# question transmitencia: the standard word is transmitancia; confirm this is a variant spelling rather than a separate word.
# question truquito: diminutives are not covered by the rules; kept with cortita for consistency
# question ufanar: split by form: ufano -> ufano
# question afijar: split by form: afijo, afijos -> afijo
# question desparejar: split by form: desparejo, despareja, desparejos, desparejas -> desparejo
# question entronar: split by form: entrono, entronos -> entorno (typo, not a real word; confirm a typo split is wanted)
# question estós: is the plural demonstrative "estos" its own lemma under the lemmatiser (like los), making the target merge:estos rather than merge:este?
# question ufanar: split by form: ufano, ufana, ufanos, ufanas -> ufano
```
