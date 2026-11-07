# Review report: zh (full)

- Ranking score: `frequency`; 148,714 candidate lemmas ranked.
- Tokens counted: 818,620,585 in 1,049,585 documents, 120 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_zh` 1.6.4 (sha256 `2840ae8dc7e00290`); fallback `backend`, units on; honeyeater `259e4dd56192`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-zh | 119 | 1,047,831 | 22,259,371 | 818,272,668 | alpha 1,517,648, exact_dup 2,369,284, gap 421,516, langid 1,551,295, length 495,812, near_dup 294,170, traditional 211,507, traditional_doc 221,290 |
| tatoeba-cmn | 1 | 1,754 | 49,067 | 347,917 | alpha 87, gap 6, length 21, near_dup 348, traditional 39,719 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 11,238,653. Sentences: 41,099,079.

## Units

Counted occurrences by kind: compound 298,935 (0.04%), compound1 4,941,046 (0.60%), construction 3,957,373 (0.48%), phrase 3,226,623 (0.39%), word 806,196,608 (98.48%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 4,898 | 5,241,152 |
| construction | 14 | 3,957,374 |
| phrase | 119 | 3,226,623 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `点头` | 129,767 | 72,343 | 847 |
| `说话` | 129,696 | 79,626 | 854 |
| `担心` | 105,128 | 74,467 | 1033 |
| `报名` | 85,770 | 26,792 | 1262 |
| `开口` | 83,730 | 47,200 | 1295 |
| `毕业` | 63,757 | 36,604 | 1656 |
| `摇头` | 63,292 | 44,628 | 1671 |
| `回家` | 58,100 | 39,623 | 1813 |
| `放心` | 56,765 | 45,616 | 1852 |
| `吃饭` | 54,656 | 34,771 | 1909 |
| `结婚` | 52,071 | 28,444 | 1982 |
| `抬头` | 46,811 | 35,734 | 2169 |
| `动手` | 42,568 | 30,436 | 2344 |
| `受伤` | 42,234 | 30,897 | 2357 |
| `帮忙` | 37,675 | 28,586 | 2593 |
| `回头` | 37,078 | 28,573 | 2629 |
| `怎么回事` | 34,787 | 25,640 | 2758 |
| `报警` | 33,307 | 16,708 | 2846 |
| `生气` | 32,670 | 23,542 | 2893 |
| `离婚` | 32,599 | 14,299 | 2899 |
| `睡觉` | 31,789 | 21,606 | 2970 |
| `深圳市` | 31,517 | 15,761 | 2994 |
| `低头` | 30,719 | 24,191 | 3051 |
| `见面` | 30,161 | 23,705 | 3097 |
| `用力` | 29,088 | 20,861 | 3190 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `被 + 动词` | 1,436,681 | 453,541 | 54 |
| `把 + 名词 + 动词` | 1,200,829 | 437,847 | 70 |
| `动词 + 得 + 补语` | 498,576 | 227,827 | 177 |
| `动词 + 得/不 + 补语` | 254,066 | 160,457 | 395 |
| `比 + 名词 + 形容词` | 240,426 | 161,562 | 427 |
| `是…的` | 229,766 | 156,243 | 453 |
| `要…了` | 62,314 | 50,483 | 1697 |
| `动词 + 得/不 + 起` | 16,401 | 14,456 | 4936 |
| `动词 + 得/不 + 动` | 8,219 | 7,515 | 8123 |
| `动词 + 得/不 + 过` | 4,262 | 4,077 | 12878 |
| `动词 + 得/不 + 下` | 3,971 | 3,738 | 13526 |
| `〜来〜去` | 1,783 | 1,676 | 23172 |
| `快…了` | 78 | 76 | 142329 |
| `就要…了` | 2 | 2 | - |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `在〜中` | 663,047 | 338,435 | 137 |
| `在〜下` | 266,804 | 183,040 | 367 |
| `虽然…但` | 172,600 | 112,219 | 627 |
| `如果…就` | 144,375 | 102,120 | 769 |
| `当…时` | 97,375 | 69,115 | 1097 |
| `尤其是` | 83,738 | 68,132 | 1294 |
| `以〜为〜` | 80,459 | 61,276 | 1348 |
| `只要…就` | 79,894 | 64,216 | 1359 |
| `对于〜来说` | 76,636 | 58,912 | 1409 |
| `像〜一样` | 62,007 | 48,572 | 1708 |
| `看起来` | 61,953 | 45,961 | 1710 |
| `从〜开始` | 59,379 | 50,621 | 1775 |
| `在…的时候` | 58,984 | 47,633 | 1788 |
| `对〜来说` | 52,683 | 43,341 | 1967 |
| `不是…而是` | 51,144 | 43,641 | 2015 |
| `虽然…但是` | 45,974 | 35,211 | 2202 |
| `和〜一样` | 42,170 | 35,584 | 2361 |
| `就算…也` | 41,063 | 33,030 | 2413 |
| `在〜上` | 40,774 | 35,860 | 2425 |
| `打电话` | 39,934 | 27,106 | 2465 |
| `即使…也` | 39,839 | 32,433 | 2476 |
| `不仅…还` | 39,665 | 35,197 | 2482 |
| `连…都` | 38,081 | 32,858 | 2568 |
| `和〜一起` | 38,046 | 31,492 | 2569 |
| `特别是` | 34,752 | 30,910 | 2759 |

## Co-occurrence (association) table

42,843,517 tokens, 2,288,075 sentences. After merging and dropping items seen fewer than 5 times: 1,909,879 items (unigrams, UPOS votes, n-grams, pairs); 1,543,402 n-grams and pairs scored (n2 809,424, n3 541,711, n4 192,267). Shipped: 400,000 rows, 8.0 MB gzipped (`zh.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`zh.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `一 个` |  | 123,115 | 29,075 | 4.83 | 0.57 | 663,520 |  |
| 2 | n | `来 的` |  | 23,300 | 11,594 | 14.33 | 1.32 | 462,980 |  |
| 3 | n | `过 来` |  | 15,988 | 7,679 | 18.56 | 1.63 | 414,704 |  |
| 4 | n | `来 了` |  | 15,905 | 8,405 | 15.44 | 1.36 | 340,817 |  |
| 5 | n | `来 到` |  | 7,680 | 4,974 | 16.05 | 1.29 | 171,157 |  |
| 6 | n | `很 多` |  | 23,032 | 12,230 | 6.04 | 0.56 | 156,372 |  |
| 7 | n | `不 敢` |  | 7,839 | 5,041 | 13.95 | 1.12 | 151,787 |  |
| 8 | n | `看 到` |  | 26,481 | 12,345 | 5.04 | 0.47 | 141,506 |  |
| 9 | n | `来 看` |  | 6,211 | 4,484 | 16.37 | 1.28 | 141,251 |  |
| 10 | n | `看 着` |  | 24,422 | 8,768 | 5.27 | 0.49 | 138,204 |  |
| 11 | n | `不 会` |  | 29,484 | 14,181 | 4.37 | 0.42 | 130,163 |  |
| 12 | n | `不 能` |  | 26,058 | 13,675 | 4.44 | 0.42 | 117,874 |  |
| 13 | n | `一 步` |  | 5,197 | 3,603 | 16.34 | 1.26 | 117,772 |  |
| 14 | n | `进 来` |  | 4,388 | 2,879 | 18.32 | 1.38 | 112,185 |  |
| 15 | n | `一 条` |  | 6,733 | 4,627 | 11.79 | 0.93 | 110,108 |  |
| 16 | n | `传 来` |  | 3,848 | 2,699 | 19.65 | 1.46 | 106,607 |  |
| 17 | n | `两 个` |  | 19,990 | 10,164 | 5.00 | 0.45 | 106,400 |  |
| 18 | n | `到 了` |  | 36,538 | 14,360 | 3.22 | 0.32 | 104,215 |  |
| 19 | n | `都 是` |  | 31,294 | 15,336 | 3.57 | 0.34 | 104,096 |  |
| 20 | n | `也 是` |  | 35,121 | 16,035 | 3.28 | 0.32 | 102,640 |  |
| 21 | n | `不 知道` |  | 18,148 | 9,410 | 5.06 | 0.45 | 99,251 |  |
| 22 | n | `一 声` |  | 14,711 | 6,717 | 5.64 | 0.49 | 98,178 |  |
| 23 | n | `一 种` |  | 20,689 | 11,237 | 4.48 | 0.41 | 95,502 |  |
| 24 | n | `正 是` |  | 5,329 | 3,959 | 12.79 | 0.99 | 94,539 |  |
| 25 | n | `更 多` |  | 13,357 | 8,591 | 6.14 | 0.53 | 91,602 |  |
| 26 | n | `还 有` |  | 17,285 | 10,797 | 4.60 | 0.41 | 80,669 |  |
| 27 | n | `一 次` |  | 17,750 | 9,906 | 4.41 | 0.39 | 80,059 |  |
| 28 | n | `年 来` |  | 3,613 | 2,847 | 15.95 | 1.18 | 80,018 |  |
| 29 | n | `心 中` |  | 10,077 | 5,023 | 6.74 | 0.56 | 79,183 |  |
| 30 | n | `想 到` |  | 14,467 | 7,780 | 5.05 | 0.44 | 76,629 |  |
| 31 | n | `句 话` |  | 6,211 | 3,877 | 9.69 | 0.76 | 76,184 |  |
| 32 | n | `只 有` |  | 13,546 | 8,924 | 5.04 | 0.43 | 71,719 |  |
| 33 | n | `带 着` |  | 9,838 | 5,875 | 6.30 | 0.52 | 70,603 |  |
| 34 | n | `个 人` |  | 21,379 | 9,551 | 3.59 | 0.33 | 70,205 |  |
| 35 | n | `听 到` |  | 10,508 | 5,755 | 5.86 | 0.49 | 68,737 |  |
| 36 | n | `上 来` |  | 3,282 | 2,499 | 15.04 | 1.10 | 68,497 |  |
| 37 | n | `几 个` |  | 12,160 | 7,045 | 5.21 | 0.44 | 68,356 |  |
| 38 | n | `脸 上` |  | 8,833 | 4,801 | 6.58 | 0.54 | 68,004 |  |
| 39 | n | `只 能` |  | 10,461 | 7,063 | 5.75 | 0.48 | 65,406 |  |
| 40 | n | `万 元` |  | 6,834 | 2,361 | 7.93 | 0.63 | 64,365 |  |
| 41 | n | `不 少` |  | 9,858 | 6,553 | 5.37 | 0.44 | 58,940 |  |
| 42 | n | `过程 中` |  | 6,608 | 4,428 | 7.25 | 0.57 | 57,885 |  |
| 43 | n | `收 到` |  | 2,927 | 1,951 | 14.19 | 1.03 | 57,633 |  |
| 44 | n | `很 快` |  | 7,186 | 4,882 | 6.62 | 0.53 | 54,302 |  |
| 45 | n | `亿 元` |  | 4,957 | 1,773 | 8.85 | 0.68 | 54,009 |  |
| 46 | n | `才 能` |  | 8,275 | 6,042 | 5.92 | 0.48 | 53,642 |  |
| 47 | n | `没 想 到` |  | 5,546 | 3,742 | 7.35 | 0.57 | 53,386 |  |
| 48 | n | `来 就` |  | 2,671 | 2,263 | 14.38 | 1.03 | 53,280 |  |
| 49 | n | `两 人` |  | 10,830 | 4,875 | 4.77 | 0.40 | 52,678 |  |
| 50 | n | `脚 步` |  | 1,815 | 1,450 | 20.77 | 1.43 | 52,671 |  |

### Verb pairs in the queue

_none_

## Rank shifts against the live snapshot (`reference/lemmas/zh.json`)

Live list 40,069 lemmas, this build 148,714; 39,962 shared. Spearman rank correlation on the shared lemmas 1.000; median rank ratio 1.00x.
Overlap of this build's top-k with the live top-k: top 1,000 100.0%, top 5,000 100.0%, top 20,000 99.9%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `人家#rénjiā` | 3591 | 3209 | -382 |
| `卡#kǎ` | 1636 | 1296 | -340 |
| `空#kōng` | 1846 | 1507 | -339 |
| `落#là` | 1399 | 1111 | -288 |
| `背#bèi` | 1658 | 1407 | -251 |
| `假#jià` | 3489 | 3308 | -181 |
| `松#loose` | 2844 | 2687 | -157 |
| `游#swim` | 1236 | 1128 | -108 |
| `入#comp` | 428 | 334 | -94 |
| `光#guāng` | 977 | 918 | -59 |
| `签#sign` | 3331 | 3282 | -49 |
| `坏#huài` | 1766 | 1721 | -45 |
| `烟#tobacco` | 2306 | 2270 | -36 |
| `冲#rush` | 997 | 962 | -35 |
| `倒#dǎo` | 945 | 911 | -34 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `大陆` | 1588 | 1594 | +6 |
| `机制` | 1340 | 1344 | +4 |
| `危险` | 1339 | 1343 | +4 |
| `忽然` | 1338 | 1342 | +4 |
| `总理` | 4281 | 4284 | +3 |
| `英文` | 3634 | 3637 | +3 |
| `精英` | 3330 | 3333 | +3 |
| `体会` | 3329 | 3332 | +3 |
| `平方米` | 3328 | 3331 | +3 |
| `浏览` | 3327 | 3330 | +3 |
| `权力` | 3326 | 3329 | +3 |
| `出色` | 3325 | 3328 | +3 |
| `闪烁` | 3324 | 3327 | +3 |
| `错过` | 3323 | 3326 | +3 |
| `别说` | 3322 | 3325 | +3 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `耳边` | 5001 | 5000 | -1 |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `卡#zhòng` | 4641 | - | - |

