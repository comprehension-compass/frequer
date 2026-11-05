# es review shard 17 (round 16): report

Branch `es-review-shard-17` from `ee1d9e0`; rules `review/rules/es-{flagged,unflagged}-final.md` (unchanged since
b65e7ed; same as full-es 34c1e92). Runtime, lemma wheel and corpus sample reused from the shard 9 work directory; the
setup script and `review/scripts/examples10.py` are unchanged. Every `review.py` call passed `--rules` and
`--decisions keep,drop,merge`.

## Counts

| step | lemmas | result |
|---|---:|---|
| flagged: examples | 362 | 289 with examples (**80 %, under the ~85 % bar**) |
| flagged: two reviewers | 362 | 358 agreed (drop 298, merge 39, keep 21), 4 disagreements; 1 accent-only merge |
| flagged: adjudication | 6 | 4 disagreements + 2 queries; 0 undecided |
| **flagged final** | **362** | **keep 24, drop 299, merge 39** (356 agreed, 6 adjudicated) |
| unflagged: screening | 400 | 2 batches, 0 failed; 268 suspects (209 by both screeners) |
| suspects: examples | 268 | 228 with examples (85 %) |
| suspects: two reviewers | 268 | 246 agreed (drop 106, merge 72, keep 68), 22 disagreements; 5 accent-only merges |
| suspects: adjudication | 27 | 22 disagreements + 5 queries; 0 undecided |
| **suspects final** | **268** | **keep 77, drop 122, merge 69** (241 agreed, 27 adjudicated) |

## Queries (the gate) and outcomes

I read every agreed merge and keep, every accent-only merge, and all agreed drops in both rounds.

Flagged:
- `véase` (agreed `merge:verse`): in *véase (también)* the se is impersonal se of ver. Adjudicated `merge:ver`.
- `uncitral` (agreed drop): a standing UN commission, and the second-set ruling keeps international bodies.
  Adjudicated `keep`.

Unflagged (agreed merges into a different word, or away from the written form):
- `estagnación` (`merge:estancamiento`): a translation target, not a spelling. Adjudicated `drop`.
- `protectivo` (`merge:protector`): a calque written consistently. Adjudicated `drop`.
- `sucrosa` (`merge:sacarosa`): an English calque. Adjudicated `drop`.
- `ecolocalización` (`merge:ecolocación`): standard and the only written form (78 of 78). Adjudicated `keep`.
- `moiré` (`merge:muaré`): the form people write (82 of 82). Adjudicated `keep`.

## Points for the coordinator

New classes of question raised by the adjudicator:
- `cattleya`: should an adapted organism name merge into its academy-adapted spelling (catleya) under the
  variant-spelling ruling, or stay as the dominant written form? (adjudicated keep as cattleya)
- `mesecvi`: does "regional and international bodies keep" cover treaty follow-up mechanisms and committees, or only
  standing organisations? (adjudicated drop)
- `putita`: regular diminutives filed as their own lemma: the same open question as shard 9's ruedecita. The
  reviewers also kept `sombrerito`, `bolsillito`, `botoncito` and `ojillo`; they follow that ruling.

Split requests (for the coordinator to write): `trajinero` (trajinera, trajineras, Trajineras, Trajinera ->
trajinera), `acamar` (acamados -> acamado; the lemma itself dropped as mostly the brand Acama), `importuno` (importuna
in verb readings -> importunar).

## What went wrong

- The flagged queue's example share is 80 %, below the ~85 % bar; carried on as the instructions say.
- Nothing else: no failed calls or batches in any step.

## Every `# question` line

### Flagged round (`s17-flagged/questions.txt`)

