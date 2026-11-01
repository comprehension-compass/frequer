# es junk-filter review, 2026-11-01

The 20k es snapshot is built from the frozen 105,726,244-token counts. The junk rules flag lemmas
(`frequer/junk.py`, `corpora/es.yaml` `junk:`), and every lemma with a single flag, or in the proper-noun
middle band, within the top 20k (round 3: within 21.5k) was reviewed. Two independent reviewers saw the rules
below, the lemma, its rank, frequency, POS, the flag(s) and 2-3 example sentences from the counted text, and
never each other's answers. An adjudicator settled the disagreements. Decisions:
`corpora/review/es.tsv` (the build applies them; a merge target counts as reviewed).

| round | lemmas | agreed | adjudicated | keep | drop | merge |
|---|---:|---:|---:|---:|---:|---:|
| 1 (top 20k) | 2,635 | 2,531 | 104 | 500 | 2,023 | 112 |
| 2 (pulled in by round 1's drops) | 587 | 568 | 19 | 92 | 462 | 33 |
| 3 (window widened to 21.5k) | 660 | 635 | 25 | 75 | 551 | 34 |
| **total** | **3,882** | | **148** | **667** | **3,036** | **179** |

## Questions for the developer

Round 1:
# question major city: no threshold given; applied Hispanic world = provincial/state capitals or over ~200k (Oviedo, Albacete, Zamora, Teruel, Elche keep; Torrevieja drop), elsewhere metro over ~1M (Perth, Brisbane, Edmonton keep; Winnipeg drop)
# question intergovernmental bodies: rules keep ONU but drop organisations; kept only household global bodies (ONU, UE, OTAN, OMS, FMI, UNESCO, UNICEF), dropped specialised/regional ones (FAO, OEA, OMC, OIT, OCDE, ACNUR, OPEP), national agencies (NASA, BOE) and sports bodies (FIFA)
# question hyphenated compounds: kept dictionary nouns (sofá-cama, espacio-tiempo), dropped web compounds and technical variants (usb-c)
# question generic-concept vs specialist acronyms: kept those used unglossed in general press and daily life (ODS, TLC, MBA, ADSL, RRHH, APA), dropped professional/specialist ones (RSE, PPA, DOP, AINE, IRM, RMN, ERGE, ATP, SPF) and named single treaties (TLCAN, ALCA)
# question genericised brands: kept only where the DLE accepts the common noun (polaroid, kevlar); dropped the rest (bic, whatsapp, which has wasap)
# question English spelling of a Spanish loan: merge to the DLE form when examples show Spanish usage (sándwich, champú, dron, píxel, bol, béisbol); drop when examples are only English names/titles (tennis, zodiac, onyx, stereo, mania)
# question real word, artefact counts: dropped when the rank comes entirely from junk (centilitro from .cl, hilandero from spam, nonagésimo from numerals, kilocaloría from kcal)
# question common sense vs name: kept when the common sense is in everyday use (gallardo, yang, hobbit); dropped when counts are names and the common sense is rare (augusto, amador, alca, kata, aba)
# question unit symbols: merged to the written word (mg to miligramo; watt to vatio); currency names kept as common nouns (rand, leu)
# question words living only in fixed phrases: kept the lemma (ton in sin ton ni son, grosso in grosso modo); multiword lemmas (feng shui) not available
# question ambiguous inflected forms: merged by the examples' sense (fue to ser); voseo forms to the infinitive (mir to mirar)
# question cultural figures: people dropped even when culturally core (Cervantes), per the people rule

Round 2:
# question talavera: round 1 drops real words whose counts are entirely junk, but what about mostly junk (one real use among place-name hits, as with talavera and tula)? I kept them; should a majority of junk counts drop the word?
# question vu: can a merge target be a multiword lemma that may not be on the list yet (déjà vu, rayos X)? Or should fragments of fixed phrases drop, or merge into a component word (rayo)?
# question shooting: where is the line for loans established mainly in Spain or in one domain (shooting in fashion, trolley in retail, wrap on menus)? I kept wrap and dropped shooting and trolley.

Round 3:
# question tifoideo: citation flag fires when the masculine lemma is never written (only fiebre tifoidea); kept as the correct DLE citation form; confirm masculine lemmas stand even when only the feminine occurs
# question tonic: lemma is one part of a multiword loan (gin tonic); kept rather than merged, since no single-token target is obvious; should such parts keep or merge into a multiword lemma?
# question celebritie: broken English plural of a loan whose Spanish equivalent is a different word (celebridad); dropped rather than merged into the translation; confirm translation targets are never merges

## The rules the reviewers had

# Review rules (the developer's; binding)

Honeyeater's Spanish frequency list (the top 20,000 lemmas a learner studies, counted from Spanish web text
and Tatoeba) is being cleaned. Each lemma below was flagged by an automatic heuristic. You decide what
happens to it. The flag says why it was sent; it is evidence, not a verdict.

**Decisions** (exactly one per lemma):
- `keep`: a real Spanish word (or an established loan) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong or misspelt lemma, when the right Spanish lemma is
  obvious; give that lemma, written as Spanish writes it (e.g. `merge:indígena`, `merge:herpes`).

**Proper nouns** (flag `propn_band`):
- Countries, languages and major cities are learnable: `keep`.
- Other names drop: people, brands, companies, products, organisations, websites, smaller places.
- Common nouns stay: words the tagger mistook for names (kayak, rock, zoo, máster, hostel, safari, palma,
  cala, bingo, jaguar, margarita): `keep`.
- Acronyms: acronyms used as ordinary words in Spanish stay (IVA, ADN, ONG, PIB, VIH, PDF, TV, PC, USB, GPS,
  SMS, ONU): `keep`. Brand, company and organisation acronyms drop (HP, LG, IBM, BBC, FBI, DHL).
  Technical acronyms only specialists use (dll, ssl, xml, rgpd) drop: a learner would not study them.

**Foreign words** (flag `foreign`): drop English words that are not established in Spanish; keep loans
established enough that an English-speaking learner would want to know Spanish uses them (show, web, online,
marketing, chat, blog, email, low cost). Real Spanish words that look English stay (once, red, pie, sale).

**Shape** (flag `shape`): drop hyphenated web compounds (calidad-precio, salón-comedor), doubled words
(señorseñor) and fragments cut mid-word (jugabl). Keep established hyphenated words or loans (wi-fi, e-mail)
if a learner would study them.

**Citation** (flag `citation`, the lemma's spelling is never written as a word): usually a broken lemma.
`merge:` into the right lemma when it is obvious; otherwise `drop`.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template or brand text; keep
real words.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
