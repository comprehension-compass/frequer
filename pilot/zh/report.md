# Review report: zh (pilot)

- Ranking score: `frequency`; 105,219 candidate lemmas ranked.
- Tokens counted: 2,895,738 in 5,646 documents, 5 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_zh` 1.6.4 (sha256 `2840ae8dc7e00290`); fallback `backend`, units on; honeyeater `8bc18170ed98`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-zh | 4 | 3,959 | 72,549 | 2,563,172 | alpha 3,493, exact_dup 3,737, gap 761, langid 6,524, length 1,737, near_dup 597, traditional 739, traditional_doc 498 |
| tatoeba-cmn | 1 | 1,687 | 46,989 | 332,566 | alpha 84, gap 6, length 20, near_dup 323, traditional 38,478 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 47,947. Sentences: 178,271.

## Units

Counted occurrences by kind: compound 1,351 (0.05%), compound1 18,372 (0.63%), construction 13,326 (0.46%), phrase 13,696 (0.47%), word 2,848,993 (98.39%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 1,542 | 19,728 |
| construction | 12 | 13,326 |
| phrase | 116 | 13,696 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `毕业` | 388 | 169 | 1075 |
| `说话` | 358 | 265 | 1178 |
| `回家` | 342 | 262 | 1230 |
| `担心` | 318 | 253 | 1311 |
| `报名` | 307 | 83 | 1369 |
| `睡觉` | 270 | 204 | 1533 |
| `结婚` | 257 | 172 | 1601 |
| `吃饭` | 250 | 158 | 1641 |
| `聊天` | 222 | 92 | 1817 |
| `游泳` | 218 | 152 | 1845 |
| `中华人民共和国` | 186 | 87 | 2103 |
| `下雨` | 168 | 148 | 2282 |
| `报警` | 165 | 81 | 2315 |
| `受伤` | 162 | 101 | 2346 |
| `巴黎圣日耳曼` | 160 | 37 | 2375 |
| `生气` | 144 | 120 | 2582 |
| `洗澡` | 141 | 89 | 2622 |
| `搬家` | 140 | 21 | 2636 |
| `部位` | 139 | 91 | 2600 |
| `离婚` | 128 | 45 | 2823 |
| `广东省` | 128 | 46 | 2817 |
| `上班` | 126 | 92 | 2859 |
| `出门` | 123 | 93 | 2909 |
| `消毒` | 123 | 52 | 2918 |
| `放心` | 118 | 100 | 3025 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `被 + 动词` | 4,326 | 1,821 | 65 |
| `把 + 名词 + 动词` | 4,216 | 2,082 | 71 |
| `动词 + 得 + 补语` | 1,642 | 1,004 | 206 |
| `比 + 名词 + 形容词` | 1,130 | 765 | 325 |
| `是…的` | 944 | 688 | 405 |
| `动词 + 得/不 + 补语` | 699 | 500 | 580 |
| `要…了` | 264 | 209 | 1567 |
| `动词 + 得/不 + 起` | 43 | 38 | 6354 |
| `动词 + 得/不 + 动` | 33 | 26 | 7623 |
| `动词 + 得/不 + 过` | 16 | 14 | 12609 |
| `动词 + 得/不 + 下` | 7 | 7 | 21743 |
| `〜来〜去` | 6 | 6 | 23551 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `在〜中` | 3,587 | 1,651 | 88 |
| `在〜下` | 1,203 | 806 | 302 |
| `如果…就` | 663 | 480 | 621 |
| `当…时` | 585 | 401 | 712 |
| `虽然…但` | 472 | 330 | 890 |
| `对于〜来说` | 328 | 256 | 1273 |
| `以〜为〜` | 317 | 244 | 1313 |
| `在…的时候` | 301 | 230 | 1384 |
| `尤其是` | 295 | 233 | 1409 |
| `从〜开始` | 254 | 209 | 1615 |
| `看起来` | 252 | 202 | 1627 |
| `像〜一样` | 251 | 184 | 1635 |
| `对〜来说` | 236 | 208 | 1714 |
| `和〜一起` | 227 | 177 | 1784 |
| `只要…就` | 220 | 180 | 1825 |
| `不仅…还` | 208 | 178 | 1914 |
| `打电话` | 196 | 168 | 2023 |
| `不是…而是` | 171 | 140 | 2250 |
| `在〜上` | 165 | 138 | 2314 |
| `和〜一样` | 153 | 130 | 2460 |
| `即使…也` | 149 | 134 | 2510 |
| `当…的时候` | 148 | 117 | 2528 |
| `如果…那么` | 143 | 115 | 2593 |
| `如果…的话` | 135 | 120 | 2707 |
| `尽管…但` | 132 | 103 | 2758 |

## Co-occurrence (association) table

2,852,139 tokens, 178,271 sentences. After merging and dropping items seen fewer than 5 times: 158,644 items (unigrams, UPOS votes, n-grams, pairs); 93,336 n-grams and pairs scored (n2 64,853, n3 22,385, n4 6,098). Shipped: 53,276 rows, 0.9 MB gzipped (`zh.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`zh.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `一 个` |  | 7,523 | 2,535 | 5.23 | 0.61 | 45,001 |  |
| 2 | n | `很 多` |  | 2,428 | 1,274 | 6.07 | 0.60 | 16,893 |  |
| 3 | n | `更 多` |  | 1,394 | 791 | 6.10 | 0.55 | 9,593 |  |
| 4 | n | `一 种` |  | 1,659 | 950 | 5.07 | 0.47 | 9,088 |  |
| 5 | n | `不 能` |  | 1,747 | 1,061 | 4.71 | 0.44 | 8,545 |  |
| 6 | n | `不 会` |  | 1,830 | 1,094 | 4.32 | 0.41 | 7,897 |  |
| 7 | n | `亿 元` |  | 629 | 197 | 8.97 | 0.74 | 7,086 |  |
| 8 | n | `过程 中` |  | 759 | 498 | 7.17 | 0.60 | 6,605 |  |
| 9 | n | `句 话` |  | 481 | 184 | 10.18 | 0.81 | 6,331 |  |
| 10 | n | `小 编` |  | 518 | 272 | 9.19 | 0.74 | 6,294 |  |
| 11 | n | `都 是` |  | 1,734 | 1,020 | 3.78 | 0.35 | 6,242 |  |
| 12 | n | `两 个` |  | 1,051 | 668 | 5.18 | 0.45 | 5,854 |  |
| 13 | n | `看 到` |  | 1,046 | 702 | 5.24 | 0.46 | 5,828 |  |
| 14 | n | `才 能` |  | 708 | 479 | 6.84 | 0.57 | 5,624 |  |
| 15 | n | `也 是` |  | 1,732 | 1,028 | 3.52 | 0.33 | 5,606 |  |
| 16 | n | `一 条` |  | 359 | 273 | 10.76 | 0.83 | 5,361 |  |
| 17 | n | `梦 见` |  | 444 | 56 | 9.50 | 0.75 | 5,335 |  |
| 18 | n | `万 元` |  | 527 | 160 | 8.00 | 0.64 | 5,042 |  |
| 19 | n | `找 到` |  | 632 | 463 | 6.43 | 0.53 | 4,687 |  |
| 20 | n | `招聘 人数` |  | 325 | 39 | 10.96 | 0.84 | 4,685 |  |
| 21 | n | `不 知道` |  | 787 | 564 | 5.23 | 0.44 | 4,460 |  |
| 22 | n | `情况 下` |  | 565 | 413 | 6.76 | 0.55 | 4,372 |  |
| 23 | n | `据 报道` |  | 181 | 77 | 17.18 | 1.23 | 4,363 |  |
| 24 | n | `一 次` |  | 934 | 642 | 4.55 | 0.39 | 4,335 |  |
| 25 | n | `到 了` |  | 1,488 | 868 | 3.25 | 0.30 | 4,241 |  |
| 26 | n | `说 过` |  | 599 | 133 | 6.00 | 0.49 | 3,945 |  |
| 27 | n | `疫情 防控` |  | 251 | 89 | 11.49 | 0.85 | 3,876 |  |
| 28 | n | `一定 要` |  | 493 | 343 | 6.74 | 0.54 | 3,832 |  |
| 29 | n | `月 学历 要求` |  | 307 | 32 | 8.91 | 0.68 | 3,734 |  |
| 30 | n | `解决 方案` |  | 312 | 163 | 9.46 | 0.72 | 3,662 |  |
| 31 | n | `做 好` |  | 619 | 344 | 5.50 | 0.45 | 3,631 |  |
| 32 | n | `只 有` |  | 663 | 471 | 5.13 | 0.43 | 3,598 |  |
| 33 | n | `适用 于` |  | 299 | 202 | 9.25 | 0.70 | 3,550 |  |
| 34 | n | `个 人` |  | 1,040 | 635 | 3.67 | 0.32 | 3,502 |  |
| 35 | n | `全职 经验 要求` |  | 244 | 28 | 9.92 | 0.73 | 3,378 |  |
| 36 | n | `是 一 个` |  | 1,098 | 722 | 3.42 | 0.30 | 3,376 |  |
| 37 | n | `说 过 一 句` |  | 274 | 51 | 8.85 | 0.66 | 3,362 |  |
| 38 | n | `手 游` |  | 265 | 51 | 9.92 | 0.74 | 3,333 |  |
| 39 | n | `公司 名称` |  | 323 | 38 | 8.38 | 0.64 | 3,328 |  |
| 40 | n | `更 好` |  | 574 | 411 | 5.24 | 0.43 | 3,154 |  |
| 41 | n | `性别 要求` |  | 247 | 28 | 9.65 | 0.71 | 3,143 |  |
| 42 | n | `还 有` |  | 717 | 565 | 4.41 | 0.37 | 3,133 |  |
| 43 | n | `经验 要求` |  | 315 | 33 | 8.23 | 0.63 | 3,110 |  |
| 44 | n | `是 一 种` |  | 609 | 422 | 4.75 | 0.39 | 3,085 |  |
| 45 | n | `几 个` |  | 548 | 408 | 5.18 | 0.42 | 3,042 |  |
| 46 | n | `件 事` |  | 261 | 201 | 9.29 | 0.69 | 2,978 |  |
| 47 | n | `很 好` |  | 646 | 489 | 4.59 | 0.38 | 2,962 |  |
| 48 | n | `工作 类型` |  | 314 | 32 | 7.80 | 0.59 | 2,929 |  |
| 49 | n | `个 月` |  | 738 | 472 | 4.10 | 0.34 | 2,919 |  |
| 50 | n | `一 句` |  | 474 | 187 | 5.48 | 0.44 | 2,909 |  |

### Verb pairs in the queue

_none_

## Rank shifts against the live snapshot (`reference/lemmas/zh.json`)

_No live snapshot to compare with._

## Ported frequer checks

### Form-ratio outliers (0)

A surface form far more frequent than the lemma's median form.

_none_

### Singular/plural mismatch (0)

Lemma looks like a plural whose stripped form maps to another listed lemma.

_none_

### Lemma consistency (1)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 4036 | `人家` | 81 | alone, `人家` lemmatises to `人家#rénjiā` (rank 6,246) |

