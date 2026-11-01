# ja junk-filter review, 2026-11-01 (no snapshot built)

The ja list is the 689,675,997-token count (`report.md`), cleaned under the developer's standard: the loaded
snapshot is the learnable set. The junk rules (`frequer/junk.py`, `corpora/ja.yaml` `junk:`) flag lemmas, and
every flagged lemma within the first 30,000 kept places was reviewed, single and multiple flags alike
(`review_multi_flag`). Each lemma had two independent reviewers (Sonnet) who saw the rules below, the lemma,
its rank, frequency, POS, the flag(s) with their evidence, its written forms and 2-3 example sentences, and
never each other's answers. An adjudicator (Opus) settled the disagreements. The examples come from a
re-streamed 125M-character sample of five HPLT files plus Tatoeba, through the same hygiene. Each one is
confirmed by the runtime: the production sentence stage files that lemma in that sentence. 91% of the
reviewed lemmas had at least one example. Decisions: `corpora/review/ja.tsv`.

## Configuration for ja (and why)

| rule | ja setting | why |
|---|---|---|
| accent merges | off | no accents |
| proper nouns | `propn_band` with `propn_evidence: dictionary` (Sudachi core 固有名詞 subtags), not the case band | no capitalisation; the dictionary's subtags are evidence, not a guess |
| | every entry 人名/組織名 **and** tagged PROPN: dropped | name evidence. Tagged NOUN instead: reviewed, because Sudachi has no entry for words it builds from parts (お花 = お+花, 数人, 日目), so the whole surface shows only a name entry |
| | every entry a proper noun with 地名 among them: `pending-names` | place names wait for `reference/learnable-names/ja.json` |
| | PROPN tag without a dictionary proper noun (返品, メンズ), or 固有名詞-一般 only (brands, eras): one flag, reviewed | the tagger's PROPN alone is not a drop |
| | NUM never a dictionary name | Sudachi lists 六十四 as a given name |
| diversity | threshold 0.2 (es 0.6) | HPLT documents are long (~730 tokens), so real words clump; under 0.2 is almost all spam, fandom names and products, and 0.2-0.3 still holds real words (ダイエット, 稽古, 業者) |
| citation | kept; verb/adjective/copula citation forms exempt (`[うくぐすつぬぶむるいだ]$`); token-separated forms read joined (の で = ので); multi-token units exempt by kind | Japanese forms are stored per token, and unit headwords (〜として, 毎日新聞) have no spaces |
| shape | kept; the short-word test applies to one character only (`short_max_length: 1`), zipf < 3.5 | two kanji is an ordinary word; a lone character the language rarely writes alone is often a clipped piece (送, 警) |
| foreign | off | `lemma_pattern` admits no Latin script; katakana loans are Japanese words |

Generic fixes found on the way (self-contained commits on `full-ja`): wordfreq lookups without MeCab,
dictionary proper-noun evidence, citation on token-separated forms and units by kind, a reviewed decision
outranking the automatic proper-noun drop.

## Rounds

| round | lemmas | agreed | adjudicated | keep | drop | merge | pending-names |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 (window to 30k) | 2,077 | 1,950 | 127 | 1,182 | 813 | 32 | 50 |
| 2 (pulled in by round 1) | 90 | 82 | 8 | 51 | 35 | 3 | 1 |
| 3 | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| 4 (NOUN-tagged name-only words, after the PROPN requirement) | 643 | 632 | 11 | 25 | 609 | 8 | 1 |
| 5 (pulled in by round 4) | 32 | 32 | 0 | 0 | 31 | 0 | 1 |
| 6 (era names the dictionary misreads) | 5 | 5 | 0 | 5 | 0 | 0 | 0 |
| **total** | **2,849** | | **146** | **1,263** | **1,489** | **44** | **53** |
| audit (100 random unflagged keeps per band, not applied) | 400 | 390 | 10 | 363 | 22 | 12 | 3 |

The per-band report, samples, merges and questions are in `band-report.md`. Per-lemma actions are in `ja.routed.tsv`.

## The rules the reviewers had

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
- Other names drop: people (real or fictional; characters), companies, brands, products, organisations,
  websites, apps, titles of works, sports teams, and named facilities (stations, lines, airports, buildings).
- Common words the tagger mistook for names stay: `keep` (返品, メンズ, ドラマー, 産後, マルチメディア).
- A word with both a name and a common sense (光, 誠): `keep` when the common sense is in everyday use and
  shows in the examples; `drop` when the counts are names and the common sense is rare.
- Genericised brands stay only when Japanese uses them as the ordinary word for the thing; otherwise `drop`.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template, shop, spam and fan-fiction
text (product and drug brand names, character names, site boilerplate); keep real words even when the examples
are spammy.

**Shape** (flag `shape`; for Japanese, a single character the wider language rarely writes alone): a single
character that is a real standalone word stays (瞼, 桶, 錆). One that is a piece of a longer word the lemmatiser
cut off (送 from 送る or 送信, 警 from 警察) is `merge:` into that word when the examples make it clear;
otherwise `drop`.

**Citation** (flag `citation`, the lemma's spelling is almost never written as a word): keep when the lemma is
the standard dictionary form even though texts write it otherwise (a kanji spelling written in kana); `merge:`
when it is a broken form of an obvious lemma; otherwise `drop`.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
