# es review shard 13 (round 15): report

Branch `es-review-shard-13` from `b65e7ed`; rules `review/rules/es-{flagged,unflagged}-final.md` as on full-es 75c5ee4
(second-set developer rulings included; identical at b65e7ed). Runtime, lemma wheel (sha256 checked) and corpus sample
reused from shard 9's work directory; the setup script and `review/scripts/examples10.py` are unchanged since then.
Every `review.py` call passed `--rules` and `--decisions keep,drop,merge`.

## Counts

| step | lemmas | result |
|---|---:|---|
| flagged: examples | 553 | 455 with examples (**82 %, under the ~85 % bar**) |
| flagged: two reviewers | 553 | 536 agreed (drop 464, merge 53, keep 19), 17 disagreements |
| flagged: adjudication | 18 | 17 disagreements + 1 query; 0 undecided |
| **flagged final** | **553** | **keep 19, drop 474, merge 60** (535 agreed, 18 adjudicated) |
| unflagged: screening | 615 | 3 batches, 0 failed; 323 suspects (272 by both screeners) |
| suspects: examples | 323 | 277 with examples (86 %) |
| suspects: two reviewers | 323 | 308 agreed (drop 152, merge 109, keep 47), 15 disagreements; 8 accent-only merges |
| suspects: adjudication | 17 | 15 disagreements + 2 queries; 0 undecided |
| **suspects final** | **323** | **keep 55, drop 155, merge 113** (306 agreed, 17 adjudicated) |

## Queries (the gate) and outcomes

I read every agreed merge and keep, every accent-only merge, and all agreed drops in both rounds.

Flagged:
- `racquetball` (agreed keep): English spelling; Spanish writes raquetbol (spelling ruling, click → clic). Adjudicated
  `merge:raquetbol`.