## Ported frequer checks

### Form-ratio outliers (190)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4 | `一` | 10,540,526 | median form 2000.5; `一` 9,548,464 (4773x) |
| 16 | `你` | 3,502,239 | median form 2891; `你` 3,498,471 (1210x) |
| 84 | `已经` | 1,024,090 | median form 766; `已经` 1,023,232 (1336x) |
| 132 | `十` | 689,426 | median form 68; `10` 470,310 (6916x), `十` 218,736 (3217x) |
| 183 | `十一` | 489,437 | median form 13.5; `11` 459,179 (34013x), `十一` 30,083 (2228x) |
| 216 | `九` | 433,026 | median form 188; `9` 269,261 (1432x) |
| 299 | `十二` | 319,410 | median form 35.5; `12` 273,008 (7690x), `十二` 46,317 (1305x) |
| 328 | `二十` | 299,833 | median form 7; `20` 248,166 (35452x), `二十` 51,620 (7374x) |
| 400 | `组织` | 252,088 | median form 63; `组织` 252,019 (4000x) |
| 516 | `为什么` | 202,772 | median form 8.5; `为什么` 202,753 (23853x) |
| 714 | `十八` | 154,283 | median form 5.5; `18` 120,369 (21885x), `十八` 33,901 (6164x) |
| 721 | `越来越` | 152,965 | median form 20.5; `越来越` 152,919 (7459x) |
| 800 | `加` | 139,512 | median form 3; `加` 139,508 (46503x) |
| 804 | `十三` | 138,879 | median form 17; `13` 115,987 (6823x), `十三` 22,859 (1345x) |
| 840 | `互联网` | 131,320 | median form 11.5; `互联网` 131,289 (11416x) |
| 857 | `加拿大` | 128,990 | median form 7; `加拿大` 128,972 (18425x) |
| 994 | `二十四` | 109,758 | median form 13; `24` 105,277 (8098x) |
| 1000 | `消费者` | 109,037 | median form 18; `消费者` 109,006 (6056x) |
| 1017 | `二十五` | 107,095 | median form 3; `25` 104,418 (34806x) |
| 1082 | `十九` | 99,389 | median form 3; `19` 84,613 (28204x), `十九` 14,768 (4923x) |
| 1094 | `团` | 98,097 | median form 3; `团` 98,093 (32698x) |
| 1137 | `怎么样` | 94,231 | median form 11; `怎么样` 94,205 (8564x) |
| 1168 | `二十一` | 92,085 | median form 2; `21` 89,001 (44500x), `二十一` 3,080 (1540x) |
| 1256 | `色` | 86,291 | median form 14; `色` 86,276 (6163x) |
| 1364 | `办公室` | 79,544 | median form 3.5; `办公室` 79,535 (22724x) |

