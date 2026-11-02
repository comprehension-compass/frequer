# Review rules (the developer's; binding)

Honeyeater's Japanese frequency list (the lemmas a learner studies, counted from Japanese web text and
Tatoeba) is being cleaned. **The list is the learnable set: anything on it is learnable by default, anything
not on it is ignored.** Each lemma below was flagged by an automatic heuristic; you decide what happens to it.
The flag says why it was sent; it is evidence, not a verdict. Lemmas are written as the lemmatiser writes them:
verbs and adjectives in their dictionary form (送る, 怖い), nouns in their usual spelling; a key after `#` is a
reading that tells two words apart (金#きん).

**Decisions** (exactly one per lemma):
- `keep`: a real Japanese word (including established katakana loans) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong or clipped lemma, when the right lemma is obvious from the
  examples; give that lemma in dictionary form as Japanese writes it (e.g. `merge:送る`, `merge:警察`).
- `pending-names`: a place name (country, region, prefecture, city, town, district, river, mountain...). Do not
  judge whether it is learnable: a separate reviewed list decides that.

**Proper nouns** (flag `propn_band`; the evidence says what Sudachi's dictionary has for the word):
- Place names: `pending-names`.
- Famous institutions stay: `keep` nationally famous universities, ministries and government bodies,
  broadcasters, and companies people talk about as institutions (東大, 文部科学省, NHK-like broadcasters,
  major household-name corporations as institutions).
- Other names drop: people (real or fictional; characters), minor companies, brands, products, websites,
  apps, titles of works, sports teams, and named facilities (stations, lines, airports, buildings).
- Era names (元号: 令和, 平成, 昭和, 明治...) stay: `keep`.
- Common words the tagger mistook for names stay: `keep` (返品, メンズ, ドラマー, 産後, マルチメディア).
- A katakana clipping of a longer word (スポ, キャ): `merge:` into it when the examples make it clear, else `drop`.
- A word with both a name and a common sense (光, 誠): `keep` when the common sense is in everyday use and
  shows in the examples; `drop` when the counts are names and the common sense is rare.
- Genericised brands stay only when Japanese uses them as the ordinary word for the thing; otherwise `drop`.

**Adult and sex-industry words**: keep the ones a learner meets in ordinary reading (風俗); drop spam and
jargon that only web spam makes frequent (デリヘル, セフレ).

**Spelled numbers** (千九百九十八, 四百六十): drop; only the core number words (up to 30, and 百 千 万 億 兆
alone) are on the list.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template, shop, spam and fan-fiction
text (product and drug brand names, character names, site boilerplate); keep real words even when the examples
are spammy.

**Shape** (flag `shape`; for Japanese, a single character the wider language rarely writes alone): a single
character that is a real standalone word stays (瞼, 桶, 錆). One that is a piece of a longer word the lemmatiser
cut off (送 from 送る or 送信, 警 from 警察) is `merge:` into that word when the examples make it clear;
otherwise `drop` (a lone bound kanji drops).

**Citation** (flag `citation`, the lemma's spelling is almost never written as a word): keep when the lemma is
the standard dictionary form even though texts write it otherwise (a kanji spelling written in kana); `merge:`
when it is a broken form of an obvious lemma; otherwise `drop`.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
