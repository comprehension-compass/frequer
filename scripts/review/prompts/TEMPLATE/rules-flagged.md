# Review rules (the developer's; binding)

Honeyeater's <Language> frequency list (the lemmas a learner studies, counted from <Language> web text and
Tatoeba) is being cleaned. **The list is the learnable set: anything on it is learnable by default, anything
not on it is ignored.** Each lemma below was flagged by an automatic heuristic; you decide what happens to it.
The flag says why it was sent; it is evidence, not a verdict. Lemmas are written as the lemmatiser writes them
<describe: dictionary forms of verbs and adjectives; nouns <capitalised?>; a key after `#` tells two words apart>.

**Decisions** (exactly one per lemma):
- `keep`: a real <Language> word (or an established loan) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong, misspelt or cut-off lemma, when the right lemma is obvious
  from the examples; give that lemma as <Language> writes it (e.g. `merge:<example>`). Never merge two different
  words (<two real words that differ only by an accent or one letter>): in that case `keep`.
- `pending-names`: a place name (country, region, province, city, town, river, mountain...). Do not judge whether
  it is learnable: a separate reviewed list decides that.

**Proper nouns**:
- Place names: `pending-names`.
- Famous institutions that aren't places stay: `keep` nationally famous universities, ministries, broadcasters,
  public bodies and household-name institutions people refer to by name (<examples>), and major international
  bodies <Language> news names (UN, EU, NATO, WHO in their <Language> forms).
- Other names drop: people (real or fictional), minor companies, brands, products, websites, apps, titles of
  works, sports clubs, events, named facilities.
- Era names and calendar names stay (<examples, if the language has them>).
- Common words the tagger mistook for names stay: `keep` (<examples from the first round>).
- A word with both a name and a common sense: `keep` when the common sense is in everyday use and shows in the
  examples; `drop` when the counts are names and the common sense is rare.
- Genericised brands stay only when <Language> uses them as the ordinary word for the thing; otherwise `drop`.
- Acronyms used as ordinary words stay (<VAT, DNA, PDF, USB, SMS in their <Language> forms>). Brand, company
  and organisation acronyms drop. Technical acronyms only specialists use drop.

**Foreign words** (flag `foreign`): drop English (or other-language) words that are not established in
<Language>; keep loans established enough that a learner would want to know <Language> uses them (<examples>).
Real <Language> words that look English stay (<examples>). A non-<Language> token whose real-word reading is a
minority of the examples drops.

**Abbreviations** are not on the list for now (they are to be lemmatised to their full word later): `merge:`
into the full word when it is obvious, otherwise `drop`.

**Adult and sex-industry words**: keep the ones a learner meets in ordinary reading; drop spam and jargon that
only web spam makes frequent.

**Shape** (flag `shape`): drop hyphenated web compounds, doubled words, codes and fragments cut mid-word
(<examples>); keep established hyphenated words or loans a learner would study. <For a script without spaces:
a single character the language rarely writes alone is usually a clipped piece: `merge:` into its word when the
examples make it clear, otherwise `drop`.>

**Citation** (flag `citation`, the lemma's spelling is almost never written as a word): usually a broken lemma.
`merge:` into the right lemma when it is obvious; keep when the lemma is the standard dictionary form even
though texts write it otherwise; otherwise `drop`.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template, shop, spam and fan-fiction
text; keep real words even when the examples are spammy.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