_165 more not shown._

### Singular/plural mismatch (0)

Lemma looks like a plural whose stripped form maps to another listed lemma.

_none_

### Lemma consistency (2)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 2176 | `人家` | 46,636 | alone, `人家` lemmatises to `人家#rénjiā` (rank 3,209) |
| 9022 | `某某` | 7,130 | alone, `某某` lemmatises to `某` (rank 485) |

### Short lemmas (1,620)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `的` | 41,861,315 | `的` -> `的` |
| 3 | `是` | 11,641,221 | `是` -> `是` |
| 4 | `一` | 10,540,526 | `一` -> `一`, `1` -> `一`, `①` -> `一`, `I` -> `?`, `Ⅰ` -> `?` |
| 5 | `在` | 8,330,091 | `在` -> `在` |
| 6 | `不` | 7,390,384 | `不` -> `不` |
| 7 | `个` | 6,128,444 | `个` -> `个` |
| 8 | `这` | 5,687,698 | `这` -> `这` |
| 9 | `和` | 4,804,311 | `和` -> `和` |
| 10 | `有` | 4,757,159 | `有` -> `有` |
| 11 | `我` | 4,671,933 | `我` -> `我` |
| 12 | `就` | 4,452,756 | `就` -> `就` |
| 13 | `也` | 4,168,886 | `也` -> `也` |
| 14 | `人` | 3,836,089 | `人` -> `人` |
| 15 | `他` | 3,786,582 | `他` -> `他` |
| 16 | `你` | 3,502,239 | `你` -> `你`, `伱` -> `伱`, `妳` -> `妳` |
| 19 | `都` | 3,046,451 | `都` -> `都` |
| 21 | `会` | 2,716,730 | `会` -> `会` |
| 24 | `年` | 2,401,716 | `年` -> `年`, `年#` -> `?` |
| 25 | `多` | 2,384,353 | `多` -> `多` |
| 26 | `对` | 2,296,842 | `对` -> `对` |
| 27 | `要` | 2,222,554 | `要` -> `要` |
| 28 | `能` | 2,180,104 | `能` -> `能` |
| 29 | `说` | 2,168,163 | `说` -> `说` |
| 31 | `很` | 2,100,276 | `很` -> `很` |
| 33 | `那` | 2,074,102 | `那` -> `那` |

_1,595 more not shown._

### Case merges (0)

Non-lowercase lemmas, with the lowercase twin where one is listed.

_none_

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 758 (75.8%).

Ours only: `彩`, `时时`, `被 + 动词`, `把 + 名词 + 动词`, `十`, `在〜中`, `百分之`, `前`, `重庆`, `动词 + 得 + 补语`, `十一`, `儿#r`, `说道`, `二十八`, `幸运`, `声`, `有限公司`, `林`, `周#week`, `软件`, `的话`, `十二`, `开奖`, `脸`, `眼`

wordfreq only: `〇〇〇〇`, `〇〇〇`, `政治`, `第`, `人民`, `运动`, `自由`, `委员会`, `人口`, `民主`, `事件`, `零点零`, `县`, `总统`, `战争`, `照片`, `时期`, `故事`, `欧洲`, `举行`, `艺术`, `独立`, `亚洲`, `人类`, `制`

## Foreign-word candidates