```
# question alcoyano: a gentilic of the place Alcoy, not an ethnonym; kept as a common adjective/noun, though it could be treated as place-derived.
# question archidemonio: real Spanish word, but the examples are all the Yu-Gi-Oh card name; dropped on the minority real reading, which I could not confirm from the samples
# question berlinetta: Italian loan used in car writing, about half lowercase; kept as established enough
# question berlinetta: a specialist car term and Italian loan; kept because over half of the occurrences are lowercase common nouns, but it may not be established enough in Spanish.
# question cattleya: orchid genus (also catleya in Spanish); treated as a raw taxon and dropped, but it could count as an adapted organism name
# question cattleya: orchid genus name is also a Latin taxon; kept as an adapted common name, but could be seen as a raw taxon
# question chequeado: mostly the Argentine fact-checking site (about 75% capitalised); the participle of chequear is under a third, so dropped
# question cross-docking: logistics loan with some establishment in Spanish business text; dropped as specialist
# question dios-con-nosotro: hyphenated title phrase for Emmanuel; dropped as a hyphenated compound, but could be a merge target of "Dios con nosotros" if the developer wants it.
# question grácia: a few occurrences are misspelt gracias (grácias), but the place name Grácia dominates
# question kayapó: capitalised as a people's name; the lowercase-ethnonym rule could argue for keep
# question kayapó: capitalised in 72% of the text; kept as an ethnonym, but a drop is defensible if it counts as a proper noun
# question kogi: could be the Colombian people (Spanish "kogui") or a Nigerian state; no examples were available to decide
# question lebaniego: gentilic of a place (Liébana), mostly capitalised; kept as a real Spanish adjective, but it could instead count as a place-derived proper name
# question lebaniego: gentilic of a place (Liébana); kept as a real common gentilic although capitalised 62%, confirm.
# question malambo: capitalised 80% and several examples are the Colombian municipality; kept for the dance reading, which may be near the one-third threshold
# question malambo: dance and a Colombian municipality are mixed in the examples; kept because the dance reading looks like at least a third
# question meibomio: eponym anatomical term (glándulas de meibomio), niche; kept as real common-noun use
# question mesecvi: the OAS keeps as a regional body, but it is a specialist mechanism; kept under the regional-bodies ruling
# question morabito: lowercase share is only about 42%, with the remainder partly a surname; kept as above the one-third threshold.
# question morabito: surname Morabito is the majority of examples; kept because lowercase morabito(s) is about a third or more
# question nethineo: biblical term (Spanish netineo); dropped as specialist, but could be a merge to netineo if the developer wants biblical vocabulary
# question okara: the real word okara (soy pulp) is about 29% of the occurrences, just under a third; dropped
# question ombúes: plural of ombú (a real word) but mostly the town name; the lowercase share is about 19%, so dropped
# question paladino: lowercase paladino/paladina forms are only about a fifth of the occurrences, so the word was dropped as mostly a surname
# question pinole: the common-word reading (maize flour) is about a third of the examples, and the rest are the place name Pinole.
# question previews: English plural of "preview"; dropped because the loan is not clearly established, but a merge to preview is possible if the developer counts it as one
# question relaja: capitalised 74% with no examples, so it may be a brand name (then drop); merged as an imperative of relajar
# question relaja: no examples were found; merged to relajar on the assumption it is a heading form of the verb
# question roleplay: it is an established gaming loan, but many examples are forum or server names, so the keep is borderline
# question roleplay: the loan is established in gaming circles but not in general Spanish; kept as borderline
# question sistina: "Capilla Sistina" is a real adjective use, but most examples are venue or place names; dropped
# question sorrentina: possible feminine gentilic of sorrentino, but mostly names/brands; dropped
# question subliminales: all capitalised, possibly a title or band name; merged on the plural-of-adjective reading
# question uncitral: international body, but a specialist one; dropped as not famous enough to count as a household name
# question vietcong: an organisation name, but used in Spanish as an ordinary noun; kept as established
# question viognier: grape names are neither place nor taxon in the rules; kept as an adapted wine term
# question viognier: grape varieties are not covered by the rules; kept because it is written as a lowercase common noun like garnacha.
# question véase: it is a fixed cross-reference expression ("see also"); merged into verse, but the developer may prefer keeping it as an expression
# question cattleya: Spanish also writes it adapted as "catleya". Should the entry merge:catleya under the variant-spelling ruling, or stay as cattleya, the dominant written form?
# question mesecvi: does the "regional and international bodies keep" ruling also cover treaty follow-up mechanisms and committees (MESECVI, and similar bodies tied to a convention), or only standing organisations?
```

