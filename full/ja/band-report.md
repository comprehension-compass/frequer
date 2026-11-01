# ja junk review: per-band report (no snapshot built)

Bands are positions in the cleaned list (the kept count), so a band holds what the developer would cut at.
Actions: `keep` (no flag), `review-keep`, `pending-names` (place names awaiting the learnable-names list), `review-drop`, `propn-drop` (every Sudachi entry a person/organisation name). Merged lemmas leave the ranking (their counts join the target).

| band | entries | keep (no flag) | review-keep | pending-names | review-drop | dictionary name drop | merged | kept share | real lemmas among reviewed (keep + merge) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0-10k | 10,177 | 9,561 | 190 | 249 | 119 | 58 | 3 | 98.3% | 61.9% of 312 |
| 10-20k | 10,663 | 9,086 | 467 | 447 | 487 | 176 | 14 | 93.8% | 49.7% of 968 |
| 20-25k | 5,531 | 4,396 | 316 | 288 | 381 | 150 | 12 | 90.4% | 46.3% of 709 |
| 25-30k | 5,691 | 4,353 | 332 | 315 | 501 | 190 | 14 | 87.9% | 40.9% of 847 |

## Estimated real-lemma share of the kept list (audit)

100 random unflagged keeps per band went through the same two-reviewer protocol (not applied, an estimate).
Unflagged keeps judged real (keep or merge): 0-10k 97 %, 10-20k 98 %, 20-25k 91 %, 25-30k 89 %. Each band
of kept places then splits roughly into:

| kept band | kept places | real lemmas (est.) | place names pending | estimated junk left | of which spelled numbers |
|---|---:|---:|---:|---:|---:|
| 0-10k | 10,000 | ~94.6 % | 2.5 % | ~2.9 % | 197 |
| 10-20k | 10,000 | ~93.7 % | 4.5 % | ~1.8 % | 201 |
| 20-25k | 5,000 | ~86.3 % | 5.8 % | ~7.9 % | 125 |
| 25-30k | 5,000 | ~84.1 % | 6.3 % | ~9.6 % | 125 |

What the audit's drops were: spelled numbers (千九百九十八, 四百六十, 八百二点一一: the number speller's output,
648 of them in the top 30k, unflagged), clipped katakana (スポ, キャ, ノシ), names the dictionary lacks (初音,
テイル) and lone characters (交, 勤). Among the flagged lemmas reviewed, the real-lemma share falls from 62 %
(0-10k) to 41 % (25-30k): the rules catch proportionally more junk deeper down. Taken together, 25-30k still
holds about 4,200 real lemmas in its 5,000 places (plus ~300 place names for the learnable-names list).

## Rule hits per band

| band | diversity | citation | shape | propn_band |
|---|---:|---:|---:|---:|
| 0-10k | 45 | 3 | 9 | 269 |
| 10-20k | 60 | 2 | 77 | 857 |
| 20-25k | 34 | 1 | 83 | 612 |
| 25-30k | 28 | 4 | 94 | 744 |

## 30 keeps around 25,000

| list position | lemma | action | POS | frequency |
|---:|---|---|---|---:|
| 24,857 | 無造作 | keep | ADJ | 1,056 |
| 24,865 | とくとく | keep | NOUN | 1,055 |
| 24,868 | モスバーガー | keep | NOUN | 1,055 |
| 24,871 | 一様 | keep | NOUN | 1,055 |
| 24,880 | 中之島 | pending-names | PROPN | 1,054 |
| 24,882 | 抜き出す | keep | VERB | 1,054 |
| 24,896 | 点滅する | keep | VERB | 1,053 |
| 24,898 | 買得 | keep | NOUN | 1,053 |
| 24,922 | 免税 | keep | NOUN | 1,050 |
| 24,930 | 頭身 | keep | NOUN | 1,050 |
| 24,944 | バイオレット | review-keep | PROPN | 1,048 |
| 24,945 | 使い手 | keep | NOUN | 1,048 |
| 24,947 | 坊や | keep | NOUN | 1,048 |
| 24,950 | 懐く | keep | VERB | 1,048 |
| 24,973 | 委任状 | keep | NOUN | 1,046 |
| 25,005 | 呂 | keep | NOUN | 1,044 |
| 25,017 | 事故後 | keep | NOUN | 1,043 |
| 25,052 | 見せ付ける | keep | VERB | 1,041 |
| 25,075 | ヤナギ | keep | NOUN | 1,039 |
| 25,078 | 密封 | keep | NOUN | 1,039 |
| 25,081 | こびりつく | keep | VERB | 1,038 |
| 25,087 | 信徒 | keep | NOUN | 1,038 |
| 25,088 | 加点 | keep | NOUN | 1,038 |
| 25,093 | 日没 | keep | NOUN | 1,038 |
| 25,110 | 八雲 | keep | NOUN | 1,036 |
| 25,112 | 大成 | keep | NOUN | 1,036 |
| 25,120 | ゆくゆく | keep | NOUN | 1,035 |
| 25,125 | 乗り継ぐ | keep | VERB | 1,035 |
| 25,136 | アラスカ | pending-names | PROPN | 1,034 |
| 25,150 | 供 | keep | NOUN | 1,033 |

## 30 keeps around 30,000