_none_

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 56 | `中国` | 1,408,336 | PROPN 98%, capitalised forms 0% |
| 138 | `美国` | 650,605 | PROPN 99%, capitalised forms 0% |
| 142 | `北京` | 608,473 | PROPN 100%, capitalised forms 0% |
| 168 | `重庆` | 518,945 | PROPN 97%, capitalised forms 0% |
| 201 | `王` | 458,970 | PROPN 100%, capitalised forms 0% |
| 261 | `林` | 369,451 | PROPN 99%, capitalised forms 0% |
| 264 | `香港` | 367,355 | PROPN 100%, capitalised forms 0% |
| 354 | `李` | 279,566 | PROPN 100%, capitalised forms 0% |
| 436 | `韩国` | 236,182 | PROPN 100%, capitalised forms 0% |
| 458 | `上海` | 228,682 | PROPN 100%, capitalised forms 0% |
| 502 | `台湾` | 207,073 | PROPN 97%, capitalised forms 0% |
| 512 | `日本` | 203,928 | PROPN 98%, capitalised forms 0% |
| 532 | `杨` | 198,396 | PROPN 99%, capitalised forms 0% |
| 606 | `广东` | 177,584 | PROPN 100%, capitalised forms 0% |
| 642 | `培训` | 167,723 | PROPN 76%, capitalised forms 0% |
| 654 | `秦` | 166,260 | PROPN 97%, capitalised forms 0% |
| 663 | `云` | 164,910 | PROPN 91%, capitalised forms 0% |
| 734 | `腾讯` | 150,759 | PROPN 100%, capitalised forms 0% |
| 822 | `安装` | 134,739 | PROPN 56%, capitalised forms 0% |
| 857 | `加拿大` | 128,990 | PROPN 100%, capitalised forms 0% |
| 858 | `走势图` | 128,989 | PROPN 99%, capitalised forms 0% |
| 884 | `英国` | 124,643 | PROPN 95%, capitalised forms 0% |
| 931 | `平` | 118,236 | PROPN 58%, capitalised forms 0% |
| 1007 | `微信` | 108,297 | PROPN 100%, capitalised forms 0% |
| 1023 | `亚洲` | 106,301 | PROPN 95%, capitalised forms 0% |

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
| `除了…外` | 6367 | 4750 | -1,617 | 12,020 | 11,243 | 0.990 | 0.039 |
| `违者` | 5433 | 3827 | -1,606 | 14,832 | 14,588 | 0.991 | 0.035 |
| `好不容易` | 6517 | 4955 | -1,562 | 11,602 | 10,623 | 0.988 | 0.048 |
| `备受` | 6093 | 4555 | -1,538 | 12,726 | 11,873 | 0.991 | 0.035 |
| `只有…才` | 5922 | 4396 | -1,526 | 13,219 | 12,395 | 0.990 | 0.040 |
| `彩霸王` | 2675 | 35327 | +32,652 | 36,989 | 717 | 0.957 | 0.172 |
| `曾道人` | 2065 | 32561 | +30,496 | 50,469 | 812 | 0.957 | 0.172 |
| `刘伯温` | 488 | 30236 | +29,748 | 214,585 | 907 | 0.957 | 0.175 |
| `九五至尊` | 4116 | 28560 | +24,444 | 21,383 | 985 | 0.958 | 0.171 |
| `赛马会` | 1472 | 20723 | +19,251 | 74,464 | 1,563 | 0.957 | 0.173 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `大事` | 4165 | 4120 | -45 | 21,151 | 18,005 | 0.992 | 0.033 |
| `偶尔` | 4168 | 4125 | -43 | 21,123 | 18,371 | 0.992 | 0.033 |
| `开玩笑` | 4991 | 4949 | -42 | 16,644 | 14,196 | 0.992 | 0.033 |
| `唯有` | 4978 | 4940 | -38 | 16,706 | 14,087 | 0.991 | 0.034 |
| `另一方面` | 4985 | 4947 | -38 | 16,668 | 15,258 | 0.991 | 0.033 |
| `海关` | 4957 | 5413 | +456 | 16,789 | 7,534 | 0.870 | 0.164 |
| `胖` | 3440 | 3896 | +456 | 27,084 | 10,857 | 0.840 | 0.232 |
| `温` | 4411 | 4723 | +312 | 19,563 | 9,098 | 0.894 | 0.147 |
| `唯美` | 4110 | 4286 | +176 | 21,416 | 5,060 | 0.930 | 0.285 |
| `枫` | 2630 | 2769 | +139 | 37,827 | 4,608 | 0.922 | 0.145 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `大事` | 4165 | 4120 | -45 | 21,151 | 18,005 | 0.992 | 0.033 |
| `偶尔` | 4168 | 4125 | -43 | 21,123 | 18,371 | 0.992 | 0.033 |
| `开玩笑` | 4991 | 4949 | -42 | 16,644 | 14,196 | 0.992 | 0.033 |
| `唯有` | 4978 | 4940 | -38 | 16,706 | 14,087 | 0.991 | 0.034 |
| `另一方面` | 4985 | 4947 | -38 | 16,668 | 15,258 | 0.991 | 0.033 |
| `海关` | 4957 | 5414 | +457 | 16,789 | 7,534 | 0.870 | 0.164 |
| `胖` | 3440 | 3896 | +456 | 27,084 | 10,857 | 0.840 | 0.232 |
| `温` | 4411 | 4725 | +314 | 19,563 | 9,098 | 0.894 | 0.147 |
| `唯美` | 4110 | 4288 | +178 | 21,416 | 5,060 | 0.930 | 0.285 |
| `枫` | 2630 | 2769 | +139 | 37,827 | 4,608 | 0.922 | 0.145 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `尽可能` | 4832 | 4705 | -127 | 17,293 | 14,962 | 0.992 | 0.033 |
| `何时` | 4913 | 4786 | -127 | 16,939 | 14,786 | 0.992 | 0.030 |
| `广阔` | 5113 | 4996 | -117 | 16,092 | 14,443 | 0.992 | 0.032 |
| `另一方面` | 4985 | 4869 | -116 | 16,668 | 15,258 | 0.991 | 0.033 |
| `感叹` | 5108 | 4994 | -114 | 16,127 | 14,285 | 0.992 | 0.033 |
| `唯美` | 4110 | 5049 | +939 | 21,416 | 5,060 | 0.930 | 0.285 |
| `头像` | 2945 | 3567 | +622 | 32,640 | 4,583 | 0.938 | 0.252 |
| `胖` | 3440 | 4028 | +588 | 27,084 | 10,857 | 0.840 | 0.232 |
| `九五至尊` | 4116 | 4524 | +408 | 21,383 | 985 | 0.958 | 0.171 |
| `海关` | 4957 | 5364 | +407 | 16,789 | 7,534 | 0.870 | 0.164 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `违者` | 5433 | 4582 | -851 | 14,832 | 14,588 | 0.991 | 0.035 |
| `除此之外` | 5741 | 4937 | -804 | 13,791 | 12,814 | 0.991 | 0.034 |
| `旨在` | 5691 | 4953 | -738 | 13,954 | 12,542 | 0.990 | 0.039 |
| `一旦…就` | 5534 | 4804 | -730 | 14,423 | 13,324 | 0.992 | 0.033 |
| `毫不` | 5118 | 4391 | -727 | 16,051 | 14,686 | 0.991 | 0.036 |
| `彩霸王` | 2675 | 10088 | +7,413 | 36,989 | 717 | 0.957 | 0.172 |
| `九五至尊` | 4116 | 10984 | +6,868 | 21,383 | 985 | 0.958 | 0.171 |
| `曾道人` | 2065 | 8525 | +6,460 | 50,469 | 812 | 0.957 | 0.172 |
| `赛马会` | 1472 | 5781 | +4,309 | 74,464 | 1,563 | 0.957 | 0.173 |
| `刘伯温` | 488 | 4786 | +4,298 | 214,585 | 907 | 0.957 | 0.175 |



