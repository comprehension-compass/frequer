# Review report: zh (full)

- Ranking score: `frequency`; 147,173 candidate lemmas ranked.
- Tokens counted: 818,671,745 in 1,049,587 documents, 120 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_zh` 1.7.0 (sha256 `13ce440dd994040c`); fallback `backend`, units on; honeyeater `4cd1389ef830`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-zh | 119 | 1,047,831 | 22,259,371 | 818,322,756 | alpha 1,517,648, exact_dup 2,369,284, gap 421,516, langid 1,551,295, length 495,812, near_dup 294,170, traditional 211,507, traditional_doc 221,290 |
| tatoeba-cmn | 1 | 1,756 | 49,078 | 348,989 | alpha 87, gap 6, length 21, near_dup 350, traditional 39,747 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 10,509,336. Sentences: 41,099,091.

## Units

Counted occurrences by kind: compound 414,702 (0.05%), compound1 7,115,584 (0.87%), construction 4,732,344 (0.58%), phrase 3,187,688 (0.39%), word 803,221,427 (98.11%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 9,734 | 7,533,767 |
| construction | 15 | 4,732,344 |
| phrase | 140 | 3,187,688 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `点头` | 164,315 | 84,548 | 657 |
| `说话` | 126,297 | 77,998 | 877 |
| `担心` | 105,127 | 74,468 | 1035 |
| `报名` | 85,655 | 27,065 | 1264 |
| `开口` | 84,912 | 47,650 | 1276 |
| `放心` | 76,678 | 57,792 | 1417 |
| `毕业` | 65,411 | 36,682 | 1637 |
| `摇头` | 62,955 | 44,203 | 1693 |
| `赛车` | 59,678 | 9,185 | 1664 |
| `回家` | 58,712 | 39,967 | 1797 |
| `结婚` | 52,270 | 28,478 | 1989 |
| `吃饭` | 51,914 | 33,454 | 1999 |
| `车型` | 50,363 | 16,575 | 1953 |
| `世界杯` | 49,236 | 12,584 | 2130 |
| `厂家` | 45,877 | 25,566 | 1652 |
| `卖家` | 43,797 | 8,824 | 2328 |
| `动手` | 42,336 | 30,266 | 2385 |
| `受伤` | 42,234 | 30,898 | 2389 |
| `帮忙` | 38,815 | 29,351 | 2551 |
| `睡觉` | 35,945 | 24,321 | 2707 |
| `报警` | 34,815 | 17,113 | 2766 |
| `离婚` | 32,676 | 14,327 | 2906 |
| `生气` | 32,559 | 23,468 | 2916 |
| `日电` | 31,466 | 23,811 | 3000 |
| `配套` | 31,269 | 23,042 | 2398 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `被 + 动词` | 1,477,936 | 460,152 | 52 |
| `把 + 名词 + 动词` | 1,406,245 | 472,103 | 58 |
| `是…的` | 527,542 | 268,244 | 163 |
| `动词 + 得 + 补语` | 426,878 | 208,039 | 216 |
| `是 + 谓语 + 的` | 402,544 | 227,893 | 234 |
| `动词 + 得/不 + 补语` | 238,292 | 153,531 | 431 |
| `比 + 名词 + 形容词` | 218,573 | 150,907 | 470 |
| `动词 + 得/不 + 起` | 23,781 | 20,113 | 3732 |
| `动词 + 得/不 + 动` | 4,556 | 4,207 | 12100 |
| `要…了` | 3,670 | 3,435 | 14033 |
| `给 + 动词` | 1,914 | 1,797 | 21546 |
| `动词 + 得/不 + 下` | 376 | 353 | 58105 |
| `为…所 + 动词` | 31 | 31 | - |
| `〜来〜去` | 5 | 5 | - |
| `快…了` | 1 | 1 | - |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `在〜中` | 431,688 | 253,562 | 213 |
| `在〜下` | 290,269 | 195,177 | 341 |
| `虽然…但` | 167,939 | 109,943 | 641 |
| `如果…就` | 117,688 | 87,447 | 937 |
| `虽然…但是` | 107,121 | 66,913 | 1018 |
| `在〜上` | 94,480 | 76,363 | 1144 |
| `当…时` | 92,389 | 66,400 | 1170 |
| `只要…就` | 84,532 | 67,249 | 1282 |
| `尤其是` | 84,067 | 68,351 | 1293 |
| `对于〜来说` | 82,321 | 61,876 | 1326 |
| `以〜为〜` | 81,495 | 61,921 | 1346 |
| `如果…的话` | 72,431 | 51,506 | 1500 |
| `从〜开始` | 58,171 | 49,741 | 1814 |
| `对〜来说` | 57,190 | 46,002 | 1838 |
| `如果…那么` | 48,973 | 38,524 | 2117 |
| `不是…而是` | 48,031 | 41,247 | 2156 |
| `即使…也` | 47,554 | 37,584 | 2178 |
| `像〜一样` | 46,769 | 38,229 | 2216 |
| `因为…所以` | 45,374 | 37,390 | 2264 |
| `特别是` | 45,011 | 38,993 | 2280 |
| `就算…也` | 42,617 | 34,043 | 2372 |
| `不仅…还` | 39,136 | 34,756 | 2528 |
| `既…又` | 37,105 | 31,997 | 2655 |
| `打电话` | 36,153 | 25,256 | 2696 |
| `连…都` | 34,985 | 30,426 | 2759 |

## Co-occurrence (association) table

343,458 tokens, 50,379 sentences. After merging and dropping items seen fewer than 5 times: 21,163 items (unigrams, UPOS votes, n-grams, pairs); 12,237 n-grams and pairs scored (n2 8,085, n3 3,551, n4 601). Shipped: 8,122 rows, 0.1 MB gzipped (`zh.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`zh.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `本 书` |  | 262 | 215 | 8.52 | 0.82 | 2,921 |  |
| 2 | n | `很 多` |  | 458 | 369 | 5.22 | 0.55 | 2,674 |  |
| 3 | n | `件 事` |  | 184 | 144 | 8.24 | 0.76 | 1,919 |  |
| 4 | n | `不 知道` |  | 400 | 307 | 4.26 | 0.44 | 1,768 |  |
| 5 | n | `不 能` |  | 438 | 345 | 3.92 | 0.41 | 1,706 |  |
| 6 | n | `不 会` |  | 503 | 375 | 3.55 | 0.38 | 1,685 |  |
| 7 | n | `汤姆 和 玛丽` |  | 158 | 104 | 6.54 | 0.59 | 1,355 |  |
| 8 | n | `住 在` |  | 228 | 199 | 4.91 | 0.47 | 1,240 |  |
| 9 | n | `我 想` |  | 548 | 410 | 2.58 | 0.28 | 1,194 |  |
| 10 | n | `个 人` |  | 352 | 285 | 3.52 | 0.35 | 1,146 |  |
| 11 | n | `看 到` |  | 231 | 195 | 4.64 | 0.44 | 1,101 |  |
| 12 | n | `找 到` |  | 151 | 138 | 6.04 | 0.54 | 1,045 |  |
| 13 | n | `有 很 多` |  | 165 | 146 | 5.36 | 0.49 | 979 |  |
| 14 | n | `不 想` |  | 313 | 255 | 3.25 | 0.32 | 908 |  |
| 15 | n | `很 好` |  | 242 | 209 | 3.86 | 0.37 | 891 |  |
| 16 | n | `看 见` |  | 139 | 120 | 5.64 | 0.50 | 859 |  |
| 17 | n | `出 去` |  | 141 | 130 | 5.51 | 0.49 | 857 |  |
| 18 | n | `封 信` |  | 61 | 55 | 10.22 | 0.82 | 826 |  |
| 19 | n | `得 很` |  | 191 | 167 | 4.20 | 0.39 | 796 |  |
| 20 | n | `孩子 们` |  | 78 | 69 | 8.33 | 0.69 | 793 |  |
| 21 | n | `个 月` |  | 131 | 116 | 5.16 | 0.45 | 763 |  |
| 22 | n | `两 个` |  | 160 | 144 | 4.49 | 0.41 | 748 |  |
| 23 | n | `有 没 有` |  | 80 | 77 | 6.78 | 0.56 | 734 |  |
| 24 | n | `不 喜欢` |  | 227 | 185 | 3.49 | 0.33 | 733 |  |
| 25 | n | `很 快` |  | 130 | 124 | 5.13 | 0.45 | 728 |  |
| 26 | n | `人 都` |  | 182 | 157 | 4.06 | 0.37 | 715 |  |
| 27 | n | `到 了` |  | 365 | 311 | 2.48 | 0.25 | 713 |  |
| 28 | n | `一 种` |  | 146 | 120 | 4.60 | 0.41 | 703 |  |
| 29 | n | `听 到` |  | 117 | 105 | 5.46 | 0.47 | 695 |  |
| 30 | n | `一 个 人` |  | 168 | 151 | 4.17 | 0.38 | 685 |  |
| 31 | n | `一 次` |  | 137 | 123 | 4.65 | 0.41 | 670 |  |
| 32 | n | `第一 次` |  | 65 | 50 | 8.37 | 0.68 | 667 |  |
| 33 | n | `死 了` |  | 171 | 140 | 3.80 | 0.35 | 667 |  |
| 34 | n | `做 什么` |  | 155 | 134 | 4.31 | 0.39 | 660 |  |
| 35 | n | `部 电影` |  | 47 | 40 | 10.39 | 0.81 | 632 |  |
| 36 | n | `首 歌` |  | 42 | 37 | 11.22 | 0.86 | 626 |  |
| 37 | n | `在 家` |  | 156 | 131 | 3.98 | 0.36 | 609 |  |
| 38 | n | `真 是` |  | 145 | 123 | 4.05 | 0.36 | 600 |  |
| 39 | n | `我 觉得` |  | 187 | 156 | 3.25 | 0.30 | 600 |  |
| 40 | n | `的 名字` |  | 125 | 115 | 3.95 | 0.35 | 574 |  |
| 41 | n | `是 一 个` |  | 237 | 187 | 2.86 | 0.27 | 568 |  |
| 42 | n | `让 我` |  | 243 | 210 | 2.69 | 0.26 | 563 |  |
| 43 | n | `大家 都` |  | 74 | 68 | 6.49 | 0.53 | 561 |  |
| 44 | n | `辆 车` |  | 52 | 49 | 8.68 | 0.68 | 551 |  |
| 45 | n | `一 天` |  | 135 | 115 | 4.04 | 0.36 | 534 |  |
| 46 | n | `世界 上` |  | 75 | 71 | 6.17 | 0.51 | 526 |  |
| 47 | n | `一会 儿` |  | 47 | 43 | 8.56 | 0.67 | 518 |  |
| 48 | n | `买 了` |  | 172 | 153 | 3.22 | 0.29 | 509 |  |
| 49 | n | `并 不` |  | 94 | 82 | 4.79 | 0.40 | 498 |  |
| 50 | n | `很 高兴` |  | 75 | 68 | 5.72 | 0.47 | 497 |  |

### Verb pairs in the queue

_none_

## Rank shifts against the live snapshot (`reference/lemmas/zh.json`)

Live list 40,069 lemmas, this build 147,173; 38,655 shared. Spearman rank correlation on the shared lemmas 0.952; median rank ratio 1.03x.
Overlap of this build's top-k with the live top-k: top 1,000 96.0%, top 5,000 95.3%, top 20,000 94.3%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `也就是说` | 38434 | 3387 | -35,047 |
| `可不` | 36396 | 3635 | -32,761 |
| `不仅…也` | 30901 | 2845 | -28,056 |
| `由此` | 29972 | 3275 | -26,697 |
| `包括〜在内` | 24648 | 4977 | -19,671 |
| `种种` | 23827 | 4731 | -19,096 |
| `即可` | 19872 | 2331 | -17,541 |
| `酥` | 21094 | 4741 | -16,353 |
| `事实上` | 17445 | 2590 | -14,855 |
| `型` | 16814 | 2387 | -14,427 |
| `折#fold` | 18481 | 4419 | -14,062 |
| `绝不` | 16493 | 2837 | -13,656 |
| `看出` | 15401 | 2515 | -12,886 |
| `韩` | 14309 | 1844 | -12,465 |
| `本来` | 11007 | 1175 | -9,832 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `行` | 3875 | 143405 | +139,530 |
| `各类` | 1613 | 123842 | +122,229 |
| `多功能` | 4642 | 117255 | +112,613 |
| `售后服务` | 4669 | 65425 | +60,756 |
| `各级` | 2998 | 56847 | +53,849 |
| `传说` | 2555 | 54000 | +51,445 |
| `人家` | 2176 | 50704 | +48,528 |
| `一幕` | 4955 | 50023 | +45,068 |
| `余` | 4146 | 44056 | +39,910 |
| `一流` | 4028 | 39434 | +35,406 |
| `就是` | 421 | 35424 | +35,003 |
| `吉` | 4066 | 36295 | +32,229 |
| `假` | 2589 | 34160 | +31,571 |
| `一带` | 3583 | 32271 | +28,688 |
| `是…还是` | 4406 | 32867 | +28,461 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `是 + 谓语 + 的` | - | 234 | - |
| `本来` | 11007 | 1175 | -9,832 |
| `更是` | - | 1497 | - |
| `行#háng` | - | 1530 | - |
| `出手` | - | 1610 | - |
| `入#rù` | - | 1661 | - |
| `一道` | 5158 | 1755 | -3,403 |
| `韩` | 14309 | 1844 | -12,465 |
| `回事` | 7173 | 2029 | -5,144 |
| `假#jiǎ` | - | 2151 | - |
| `即可` | 19872 | 2331 | -17,541 |
| `型` | 16814 | 2387 | -14,427 |
| `评` | 5146 | 2410 | -2,736 |
| `看出` | 15401 | 2515 | -12,886 |
| `思` | 6676 | 2520 | -4,156 |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `就是` | 421 | 35424 | +35,003 |
| `各种` | 510 | - | - |
| `还有` | 684 | - | - |
| `中#zhòng` | 1496 | 5760 | +4,264 |
| `各类` | 1613 | 123842 | +122,229 |
| `要…了` | 1697 | 14033 | +12,336 |
| `世` | 1703 | 5731 | +4,028 |
| `看起来` | 1710 | - | - |
| `乐` | 1728 | - | - |
| `留下` | 1741 | 5956 | +4,215 |
| `怀` | 1758 | 5384 | +3,626 |
| `在…的时候` | 1788 | 5854 | +4,066 |
| `只有` | 1809 | 6360 | +4,551 |
| `种#zhòng` | 1879 | 8991 | +7,112 |
| `如下` | 1976 | 6639 | +4,663 |

