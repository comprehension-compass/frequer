# Review report: zh (full)

- Ranking score: `frequency`; 192,409 candidate lemmas ranked.
- Tokens counted: 818,629,336 in 1,049,585 documents, 120 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_zh` 1.6.4 (sha256 `2840ae8dc7e00290`); fallback `backend`, units on; honeyeater `8bc18170ed98`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-zh | 119 | 1,047,831 | 22,259,371 | 818,281,416 | alpha 1,517,648, exact_dup 2,369,284, gap 421,516, langid 1,551,295, length 495,812, near_dup 294,170, traditional 211,507, traditional_doc 221,290 |
| tatoeba-cmn | 1 | 1,754 | 49,067 | 347,920 | alpha 87, gap 6, length 21, near_dup 348, traditional 39,719 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 11,229,096. Sentences: 41,099,079.

## Units

Counted occurrences by kind: compound 298,455 (0.04%), compound1 4,941,045 (0.60%), construction 3,956,481 (0.48%), phrase 3,226,206 (0.39%), word 806,207,149 (98.48%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 4,898 | 5,240,672 |
| construction | 14 | 3,956,482 |
| phrase | 119 | 3,226,206 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `点头` | 129,767 | 72,343 | 858 |
| `说话` | 129,683 | 79,622 | 860 |
| `担心` | 105,128 | 74,467 | 1040 |
| `报名` | 85,770 | 26,792 | 1268 |
| `开口` | 83,730 | 47,200 | 1299 |
| `毕业` | 63,757 | 36,604 | 1664 |
| `摇头` | 63,292 | 44,628 | 1681 |
| `回家` | 58,100 | 39,623 | 1822 |
| `放心` | 56,765 | 45,616 | 1862 |
| `吃饭` | 54,650 | 34,769 | 1917 |
| `结婚` | 52,071 | 28,444 | 1993 |
| `抬头` | 46,811 | 35,734 | 2182 |
| `动手` | 42,568 | 30,436 | 2359 |
| `受伤` | 42,234 | 30,897 | 2372 |
| `帮忙` | 37,676 | 28,587 | 2609 |
| `回头` | 37,078 | 28,573 | 2644 |
| `怎么回事` | 34,787 | 25,640 | 2774 |
| `报警` | 33,307 | 16,708 | 2863 |
| `生气` | 32,670 | 23,542 | 2911 |
| `离婚` | 32,599 | 14,299 | 2916 |
| `睡觉` | 31,786 | 21,604 | 2985 |
| `深圳市` | 31,517 | 15,761 | 3007 |
| `低头` | 30,718 | 24,190 | 3068 |
| `见面` | 30,161 | 23,705 | 3115 |
| `用力` | 29,088 | 20,861 | 3211 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `被 + 动词` | 1,436,736 | 453,559 | 54 |
| `把 + 名词 + 动词` | 1,200,690 | 437,839 | 70 |
| `动词 + 得 + 补语` | 498,294 | 227,784 | 178 |
| `动词 + 得/不 + 补语` | 253,884 | 160,388 | 395 |
| `比 + 名词 + 形容词` | 240,464 | 161,619 | 426 |
| `是…的` | 229,397 | 156,064 | 454 |
| `要…了` | 62,296 | 50,475 | 1707 |
| `动词 + 得/不 + 起` | 16,409 | 14,462 | 4978 |
| `动词 + 得/不 + 动` | 8,218 | 7,514 | 8251 |
| `动词 + 得/不 + 过` | 4,263 | 4,078 | 13157 |
| `动词 + 得/不 + 下` | 3,970 | 3,737 | 13835 |
| `〜来〜去` | 1,781 | 1,674 | 24073 |
| `快…了` | 78 | 76 | 148148 |
| `就要…了` | 2 | 2 | - |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `在〜中` | 662,836 | 338,373 | 137 |
| `在〜下` | 266,733 | 183,014 | 366 |
| `虽然…但` | 172,600 | 112,219 | 628 |
| `如果…就` | 144,379 | 102,121 | 771 |
| `当…时` | 97,355 | 69,104 | 1103 |
| `尤其是` | 83,734 | 68,129 | 1298 |
| `以〜为〜` | 80,508 | 61,315 | 1353 |
| `只要…就` | 79,894 | 64,216 | 1365 |
| `对于〜来说` | 76,636 | 58,912 | 1415 |
| `像〜一样` | 62,003 | 48,569 | 1718 |
| `看起来` | 61,956 | 45,966 | 1720 |
| `从〜开始` | 59,380 | 50,623 | 1786 |
| `在…的时候` | 58,934 | 47,605 | 1799 |
| `对〜来说` | 52,684 | 43,341 | 1978 |
| `不是…而是` | 51,142 | 43,640 | 2026 |
| `虽然…但是` | 45,974 | 35,211 | 2217 |
| `和〜一样` | 42,173 | 35,588 | 2376 |
| `就算…也` | 41,063 | 33,029 | 2428 |
| `在〜上` | 40,759 | 35,862 | 2440 |
| `打电话` | 39,915 | 27,097 | 2481 |
| `即使…也` | 39,840 | 32,434 | 2489 |
| `不仅…还` | 39,666 | 35,197 | 2495 |
| `连…都` | 38,080 | 32,858 | 2582 |
| `和〜一起` | 38,044 | 31,492 | 2583 |
| `特别是` | 34,749 | 30,908 | 2775 |

## Co-occurrence (association) table

96,161,809 tokens, 4,948,793 sentences. After merging and dropping items seen fewer than 5 times: 4,147,794 items (unigrams, UPOS votes, n-grams, pairs); 3,577,634 n-grams and pairs scored (n2 1,660,773, n3 1,338,264, n4 578,597). Shipped: 400,000 rows, 8.7 MB gzipped (`zh.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`zh.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `时时 彩` |  | 285,581 | 1,524 | 8.15 | 0.97 | 3,542,784 |  |
| 2 | n | `一 个` |  | 261,898 | 62,735 | 4.89 | 0.57 | 1,432,970 |  |
| 3 | n | `来 的` |  | 46,588 | 23,770 | 14.65 | 1.33 | 946,721 |  |
| 4 | n | `过 来` |  | 30,833 | 15,192 | 18.93 | 1.63 | 814,973 |  |
| 5 | n | `来 了` |  | 32,199 | 16,913 | 15.84 | 1.37 | 707,644 |  |
| 6 | n | `重庆 时时 彩` |  | 63,768 | 974 | 8.07 | 0.76 | 677,090 |  |
| 7 | n | `pc 蛋蛋` |  | 23,462 | 151 | 11.65 | 0.97 | 401,526 |  |
| 8 | n | `北京 pk10` |  | 28,400 | 309 | 9.83 | 0.84 | 374,474 |  |
| 9 | n | `来 到` |  | 15,610 | 10,300 | 16.43 | 1.31 | 356,125 |  |
| 10 | n | `很 多` |  | 49,859 | 26,411 | 6.13 | 0.56 | 345,381 |  |
| 11 | n | `来 看` |  | 13,912 | 10,049 | 16.94 | 1.33 | 327,353 |  |
| 12 | n | `不 敢` |  | 15,885 | 10,149 | 14.02 | 1.12 | 308,990 |  |
| 13 | n | `心 水 论坛` |  | 21,604 | 224 | 10.22 | 0.84 | 307,147 |  |
| 14 | n | `看 到` |  | 52,831 | 25,346 | 5.11 | 0.47 | 286,387 |  |
| 15 | n | `看 着` |  | 46,024 | 16,991 | 5.34 | 0.48 | 264,108 |  |
| 16 | n | `不 会` |  | 59,272 | 28,921 | 4.32 | 0.40 | 256,248 |  |
| 17 | n | `不 能` |  | 54,989 | 29,109 | 4.51 | 0.42 | 253,218 |  |
| 18 | n | `一 步` |  | 10,956 | 7,741 | 16.63 | 1.27 | 252,723 |  |
| 19 | n | `香港 马 会` |  | 20,199 | 269 | 8.21 | 0.67 | 230,175 |  |
| 20 | n | `都 是` |  | 66,492 | 32,583 | 3.65 | 0.35 | 227,937 |  |
| 21 | n | `两 个` |  | 42,258 | 21,604 | 5.04 | 0.45 | 226,660 |  |
| 22 | n | `进 来` |  | 8,677 | 5,706 | 18.61 | 1.38 | 225,141 |  |
| 23 | n | `也 是` |  | 73,404 | 34,130 | 3.34 | 0.32 | 220,336 |  |
| 24 | n | `到 了` |  | 73,634 | 29,721 | 3.27 | 0.32 | 214,686 |  |
| 25 | n | `更 多` |  | 30,789 | 19,725 | 6.18 | 0.53 | 213,200 |  |
| 26 | n | `传 来` |  | 7,406 | 5,265 | 19.93 | 1.46 | 207,720 |  |
| 27 | n | `一 种` |  | 44,146 | 23,931 | 4.54 | 0.41 | 207,536 |  |
| 28 | n | `一 条` |  | 14,236 | 9,760 | 10.41 | 0.82 | 205,630 |  |
| 29 | n | `不 知道` |  | 35,652 | 18,372 | 5.18 | 0.45 | 200,871 |  |
| 30 | n | `正 是` |  | 11,356 | 8,402 | 12.56 | 0.96 | 197,860 |  |
| 31 | n | `年 来` |  | 8,646 | 6,884 | 16.41 | 1.22 | 196,964 |  |
| 32 | n | `一 声` |  | 29,104 | 12,809 | 5.70 | 0.49 | 196,645 |  |
| 33 | n | `还 有` |  | 36,498 | 23,133 | 4.67 | 0.41 | 173,567 |  |
| 34 | n | `一 次` |  | 37,987 | 21,752 | 4.43 | 0.39 | 172,157 |  |
| 35 | n | `幸运 飞艇` |  | 11,829 | 134 | 10.48 | 0.81 | 171,337 |  |
| 36 | n | `句 话` |  | 12,994 | 8,149 | 9.84 | 0.77 | 162,021 |  |
| 37 | n | `腾讯 分 分 彩` |  | 14,356 | 130 | 8.18 | 0.64 | 159,514 |  |
| 38 | n | `万 元` |  | 17,277 | 6,433 | 7.78 | 0.62 | 159,155 |  |
| 39 | n | `上 来` |  | 7,090 | 5,248 | 15.49 | 1.13 | 152,343 |  |
| 40 | n | `只 有` |  | 27,644 | 18,495 | 5.08 | 0.43 | 147,921 |  |
| 41 | n | `想 到` |  | 27,608 | 15,274 | 5.09 | 0.43 | 147,644 |  |
| 42 | n | `亿 元` |  | 13,792 | 5,346 | 8.70 | 0.68 | 147,275 |  |
| 43 | n | `幸运 农场` |  | 10,328 | 118 | 10.39 | 0.79 | 145,632 |  |
| 44 | n | `几 个` |  | 25,275 | 14,739 | 5.20 | 0.44 | 141,188 |  |
| 45 | n | `个 人` |  | 42,385 | 19,139 | 3.60 | 0.32 | 139,568 |  |
| 46 | n | `带 着` |  | 19,154 | 11,552 | 6.38 | 0.52 | 139,173 |  |
| 47 | n | `只 能` |  | 21,588 | 14,741 | 5.81 | 0.48 | 136,634 |  |
| 48 | n | `近年 来` |  | 4,413 | 3,718 | 21.19 | 1.47 | 135,834 |  |
| 49 | n | `心 中` |  | 19,498 | 9,949 | 6.19 | 0.50 | 135,378 |  |
| 50 | n | `讯 网` |  | 10,162 | 148 | 9.97 | 0.75 | 130,846 |  |

### Verb pairs in the queue

_none_

## Rank shifts against the live snapshot (`reference/lemmas/zh.json`)

_No live snapshot to compare with._

## Ported frequer checks

### Form-ratio outliers (192)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4 | `一` | 10,537,043 | median form 518; `一` 9,548,464 (18433x), `1` 971,769 (1876x) |
| 132 | `十` | 689,426 | median form 68; `10` 470,310 (6916x), `十` 218,736 (3217x) |
| 183 | `十一` | 489,437 | median form 13.5; `11` 459,179 (34013x), `十一` 30,083 (2228x) |
| 216 | `九` | 433,026 | median form 188; `9` 269,261 (1432x) |
| 299 | `十二` | 319,410 | median form 35.5; `12` 273,008 (7690x), `十二` 46,317 (1305x) |
| 328 | `二十` | 299,833 | median form 7; `20` 248,166 (35452x), `二十` 51,620 (7374x) |
| 516 | `为什么` | 202,772 | median form 8.5; `为什么` 202,753 (23853x) |
| 716 | `十八` | 154,283 | median form 5.5; `18` 120,369 (21885x), `十八` 33,901 (6164x) |
| 723 | `越来越` | 152,965 | median form 20.5; `越来越` 152,919 (7459x) |
| 802 | `加` | 139,512 | median form 3; `加` 139,508 (46503x) |
| 806 | `十三` | 138,879 | median form 17; `13` 115,987 (6823x), `十三` 22,859 (1345x) |
| 844 | `互联网` | 131,320 | median form 11.5; `互联网` 131,289 (11416x) |
| 862 | `加拿大` | 128,990 | median form 7; `加拿大` 128,972 (18425x) |
| 1001 | `二十四` | 109,758 | median form 13; `24` 105,277 (8098x) |
| 1008 | `消费者` | 109,037 | median form 18; `消费者` 109,006 (6056x) |
| 1025 | `二十五` | 107,095 | median form 3; `25` 104,418 (34806x) |
| 1088 | `十九` | 99,389 | median form 3; `19` 84,613 (28204x), `十九` 14,768 (4923x) |
| 1099 | `团` | 98,097 | median form 3; `团` 98,093 (32698x) |
| 1141 | `怎么样` | 94,231 | median form 11; `怎么样` 94,205 (8564x) |
| 1173 | `二十一` | 92,085 | median form 2; `21` 89,001 (44500x), `二十一` 3,080 (1540x) |
| 1262 | `色` | 86,291 | median form 14; `色` 86,276 (6163x) |
| 1370 | `办公室` | 79,544 | median form 3.5; `办公室` 79,535 (22724x) |
| 1472 | `二十三` | 73,956 | median form 10.5; `23` 72,777 (6931x) |
| 1567 | `负责人` | 68,523 | median form 30.5; `负责人` 68,460 (2245x) |
| 1596 | `人民币` | 67,080 | median form 18.5; `人民币` 67,042 (3624x) |

_167 more not shown._

### Singular/plural mismatch (0)

Lemma looks like a plural whose stripped form maps to another listed lemma.

_none_

### Lemma consistency (2)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 2190 | `人家` | 46,636 | alone, `人家` lemmatises to `人家#rénjiā` (rank 3,613) |
| 9172 | `某某` | 7,130 | alone, `某某` lemmatises to `某` (rank 485) |