## Junk-filter heuristics

Rules on: diversity, citation, shape, propn_band; accent merges at ratio None. Window: the 44,750 ranked lemmas (after the exclusion list) that fill the top 40,000. Actions: keep 29,063, number-drop 340, review-drop 4,410, review-keep 10,937.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band | propn_usage |
|---|---:|---:|---:|---:|---:|---:|
| diversity | 732 | 0 | 0 | 14 | 194 | 0 |
| citation | 0 | 32 | 0 | 1 | 0 | 0 |
| foreign | 0 | 0 | 0 | 0 | 0 | 0 |
| shape | 14 | 1 | 0 | 924 | 44 | 0 |
| propn_band | 194 | 0 | 0 | 44 | 5,248 | 0 |
| propn_usage | 0 | 0 | 0 | 0 | 0 | 0 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 0.

### Low diversity

Documents reached / documents expected at random, below 0.2 (frequency >= 20): 732 in the window. For comparison, each log2-frequency band's 2nd percentile: 64-127: 0.06, 128-255: 0.09, 256-511: 0.13, 512-1023: 0.18, 1024-2047: 0.21, 2048-4095: 0.23, 4096-8191: 0.26, 8192-16383: 0.23, 16384-32767: 0.27, 32768-65535: 0.22, 65536-131071: 0.26, 131072-262143: 0.2, 262144-524287: 0.21.

Examples: `彩` (35), `时时` (36), `重庆` (168), `二十八` (231), `幸运` (239), `开奖` (308), `论坛` (389), `刘伯温` (488), `技巧` (558), `秦` (660), `预测` (710), `腾讯` (742), `蛋蛋` (747), `叶` (752), `传奇` (816), `投注` (834), `加拿大` (868), `走势图` (869), `彩票` (1181), `陆` (1232), `新疆` (1253), `飞艇` (1442), `楚` (1462), `赛马会` (1472), `玩法` (1487), `农场` (1526), `修士` (1702), `赛车` (1730), `胆` (1805), `娱乐城` (1863), `五星` (1949), `肖` (1950), `萧` (1996), `曾道人` (2065), `私服` (2100), `遗漏` (2106), `图表` (2179), `二手` (2332), `白癜风` (2425), `龙虎` (2434)

