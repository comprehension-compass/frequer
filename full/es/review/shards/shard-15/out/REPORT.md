# es review shard 15: report (round 16, cascade)

Branch `es-review-shard-15`, created from `origin/full-es` at `ee1d9e0`. The rules files are unchanged since
0095cdd. I reused shard 11's runtime, wheel and sample, copied into `$HOME/es-review-15`, and reran the setup
script there for the config and `routed.tsv`. All `review.py` lines passed `--rules` and
`--decisions keep,drop,merge`. There were no failed calls and nothing was rerun.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 368 |
| flagged with an example | 290 (78.8%: **under the ~85% mark**) |
| flagged reviewers agreed | 357 (drop 295, merge 44, keep 18); 11 sent to the adjudicator; 0 accent-only merges |
| flagged queried at the gate | 2 |
| flagged adjudicated (11 disagreements + 2 queries) | 13 (keep 1, drop 9, merge 3) |
| **flagged final** | **keep 17, drop 304, merge 47** |
| unflagged screened | 394 (2 batches, 0 failed) |
| suspects (either screener) | 229 (201 marked by both) |
| suspects with an example | 187 (81.7%: **under the ~85% mark**) |
| unflagged reviewers agreed | 219 (drop 95, merge 62, keep 62); 10 sent to the adjudicator; 3 accent-only merges (dueno, mercaderia, copisteria) |
| unflagged queried at the gate | 1 |
| unflagged adjudicated (10 disagreements + 1 query) | 11 (drop 4, merge 7) |
| **unflagged final** (suspects only; the 165 non-suspects stay keep) | **keep 62, drop 98, merge 69** |

## Gate

I read every agreed merge and keep in both rounds and all the agreed drops (lemma and reason). I checked forms
where a drop or merge might hide a real word (almirez, chicote, butrón, nade, milodón, recriar, golosinar,
asulto, motoquero, farellón, descasar, rezón); those decisions hold, each real reading being a small minority.
The accent-only merges are plain misspellings.