### Short lemmas (1,454)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `的` | 151,864 | `的` -> `的` |
| 2 | `是` | 38,982 | `是` -> `是` |
| 4 | `在` | 33,422 | `在` -> `在` |
| 5 | `一` | 31,510 | `一` -> `一`, `1` -> `一`, `①` -> `一`, `I` -> `?` |
| 6 | `我` | 26,559 | `我` -> `我` |
| 7 | `不` | 23,766 | `不` -> `不` |
| 8 | `和` | 21,479 | `和` -> `和` |
| 9 | `个` | 21,379 | `个` -> `个` |
| 10 | `这` | 17,203 | `这` -> `这` |
| 11 | `有` | 17,082 | `有` -> `有` |
| 12 | `你` | 15,699 | `你` -> `你` |
| 13 | `就` | 12,440 | `就` -> `就` |
| 14 | `他` | 12,397 | `他` -> `他` |
| 15 | `会` | 11,026 | `会` -> `会` |
| 16 | `也` | 11,019 | `也` -> `也` |
| 17 | `人` | 10,899 | `人` -> `人` |
| 19 | `多` | 10,168 | `多` -> `多` |
| 20 | `年` | 10,168 | `年` -> `年` |
| 21 | `很` | 10,117 | `很` -> `很` |
| 25 | `都` | 9,233 | `都` -> `都` |
| 26 | `对` | 9,163 | `对` -> `对` |
| 27 | `等` | 8,828 | `等` -> `等` |
| 28 | `要` | 8,503 | `要` -> `要` |
| 29 | `能` | 8,027 | `能` -> `能` |
| 30 | `与` | 7,705 | `与` -> `与` |

