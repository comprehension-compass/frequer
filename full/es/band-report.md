# es band report: where real lemmas stop (review to 30k, current counts)

Built from the frozen 105,726,244-token counts. The exclusion list, 2,519 merges (accent and review), the junk
rules and six review rounds (two independent reviewers each, plus an adjudicator) are applied. Nothing is
pending in the 30k list except 184 place names, which wait for the reviewed learnable-names list. **Not a
snapshot**: the developer chooses the cutoff.

## Per band (positions in the reviewed list)

| band | frequency at band edges | candidates in band | kept | dropped: proper nouns | dropped: other junk | real share of candidates | unflagged keeps that are not real (blind check, n=60) | est. real lemmas in band |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 0–10k | – / 332 | 11,575 | 10,000 | 1,190 | 385 | 85 % | ~2 % (3 of the 4 flagged were learnable places) | ~9,800 |
| 10–20k | 332 / 62 | 17,521 | 10,000 | 5,264 | 2,257 | 54 % | ~8 % | ~9,200 |
| 20–25k | 62 / 33 | 11,526 | 5,000 | 4,440 | 2,086 | 34 % | ~22 % | ~3,900 |
| 25–30k | 33 / 20 | 13,260 | 5,000 | 5,684 | 2,576 | 29 % | ~23 % | ~3,850 |

"Real share of candidates" = kept x (1 - residual junk rate) / candidates. The residual rate comes from 60
random unflagged keeps per band judged blind (real / wrong form / junk). With n=60 each estimate is ±~10 points.

**How thin the bands are** (split halves of the counted text, current filters):

| depth | halves agree on top-N | median rank difference between halves |
|---|---:|---:|
| 10k | 97.8 % | 348 |
| 20k | 95.1 % | 1,354 |
| 25k | 93.5 % | 2,376 |
| 30k | 90.4 % | 3,785 |

The halves each have half the text; the full list is about 1.4x steadier. Rank 25k rests on about 33
occurrences, rank 30k on about 20. The extended count (running) roughly doubles that.

## Residual junk the blind check found in kept lemmas

- 20–25k: putt, cnel, mamma, whiskey, garnet, preciollamar, suomi, flore, eletrobras; wrong forms adecue,
  amadísimos, nausear, masajea.
- 25–30k: dente, mutandis, qe, sopra, asamblea nacional constituyente, conselleria, huevar, sequim, cruzi,
  back-office, elektra, estadio olímpico; wrong forms amiotrófica, interesantísimo.

Kept lemmas carried no flag, so no rule caught these: Italian and Catalan words, Latin phrase pieces,
inflected forms filed as lemmas, and multi-word names. Below 20k, roughly one kept lemma in five is still
junk. A deeper cutoff would want a further pass, either another rule or a review of unflagged lemmas.

## Samples of kept lemmas ([rev] = kept by review; [place?] = waiting for the names list)

Near 25k: waffle, avísenme, benzodiazepina, cooperante, escrutar, excomulgar, mesoterapia, poner en peligro algo,
tipi, autocrático, ceca [rev], dipolo, policlínico, religiosamente, benzodiacepina, elusivo, equinácea,
exnovia [rev], menopáusico, muellir, oceanografía, popper, pulular, ghee, humear, laicidad, marginalidad,
subestructura, tagalo, tuareg

Near 30k: psicomotricidad, sirolimus, titubeo, usurero, zambo, de escándalo, encarrilar, encintadora, facetada,
hanseático, mandón, motoniveladora, progubernamental, rencoroso, serr [place?], servio, sitel, uff, ídem,
aleatorización, arable, areata, crisma, dramamine, espadaña, hurra, infotainment, limonar [rev], multiétnica,
myqnapcloud

## Fragment merges (citation + shape; reviewed, applied)