Flagged queries → adjudicator:
- feoga (agreed keep as an international body; an EU agricultural fund) → **drop** (specialist; consistent with
  shard 11's ORECE).
- sicofaa (agreed keep as a regional body; an air-force cooperation system of the Americas) → **drop** (not a
  household name like OEA).

Unflagged queries → adjudicator:
- mujere (agreed drop as not a word; 79 occurrences of "mujeres" cut off) → **merge:mujer** (an obvious merge).

## Things for the coordinator

- Example coverage is under ~85% in both queues (78.8% and 81.7%). Per the instructions I noted it and carried on.
- Split-by-form questions (ruling 2), which the coordinator writes: habar (habar, the real noun → habar; the rest
  are misspelt haber), salariar (salaries → drop as English; the salariado forms → salariado).
- Possible new classes of question:
  - how famous a "regional or international body" must be under the 2026-11-02 ruling (feoga, sicofaa, orop,
    mibel); the adjudicator applied the base rule's fame test;
  - programmes and benefits rather than institutions (imv, Ingreso Mínimo Vital);
  - hospital acronyms that patients use (ucip);
  - a split loan whose first half isn't in the batch (fraiche, from crème fraîche);
  - very technical but well-formed Spanish words (lipopolisacárido, braquioplastia);
  - where common generic drugs end and specialist ones begin (venlafaxine, temazepam, nitrofurantoína);
  - fanclub: solid form, or a unit such as fan club or club de fans?

## Every `# question` line

The question lines are in `s15-flagged/questions.txt` (41 lines) and `s15-unflagged/questions.txt` (35 lines),
reproduced below.

### s15-flagged
```
# question afro-americanas: target lemma written as masculine singular "afroamericano" per the gentilic-to-masculine ruling; the list may spell it "afroamericano" or "afro-americano", please confirm.
# question afro-americanas: target spelled afroamericano (masculine, no hyphen) per feminine-gentilic and hyphen-variant rulings; confirm this is the standard form on the list.
# question almirez: real word (mortar), but only about a quarter of the examples use it that way, so I dropped it under the one-third rule
# question anti-rayado: antirrayado is the regular prefix spelling, but antirayaduras is also common; merged to antirrayado.
# question anti-rayado: the standard Spanish form is unclear (antirrayado vs antirrayaduras); merged to antirrayado
# question areal: real Spanish word, but only about a fifth of examples are the common word (areal/areales), so dropped under the one-third rule
# question areal: real word (areal, areales) is about a quarter of occurrences; the rest are place names, so I dropped it under the one-third rule
# question cfgs: Spanish vocational-training acronym (ciclo formativo de grado superior) used in public life, so it could count as a public term; I dropped it as an education acronym.
# question colona: kept as the feminine of colono, but 66% of occurrences are capitalised and may be a place or name
# question colona: lowercase real-word reading is about 34%, borderline for the one-third rule; kept
# question conred: kept as a national body that is a household name in Guatemala, following the ETECSA ruling; other readings of the token are not attested.
# question conred: national disaster agency of Guatemala, kept under the national-bodies ruling; confirm it counts as a household name.
# question cubesat: established in space news but specialist; dropped as technical term
# question cubesat: specialist-leaning term; kept because it is common in Spanish space news
# question enlazado: kept as an adjective; it could be merged into enlazar if the lemmatiser treats participles that way
# question exedra: a real architectural term, but most occurrences are the Exedra hotel name, so dropped under the one-third rule
# question fanclub: established loan, though Spanish more often writes "club de fans"
# question feoga: obsolete EU fund; kept as an international body, but it could be treated as a specialist acronym
# question fraiche: "crème fraîche" has been treated as a split loan, with fraiche as the second half; the first-half lemma (creme) was not shown, so its merge is left to the coordinator.
# question fraiche: could be a loan "crème fraîche" kept as a unit; there is no first half "creme" or "crème" in this batch to merge, so I dropped it.
# question geo-cerca: merge target geocerca assumed as the standard spelling; unsure if the list uses geovalla or geocerca.
# question home-page: target homepage assumed; could instead be página de inicio if homepage is not on the list
# question imv: the Ingreso Mínimo Vital benefit is well known in Spain, but it is a programme rather than an institution; no examples to check
# question low-code: English tech term, may be established enough to keep; dropped as hyphenated and not yet a common Spanish loan
# question low-code: kept as established tech loan; borderline since it is hyphenated and fairly specialist.
# question mibel: Iberian electricity market, widely cited in Spanish energy news; I treated it as a market, not a national body, and dropped it.
# question orop: regional fisheries bodies could count as regional bodies (keep), but the acronym is specialist, so dropped.
# question pehuén: many examples are place or brand names ("Bosque Pehuén"), so the real-word share is unclear; I kept it as the tree name.
# question polycarbonate: examples are mostly English product titles, but merged as an English spelling of an adapted word
# question post-electoral: target postelectoral assumed (RAE prefers unhyphenated post- forms).
# question semi-estructuradas: target semiestructurado assumed; hyphen-less standard form.
# question sicofaa: international body but only known to specialists; kept under the regional/international bodies ruling
# question socio-espacial: merged to the solid spelling, though the rule says hyphenated compounds of two listed words drop; socio- is a prefix, not a listed word
# question storyline: English loan used in media/gaming; judged not established enough, borderline
# question taina: capitalised 65% of the time and may be a personal name; merged as the lowercase gentilic reading (taíno) is the only learner-relevant one
# question taina: no examples; merged to taíno on the assumption that most occurrences are the ethnonym, but it may be mostly a given name
# question traviesa: the examples show "campo a traviesa" (cross-country) and the lemmatiser may have filed feminine travieso here; if so, merge:travieso.
# question ucip: a common Spanish hospital acronym (unidad de cuidados intensivos pediátricos), but I treated it as specialist and dropped it
# question ucip: hospital acronym that is common among parents and patients but could count as specialist; kept
# question fanclub: keep the solid form, or merge into a two-word unit (fan club or club de fans)?
# question sicofaa, feoga: the 2026-11-02 ruling says "regional and international bodies keep", but the base rule requires fame. I dropped obscure ones (SICOFAA, FEOGA, like ORECE). Should every regional or EU body keep regardless of fame?
```

### s15-unflagged
```
# question aceña: many occurrences are place names (La Aceña de la Borrega), but the lowercase word is about a third of the examples, so it stays as the common word.
# question aceña: the examples are mostly place names, but the lowercase common word is about 39% of occurrences, so I kept it.
# question braquioplastia: a real adapted Spanish word, but a specialist procedure term; I dropped it as too technical.
# question camagüeyano: demonym derived from a place name; kept as a common word, rules don't mention demonyms of places explicitly.
# question cantalupo: examples mix the melon sense and the place name Cantalupo; the melon reading seems at least a third, so kept.
# question cantalupo: the place name Cantalupo is a large share of the examples; kept because the melon reading is likely about a third or more
# question chozo: capitalised Metroid-race uses are close to a third of the examples; kept because the lowercase real-word reading and sentence-initial uses are substantial.
# question dashi: increasingly used in Spanish cooking texts; dropped as not yet established.
# question desarrolado: lemma could be desarrollar (verb) rather than the adjective desarrollado; I merged to desarrollado.
# question descasar: real verb descasar is a minority of the forms, while descaso is Portuguese and descasamos often means "descansamos"; dropped as mixed
# question descubriéndose: could also go to the pronominal descubrirse; I chose the plain verb because the examples are mostly passive or reflexive uses.
# question descubriéndose: merged into the pronominal descubrirse; plain descubrir is a possible alternative.
# question djing: it is a loan with only moderate establishment in Spanish. I kept it, but it could instead merge into the DJ entry.
# question djing: kept as an established loan, but it is borderline; it could alternatively merge into DJ.
# question estrogenic: examples are untranslated English text, so merging into estrogénico is a judgement call
# question habar: split by form: habar (rare real noun, field of broad beans) -> habar; merged here to haber because the examples are misspelt haber
# question interiorizada: lemma is a participle adjective; target interiorizado assumed to be the listed adjective form, though interiorizar is also arguable.
# question lipopolisacárido: very specialist biochemical term; kept because it is a normal word, not junk, but the rules don't say whether such technical terms belong on a learner's list
# question machnovistas: merged into machnovista on the assumption that it is a real political term; drop it if it is judged too specialist.
# question manter: examples may be typos for mantener rather than true Portuguese; I dropped it as foreign.
# question metajuego: borderline loan-calque; kept as a common gaming term, but it could be judged too niche.
# question motoquero: a real regional word (Argentina/Uruguay), but all the examples are the site name "Motoqueros"; dropped on the one-third rule from the visible examples only
# question motoquero: real regional word (Argentina) but the examples are all the name "Motoqueros"; dropped as the real reading looks under a third.
# question muniqués: gentilic, kept as a lowercase demonym. The feminine and plural forms are folded into it; confirm the lemma is not treated as a place name.
# question nicrom: generic alloy name (nichrome) rather than a brand; dropped as specialist.
# question nitrofurantoína: a common antibiotic, but narrower than ibuprofeno or paracetamol; I dropped it as specialist, whereas the better-known mebendazol was kept.
# question plegadizo: forms are mostly feminine plural (plegadizas); kept as the masculine lemma.
# question registar: forms are both bare infinitive and clitic forms (registarse, registarte); merged into registrarse by the pronominal-verb convention, but plain registrar is also arguable.
# question revenir: revenir is not a dictionary headword; revenirse is the DLE verb, but the forms are almost all the participle revenido as an adjective, so a split or an adjective entry may be preferable.
# question salariar: split by form: salaries -> drop (English); salariado forms are the Spanish word, merged into salariado
# question temazepam: prescription sleep drug; unclear whether it counts as a common generic drug, decided drop
# question transpondor: RAE standard is transpondedor, but the list may prefer transponder; merged to transpondedor
# question transpondor: transpondedor vs the loan transponder as target; I chose the academy form transpondedor.
# question upselling: could count as an established business loan like marketing; dropped as specialist.
# question venlafaxine: the rules say specialist drugs drop and English spellings of adapted words merge; I merged it into venlafaxina, but the coordinator may prefer to drop it if venlafaxina counts as specialist.
```
