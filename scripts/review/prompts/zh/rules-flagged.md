# Review rules (the developer's; binding)

Honeyeater's Mandarin Chinese frequency list (the lemmas a learner studies, counted from Simplified Chinese web
text and Tatoeba) is being cleaned. **The list is the learnable set: anything on it is learnable by default,
anything not on it is ignored.** Each lemma below was flagged by an automatic heuristic; you decide what happens to
it. The flag says why it was sent; it is evidence, not a verdict.

**How lemmas are written.** The lemmatiser (honeyeater-lemmatiser zh 1.6.4) cuts text into words and gives each
word its lemma in Simplified characters. A key after `#` is part of the lemma's identity and tells two words apart:
a **reading key** in pinyin with tone marks (行#xíng / 行#háng, 觉#jiào / 觉#jué, 了#le / 了#liǎo), a **sense key**
(花#flower / 花#spend), **#comp** for a resultative or directional complement (到#comp, 去#comp, 起来#comp),
**#mw** for a measure-word use (起#mw, 回#mw, 下#mw), and similar short labels (来#since, 地#de). **Each keyed lemma
is a word of its own**: judge it on its own sense; never merge one keyed lemma into another or into its bare form.
A unit headword names a multi-word unit the release found: a separable verb or other compound (睡觉, 帮忙, 见面),
a 成语 or other fixed expression, or a construction or frame with slots (要…了, 对〜来说, 一…就). The release's main
spellings stand (冰激凌, 吗, 地#de).

**Decisions** (exactly one per lemma):
- `keep`: a real Mandarin word, fixed expression or learnable name (below) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong, cut-off or broken lemma, when the right lemma is obvious from the
  examples; give that lemma in Simplified characters as the list writes it (e.g. `merge:警察`). Never merge two
  different words, and never merge a keyed lemma: in that case `keep` (or `drop` if it is junk).

**Grammatical words stay** (`keep`): particles (的, 了#le, 吗, 呢, 吧, 啊, 嘛, 着, 过), measure words and their #mw
senses (个, 张, 条, 本, 位, 只, 次), localisers (上, 里, 中, 以后), pronouns, conjunctions, prepositions, modal verbs,
complements (#comp), interjections and onomatopoeia in ordinary use, and literary function words a reader meets
in news and formal prose (之, 其, 乃, 亦, 于).

**Fixed expressions stay**: a 成语 or other established four-character (or longer) fixed expression is one word to
learn: `keep` (一帆风顺, 不可思议, 与此同时, 总而言之). A string that is not a fixed expression (two ordinary words
the segmenter glued, a slogan, a product line, a site's template phrase) is `drop`. Established abbreviations
(缩略语) that are ordinary vocabulary stay (高铁, 环保, 空调, 北大, 央视, 新冠); they are words, not abbreviations to
expand.

**Names are learnable things** (lemmatiser ruling R12, the developer's: "these are technically names but as they
are things you would want to learn all stay learnable"). `keep`:
- **Places**: countries and territories, continents, oceans and seas; China's provinces, autonomous regions,
  municipalities and SARs (广东, 新疆, 重庆, 香港) and their capitals and other well-known cities; well-known
  cities abroad with Chinese names (纽约, 伦敦, 东京, 首尔); major regions, rivers, lakes, mountains and landmarks a
  reader meets (长江, 黄河, 西藏高原, 珠穆朗玛峰, 长城, 故宫). **Drop** minor places: counties, districts, towns,
  villages, streets, and small foreign places.
- **Holidays, festivals and calendar names** (春节, 端午节, 中秋节, 圣诞节, 清明), and era or dynasty names (唐朝, 明朝).
- **Platforms and products in everyday use** that a reader meets by name (微信, 微博, 淘宝, 支付宝, 抖音, 高德).
- **Famous institutions and organisations**: nationally famous universities, ministries, state bodies, parties,
  broadcasters, and household-name companies talked about as institutions (国务院, 外交部, 北京大学, 清华, 共产党,
  央视, 新华社, 华为); major international bodies (联合国, 欧盟, 世卫组织, 北约).
- **Named diseases and viruses, ethnic groups, planets and constellations, named groups and sets** (新冠, 汉族,
  藏族, 火星, 金星, 二十四节气).
**Other names drop**: people (real, historical or fictional, characters), minor companies, minor brands and products,
websites and apps nobody meets by name, gambling and spam site names, titles of works, games, sports clubs, and
named facilities (stations, buildings, hotels) other than famous landmarks. A one-token surname or given name, or
a piece of a cut name (江|宜|桦), drops. A word with both a name and a common sense: `keep` when the common sense is
in everyday use and shows in the examples (the tagger often calls common words PROPN); `drop` when the counts are
names and the common sense is rare.

**Numbers** (the app's speller writes every figure out: 二〇二五, 三点五, 一千零五): the core number words stay
(零, 〇, 一 to 十, 两, 百, 千, 万, 亿, 半, 几, and 十一 to 三十, which the app's own number check keeps). Any other
spelled number built only from number words drops however frequent (一百, 五十, 两百, 一千, 一万, 二〇二五 and other
digit-by-digit years or codes, 三点五, 百分之五十). Ordinals 第一 to 第三十 stay if the release keeps them as one word;
higher ones drop. Number + measure word or unit glued together (三个, 五年) drops unless it is a word in its own right
(一些, 一下, 一起, 一定, 一样, 万一, 百分之 are words).

**Latin script, codes and junk**: a lemma or unit headword holding Latin letters, digits or codes, broken
characters, or a Traditional-script spelling of a word the list holds in Simplified (`merge:` the Simplified
lemma when it is obvious, else `drop`).

**Adult and sex-industry words**: keep the ones a learner meets in ordinary reading; drop spam and jargon only
web spam makes frequent. Slurs drop.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template, shop, spam, gambling, SEO and
fan-fiction text (product and drug brand names, character names, site boilerplate); keep real words even when the
examples are spammy.

**Shape** (flag `shape`; a single character the wider language rarely writes alone, or an over-long lemma): a single
character that is a real standalone word stays (猫, 桶, 嗯, 啦). One that is a piece of a longer word the lemmatiser
cut off is `merge:` into that word when the examples make it clear; otherwise `drop` (a lone bound morpheme drops).
An over-long lemma is usually a glued phrase or name: `drop` unless it is a fixed expression.

**Citation** (flag `citation`, the lemma's spelling is almost never written as a word): keep when the lemma is the
release's standard form even though texts write it otherwise (冰激凌 for 冰淇淋, 吗 for 么, a keyed lemma);
`merge:` when it is a broken form of an obvious lemma; otherwise `drop`.

**Proper nouns** (flag `propn_band`: the release tagged the word PROPN; there is no dictionary or case evidence):
apply the name rules above.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
