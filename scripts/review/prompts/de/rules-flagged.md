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
- **Nationally famous institutions** that people refer to by name are learnable: `keep` (Bundestag,
  Bundesrat, Bundesregierung, Bundeswehr, Bundesliga, ARD, ZDF, Deutsche Bahn, Polizei-like bodies, EU, UNO,
  NATO). Developer ruling 2026-11-01.
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

**Shape** (flag `shape`): drop hyphenated web compounds and doubled words; keep established hyphenated words
(E-Mail, T-Shirt, Know-how, Make-up) and established abbreviations a learner meets everywhere (z. B. as
`zum Beispiel` is a unit; bzw, ca, usw as words: `keep` only if the lemma is the abbreviation a learner reads
daily). Single letters drop, except real one-letter words (none in German besides the article-like letters in
names: drop them). Lemmas over the length limit: keep real compounds, drop concatenation junk.

**Citation** (flag `citation`: the lemma's own spelling is almost never written as a word): usually a broken
or cut-off lemma. `merge:` into the right lemma when it is obvious (a clipped real word: *Famili* ->
`merge:Familie`; a wrong-case or wrong-ending citation: `merge:` the dictionary form); otherwise `drop`.

**Low diversity** (flag `diversity`: concentrated in few documents): drop template, spam or brand text; keep
real words.

**Spelled numbers** (standing rule, developer 2026-11-01): a lemma made only of number words is `drop` unless
it is one of 0-30 (null ... dreißig), the tens (vierzig ... neunzig), hundert, tausend, Million, Milliarde,
Billion; compounds such as *einundvierzig*, *dreihundertsechzig*, *zweitausendzweiundzwanzig* drop. Ordinals
and number-derived ordinary words (erste, zweite, Hälfte, Dutzend, doppelt) are words: decide normally.

**Umlaut merges** (proposed `merge` on a plain spelling: *fur*, *fuer*, *strasse*): confirm with
`merge:<target>` if the plain spelling is only the umlaut/ß word written without it; `keep` if it is a
different real word (then it is not merged).

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