- Checked and not queried: `listán` (drop; 72 of 87 capitalised, under a third lowercase, so consistent with the
  one-third ruling despite shard 9's sangiovese keep).

Unflagged:
- `cubicar` (agreed `merge:cúbico`): about 15 of 97 occurrences are the real verb cubicar. Adjudicated `keep`, with
  a split question (cubico, cubicas -> cúbico).
- `kasba` (agreed `merge:casba`): the list uses the form people write. Adjudicated `keep` (all forms are kasba).
- Checked and not queried: `gorditas` (examples are all the adjective, not the dish).

## Points for the coordinator

New classes of question raised by the adjudicator:
- `censurado`: participles used only adjectivally or as a fixed marker ([CENSURADO]): merge into the verb or keep?
  (adjudicated `merge:censurar`)
- `racquetball`: confirm raquetbol is "the form people write" when the English spelling is frequent on the web.
- `customizable`: adjectives formed from a discouraged but established anglicism verb (customizar): keep, or drop in
  favour of personalizable? (adjudicated keep)

Split requests (for the coordinator to write): `cubicar` (cubico, cubicas -> cúbico), `mariscar` (mariscada,
mariscadas, Mariscadas -> mariscada), `amurar` (amura, amuradas -> amura; the lemma itself dropped),
`hoster` (hostería -> hostería; the lemma itself dropped).

Consistency with shard 9's open question on diminutives (ruedecita): the reviewers kept `sorbito`, `trabajito`,
`semillita` and `viajecito` as their own entries; they follow whatever the ruling on regular diminutives turns out to be.

## What went wrong

- The flagged queue's example share is 82 %, below the ~85 % bar; carried on as the instructions say.
- Nothing else: no failed calls or batches in any step.

## Every `# question` line

### Flagged round (`s13-flagged/questions.txt`)

```
# question adaptor: only 4 of 86 plural/Spanish forms and examples are English product names; merged to adaptador on spelling rule, though the examples show "Power Adaptor" as English.
# question agnus: assumed that "dei" is filed as a separate lemma and merges into the same phrase.
# question agnus: the half-merge assumes "dei" is also in the batch, and "agnus dei" is liturgical Latin that may be better dropped
# question animao: -os imperative clitic isn't covered by the -nos/-te ruling; treated the same way, merged into animarse.
# question animao: animaos is the imperative with -os, which the clitic rulings (-nos/-te) do not cover; merged into animarse.
# question aquilino: examples show given-name use, adjective reading may be under a third
# question asoc: possibly an abbreviation of asociación (merge:asociación), but no examples were available and ASOC is also an organisation acronym
# question awá: capitalised in 64% of running text, so the ethnonym reading is mixed; kept as an ethnonym.
# question burguer: brand use (Burger King) is about two of three examples; merged to hamburguesa since the real reading is near a third.
# question bussines: mostly company or event names ("Bussines TICC") and junk, so I dropped it rather than merging it into business.
# question cefixime: it is unclear whether cefixima is a common enough generic drug to keep; merged into it on the spelling rule.
# question cenidh: Nicaraguan human rights centre is a national body but perhaps not a household name like ETECSA; kept as a national public-interest body.
# question censurado: all examples are the "[CENSURADO]" redaction marker; kept as a real adjective, but could be merge:censurar
# question dedicarl: lemma is cut-off from dedicarles; merged to dedicar as the clitic form is a plain verb
# question eco-eficiencia: merge target ecoeficiencia assumed to be the standard unhyphenated spelling
# question eco-eficiente: ecoeficiente may not be on the list as an entry; the alternative is drop as a hyphenated compound
# question enusa: state-owned nuclear fuel company; treated as a minor company rather than a household-name national body
# question enusa: state-owned uranium company; might count as a national body, but treated as an ordinary company
# question euro-mediterránea: merged to euromediterráneo as the obvious unhyphenated Spanish form; drop if that form is not wanted.
# question euro-mediterránea: the rules don't say whether the euro- prefix is written joined; euromediterráneo is assumed.
# question goyim: Hebrew/Yiddish plural of goy, used in Spanish quotations and also as a biblical place name; dropped as not established, but could merge to goy if the developer wants it
# question goyim: mixed capitalisation (47%) and mostly Biblical/discourse use; kept as a loanword-like ethnonym, could be dropped as foreign
# question hcch: international body (Hague Conference on Private International Law) but not a household name; dropped as specialist
# question hcch: international body but obscure to learners; dropped
# question impro: could be a clipping of improvisación, but most occurrences are names/brands, so dropped
# question impro: lowercase impro may abbreviate improvisación, but most occurrences are IMPRO as a name, and no examples were available to check.
# question inem: also used for a Colombian school (INEM), but the Spanish employment institute is the main reading
# question inem: examples include a school name (INEM Medellín) and "curso INEM"; kept as the Spanish employment institute, the main reading
# question jarretera: the Order of the Garter reading is a proper-noun use; kept because the common word (garter, garter shark) is real.
# question jute: some examples are a place or business name (Teatro Jute), but the material reading looks like a third or more, so merged into yute
# question jute: yute is the Spanish word but the examples mix the material with a theatre name; merged on the material reading
# question krona: some occurrences are a DC character, but the currency reading looks like at least a third, so I kept it
# question laminada: could instead be seen as a participle form of laminar; merged into laminado as the adjective
# question minae: Costa Rica's environment ministry is a national body, but it is unclear whether it counts as a household name; kept as a ministry.
# question minae: national ministry of Costa Rica; kept as household name there, but a borderline case.
# question mini-álbum: assumed the target is the closed spelling miniálbum; drop instead if that is not listed
# question mini-álbum: merging assumes miniálbum is the standard one-word spelling; if it is not on the list, drop instead
# question multi-efecto: merged into multiefecto on the assumption it is the standard spelling; the target lemma may not exist on the list
# question multi-efecto: no clear standard Spanish spelling (multiefecto?) to merge into, so dropped
# question omicron: Greek letter (ómicron) vs. variant/brand name; examples mostly brand, but kept as the Greek letter/Covid variant word, spelled without accent here
# question omicron: the Greek letter/variant would be ómicron, but the examples are all brand or star names; dropped.
# question part-time: hyphenated English loan; kept as an established loan, though Spanish also says "a tiempo parcial"
# question plexi: plexi is a clipped form of plexiglás; if plexiglás is not itself on the list, keep plexi instead.
# question plexi: shortened form of plexiglás, which may not be a listed lemma; if it isn't, keep plexi as its own entry
# question poms: "Pom Poms" may be a split loan or a cheerleading item; merged to pompón as the adapted Spanish spelling.
# question poms: the "Pom Poms" reading would merge to pompón, but the halves are split and POMS also has a scale reading, so I dropped it
# question protegiéndono: protegerse is also common, but the example is non-reflexive, so merged into the plain verb.
# question racquetball: English spelling of a sport; Spanish may write raquetbol, kept as an established loan like squash
# question racquetball: tagged VERB by the lemmatiser, but a noun for the sport; kept as an established loan
# question shunga: genre reading is under half of examples (about a third), dropped as non-established foreign word
# question sutta: Pali/Sanskrit loan in Buddhist texts; capitalised in 54% as part of titles, kept as an established term but borderline
# question tengu: Japanese creature with a plural in Spanish text; dropped as not established, could be kept like lowercase ethnonyms
# question tengu: lowercase uses (34 of 87) refer to the Japanese creature; dropped as not established in Spanish, but could be kept if the developer considers it an adapted organism-like cultural term
# question terrazzo: Spanish also writes terrazo (RAE); kept as the form people write, coordinator may prefer merge:terrazo.
# question terrazzo: terrazo is the Spanish spelling; the Italian form may be common enough in the trade to keep as a loan.
# question upct: regional technical university; not clearly a household name, so dropped
# question upct: single regional university (Cartagena); treated as not nationally famous
# question vaisnavas: religious adherents term, merged to singular vaisnava; could instead be dropped as specialist
# question viceversa: assumed viceversa is the standard form over the two-word vice versa
# question censurado: should participles used only adjectivally or as a fixed marker ([CENSURADO]) merge into the verb or keep their own adjective entry?
# question racquetball: the English spelling is frequent in Spanish web text; confirm raquetbol counts as the "form people write"
```

### Unflagged round (`s13-unflagged/questions.txt`)

```
# question amurar: forms (amura, amurado, amuro) are mixed; dropped as nautical jargon, but amura could be kept as a noun
# question amurar: split by form: amura, amuradas -> amura
# question bikiní: bikini and biquini are both accepted spellings; merged into bikini on the assumption that is the list's form.
# question choctaw: mostly capitalised in the sample, so it may be a name rather than a lowercase ethnonym; kept as an ethnonym
# question ciano: the colour cian is a DLE word, but the lemma is mostly the surname Ciano, so dropped
# question clarithromycin: the text is English, but claritromicina is a common generic antibiotic, so I merged it. Drop instead if only Spanish-form drug names should be counted.
# question clarithromycin: the text is untranslated English drug leaflets, so it could be dropped as a specialist drug; I treated it as a common generic antibiotic whose English spelling merges into claritromicina.
# question coatita: biblical clan name used as a lowercase ethnonym; kept as ethnonym, could be treated as a proper noun
# question creepers: Minecraft "creepers" is used in Spanish gaming text and the shoe style is also common; I judged it not established enough and dropped it.
# question cubicar: forms are mostly cubico/cubicas, probably cúbico without the accent, but the verb cubicar (8 cubicar, 4 cubicaron) is also real; I chose the majority reading
# question cubicar: no examples were shown; I assumed cubico/cubicas are mostly misspelt cúbico/cúbicas, but "cubicar" (to measure volume) is a real verb, so a split by form may be needed: split by form: cubicar, cubicaron, Cubique -> cubicar.
# question elementar: forms (elementares, elementes, Elementaría) look Portuguese or garbled; merge:elemental was considered but is not clear
# question elementar: forms (elementares, elementes, Elementaría) mix elemental plural and noise; dropped, but elementares could merge into elemental
# question escán: no examples; assumed a clipped form of escáner, though it could be a different word
# question escán: no examples; merged to escáner on the assumption it is a clipped form of the scan loan
# question fakes: is "fake" itself on the list as a loan? Merged on the assumption it is.
# question fakes: possible merge into fake if "fake" is an established loan; dropped for now
# question fluídica: RAE lists fluídico, but fluido/fluídico may be preferred; merged into fluídico as the lemma form
# question fluídica: the accent on fluídico is uncertain, I merged it to fluídico as the spelling in the counted text.
# question foodies: is "foodie" established enough in Spanish? Merged on the assumption it is.
# question fuéle: rules cover clitics -nos/-te only; I merged to the plain verb ser for the archaic fue + le
# question gamonal: real Spanish word (cacique) is present in lowercase and plural forms but is under a third of examples; dropped as mainly a place name.
# question hoster: split by form: hostería -> hostería
# question háganse: could also merge into plain hacer; I chose hacerse since "hacerse escuchar" is a pronominal use
# question incompresible: examples mix the real physics word with misspellings of incomprensible; kept as the real word.
# question incompresible: the real physics reading is about a third of the examples; the other two are typos for incomprensible
# question kasba: casba is the RAE form, but the list may prefer the form people write (kasba); merged to the academy form
# question marcaria: could also be marcaría (conditional of marcar) without the accent, but the examples all show the adjective, so merged into marcario
# question marcaria: possibly the rare adjective marcario (imagen marcaria), but some hits may be the verb form marcaría. Dropped as too rare and mixed.
# question mariscar: split by form: mariscada, mariscadas, Mariscadas -> mariscada
# question microempresaria: rules keep nouns with their own feminine entry, but this is only a regular -a form of microempresario, so I merged it
# question montadora: it may be a Portuguese-influenced feminine ("automaker") that could instead merge into montador
# question pecanas: the lemma could be pecano or pecana; I chose pecana, as in "nuez pecana".
# question pegilado: adapted medical adjective, could count as a common generic drug term; dropped as specialist
# question playitas: the common-noun reading (small beaches) is unclear and below a third of the examples, so dropped
# question quántum: the form is mixed with the company name Quanta System and the plural "quanta"; unclear whether the target should be quantum or cuanto
# question rodiada: target could be rodiar (verb) vs rodiado (adjective); chose the adjective since it is used as one
# question semillita: diminutives are not covered by the rules; kept as separate entries (same for viajecito)
# question tethering: the rules don't settle whether it is an established loan; dropped
# question cubicar: split by form: cubico, cubicas -> cúbico
# question customizable: should a Spanish-formed adjective from a discouraged but established anglicism verb (customizar) keep its own entry, rather than drop in favour of personalizable?
# question mariscar: split by form: mariscada, mariscadas, Mariscadas -> mariscada
```