### Short lemmas (1,674)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `的` | 41,861,315 | `的` -> `的` |
| 3 | `是` | 11,641,221 | `是` -> `是` |
| 4 | `一` | 10,537,043 | `一` -> `一`, `1` -> `一`, `①` -> `一`, `I` -> `?`, `Ⅰ` -> `?` |
| 5 | `在` | 8,330,092 | `在` -> `在` |
| 6 | `不` | 7,390,384 | `不` -> `不` |
| 7 | `个` | 6,128,444 | `个` -> `个` |
| 8 | `这` | 5,687,698 | `这` -> `这` |
| 9 | `和` | 4,804,311 | `和` -> `和` |
| 10 | `有` | 4,757,170 | `有` -> `有` |
| 11 | `我` | 4,671,933 | `我` -> `我` |
| 12 | `就` | 4,452,756 | `就` -> `就` |
| 13 | `也` | 4,168,886 | `也` -> `也` |
| 14 | `人` | 3,835,993 | `人` -> `人` |
| 15 | `他` | 3,786,582 | `他` -> `他` |
| 16 | `你` | 3,499,348 | `你` -> `你`, `伱` -> `伱` |
| 19 | `都` | 3,046,451 | `都` -> `都` |
| 21 | `会` | 2,716,734 | `会` -> `会` |
| 24 | `年` | 2,401,715 | `年` -> `年`, `年#` -> `?` |
| 25 | `多` | 2,384,353 | `多` -> `多` |
| 26 | `对` | 2,296,842 | `对` -> `对` |
| 27 | `要` | 2,222,554 | `要` -> `要` |
| 28 | `能` | 2,180,104 | `能` -> `能` |
| 29 | `说` | 2,168,176 | `说` -> `说` |
| 31 | `很` | 2,100,276 | `很` -> `很` |
| 33 | `那` | 2,074,112 | `那` -> `那` |