muell → muelle, personalizabl → personalizable, ofrecerl → ofrecer, dobl → doble, encuentr → encontrar, brindarl → brindar, puzl → puzle, descargabl → descargable, enseñarl → enseñar, proporcionarl → proporcionar, multipl → múltiple, azafr → azafrán, increibl → increíble, mostrarl → mostrar, coleccionabl → coleccionable, psiquiatr → psiquiatría, prevenibl → prevenible, jugabl → jugable, servirl → servir, waffl → wafle, masticabl → masticable, invaluabl → invaluable, agradecerl → agradecer, otorgarl → otorgar, permitirl → permitir, descartabl → descartable, transmitirl → transmitir, enviarl → enviar, espectrometr → espectrometría, idolatr → idolatría, liposolubl → liposoluble, causarl → causar, compartirl → compartir, hablarl → hablar, llevarl → llevar, hazl → hacer.

Dropped: prorock-perforación, start-ups, al-tec, hijoshijo, autr, sampl, sagr, wearabl, recogedoras-picadora, chevr, chambr, chartr, cazadores-recolector, pre-order, u-erre. Pending names: cornuall, roncesvall.

## Questions from review rounds 4-6

# question calleja/chau/molle/vernal/tola/peta: lemma is a real DLE common word but most counted occurrences are a place, surname or organisation; applied keep (a real word is never dropped or sent to pending-names for contamination), so its rank is inflated
# question vigesimoprimero/decimonoveno/vigesimoséptimo: ordinal counted only from numerals (21º, 19ª), never written as a word; applied drop (a learner reads digits, not this word)
# question nro/ctra/dra/bloq: abbreviations are neither acronyms nor words in the rules; applied merge into the full word (número, carretera, doctor, bloqueo) rather than drop
# question walkman/post-it/pyrex: genericised brand names used as ordinary nouns; applied keep or merge into the DLE spelling (pósit, pírex) instead of the brand-drop rule; scotch dropped because its counts are brand/whisky labels
# question vitamin/aluminum/magnesium/condominium/apocalypse/patche: English spelling whose counts are English product text or titles, not Spanish use; applied merge into the DLE word per the adapted-spelling rule, which adds non-Spanish counts to it
# question jaina/aten/rie/sistem/ced: lemma is not itself a Spanish word, real-word reading is a minority of occurrences; applied drop (dominant sense is a name/brand/mix) rather than merge
# question rae/socimi/sicav/dafo/crispr: line between organisation, specialist and ordinary-word acronyms; applied drop for RAE (organisation) and CRISPR (specialist), keep for SOCIMI, SICAV (DLE) and DAFO (ordinary business term)
# question espa/erg/salut/mesto/aar/tyre/verger: non-Spanish token or fragment occurring only inside place names; applied pending-names, though the names list may want the full name (España, Erg Chebbi) rather than the fragment
# question sentaos/acercaos/expresas: inflected or enclitic verb forms filed as lemmas; applied merge to the bare infinitive (sentar, acercar, expresar), not the pronominal form
# question vending/kale/snooker/lager/commodity/emailing vs dimmer/shaker/sneaker/soundtrack/ecolodge/gelato: "established loan" threshold; applied keep where Spanish has no common everyday equivalent in general text, drop where Spanish routinely uses its own word (regulador, coctelera, zapatilla, banda sonora, helado)
# question causa-efecto: established but compositional hyphen compounds (also investigación-acción, marxismo-leninismo, árabe-israelí, contencioso-administrativo, cubano-americano) dropped because both parts are already on the list; confirm, or should fixed terms of art be kept?
# question huai: tokens seen only as pieces of multiword place names (also lesser, prata) were sent to pending-names; should the names list take fragments, or should these drop here?
# question bobal: grape varieties treated as common nouns (lowercase in Spanish wine text) and kept; confirm this applies to the whole class
# question roast: the English half of a multiword loan (roast beef) merged into the one-word DLE form rosbif; confirm this is the intended handling for such pieces
# question hmong: ethnonyms/language names (hmong, lakota) are not places or personal names; kept as lowercase common nouns. Confirm, or should they drop or go to pending-names?
# question selo: a token that is only one word of multiword place names (selo in Donje Selo, conta in Cala Conta) was sent to pending-names. Confirm, or should such fragments drop?
# question berebere: a DLE-listed variant spelling (berebere) was merged into the main DLE form (bereber). Confirm that DLE variants merge rather than stay separate.
# question extensométrico: specialist but ordinary-form words (not acronyms) were kept, since the specialist rule names only acronyms. Confirm.