## Ported frequer checks

### Form-ratio outliers (212)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `的` | 41,939,618 | median form 2565; `的` 41,936,975 (16350x) |
| 4 | `一` | 10,996,876 | median form 1773; `一` 9,993,214 (5636x) |
| 35 | `三` | 1,950,574 | median form 1020; `三` 1,078,658 (1058x) |
| 129 | `十` | 705,791 | median form 42; `10` 460,525 (10965x), `十` 244,854 (5830x) |
| 150 | `百分之` | 591,724 | median form 2; `%` 584,871 (292436x), `百分之` 6,848 (3424x) |
| 164 | `技术` | 526,105 | median form 297; `技术` 525,612 (1770x) |
| 172 | `计划` | 515,021 | median form 502; `计划` 514,463 (1025x) |
| 185 | `十一` | 490,069 | median form 14; `11` 462,337 (33024x), `十一` 27,632 (1974x) |
| 245 | `九` | 389,194 | median form 2; `9` 257,789 (128894x), `九` 131,033 (65516x) |
| 262 | `有限公司` | 373,050 | median form 51; `有限公司` 371,654 (7287x) |
| 314 | `十二` | 317,659 | median form 43.5; `12` 270,046 (6208x), `十二` 47,518 (1092x) |
| 334 | `二十` | 294,530 | median form 7; `20` 245,230 (35033x), `二十` 49,253 (7036x) |
| 510 | `为什么` | 203,065 | median form 14; `为什么` 202,765 (14483x) |
| 540 | `十五` | 194,773 | median form 9; `15` 170,677 (18964x), `十五` 24,084 (2676x) |
| 553 | `开发` | 190,725 | median form 72; `开发` 190,595 (2647x) |
| 703 | `越来越` | 154,711 | median form 20.5; `越来越` 154,665 (7545x) |
| 730 | `十八` | 150,021 | median form 2; `18` 117,184 (58592x), `十八` 32,823 (16412x) |
| 783 | `十三` | 140,638 | median form 15; `13` 112,654 (7510x), `十三` 27,955 (1864x) |
| 835 | `互联网` | 131,834 | median form 14; `互联网` 131,798 (9414x) |
| 841 | `加拿大` | 131,111 | median form 11; `加拿大` 129,512 (11774x) |
| 989 | `不管` | 110,803 | median form 9; `不管` 110,787 (12310x) |
| 1002 | `二十四` | 109,229 | median form 58; `24` 104,456 (1801x) |
| 1004 | `消费者` | 109,197 | median form 16; `消费者` 109,168 (6823x) |
| 1017 | `二十五` | 107,349 | median form 3; `25` 103,854 (34618x), `二十五` 3,488 (1163x) |
| 1034 | `十七` | 105,345 | median form 5; `17` 91,876 (18375x), `十七` 13,459 (2692x) |

