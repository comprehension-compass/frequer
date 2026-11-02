# es review shard 3: report

Branch `es-review-shard-3` from `c4aacac`. First pass only: nothing is applied to `corpora/review/es.tsv` and
`collect.py` was not run.

**Adjudication rerun (coordinator's request).** The first adjudication ran without `--rules`, so it used uplift's
old rules. Both rounds were adjudicated again with the same gate queries under the final rules
(`--rules review/rules/es-flagged-final.md` and `es-unflagged-final.md`, as in full-es `f117a3a`). Before the rerun I
moved the old `adjudication/` aside and restored `questions.txt` to the reviewers' stage-1 set. All numbers below come
from the rerun. Compared with the old-rules run, 19 flagged decisions and 18 unflagged decisions changed, and no lemma
is `pending-names` any more.

## Counts

| step | result |
|---|---|
| flagged queue | 963 lemmas (`pending`) |
| flagged examples | 867 / 963 (90.0 %) |
| flagged reviewers | 933 agreed (83 keep, 776 drop, 74 merge), 30 disagreements, 7 accent-only merges, 0 failed calls |
| flagged gate | 16 queries |
| flagged adjudication | 917 agreed + 46 adjudicated (30 disagreements + 16 queries), 0 undecided |
| **flagged final** | **keep 93, drop 786, merge 84** |
| unflagged screening | 4,955 screened (the 4,956th was left out as a learnable-name release entry), 20 batches, 0 failed; 895 suspects (685 marked by both screeners) |
| suspect examples | 825 / 895 (92.2 %) |
| suspect reviewers | 837 agreed (420 keep, 228 drop, 189 merge), 58 disagreements, 13 accent-only merges, 0 failed calls |
| suspect gate | 19 queries |
| suspect adjudication | 818 agreed + 77 adjudicated (58 disagreements + 19 queries), 0 undecided |
| **unflagged final** | **keep 447, drop 236, merge 212** (the other 4,060 screened lemmas stay `keep`) |

Both example shares are above 85 %.

## Gate queries and outcomes

I read every agreed merge, both rounds' accent-only merges, every flagged-round agreed keep, and all of the
unflagged-round agreed drops (plus a sample of 80 flagged drops). I queried agreed decisions that might hide a
second real word: merges whose source is also a separate word, and drops of real common words that the
common-word rule might keep. The full reasons are in each round's `queries.tsv`.

**Flagged** (16 queries):
- Merges upheld: moje → mojar, meleno → melena, siller → sillería, distraerno → distraer, haciéndono → hacer and
  escríbano → escribir.
- jesus → Jesús was changed to **drop** (every example is the person).
- Drops checked against the common-word rule: ruma, jobo, ilion, champa, casimir, pepito and bode became **keep**;
  medica and rema stayed **drop**.

**Unflagged** (19 queries):
- guarda, decorado, colocado and logos became **keep** (each is a separate noun or adjective).
- refino, critico, desdecir, marrar, mochar and translucir kept their merges.
- samario, castillejo, rolar and cienciología became **keep**; gob became **merge:gobierno**; sueno became
  **merge:sueño**; luxar, medicinar and rho stayed or became **drop**.

## Points for the coordinator

- **Pronominal clitic forms are still mixed.** reconciliarno, uniéndote and uníos now merge to the pronominal verb,
  but distraerno and haciéndono merge to the plain verb (both agreed by the reviewers and upheld on query).
- **`pending-names`.** The flagged adjudicator notes that the answer format offers `pending-names` but the final rules
  don't define it, so it never used it.
- **Too many questions.** The unflagged adjudicator again wrote 10 grouped questions, above the README's 5–6.
- **The out/ directory is gitignored.** A generic `out/` rule in `.gitignore` covers this directory, so the files
  were added with `git add -f`.

## Adjudicator questions (grouped, final-rules run)

**s3-flagged**
# question jesus: should major religious figures (Jesús, Dios's peers) or the interjection ¡Jesús! be a list lemma, overriding the drop rule for people's names?
# question bode, champa: real words that are rare or regional (archaic, Central American only); does the common-word rule keep them even when a learner would rarely meet them?
# question ala-pívot: the hyphenated-compound drop rule removes an established term written hyphenated by convention; should such terms be an exception?
# question pending-names: the answer format offers this decision, but the rules don't define it, so I didn't use it
# question contra-notificación, pre-evento: should a hyphenated prefix (contra-, pre-) count as an adapted word to merge into the joined spelling, or as a "hyphenated compound of two listed words" to drop when the prefix is also a listed word (contra)? And should rare prefixed technical terms merge at all?
# question hadith: the "form people write" rule (forint) and the "English spelling merges" rule (click → clic) conflict when the English spelling (hadith) is about as common in Spanish text as the adapted form (hadiz). Which rule wins?

**s3-unflagged**
# question olimpíada, trascurrir, trasgresión: when an accepted variant is a separate lemma beside the standard form (olimpiada, transcurrir, transgresión), should both stay, or should the minority variant merge?
# question guarda, decorado, colocado, hinchada: when kept for the noun or adjective reading, should the occurrences that are really the verb (guárdala, the decorado/hinchada participles) be moved to the verb lemma?
# question oseltamivir: should generic drug names be dropped as specialist, or kept when common (ibuprofeno, paracetamol)? Where is the line?
# question rho: for Greek letters, should the English-style spelling (rho) merge into the Spanish form (ro) when the letter reading dominates?
# question metoprolol, haloperidol: should generic drug names count as specialist and drop, or as ordinary common nouns that are kept?
# question bajísimo, preciosísima: should -ísimo superlatives stay as their own lemmas or merge into the base adjective?
# question parquing: is a regional (Catalan-influenced) adapted spelling kept as written, or merged into parking or parquin?
# question ametrallador: 112 of 161 occurrences are ametralladora, a separate common noun; should it get its own entry rather than stay hidden under ametrallador?
# question videir: is the list's lemma video or vídeo? Both are standard, and the rules don't say which form wins when regions differ.
# question gob: with no examples, some GOB/gob occurrences may be gob.mx/gob.es domain artefacts rather than the abbreviation.

## Every `# question` line (reviewers, then the adjudicator, as pooled in `questions.txt`)

### s3-flagged

```
# question aguayo: the surname reading dominates, but the lowercase uses are the real Spanish word.
# question ala-pívot: established basketball term, but the rule says to drop hyphenated compounds of two listed words
# question atascadero: the examples are almost all the place name, but it is also a real Spanish common word, so I kept it
# question balaclava: examples are mostly the place name, but the lowercase common word exists. Kept as a common word.
# question banzai: mostly capitalised in names (Banzai Pipeline, Banzai Athletic), but a real DLE word; kept as common word
# question banzai: the interjection exists in Spanish, but the examples are mostly names, so dropped
# question barangay: Philippine administrative unit with some Spanish-language use; I judged it not established
# question batel: 79% of occurrences are the Curitiba neighbourhood or a surname, but batel is a real Spanish common word, so I kept it
# question batel: most occurrences are the name Batel (a Curitiba district and a surname), but batel is a real Spanish word with plural bateles, so I kept it.
# question biotec: split between lowercase "biotec" as an abbreviation of biotecnología and capitalised company names; I chose drop because the abbreviation reading is not clearly the majority.
# question bluray: could be read as a product/brand (drop) or an established technology term like DVD (keep); I kept it
# question bluray: the standard spelling is Blu-ray or blu-ray, and the hyphenated-spelling rule might apply. Kept as an established loan.
# question bottom-up: a finance and management loan, but hyphenated and English; dropped.
# question braña: dialect word whose occurrences are mostly names; kept as a real common word.
# question braña: mostly surnames/place names, but also a real dialect word; kept as common word
# question carrero: a real but rare word that is mostly a surname in the text; kept under the common-word rule
# question casimir: the cloth sense (casimir) is possible, but the name dominates
# question ceoe: a business confederation; treated as a famous national body, not an ordinary organisation.
# question cereteo: a biblical people name that appears only in the plural. I treated it as a proper noun and dropped it, but it could count as a common gentilic.
# question cereteo: biblical people name, only plural attested; dropped as a proper name, though it could be read as a rare common noun
# question chaise-longue: the loan is established, but I am not sure whether the list writes it "chaise longue" or "chaise-longue"
# question champa: examples missing; judged name/place
# question chilli: could be a person or brand name rather than an English spelling of chile
# question chute: The real-word reading (shot) is a minority of the examples, but chute is a genuine Spanish word.
# question chute: lowercase chutes is a real Spanish word for shots in football, but the capitalised uses are mostly place names; dropped.
# question cireneo: gentilicio of Cirene, so arguably a place-derived word; kept as a real common word (RAE also lists cirineo).
# question clipping: it is an established term in Latin American press and PR, but the examples are mostly page headings.
# question clipping: many examples are menu or site text, but the PR and audio sense is established
# question cloche: kept as an established fashion loan, but the examples mix French and English contexts.
# question cnte: a Mexican teachers' union could count as a famous public body, but it is a trade union, so I dropped it
# question cofides: state-owned development finance company; unclear whether it counts as a public body
# question coulomb: Spanish standard form is culombio, so merge:culombio may be better, but examples show the surname (Coulomb's law) and columbio (niobium), so the lemma is mixed.
# question coulomb: the Spanish adapted form is culombio; the examples mix the unit with the surname and "columbio" (an old name for niobium), so merge:culombio could be argued, but I kept it as the unit name.
# question cul-de-sac: hyphenated French loan; kept as established, though many examples are place names
# question cunef: a notable Madrid business school, but probably not a nationally famous institution.
# question cunef: nationally famous institution or a minor private school? Kept as a known Madrid university centre.
# question duce: historical title for Mussolini; kept as a dictionary word, but the rule on titles could be read to drop it
# question e-bikes: could be dropped as a hyphenated loan, but I merged it into e-bike
# question e-bikes: e-bike itself is hyphenated; I merged the plural into the singular, but the whole family could be dropped as a hyphenated spelling
# question esplanada: Spanish has explanada, but the examples are all the Brasília name, so I dropped it.
# question floorball: a real sport name, but not common enough in Spanish to count as established.
# question floorball: niche sport name, kept as a loan only because Spanish texts use it by that name
# question franchising: Spanish also uses franquicia, but franchising is common in business Spanish, so I kept it.
# question franchising: loan is established in business Spanish, though franquicia is the native form; kept.
# question free-to-play: hyphenated three-word English loan; kept as an established gaming term, but it could instead be dropped as a hyphenated compound.
# question free-to-play: hyphenated three-word English loan; kept as an established gaming term, but not clearly covered by the rules
# question fué: Merged into ser as the lemma of "fue", but fue could also be ir.
# question gavi: could count as a famous international body like OMS, but it is a vaccine alliance and not widely known by name, so I dropped it.
# question gavi: international vaccine alliance; unclear if famous enough to count as a famous international body
# question gchq: a famous national body but not a Spanish-world one or on the international list, so I dropped it
# question hadith: Spanish also writes hadiz; kept as written since the list uses the form people write
# question hadith: hadiz is the academy form, but people often write hadith; I merged it as an English spelling of an adapted word
# question ieo: could be the Instituto Español de Oceanografía, but the examples mix in a crypto token offering
# question igv: a national tax acronym like IVA, but only Peruvian; kept as ordinary-word acronym
# question igv: a regional (Peru) tax acronym; I treated it like IVA, but it could be seen as too specialised.
# question ilion: the anatomical ilion is a real but rare word, and most examples are Troy or a US town, so I dropped it.
# question ilion: the bone sense "ilion" is real Spanish, but most examples are Troy or Ilion, NY, so I dropped it
# question in-game: hyphenated gaming loan, could count as an established loan, but not adapted into Spanish; dropped
# question jesus: Jesús is a person's name, which would drop, but the form is a missing-accent spelling of a common Spanish word and interjection, so I merged it
# question jesus: the occurrences are the religious figure, which could count as a person name and drop. Merged because the accent is clearly missing and ¡Jesús! is also a real interjection.
# question jobo: Jobo is a real tree name, but the examples are overwhelmingly the company; dropped as unlikely for learners.
# question kaiju: it may count as an established loan through film use, but I judged it a franchise term
# question kundalini: a Sanskrit term used in Spanish yoga and spirituality writing; unclear whether it counts as established enough to keep
# question kundalini: a Sanskrit term used in Spanish yoga texts; unclear whether it counts as established enough to keep.
# question li-polímero: hyphenated, but the unhyphenated battery term may be a real word; dropped under the hyphenated-compound rule
# question lo-fi: hyphenated, but not a compound of two listed Spanish words, so it was kept as an established music loan
# question lombardo: the lemma mixes the demonym/adjective with the surname; I kept it as a common word
# question maasai: many examples are place names (Maasai Mara); merged because community use is the real-word reading
# question medica: some all-caps examples read as unaccented MEDICA for médica, but most are the trade fair or company name; I dropped it
# question mers: disease acronym; kept as in-news ordinary word, but could count as specialist.
# question mers: specialist disease acronym or ordinary word like VIH?
# question mici: Panamanian ministry acronym, but the examples are thin and "mici" also names a Romanian dish. Kept as a ministry.
# question mici: may be Panama's Ministerio de Comercio e Industrias, which would be a ministry; dropped as too obscure.
# question midrash: Spanish writes midrash/midrás; kept as an established religious term, but it is specialist vocabulary
# question midrash: a specialist religious term, but it is established in Spanish, so I kept it.
# question mili: capitalised in 67% of text and no examples were available, so the name reading may dominate; I kept it as the real word.
# question mili: mostly a name in the counted text, but "la mili" is a real Spanish word; kept
# question nnuu: abbreviation of Naciones Unidas; merged into ONU as the nearest listed form
# question nodosa: mixed medical adjective (nodoso) and company name; merged on the adjective reading
# question nodosa: the lowercase medical use (poliarteritis nodosa) is a real word, but it is a minority of the examples
# question noh: Japanese theatre genre; "teatro noh" is used in Spanish, but it is specialist
# question olvídate: the target could be olvidar or olvidarse; I chose the pronominal olvidarse because the imperative with "te" matches it.
# question oops: could be kept as an English interjection loan, but the Spanish adaptation is ups, so it was merged.
# question opensource: merged into "open source" as a split-loan style spelling; "código abierto" would be the Spanish alternative
# question parfait: real dessert word in some examples, but most occurrences are names or brands, so I dropped it
# question parfait: the examples mix the dessert, a jar brand and a beer style, so the dessert reading may not be the majority
# question passiflora: it could merge to pasiflora, but the text uses the Latin genus name, so I dropped it
# question pepito: Pepito also means a sandwich in Spanish, but the examples are mostly the name, so I dropped it.
# question pnv: a famous Spanish political party, but parties are not on the list of kept institutions; dropped as an ordinary organisation
# question pnv: major Spanish party, but the rules keep only institutions like universities, ministries, broadcasters and public bodies, not parties; dropped as an ordinary organisation
# question poké: no examples shown, and 89% capitalised suggests restaurant or brand names; kept as the established loan
# question poké: poke (Hawaiian dish) is arguably an established loan, but the evidence (89% capitalised, no examples) points to names, so I dropped it
# question ponibl: forms are -ponibles from several verbs (disponibles, componibles, reponibles); merge to disponible is a best guess
# question poum: historical Spanish party; treated as an ordinary organisation, not a famous institution
# question poum: historically famous Spanish party, but not an institution on the keep list; dropped as an ordinary organisation.
# question punky: mixed brand/name use; merged to punki since the common-word reading dominates
# question rema: "rema" is a real Spanish word (rheme / verb form of remar), but the counts are mostly all-caps or capitalised acronym/name use, so I dropped it
# question rfef: a federation rather than a ministry or broadcaster; kept as a nationally famous public body, which may be a stretch
# question ruma: Spanish "ruma" (pile, Andean usage) exists, but the capitalised-name reading dominates, so dropped.
# question sepi: SEPI is a state holding company rather than a public body in the usual sense, so keep is borderline
# question serón: common word, but most occurrences are the town Serón; kept under the common-word rule
# question shipibo: The rules don't cover ethnonyms; kept as a common noun/adjective.
# question sisben: a Colombian state system rather than a body, but referred to by name like a public body; kept.
# question tex-mex: hyphenated loan whose parts are not listed words; kept as an established loan
# question tex-mex: hyphenated, but not a compound of two listed words; kept as established loan
# question theravada: a proper-noun school of Buddhism, not a place or institution; kept as an established term in Spanish religious writing, but could be read as "other names drop".
# question theravada: a religious tradition rather than a person or place, which the proper-noun rules do not cover; I chose drop.
# question tomatina: the festival is a Spanish cultural term, but the rules treat events as names; dropped
# question tomatina: the festival name is an event, but "tomatina" is also a dictionary common noun; I kept it.
# question tooltip: could count as an established computing loan; I dropped it because most examples are English UI text.
# question tooltip: used in Spanish software texts but mostly in English strings; dropped as not yet an established loan
# question triqui: ethnonym rather than a place name, so kept as a common word
# question triqui: mostly an ethnonym, but the lowercase uses are the adjective or language, so it may be a learner word.
# question tupperware: brand name but used generically as "tupper"; rules say brands drop, so dropped
# question tupperware: genericised brand used as a common noun in some uses, but it is a brand and the usual Spanish word is "tupper"
# question uclm: Regional public university (Castilla-La Mancha); unclear if "nationally famous" enough to keep.
# question uclm: a large public university, but regional rather than nationally famous like UNAM; dropped.
# question uip: Inter-Parliamentary Union is international but not clearly as famous as ONU or OMS.
# question unitec: Mexican university, but private and not as widely known as UNAM
# question unitec: UNITEC may be a known Mexican or Honduran university, but it is not clearly nationally famous; dropped
# question varo: common word in Mexican slang, but 88% capitalised and likely mostly a surname; kept under the common-word rule
# question varo: mostly capitalised surname in examples, but a real Spanish word (Mexican "varos" = money), so kept
# question win-win: hyphenated English, kept as an established business loan; it could instead be treated as a foreign hyphenated spelling
# question win-win: hyphenated, but an established business loan; kept as such
# question yeshiva: established loan or foreign term? Kept.
# question yeshiva: established loan, or a foreign proper noun (mostly "Yeshiva University")?
# question zirconia: the real-word reading (zirconia cúbica) may be a minority of the examples, many of which are English product listings.
# question ala-pívot: the hyphenated-compound drop rule removes an established term written hyphenated by convention; should such terms be an exception?
# question bode, champa: real words that are rare or regional (archaic, Central American only); does the common-word rule keep them even when a learner would rarely meet them?
# question contra-notificación, pre-evento: should a hyphenated prefix (contra-, pre-) count as an adapted word to merge into the joined spelling, or as a "hyphenated compound of two listed words" to drop when the prefix is also a listed word (contra)? And should rare prefixed technical terms merge at all?
# question hadith: the "form people write" rule (forint) and the "English spelling merges" rule (click → clic) conflict when the English spelling (hadith) is about as common in Spanish text as the adapted form (hadiz). Which rule wins?
# question jesus: should major religious figures (Jesús, Dios's peers) or the interjection ¡Jesús! be a list lemma, overriding the drop rule for people's names?
# question pending-names: the answer format offers this decision, but the rules don't define it, so I didn't use it
```

### s3-unflagged

```
# question acolchonar: the verb is real, but most forms are participles; merged into acolchonado like abullonar.
# question aforar: most occurrences are the noun aforo or the adjective aforado, so merge:aforo is possible, but aforar is a valid verb.
# question aforar: the examples mix the verb aforar (to gauge) with the noun aforo; merged to aforo as the dominant form
# question alambrar: alambrada and alambrado are about equal in frequency, so merge:alambrada is a coin flip
# question ametrallador: occurrences are mostly ametralladora (machine gun), a different noun from ametrallador (gunner); kept per the own-entry convention
# question antemano: kept because it occurs only in "de antemano", but it could count as a fragment
# question antemano: only occurs in the fixed phrase "de antemano"; kept as a real word rather than dropped as a fragment
# question antifatiga: it is tagged as a verb, but it is really an invariable adjective used after a noun. I kept it.
# question aplicante: English calque, but in real use in Latin American Spanish
# question aplicante: it may be a usable Latin American usage, but it is a calque with no standard status, so I dropped it.
# question aposentar: the noun aposento dominates the forms, but the verb lemma is real, so I kept it rather than merging
# question arquea: noun archaea (arqueas) mixed with verb arquear forms; kept as noun
# question azol: a real term but specialist; kept because it is a common noun, not an acronym or name
# question azol: real chemical-class noun in Spanish medical text, but I judged it specialist and dropped it.
# question backlink: SEO loan might count as established like "marketing" or "blog"; judged too niche
# question backlink: whether it counts as an established loan or specialist SEO jargon is unclear.
# question best-seller: unsure whether the list form is "bestseller", "best seller" or the hyphenated form; I merged to bestseller.
# question bilbaíno: demonyms derive from place names, but they are common words, so kept (same for tinerfeño)
# question bitcoines: the academy writes bitcóin, but many people write bitcoin; I chose the academy form.
# question biturbo: could be read as a brand term (BiTurbo), but it is a generic engine type, so I kept it.
# question brevísimo: superlatives that have their own dictionary entry are kept here, but the rules do not say whether to merge them into the base adjective (breve)
# question bundesbank: it is a famous institution but a German one, not a Spanish-world or international body, so I dropped it.
# question cantear: forms are mostly canteado/canteo; kept as a real verb and noun.
# question castillejo: also a rare common word (small castle), but nearly all uses are place names or surnames
# question ciclofosfamida: specialist drug name, unclear if a learner would want it; kept like mifepristona
# question ciclofosfamida: this may be a specialist term, though its sibling mifepristona is kept as a general health word.
# question cienciología: religion/organisation name, dropped as a proper name though it is a Spanish-spelt word
# question cogida: also a real noun (goring in bullfighting), but the examples and forms are the participle of coger, so merged
# question cogida: the noun (bullfighting goring) is real, but the evidence is mostly the participle, so merged into coger
# question cols: "y cols." is an abbreviation of colaboradores, and I merged it into the singular lemma colaborador.
# question confederar: merged to confederado because the forms are mostly the noun or adjective, but confederar is a real verb
# question confitar: kept as a real verb although forms are mostly the adjective confitado; same for liofilizar, entumecer, censar and escaldar
# question contouring: an established loan in beauty contexts, but many examples are product or event names.
# question contouring: makeup term, mostly in product and event names; kept as an established loan, but it could count as brand use
# question cosido: it is also a real adjective/noun, but here it is only a participle, so I merged it into coser.
# question cosido: participle used as adjective and noun; kept as its own entry, though merge:coser is arguable
# question crizotinib: same situation as darunavir, dropped
# question crossfader: DJ loan may be established enough to keep; treated as specialist and dropped
# question crossfader: DJ-equipment loan; may count as established enough to keep
# question cusita: a biblical demonym (Cushite) is kept as a common word, but it is rare and a learner may not want it
# question darunavir: drug INN spelled the same in Spanish; no rule covers specialist drug names, treated like specialist terms and dropped
# question desdecir: the lemma is a real verb (desdijo, desdecirse), but most occurrences are the noun desdicha; I merged on the majority.
# question desparecido: The correct lemma could be desaparecer (tagged VERB) rather than the participle desaparecido.
# question desparecido: the verb lemma desaparecer was chosen over the participle desaparecido because the examples are verbal.
# question desuscribir: attested in web Spanish but a calque; I dropped it, though a loan-like keep is arguable
# question desuscribir: widely used on web unsubscribe links, but non-standard; dropped as a calque
# question diada: Catalan loan; kept because the Spanish press uses it, but the rules don't cover regional-language words.
# question diada: the Catalan national day is widely used in Spanish, but I treated it as a foreign name
# question edomita: a biblical demonym; kept as an ordinary gentilic noun, though a learner may rarely need it.
# question ellxs: an inclusive-language variant of ellos; it could instead be dropped as a non-standard form.
# question ellxs: inclusive-language spelling; merged into ellos, but could be dropped as a non-standard form
# question encastrar: the forms are mostly participles and the noun encastre, but encastrar is a real verb, so I kept it.
# question ende: kept because it occurs only in "por ende", but it could count as a fragment
# question ende: only occurs in "por ende" and the screeners said fragment; kept as a real word
# question escarmentar: the forms are mixed noun (escarmiento) and verb, and I kept the verb lemma.
# question eslálom: the academy form is eslalon, but people mostly write slalom; merge:slalom could also be right
# question eslálom: the academy forms are eslalon and eslálom, but the counted text overwhelmingly writes slalom, so I merged into slalom.
# question estragar: estragar is a real verb, but the counted forms are mostly the noun estrago, so merged to estrago
# question estragar: most tokens are "estrago" (a noun), so the verb lemma may be a lemmatiser error. The verb itself is real.
# question exculparse: pronominal verb is valid, but the forms are non-pronominal, so merged into exculpar
# question extremi: "in extremis" is an established Latin phrase, but the split-loan rule would put its first half under a compound and drop this half, so the first half "in" is not in this batch
# question extremi: could instead be merge:extremis, depending on whether the list holds "in extremis" as one entry
# question filgrastim: a specialist INN drug name, kept for consistency with trazodona, though it may count as too technical
# question filgrastim: dropped as a specialist drug INN, in tension with keeping trazodona
# question flanger: it is a niche audio-effect loan, so I'm unsure how established it is.
# question flashcards: borderline loan; judged not established enough
# question flashcards: unclear whether flashcard is established enough in Spanish to keep, so I merged it into the singular.
# question flasheo: niche jargon from "flashear"; could count as an established derivation, but dropped as too specialist.
# question flasheo: slang/anglicism derivative from a narrow phone-repair domain; kept as established there
# question freaks: friki is the adapted form, but freak itself is also used in Spanish
# question genisteína: a real Spanish word but only specialists use it; dropped as specialist vocabulary
# question genisteína: real Spanish word, but I judged it a specialist chemical and dropped it.
# question glucomanano: rare specialist substance names (glucomanano, imatinib, rituximab, levodopa) are not covered by the rules; I kept them as generic non-brand common nouns.
# question gob: no examples; could be an abbreviation of gobierno, but not clear enough to merge
# question haloperidol: generic drug name, kept as an ordinary noun; the rules don't cover drug names (sulforafano and aliskiren dropped as more specialist)
# question haloperidol: generic drug names (haloperidol, aliskiren) are not covered by the rules; dropped as specialist terms.
# question hype: borderline loan; kept as established enough in media
# question innovativo: attested but nonstandard, merged to innovador.
# question innovativo: non-standard calque of innovador; dropped rather than merged because the lemma is not clearly broken
# question kasbahs: the RAE spelling is casba, but people write kasbah; merged to casba
# question kasbahs: unsure whether the list form should be casba or kasbah
# question lamanita: gentilic-like noun but a Book of Mormon group name; treated as a proper noun
# question laminar: forms are mostly laminado, but laminar is itself a real word, so kept
# question levodopa: generic drug names (also glucomanano, imatinib, rituximab) are kept as common nouns, but a learner list might treat them as specialist vocabulary.
# question lobbista: lobista is the academy form, but lobbista is what people write; I merged to lobista as an adapted spelling.
# question logos: Greek philosophical term vs. plural of logo; examples mostly the plural of logo, so merged
# question logos: Logos is also a real Spanish philosophical term, but the examples lean toward the plural of logo, and only capitalised forms occur.
# question mariguana: accepted academy variant of marihuana, so I kept it; merge:marihuana is the alternative
# question medido: forms are mostly "medida", which could be noun medida or the participle feminine; merged to medida
# question misceláneo: forms are mostly miscelánea, which may deserve its own lemma, but I kept the existing one
# question mochar: moche is also the Moche culture (a name) while mocho is a common adjective, so the merge target is uncertain.
# question monodisco: A real but specialist word; I dropped it, and turbomaquinaria likewise, but both are valid Spanish.
# question máxime: the screener called it Latin, but it is an ordinary Spanish adverb; I treated it as keep.
# question neurofeedback: established loan or specialist term, dropped as specialist
# question neurofeedback: possibly an established loan, but the examples read as a specialist term, so dropped
# question olimpíada: academy accepts both olimpiada and olimpíada, so it may merge into olimpiada if the list prefers the more common spelling.
# question onboarding: English business term; kept as an established loan but could be seen as jargon
# question onboarding: English business term; kept as an established loan, but it may not be established enough.
# question oseltamivir: generic drug name, not covered by the rules; dropped as specialist (same for metoprolol)
# question oseltamivir: rules do not cover generic drug names; kept as common nouns (same for metoprolol).
# question oximetolona: it is a real Spanish drug name, but I dropped it as too specialist.
# question oximetolona: this is a Spanish-form drug name. The rules don't say whether specialist drug names count, so I dropped it as too specialist, unlike triptano.
# question palmita: Most occurrences are place or group names; I kept it as the common diminutive of palma.
# question palmita: all examples are place or group names; kept only as the diminutive common word, so it may need to be dropped.
# question parquing: could merge to parking, but kept since it is the adapted spelling people write
# question pendientes: kept as the earrings noun, a plural-only use, but it could be merged into pendiente as a plural filed as lemma
# question pequeñísimo: unclear whether the superlative counts as a clearly broken lemma; merged into pequeño.
# question pescaíto: could merge to pescadito, but kept as the written colloquial form
# question pescaíto: dialectal spelling of pescadito; kept as an established Andalusian form, but merge:pescadito is arguable
# question pladur: it began as a brand, but it is used generically in Spanish, so I kept it.
# question pomodoro: Italian for tomato, but the technique name is a known loan; the pizza-brand examples are a minority, so I kept it.
# question pomodoro: the "Técnica Pomodoro" is a known loan, but most occurrences are the brand or the Italian word, so I dropped it.
# question ponzi: "esquema Ponzi" is common in Spanish, but it is a person's name, so dropped.
# question ponzi: a proper-noun-derived term in "esquema Ponzi"; dropped as a name but could count as established
# question portear: forms are mostly the noun porteo; kept rather than merged because both noun and verb are real.
# question preciosísima: feminine superlative filed as lemma; merged to preciosísimo, but could be kept as a derived form like bajísimo
# question preciosísima: superlatives (preciosísima, bajísimo) are merged into the base adjective as inflected forms; if the lemmatiser treats -ísimo forms as their own lemmas, keep them instead.
# question probenecid: also a Spanish pharmaceutical name; judged specialist
# question probenecid: this is also the Spanish drug name, but I treated it as a specialist term.
# question prácticar: nearly all occurrences are the form práctica (noun or verb); I chose the verb practicar
# question psyllium: Latin/English plant name used unchanged in Spanish supplement texts; kept as established
# question psyllium: Latin/English plant term used unadapted in Spanish; kept as established in health texts.
# question pudrir: its forms are mostly misspelt podrá/podrás, so merged to poder, though pudrir is also a real verb
# question pudrir: the lemma is real, but most of its counted forms are podra/podras, which are poder misspelt without the accent
# question rajatabla: it is a single word in the counted text, but the dictionary entry is the locution "a rajatabla". I kept it as a word.
# question rajatabla: it is only used in "a rajatabla"; I kept it as a single-token locution word rather than treating it as a fragment.
# question ralear: lemma mixes raleo, ralea and ralear forms; kept as a real verb.
# question renderizado: kept as a noun, but it could be merged into renderizar as a participle
# question ribavirin: drug names are specialist terms, but the Spanish form ribavirina is obvious, so I merged rather than dropped.
# question rohingyas: Fundéu prefers rohinyá, but the corpus writes rohingya; I used the form people write.
# question rohingyas: the RAE form is "rohinyá", but I used "rohingya" as the form people write; the rules do not say which to prefer.
# question rohinyás: The RAE form rohinyá is assumed to be the intended lemma; the learner list may prefer another spelling.
# question rolar: rolar exists in Mexican Spanish, but the forms are mostly role/Rolando, so dropped
# question rolar: rolar is a real verb in Latin American Spanish, but the forms are dominated by names and role, and no examples were shown.
# question rrss: abbreviation of "redes sociales", which is a two-word phrase and not a single lemma, so there is nothing obvious to merge into; dropped.
# question samario: samario is also the chemical element and a demonym, but the counted forms are mostly Samaria, so I dropped it.
# question silicón: merged into silicona, but it may be a legitimate Latin American variant
# question subzona: the dictionary lacks it, but it is a transparent sub- compound that is in real use. I kept it.
# question sueno: could be the unaccented form of sueño, but all examples are the place name Los Suenos, so dropped
# question sueno: the examples are mostly the place name Los Suenos, so it is dropped rather than merged into sueño; merge:sueño is the alternative.
# question sunamita: gentilic of a biblical place; dropped as a biblical name, but could be kept as a demonym like bilbaíno.
# question tenazas: it could be merged into tenaza, but I kept it because it is the usual plural-only form.
# question tica: could be merged into tico, but kept as a feminine form with its own entry.
# question tracio: forms are mostly Tracia, the place, which would be dropped; I kept the lemma for the demonym.
# question trascurrir: RAE accepts trascurrir as a variant of transcurrir, so I kept it rather than merging, but the list's convention on accepted variants is not explicit.
# question trasgresión: same case as trascurrir, an accepted variant of transgresión, kept as written.
# question trasmisión: the RAE accepts it as a variant, but I merged it because the list uses the form people write
# question trazodona: generic drug name; keep chosen as it is written in Spanish form, but the rules do not cover drug names
# question video: both video and vídeo are accepted; I kept video since the counted text mostly writes it that way (Latin American usage)
# question video: both vídeo and video are accepted by the RAE and the list uses the form people write, so I kept it rather than merging it into vídeo
# question violoncello: it is an Italian spelling of an adapted word rather than an English one, so merge is not clearly covered by the rules.
# question violoncello: the DLE lists violonchelo and violoncelo, so I merged into the more common violonchelo.
# question webhook: it could count as an established tech loan like web or blog, but I dropped it as developer jargon.
# question webhook: may count as an established tech loan like web or email; judged too specialist
# question xantana: feminine adjective form of xantano, but it is nearly always written this way in "goma xantana"; kept rather than merged
# question xantana: the feminine form of an adjective whose masculine "xantano" is rare. I kept it because the word appears almost only in "goma xantana".
# question zamak: could count as an ordinary technical noun for the alloy rather than a brand
# question zozobrar: the forms are mixed noun and verb, and I kept the verb lemma.
# question ametrallador: 112 of 161 occurrences are ametralladora, a separate common noun; should it get its own entry rather than stay hidden under ametrallador?
# question bajísimo, preciosísima: should -ísimo superlatives stay as their own lemmas or merge into the base adjective?
# question gob: with no examples, some GOB/gob occurrences may be gob.mx/gob.es domain artefacts rather than the abbreviation.
# question guarda, decorado, colocado, hinchada: when kept for the noun or adjective reading, should the occurrences that are really the verb (guárdala, the decorado/hinchada participles) be moved to the verb lemma?
# question metoprolol, haloperidol: should generic drug names count as specialist and drop, or as ordinary common nouns that are kept?
# question olimpíada, trascurrir, trasgresión: when an accepted variant is a separate lemma beside the standard form (olimpiada, transcurrir, transgresión), should both stay, or should the minority variant merge?
# question oseltamivir: should generic drug names be dropped as specialist, or kept when common (ibuprofeno, paracetamol)? Where is the line?
# question parquing: is a regional (Catalan-influenced) adapted spelling kept as written, or merged into parking or parquin?
# question rho: for Greek letters, should the English-style spelling (rho) merge into the Spanish form (ro) when the letter reading dominates?
# question videir: is the list's lemma video or vídeo? Both are standard, and the rules don't say which form wins when regions differ.
```