_1,429 more not shown._

### Case merges (0)

Non-lowercase lemmas, with the lowercase twin where one is listed.

_none_

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 747 (74.7%).

Ours only: `被 + 动词`, `把 + 名词 + 动词`, `在〜中`, `汤姆`, `百分之`, `十`, `前`, `动词 + 得 + 补语`, `二〇二二`, `不要`, `材料`, `儿#r`, `客户`, `二十`, `品牌`, `在〜下`, `项`, `比 + 名词 + 形容词`, `句`, `十二`, `有限公司`, `提升`, `效果`, `的话`, `周#week`

wordfreq only: `〇〇〇〇`, `〇〇〇`, `政治`, `第`, `香港`, `人民`, `自由`, `当时`, `英国`, `委员会`, `人口`, `民主`, `事件`, `零点零`, `县`, `总统`, `战争`, `照片`, `时期`, `故事`, `举行`, `艺术`, `独立`, `人类`, `制`

## Foreign-word candidates

_none_

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 51 | `中国` | 4,795 | PROPN 98%, capitalised forms 0% |
| 104 | `汤姆` | 3,183 | PROPN 100%, capitalised forms 0% |
| 132 | `美国` | 2,539 | PROPN 99%, capitalised forms 0% |
| 399 | `北京` | 952 | PROPN 100%, capitalised forms 0% |
| 418 | `培训` | 911 | PROPN 76%, capitalised forms 0% |
| 422 | `日本` | 903 | PROPN 99%, capitalised forms 0% |
| 450 | `安装` | 860 | PROPN 59%, capitalised forms 0% |
| 466 | `上海` | 840 | PROPN 100%, capitalised forms 0% |
| 478 | `王` | 822 | PROPN 100%, capitalised forms 0% |
| 515 | `玛丽` | 773 | PROPN 100%, capitalised forms 0% |
| 583 | `台湾` | 697 | PROPN 96%, capitalised forms 0% |
| 654 | `韩国` | 634 | PROPN 100%, capitalised forms 0% |
| 776 | `红` | 541 | PROPN 52%, capitalised forms 0% |
| 897 | `马` | 469 | PROPN 63%, capitalised forms 0% |
| 933 | `欧洲` | 448 | PROPN 99%, capitalised forms 0% |
| 946 | `李` | 442 | PROPN 100%, capitalised forms 0% |
| 977 | `亚洲` | 429 | PROPN 97%, capitalised forms 0% |
| 1026 | `英国` | 408 | PROPN 99%, capitalised forms 0% |
| 1041 | `香港` | 402 | PROPN 100%, capitalised forms 0% |
| 1061 | `深圳` | 393 | PROPN 100%, capitalised forms 0% |
| 1095 | `广州` | 382 | PROPN 100%, capitalised forms 0% |
| 1163 | `刘` | 362 | PROPN 100%, capitalised forms 0% |
| 1206 | `俄罗斯` | 350 | PROPN 100%, capitalised forms 0% |
| 1218 | `微信` | 346 | PROPN 100%, capitalised forms 0% |
| 1232 | `法国` | 342 | PROPN 95%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 89.3% | 0.889 |
| juilland_u | 95.7% | 0.978 |
| juilland_u_corrected | 95.5% | 0.976 |
| dp_adjusted | 94.3% | 0.960 |
| cd_blend | 93.9% | 0.961 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `除了…外` | 6831 | 4753 | -2,078 | 40 | 40 | 0.840 | 0.642 |
| `看似` | 6941 | 4922 | -2,019 | 39 | 38 | 0.848 | 0.625 |
| `责任编辑` | 6824 | 4828 | -1,996 | 40 | 39 | 0.838 | 0.676 |
| `免责` | 6861 | 4921 | -1,940 | 39 | 38 | 0.816 | 0.678 |
| `敬请` | 6444 | 4510 | -1,934 | 43 | 43 | 0.842 | 0.656 |
| `贤芝` | 2126 | 48971 | +46,845 | 185 | 1 | 0.000 | 0.994 |
| `中智` | 2264 | 48972 | +46,708 | 171 | 1 | 0.000 | 0.994 |
| `徐天宏` | 2309 | 48973 | +46,664 | 167 | 1 | 0.000 | 0.989 |
| `温铁军` | 3101 | 48974 | +45,873 | 115 | 1 | 0.000 | 0.979 |
| `棒磨机` | 3682 | 48975 | +45,293 | 93 | 1 | -0.000 | 0.996 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `所有人` | 5420 | 4838 | -582 | 55 | 55 | 0.876 | 0.542 |
| `尽力` | 5567 | 4999 | -568 | 53 | 50 | 0.863 | 0.575 |
| `火爆` | 5499 | 4940 | -559 | 54 | 48 | 0.863 | 0.537 |
| `不适` | 5458 | 4914 | -544 | 54 | 49 | 0.870 | 0.540 |
| `跳舞` | 5517 | 4976 | -541 | 54 | 54 | 0.853 | 0.579 |
| `贤芝` | 2126 | 55225 | +53,099 | 185 | 1 | 0.000 | 0.994 |
| `中智` | 2264 | 55226 | +52,962 | 171 | 1 | 0.000 | 0.994 |
| `徐天宏` | 2309 | 55227 | +52,918 | 167 | 1 | 0.000 | 0.989 |
| `温铁军` | 3101 | 55228 | +52,127 | 115 | 1 | 0.000 | 0.979 |
| `棒磨机` | 3682 | 55229 | +51,547 | 93 | 1 | -0.000 | 0.996 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `比起` | 5584 | 4984 | -600 | 53 | 47 | 0.858 | 0.591 |
| `尽力` | 5567 | 4973 | -594 | 53 | 50 | 0.863 | 0.575 |
| `火爆` | 5499 | 4915 | -584 | 54 | 48 | 0.863 | 0.537 |
| `所有人` | 5420 | 4847 | -573 | 55 | 55 | 0.876 | 0.542 |
| `跳舞` | 5517 | 4952 | -565 | 54 | 54 | 0.853 | 0.579 |
| `贤芝` | 2126 | 49812 | +47,686 | 185 | 1 | 0.000 | 0.994 |
| `中智` | 2264 | 49813 | +47,549 | 171 | 1 | 0.000 | 0.994 |
| `徐天宏` | 2309 | 49814 | +47,505 | 167 | 1 | 0.000 | 0.989 |
| `温铁军` | 3101 | 49815 | +46,714 | 115 | 1 | 0.000 | 0.979 |
| `棒磨机` | 3682 | 49816 | +46,134 | 93 | 1 | -0.000 | 0.996 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `随之` | 5830 | 4649 | -1,181 | 50 | 48 | 0.883 | 0.554 |
| `坚实` | 5853 | 4699 | -1,154 | 49 | 48 | 0.869 | 0.554 |
| `无比` | 5946 | 4846 | -1,100 | 48 | 46 | 0.859 | 0.578 |
| `六百` | 5616 | 4538 | -1,078 | 52 | 50 | 0.873 | 0.546 |
| `火爆` | 5499 | 4424 | -1,075 | 54 | 48 | 0.863 | 0.537 |
| `菱镁` | 4471 | 24854 | +20,383 | 72 | 1 | 0.000 | 0.997 |
| `游蚊` | 4001 | 21848 | +17,847 | 83 | 1 | -0.000 | 0.996 |
| `棒磨机` | 3682 | 19925 | +16,243 | 93 | 1 | -0.000 | 0.996 |
| `钠斯` | 3754 | 18015 | +14,261 | 91 | 1 | -0.000 | 0.994 |
| `中智` | 2264 | 14197 | +11,933 | 171 | 1 | 0.000 | 0.994 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `属` | 5637 | 4623 | -1,014 | 52 | 52 | 0.857 | 0.586 |
| `从何而来` | 5840 | 4829 | -1,011 | 49 | 49 | 0.851 | 0.576 |
| `跳舞` | 5517 | 4507 | -1,010 | 54 | 54 | 0.853 | 0.579 |
| `随之` | 5830 | 4832 | -998 | 50 | 48 | 0.883 | 0.554 |
| `坚实` | 5853 | 4864 | -989 | 49 | 48 | 0.869 | 0.554 |
| `周绮` | 4449 | 16533 | +12,084 | 72 | 1 | -0.000 | 0.989 |
| `菱镁` | 4471 | 16534 | +12,063 | 72 | 1 | 0.000 | 0.997 |
| `游蚊` | 4001 | 15922 | +11,921 | 83 | 1 | -0.000 | 0.996 |
| `小惠` | 4071 | 15925 | +11,854 | 81 | 1 | 0.000 | 0.990 |
| `棒磨机` | 3682 | 15313 | +11,631 | 93 | 1 | -0.000 | 0.996 |