### Unflagged round (`s17-unflagged/questions.txt`)

```
# question acamar: lemma holds the brand "acama" (46) and the real verb/adjective acamar/acamado; split by form: acamados -> acamado
# question acamar: split by form: acamados -> acamado
# question aféitate: afeitarse chosen as the common pronominal verb; imperative with -te
# question atletica: the example is a Portuguese club name (Associacao Atletica), so real reading may be a minority; merged to atlética per the missing-accent rule
# question barreta: real Spanish word (crowbar, small bar) but the examples look like mistranslations or foreign text; dropped because the real reading is under a third
# question barreta: real Spanish word (small bar/crowbar) but the examples mostly show other uses; dropped as the real reading looks under a third
# question benefi: fragment could be beneficio or beneficiar; no obvious target, so dropped
# question bisabolol: cosmetic ingredient, not clearly generic or specialist; dropped
# question bolsillito: same diminutive issue; kept
# question calderín: unclear what share of the examples is the surname Calderín versus the common noun
# question cilostazol: borderline between common generic drug and specialist drug; treated as specialist
# question coloproctología: specialist medical term and mostly appears in society names, but it is a real Spanish word, so kept.
# question currys: Currys is also a UK retailer brand (about a third of the examples), but the plural of curry is the majority reading, so I merged it.
# question dejano: forms are mostly "dejanos" (déjanos), a clitic of -nos; dejar is chosen as plain verb since dejarse is less central
# question desmopressin: merged on the spelling rule; desmopresina may itself be a specialist drug and drop at review
# question despojador: real but rare, and the examples are missing so the product sense can't be checked, so kept.
# question estagnación: could be a rare real variant; merged to estancamiento
# question estagnación: could be a real but rare variant (Portuguese/Catalan-influenced); merged into estancamiento as the obvious Spanish lemma.
# question exprimera: ex- glued to primera (exprimera dama, exprimera bailarina); merged to primero, but drop is also defensible
# question fíat: Latin/economic term versus the brand Fiat; kept with the accented spelling as written, though the standard spelling is "fiat"
# question fíat: merged to fiat (the dictionary spelling); fiat money use is also covered by this entry
# question importuno: lemma holds adjective importuno/a and verb importunar (importuna as 3sg); split by form: importuna (verb readings) -> importunar
# question importuno: the lemma holds importunar (verb form "importuna") and the adjective importuno; decided for the adjective, split by form: importuna (verb reading) -> importunar
# question kickoff: some examples are the site name Kickoff and NFL commentary; kept as an established loan, but the real-word share is unclear
# question logins: assumed login is already a listed loan; if it is not, drop instead
# question logins: unsure whether "login" is established enough in Spanish to be a target; merged on the assumption it is
# question moxifloxacin: dropped as a specialist drug; if moxifloxacino counts as a common generic antibiotic, it should merge there instead
# question obcecar: split by form: n/a, single verb; forms mostly participles/adjective obcecado, kept as the verb lemma
# question quimioembolización: real but specialist medical term; dropped as too specialist
# question remasterizadas: unclear whether the target should be remasterizado or remasterizar; chose the adjective because of the tag
# question sombrerito: diminutives are not covered by the rules; kept as a regular diminutive, though "El Sombrerito" is also a place name
# question telemercader: dropped as unattested in dictionaries; it could instead be treated as a real compound for telemarketer
# question telemercader: it may belong under telemercadeo or telemarketing; I kept it because the word is attested in its own right
# question torón: kept as a technical term for cable strands; the entries seen are all engineering uses, and the dictionary status of "torón" is uncertain
# question torón: real word for a cable strand, but the evidence is thin (one example) and the word is specialist
# question trajinero: trajinero (carrier) and trajinera (Xochimilco boat) are separate words; nearly all forms here are the boat, so I merged into trajinera.
# question virginiano: the gentilic reading may be a third or more of the examples; the taxon reading looks larger, so I dropped it
# question putita: no ruling yet on regular diminutives filed as their own lemma (keep as here, or merge into the base like regular -ísimo superlatives?)
# question trajinero: split by form: trajinera, trajineras, Trajineras, Trajinera -> trajinera
```