### Accent merges (417)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `云湾` | `云` | 10,647 | review: merge |
| `一提的是` | `值得一提的是` | 6,691 | review: merge |
| `博会` | `进博会` | 4,238 | review: merge |
| `是否是` | `是否` | 3,080 | review: merge |
| `显露出` | `显露` | 2,817 | review: merge |
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
| `折射出` | `折射` | 1,617 | review: merge |
| `蹦出` | `蹦` | 1,256 | review: merge |
| `大部份` | `大部分` | 1,142 | review: merge |
| `大打出` | `大打出手` | 1,028 | review: merge |
| `飚` | `飙` | 1,119 | review: merge |
| `丛林中` | `丛林` | 979 | review: merge |
| `交组织` | `交织` | 1,067 | review: merge |
| `伱` | `你` | 877 | review: merge |
| `挑选出` | `挑选` | 982 | review: merge |
| `特有的` | `特有` | 949 | review: merge |
| `谴` | `天谴` | 880 | review: merge |
| `讲话中` | `讲话` | 1,100 | review: merge |
| `幻化成` | `幻化` | 921 | review: merge |
| `片狼藉` | `一片狼藉` | 859 | review: merge |
| `淬` | `淬火` | 868 | review: merge |
| `基丹` | `筑基丹` | 761 | review: merge |
| `编组织` | `编织` | 733 | review: merge |
| `卓` | `安卓` | 20,275 | review: merge |
| `企` | `企业` | 21,889 | review: merge |
| `无论是` | `无论` | 18,162 | review: merge |
| `来源于` | `来源` | 13,515 | review: merge |
| `伴随着` | `伴随` | 11,712 | review: merge |
| `手车` | `二手车` | 8,289 | review: merge |
| `流露出` | `流露` | 8,879 | review: merge |
| `自已` | `自己` | 7,375 | review: merge |
| `淡淡的` | `淡淡` | 6,384 | review: merge |
| `不锈` | `不锈钢` | 8,165 | review: merge |
| `不论是` | `不论` | 6,793 | review: merge |
| `前所未` | `前所未有` | 6,843 | review: merge |
| `离不` | `离不开` | 7,244 | review: merge |
| `忍不` | `忍不住` | 6,110 | review: merge |
| `捂着` | `捂` | 5,986 | review: merge |
| `与众` | `与众不同` | 6,955 | review: merge |
| `好象` | `好像` | 6,182 | review: merge |
| `散发出` | `散发` | 5,450 | review: merge |
| `无表情` | `面无表情` | 5,524 | review: merge |
| `条龙` | `一条龙` | 7,994 | review: merge |
| `法定代表` | `法定代表人` | 5,490 | review: merge |
| `元化` | `多元化` | 5,663 | review: merge |
| `狐` | `狐狸` | 6,132 | review: merge |
| `步声` | `脚步声` | 4,858 | review: merge |
| `党和` | `党` | 6,338 | review: merge |
| `交待` | `交代` | 4,722 | review: merge |
| `展现出` | `展现` | 4,608 | review: merge |
| `回过` | `回` | 4,515 | review: merge |
| `帐户` | `账户` | 4,884 | review: merge |
| `以为然` | `不以为然` | 4,248 | review: merge |
| `粘膜` | `黏膜` | 4,628 | review: merge |
| `分出` | `分` | 4,157 | review: merge |
| `大不` | `大不了` | 3,862 | review: merge |
| `成份` | `成分` | 4,112 | review: merge |
| `三板` | `新三板` | 5,533 | review: merge |
| `咬着牙` | `咬牙` | 3,721 | review: merge |
| `先容` | `介绍` | 4,004 | review: merge |
| `什` | `什么` | 3,838 | review: merge |
| `官方网` | `官方网站` | 8,564 | review: merge |
| `〜起` | `起` | 4,374 | review: merge |
| `指着` | `指` | 3,519 | review: merge |
| `黑龙` | `黑龙江` | 3,308 | review: merge |
| `在心上` | `放在心上` | 3,450 | review: merge |
| `一辈` | `一辈子` | 3,491 | review: merge |
| `拍了拍` | `拍` | 3,362 | review: merge |
| `在眼里` | `眼里` | 3,237 | review: merge |
| `询问道` | `询问` | 3,195 | review: merge |
| `楞` | `愣` | 3,100 | review: merge |
| `拍了` | `拍` | 3,098 | review: merge |
| `知不觉` | `不知不觉` | 3,025 | review: merge |
| `身分` | `身份` | 3,241 | review: merge |
| `年青` | `年轻` | 3,364 | review: merge |
| `高高在` | `高高在上` | 2,958 | review: merge |
| `妳` | `你` | 2,891 | review: merge |
| `角度看` | `角度` | 3,372 | review: merge |
| `污` | `污染` | 3,335 | review: merge |
| `呈现出` | `呈现` | 3,131 | review: merge |
| `生活中` | `生活` | 3,456 | review: merge |
| `碎机` | `破碎机` | 2,636 | review: merge |
| `双十` | `双十一` | 3,253 | review: merge |
| `动声色` | `不动声色` | 2,820 | review: merge |
| `蕴含着` | `蕴含` | 2,678 | review: merge |
| `随时随` | `随时随地` | 2,957 | review: merge |
| `婴幼` | `婴幼儿` | 2,730 | review: merge |
| `篇文章` | `文章` | 2,881 | review: merge |
| `显现出` | `显现` | 2,731 | review: merge |
| `壹` | `一` | 3,483 | review: merge |
| `聊着` | `聊` | 2,539 | review: merge |
| `锈钢` | `不锈钢` | 2,692 | review: merge |
| `以为意` | `不以为意` | 2,457 | review: merge |
| `就算是` | `就算` | 2,361 | review: merge |
| `座落` | `坐落` | 2,403 | review: merge |
| `机率` | `几率` | 2,919 | review: merge |
| `个劲` | `一个劲` | 2,423 | review: merge |
| `签定` | `签订` | 2,569 | review: merge |
| `免不` | `免不了` | 2,461 | review: merge |
| `哭笑` | `哭笑不得` | 2,347 | review: merge |
| `低着` | `低` | 2,377 | review: merge |
| `名副` | `名副其实` | 2,610 | review: merge |
| `半响` | `半晌` | 2,195 | review: merge |
| `实实在` | `实实在在` | 2,410 | review: merge |
| `部份` | `部分` | 2,343 | review: merge |
| `排名第` | `排名` | 2,261 | review: merge |
| `模版` | `模板` | 2,675 | review: merge |
| `党的` | `党` | 2,729 | review: merge |
| `迈着` | `迈` | 2,136 | review: merge |
| `打着` | `打` | 2,162 | review: merge |
| `回忆起` | `回忆` | 2,405 | review: merge |
| `浑身上` | `浑身上下` | 1,991 | review: merge |
| `前所未有的` | `前所未有` | 2,206 | review: merge |
| `份量` | `分量` | 2,206 | review: merge |
| `凝视着` | `凝视` | 1,984 | review: merge |
| `神祗` | `神祇` | 1,866 | review: merge |
| `永远都` | `永远` | 2,065 | review: merge |
| `是如此` | `如此` | 2,096 | review: merge |
| `迟早会` | `迟早` | 1,992 | review: merge |
| `无数道` | `无数` | 1,937 | review: merge |
| `殊不` | `殊不知` | 2,055 | review: merge |
| `视而` | `视而不见` | 2,066 | review: merge |
| `无奇` | `平平无奇` | 1,545 | review: merge |
| `暴露出` | `暴露` | 2,178 | review: merge |
| `现状及` | `现状` | 1,899 | review: merge |
| `笼罩着` | `笼罩` | 1,924 | review: merge |
| `代会` | `党代会` | 2,062 | review: merge |
| `容错过` | `错过` | 1,870 | review: merge |
| `建部` | `住建部` | 2,116 | review: merge |
| `开发新` | `开发` | 1,788 | review: merge |
| `很惨` | `惨` | 1,823 | review: merge |
| `多平方米` | `平方米` | 1,903 | review: merge |
| `地点点头` | `点点头` | 1,706 | review: merge |
| `热衷于` | `热衷` | 1,776 | review: merge |
| `暖暖的` | `暖暖` | 1,688 | review: merge |
| `随之而` | `随之而来` | 1,782 | review: merge |
| `处处长` | `处长` | 2,014 | review: merge |
| `话下` | `不在话下` | 1,648 | review: merge |
| `个方面` | `方面` | 1,701 | review: merge |
| `更让` | `让` | 1,750 | review: merge |
| `很淡` | `淡` | 1,685 | review: merge |
| `磨擦` | `摩擦` | 1,605 | review: merge |
| `回头一` | `回头一看` | 1,595 | review: merge |
| `类药物` | `药物` | 1,656 | review: merge |
| `惟有` | `唯有` | 1,703 | review: merge |
| `型基金` | `基金` | 1,839 | review: merge |
| `发症` | `并发症` | 1,717 | review: merge |
| `自来` | `自来水` | 1,591 | review: merge |
| `以赴` | `全力以赴` | 1,578 | review: merge |
| `彷佛` | `仿佛` | 1,696 | review: merge |
| `澡` | `洗澡` | 1,526 | review: merge |
| `年青人` | `年轻人` | 1,714 | review: merge |
| `象是` | `像是` | 1,481 | review: merge |
| `各乡镇` | `乡镇` | 1,765 | review: merge |
| `薰` | `熏` | 1,737 | review: merge |
| `无天` | `无法无天` | 1,452 | review: merge |
| `积极向` | `积极向上` | 1,513 | review: merge |
| `中老` | `中老年` | 1,543 | review: merge |
| `处罚金` | `罚金` | 2,007 | review: merge |
| `零配` | `零配件` | 1,427 | review: merge |
| `最重` | `重` | 1,568 | review: merge |
| `座落在` | `坐落` | 1,318 | review: merge |
| `个环节` | `环节` | 1,513 | review: merge |
| `原有的` | `原有` | 1,543 | review: merge |
| `聊得` | `聊` | 1,446 | review: merge |
| `姊姊` | `姐姐` | 1,245 | review: merge |
| `届生` | `应届生` | 1,404 | review: merge |
| `摸样` | `模样` | 1,324 | review: merge |
| `声令下` | `一声令下` | 1,335 | review: merge |
| `香奈` | `香奈儿` | 1,485 | review: merge |
| `觉察到` | `觉察` | 1,402 | review: merge |
| `独有的` | `独有` | 1,393 | review: merge |
| `比不` | `比不上` | 1,352 | review: merge |
| `上用品` | `床上用品` | 1,412 | review: merge |
| `等奖` | `一等奖` | 1,588 | review: merge |
| `无限公司` | `有限公司` | 1,335 | review: merge |
| `闪耀着` | `闪耀` | 1,351 | review: merge |
| `名度` | `知名度` | 1,452 | review: merge |
| `肩负着` | `肩负` | 1,479 | review: merge |
| `舔着` | `舔` | 1,169 | review: merge |
| `挑出` | `挑` | 1,302 | review: merge |
| `贴着` | `贴` | 1,215 | review: merge |
| `以为是` | `自以为是` | 1,313 | review: merge |
| `好样` | `好样的` | 1,237 | review: merge |
| `胜区` | `风景名胜区` | 1,539 | review: merge |
| `天而降` | `从天而降` | 1,223 | review: merge |
| `乍一` | `乍一看` | 1,275 | review: merge |
| `暴光` | `曝光` | 1,231 | review: merge |
| `网路` | `网络` | 1,228 | review: merge |
| `八路` | `八路军` | 1,068 | review: merge |
| `抿着` | `抿` | 1,181 | review: merge |
| `卫健` | `卫健委` | 1,371 | review: merge |
| `汉兰` | `汉兰达` | 1,063 | review: merge |
| `丝一毫` | `一丝一毫` | 1,095 | review: merge |
| `图象` | `图像` | 1,373 | review: merge |
| `切不` | `切不可` | 1,178 | review: merge |
| `在技术` | `技术` | 1,250 | review: merge |
| `手把` | `把手` | 1,101 | review: merge |
| `符篆` | `符箓` | 1,073 | review: merge |
| `制做` | `制作` | 1,040 | review: merge |
| `字型` | `字体` | 1,115 | review: merge |
| `检查和` | `检查` | 1,184 | review: merge |
| `性皮炎` | `皮炎` | 1,236 | review: merge |
| `盘算着` | `盘算` | 1,115 | review: merge |
| `老人们` | `老人` | 1,298 | review: merge |
| `价实` | `货真价实` | 1,112 | review: merge |
| `交所` | `交易所` | 1,376 | review: merge |
| `存眷` | `关注` | 1,349 | review: merge |
| `总裁兼` | `总裁` | 1,333 | review: merge |
| `冒然` | `贸然` | 1,021 | review: merge |
| `透漏` | `透露` | 1,004 | review: merge |
| `唯品` | `唯品会` | 1,269 | review: merge |
| `并作` | `作` | 1,242 | review: merge |
| `眯着` | `眯` | 1,036 | review: merge |
| `地拉` | `拉` | 1,037 | review: merge |
| `丝毫不` | `丝毫` | 1,042 | review: merge |
| `货真` | `货真价实` | 1,085 | review: merge |
| `来不` | `来不及` | 1,001 | review: merge |
| `八蛋` | `王八蛋` | 1,022 | review: merge |
| `过份` | `过分` | 1,053 | review: merge |
| `惊心` | `惊心动魄` | 1,260 | review: merge |
| `连云` | `连云港` | 1,037 | review: merge |
| `掐着` | `掐` | 1,043 | review: merge |
| `凝炼` | `凝练` | 985 | review: merge |
| `地面积` | `面积` | 1,009 | review: merge |
| `柄剑` | `剑` | 960 | review: merge |
| `动地` | `惊天动地` | 1,045 | review: merge |
| `见识一下` | `见识` | 973 | review: merge |
| `恶梦` | `噩梦` | 1,141 | review: merge |
| `皂` | `肥皂` | 1,014 | review: merge |
| `睁一` | `睁一只眼闭一只眼` | 1,084 | review: merge |
| `地点头` | `点头` | 957 | review: merge |
| `定睛一` | `定睛` | 998 | review: merge |
| `更惨` | `惨` | 1,019 | review: merge |
| `件套` | `四件套` | 1,082 | review: merge |
| `粥样` | `动脉粥样硬化` | 1,140 | review: merge |
| `针锋` | `针锋相对` | 1,075 | review: merge |
| `化身为` | `化身` | 1,052 | review: merge |
| `拄着` | `拄` | 1,020 | review: merge |
| `息息` | `息息相关` | 1,048 | review: merge |
| `国家知识产权` | `国家知识产权局` | 1,124 | review: merge |
| `道菜` | `菜` | 1,009 | review: merge |
| `道工序` | `工序` | 1,023 | review: merge |
| `少不` | `少不了` | 992 | review: merge |
| `拔赛` | `选拔赛` | 1,122 | review: merge |
| `下无敌` | `天下无敌` | 928 | review: merge |
| `而语` | `不可同日而语` | 954 | review: merge |
| `不惯` | `看不惯` | 949 | review: merge |
| `保不` | `保不住` | 900 | review: merge |
| `闭一` | `睁一只眼闭一只眼` | 998 | review: merge |
| `丝不苟` | `一丝不苟` | 1,027 | review: merge |
| `口机` | `封口机` | 929 | review: merge |
| `工信` | `工信部` | 1,241 | review: merge |
| `家子` | `一家子` | 998 | review: merge |
| `副县` | `副县长` | 1,092 | review: merge |
| `火机` | `打火机` | 923 | review: merge |
| `屁颠` | `屁颠屁颠` | 974 | review: merge |
| `总的` | `总` | 959 | review: merge |
| `手握着` | `手握` | 863 | review: merge |
| `震得` | `震` | 886 | review: merge |
| `经意` | `不经意` | 954 | review: merge |
| `纳西` | `纳西族` | 791 | review: merge |
| `动了动` | `动` | 888 | review: merge |
| `政斧` | `政府` | 650 | review: merge |
| `令下` | `一声令下` | 874 | review: merge |
| `条线` | `线` | 896 | review: merge |
| `个脚印` | `脚印` | 978 | review: merge |
| `朵花` | `花` | 911 | review: merge |
| `稍安` | `稍安勿躁` | 868 | review: merge |
| `长白` | `长白山` | 908 | review: merge |
| `以上者` | `以上` | 879 | review: merge |
| `晕过` | `晕` | 862 | review: merge |
| `桌面上` | `桌面` | 870 | review: merge |
| `等不` | `等` | 882 | review: merge |
| `被扣` | `扣` | 1,095 | review: merge |
| `倍受` | `备受` | 917 | review: merge |
| `晋升为` | `晋升` | 931 | review: merge |
| `奉献给` | `奉献` | 949 | review: merge |
| `不单单是` | `不单单` | 875 | review: merge |
| `扛不` | `扛不住` | 915 | review: merge |
| `荡起` | `荡` | 860 | review: merge |
| `传授给` | `传授` | 878 | review: merge |
| `被称作` | `称作` | 857 | review: merge |
| `方米` | `平方米` | 892 | review: merge |
| `轰成` | `轰` | 815 | review: merge |
| `坐椅` | `座椅` | 748 | review: merge |
| `咧着` | `咧` | 859 | review: merge |
| `孕育出` | `孕育` | 886 | review: merge |
| `创造性地` | `创造性` | 968 | review: merge |
| `公积` | `公积金` | 758 | review: merge |
| `展露出` | `展露` | 849 | review: merge |
| `压抑着` | `压抑` | 860 | review: merge |
| `异想` | `异想天开` | 891 | review: merge |
| `沉迷于` | `沉迷` | 932 | review: merge |
| `涵义` | `含义` | 940 | review: merge |
| `个箭步` | `箭步` | 805 | review: merge |
| `掉落在` | `掉落` | 856 | review: merge |
| `很浓` | `浓` | 862 | review: merge |
| `事半功` | `事半功倍` | 867 | review: merge |
| `缠绕着` | `缠绕` | 790 | review: merge |
| `天开` | `异想天开` | 887 | review: merge |
| `不可同日` | `不可同日而语` | 814 | review: merge |
| `全方` | `全方位` | 882 | review: merge |
| `贴子` | `帖子` | 864 | review: merge |
| `庙里` | `庙` | 849 | review: merge |
| `真不愧是` | `不愧是` | 802 | review: merge |
| `赶不` | `赶不上` | 785 | review: merge |
| `可任意` | `任意` | 807 | review: merge |
| `推波` | `推波助澜` | 1,634 | review: merge |
| `国务` | `国务院` | 1,270 | review: merge |
| `视屏` | `视频` | 1,166 | review: merge |
| `农村部` | `农业农村部` | 1,165 | review: merge |
| `天三夜` | `三天三夜` | 1,103 | review: merge |
| `参考报` | `经济参考报` | 1,051 | review: merge |
| `乐福` | `乐福鞋` | 1,040 | review: merge |
| `蓝球` | `篮球` | 1,001 | review: merge |
| `安微` | `安徽` | 976 | review: merge |
| `金白银` | `真金白银` | 951 | review: merge |
| `创板` | `科创板` | 929 | review: merge |
| `纷歧` | `分歧` | 899 | review: merge |
| `保护部` | `环境保护部` | 882 | review: merge |
| `在首位` | `首位` | 866 | review: merge |
| `傍边` | `旁边` | 860 | review: merge |
| `凸显出` | `凸显` | 845 | review: merge |
| `悠闲地` | `悠闲` | 833 | review: merge |
| `社厅` | `人社厅` | 832 | review: merge |
| `板机` | `扳机` | 831 | review: merge |
| `分解成` | `分解` | 824 | review: merge |
| `小化` | `最小化` | 815 | review: merge |
| `那末` | `那么` | 815 | review: merge |
| `思惟` | `思维` | 811 | review: merge |
| `捐给` | `捐` | 807 | review: merge |
| `堪言` | `苦不堪言` | 805 | review: merge |
| `颠峰` | `巅峰` | 803 | review: merge |
| `一举一` | `一举一动` | 798 | review: merge |
| `中关` | `中关村` | 796 | review: merge |
| `挖掘出` | `挖掘` | 796 | review: merge |
| `挥出` | `挥` | 795 | review: merge |
| `极管` | `二极管` | 792 | review: merge |
| `气不打` | `气不打一处来` | 790 | review: merge |
| `奇艺` | `爱奇艺` | 789 | review: merge |
| `描绘出` | `描绘` | 788 | review: merge |
| `战成` | `战` | 782 | review: merge |
| `临走时` | `临走` | 780 | review: merge |
| `足不` | `足不出户` | 777 | review: merge |
| `苦不` | `苦不堪言` | 776 | review: merge |
| `脚色` | `角色` | 772 | review: merge |
| `涅盘` | `涅槃` | 771 | review: merge |
| `己经` | `已经` | 766 | review: merge |
| `一提` | `值得一提` | 764 | review: merge |
| `抢过` | `抢` | 763 | review: merge |
| `有志于` | `有志` | 763 | review: merge |
| `未办理` | `办理` | 763 | review: merge |
| `不逊于` | `不逊` | 758 | review: merge |
| `衬托出` | `衬托` | 756 | review: merge |
| `产于` | `产` | 755 | review: merge |
| `改编自` | `改编` | 754 | review: merge |
| `奥迪车` | `奥迪` | 751 | review: merge |
| `碗机` | `洗碗机` | 751 | review: merge |
| `迁往` | `迁` | 743 | review: merge |
| `出户` | `足不出户` | 742 | review: merge |
| `培育出` | `培育` | 910 | review: merge |
| `微信扫` | `微信` | 902 | review: merge |
| `华中科技` | `华中科技大学` | 880 | review: merge |
| `金九银` | `金九银十` | 803 | review: merge |
| `什幺` | `什么` | 797 | review: merge |
| `忍受着` | `忍受` | 770 | review: merge |
| `捂着脸` | `捂` | 765 | review: merge |
| `眯着眼` | `眯` | 758 | review: merge |
| `迄今已` | `迄今` | 758 | review: merge |
| `捕捉到` | `捕捉` | 754 | review: merge |
| `西安交通` | `西安交通大学` | 750 | review: merge |
| `耸了耸` | `耸` | 743 | review: merge |
| `惦记着` | `惦记` | 738 | review: merge |
| `伪装成` | `伪装` | 729 | review: merge |
| `新疆生产建设` | `新疆生产建设兵团` | 717 | review: merge |
| `广交` | `广交会` | 737 | review: merge |
| `噗哧` | `噗嗤` | 732 | review: merge |
| `桶金` | `第一桶金` | 729 | review: merge |
| `个劲儿` | `一个劲儿` | 725 | review: merge |
| `卡路` | `卡路里` | 725 | review: merge |
| `记忆里` | `记忆` | 725 | review: merge |
| `谈一` | `谈` | 724 | review: merge |
| `关健` | `关键` | 723 | review: merge |
| `奖得主` | `得主` | 723 | review: merge |
| `戴绿` | `戴绿帽` | 722 | review: merge |
| `无聊赖` | `百无聊赖` | 719 | review: merge |
| `不美观` | `美观` | 718 | review: merge |
| `唤出` | `唤` | 717 | review: merge |
| `老两` | `老两口` | 717 | review: merge |
| `轨制` | `双轨制` | 717 | review: merge |
| `三驾` | `三驾马车` | 716 | review: merge |
| `明眼` | `明眼人` | 716 | review: merge |
| `最优` | `优` | 4,033 | review: merge |
| `太重` | `重` | 3,330 | review: merge |
| `最差` | `差` | 2,524 | review: merge |
| `最远` | `远` | 1,351 | review: merge |
| `最深` | `深` | 1,186 | review: merge |
| `较晚` | `晚` | 983 | review: merge |
| `较佳` | `佳` | 928 | review: merge |
| `最惨` | `惨` | 896 | review: merge |
| `发贴` | `发帖` | 715 | review: merge |
| `真不错` | `不错` | 714 | review: merge |
| `啃着` | `啃` | 713 | review: merge |
| `提炼出` | `提炼` | 713 | review: merge |
| `斜斜` | `斜` | 712 | review: merge |
| `稍差` | `差` | 712 | review: merge |
| `办完` | `办` | 711 | review: merge |

### Dropped by 2+ flags: random sample of 0 of 0 in the window

| rank | lemma | flags |
|---:|---|---|

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 15,347 (keep 10,937, drop 4,410); review merges: 417.
