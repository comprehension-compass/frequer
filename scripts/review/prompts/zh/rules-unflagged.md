# Review rules (the developer's; binding)

Honeyeater's Mandarin Chinese frequency list (the lemmas a learner studies) is being cleaned. **The list is the
learnable set.** Each lemma below passed every automatic filter, but a screener marked it as possibly junk. You
decide what happens to it. The screener's note is a hint, not a verdict; most of these will turn out to be fine.

**Decisions** (exactly one per lemma): `keep`, `drop` or `merge:<lemma>`, as in the rules below.

**The lemmatiser's conventions stand.** Its word cut, its main spellings (冰激凌, 吗, 地#de) and its keys are
binding: a key after `#` (a pinyin reading key such as 行#xíng, a sense key such as 花#spend, #comp for a
complement, #mw for a measure-word use) makes a word of its own; never merge one keyed lemma into another or into
its bare form. Particles, measure words, localisers, pronouns, complements, interjections and literary function
words are `keep`. Unit headwords (separable verbs such as 睡觉, 成语, constructions with slots such as 要…了) are
the release's own entries and stay. Don't merge a word into another just because a dictionary lists them
together; merge only when the lemma is clearly broken (a cut-off piece of a longer word, a Traditional or variant
spelling of a listed Simplified word, a garbled form).

The rest exactly as in the flagged rules:

**Words are the release's cut.** A multi-character word the segmenter made is a word of the list even when its
meaning is the sum of its parts (户外广告, 风险管理, 水利水电, 不忍心, 动不动): the reader shows it as one word, so
dropping it would leave it ignored. `keep` it unless it is junk on other grounds (a name that drops, template or
spam text, a code). Only a **mis-cut** drops: a string that crosses a word boundary, holding a piece of one word
and part of the next (书目的 = 书目 + 的, 交组织); `merge:` the real word when one plainly carries the counts,
otherwise `drop`. A 成语 or other established fixed expression is one word to learn: `keep` (一帆风顺, 不可思议,
与此同时, 总而言之). Established abbreviations (缩略语) that are ordinary vocabulary stay (高铁, 环保, 空调, 北大,
央视, 新冠); they are words, not abbreviations to expand.

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

**A character or word that is also a surname or given name** keeps when it is also an ordinary word, however
many of the examples are names: 王 (king), 林 (forest), 张 (measure word), 黄 (yellow), 周 (week), 高, 方, 马, 金,
石, 白, 明, 华. Drop only what is a name and nothing else in modern use (刘, 陈, 赵, 吴; given-name characters such as
瑜, 娟). **A real word keeps even when its examples are spam**: judge the word, not the documents (时时 "constantly"
keeps though 时时彩 lottery spam supplies examples).

**Adult and sex-industry words**: keep the ones a learner meets in ordinary reading; drop spam and jargon only
web spam makes frequent. Slurs drop.

**Single characters**: a real standalone word stays (also one used on its own in literary or formal prose, or as a
measure word); a piece of a name or longer word the lemmatiser cut off is `merge:` into that word when the examples
make it clear, otherwise `drop`.

**Calls of 2026-11-07 (binding; made under the established rulings):**
1. **Chinese cities**: every prefecture-level city and autonomous prefecture of China keeps (黄石, 惠州, 随州, 平顶山, 阿克苏): the target language's own country, a bounded set a news reader meets. County-level places and below drop unless nationally famous (义乌, 昆山 keep). Districts drop unless nationally famous (海淀, 浦东, 朝阳 as the Beijing district); state-level new areas keep (滨海新区, 浦东新区, 雄安新区). Abroad: well-known cities only.
2. **Suffixed forms** (东莞市, 唐山市, 广东省, 海淀区): the release's one-word cut stands: `keep` when the place keeps, `drop` when it drops.
3. **Companies and brands**: household-name companies and marques a reader meets by name in the news keep (华为, 阿里, 腾讯, 百度, 小米, 京东, 比亚迪, 丰田, 奔驰, 宝马, 宜家, and the major state-owned groups 中石油, 中石化, 中粮, 中铁, 国家电网); car models, product lines, lesser brands and companies drop (凯美瑞, 斯柯达 models; small firms). Major sports leagues keep (中超, 英超, NBA in Chinese 美职篮); clubs drop.
4. **People drop, mythic and literary figures included** (盘古, 孙悟空, 孔子, 毛泽东): the people ruling stands. **Canonical works** a schoolchild learns by name keep as cultural landmarks (三国演义, 红楼梦, 西游记, 水浒传, 论语, 诗经); other titles drop.
5. **Historical titles and offices** are ordinary words (司马 as an office, 太尉, 丞相): `keep` (a surname-only use still drops: see the surname rule).
6. **Fused verb + complement words** the segmenter made (涌现出, 走出来) keep: the release's cut stands beside its #comp lemmas.
7. **Variant characters** (异体字: 飚 for 飙): `merge:` the standard Simplified form, as for a Traditional spelling.
8. **Quarter and period words** (一季度, 二季度, 上半年) are words: keep. Number + measure word (三次, 四位) stays a drop.
9. **Genre words** in wide use (修仙, 穿越, 玄幻) keep even when the examples are fiction; generic game names that are common nouns (百家乐 baccarat, 麻将) keep; titles of games drop.
10. **A single character with no examples**: keep when modern Chinese uses it as a word on its own (dictionary standalone use, literary included); drop when it only occurs inside words or names.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