_1,649 more not shown._

### Case merges (0)

Non-lowercase lemmas, with the lowercase twin where one is listed.

_none_

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 754 (75.4%).

Ours only: `彩`, `时时`, `被 + 动词`, `把 + 名词 + 动词`, `十`, `在〜中`, `百分之`, `前`, `重庆`, `动词 + 得 + 补语`, `十一`, `儿#r`, `说道`, `二十八`, `幸运`, `声`, `有限公司`, `林`, `周#week`, `软件`, `的话`, `十二`, `开奖`, `脸`, `眼`

wordfreq only: `〇〇〇〇`, `〇〇〇`, `政治`, `第`, `人民`, `运动`, `自由`, `委员会`, `人口`, `民主`, `事件`, `零点零`, `县`, `总统`, `战争`, `照片`, `时期`, `故事`, `欧洲`, `举行`, `艺术`, `独立`, `亚洲`, `人类`, `制`

## Foreign-word candidates

_none_

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 56 | `中国` | 1,408,434 | PROPN 98%, capitalised forms 0% |
| 138 | `美国` | 650,268 | PROPN 99%, capitalised forms 0% |
| 142 | `北京` | 608,559 | PROPN 100%, capitalised forms 0% |
| 168 | `重庆` | 518,945 | PROPN 97%, capitalised forms 0% |
| 201 | `王` | 458,968 | PROPN 100%, capitalised forms 0% |
| 261 | `林` | 369,451 | PROPN 99%, capitalised forms 0% |
| 264 | `香港` | 367,132 | PROPN 100%, capitalised forms 0% |
| 353 | `李` | 279,566 | PROPN 100%, capitalised forms 0% |
| 437 | `韩国` | 235,996 | PROPN 100%, capitalised forms 0% |
| 457 | `上海` | 228,681 | PROPN 100%, capitalised forms 0% |
| 503 | `台湾` | 206,955 | PROPN 97%, capitalised forms 0% |
| 512 | `日本` | 203,928 | PROPN 98%, capitalised forms 0% |
| 531 | `杨` | 198,396 | PROPN 99%, capitalised forms 0% |
| 606 | `广东` | 177,584 | PROPN 100%, capitalised forms 0% |
| 644 | `培训` | 167,723 | PROPN 76%, capitalised forms 0% |
| 655 | `秦` | 166,260 | PROPN 97%, capitalised forms 0% |
| 665 | `云` | 164,896 | PROPN 91%, capitalised forms 0% |
| 736 | `腾讯` | 150,760 | PROPN 100%, capitalised forms 0% |
| 824 | `安装` | 134,739 | PROPN 56%, capitalised forms 0% |
| 862 | `加拿大` | 128,990 | PROPN 100%, capitalised forms 0% |
| 863 | `走势图` | 128,989 | PROPN 99%, capitalised forms 0% |
| 896 | `英国` | 123,805 | PROPN 96%, capitalised forms 0% |
| 935 | `平` | 118,236 | PROPN 58%, capitalised forms 0% |
| 1022 | `微信` | 107,395 | PROPN 100%, capitalised forms 0% |
| 1031 | `亚洲` | 106,301 | PROPN 95%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 91.0% | 0.911 |
| juilland_u | 99.7% | 1.000 |
| juilland_u_corrected | 99.7% | 1.000 |
| dp_adjusted | 99.2% | 0.999 |
| cd_blend | 95.3% | 0.971 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `除了…外` | 6362 | 4745 | -1,617 | 12,020 | 11,243 | 0.990 | 0.039 |
| `违者` | 5427 | 3820 | -1,607 | 14,832 | 14,588 | 0.991 | 0.035 |
| `备受` | 6437 | 4836 | -1,601 | 11,809 | 10,990 | 0.991 | 0.038 |
| `好不容易` | 6513 | 4953 | -1,560 | 11,602 | 10,623 | 0.988 | 0.048 |
| `只有…才` | 5922 | 4392 | -1,530 | 13,219 | 12,395 | 0.990 | 0.040 |
| `彩霸王` | 2672 | 35606 | +32,934 | 36,989 | 717 | 0.957 | 0.172 |
| `曾道人` | 2063 | 32792 | +30,729 | 50,469 | 812 | 0.957 | 0.172 |
| `刘伯温` | 488 | 30416 | +29,928 | 214,585 | 907 | 0.957 | 0.175 |
| `九五至尊` | 4107 | 28717 | +24,610 | 21,383 | 985 | 0.958 | 0.171 |
| `赛马会` | 1470 | 20798 | +19,328 | 74,464 | 1,563 | 0.957 | 0.173 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `大事` | 4157 | 4111 | -46 | 21,151 | 18,005 | 0.992 | 0.033 |
| `偶尔` | 4160 | 4116 | -44 | 21,123 | 18,371 | 0.992 | 0.033 |
| `开玩笑` | 4985 | 4944 | -41 | 16,644 | 14,196 | 0.992 | 0.033 |
| `五十五` | 4156 | 4119 | -37 | 21,156 | 15,365 | 0.990 | 0.041 |
| `另一方面` | 4979 | 4942 | -37 | 16,668 | 15,258 | 0.991 | 0.033 |
| `胖` | 3431 | 3889 | +458 | 27,084 | 10,857 | 0.840 | 0.232 |
| `海关` | 4952 | 5407 | +455 | 16,789 | 7,534 | 0.870 | 0.164 |
| `温` | 4407 | 4719 | +312 | 19,563 | 9,098 | 0.894 | 0.147 |
| `唯美` | 4101 | 4278 | +177 | 21,416 | 5,060 | 0.930 | 0.285 |
| `枫` | 2628 | 2766 | +138 | 37,827 | 4,608 | 0.922 | 0.145 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `大事` | 4157 | 4111 | -46 | 21,151 | 18,005 | 0.992 | 0.033 |
| `偶尔` | 4160 | 4116 | -44 | 21,123 | 18,371 | 0.992 | 0.033 |
| `开玩笑` | 4985 | 4944 | -41 | 16,644 | 14,196 | 0.992 | 0.033 |
| `五十五` | 4156 | 4119 | -37 | 21,156 | 15,365 | 0.990 | 0.041 |
| `另一方面` | 4979 | 4942 | -37 | 16,668 | 15,258 | 0.991 | 0.033 |
| `胖` | 3431 | 3889 | +458 | 27,084 | 10,857 | 0.840 | 0.232 |
| `海关` | 4952 | 5408 | +456 | 16,789 | 7,534 | 0.870 | 0.164 |
| `温` | 4407 | 4721 | +314 | 19,563 | 9,098 | 0.894 | 0.147 |
| `唯美` | 4101 | 4280 | +179 | 21,416 | 5,060 | 0.930 | 0.285 |
| `枫` | 2628 | 2766 | +138 | 37,827 | 4,608 | 0.922 | 0.145 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `尽可能` | 4828 | 4702 | -126 | 17,293 | 14,962 | 0.992 | 0.033 |
| `何时` | 4907 | 4781 | -126 | 16,939 | 14,786 | 0.992 | 0.030 |
| `广阔` | 5109 | 4990 | -119 | 16,092 | 14,443 | 0.992 | 0.032 |
| `另一方面` | 4979 | 4863 | -116 | 16,668 | 15,258 | 0.991 | 0.033 |
| `感叹` | 5104 | 4988 | -116 | 16,127 | 14,285 | 0.992 | 0.033 |
| `唯美` | 4101 | 5044 | +943 | 21,416 | 5,060 | 0.930 | 0.285 |
| `头像` | 2942 | 3556 | +614 | 32,640 | 4,583 | 0.938 | 0.252 |
| `胖` | 3431 | 4020 | +589 | 27,084 | 10,857 | 0.840 | 0.232 |
| `九五至尊` | 4107 | 4520 | +413 | 21,383 | 985 | 0.958 | 0.171 |
| `海关` | 4952 | 5358 | +406 | 16,789 | 7,534 | 0.870 | 0.164 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `违者` | 5427 | 4573 | -854 | 14,832 | 14,588 | 0.991 | 0.035 |
| `除此之外` | 5736 | 4935 | -801 | 13,791 | 12,814 | 0.991 | 0.034 |
| `旨在` | 5685 | 4952 | -733 | 13,954 | 12,542 | 0.990 | 0.039 |
| `毫不` | 5114 | 4384 | -730 | 16,051 | 14,686 | 0.991 | 0.036 |
| `一旦…就` | 5528 | 4802 | -726 | 14,423 | 13,324 | 0.992 | 0.033 |
| `彩霸王` | 2672 | 10084 | +7,412 | 36,989 | 717 | 0.957 | 0.172 |
| `九五至尊` | 4107 | 10983 | +6,876 | 21,383 | 985 | 0.958 | 0.171 |
| `曾道人` | 2063 | 8524 | +6,461 | 50,469 | 812 | 0.957 | 0.172 |
| `赛马会` | 1470 | 5777 | +4,307 | 74,464 | 1,563 | 0.957 | 0.173 |
| `刘伯温` | 488 | 4781 | +4,293 | 214,585 | 907 | 0.957 | 0.175 |



