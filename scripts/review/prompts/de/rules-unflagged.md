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

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