| list position | lemma | action | POS | frequency |
|---:|---|---|---|---:|
| 29,850 | 講評 | keep | NOUN | 759 |
| 29,851 | 連邦軍 | keep | NOUN | 759 |
| 29,852 | 風鈴 | keep | NOUN | 759 |
| 29,857 | 三橋 | pending-names | PROPN | 758 |
| 29,867 | 職員室 | keep | NOUN | 758 |
| 29,871 | ほどく | keep | VERB | 757 |
| 29,877 | ビル内 | keep | NOUN | 757 |
| 29,908 | 小野田 | pending-names | PROPN | 756 |
| 29,909 | 忠臣 | keep | VERB | 756 |
| 29,915 | 自傷 | keep | NOUN | 756 |
| 29,921 | ハイレグ | keep | NOUN | 755 |
| 29,923 | ブリュッセル | keep | PROPN | 755 |
| 29,924 | ベースライン | keep | NOUN | 755 |
| 29,925 | 一理 | keep | NOUN | 755 |
| 29,930 | 執務 | keep | NOUN | 755 |
| 29,937 | 骨組み | keep | NOUN | 755 |
| 29,948 | 本大会 | keep | NOUN | 754 |
| 29,952 | 販売所 | keep | NOUN | 754 |
| 29,954 | 銅メダル | keep | NOUN | 754 |
| 29,958 | スクーリング | keep | NOUN | 753 |
| 29,967 | 律儀 | keep | NOUN | 753 |
| 29,972 | 装用 | keep | NOUN | 753 |
| 29,977 | 骨太 | keep | NOUN | 753 |
| 29,980 | ダンシング | review-keep | PROPN | 752 |
| 29,981 | チューリッヒ | keep | PROPN | 752 |
| 29,982 | フォルテ | review-keep | PROPN | 752 |
| 29,983 | 三毛 | keep | NUM | 752 |
| 29,991 | 薄力粉 | keep | NOUN | 752 |
| 29,995 | カスタードクリーム | keep | NOUN | 751 |
| 30,000 | 備え付ける | keep | VERB | 751 |

## 50 random drops