## Junk-filter heuristics

Rules on: diversity, citation, shape, propn_band; accent merges at ratio None. Window: the 50,475 ranked lemmas (after the exclusion list) that fill the top 50,000. Actions: drop 13, keep 43,415, number-drop 462, pending 6,585.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band | propn_usage |
|---|---:|---:|---:|---:|---:|---:|
| diversity | 596 | 0 | 0 | 8 | 114 | 0 |
| citation | 0 | 6 | 0 | 0 | 0 | 0 |
| foreign | 0 | 0 | 0 | 0 | 0 | 0 |
| shape | 8 | 0 | 0 | 784 | 56 | 0 |
| propn_band | 114 | 0 | 0 | 56 | 7,242 | 0 |
| propn_usage | 0 | 0 | 0 | 0 | 0 | 0 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 0.

### Low diversity

Documents reached / documents expected at random, below 0.2 (frequency >= 20): 596 in the window. For comparison, each log2-frequency band's 2nd percentile: 16-31: 0.05, 32-63: 0.07, 64-127: 0.12, 128-255: 0.19, 256-511: 0.17, 512-1023: 0.27, 1024-2047: 0.32.

Examples: `招聘` (444), `基金` (462), `操` (663), `白癜风` (819), `应急` (856), `美女` (860), `证券` (880), `学历` (898), `啪啪` (903), `搜索引擎` (1083), `商标` (1111), `梦见` (1136), `妹子` (1154), `薪水` (1188), `传奇` (1190), `诱惑` (1254), `全职` (1279), `速` (1311), `住房` (1317), `性感` (1322), `考生` (1323), `三国` (1341), `极品` (1393), `整容` (1404), `电网` (1527), `女神` (1706), `救援` (1714), `电缆` (1770), `温` (1798), `砂` (1823), `少妇` (1856), `供水` (1932), `中小企业` (1953), `自慰` (1957), `天线` (1976), `光纤` (1989), `癫痫` (2074), `当事人` (2091), `陶瓷` (2106), `贤芝` (2126)

