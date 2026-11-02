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

Generic fixes found on the way (on frequer `uplift`): wordfreq lookups without MeCab,
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

## The 40k snapshot (final, 2026-11-02)

The developer chose **40k**, after a final edge cleanup: rounds 14-16 (two reviewers plus the adjudicator)
over the flagged lemmas left at the edge, a second screen of the unflagged keeps in kept 35,000-40,500
(80 suspects), the named brand and fragment cases (分過ぎ, のり子, ギデオン, ソースネクスト dropped; ネットフリックス
kept under the famous-institutions ruling; 七号 kept as an ordinary noun, "No. 7"), and every undecided
unflagged keep in 39,900-40,500 (439). No lemma within the cut is pending.

`snapshots/ja.json`: **40,301 entries**, the reviewed top 40,000 (rank 40,000: とりとめ, 343 occurrences,
0.50 per million) plus 301 learnable names (250 counted below the cut, 51 never counted, さいたま filed
under 埼玉); 307 split multiword names in `learnable-multiword-names.tsv`. Counted through Honeyeater
`c07c7015` with `honeyeater_lemma_ja` 1.5.0; reference checkout Honeyeater #766 `5a12937`.
`load_lemmas ja --dry-run` (at #766): 40,301 ranked, 0 skipped, 2,542 unit headwords, 90 homograph keys.
Actions in the window: 34,606 keep, 5,394 review-keep, 4,652 review-drop, 2,297 place-drop, 1,218
dictionary name drop, 950 number drop; 560 merges; 10,651 review decisions over 16 rounds. Report:
`build-40k/report.md`. The 30k build is kept as an artefact in `build-30k/` (its `ja.json`, report, perf).

## The 30k build (2026-11-02, superseded by the 40k)

`ja.json` (in the build directory; the snapshot is not committed): **30,422 entries**, the reviewed
top 30,000 (rank 30,000: 表せる, 648 occurrences, 0.94 per million) plus 422 learnable names: 329 counted
below the cut, 93 never counted (frequency 0), and さいたま filed under 埼玉. 307 listed names the segmenter
splits (language names such as アイルランド語, seas, mountain ranges) are not appended: they are
`learnable-multiword-names.tsv`, input for lemma release 1.6. Reference checkout Honeyeater #766 `5a12937`
(learnable names, `lexicon.number_words.number_is_learnable`); counts stamped `c07c7015`.
`load_lemmas ja --dry-run` (at #766): 30,422 ranked, 0 skipped, 2,082 unit headwords, 84 homograph keys.

Actions in the 30k window: 27,636 keep, 2,364 review-keep, 2,367 review-drop, 1,211 place-drop,
682 dictionary name drop, 607 number drop; 527 merges; 10,102 review decisions over 13 rounds (round 9:
the 0-30k unflagged screen's 1,372 suspects; rounds 10-13: the 30-40k extension). Report:
`build-30k/report.md`. The 40k build is ready as an option; 19 flagged lemmas at its very edge
(kept 39,654-40,000) were left unreviewed.

## Developer rulings (2026-11-02)

Folded into the reviewer rules (`scripts/review/prompts/rules-ja.md`) and applied by re-review (round 8) where
they changed earlier decisions:

1. **Era names are kept** (令和, 平成, 昭和, 大正, 明治, 江戸): everyday vocabulary for dates.
2. **Famous institutions are kept**: nationally famous universities, ministries and government bodies,
   broadcasters, and companies people talk about as institutions (東大, 文部科学省, フジテレビ, トヨタ, 任天堂). This
   supersedes the provisional "drop as names". Ordinary names still drop: people, minor companies, brands,
   products. Round 8 re-decided the 281 institution drops: 190 now kept.
3. **Adult and sex-industry words**: kept when a learner meets them in ordinary reading (風俗); dropped when
   only web spam makes them frequent (デリヘル, セフレ, テレクラ). Round 8 re-decided the 57 slang and adult keeps:
   6 dropped.
4. **Lone bound kanji drop** (該, 弊, 耐): no merge target, so dropped; listed as segmentation feedback for
   lemma release 1.6 (Honeyeater `docs/plans/lemmatiser-release-1.6.md` §3).
5. **さくら kept, 楽天 dropped.** The explicit ruling wins over ruling 2, under which round 8 had kept 楽天;
   explicit developer rulings are a decisions file applied after every review round.
6. **Spelled numbers follow the app** (the number rule, `number_rule: true`): a lemma Honeyeater's
   `lexicon.number_words.number_is_learnable` calls a number it does not learn is dropped (千九百九十八, 五十,
   一万); its number vocabulary (百, 千, 万, 億, 兆, 三百, 六百, 八百, 千万, 三千, 八千...) and numerals up to 30 stay,
   and counters and date forms are not numbers (一つ, 二十日).
7. **Cutoff: 30,000**, then the reviewed learnable names that ranked below it are appended; every pending
   place name is resolved by the final list (listed: kept; otherwise dropped).

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
