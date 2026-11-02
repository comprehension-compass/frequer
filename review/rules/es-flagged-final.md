# Review rules (the developer's; binding)

Honeyeater's Spanish frequency list (the lemmas a learner studies, counted from Spanish web text and Tatoeba)
is being cleaned. Each lemma below was flagged by an automatic heuristic (shown with its evidence). You decide
what happens to it. The flag says why it was sent; it is evidence, not a verdict.

**Decisions** (exactly one per lemma):
- `keep`: a real Spanish word (or an established loan) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong or misspelt lemma, when the right Spanish lemma is
  obvious; give that lemma, written as Spanish writes it (e.g. `merge:indígena`, `merge:herpes`).

**The lemmatiser's conventions stand.** Function words that are their own lemma (la, los, una, al, del),
pronouns, nouns with their own feminine or masculine entry (hermana, actriz, reina), pronominal verbs
(hacerse, quedarse), and established plural-only nouns (gafas, vacaciones) are `keep`. Don't merge a word
into a lemma just because the dictionary lists them together; merge only when the lemma is clearly broken
(a misspelling, a missing accent, a plural or conjugated form filed as a lemma, an English spelling of an
adapted word, an abbreviation of a listed word, a cut-off fragment).

**Proper nouns**:
- **Place names** of any kind (cities, towns, regions, rivers, mountains, islands): `drop`. The reviewed list of the place names a learner needs is final, and every place on it is already kept automatically, so a place reaching you is not on it.
- **Famous institutions that aren't places are `keep`**: nationally famous universities, ministries,
  broadcasters and public bodies people refer to by name in the Spanish-speaking world (UNAM, RENFE, RTVE,
  Real Academia Española, Hacienda, Guardia Civil, ONCE, Seguridad Social and the like), and famous international
  bodies (ONU, UE, OTAN, OMS, AIEA, FMI, Unesco).
- Other names drop: people, minor companies, brands, products, ordinary organisations, websites, events,
  titles.
- A place name that is also a real Spanish common word stays as the common word (granada, nevada, sierra).
- A real Spanish common word stays even if many occurrences are a name (palma, cala, real, sol).
- Acronyms used as ordinary words in Spanish stay (IVA, ADN, ONG, PIB, VIH, PDF, TV, PC, USB, GPS, SMS, ONU,
  IP, WiFi). Brand, company and organisation acronyms drop. Technical acronyms only specialists use drop.

**Foreign words**: drop words from other languages that are not established in Spanish; keep loans
established enough that a learner would want to know Spanish uses them (show, web, online, marketing, chat,
blog, email, low cost, versus). Real Spanish words that look foreign stay (once, red, pie, sale).
A non-Spanish token whose real-word reading is a minority of the examples drops.

**Shape**: drop web artefacts, codes, doubled words and fragments cut mid-word unless a merge is obvious.
Specialist acronyms drop; ordinals only ever written as digits drop.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.

**Split loans**: a two-token loan whose halves only occur together is one entry: the first half
`merge:<the compound>` (hip → `merge:hip hop`), the second half `drop` (its occurrences are the same phrase).
**Interjections** that are their own lemma (vaya, hala, ojalá) are `keep`.
**Spellings**: the list uses the form people write (forint, not the academy's forinto); English or hyphenated
spellings of an adapted word that Spanish writes otherwise merge into that form (click → clic). Hyphenated
compounds of two listed words drop.