_187 more not shown._

### Singular/plural mismatch (0)

Lemma looks like a plural whose stripped form maps to another listed lemma.

_none_

### Lemma consistency (2)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 3561 | `纪录` | 25,327 | alone, `纪录` lemmatises to `记录` (rank 990) |
| 9523 | `某某` | 6,460 | alone, `某某` lemmatises to `某` (rank 464) |

### Short lemmas (1,492)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `的` | 41,939,618 | `的` -> `的`, `地` -> `地#de`, `到` -> `到#dào` |
| 3 | `是` | 11,969,230 | `是` -> `是` |
| 4 | `一` | 10,996,876 | `一` -> `一`, `1` -> `一`, `①` -> `一`, `I` -> `?`, `Ⅰ` -> `?` |
| 5 | `在` | 8,374,290 | `在` -> `在` |
| 6 | `不` | 7,497,340 | `不` -> `不` |
| 7 | `个` | 6,152,672 | `个` -> `个` |
| 8 | `这` | 5,779,373 | `这` -> `这` |
| 9 | `有` | 4,964,502 | `有` -> `有` |
| 10 | `和` | 4,815,366 | `和` -> `和` |
| 11 | `我` | 4,693,894 | `我` -> `我` |
| 12 | `就` | 4,643,677 | `就` -> `就` |
| 13 | `也` | 4,152,874 | `也` -> `也` |
| 14 | `人` | 3,796,933 | `人` -> `人` |
| 15 | `他` | 3,791,609 | `他` -> `他` |
| 16 | `你` | 3,512,558 | `你` -> `你`, `妳` -> `你`, `伱` -> `伱` |
| 18 | `都` | 3,062,817 | `都` -> `都` |
| 22 | `会` | 2,679,787 | `会` -> `会`, `户` -> `户` |
| 24 | `多` | 2,501,183 | `多` -> `多` |
| 25 | `年` | 2,448,194 | `年` -> `年` |
| 26 | `对` | 2,334,232 | `对` -> `对` |
| 28 | `要` | 2,241,535 | `要` -> `要` |
| 30 | `说` | 2,219,327 | `说` -> `说`, `说一` -> `?` |
| 31 | `能` | 2,152,777 | `能` -> `能` |
| 32 | `很` | 2,108,891 | `很` -> `很` |
| 33 | `那` | 2,096,691 | `那` -> `那` |

_1,467 more not shown._

### Case merges (0)

Non-lowercase lemmas, with the lowercase twin where one is listed.

_none_

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 762 (76.2%).

Ours only: `时时`, `彩`, `被 + 动词`, `把 + 名词 + 动词`, `十`, `前`, `百分之`, `是…的`, `重庆`, `儿#r`, `十一`, `说道`, `在〜中`, `动词 + 得 + 补语`, `二十八`, `是 + 谓语 + 的`, `幸运`, `声`, `有限公司`, `眼`, `脸`, `软件`, `十二`, `二十`, `周#week`

wordfreq only: `〇〇〇〇`, `〇〇〇`, `政治`, `第`, `人民`, `自由`, `委员会`, `人口`, `民主`, `事件`, `零点零`, `总统`, `战争`, `照片`, `时期`, `作`, `故事`, `欧洲`, `科学`, `举行`, `艺术`, `独立`, `亚洲`, `人类`, `制`

## Foreign-word candidates