## Junk-filter heuristics

Rules on: diversity, citation, shape, propn_band; accent merges at ratio None. Window: the 52,219 ranked lemmas (after the exclusion list) that fill the top 50,000. Actions: drop 62, keep 45,381, number-drop 387, pending 567, review-drop 1,770, review-keep 4,052.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band | propn_usage |
|---|---:|---:|---:|---:|---:|---:|
| diversity | 899 | 0 | 0 | 19 | 259 | 0 |
| citation | 0 | 1 | 0 | 0 | 0 | 0 |
| foreign | 0 | 0 | 0 | 0 | 0 | 0 |
| shape | 19 | 0 | 0 | 1,078 | 49 | 0 |
| propn_band | 259 | 0 | 0 | 49 | 6,578 | 0 |
| propn_usage | 0 | 0 | 0 | 0 | 0 | 0 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 0.

### Low diversity

Documents reached / documents expected at random, below 0.2 (frequency >= 20): 899 in the window. For comparison, each log2-frequency band's 2nd percentile: 32-63: 0.04, 64-127: 0.06, 128-255: 0.09, 256-511: 0.13, 512-1023: 0.18, 1024-2047: 0.21, 2048-4095: 0.23, 4096-8191: 0.26, 8192-16383: 0.23, 16384-32767: 0.27, 32768-65535: 0.22, 65536-131071: 0.26, 131072-262143: 0.2, 262144-524287: 0.21.

