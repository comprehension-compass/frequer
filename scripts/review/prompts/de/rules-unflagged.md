# Review rules (the developer's; binding)

Honeyeater's German frequency list (the lemmas a learner studies) is being cleaned. **The list is the
learnable set.** Each lemma below passed every automatic filter, but a screener marked it as possibly junk. You
decide what happens to it. The screener's note is a hint, not a verdict; most of these will turn out to be fine.

**Decisions** (exactly one per lemma): `keep`, `drop` or `merge:<lemma>`, as in the flagged rules.

**The lemmatiser's conventions stand.** Function words that are their own lemma, pronouns, nouns with their own
feminine or masculine entry, pronominal verbs and established plural-only nouns are `keep` (der, die, das, ein, eine as their own lemmas; Lehrerin; sich freuen; Leute, Ferien). Don't
merge a word into a lemma just because a dictionary lists them together; merge only when the lemma is clearly
broken (a misspelling, a missing accent, a plural or conjugated form filed as a lemma, an English spelling of an
adapted word, an abbreviation of a listed word, a cut-off fragment).

**Proper nouns**, **foreign words**, **abbreviations** and **shape**: as in the flagged rules (place names not on the list
drop; famous institutions `keep`; other names drop; established loans keep; specialist acronyms and
digit-only ordinals drop).

**Case and plural merges** (developer rulings 2026-11-02; fragments are merged, not dropped):
- A noun filed under a lower-case lemma (*vater*, *hammer*, *gesundheit*) or an adjective, adverb or verb filed under a
  capitalised lemma (*Blöd*, *Betätige*): `merge:<the correctly written lemma>` (*merge:Vater*, *merge:blöd*,
  *merge:betätigen*). A capitalised word that is really a noun in its own right (*das Gute*, *Essen*) stays `keep`.
- A noun filed under its plural (*Lippenstifte*, *Puzzles*, *Gruppenreisen*): `merge:<the singular>`. Plural-only
  nouns (*Leute*, *Ferien*, *Eltern*, *Kosten*) and plurals with a meaning of their own stay `keep`.
- An inflected or participle form filed as a lemma (*intakte*, *beworben*, *gesponsert*): `merge:` its dictionary
  form (*intakt*, *bewerben*, *sponsern*), unless the participle is an adjective with its own dictionary entry
  (*bekannt*, *verheiratet*, *ausgezeichnet*): then `keep`.
- Broken encoding or a dropped letter (*wrde*, *nchst*, *whlen*): `merge:` the real word when it is obvious.

Place names: the learnable ones are on Honeyeater's reviewed list and are kept automatically; **any place name you
still see is not on that list: `drop`**.

**Developer rulings of 2026-11-02 (second set; binding):**
1. Demonyms and place adjectives: `keep` for places on the learnable list (Berliner, Kölner, Münchner, Pariser); `drop` the rest (Erfurter, Essener, Gelsenkirchener).
2. Places added to the learnable list: Bosnien-Herzegowina, Moldawien, San Marino, Pjöngjang, Reykjavik, Themse, VAE (`keep`). Variant spellings of a listed place `merge:` its German form (Zimbabwe -> Simbabwe, Brasil -> Brasilien).
3. Institutions: `keep` AOK, TK, DAK, Barmer, PETA, Destatis and the major Swiss and Austrian parties (SVP, SP, FDP, ÖVP, SPÖ, FPÖ type); `drop` federal-ministry acronyms (BMZ, BMBF, BMAS, BMWi, BfArM), minor parties (GLP) and research institutes (DIW).
4. Famous landmarks with German names `keep` (Eiffelturm, Kolosseum, Jakobsweg); others such as Hockenheimring `drop`. Planets are learnable (Jupiter, Merkur, Saturn, Mars, Venus …): `keep`.
5. Genericised brands used as common nouns `keep` (Tempo, Kärcher, LEGO, Segway); other brands `drop` (Unimog, Maggi).
6. Ordinals: the -te form is the lemma (zweite, vierte): `merge:` other forms into it.
7. Binnen-I and other gender-inclusive forms (KundInnen, MitarbeiterInnen): `merge:` the base headword (Kunde, Mitarbeiter).
8. Colloquial contractions (ner, nem, gabs, ists, kannste, aufm, weils): `merge:` the host word (eine, ein, geben, sein, können, auf, weil).
9. Nominalisations: productive -en infinitives `merge:` the verb (das Fahren -> fahren); lexicalised ones keep their own entry (das Essen, das Leben, das Gute, Angestellte, Selbstständige).
10. einem, eines, einer, einen are their own lemmas (`keep`), like ein, eine.
11. Slurs and offensive words: `drop` as a class.
12. Abbreviations used as words `keep` (WG, Kita, Lkw, BH, OP, PR); unit symbols `drop` (kWh, kHz).
13. A lemma whose counts are mostly another word: decide by the lemma's own reading (the counts cannot be split here; such lemmas are listed for the lemmatiser).
14. Swiss ss spellings `merge:` the ß form (Gruss -> Gruß, Süsse -> süß).

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
