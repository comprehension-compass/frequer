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

## Later rounds (2026-11-01/02)

Rounds 4-7 reviewed the lemmas pulled into the widening window (to 31.5k) and turned the lemmatiser
fragments into merges. Rounds 8-9 reviewed the lemmas no rule flagged, in two stages: two screeners marked
each `ok` or `suspect`, and the union of suspects (minus units, homograph keys and learnable names, which are
the release's own entries) went through two reviewers and an adjudicator, with example sentences.

| round | screened | reviewed | keep | drop | merge | pending-names |
|---|---:|---:|---:|---:|---:|---:|
| 8 (positions 1-10k) | 9,538 | 307 | 139 | 62 | 102 | 4 |
| 9 (positions 10k-30k) | 18,744 | 2,946 | 323 | 1,239 | 1,160 | 224 |

**Institutions** (developer ruling, 2026-11-01: famous institutions that aren't places are kept): four
screeners read the 23,842 earlier drops in the 30k window (7,286 review drops, 16,556 automatic proper-noun
drops) and picked 754; two reviewers and an adjudicator kept 158 (127 earlier review drops overturned). A
reviewed keep now overrides the automatic proper-noun drop.

**Place names** (Honeyeater #766 `1bf77f0`, `reference/learnable-names/es.json`, 1,010 names): a place in
the list is learnable even when its name is also a common word; any other place drops. Of the 430 pending
place names, 11 are in the list (kept) and 419 drop. Round 1's "major city" keeps that are not in the list
drop (Perth, Brisbane, Edmonton, Albacete, Zamora, Elche, Teruel, Bursa, Freetown, Perm, URSS); CDMX and EUA
merge into Ciudad de México and Estados Unidos. Learnable names outside the top 30k are appended after it.

## Developer rulings (2026-11-02)

1. **Split loanwords.** A two-token loan whose halves only occur together is one entry: the first half
   merges into the compound and the second half follows it (*ping* → *ping-pong*, *pong* follows; *hip* →
   *hip hop*, *hop* follows; also *modus operandi*, *mutatis mutandis*, *savoir faire*, found as the list
   pairs whose two-token sequence covers at least 60 % of both halves' frequency). The second half is
   dropped rather than merged, because its occurrences are the same phrase: merging both would count each
   occurrence twice.
2. ***halar* / *hala*.** *halar* was a broken lemma holding two words. It is split by form
   (`split:halo|hala=…` in `corpora/review/es.tsv`, `junk.apply_splits`): the *Hala* forms go to *hala*,
   the interjection, which is its own entry; the rest (*halo* the noun, plus a few verb forms) merge into *halo*.
   The other counts (documents, POS, sources) move in proportion to the forms.
3. **Verb forms that are also interjections.** A learner's need decides, not the sampled sentences.
   Where the release keys the interjection as its own lemma (*vaya*, from capitalised *Vaya*; *ojalá*;
   *hala*), it stays as its own entry. Where the release folds it into the verb (*venga* → *venir*,
   *anda* → *andar*, *oye* → *oír*, *vamos* → *ir*), the interjection is counted inside the verb's entry:
   a separate key the release never produces would never match a token in the reader.

4. **Adapted spellings of currencies and loans:** the list uses the form people write (*forint*, not the
   academy's *forinto*); the recommended form can be a card note later.
5. **International bodies:** the institutions rule covers famous international bodies (OTAN, OMS, AIEA, ONU, UE),
   which are kept.

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