Examples: `彩` (35), `时时` (36), `重庆` (168), `二十八` (231), `幸运` (239), `开奖` (308), `论坛` (388), `刘伯温` (488), `技巧` (558), `秦` (659), `预测` (710), `腾讯` (741), `蛋蛋` (747), `叶` (752), `传奇` (815), `投注` (832), `加拿大` (868), `走势图` (869), `彩票` (1178), `陆` (1227), `新疆` (1249), `飞艇` (1439), `楚` (1460), `赛马会` (1470), `玩法` (1484), `农场` (1524), `修士` (1700), `赛车` (1728), `胆` (1804), `娱乐城` (1861), `五星` (1944), `肖` (1946), `萧` (1993), `曾道人` (2063), `私服` (2097), `遗漏` (2103), `图表` (2176), `二手` (2330), `白癜风` (2422), `龙虎` (2431)

### Accent merges (26)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `云湾` | `云` | 10,647 | review: merge |
| `一提的是` | `值得一提的是` | 6,691 | review: merge |
| `博会` | `进博会` | 4,238 | review: merge |
| `是否是` | `是否` | 3,080 | review: merge |
| `白了` | `说白了` | 2,224 | review: merge |
| `书目的` | `书目` | 1,833 | review: merge |
| `二话不` | `二话不说` | 2,036 | review: merge |
| `百度网` | `百度网盘` | 2,106 | review: merge |
| `少先` | `少先队` | 1,839 | review: merge |
| `钣` | `钣金` | 1,581 | review: merge |
| `源热泵` | `热泵` | 1,641 | review: merge |
| `名目的` | `名目` | 1,990 | review: merge |
| `地方湾` | `地方` | 2,019 | review: merge |
| `完全全` | `完完全全` | 1,811 | review: merge |
| `大部份` | `大部分` | 1,142 | review: merge |
| `大打出` | `大打出手` | 1,028 | review: merge |
| `飚` | `飙` | 1,119 | review: merge |
| `丛林中` | `丛林` | 979 | review: merge |
| `交组织` | `交织` | 1,067 | review: merge |
| `伱` | `你` | 877 | review: merge |
| `特有的` | `特有` | 949 | review: merge |
| `谴` | `天谴` | 880 | review: merge |
| `讲话中` | `讲话` | 1,100 | review: merge |
| `片狼藉` | `一片狼藉` | 859 | review: merge |
| `淬` | `淬火` | 868 | review: merge |
| `编组织` | `编织` | 733 | review: merge |