### Accent merges (0)

| from | into | frequency moved | evidence |
|---|---|---:|---|

### Dropped by 2+ flags: random sample of 13 of 13 in the window

| rank | lemma | flags |
|---:|---|---|
| 41552 | `荀` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 41646 | `藕` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 42319 | `邢` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 42534 | `闫` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 43827 | `中国残疾人福利基金会` | shape: length 10; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 44367 | `仉` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 44988 | `全国五一劳动奖章` | shape: length 8; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45156 | `共青团中央书记处` | shape: length 8; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45733 | `加布里埃尔皮拉尼` | shape: length 8; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 45879 | `匠` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48511 | `巧妇难为无米之炊` | shape: length 8; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 48791 | `廓` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 50414 | `旐` | shape: length 1; propn_band: tagged PROPN by the release (no case or dictionary evidence) |

### Single flag, not yet reviewed: 6,585 (kept until reviewed)

| rank | lemma | flag |
|---:|---|---|
| 51 | `中国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 104 | `汤姆` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 132 | `美国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 399 | `北京` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 418 | `培训` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 422 | `日本` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 444 | `招聘` | diversity: in 120 documents, 0.15 of the 870 occurrences' random spread (threshold 0.2) |
| 450 | `安装` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 462 | `基金` | diversity: in 106 documents, 0.14 of the 844 occurrences' random spread (threshold 0.2) |
| 466 | `上海` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 478 | `王` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 515 | `玛丽` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 583 | `台湾` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 655 | `韩国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 663 | `操` | diversity: in 60 documents, 0.10 of the 623 occurrences' random spread (threshold 0.2) |
| 778 | `红` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 819 | `白癜风` | diversity: in 34 documents, 0.07 of the 514 occurrences' random spread (threshold 0.2) |
| 856 | `应急` | diversity: in 88 documents, 0.19 of the 495 occurrences' random spread (threshold 0.2) |
| 860 | `美女` | diversity: in 57 documents, 0.12 of the 494 occurrences' random spread (threshold 0.2) |
| 880 | `证券` | diversity: in 68 documents, 0.15 of the 478 occurrences' random spread (threshold 0.2) |
| 898 | `学历` | diversity: in 87 documents, 0.19 of the 469 occurrences' random spread (threshold 0.2) |
| 899 | `马` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 903 | `啪啪` | diversity: in 26 documents, 0.06 of the 466 occurrences' random spread (threshold 0.2) |
| 935 | `欧洲` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 948 | `李` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 979 | `亚洲` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1028 | `英国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1043 | `香港` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1063 | `深圳` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1083 | `搜索引擎` | diversity: in 44 documents, 0.12 of the 386 occurrences' random spread (threshold 0.2) |
| 1097 | `广州` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1111 | `商标` | diversity: in 42 documents, 0.12 of the 377 occurrences' random spread (threshold 0.2) |
| 1136 | `梦见` | diversity: in 46 documents, 0.13 of the 370 occurrences' random spread (threshold 0.2) |
| 1154 | `妹子` | diversity: in 34 documents, 0.10 of the 365 occurrences' random spread (threshold 0.2) |
| 1165 | `刘` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1188 | `薪水` | diversity: in 68 documents, 0.20 of the 357 occurrences' random spread (threshold 0.2) |
| 1190 | `传奇` | diversity: in 58 documents, 0.17 of the 356 occurrences' random spread (threshold 0.2) |
| 1209 | `俄罗斯` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1221 | `微信` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1235 | `法国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1247 | `意大利` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1254 | `诱惑` | diversity: in 55 documents, 0.17 of the 335 occurrences' random spread (threshold 0.2) |
| 1279 | `全职` | diversity: in 45 documents, 0.14 of the 327 occurrences' random spread (threshold 0.2) |
| 1282 | `林` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1311 | `速` | diversity: in 41 documents, 0.13 of the 319 occurrences' random spread (threshold 0.2) |
| 1317 | `住房` | diversity: in 43 documents, 0.14 of the 317 occurrences' random spread (threshold 0.2) |
| 1322 | `性感` | diversity: in 46 documents, 0.15 of the 316 occurrences' random spread (threshold 0.2) |
| 1323 | `考生` | diversity: in 59 documents, 0.19 of the 316 occurrences' random spread (threshold 0.2) |
| 1327 | `加快` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1336 | `平` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1341 | `三国` | diversity: in 19 documents, 0.06 of the 311 occurrences' random spread (threshold 0.2) |
| 1393 | `极品` | diversity: in 34 documents, 0.12 of the 300 occurrences' random spread (threshold 0.2) |
| 1404 | `整容` | diversity: in 11 documents, 0.04 of the 297 occurrences' random spread (threshold 0.2) |
| 1417 | `云` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1428 | `陈` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1452 | `德国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1494 | `乌克兰` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1527 | `电网` | diversity: in 28 documents, 0.11 of the 271 occurrences' random spread (threshold 0.2) |
| 1540 | `安` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1548 | `广东` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1578 | `曼联` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1595 | `宝宝` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1663 | `百度` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1706 | `女神` | diversity: in 45 documents, 0.19 of the 238 occurrences' random spread (threshold 0.2) |
| 1714 | `救援` | diversity: in 33 documents, 0.14 of the 237 occurrences' random spread (threshold 0.2) |
| 1770 | `电缆` | diversity: in 34 documents, 0.15 of the 230 occurrences' random spread (threshold 0.2) |
| 1798 | `温` | diversity: in 37 documents, 0.17 of the 226 occurrences' random spread (threshold 0.2) |
| 1804 | `巴黎` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1823 | `砂` | diversity: in 18 documents, 0.08 of the 222 occurrences' random spread (threshold 0.2) |
| 1840 | `成都` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1856 | `少妇` | diversity: in 29 documents, 0.14 of the 217 occurrences' random spread (threshold 0.2) |
| 1872 | `印度` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1898 | `巴塞罗那` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1932 | `供水` | diversity: in 29 documents, 0.14 of the 207 occurrences' random spread (threshold 0.2) |
| 1945 | `西班牙` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1950 | `杨` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1953 | `中小企业` | diversity: in 40 documents, 0.20 of the 204 occurrences' random spread (threshold 0.2) |
| 1957 | `自慰` | diversity: in 29 documents, 0.14 of the 204 occurrences' random spread (threshold 0.2) |
| 1976 | `天线` | diversity: in 9 documents, 0.05 of the 202 occurrences' random spread (threshold 0.2) |
| 1980 | `澳门` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 1989 | `光纤` | diversity: in 10 documents, 0.05 of the 201 occurrences' random spread (threshold 0.2) |
| 2004 | `武汉` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2040 | `山东` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2074 | `癫痫` | diversity: in 23 documents, 0.12 of the 191 occurrences' random spread (threshold 0.2) |
| 2085 | `广西` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2091 | `当事人` | diversity: in 35 documents, 0.19 of the 189 occurrences' random spread (threshold 0.2) |
| 2106 | `陶瓷` | diversity: in 35 documents, 0.19 of the 188 occurrences' random spread (threshold 0.2) |
| 2114 | `中华人民共和国` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2126 | `贤芝` | diversity: in 1 documents, 0.01 of the 185 occurrences' random spread (threshold 0.2) |
| 2127 | `重庆` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2163 | `图表` | diversity: in 25 documents, 0.14 of the 180 occurrences' random spread (threshold 0.2) |
| 2192 | `第三方` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2214 | `新冠` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2222 | `赵` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2228 | `经营者` | diversity: in 19 documents, 0.11 of the 175 occurrences' random spread (threshold 0.2) |
| 2237 | `澳大利亚` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2248 | `抖音` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2264 | `中智` | diversity: in 1 documents, 0.01 of the 171 occurrences' random spread (threshold 0.2); propn_band: tagged PROPN by the release (no case or dictionary evidence) |
| 2275 | `天气预报` | diversity: in 23 documents, 0.14 of the 170 occurrences' random spread (threshold 0.2) |
| 2287 | `孙` | propn_band: tagged PROPN by the release (no case or dictionary evidence) |

_6,485 more in the flags sidecar._

Reviewed decisions applied in the window: 0 (keep 0, drop 0); review merges: 0.
