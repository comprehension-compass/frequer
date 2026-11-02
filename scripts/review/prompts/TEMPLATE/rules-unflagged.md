# Review rules (the developer's; binding)

Honeyeater's <Language> frequency list (the lemmas a learner studies) is being cleaned. **The list is the
learnable set.** Each lemma below passed every automatic filter, but a screener marked it as possibly junk. You
decide what happens to it. The screener's note is a hint, not a verdict; most of these will turn out to be fine.

**Decisions** (exactly one per lemma): `keep`, `drop`, `merge:<lemma>`, `pending-names`, as in the flagged rules.

**The lemmatiser's conventions stand.** Function words that are their own lemma, pronouns, nouns with their own
feminine or masculine entry, pronominal verbs and established plural-only nouns are `keep` (<examples>). Don't
merge a word into a lemma just because a dictionary lists them together; merge only when the lemma is clearly
broken (a misspelling, a missing accent, a plural or conjugated form filed as a lemma, an English spelling of an
adapted word, an abbreviation of a listed word, a cut-off fragment).

**Proper nouns**, **foreign words**, **abbreviations** and **shape**: as in the flagged rules (place names
`pending-names`; famous institutions `keep`; other names drop; established loans keep; specialist acronyms and
digit-only ordinals drop).

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
