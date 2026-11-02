# Review rules (German; adapted from the developer's binding es rules, 2026-11-01)

Honeyeater's German frequency list (the lemmas a learner studies, counted from 451M tokens of German web
text and Tatoeba) is being cleaned. **The loaded list is the learnable set: anything on it is learnable,
anything not on it is ignored by the app.** Each lemma below was flagged by an automatic heuristic. You
decide what happens to it. The flag says why it was sent; it is evidence, not a verdict.

**Decisions** (exactly one per lemma):
- `keep`: a real German word (or an established loan) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong, misspelt or cut-off lemma, when the right German lemma is
  obvious; give that lemma as German writes it, with its capital if it is a noun (e.g. `merge:für`,
  `merge:Straße`, `merge:Familie`). Never merge two different words (*schon* is not *schön*, *Masse* is not
  *Maße*, *zahlen* is not *zählen*): in that case `keep`.
**Proper nouns** (flag `propn_usage`; the percentage is how often the word follows *ein/kein* or an
adjective, which names rarely do: under 3 % reads as a name):
- Place names: the learnable ones (countries, continents, oceans, major regions, well-known cities) are on a
  separate reviewed list and have already been taken out of your batch. **Any place name you still see is not
  on that list: `drop`** (towns, villages, districts, streets, minor rivers, foreign cities).
- Languages and nationalities are ordinary words in German (Deutsch, Englisch, Franzose): `keep`.
- The developer added Atlantik, Pazifik, Arktis, Sibirien, Sahara, Skandinavien, Korea, Weißrussland, Mazedonien,
  Westdeutschland, Dublin and Seoul to the learnable places (2026-11-02).
- **Nationally famous institutions** that people refer to by name are learnable: `keep` (Bundestag,
  Bundesrat, Bundesregierung, Bundeswehr, Bundesliga, ARD, ZDF, Deutsche Bahn, Polizei-like bodies, EU, UNO,
  NATO, DB, Telekom, WDR, Greenpeace, UEFA, Hamas, taz, NABU, KfW, EKD). Developer rulings 2026-11-01/02.
- Other names drop: people (first names, surnames, historical and cultural figures), brands, companies,
  products, minor organisations, websites, sports clubs, titles.
- Common nouns stay: words the tagger mistook for names (Hotel, Pizza, Villa, Jury, Meditation, Union in
  its common sense): `keep`.
- Acronyms used as ordinary words in German stay (EU, USA, DDR, GmbH, PDF, USB, SMS, CD, WLAN, ICE): `keep`
  (USA and EU are also place-like: `keep`). Brand, company, party and organisation acronyms drop (BMW, VW,
  SAP, FC, BVB are names: `drop`; parties such as CDU, SPD are nationally famous institutions: `keep`). Technical acronyms only specialists use (HTML, SEO,
  URL, CSS, SSL) drop.

**Foreign words** (flag `foreign`): drop English words that are not established in German; keep loans
established enough that an English-speaking learner would want to know German uses them (Computer, Team,
Job, Internet, online, Website, Software, Marketing, Shop, Event, cool). Real German words that look English
stay (also, will, die, man, war, Hand, Kind, Gift, Rat, bald).

**Shape** (flag `shape`): **a hyphenated compound is judged like any other word** (developer ruling 2026-11-02): keep
it when it is a real German compound a learner would want (Android-Smartphone, PDF-Format, E-Mail, T-Shirt, Know-how);
drop doubled words and splitter junk (Arbeits-Bahn). **Abbreviations are excluded for now** (developer ruling
2026-11-02: zB, Hbf, cm, mg, Dr, ca, Kfz, PLZ; they will be lemmatised to their full words): `drop`. Acronyms used
as words (EU, USA, DDR, GmbH, PDF, USB, SMS, WLAN) stay. Single letters drop, except real one-letter words (none in German besides the article-like letters in
names: drop them). Lemmas over the length limit: keep real compounds, drop concatenation junk.

**Citation** (flag `citation`: the lemma's own spelling is almost never written as a word): usually a broken
or cut-off lemma. `merge:` into the right lemma when it is obvious (a clipped real word: *Famili* ->
`merge:Familie`; a wrong-case or wrong-ending citation: `merge:` the dictionary form); otherwise `drop`.

**Low diversity** (flag `diversity`: concentrated in few documents): drop template, spam or brand text; keep
real words.

**Spelled numbers** (standing rule, developer 2026-11-01): a lemma made only of number words is `drop` unless
it is one of 0-30 (null ... dreißig), the tens (vierzig ... neunzig), hundert, tausend, Million, Milliarde,
Billion; compounds such as *einundvierzig*, *dreihundertsechzig*, *zweitausendzweiundzwanzig* drop. Ordinals
above 30 drop too (einunddreißigste); ordinals 1-30 and number-derived ordinary words (erste, zweite, Hälfte, Dutzend, doppelt) are words: decide normally.

**Umlaut merges** (proposed `merge` on a plain spelling: *fur*, *fuer*, *strasse*): confirm with
`merge:<target>` if the plain spelling is only the umlaut/ß word written without it; `keep` if it is a
different real word (then it is not merged).

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
