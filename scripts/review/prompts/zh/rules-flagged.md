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
a piece of a cut name (江|宜|桦), drops. **A character or word that is also a surname or given name** keeps when it is also an ordinary word, however
many of the examples are names: 王 (king), 林 (forest), 张 (measure word), 黄 (yellow), 周 (week), 高, 方, 马, 金,
石, 白, 明, 华. Drop only what is a name and nothing else in modern use (刘, 陈, 赵, 吴; given-name characters such as
瑜, 娟). **A real word keeps even when its examples are spam**: judge the word, not the documents (时时 "constantly"
keeps though 时时彩 lottery spam supplies examples).
A word with both a name and a common sense: `keep` when the common sense is
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
cut off (a piece of a name or of a longer word, in all the examples) is `merge:` into that word when the examples make
it clear; otherwise `drop`. A character also used as a word on its own, in literary or formal prose, or as a
measure word, stays.
An over-long lemma is usually a name or a mis-cut: judge it by the name and word rules above.

**Citation** (flag `citation`, the lemma's spelling is almost never written as a word): keep when the lemma is the
release's standard form even though texts write it otherwise (冰激凌 for 冰淇淋, 吗 for 么, a keyed lemma);
`merge:` when it is a broken form of an obvious lemma; otherwise `drop`.

**Proper nouns** (flag `propn_band`: the release tagged the word PROPN; there is no dictionary or case evidence):
apply the name rules above.

**Calls of 2026-11-07 (binding; made under the established rulings):**
1. **Chinese cities**: every prefecture-level city and autonomous prefecture of China keeps (黄石, 惠州, 随州, 平顶山, 阿克苏): the target language's own country, a bounded set a news reader meets. County-level places and below drop unless nationally famous (义乌, 昆山 keep). Districts drop unless nationally famous (海淀, 浦东, 朝阳 as the Beijing district); state-level new areas keep (滨海新区, 浦东新区, 雄安新区). Abroad: well-known cities only.
2. **Suffixed forms** (东莞市, 唐山市, 广东省, 海淀区): the release's one-word cut stands: `keep` when the place keeps, `drop` when it drops.
3. **Companies and brands**: household-name companies and marques a reader meets by name in the news keep (华为, 阿里, 腾讯, 百度, 小米, 京东, 比亚迪, 丰田, 奔驰, 宝马, 宜家, and the major state-owned groups 中石油, 中石化, 中粮, 中铁, 国家电网); car models, product lines, lesser brands and companies drop (凯美瑞, 斯柯达 models; small firms). Major sports leagues keep (中超, 英超, NBA in Chinese 美职篮); clubs drop.
4. **People drop, mythic and literary figures included** (盘古, 孙悟空, 孔子, 毛泽东): the people ruling stands. **Canonical works** a schoolchild learns by name keep as cultural landmarks (三国演义, 红楼梦, 西游记, 水浒传, 论语, 诗经); other titles drop.
5. **Historical titles and offices** are ordinary words (司马 as an office, 太尉, 丞相): `keep` (a surname-only use still drops: see the surname rule).
6. **Fused verb + complement or particle**: a lexicalised verb + complement word the segmenter made keeps (看出, 想起, 涌现出 where it reads as one verb); a transparent verb + 出/到/起 complement, or a verb + aspect particle 着/了/过 or + 于 (流露出, 觉察到, 凝视着, 沉迷于), is the release's mis-cut (the guide splits them): `merge:` the verb.
7. **Variant characters** (异体字: 飚 for 飙): `merge:` the standard Simplified form, as for a Traditional spelling.
8. **Quarter and period words** (一季度, 二季度, 上半年) are words: keep. Number + measure word (三次, 四位) stays a drop.
9. **Genre words** in wide use (修仙, 穿越, 玄幻) keep even when the examples are fiction; generic game names that are common nouns (百家乐 baccarat, 麻将) keep; titles of games drop.
10. **A single character with no examples**: keep when modern Chinese uses it as a word on its own (dictionary standalone use, literary included); drop when it only occurs inside words or names.

11. **Adverb or conjunction + 是**: dictionary words keep (只是, 还是, 就是, 于是, 但是, 正是, 竟是 as the release's cut); 无论是, 不管是 merge into 无论, 不管 (the guide splits them).
12. **Number words**: fractions (三分之一), approximate pairs (三四, 七八), reduplicated 一 + measure (一个个, 一道道) and ordinal + measure (第三节) are spelled numbers or number + measure: `drop`. Number + 大 / 级 words with a meaning of their own keep (四大, 八大, 四级 and 六级 the exams).
13. **Web-fiction words**: genre-internal common nouns that are not names keep (灵石, 丹药, 法宝, 散修); character, sect and place names of fiction drop.
14. **A person's name that became an everyday common term** keeps (雷锋 in 学雷锋); otherwise people drop.
15. **A lemma whose counts include another word** (故 also holding 固): decide by the lemma's own reading; the counts cannot be split here (listed for the lemmatiser).

16. **Newspapers, broadcasters and agencies**: nationally famous ones keep as institutions (人民日报, 新京报, 新华社, 央视); regional papers drop.
17. **Named national products in everyday use** keep (复兴号, 和谐号 trains); call 3's household-name test applies to foreign and Taiwanese brands alike (联想, 华硕 keep; minor marques drop).
18. **Negator + verb** the segmenter fused (未办理, 未完成, 不减) is a mis-cut the guide splits: `merge:` the verb; dictionary words keep (未必, 不必, 没有, 不得不).
19. **Gambling words**: ordinary vocabulary keeps (博彩, 赌场, 彩票); tools, site and game names that only spam makes frequent drop (投注器, 时时彩).

20. **Development zones**: national-level zones keep only when nationally famous (中关村, 苏州工业园区); others drop, as districts.
21. **Surname + 家** (苏家, 李家) is a name: `drop`.
22. **Degree adverb + adjective** the segmenter fused (较厚, 很好, 太大, 更多 where it is degree + adjective) is a mis-cut the guide splits (R13): `merge:` the adjective; dictionary words keep (最近, 最后, 更加, 太太). Other adverb + verb words are the release's cut and keep (先回, 紧追).
23. **Real-word pieces of a split fixed term** (红头 from 红头文件) keep as the words they are.
24. **A mis-cut that holds a whole word** (资金链|断裂 → 链断裂): `merge:` that whole word when it carries the meaning, else `drop`.

25. **Deities and objects of worship** are religious vocabulary and keep (上帝, 真主, 佛祖, 如来, 观音, 耶稣, 玉帝, 关公 as the god, 女娲, 财神爷); people, historical or legendary (炎帝, 黄帝, 尧), drop.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