| rank | lemma | how | flags | reviewers' reason |
|---:|---|---|---|---|
| 2,500 | レンタ | propn-drop | diversity: in 926 documents, 0.03 of the 27,153 occurrences' random spread (thre |  |
| 5,938 | 東急 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | railway/company brand name |
| 6,132 | 西武 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | railway/department-store brand name |
| 7,010 | マリオ | propn-drop |  |  |
| 7,680 | 金剛 | review-drop | diversity: in 887 documents, 0.13 of the 6,701 occurrences' random spread (thres | examples only show proper-noun uses (ship, temple); no common "vajra/diamond" se |
| 10,067 | マリー | review-drop | propn_band: tagged PROPN; dictionary has proper and common entries (common/perso | all examples are the person name Marie (Antoinette)/unrelated substring match |
| 11,052 | 工藤 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | surname |
| 11,916 | ファミコン | review-drop | propn_band: tagged PROPN; the dictionary has only common entries | specific product name (Nintendo Famicom), not genericised |
| 13,057 | みさ | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person given name |
| 13,998 | 四位 | propn-drop |  |  |
| 14,815 | セガ | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | company brand name (Sega) |
| 14,852 | オリコン | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | company/brand name (Oricon) |
| 15,739 | フィリップ | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person name (Philip) |
| 15,840 | 文部科学省 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | specific government ministry, treated as organisation name |
| 16,572 | ランカ | review-drop | diversity: in 159 documents, 0.07 of the 2,203 occurrences' random spread (thres | character name (Macross Frontier's Ranka), fan-content concentration matches div |
| 16,820 | 松村 | propn-drop |  |  |
| 17,585 | バッハ | propn-drop |  |  |
| 19,345 | ライアン | propn-drop |  |  |
| 19,826 | 相葉 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person surname (celebrity Aiba) |
| 19,850 | 新日本 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | refers to named org/show/ranking (New Japan Pro-Wrestling etc.), not common word |
| 20,004 | テリー | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person given name (foreign) |
| 20,512 | ゴードン | propn-drop |  |  |
| 21,147 | オスカー | propn-drop |  |  |
| 21,225 | 翔子 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | only a person name |
| 21,342 | 閣 | review-drop | shape: length 1 | no examples found; appears only as part of compounds like 内閣/天守閣 |
| 21,352 | シリウス | review-drop | propn_band: dictionary: every entry a name (person/proper), but not tagged PROPN | used only as product/magazine/building names in examples, not an everyday common |
| 22,757 | 公明 | review-drop | propn_band: tagged PROPN; dictionary has proper and common entries (common/perso | examples show only party/person-name uses, no everyday "fairness" sense shown |
| 23,259 | 経団連 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | business federation organisation name |
| 23,794 | ジル | propn-drop |  |  |
| 24,875 | 防衛省 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | organisation (government ministry) name |
| 25,212 | 北原 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | surname, no common sense |
| 25,454 | 悠斗 | review-drop | diversity: in 77 documents, 0.07 of the 1,107 occurrences' random spread (thresh | person given name |
| 26,227 | タカラトミー | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | company name |
| 26,298 | コクヨ | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | company name (Kokuyo) |
| 26,447 | 涼介 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person name, no common-word sense |
| 27,847 | クリストファー | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person given name, no common sense |
| 28,188 | JR東海 | review-drop | propn_band: tagged PROPN; the dictionary lacks it | railway company name |
| 28,259 | 良子 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person given name, no common sense |
| 28,552 | ベ | review-drop | shape: length 1 | bare single syllable with no examples; not a standalone word, no clear merge tar |
| 28,574 | 希志 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | AV performer's stage name, spam-style listings |
| 28,639 | 久美 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | given name, no common sense |
| 29,099 | 壮 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | given name character, no common sense |
| 29,457 | ねね | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person/character name only |
| 29,469 | 吊 | review-drop | shape: length 1 | bound verb stem (吊る/吊り), no examples |
| 29,489 | ディック | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person name only, no common sense shown |
| 30,086 | 古畑 | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person surname (drama title) |
| 30,248 | マートン | review-drop | diversity: in 151 documents, 0.18 of the 831 occurrences' random spread (thresho | person surname (baseball player) |
| 30,804 | 光文 | review-drop | propn_band: dictionary: proper noun, not a person or place (proper) | clipped from publisher name 光文社 (company) |
| 30,992 | インペリアル | review-drop | propn_band: tagged PROPN; dictionary has proper and common entries (common/perso | used only as part of other proper names (hotel, gem variety, club), no standalon |
| 31,470 | オスマン | review-drop | propn_band: dictionary: every entry a name (person), but not tagged PROPN | person name (Osman); not a place lemma itself |

## Merges (44)

| lemma | into | reason | decided |
|---|---|---|---|
| おっ | おっさん | examples all show the clipped piece of おっさん, not the standalone interjection | agreed (round1) |
| おとく | お得 | kana spelling of the ordinary word お得, which is the dictionary form | adjudicated (round4) |
| しゅうとめ | 姑 | word is overwhelmingly written with the kanji 姑; lemma should be that form | agreed (round1) |
| ずきん | 頭巾 | kana fragment of 頭巾; all uses are bound (赤ずきん), so file under the standard spell | adjudicated (round2) |
| であいけい | 出会い系 | kana spelling of the real word 出会い系, spammy dating-site context | agreed (round1) |
| どう喝 | 恫喝 | kana variant spelling of 恫喝 (intimidation); standard form dominates | agreed (round1) |
| まーん | ます | citation artefact of elongated auxiliary ます (しまーす) | adjudicated (round1) |
| らーめん | ラーメン | kana spelling of the common word whose standard form is katakana | adjudicated (round1) |
| り様 | 様 | broken/clipped lemma, always written as 様 | agreed (round1) |
| アフォ | アホ | netspeak variant spelling of アホ, same word, canonical lemma obvious | adjudicated (round4) |
| アルティ | アルティメット | clipped form of アルティメット | agreed (round1) |
| イイネ | いいね | Katakana-emphasis spelling of the ordinary いいね expression | adjudicated (round1) |
| エイプリル | エイプリルフール | all examples are the clipped compound "April Fool's", not standalone "April" | agreed (round1) |
| オバ | おばさん | katakana clip of おばさん shown in the example; オバ alone is not a word | adjudicated (round1) |
| カッターシャツ | カッター | examples all use カッター to mean a cutting tool/knife, not カッターシャツ (dress shirt); b | agreed (round1) |
| カンジ | 感じ | katakana spelling of 感じ ("feeling/vibe"), as shown in all examples | agreed (round4) |
| コキ | 手コキ | bound element; dominant compound 手コキ is the real (vulgar) word, name tag is wron | adjudicated (round4) |
| シーザー | シーザーサラダ | counts are the food compound, not the person; シーザーサラダ is the obvious lemma | adjudicated (round4) |
| ジャケ | ジャケット | clipped slang for album/clothing jacket, as in the example | agreed (round1) |
| スカッ | スカッと | onomatopoeic stem of スカッと, mistagged PROPN from product-name examples | agreed (round1) |
| チャイナドレス | チャイナ | all occurrences actually written as clipped チャイナ, not as チャイナドレス, used generical | agreed (round1) |
| ツッコミー | ツッコミ | spelling never actually used; real word is ツッコミ | agreed (round1) |
| ナマ | 生 | kana spelling of the common word 生 ("raw/live") | agreed (round1) |
| バサミ | ハサミ | rendaku form only in compounds; merge into the usual modern spelling of the word | adjudicated (round2) |
| パーキンソン | パーキンソン病 | every example is the disease compound; the full term is the learnable lemma | adjudicated (round4) |
| ボリンジャー | ボリンジャーバンド | clipped form of the financial term "ボリンジャーバンド" | agreed (round4) |
| メーリング | メーリングリスト | clipped from メーリングリスト in all examples | agreed (round1) |
| ヤル気 | やる気 | emphatic katakana spelling of common word やる気 | agreed (round1) |
| レバ | レバー | clipped form of レバー used in compounds like レバ刺し | agreed (round4) |
| レフカメラ | 一眼レフカメラ | all examples are 一眼レフカメラ; レフカメラ is a clipped fragment of that compound | agreed (round1) |
| ローヤル | ローヤルゼリー | always appears as part of ローヤルゼリー in examples | agreed (round1) |
| 労務士 | 社会保険労務士 | always occurs as part of clipped 社会保険労務士 | agreed (round1) |
| 四苦 | 四苦八苦 | all examples are 四苦八苦; the Buddhist term alone is not evidenced | adjudicated (round1) |
| 天真 | 天真爛漫 | all examples are the idiom 天真爛漫; lemma is a split-off piece | adjudicated (round1) |
| 契 | 契約 | examples show it cut off from 契約 (contract) | agreed (round2) |
| 姐 | 姐さん | single character appearing only as part of 姐さん in the examples | adjudicated (round1) |
| 心療 | 心療内科 | always appears as part of 心療内科/心療科, a clinical specialty compound; no standalone | agreed (round1) |
| 憧 | 憧れる | shape: single character is a clipped piece of 憧れる (憧憬), not standalone | agreed (round3) |
| 懐っこい | 人懐っこい | clipped inflected forms of 人懐っこい, mostly appearing with 人 | agreed (round1) |
| 支 | 支持 | only example is a truncated 改革を支持, the obvious target | adjudicated (round1) |
| 正真 | 正真正銘 | examples show it only as part of 正真正銘; the 正真性 use is marginal | adjudicated (round1) |
| 氣 | 気 | old-style kanji variant of 気 | agreed (round1) |
| 耳鼻 | 耳鼻咽喉科 | bound element clipped from 耳鼻咽喉科 in every example | adjudicated (round1) |
| 萬 | 万 | old-style kanji variant of 万 "ten thousand", seen in "20萬" | agreed (round1) |

## Questions (259 lemmas; first question per lemma)

# question あき: no examples found, so the common vacancy/autumn sense couldn't be confirmed against the name sense
# question あま: no example given; ambiguous whether this instance is 尼, 海女, or something else, so common-sense use can't be confirmed from the data provided.
# question あや: no example sentence provided; unclear if this lemma is ever used as a common word rather than the given name
# question さくら: common "cherry blossom" sense is well known in Japanese but none of the sampled examples show it in plain common use, only proper-noun uses
# question ちゃんねる: could be judged diversity/brand (named forums) rather than citation of チャンネル
# question てっ: no example found at all, so its intended meaning/lemma is unknown
# question はやぶさ: dictionary has only common entries (falcon), but all sampled uses are the Shinkansen/probe names; routed to pending-names rather than drop so the names list can settle it.
# question まーん: the intended target word for this broken elongated form is inferred (ます) but not shown directly in examples
# question ゆる: unclear what word the varied forms (ゆる/ゆん/ゆり/ゆれ/ゆら) actually represent; no examples to confirm
# question ゎ: whether stylised kana variants should be merged to their base kana (は in most of these examples) instead of dropped
# question アイ: ambiguous between loanword "eye" and the given name "Ai"; only example found is a title reference
# question アクア: could plausibly be a common loan prefix (aqua-) in product naming rather than a standalone word; unclear if a standalone common sense exists beyond name/product fragments
# question アッ: no examples given; decision assumes it's the common interjection あっ/アッ rather than a cut fragment
# question アッシュ: unclear whether the common hair/color sense is frequent enough given the sample skews toward the Banana Fish character name
# question アバン: frequency mostly looks like the Dragon Quest character アバン先生, but one example shows the common anime-production term for the pre-title "cold open"; unclear which sense dominates the count
# question アル: no examples given; dictionary entries suggest person/proper noun, but can't verify whether it's a common word, name, or clipped form
# question アルス: unclear what common (non-name) sense the dictionary registers; only example is a building name
# question アン: no examples available to confirm whether any common sense (vs. the name Ann/Anne) is in everyday use
# question イ: no example given; meaning (kana ordering symbol vs. something else) is unclear from the data provided
# question イイネ: merge target いいね is a phrase (adjective + particle), so it may not exist as a lemma on the list; if it does not, keep イイネ as the attested spelling.
# question イオ: no examples given; unclear whether this is a name, a common word, or a clipped loanword (e.g. イオン)
# question イカセ: unclear whether this slang causative form should merge into a verb lemma (e.g. 行かせる/イカせる) or be dropped as spam-only slang
# question イズ: no example given; unclear what word or fragment this represents
# question インフォ: unclear whether it has any standalone use beyond being a prefix in brand names
# question イー: no clear examples; could be an interjection/sound-stretch rather than an established word
# question ウィンド: unclear whether any genuine standalone common use exists beyond brand/compound fragments
# question ウェスト: examples shown are all proper-noun uses (West Side, Westport, etc.); no example shows the common "waist" sense even though that sense is everyday vocabulary—unclear if the counted frequency actually reflects common usage.
# question エス: no example given to confirm which common sense (if any) is actually attested
# question エステル: no example shows the chemistry sense; kept on dictionary grounds, but counts may be character names.
# question オ: no examples given; likely a fragment of a longer name but the target word is unclear
# question オナ: no examples given to confirm whether it's used as an independent word rather than only as a prefix (オナニー/オナ禁/etc.)
# question カミ: no example sentences given, so can't confirm whether usage is the common sense (god/paper/hair stylized in katakana) or a name
# question ガーディアン: katakana loan "guardian" has a plausible common sense but no example clearly shows it in use
# question クレ: no example text given; unclear whether this is a specific brand/product or something else, decision made on thin evidence
# question クロ: no examples given; unclear whether usage is mostly as common word for "black" or as a name/character, decided keep on the strength of the established common sense
# question クー: no examples given; unclear whether this is a genuine interjection/word or noise from an elongated sound
# question グ: no example sentences; unclear which longer word (if any) it is clipped from
# question ケイ: no example text; unclear whether any common sense (e.g. a letter/unit reading) is actually in use
# question ゲ: no examples given, so true usage (fragment vs standalone) can't be verified
# question サ: no example provided and no clear standalone meaning in general Japanese; can't confirm if this is a real word (e.g. sauna slang) or junk
# question サン: no example sentences given, so the actual intended sense (loan "sun"-prefix vs. honorific vs. name "Son") can't be confirmed from evidence.
# question シナ: no example text given; unclear whether this instance is the old place name for China or a common-noun sense (e.g. しな "quality/goods")
# question シー: no example shows a clear generic word sense; unclear if this represents "sea", a letter "C", or just fragments of names
# question ジョーダン: one example suggests a pun on 冗談 ("joke") but most examples are brand/name uses of "Jordan"; unclear which sense is intended for the list
# question スタン: no example text; decision rests on inference from romanized spelling variants "stun"/"Stun"
# question ステ: no examples found; unclear what common word (ステータス? 捨て?) it clips, if any
# question セ: no example given, can't tell what word this fragment represents
# question セブンス: dictionary flag suggests common word, but all examples are franchise/product titles; unclear how often it's used generically (e.g. music "seventh")
# question ダ: no example sentence is given, so it's unclear whether this has any standalone common-word use
# question ダイア: the single example is a clipped title, but ダイア is independently an established loan; kept rather than merged.
# question ダイナ: no examples found; unclear referent (Toyota Dyna truck, a name Dyna, etc.)
# question チャ: no example sentence is given, so it's unclear whether this is a real common word (e.g. clipped 茶) or purely a name fragment
# question チャイナドレス: all occurrences written only as チャイナ in unrelated compounds, not the lemma's own spelling; unclear if チャイナ itself should land on pending-names or stay common
# question チャップ: only one sample example, seemingly a fragment of ポークチャップ/ポークチョップ; unclear if this is junk or should merge to チョップ
# question チャー: no examples at all; unclear whether it's a real word, an onomatopoeia, or a clipped brand/name fragment
# question デ: no example text was given; can't confirm if it's ever a real standalone word or identify a merge target
# question ディティール: unclear if this is an established alternate spelling of ディテール worth keeping separately, or should be merged into it
# question トゥ: polysemous between a real technical loanword (toe) and a meaningless fragment of a foreign phrase (オデ・トゥ・ザ・デイ); decided based on the first example
# question トメ: no examples given; unclear whether this is a personal name or the colloquial "mother-in-law" slang sense
# question トロイ	: the katakana spelling covers both トロイの木馬 (place-derived) and とろい; kept as the katakana lemma rather than merging, since merging to とろい would lose the dominant トロイ spelling.
# question トロン: dictionary lists both proper and common senses, but the sole example ("青トロン") doesn't clarify whether a common meaning is actually in everyday use here.
# question ナミ: no example text given; can't tell if it's a character name or a common/clipped word
# question ナン: no example sentences given, so can't confirm whether occurrences are the loanword "naan" versus some other reading/use.
# question ニ: no examples found; unclear whether it's a numeral/musical-note fragment or something else
# question ノーベル賞 / パラリンピック: these named-award/event terms aren't explicitly covered by the listed proper-noun drop categories, so keep was chosen by analogy to vocabulary learners need
# question ノーベル賞: award name tied to a specific foundation isn't explicitly covered by the organisation/brand/title list; judged as a specific named entity like a company, so dropped
# question ハイドロ: dictionary flag suggests common word, but examples don't clearly show it used as an independent noun rather than a compound prefix
# question バリ: no examples given; unclear whether occurrences are mostly the place name Bali, the common noun "burr", or Kansai slang "very"
# question ヒル: no example sentence given, can't confirm the common "leech" sense actually shows in the corpus rather than the person-name sense
# question ピ: no example text was available; could not determine if it's junk or part of a cut-off word
# question ブラン: no examples given; dictionary entries suggest person/proper noun, but can't verify sense or whether it's a clipped loanword (e.g. "bran")
# question ブロ: no example text given; can't tell what common or clipped word it might be
# question プー: no example text; unclear whether usage is the Pooh character/other name or an onomatopoeic interjection (elongated variants suggest the latter)
# question ホン: no example sentence is given, so it's unclear whether this represents a common word (e.g. phon, book counter) or only names
# question ホープ: "hope" is a real loanword sense but all sampled examples are brand/company names
# question ボン: no examples found; unclear whether it's mainly a name (e.g. Bonn) or the common onomatopoeic/colloquial word
# question ボーイング: could arguably be treated like a genericised brand for "a Boeing aircraft"; unclear if that counts as ordinary generic use
# question マグナ: unclear what the dictionary's common sense of マグナ is; examples only show brand/product usage
# question マスターズ: unclear whether this counts as a generic sports-category word or should be treated like a tournament/brand name
# question メイ: no examples given, so it's unclear whether any occurrences are the common noun use rather than the name
# question メリー: mixed evidence between brand/media name (MERY) and genericised baby-mobile term; kept on the generic sense
# question メル: no example sentences available to confirm what メル actually means/how it's used
# question モス: no examples given; unclear whether usage is common noun (moss) or MOS Burger brand
# question モバ: no example text was available; likely a clip of モバイル but no evidence to confirm merge target
# question モモ: no example given; could be common "peach" or a character/person name, can't verify from evidence
# question ヤクルト: examples only show the baseball team sense; kept assuming the genericized drink-name sense is still in everyday use but this isn't confirmed by the sample
# question ヤン: no example given; unclear if it has any common use beyond being a surname/character name
# question ユダヤ: ethnonym/historic region name, unclear whether it should fall under pending-names like a place or stay as a common word
# question ヨーク: no examples found; unclear whether counts reflect the place name, the dress/egg term, or something else
# question ライ: no examples given and the word is highly ambiguous (rye? an old disease name? a nickname?); unclear which sense, if any, belongs on a learner's list.
# question ライツ: shown mostly inside compounds and proper nouns (ライツ・オファリング, スーパークロス・ライツ); unclear if bare ライツ has independent common use
# question ラス: no example given; assuming common slang sense ("last place") rather than a name, but this is unverified
# question ランカ: no examples given; unclear if this is a place name, character name, or something learnable
# question リブログ: whether a genuine but niche internet loanword occurring almost entirely in site boilerplate counts as learnable
# question ル: no example text was given; can't confirm if it's ever a real standalone word or identify a merge target
# question レイ: no examples available to tell whether a common sense (e.g. "lei", "zero") is in everyday use versus the name Rei/Ray
# question ワンダー: dictionary shows only common entries but no example shows genuine standalone "wonder" usage outside names
# question 与: no examples given; decided keep based on known political-jargon abbreviation (与党), but usage in this corpus is unconfirmed
# question 中山: could be the common place name Nakayama rather than only the surname; no place example in sample
# question 中日: unclear whether the common Japan-China relation/middle-day sense is frequent enough to outweigh the proper-noun-dominated examples
# question 伊吹: examples mix a place (伊吹島) with character/person names (伊吹萃香, 伊吹隊長); unclear whether the common/learnable sense is the mountain/place or just names
# question 信: no examples found; unclear whether counts are the common word "trust" or the personal name "Shin"
# question 儀: no examples provided; unclear whether 儀 is ever used as a standalone word versus always bound into compounds like 儀式
# question 元禄: era names (元号) aren't explicitly covered by the proper-noun categories; treated as keepable general vocabulary
# question 八幡: examples split between place name (Yawata) and Shinto deity/shrine name; unclear which sense should govern the decision
# question 凌: unclear whether it's a clipped piece of 凌ぐ; no example text to confirm
# question 凛: no example given; relies on outside knowledge that 凛 has a real adjectival-noun common sense (凛とした) beyond the given name
# question 労働省: unclear whether a specific (defunct) ministry name counts as a dropped "organisation" or as learnable institutional vocabulary
# question 北海: no clear examples; unclear whether occurrences are the common noun "north sea" or a place-name usage (e.g. clipped 北海道 or a Chinese city name)
# question 博: no examples given; unclear if common sense (学/博覧会) or personal name dominates
# question 厚生労働省: unclear whether a major government ministry name should be dropped like a company/organisation or kept as basic civic vocabulary
# question 古泉: unclear whether "三古泉" reflects a real lexical compound or is just incidental juxtaposition of 古+泉
# question 吐露: examples mostly show とろ meaning "melty/creamy" (food texture), unrelated to 吐露's meaning "confession"; unclear if these are a true homophone collision or mislemmatization
# question 吸: no examples given; unclear which longer word (吸う, 吸収, etc.) it was clipped from
# question 味の素: unclear whether 味の素 counts as a genericised brand name for MSG/seasoning or should be treated as a trademark to drop
# question 呼: no examples given; unclear which longer word (呼ぶ, 呼吸, etc.) it was clipped from
# question 営: no examples found; can't tell which longer word (経営, 営業, 運営...) it was cut from
# question 壇: no examples given; unclear how often 壇 is actually used standalone versus only in compounds like 祭壇/演壇
# question 大島: dictionary lists place and person senses, but all sampled examples are person surname uses; unclear if a genuine standalone place use exists
# question 大橋: mixed person/place senses; sampled examples are person surname and a place-compound (池尻大橋), unclear if bare 大橋 is ever used as an ordinary place reference
# question 妖: no examples given; unclear if 妖 is used as a standalone word (vs. part of 妖怪/妖精)
# question 容: no examples given; unclear whether any standalone sense of 容 is common enough to keep
# question 寛永: era name (元号); rules don't specify whether era names should be treated like other proper names (drop) or ordinary vocabulary
# question 小・中学: always seen followed by 校 or 生 in examples; unclear if it is a genuine standalone lexical item or a cut piece of 小・中学校/小・中学生
# question 小倉: similarly mixed person/place dictionary senses; sampled examples lean person/cultural-title, unclear if standalone place use is common enough for pending-names
# question 山口: ambiguous between a notable place name (Yamaguchi) and a very common surname; examples lean surname but place sense is well known
# question 山手: examples mix person name, building name, and possible common "hilly area" sense; unclear which dominates
# question 山村: common noun "mountain village" sense exists but not shown in any example, all examples are surname/company uses
# question 岡: no example text; unclear whether the standalone "hill" sense is ever used versus only as surname/place component
# question 峡: unclear whether 峡 alone (gorge/strait) is used independently enough to keep, or only as a place-name suffix
# question 島田: evidence mixes a possible place (Shimada city/club) with clear personal surnames; decided drop based on examples skewing personal, but could be pending-names.
# question 川口: majority examples are a surname, but 川口 is also a well-known place (Saitama); unclear which sense dominates
# question 巴: dictionary lists common/person/place senses but examples only show company names; unclear if common "tomoe" sense is in everyday use
# question 平成	era name isn't a place/person/company/product/etc.; unclear which bucket of the proper-noun rules it falls under
# question 幼: no example text was available to judge standalone use versus a clipped piece of 幼い/幼児
# question 弊: no example text; unclear if it's ever a real standalone word or only a bound/cut-off piece (e.g. 弊社)
# question 張: no examples given, so it's unclear whether any occurrences are a common-word sense rather than the surname
# question 徒: written forms suggest it's a cut piece of several different compounds (教徒, 使徒, etc.); no single obvious merge target
# question 心療: whether 心療内科 or another compound is the "obvious" merge target, since several 心療-compounds appear
# question 応: no examples found; unclear if it should merge into a specific compound (e.g. 対応, 応じる)
# question 思: no examples found; readings suggest personal names, but dictionary also lists a common sense, so it's unclear if it should be kept as a common word
# question 恵: no examples given; unclear whether personal name "Megumi" or common noun "blessing/grace" dominates
# question 憂: unclear if there is any genuine common-noun usage beyond being a person's name in this sample
# question 排: single kanji with no examples; likely a fragment of a longer word (排除/排水) but no examples to confirm which
# question 接: no examples found; can't tell which longer word (接続, 接触, 直接...) it was cut from
# question 援: no examples given; likely a fragment of 援助/応援/支援 but no evidence to confirm a merge target
# question 支: single example is a truncated sentence ("...改革を支..."); unclear which word it was cut off from
# question 敏: no examples found aside from reading count; unclear if standalone adjective use exists or it's purely a name/compound fragment
# question 散: no examples found; unclear if it should merge into a specific compound (e.g. 散歩, 散る)
# question 斎: no examples given; unclear whether it's used as a standalone word or only as a name/clipped form
# question 新田: could instead be mainly a surname rather than a place name; examples mix both
# question 旭: dictionary lists common/person/place senses but examples only show company-name (旭化成) and personal given-name use, not clearly place or common noun — unclear which sense dominates.
# question 昇: no examples given; unclear whether it is a cut-off piece of 上昇/昇る or mainly a name (しょう/のぼる), so merge target is not obvious
# question 明: no example given; unclear whether any common standalone sense (vs. personal-name reading) is actually attested in the corpus
# question 明星: "shining star/celebrity" sense exists but no example shows it; all samples are brand/product names
# question 明智: person name dominates examples but place sense (明智町) also exists in the dictionary; unclear which to prefer
# question 昨: no examples found; unclear whether it should merge into 昨日/昨年/昨夜 or just be dropped as a bound prefix
# question 昭: single kanji with no examples; could be a cut-off piece of 昭和/a name, but evidence insufficient to pick a merge target
# question 朴: counts are high and could include the common tree-name sense (朴の木) not shown in the sampled examples
# question 東大: unclear whether a famous university name should be treated as a named-facility/organisation (drop) or kept as very common everyday vocabulary
# question 東邦: unclear if the classical "Eastern countries" sense is common enough among learners to count as everyday use
# question 東都: functions both as a classical place-name for Tokyo and as part of organisation names (東都リーグ, 東都不動産); treated as place reference
# question 柏: ambiguous between the city name Kashiwa and the common noun "oak"; examples only show place-derived uses
# question 柔: no examples; unclear whether 柔 is used standalone (as in classical idiom) or only as a bound morpheme (柔道, 柔らかい)
# question 楽天: examples are all company/service usage; unclear whether the "optimism" common sense is frequent enough in everyday Japanese to count as "shows in the examples"
# question 標: no examples; unclear whether 標 is ever written alone as a standalone word in modern usage or is always bound in compounds
# question 正真: one example uses 正真性 as a standalone technical term (data integrity/authenticity) distinct from 正真正銘; unclear if this sense is common enough to keep separately
# question 江: no example given, can't confirm whether the common "inlet" sense is in everyday use
# question 決: no examples given; readings (決/けつ) suggest possible clipped form (e.g. 決勝) but no evidence to confirm a merge target
# question 泣: unclear whether the "(泣)" emoticon usage should be treated as its own interjection or merged into 泣く
# question 浅: no example sentences; unclear if it is ever used as a standalone word rather than an adjective stem/name fragment
# question 淫: unclear which single compound (淫語, 淫乱, 淫行...) the cut lemma should merge into
# question 混: cut-off suffix seen in fabric-blend contexts (ウール混); no single obvious full-word target to merge into, so dropped rather than merged
# question 漏: no example sample given; unclear what the intended word/merge target is, if any
# question 瀬戸: ambiguous between the place name Seto and the common noun "strait"; examples only show place-derived compounds
# question 灘: real standalone word meaning "rough strait" exists, but examples here are dominated by the place name Nada; unclear whether to treat as common word or defer to the names list
# question 火星: unclear if planet names count under the pending-names place-name category or are plain common vocabulary
# question 煌: examples are mixed between names/brands and a possible 煌びやか clip; unclear whether a merge target is "obvious"
# question 牧: unclear whether 牧 has genuine standalone common-noun use or is purely a name component (李牧)
# question 瑞穂: mixes bank company name, politician's name, and possible place/market name; unclear which sense dominates
# question 白金: examples only show place usage (Shirokane) but furigana counts show some プラチナ (platinum) readings too; unclear which sense dominates overall
# question 石山: unclear whether most occurrences are the place name (Ishiyama, a real locality/temple) or the common surname; examples show both
# question 祖: no examples given to confirm whether it's a standalone word or a clipped fragment of a longer compound
# question 稲田: no example provided; can't confirm whether usage is mostly the surname (person name, drop) or the literal common noun "rice field" (keep)
# question 積: no example sample given; unclear whether current usage matches the standalone dictionary sense (せき, "product") or is a fragment of something else
# question 突: no examples and the readings (てんとつ/だんとつ) don't clearly point to one source word for a merge
# question 立花: examples mix surname use (立花さんと先生), company names (立花エレテック), and a possibly place-derived facility name (立花ジョイタウン); unclear whether this should be pending-names instead of drop
# question 総武: unclear whether this should be treated as a named-facility fragment (drop) or as a historical regional term eligible for pending-names
# question 緒方: could be a place name (town in Ōita) as well as a common surname; examples only show person use, so treated as drop rather than pending-names
# question 耐: unclear which single compound (耐久, 耐熱, 耐震...) the cut lemma should merge into
# question 聴: no examples provided to tell whether this is a stray piece of 聴く/聴覚 or something else; defaulted to drop
# question 自衛隊: unclear whether this should be treated as a specific named organisation (drop) or as ordinary institutional vocabulary like 警察 (keep)
# question 苑: unclear whether 苑 is ever written as a genuine standalone word versus only as a name-suffix
# question 萬: unclear whether this old kanji form should be kept as its own entry or merged into 万, since most uses are inside names rather than as the number itself
# question 藤: no examples in the sample to confirm common "wisteria" usage vs. pure surname use
# question 裂: unclear whether this is a genuine standalone technical term (botanical n裂 counter) or should merge into a specific word like 裂ける/裂け目
# question 補: no example text was available to judge whether this is a standalone word or a clipped piece
# question 覚: no example provided; can't tell if this is a fragment of 覚える/自覚 (merge target unclear) or has its own standalone use
# question 設: single kanji with no examples; likely a fragment of a longer word (設置/設定) but no examples to confirm which
# question 許: no examples given; unclear whether 許(もと) standalone sense is common enough to keep rather than drop
# question 該: no example text; unclear if it's ever standalone or only part of 該当 etc.
# question 警: no examples given; cannot tell if it's a clipped piece of a specific word (e.g. 警察) to merge into
# question 議: no example sentence is given, so the compound it was clipped from (議会, 会議, 議論...) can't be confirmed for a merge
# question 貨: no example text was given; the "か" reading dominance suggests a possible mix-up with the grammatical particle か, unclear what it should merge into
# question 資: no examples found to confirm whether this is a standalone word, part of a cut-off compound, or just name readings; treated as drop for lack of evidence
# question 赤十字: unclear whether to treat as organisation name (drop) or as a generic widely-understood term for the symbol/concept
# question 迷: no examples given; likely a fragment of 迷惑/迷子/迷彩 but no evidence to confirm a merge target
# question 送: no examples given; can't confirm whether it should merge into 送る/送信 or is unused alone
# question 郭: standalone くるわ use is not in the sample, only reading annotations.
# question 釈迦: a specific religious figure's name, but the word is deeply embedded in common idioms (釈迦に説法); unclear if it should count as a droppable "person" or a keepable common religious term
# question 野田: ambiguous whether primarily a place name (Noda city/line) or a person surname; chose pending-names
# question 閃: unclear whether this is a fragment of 閃く/閃光 or just part of the work title 閃乱カグラ; no clear merge target
# question 閉: no example given; unclear what compound it was cut from, so the merge target can't be confirmed
# question 閣: no examples found; unclear whether it's a standalone word or a compound fragment to merge
# question 隠: no example sentences; unclear which word (if any) it is clipped from
# question 高瀬: all examples show it as a surname, but it is also a known river/place name element; uncertain whether some underlying occurrences are place names
# question 高砂	: place name vs. common wedding-seat sense both present; unclear whether pending-names should take priority
# question 麻布: dictionary also lists a common sense (hemp cloth); unclear if that sense is common enough to keep rather than send to pending-names
# question 麻生: examples mix politician surname and a ward/police-station name derived from a place; unclear which sense should govern
# question ずきん: examples only show it inside the title/character name 赤ずきん, unclear if plain 頭巾 sense is attested independently
# question アシ: no examples given to confirm which common sense (reed vs. leg slang) is actually in use
# question カーリー: dictionary lists common, person, and proper senses; the given examples are mixed (a singer's name, a bare katakana token, a product name) and don't clearly show the common "curly" sense in everyday use.
# question トレス: no example given; unclear whether usage reflects the common art-slang sense "tracing" or a person/character name "Tres"
# question バサミ: the merge target spelling depends on which form (ハサミ / はさみ / 鋏) the list already carries for this word
# question パト: no example sentences given to confirm it's used as clipped パトカー rather than a name
# question モリ: no example given; unclear whether usage is mostly the common word (e.g. 銛/harpoon) or the katakana surname/given name "Mori"
# question ラバ: no example sentence given; assumed to be the common word for "mule", but can't confirm against actual usage.
# question よな: no examples available; could be a mislemmatized colloquial ending (だよな) rather than a real noun lemma
# question アニ: the only example is garbled/spam text, so it's unclear what sense (if any) this lemma is meant to capture
# question エホバ: deity's proper name isn't explicitly covered by the person/company/brand categories; treated as a name like a person, but could arguably warrant its own category
# question エリオット: examples split between a person's surname and a fragment of the place name レディエリオット島; no single clear category
# question ガリ: no example sentences given; unclear whether occurrences are the common noun (pickled ginger) or a character name, since the dictionary flag lists only name entries
# question ガー: no examples to confirm whether this is a real onomatopoeia/interjection or purely a name; dictionary says every sense is a person name but no example supports that
# question キチ: only one example given; unclear if "キチ" truly stands alone as common slang vs. being a clipped fragment of キチガイ that should instead be merge:気違い
# question キラ: no example sample given; unclear if any common-noun "kira" sense (e.g. glitter/jewel cut) is in everyday use vs. purely the character name
# question クウ: spelling split between ク(820)/クウ(174) suggests lemmatiser error; unclear what the intended word/name actually is
# question コキ: unclear if it ever stands alone outside 手コキ/両足コキ-type compounds, or is purely a clipped suffix
# question ション: no examples given; unclear if this is a standalone name, a clipped foreign-name syllable, or a cut-off piece of a longer word ending in -ション (e.g. セクション, ミッション); defaulted to drop.
# question シーザー: could also be dropped outright as a person's-name-only noun rather than merged into シーザーサラダ, since no example shows シーザー alone used as a common word
# question パーキンソン: similarly unclear whether to merge into パーキンソン病 or drop as purely a surname reference
# question マー: no examples found; unclear if it's ever used as a real word (interjection?) vs just a name entry
# question メビウス: examples shown are all the name/brand use; unclear how much of the corpus is the generic math term メビウスの輪/帯 versus the proper name
# question レコ: no examples retrieved; unclear whether occurrences are the person name or the common music-industry clipping of レコーディング/レコード
# question 今泉: appears both as a Fukuoka district name and as a common surname; unclear whether it should instead be pending-names
# question 備: no examples at all were provided, so it's unclear whether 備 is ever used standalone or only as a piece of compounds (設備, 準備, 完備)
# question 勉: one example suggests colloquial clipped use of 勉強, but rest of data is dominated by person-name readings; unclear whether this should merge into 勉強 instead
# question 宇: flagged shape with no examples; could be a piece of a longer word (e.g. 宇宙) or a standalone name character; no evidence to decide a merge target, defaulted to drop.
# question 宣: flagged shape with no examples; could be a piece of a longer word (宣伝, 宣言) or a name character; no evidence to decide a merge target, defaulted to drop.
# question 弁慶: whether a name whose only live general use is inside compounds (ネット弁慶, 内弁慶) counts as a "common sense in everyday use" under the both-senses rule.
# question 怜: flagged shape with examples only showing it as a given name; unclear if it has standalone common-word use as a character trait term, defaulted to drop.
# question 瞬: no examples shown; unclear if any common standalone use (vs. name/verb stem) exists
# question 萌: unclear how often the "moe" common sense is actually written as bare 萌 vs. 萌え in real text
# question 譲: the single usable example ("デリヘル譲と遊ばれたり") doesn't clearly show a common-noun use; may be a mangled/garbled text rather than a true word
# question 輝: no example sample given; unclear if the common "radiance" noun sense is in everyday standalone use vs. mostly a given name
# question 郁: unclear whether this kanji has any residual standalone literary use (e.g. 郁々) worth keeping, or is purely a name component
# question 金正: fragment is shared by 金正日 and 金正恩, so no single obvious merge target
# question 鳴: no examples available to tell if the 837 plain occurrences are a real standalone usage or a clipped compound (e.g. 悲鳴, 鳴き声) that should be merged
# question 片瀬: one example (片瀬龍口寺) suggests the Fujisawa place name 片瀬, but most examples are surname/character uses, unclear which sense dominates
# question 江戸: it names both the Edo era (time period, keep-worthy) and the historical city/place now Tokyo (would be pending-names); rules don't say how to treat era names derived from place names, and examples here lean toward era usage