_none_

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 57 | `中国` | 1,406,844 | PROPN 99%, capitalised forms 0% |
| 137 | `张` | 634,432 | PROPN 57%, capitalised forms 0% |
| 139 | `北京` | 630,558 | PROPN 100%, capitalised forms 0% |
| 140 | `美国` | 628,468 | PROPN 99%, capitalised forms 0% |
| 167 | `重庆` | 519,339 | PROPN 100%, capitalised forms 0% |
| 225 | `王` | 417,281 | PROPN 100%, capitalised forms 0% |
| 269 | `香港` | 363,678 | PROPN 100%, capitalised forms 0% |
| 383 | `日本` | 261,513 | PROPN 89%, capitalised forms 0% |
| 460 | `上海` | 224,659 | PROPN 100%, capitalised forms 0% |
| 506 | `李` | 204,340 | PROPN 100%, capitalised forms 0% |
| 535 | `林` | 195,666 | PROPN 98%, capitalised forms 0% |
| 587 | `广东` | 182,189 | PROPN 99%, capitalised forms 0% |
| 638 | `金` | 169,834 | PROPN 70%, capitalised forms 0% |
| 659 | `台湾` | 163,784 | PROPN 92%, capitalised forms 0% |
| 711 | `韩国` | 152,823 | PROPN 100%, capitalised forms 0% |
| 724 | `腾讯` | 150,956 | PROPN 100%, capitalised forms 0% |
| 798 | `微信` | 137,939 | PROPN 100%, capitalised forms 0% |
| 830 | `走势图` | 132,425 | PROPN 90%, capitalised forms 0% |
| 841 | `加拿大` | 131,111 | PROPN 99%, capitalised forms 0% |
| 879 | `英国` | 126,224 | PROPN 98%, capitalised forms 0% |
| 886 | `杨` | 125,201 | PROPN 97%, capitalised forms 0% |
| 978 | `秦` | 112,158 | PROPN 98%, capitalised forms 0% |
| 1082 | `山东` | 100,267 | PROPN 99%, capitalised forms 0% |
| 1104 | `广州` | 97,979 | PROPN 100%, capitalised forms 0% |
| 1162 | `亚洲` | 92,829 | PROPN 90%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 91.4% | 0.916 |
| juilland_u | 99.8% | 1.000 |
| juilland_u_corrected | 99.8% | 1.000 |
| dp_adjusted | 99.3% | 0.999 |
| cd_blend | 95.3% | 0.972 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `只有` | 6520 | 4912 | -1,608 | 11,396 | 10,756 | 0.990 | 0.042 |
| `违者` | 5394 | 3874 | -1,520 | 14,848 | 14,597 | 0.991 | 0.035 |
| `不知不觉` | 6196 | 4676 | -1,520 | 12,245 | 11,544 | 0.989 | 0.044 |
| `不到` | 6041 | 4547 | -1,494 | 12,677 | 11,888 | 0.991 | 0.035 |
| `不至于` | 6404 | 4911 | -1,493 | 11,720 | 10,761 | 0.989 | 0.041 |
| `彩霸王` | 2660 | 33760 | +31,100 | 37,734 | 722 | 0.957 | 0.172 |
| `曾道人` | 2078 | 31452 | +29,374 | 50,780 | 807 | 0.957 | 0.172 |
| `刘伯温` | 485 | 29030 | +28,545 | 214,070 | 910 | 0.957 | 0.175 |
| `九五至尊` | 4124 | 27643 | +23,519 | 21,332 | 980 | 0.958 | 0.171 |
| `分分彩` | 1120 | 22336 | +21,216 | 97,909 | 1,343 | 0.951 | 0.196 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `致力` | 4800 | 4765 | -35 | 17,457 | 15,954 | 0.991 | 0.035 |
| `郁闷` | 4706 | 4672 | -34 | 17,923 | 14,532 | 0.992 | 0.033 |
| `表现出` | 4691 | 4658 | -33 | 17,985 | 15,769 | 0.991 | 0.035 |
| `下手` | 4913 | 4881 | -32 | 16,931 | 14,410 | 0.991 | 0.036 |
| `相处` | 4919 | 4887 | -32 | 16,921 | 13,794 | 0.991 | 0.037 |
| `胖` | 3521 | 3972 | +451 | 26,387 | 10,480 | 0.836 | 0.238 |
| `份额` | 4547 | 4819 | +272 | 18,653 | 7,407 | 0.915 | 0.244 |
| `唯美` | 4119 | 4288 | +169 | 21,361 | 5,044 | 0.930 | 0.285 |
| `头像` | 2865 | 2990 | +125 | 33,921 | 4,720 | 0.938 | 0.250 |
| `宗教` | 4845 | 4952 | +107 | 17,227 | 7,651 | 0.959 | 0.139 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `致力` | 4800 | 4765 | -35 | 17,457 | 15,954 | 0.991 | 0.035 |
| `郁闷` | 4706 | 4672 | -34 | 17,923 | 14,532 | 0.992 | 0.033 |
| `下手` | 4913 | 4880 | -33 | 16,931 | 14,410 | 0.991 | 0.036 |
| `表现出` | 4691 | 4658 | -33 | 17,985 | 15,769 | 0.991 | 0.035 |
| `相处` | 4919 | 4887 | -32 | 16,921 | 13,794 | 0.991 | 0.037 |
| `胖` | 3521 | 3972 | +451 | 26,387 | 10,480 | 0.836 | 0.238 |
| `份额` | 4547 | 4819 | +272 | 18,653 | 7,407 | 0.915 | 0.244 |
| `唯美` | 4119 | 4288 | +169 | 21,361 | 5,044 | 0.930 | 0.285 |
| `头像` | 2865 | 2990 | +125 | 33,921 | 4,720 | 0.938 | 0.250 |
| `宗教` | 4845 | 4952 | +107 | 17,227 | 7,651 | 0.959 | 0.139 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `难怪` | 4986 | 4861 | -125 | 16,626 | 14,647 | 0.992 | 0.033 |
| `遇` | 4902 | 4780 | -122 | 16,967 | 14,501 | 0.992 | 0.031 |
| `广阔` | 5120 | 4999 | -121 | 16,048 | 14,401 | 0.992 | 0.032 |
| `开玩笑` | 4981 | 4860 | -121 | 16,640 | 14,193 | 0.992 | 0.033 |
| `唯有` | 4969 | 4851 | -118 | 16,692 | 14,076 | 0.991 | 0.034 |
| `唯美` | 4119 | 5062 | +943 | 21,361 | 5,044 | 0.930 | 0.285 |
| `份额` | 4547 | 5322 | +775 | 18,653 | 7,407 | 0.915 | 0.244 |
| `胖` | 3521 | 4132 | +611 | 26,387 | 10,480 | 0.836 | 0.238 |
| `头像` | 2865 | 3476 | +611 | 33,921 | 4,720 | 0.938 | 0.250 |
| `九五至尊` | 4124 | 4522 | +398 | 21,332 | 980 | 0.958 | 0.171 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `违者` | 5394 | 4576 | -818 | 14,848 | 14,597 | 0.991 | 0.035 |
| `除此之外` | 5674 | 4930 | -744 | 13,803 | 12,826 | 0.991 | 0.033 |
| `不仅…而且` | 5529 | 4799 | -730 | 14,333 | 13,285 | 0.991 | 0.036 |
| `着手` | 5582 | 4863 | -719 | 14,123 | 13,027 | 0.991 | 0.035 |
| `深受` | 5558 | 4849 | -709 | 14,223 | 13,038 | 0.992 | 0.033 |
| `彩霸王` | 2660 | 9819 | +7,159 | 37,734 | 722 | 0.957 | 0.172 |
| `九五至尊` | 4124 | 10842 | +6,718 | 21,332 | 980 | 0.958 | 0.171 |
| `曾道人` | 2078 | 8419 | +6,341 | 50,780 | 807 | 0.957 | 0.172 |
| `稳赚` | 3778 | 8385 | +4,607 | 23,933 | 1,732 | 0.958 | 0.169 |
| `分分彩` | 1120 | 5510 | +4,390 | 97,909 | 1,343 | 0.951 | 0.196 |



## Junk-filter heuristics

Rules on: diversity, citation, shape, propn_band; accent merges at ratio None. Window: the 45,093 ranked lemmas (after the exclusion list) that fill the top 40,000. Actions: keep 28,341, number-drop 372, review-drop 4,721, review-keep 11,659.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band | propn_usage |
|---|---:|---:|---:|---:|---:|---:|
| diversity | 983 | 0 | 0 | 7 | 257 | 0 |
| citation | 0 | 114 | 0 | 1 | 0 | 0 |
| foreign | 0 | 0 | 0 | 0 | 0 | 0 |
| shape | 7 | 1 | 0 | 771 | 50 | 0 |
| propn_band | 257 | 0 | 0 | 50 | 4,523 | 0 |
| propn_usage | 0 | 0 | 0 | 0 | 0 | 0 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 0.

### Low diversity

Documents reached / documents expected at random, below 0.2 (frequency >= 20): 983 in the window. For comparison, each log2-frequency band's 2nd percentile: 64-127: 0.05, 128-255: 0.07, 256-511: 0.09, 512-1023: 0.12, 1024-2047: 0.16, 2048-4095: 0.21, 4096-8191: 0.25, 8192-16383: 0.23, 16384-32767: 0.28, 32768-65535: 0.26, 65536-131071: 0.27, 131072-262143: 0.17, 262144-524287: 0.21.

Examples: `时时` (36), `彩` (37), `重庆` (167), `二十八` (229), `幸运` (236), `论坛` (391), `开奖` (402), `码` (480), `刘伯温` (485), `技巧` (545), `预测` (684), `腾讯` (729), `蛋蛋` (786), `投注` (834), `传奇` (837), `走势图` (839), `加拿大` (852), `秦` (991), `叶` (1077), `分分彩` (1120), `号码` (1127), `新疆` (1236), `彩票` (1257), `飞艇` (1467), `赛马会` (1484), `肖` (1495), `玩法` (1514), `农场` (1543), `赛车` (1687), `修士` (1748), `私服` (1999), `曾道人` (2078), `二手` (2145), `娱乐城` (2156), `图表` (2168), `遗漏` (2181), `胆` (2328), `楚` (2424), `白癜风` (2459), `公式` (2598)