### Dropped by 2+ flags: random sample of 50 of 62 in the window

| rank | lemma | flags |
|---:|---|---|
| 42576 | `巩` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 42891 | `李睿` | diversity: in 77 documents, 0.10 of the 784 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43163 | `王世充` | diversity: in 150 documents, 0.19 of the 776 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43191 | `李兴` | diversity: in 107 documents, 0.14 of the 775 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43627 | `阿木` | diversity: in 130 documents, 0.17 of the 764 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43774 | `刘镒华` | diversity: in 52 documents, 0.07 of the 759 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43845 | `隽` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 44277 | `李轩` | diversity: in 89 documents, 0.12 of the 746 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 44348 | `徐少杰` | diversity: in 29 documents, 0.04 of the 744 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 44450 | `古枫` | diversity: in 49 documents, 0.07 of the 741 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45058 | `昧` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45141 | `叶音竹` | diversity: in 104 documents, 0.14 of the 723 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45335 | `菁` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46135 | `太夫人` | diversity: in 121 documents, 0.17 of the 698 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46322 | `苏墨` | diversity: in 56 documents, 0.08 of the 694 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46606 | `唐焱` | diversity: in 53 documents, 0.08 of the 686 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46632 | `自攻螺钉` | diversity: in 93 documents, 0.14 of the 686 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46797 | `王轲` | diversity: in 82 documents, 0.12 of the 682 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 46833 | `李叶` | diversity: in 59 documents, 0.09 of the 681 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47153 | `罗睺` | diversity: in 113 documents, 0.17 of the 674 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47320 | `欧阳明` | diversity: in 112 documents, 0.17 of the 670 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47385 | `苏方` | diversity: in 81 documents, 0.12 of the 669 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47617 | `林若溪` | diversity: in 68 documents, 0.10 of the 664 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47693 | `奥斯丁` | diversity: in 130 documents, 0.20 of the 662 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 47726 | `亘` | diversity: in 113 documents, 0.17 of the 661 occurrences' random spread (threshold 0.2); shape: length 1 |
| 47938 | `夯` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48092 | `苏悠悠` | diversity: in 47 documents, 0.07 of the 653 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48824 | `逸轩` | diversity: in 83 documents, 0.13 of the 639 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48839 | `季子` | diversity: in 94 documents, 0.15 of the 638 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48854 | `琨` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48985 | `苏易` | diversity: in 44 documents, 0.07 of the 635 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 49197 | `朱厚照` | diversity: in 80 documents, 0.13 of the 630 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 49202 | `燚` | diversity: in 78 documents, 0.12 of the 630 occurrences' random spread (threshold 0.2); shape: length 1 |
| 49639 | `苏萌` | diversity: in 36 documents, 0.06 of the 621 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 49721 | `穆浩` | diversity: in 14 documents, 0.02 of the 619 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50114 | `瓢` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50177 | `燕青` | diversity: in 113 documents, 0.19 of the 610 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50305 | `罗川` | diversity: in 55 documents, 0.09 of the 608 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50492 | `浅悠凉` | diversity: in 17 documents, 0.03 of the 604 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50544 | `洛璃` | diversity: in 110 documents, 0.18 of the 603 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50608 | `韩宇` | diversity: in 98 documents, 0.16 of the 602 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50639 | `林易衍` | diversity: in 24 documents, 0.04 of the 601 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50769 | `李玄` | diversity: in 93 documents, 0.16 of the 598 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50794 | `陈寻` | diversity: in 48 documents, 0.08 of the 598 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 51353 | `李瑞` | diversity: in 112 documents, 0.19 of the 587 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 51544 | `苏婉` | diversity: in 73 documents, 0.13 of the 584 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 51714 | `苏荆` | diversity: in 42 documents, 0.07 of the 581 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 51845 | `傲宇` | diversity: in 56 documents, 0.10 of the 578 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 52081 | `锣` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 52085 | `马克西` | diversity: in 95 documents, 0.17 of the 575 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |

### Single flag, not yet reviewed: 567 (kept until reviewed)

| rank | lemma | flag |
|---:|---|---|
| 231 | `二十八` | diversity: in 53,589 documents, 0.16 of the 412,417 occurrences' random spread (threshold 0.2) |
| 388 | `论坛` | diversity: in 38,426 documents, 0.17 of the 257,141 occurrences' random spread (threshold 0.2) |
| 558 | `技巧` | diversity: in 34,318 documents, 0.20 of the 192,390 occurrences' random spread (threshold 0.2) |
| 710 | `预测` | diversity: in 26,548 documents, 0.18 of the 156,010 occurrences' random spread (threshold 0.2) |
| 815 | `传奇` | diversity: in 20,527 documents, 0.16 of the 138,509 occurrences' random spread (threshold 0.2) |
| 1484 | `玩法` | diversity: in 13,568 documents, 0.19 of the 73,901 occurrences' random spread (threshold 0.2) |
| 1728 | `赛车` | diversity: in 9,739 documents, 0.16 of the 62,099 occurrences' random spread (threshold 0.2) |
| 1804 | `胆` | diversity: in 6,484 documents, 0.11 of the 59,113 occurrences' random spread (threshold 0.2) |
| 1944 | `五星` | diversity: in 5,475 documents, 0.10 of the 54,375 occurrences' random spread (threshold 0.2) |
| 2103 | `遗漏` | diversity: in 5,502 documents, 0.11 of the 49,104 occurrences' random spread (threshold 0.2) |
| 2155 | `三星` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2535 | `公式` | diversity: in 5,515 documents, 0.14 of the 39,323 occurrences' random spread (threshold 0.2) |
| 2779 | `源码` | diversity: in 5,063 documents, 0.15 of the 35,157 occurrences' random spread (threshold 0.2) |
| 3329 | `缩水` | diversity: in 4,951 documents, 0.18 of the 28,212 occurrences' random spread (threshold 0.2) |
| 3444 | `投标` | diversity: in 5,269 documents, 0.20 of the 26,882 occurrences' random spread (threshold 0.2) |
| 4106 | `福彩` | diversity: in 3,708 documents, 0.18 of the 21,388 occurrences' random spread (threshold 0.2) |
| 4151 | `六合彩` | diversity: in 4,050 documents, 0.19 of the 21,171 occurrences' random spread (threshold 0.2) |
| 4675 | `玄机` | diversity: in 3,501 documents, 0.20 of the 18,012 occurrences' random spread (threshold 0.2) |
| 5046 | `复式` | diversity: in 2,804 documents, 0.17 of the 16,370 occurrences' random spread (threshold 0.2) |
| 5406 | `任选` | diversity: in 2,458 documents, 0.17 of the 14,868 occurrences' random spread (threshold 0.2) |
| 5439 | `赔率` | diversity: in 2,552 documents, 0.17 of the 14,778 occurrences' random spread (threshold 0.2) |
| 5594 | `合击` | diversity: in 2,717 documents, 0.19 of the 14,223 occurrences' random spread (threshold 0.2) |
| 5709 | `宫颈` | diversity: in 2,723 documents, 0.20 of the 13,869 occurrences' random spread (threshold 0.2) |
| 5762 | `四星` | diversity: in 2,098 documents, 0.15 of the 13,696 occurrences' random spread (threshold 0.2) |
| 6020 | `翡翠` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 6458 | `豹子` | diversity: in 2,087 documents, 0.18 of the 11,764 occurrences' random spread (threshold 0.2) |
| 8018 | `豆豆` | diversity: in 1,502 documents, 0.17 of the 8,757 occurrences' random spread (threshold 0.2) |
| 8047 | `投注网` | diversity: in 1,402 documents, 0.16 of the 8,724 occurrences' random spread (threshold 0.2) |
| 8402 | `投注站` | diversity: in 1,312 documents, 0.16 of the 8,226 occurrences' random spread (threshold 0.2) |
| 8801 | `除尘器` | diversity: in 1,317 documents, 0.17 of the 7,720 occurrences' random spread (threshold 0.2) |
| 9072 | `土豆` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 9259 | `小强` | diversity: in 1,413 documents, 0.20 of the 7,226 occurrences' random spread (threshold 0.2) |
| 9563 | `神算` | diversity: in 1,084 documents, 0.16 of the 6,911 occurrences' random spread (threshold 0.2) |
| 9950 | `腾龙` | diversity: in 1,150 documents, 0.18 of the 6,536 occurrences' random spread (threshold 0.2) |
| 10003 | `杰克` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 11000 | `老二` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 11817 | `专业性` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 12079 | `温室` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 12766 | `坚定不移` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 13434 | `莫言` | diversity: in 705 documents, 0.16 of the 4,287 occurrences' random spread (threshold 0.2) |
| 13897 | `教职工` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 14280 | `莱恩` | diversity: in 726 documents, 0.18 of the 3,938 occurrences' random spread (threshold 0.2) |
| 14756 | `算账` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 15094 | `五码` | diversity: in 678 documents, 0.19 of the 3,647 occurrences' random spread (threshold 0.2) |
| 15402 | `啥意思` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 15691 | `滤袋` | diversity: in 664 documents, 0.19 of the 3,456 occurrences' random spread (threshold 0.2) |
| 16504 | `冲压` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 16639 | `林龙` | diversity: in 250 documents, 0.08 of the 3,166 occurrences' random spread (threshold 0.2) |
| 16722 | `彩返` | diversity: in 615 documents, 0.20 of the 3,148 occurrences' random spread (threshold 0.2) |
| 17542 | `市面上` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 17995 | `黄沙` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 18091 | `试剂盒` | diversity: in 550 documents, 0.20 of the 2,808 occurrences' random spread (threshold 0.2) |
| 18093 | `林中` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 19780 | `处女膜` | diversity: in 495 documents, 0.20 of the 2,490 occurrences' random spread (threshold 0.2) |
| 20272 | `丰台` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 20643 | `铜材` | diversity: in 408 documents, 0.17 of the 2,342 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 21994 | `胜负彩` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 22056 | `波色` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 22431 | `曼哈顿` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 22672 | `唐浩` | diversity: in 93 documents, 0.05 of the 2,037 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 23267 | `李云飞` | diversity: in 184 documents, 0.09 of the 1,967 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 23888 | `天问` | diversity: in 374 documents, 0.20 of the 1,895 occurrences' random spread (threshold 0.2) |
| 24321 | `铜制品` | diversity: in 216 documents, 0.12 of the 1,849 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 24421 | `本港台` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 24556 | `滗` | diversity: in 240 documents, 0.13 of the 1,824 occurrences' random spread (threshold 0.2); shape: length 1 |
| 24837 | `彩毒胆` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 24852 | `彩乐` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 24878 | `诈骗案` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 25322 | `哈萨克斯坦共和国` | diversity: in 40 documents, 0.02 of the 1,744 occurrences' random spread (threshold 0.2); shape: length 8; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 25369 | `中奖率` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 25379 | `秒速` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 26132 | `江晨` | diversity: in 68 documents, 0.04 of the 1,665 occurrences' random spread (threshold 0.2) |
| 26322 | `华宇` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 26346 | `李善长` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 26906 | `蛋蛋微信` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 27482 | `今期` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 28281 | `奥丁` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 28304 | `王小强` | diversity: in 135 documents, 0.09 of the 1,484 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 28305 | `知名企业` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 28573 | `排列三` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 28813 | `左莫` | diversity: in 84 documents, 0.06 of the 1,445 occurrences' random spread (threshold 0.2) |
| 28911 | `莫浩然` | diversity: in 27 documents, 0.02 of the 1,439 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29140 | `发起人` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29320 | `文在寅` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29376 | `曾仕强` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29513 | `标线` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29647 | `债转股` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29880 | `彩单` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29965 | `新大陆` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 29995 | `一点红` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 30091 | `青田` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 30196 | `安全区` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 30272 | `肖易` | diversity: in 31 documents, 0.02 of the 1,342 occurrences' random spread (threshold 0.2) |
| 30379 | `加征` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 30435 | `海军陆战队` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 31025 | `磁珠` | diversity: in 181 documents, 0.14 of the 1,294 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 31299 | `保护主义` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 31428 | `浮生` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 31434 | `莉雅` | diversity: in 237 documents, 0.19 of the 1,270 occurrences' random spread (threshold 0.2) |
| 31475 | `萧奇` | diversity: in 101 documents, 0.08 of the 1,267 occurrences' random spread (threshold 0.2) |

_467 more in the flags sidecar._

Reviewed decisions applied in the window: 5,822 (keep 4,052, drop 1,770); review merges: 26.