### Accent merges (572)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `博会` | `进博会` | 4,851 | review: merge |
| `显露出` | `显露` | 3,472 | review: merge |
| `书目的` | `书目` | 1,731 | review: merge |
| `百度网` | `百度网盘` | 1,243 | review: merge |
| `少先` | `少先队` | 2,461 | review: merge |
| `钣` | `钣金` | 1,082 | review: merge |
| `源热泵` | `热泵` | 1,421 | review: merge |
| `名目的` | `名目` | 1,260 | review: merge |
| `完全全` | `完完全全` | 2,470 | review: merge |
| `蹦出` | `蹦` | 2,147 | review: merge |
| `丛林中` | `丛林` | 721 | review: merge |
| `交组织` | `交织` | 1,012 | review: merge |
| `伱` | `你` | 799 | review: merge |
| `谴` | `天谴` | 496 | review: merge |
| `幻化成` | `幻化` | 777 | review: merge |
| `片狼藉` | `一片狼藉` | 1,308 | review: merge |
| `淬` | `淬火` | 412 | review: merge |
| `基丹` | `筑基丹` | 427 | review: merge |
| `编组织` | `编织` | 1,755 | review: merge |
| `卓` | `安卓` | 3,157 | review: merge |
| `企` | `企业` | 5,538 | review: merge |
| `手车` | `二手车` | 853 | review: merge |
| `流露出` | `流露` | 8,774 | review: merge |
| `自已` | `自己` | 6,520 | review: merge |
| `淡淡的` | `淡淡` | 1,496 | review: merge |
| `不锈` | `不锈钢` | 8,333 | review: merge |
| `离不` | `离不开` | 5,532 | review: merge |
| `捂着` | `捂` | 5,587 | review: merge |
| `好象` | `好像` | 8,150 | review: merge |
| `散发出` | `散发` | 1,824 | review: merge |
| `无表情` | `面无表情` | 73 | review: merge |
| `条龙` | `一条龙` | 8,594 | review: merge |
| `元化` | `多元化` | 112 | review: merge |
| `狐` | `狐狸` | 4,720 | review: merge |
| `步声` | `脚步声` | 94 | review: merge |
| `党和` | `党` | 8,928 | review: merge |
| `交待` | `交代` | 5,094 | review: merge |
| `展现出` | `展现` | 7,266 | review: merge |
| `帐户` | `账户` | 4,870 | review: merge |
| `以为然` | `不以为然` | 3,870 | review: merge |
| `粘膜` | `黏膜` | 4,429 | review: merge |
| `分出` | `分` | 4,561 | review: merge |
| `大不` | `大不了` | 1,347 | review: merge |
| `成份` | `成分` | 4,286 | review: merge |
| `三板` | `新三板` | 5,352 | review: merge |
| `咬着牙` | `咬牙` | 362 | review: merge |
| `先容` | `介绍` | 4,052 | review: merge |
| `什` | `什么` | 3,059 | review: merge |
| `官方网` | `官方网站` | 6,391 | review: merge |
| `〜起` | `起` | 12,443 | review: merge |
| `黑龙` | `黑龙江` | 4,484 | review: merge |
| `在心上` | `放在心上` | 1,432 | review: merge |
| `一辈` | `一辈子` | 3,176 | review: merge |
| `在眼里` | `眼里` | 262 | review: merge |
| `楞` | `愣` | 3,079 | review: merge |
| `知不觉` | `不知不觉` | 5,809 | review: merge |
| `身分` | `身份` | 3,205 | review: merge |
| `年青` | `年轻` | 3,962 | review: merge |
| `高高在` | `高高在上` | 4,798 | review: merge |
| `污` | `污染` | 2,184 | review: merge |
| `生活中` | `生活` | 1,654 | review: merge |
| `双十` | `双十一` | 937 | review: merge |
| `随时随` | `随时随地` | 98 | review: merge |
| `婴幼` | `婴幼儿` | 367 | review: merge |
| `显现出` | `显现` | 442 | review: merge |
| `壹` | `一` | 2,649 | review: merge |
| `聊着` | `聊` | 1,490 | review: merge |
| `锈钢` | `不锈钢` | 603 | review: merge |
| `以为意` | `不以为意` | 2,260 | review: merge |
| `座落` | `坐落` | 3,677 | review: merge |
| `机率` | `几率` | 2,918 | review: merge |
| `个劲` | `一个劲` | 2,528 | review: merge |
| `签定` | `签订` | 2,559 | review: merge |
| `免不` | `免不了` | 285 | review: merge |
| `哭笑` | `哭笑不得` | 961 | review: merge |
| `低着` | `低` | 1,612 | review: merge |
| `名副` | `名副其实` | 3,133 | review: merge |
| `半响` | `半晌` | 2,504 | review: merge |
| `实实在` | `实实在在` | 6,091 | review: merge |
| `排名第` | `排名` | 2,664 | review: merge |
| `模版` | `模板` | 2,589 | review: merge |
| `党的` | `党` | 255 | review: merge |
| `迈着` | `迈` | 128 | review: merge |
| `浑身上` | `浑身上下` | 2,983 | review: merge |
| `份量` | `分量` | 2,231 | review: merge |
| `凝视着` | `凝视` | 2,458 | review: merge |
| `神祗` | `神祇` | 1,838 | review: merge |
| `永远都` | `永远` | 1,612 | review: merge |
| `迟早会` | `迟早` | 2,041 | review: merge |
| `无数道` | `无数` | 1,967 | review: merge |
| `殊不` | `殊不知` | 3,085 | review: merge |
| `视而` | `视而不见` | 1,108 | review: merge |
| `无奇` | `平平无奇` | 1,547 | review: merge |
| `暴露出` | `暴露` | 2,183 | review: merge |
| `现状及` | `现状` | 1,415 | review: merge |
| `代会` | `党代会` | 401 | review: merge |
| `建部` | `住建部` | 1,630 | review: merge |
| `开发新` | `开发` | 72 | review: merge |
| `很惨` | `惨` | 1,225 | review: merge |
| `热衷于` | `热衷` | 1,305 | review: merge |
| `处处长` | `处长` | 2,036 | review: merge |
| `话下` | `不在话下` | 1,838 | review: merge |
| `更让` | `让` | 320 | review: merge |
| `很淡` | `淡` | 427 | review: merge |
| `磨擦` | `摩擦` | 1,608 | review: merge |
| `类药物` | `药物` | 1,661 | review: merge |
| `惟有` | `唯有` | 1,705 | review: merge |
| `型基金` | `基金` | 1,815 | review: merge |
| `发症` | `并发症` | 3,701 | review: merge |
| `自来` | `自来水` | 426 | review: merge |
| `彷佛` | `仿佛` | 1,654 | review: merge |
| `澡` | `洗澡` | 1,515 | review: merge |
| `年青人` | `年轻人` | 1,096 | review: merge |
| `象是` | `像是` | 1,870 | review: merge |
| `各乡镇` | `乡镇` | 1,480 | review: merge |
| `薰` | `熏` | 1,523 | review: merge |
| `中老` | `中老年` | 1,019 | review: merge |
| `处罚金` | `罚金` | 1,748 | review: merge |
| `零配` | `零配件` | 2,102 | review: merge |
| `最重` | `重` | 1,822 | review: merge |
| `聊得` | `聊` | 1,436 | review: merge |
| `姊姊` | `姐姐` | 1,229 | review: merge |
| `届生` | `应届生` | 1,995 | review: merge |
| `摸样` | `模样` | 2,083 | review: merge |
| `声令下` | `一声令下` | 2,793 | review: merge |
| `香奈` | `香奈儿` | 830 | review: merge |
| `比不` | `比不上` | 4,785 | review: merge |
| `上用品` | `床上用品` | 1,381 | review: merge |
| `等奖` | `一等奖` | 10,255 | review: merge |
| `无限公司` | `有限公司` | 1,220 | review: merge |
| `闪耀着` | `闪耀` | 703 | review: merge |
| `舔着` | `舔` | 1,025 | review: merge |
| `挑出` | `挑` | 1,301 | review: merge |
| `贴着` | `贴` | 87 | review: merge |
| `好样` | `好样的` | 1,233 | review: merge |
| `天而降` | `从天而降` | 4,133 | review: merge |
| `乍一` | `乍一看` | 1,556 | review: merge |
| `暴光` | `曝光` | 1,218 | review: merge |
| `网路` | `网络` | 1,613 | review: merge |
| `抿着` | `抿` | 776 | review: merge |
| `汉兰` | `汉兰达` | 235 | review: merge |
| `丝一毫` | `一丝一毫` | 996 | review: merge |
| `图象` | `图像` | 1,424 | review: merge |
| `切不` | `切不可` | 248 | review: merge |
| `在技术` | `技术` | 297 | review: merge |
| `手把` | `把手` | 438 | review: merge |
| `符篆` | `符箓` | 1,081 | review: merge |
| `制做` | `制作` | 1,024 | review: merge |
| `字型` | `字体` | 1,254 | review: merge |
| `性皮炎` | `皮炎` | 1,194 | review: merge |
| `盘算着` | `盘算` | 701 | review: merge |
| `存眷` | `关注` | 1,203 | review: merge |
| `总裁兼` | `总裁` | 913 | review: merge |
| `冒然` | `贸然` | 986 | review: merge |
| `透漏` | `透露` | 1,041 | review: merge |
| `唯品` | `唯品会` | 824 | review: merge |
| `并作` | `作` | 458 | review: merge |
| `眯着` | `眯` | 1,917 | review: merge |
| `地拉` | `拉` | 1,008 | review: merge |
| `丝毫不` | `丝毫` | 129 | review: merge |
| `来不` | `来不及` | 2,979 | review: merge |
| `过份` | `过分` | 787 | review: merge |
| `惊心` | `惊心动魄` | 1,401 | review: merge |
| `连云` | `连云港` | 812 | review: merge |
| `掐着` | `掐` | 1,026 | review: merge |
| `凝炼` | `凝练` | 950 | review: merge |
| `柄剑` | `剑` | 934 | review: merge |
| `恶梦` | `噩梦` | 1,142 | review: merge |
| `皂` | `肥皂` | 328 | review: merge |
| `睁一` | `睁一只眼闭一只眼` | 997 | review: merge |
| `定睛一` | `定睛` | 899 | review: merge |
| `更惨` | `惨` | 607 | review: merge |
| `件套` | `四件套` | 229 | review: merge |
| `粥样` | `动脉粥样硬化` | 1,122 | review: merge |
| `针锋` | `针锋相对` | 1,545 | review: merge |
| `化身为` | `化身` | 1,298 | review: merge |
| `拄着` | `拄` | 889 | review: merge |
| `息息` | `息息相关` | 139 | review: merge |
| `国家知识产权` | `国家知识产权局` | 1,125 | review: merge |
| `道菜` | `菜` | 1,446 | review: merge |
| `道工序` | `工序` | 1,053 | review: merge |
| `拔赛` | `选拔赛` | 223 | review: merge |
| `下无敌` | `天下无敌` | 144 | review: merge |
| `不惯` | `看不惯` | 1,318 | review: merge |
| `保不` | `保不住` | 1,365 | review: merge |
| `闭一` | `睁一只眼闭一只眼` | 999 | review: merge |
| `丝不苟` | `一丝不苟` | 396 | review: merge |
| `工信` | `工信部` | 71 | review: merge |
| `家子` | `一家子` | 990 | review: merge |
| `火机` | `打火机` | 412 | review: merge |
| `总的` | `总` | 3,146 | review: merge |
| `手握着` | `手握` | 695 | review: merge |
| `震得` | `震` | 143 | review: merge |
| `经意` | `不经意` | 96 | review: merge |
| `纳西` | `纳西族` | 539 | review: merge |
| `动了动` | `动` | 120 | review: merge |
| `政斧` | `政府` | 686 | review: merge |
| `条线` | `线` | 1,827 | review: merge |
| `个脚印` | `脚印` | 1,092 | review: merge |
| `朵花` | `花` | 1,591 | review: merge |
| `稍安` | `稍安勿躁` | 847 | review: merge |
| `长白` | `长白山` | 986 | review: merge |
| `以上者` | `以上` | 886 | review: merge |
| `晕过` | `晕` | 502 | review: merge |
| `桌面上` | `桌面` | 762 | review: merge |
| `等不` | `等` | 231 | review: merge |
| `倍受` | `备受` | 1,593 | review: merge |
| `晋升为` | `晋升` | 1,495 | review: merge |
| `不单单是` | `不单单` | 347 | review: merge |
| `荡起` | `荡` | 910 | review: merge |
| `传授给` | `传授` | 720 | review: merge |
| `轰成` | `轰` | 591 | review: merge |
| `坐椅` | `座椅` | 747 | review: merge |
| `咧着` | `咧` | 785 | review: merge |
| `孕育出` | `孕育` | 264 | review: merge |
| `创造性地` | `创造性` | 1,113 | review: merge |
| `公积` | `公积金` | 761 | review: merge |
| `展露出` | `展露` | 786 | review: merge |
| `压抑着` | `压抑` | 607 | review: merge |
| `异想` | `异想天开` | 168 | review: merge |
| `沉迷于` | `沉迷` | 937 | review: merge |
| `涵义` | `含义` | 936 | review: merge |
| `个箭步` | `箭步` | 987 | review: merge |
| `很浓` | `浓` | 556 | review: merge |
| `缠绕着` | `缠绕` | 499 | review: merge |
| `贴子` | `帖子` | 866 | review: merge |
| `庙里` | `庙` | 835 | review: merge |
| `真不愧是` | `不愧是` | 799 | review: merge |
| `赶不` | `赶不上` | 1,266 | review: merge |
| `可任意` | `任意` | 266 | review: merge |
| `推波` | `推波助澜` | 1,048 | review: merge |
| `国务` | `国务院` | 1,252 | review: merge |
| `视屏` | `视频` | 1,156 | review: merge |
| `农村部` | `农业农村部` | 1,043 | review: merge |
| `天三夜` | `三天三夜` | 1,520 | review: merge |
| `参考报` | `经济参考报` | 1,057 | review: merge |
| `乐福` | `乐福鞋` | 984 | review: merge |
| `蓝球` | `篮球` | 1,000 | review: merge |
| `金白银` | `真金白银` | 950 | review: merge |
| `创板` | `科创板` | 1,328 | review: merge |
| `纷歧` | `分歧` | 313 | review: merge |
| `保护部` | `环境保护部` | 856 | review: merge |
| `傍边` | `旁边` | 871 | review: merge |
| `凸显出` | `凸显` | 377 | review: merge |
| `悠闲地` | `悠闲` | 968 | review: merge |
| `板机` | `扳机` | 861 | review: merge |
| `分解成` | `分解` | 580 | review: merge |
| `那末` | `那么` | 957 | review: merge |
| `思惟` | `思维` | 786 | review: merge |
| `颠峰` | `巅峰` | 776 | review: merge |
| `中关` | `中关村` | 274 | review: merge |
| `挖掘出` | `挖掘` | 536 | review: merge |
| `极管` | `二极管` | 832 | review: merge |
| `奇艺` | `爱奇艺` | 920 | review: merge |
| `战成` | `战` | 431 | review: merge |
| `临走时` | `临走` | 626 | review: merge |
| `脚色` | `角色` | 766 | review: merge |
| `涅盘` | `涅槃` | 717 | review: merge |
| `己经` | `已经` | 1,265 | review: merge |
| `一提` | `值得一提` | 638 | review: merge |
| `有志于` | `有志` | 164 | review: merge |
| `未办理` | `办理` | 75 | review: merge |
| `不逊于` | `不逊` | 630 | review: merge |
| `衬托出` | `衬托` | 774 | review: merge |
| `奥迪车` | `奥迪` | 771 | review: merge |
| `迁往` | `迁` | 734 | review: merge |
| `华中科技` | `华中科技大学` | 1,265 | review: merge |
| `金九银` | `金九银十` | 807 | review: merge |
| `什幺` | `什么` | 890 | review: merge |
| `捂着脸` | `捂` | 898 | review: merge |
| `眯着眼` | `眯` | 1,481 | review: merge |
| `迄今已` | `迄今` | 133 | review: merge |
| `耸了耸` | `耸` | 829 | review: merge |
| `惦记着` | `惦记` | 794 | review: merge |
| `伪装成` | `伪装` | 1,026 | review: merge |
| `广交` | `广交会` | 429 | review: merge |
| `噗哧` | `噗嗤` | 731 | review: merge |
| `桶金` | `第一桶金` | 734 | review: merge |
| `个劲儿` | `一个劲儿` | 1,093 | review: merge |
| `记忆里` | `记忆` | 759 | review: merge |
| `关健` | `关键` | 718 | review: merge |
| `奖得主` | `得主` | 89 | review: merge |
| `戴绿` | `戴绿帽` | 398 | review: merge |
| `无聊赖` | `百无聊赖` | 214 | review: merge |
| `不美观` | `美观` | 632 | review: merge |
| `唤出` | `唤` | 743 | review: merge |
| `老两` | `老两口` | 353 | review: merge |
| `轨制` | `双轨制` | 798 | review: merge |
| `三驾` | `三驾马车` | 705 | review: merge |
| `明眼` | `明眼人` | 710 | review: merge |
| `最优` | `优` | 4,116 | review: merge |
| `太重` | `重` | 3,016 | review: merge |
| `最差` | `差` | 1,612 | review: merge |
| `最远` | `远` | 489 | review: merge |
| `较晚` | `晚` | 1,426 | review: merge |
| `较佳` | `佳` | 917 | review: merge |
| `最惨` | `惨` | 891 | review: merge |
| `发贴` | `发帖` | 743 | review: merge |
| `啃着` | `啃` | 538 | review: merge |
| `提炼出` | `提炼` | 672 | review: merge |
| `斜斜` | `斜` | 763 | review: merge |
| `稍差` | `差` | 710 | review: merge |
| `办完` | `办` | 79 | review: merge |
| `莫三比克` | `莫` | 22,311 | review: merge |
| `头目的` | `头目` | 3,755 | review: merge |
| `瓦努阿图` | `瓦` | 3,642 | review: merge |
| `醒目的` | `醒目` | 1,656 | review: merge |
| `类目的` | `类目` | 1,436 | review: merge |
| `建议您` | `建议` | 1,405 | review: merge |
| `上老君` | `太上老君` | 1,212 | review: merge |
| `香港特别` | `香港特别行政区` | 1,185 | review: merge |
| `领悟到` | `领悟` | 1,014 | review: merge |
| `毁于` | `毁` | 871 | review: merge |
| `娓娓道` | `娓娓道来` | 835 | review: merge |
| `揣着` | `揣` | 785 | review: merge |
| `天不怕地` | `天不怕地不怕` | 747 | review: merge |
| `带天窗` | `天窗` | 729 | review: merge |
| `市民政局` | `民政局` | 728 | review: merge |
| `到擒来` | `手到擒来` | 717 | review: merge |
| `辛辛苦` | `辛辛苦苦` | 716 | review: merge |
| `这样一` | `这样一来` | 9,973 | review: merge |
| `站式` | `一站式` | 8,450 | review: merge |
| `不一会` | `不一会儿` | 6,590 | review: merge |
| `值得一提的` | `值得一提` | 5,198 | review: merge |
| `用不` | `用不着` | 5,002 | review: merge |
| `突如其` | `突如其来` | 4,881 | review: merge |
| `难不` | `难不成` | 4,879 | review: merge |
| `冷冷地` | `冷冷` | 4,768 | review: merge |
| `氨基丁` | `氨基丁酸` | 4,139 | review: merge |
| `大湾` | `大湾区` | 4,138 | review: merge |
| `着牙` | `咬牙` | 3,603 | review: merge |
| `禁不` | `禁不住` | 3,481 | review: merge |
| `恰到` | `恰到好处` | 3,314 | review: merge |
| `下子` | `一下子` | 3,300 | review: merge |
| `货到` | `货到付款` | 3,152 | review: merge |
| `引人` | `引人入胜` | 3,113 | review: merge |
| `层楼` | `更上一层楼` | 3,079 | review: merge |
| `大早` | `一大早` | 3,025 | review: merge |
| `来水` | `自来水` | 2,921 | review: merge |
| `起彼伏` | `此起彼伏` | 2,852 | review: merge |
| `打麻` | `打麻将` | 2,755 | review: merge |
| `句话` | `一句话` | 2,616 | review: merge |
| `情药` | `催情药` | 2,462 | review: merge |
| `级片` | `三级片` | 2,302 | review: merge |
| `种多样` | `多种多样` | 2,284 | review: merge |
| `久之` | `久而久之` | 2,279 | review: merge |
| `深不` | `深不可测` | 2,272 | review: merge |
| `农副` | `农副产品` | 2,256 | review: merge |
| `比力` | `比较` | 2,254 | review: merge |
| `婴期` | `元婴期` | 2,216 | review: merge |
| `改委` | `发改委` | 2,169 | review: merge |
| `片空白` | `一片空白` | 2,164 | review: merge |
| `年四季` | `一年四季` | 2,081 | review: merge |
| `本正经` | `一本正经` | 2,058 | review: merge |
| `久而` | `久而久之` | 2,042 | review: merge |
| `刀切` | `一刀切` | 2,041 | review: merge |
| `行之` | `行之有效` | 2,015 | review: merge |
| `不相` | `不相上下` | 1,989 | review: merge |
| `轰的` | `轰` | 1,980 | review: merge |
| `见钟情` | `一见钟情` | 1,953 | review: merge |
| `节课` | `课` | 1,890 | review: merge |
| `上角` | `右上角` | 1,886 | review: merge |
| `恭敬地` | `恭敬` | 1,868 | review: merge |
| `问起` | `问` | 1,860 | review: merge |
| `追究其` | `追究` | 1,841 | review: merge |
| `天材` | `天材地宝` | 1,825 | review: merge |
| `种规格` | `规格` | 1,778 | review: merge |
| `扫一` | `扫一扫` | 1,754 | review: merge |
| `追问道` | `追问` | 1,716 | review: merge |
| `死我活` | `你死我活` | 1,698 | review: merge |
| `去何` | `何去何从` | 1,684 | review: merge |
| `别怕` | `怕` | 1,677 | review: merge |
| `新月异` | `日新月异` | 1,659 | review: merge |
| `多少少` | `多多少少` | 1,653 | review: merge |
| `切实做` | `切实` | 1,652 | review: merge |
| `闪而` | `一闪而过` | 1,647 | review: merge |
| `有所思` | `若有所思` | 1,590 | review: merge |
| `人为本` | `以人为本` | 1,577 | review: merge |
| `放矢` | `有的放矢` | 1,570 | review: merge |
| `到之处` | `所到之处` | 1,536 | review: merge |
| `欲罢不` | `欲罢不能` | 1,521 | review: merge |
| `为力` | `无能为力` | 1,517 | review: merge |
| `受得` | `受得了` | 1,504 | review: merge |
| `风生水` | `风生水起` | 1,501 | review: merge |
| `步之遥` | `一步之遥` | 1,483 | review: merge |
| `来人往` | `人来人往` | 1,467 | review: merge |
| `满不` | `满不在乎` | 1,459 | review: merge |
| `势在` | `势在必行` | 1,446 | review: merge |
| `功不` | `功不可没` | 1,441 | review: merge |
| `至高无` | `至高无上` | 1,422 | review: merge |
| `中有数` | `心中有数` | 1,415 | review: merge |
| `许多多` | `许许多多` | 1,384 | review: merge |
| `开心心` | `开开心心` | 1,380 | review: merge |
| `国人民` | `中国人民` | 1,369 | review: merge |
| `声不吭` | `一声不吭` | 1,367 | review: merge |
| `审判决` | `判决` | 1,367 | review: merge |
| `高科` | `高科技` | 1,365 | review: merge |
| `条不紊` | `有条不紊` | 1,344 | review: merge |
| `明摆` | `明摆着` | 1,319 | review: merge |
| `缺一` | `缺一不可` | 1,317 | review: merge |
| `股脑` | `一股脑` | 1,312 | review: merge |
| `里人` | `城里人` | 1,296 | review: merge |
| `梦之` | `梦之队` | 1,295 | review: merge |
| `彻彻底` | `彻彻底底` | 1,282 | review: merge |
| `不适用` | `适用` | 1,281 | review: merge |
| `适用房` | `经济适用房` | 1,276 | review: merge |
| `耐不` | `耐不住` | 1,275 | review: merge |
| `成不变` | `一成不变` | 1,273 | review: merge |
| `覆去` | `翻来覆去` | 1,247 | review: merge |
| `渠成` | `水到渠成` | 1,239 | review: merge |
| `没话` | `没话说` | 1,237 | review: merge |
| `事到` | `事到如今` | 1,232 | review: merge |
| `熟练地` | `熟练` | 1,228 | review: merge |
| `可遇` | `可遇不可求` | 1,221 | review: merge |
| `真诚地` | `真诚` | 1,205 | review: merge |
| `囊卵巢` | `多囊卵巢` | 1,197 | review: merge |
| `别动` | `动` | 1,181 | review: merge |
| `配不` | `配不上` | 1,170 | review: merge |
| `时侯` | `时候` | 1,154 | review: merge |
| `纷歧样` | `不一样` | 1,152 | review: merge |
| `惹不` | `惹` | 1,139 | review: merge |
| `归根` | `归根到底` | 1,135 | review: merge |
| `侧重于` | `侧重` | 1,131 | review: merge |
| `事成` | `心想事成` | 1,128 | review: merge |
| `抵挡不` | `抵挡` | 1,128 | review: merge |
| `溜烟` | `一溜烟` | 1,128 | review: merge |
| `口价` | `一口价` | 1,120 | review: merge |
| `可拨打` | `拨打` | 1,114 | review: merge |
| `排入` | `排` | 1,113 | review: merge |
| `大得` | `大` | 1,096 | review: merge |
| `停不` | `停` | 1,093 | review: merge |
| `次感` | `层次感` | 1,088 | review: merge |
| `一闪而` | `一闪而过` | 1,074 | review: merge |
| `年生` | `多年生` | 1,072 | review: merge |
| `去活` | `死去活来` | 1,069 | review: merge |
| `说一` | `说` | 1,053 | review: merge |
| `过望` | `大喜过望` | 1,051 | review: merge |
| `我往` | `你来我往` | 1,044 | review: merge |
| `霎那` | `刹那` | 1,040 | review: merge |
| `偏弱` | `弱` | 1,028 | review: merge |
| `止不` | `止不住` | 1,024 | review: merge |
| `挺起` | `挺` | 1,022 | review: merge |
| `大镜` | `放大镜` | 1,020 | review: merge |
| `算得` | `算` | 1,019 | review: merge |
| `挡得` | `挡` | 992 | review: merge |
| `冷哼道` | `冷哼` | 990 | review: merge |
| `独当` | `独当一面` | 974 | review: merge |
| `说走就` | `说走就走` | 961 | review: merge |
| `老和` | `老和尚` | 959 | review: merge |
| `目中` | `目中无人` | 952 | review: merge |
| `视而不` | `视而不见` | 945 | review: merge |
| `体机` | `一体机` | 928 | review: merge |
| `校生` | `在校生` | 928 | review: merge |
| `较慢` | `慢` | 924 | review: merge |
| `供选择` | `选择` | 922 | review: merge |
| `朝一夕` | `一朝一夕` | 921 | review: merge |
| `渐行` | `渐行渐远` | 920 | review: merge |
| `继往` | `继往开来` | 920 | review: merge |
| `敏锐地` | `敏锐` | 919 | review: merge |
| `流大学` | `一流大学` | 913 | review: merge |
| `中央财经` | `中央财经大学` | 912 | review: merge |
| `掷地` | `掷地有声` | 906 | review: merge |
| `过意不` | `过意不去` | 906 | review: merge |
| `低着头` | `低头` | 899 | review: merge |
| `内膜炎` | `子宫内膜炎` | 897 | review: merge |
| `差远` | `差` | 896 | review: merge |
| `吊起` | `吊` | 878 | review: merge |
| `特莱斯` | `奥特莱斯` | 877 | review: merge |
| `的确确` | `的的确确` | 877 | review: merge |
| `烧热` | `烧` | 874 | review: merge |
| `信誉至` | `信誉至上` | 873 | review: merge |
| `激发出` | `激发` | 873 | review: merge |
| `脚踢` | `踢` | 871 | review: merge |
| `堂课` | `课` | 868 | review: merge |
| `分为二` | `一分为二` | 859 | review: merge |
| `紧跟着` | `紧跟` | 856 | review: merge |
| `喃喃地` | `喃喃` | 855 | review: merge |
| `靠谱吗` | `靠谱` | 836 | review: merge |
| `不亚` | `不亚于` | 831 | review: merge |
| `终究会` | `终究` | 828 | review: merge |
| `自下而` | `自下而上` | 826 | review: merge |
| `追不` | `追` | 825 | review: merge |
| `顾得` | `顾` | 823 | review: merge |
| `港珠` | `港珠澳大桥` | 821 | review: merge |
| `联发` | `联发科` | 821 | review: merge |
| `成竹` | `胸有成竹` | 819 | review: merge |
| `实践中` | `实践` | 817 | review: merge |
| `剧烈地` | `剧烈` | 816 | review: merge |
| `生俱来` | `与生俱来` | 806 | review: merge |
| `彩赌博` | `赌博` | 804 | review: merge |
| `无情地` | `无情` | 804 | review: merge |
| `白富` | `白富美` | 798 | review: merge |
| `旁若` | `旁若无人` | 795 | review: merge |
| `过世面` | `世面` | 794 | review: merge |
| `扬长而` | `扬长而去` | 780 | review: merge |
| `个劲地` | `一个劲` | 779 | review: merge |
| `耸了` | `耸` | 777 | review: merge |
| `见度` | `能见度` | 777 | review: merge |
| `防城` | `防城港` | 777 | review: merge |
| `重于` | `重` | 773 | review: merge |
| `细细地` | `细细` | 772 | review: merge |
| `食尸` | `食尸鬼` | 771 | review: merge |
| `为数不` | `为数不少` | 768 | review: merge |
| `事无成` | `一事无成` | 767 | review: merge |
| `求成` | `急于求成` | 767 | review: merge |
| `凝心` | `凝心聚力` | 766 | review: merge |
| `池内` | `池` | 761 | review: merge |
| `手房` | `二手房` | 759 | review: merge |
| `如此一` | `如此一来` | 756 | review: merge |
| `原原本` | `原原本本` | 754 | review: merge |
| `锅内` | `锅` | 753 | review: merge |
| `眼眶里` | `眼眶` | 750 | review: merge |
| `今曰` | `今日` | 747 | review: merge |
| `说有笑` | `有说有笑` | 747 | review: merge |
| `下无双` | `天下无双` | 743 | review: merge |
| `少废话` | `废话` | 742 | review: merge |
| `动不` | `动不动` | 741 | review: merge |
| `成百` | `成百上千` | 738 | review: merge |
| `大美` | `美女` | 737 | review: merge |
| `众矢之` | `众矢之的` | 736 | review: merge |
| `滚回` | `滚` | 735 | review: merge |
| `皇太` | `皇太后` | 733 | review: merge |
| `位一体` | `三位一体` | 730 | review: merge |
| `瞧不` | `瞧不起` | 728 | review: merge |
| `拳砸` | `砸` | 723 | review: merge |
| `住气` | `沉住气` | 722 | review: merge |
| `减至` | `减` | 720 | review: merge |
| `适时地` | `适时` | 717 | review: merge |
| `融于` | `融` | 716 | review: merge |
| `抛向` | `抛` | 715 | review: merge |
| `作主` | `做主` | 714 | review: merge |
| `靠得` | `靠得住` | 714 | review: merge |
| `步登天` | `一步登天` | 712 | review: merge |
| `成区` | `建成区` | 706 | review: merge |
| `擅于` | `善于` | 706 | review: merge |
| `细细的` | `细细` | 706 | review: merge |
| `导图` | `思维导图` | 701 | review: merge |
| `成投产` | `投产` | 701 | review: merge |
| `胸有` | `胸有成竹` | 701 | review: merge |
| `头雾水` | `一头雾水` | 700 | review: merge |
| `江小` | `江小白` | 699 | review: merge |
| `黑夜里` | `黑夜` | 698 | review: merge |
| `超一` | `一流` | 697 | review: merge |
| `弯着腰` | `弯腰` | 676 | review: merge |
| `屡遭` | `遭` | 692 | review: merge |
| `偏小` | `小` | 689 | review: merge |
| `不复返` | `一去不复返` | 686 | review: merge |
| `牠` | `它` | 686 | review: merge |
| `迸出` | `迸` | 686 | review: merge |
| `叹一口气` | `叹气` | 682 | review: merge |
| `对望一眼` | `对望` | 680 | review: merge |
| `幽幽地` | `幽幽` | 680 | review: merge |
| `时刻刻` | `时时刻刻` | 680 | review: merge |
| `了晃` | `晃` | 677 | review: merge |
| `大杀` | `大杀器` | 677 | review: merge |
| `演绎出` | `演绎` | 677 | review: merge |
| `缘份` | `缘分` | 677 | review: merge |
| `美元兑` | `美元` | 677 | review: merge |
| `致词` | `致辞` | 675 | review: merge |
| `不省` | `不省人事` | 673 | review: merge |
| `轮车` | `三轮车` | 673 | review: merge |
| `相吻合` | `吻合` | 671 | review: merge |
| `相符合` | `符合` | 671 | review: merge |
| `疲于` | `疲` | 670 | review: merge |
| `轻轻叹` | `叹` | 670 | review: merge |
| `颇高` | `高` | 670 | review: merge |
| `无痛苦` | `痛苦` | 669 | review: merge |
| `包小包` | `大包小包` | 668 | review: merge |
| `团糟` | `一团糟` | 667 | review: merge |
| `类食品` | `食品` | 667 | review: merge |
| `俯下` | `俯` | 665 | review: merge |
| `君不` | `君不见` | 665 | review: merge |

### Dropped by 2+ flags: random sample of 0 of 0 in the window

| rank | lemma | flags |
|---:|---|---|

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 16,380 (keep 11,659, drop 4,721); review merges: 572.
