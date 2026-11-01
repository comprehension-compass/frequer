# Review report: de (full)

- Ranking score: `frequency`; 200,000 candidate lemmas ranked.
- Tokens counted: 451,548,754 in 1,427,010 documents, 274 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_de` 1.5.1 (sha256 `c90dad72ceb2ef3c`); fallback `spacy-list`, units on; honeyeater `c07c70158590`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-de-deep | 102 | 524,285 | 7,329,833 | 165,429,911 | alpha 132,824, exact_dup 488,154, gap 237,300, langid 377,319, length 1,429,662, near_dup 92,908 |
| hplt-v2-de | 170 | 887,011 | 11,955,050 | 280,008,929 | alpha 228,346, exact_dup 845,733, gap 399,834, langid 618,332, length 2,396,507, near_dup 145,589 |
| tatoeba-deu | 2 | 15,714 | 780,742 | 6,109,914 | alpha 35, exact_dup 10, gap 404, length 1,172, near_dup 3,310 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 7,319,938. Sentences: 38,264,311.

## Units

Counted occurrences by kind: compound 3,017,173 (0.67%), compound1 45,314,413 (10.04%), construction 5,350,583 (1.18%), phrase 4,730,973 (1.05%), word 393,135,612 (87.06%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 1,508,373 | 49,243,216 |
| construction | 15 | 5,359,924 |
| phrase | 1,076 | 4,738,158 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `damit` | 399,146 | 262,112 | 107 |
| `dabei` | 354,755 | 244,624 | 118 |
| `dazu` | 281,561 | 198,416 | 146 |
| `natürlich` | 255,109 | 167,778 | 156 |
| `dafür` | 194,181 | 146,054 | 211 |
| `Möglichkeit` | 181,904 | 133,424 | 227 |
| `anbieten` | 166,153 | 121,015 | 245 |
| `kostenlos` | 165,138 | 89,494 | 246 |
| `darauf` | 159,735 | 121,335 | 251 |
| `persönlich` | 151,172 | 106,551 | 261 |
| `zusätzlich` | 134,338 | 100,808 | 288 |
| `davon` | 133,218 | 103,410 | 297 |
| `darüber` | 131,140 | 103,108 | 303 |
| `Erfahrung` | 122,006 | 89,460 | 320 |
| `Verfügung` | 116,741 | 90,676 | 337 |
| `stattfinden` | 113,640 | 82,691 | 349 |
| `sich befinden` | 112,712 | 80,547 | 352 |
| `unterschiedlich` | 111,265 | 85,957 | 357 |
| `sich freuen` | 108,472 | 86,238 | 610 |
| `Entwicklung` | 105,489 | 71,904 | 375 |
| `aussehen` | 100,672 | 73,756 | 372 |
| `bearbeiten` | 99,444 | 32,282 | 397 |
| `Leistung` | 98,734 | 61,752 | 399 |
| `Mitarbeiter` | 98,287 | 58,914 | 403 |
| `Lösung` | 93,571 | 63,541 | 422 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `werden + Partizip II` | 3,110,140 | 857,694 | 15 |
| `werden + Infinitiv` | 524,971 | 300,650 | 91 |
| `um … zu + Infinitiv` | 505,505 | 290,688 | 94 |
| `sein + Partizip II` | 494,384 | 309,040 | 95 |
| `lassen + Infinitiv` | 338,656 | 225,473 | 121 |
| `würde + Infinitiv` | 201,618 | 120,250 | 202 |
| `sein + zu + Infinitiv` | 122,884 | 96,972 | 326 |
| `gehen + Infinitiv` | 21,874 | 19,147 | 2044 |
| `ohne … zu + Infinitiv` | 20,330 | 18,437 | 2124 |
| `Modalverb + Infinitiv Perfekt` | 8,217 | 7,403 | 4239 |
| `haben … zu + Infinitiv` | 6,589 | 6,233 | 5659 |
| `werden + Infinitiv Perfekt` | 3,325 | 3,159 | 8269 |
| `statt … zu + Infinitiv` | 1,040 | 1,009 | 19502 |
| `(an)statt … zu + Infinitiv` | 354 | 347 | 43574 |
| `vorhaben + zu + Infinitiv` | 37 | 37 | - |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `es gibt` | 640,096 | 342,019 | 76 |
| `nicht mehr` | 186,729 | 130,852 | 222 |
| `vor allem` | 154,312 | 116,929 | 255 |
| `ein paar` | 111,546 | 82,059 | 356 |
| `für etwas sorgen` | 97,199 | 77,472 | 406 |
| `zum Beispiel` | 86,352 | 65,419 | 462 |
| `im Rahmen` | 85,084 | 61,976 | 472 |
| `immer wieder` | 78,468 | 63,331 | 517 |
| `zu etwas gehören` | 73,163 | 61,679 | 568 |
| `immer noch` | 70,484 | 55,050 | 592 |
| `nicht nur … sondern auch` | 70,418 | 61,639 | 593 |
| `unter anderem` | 63,514 | 53,948 | 670 |
| `sowohl … als auch` | 63,274 | 55,489 | 672 |
| `über etwas verfügen` | 62,548 | 48,393 | 684 |
| `es handelt sich um etwas` | 60,839 | 49,453 | 705 |
| `auch wenn` | 60,290 | 51,090 | 712 |
| `je nach` | 53,814 | 44,684 | 795 |
| `in der Regel` | 50,320 | 38,979 | 852 |
| `darüber hinaus` | 50,092 | 42,794 | 859 |
| `aus etwas bestehen` | 49,161 | 40,162 | 880 |
| `vor Ort` | 47,160 | 37,263 | 914 |
| `ein wenig` | 47,124 | 37,010 | 915 |
| `zusammen mit` | 43,189 | 37,639 | 1010 |
| `es kommt zu etwas` | 42,089 | 34,681 | 1033 |
| `zwar … aber` | 39,344 | 34,629 | 1099 |

## Co-occurrence (association) table

127,125,104 tokens, 11,123,018 sentences. After merging and dropping items seen fewer than 5 times: 5,354,148 items (unigrams, UPOS votes, n-grams, pairs); 4,361,826 n-grams and pairs scored (n2 1,673,005, n3 1,840,610, n4 783,281, p2 59,177, p3 5,753). Shipped: 400,000 rows, 8.7 MB gzipped (`de.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`de.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `z. b` |  | 15,486 | 9,238 | 11.79 | 0.91 | 253,779 |  |
| 2 | n | `personenbezogen datum` |  | 12,396 | 2,371 | 11.06 | 0.83 | 185,670 |  |
| 3 | n | `finden sie` |  | 41,703 | 29,371 | 4.35 | 0.38 | 182,008 |  |
| 4 | p | `machen sich` | `sich machen` | 18,986 | 15,798 | 7.43 | 0.58 | 159,973 |  |
| 5 | n | `rund um` |  | 19,229 | 15,572 | 6.99 | 0.55 | 157,525 |  |
| 6 | n | `sehr gut` |  | 25,268 | 17,484 | 5.64 | 0.46 | 153,087 |  |
| 7 | n | `per e-mail` |  | 10,014 | 7,765 | 10.25 | 0.75 | 129,460 |  |
| 8 | n | `hundert prozent` |  | 11,381 | 8,180 | 8.55 | 0.64 | 117,179 |  |
| 9 | n | `weiter information` |  | 13,619 | 10,840 | 7.02 | 0.53 | 109,019 |  |
| 10 | n | `absatz eins` |  | 9,735 | 2,840 | 8.92 | 0.65 | 107,090 |  |
| 11 | n | `noch nicht` |  | 27,913 | 22,231 | 3.70 | 0.30 | 94,664 |  |
| 12 | n | `an ende` |  | 15,658 | 12,973 | 5.41 | 0.42 | 92,545 |  |
| 13 | n | `tom und maria` |  | 6,359 | 2,282 | 10.04 | 0.70 | 86,676 |  |
| 14 | n | `quelltext bearbeiten` |  | 4,993 | 702 | 12.45 | 0.85 | 85,909 |  |
| 15 | n | `million euro` |  | 7,155 | 4,057 | 9.11 | 0.65 | 78,974 |  |
| 16 | n | `bitte beachten` |  | 6,981 | 5,828 | 9.20 | 0.65 | 78,411 |  |
| 17 | p | `finden hier` | `hierfinden` | 8,138 | 6,490 | 8.33 | 0.60 | 78,402 |  |
| 18 | n | `wir freuen sich` |  | 10,168 | 8,840 | 6.61 | 0.49 | 78,259 | sich freuen |
| 19 | n | `information zu` |  | 19,203 | 14,705 | 4.02 | 0.32 | 75,862 |  |
| 20 | n | `schülerin und schüler` |  | 4,068 | 2,071 | 12.87 | 0.86 | 72,646 |  |
| 21 | n | `jahr alt` |  | 10,390 | 7,919 | 6.26 | 0.46 | 71,669 |  |
| 22 | n | `professor doktor` |  | 5,096 | 2,431 | 11.04 | 0.76 | 71,467 |  |
| 23 | n | `umgang mit` |  | 8,823 | 7,180 | 6.27 | 0.45 | 70,357 |  |
| 24 | n | `letzte jahr` |  | 9,978 | 8,601 | 6.27 | 0.46 | 69,030 |  |
| 25 | n | `egal ob` |  | 6,214 | 5,641 | 9.02 | 0.63 | 68,164 |  |
| 26 | n | `book of ra` |  | 3,225 | 768 | 14.65 | 0.96 | 67,474 |  |
| 27 | n | `in bereich` |  | 17,169 | 13,092 | 3.86 | 0.30 | 65,732 |  |
| 28 | n | `social media` |  | 3,449 | 1,843 | 13.46 | 0.89 | 62,255 |  |
| 29 | n | `ich glauben` |  | 10,245 | 7,461 | 5.54 | 0.41 | 62,246 |  |
| 30 | n | `in den letzte` |  | 9,870 | 8,616 | 5.07 | 0.37 | 61,028 |  |
| 31 | n | `an samstag` |  | 8,310 | 5,927 | 6.20 | 0.45 | 60,622 |  |
| 32 | n | `ich denken` |  | 11,474 | 8,395 | 5.04 | 0.37 | 60,593 |  |
| 33 | n | `kind und jugendliche` |  | 4,284 | 2,892 | 10.20 | 0.69 | 59,014 |  |
| 34 | n | `erhalten sie` |  | 13,859 | 11,040 | 4.22 | 0.32 | 57,389 |  |
| 35 | n | `vergangen jahr` |  | 6,321 | 5,430 | 7.48 | 0.52 | 55,643 |  |
| 36 | n | `in internet` |  | 11,950 | 9,159 | 4.34 | 0.32 | 55,345 |  |
| 37 | n | `bieten ihnen` |  | 7,824 | 6,523 | 6.29 | 0.45 | 53,820 |  |
| 38 | n | `noch nie` |  | 7,431 | 6,318 | 6.45 | 0.46 | 53,639 |  |
| 39 | p | `nehmen sich` | `sich nehmen` | 6,485 | 5,580 | 7.25 | 0.51 | 52,864 |  |
| 40 | n | `zu thema` |  | 14,516 | 11,576 | 3.78 | 0.29 | 52,063 |  |
| 41 | n | `milliarde euro` |  | 4,237 | 2,363 | 9.88 | 0.66 | 52,026 |  |
| 42 | n | `art und weise` |  | 3,365 | 3,115 | 11.23 | 0.74 | 51,687 |  |
| 43 | n | `in dieser fall` |  | 7,426 | 6,023 | 5.31 | 0.38 | 51,286 |  |
| 44 | p | `informieren sich` | `sich informieren` | 4,833 | 4,117 | 8.71 | 0.59 | 49,817 |  |
| 45 | n | `ich hoffen` |  | 7,392 | 5,891 | 5.90 | 0.42 | 49,434 |  |
| 46 | n | `vierundzwanzig stunde` |  | 4,025 | 3,257 | 9.94 | 0.67 | 49,179 |  |
| 47 | n | `zehn jahr` |  | 7,635 | 6,392 | 5.93 | 0.42 | 48,873 |  |
| 48 | n | `klicken sie` |  | 7,646 | 4,395 | 5.59 | 0.40 | 48,662 |  |
| 49 | n | `finden sie hier` |  | 6,676 | 5,289 | 6.53 | 0.46 | 48,581 |  |
| 50 | n | `zugang zu` |  | 7,505 | 6,077 | 5.43 | 0.39 | 48,273 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `machen sich` | `sich machen` | 18,986 | 15,798 | 7.43 | 0.58 | 159,973 |
| `finden hier` | `hierfinden` | 8,138 | 6,490 | 8.33 | 0.60 | 78,402 |
| `nehmen sich` | `sich nehmen` | 6,485 | 5,580 | 7.25 | 0.51 | 52,864 |
| `informieren sich` | `sich informieren` | 4,833 | 4,117 | 8.71 | 0.59 | 49,817 |
| `ziehen sich` | `sich ziehen` | 4,717 | 4,099 | 8.11 | 0.55 | 44,315 |
| `holen sich` | `sich holen` | 3,013 | 2,654 | 8.67 | 0.56 | 30,903 |
| `geben sich` | `sich geben` | 5,040 | 4,514 | 5.12 | 0.35 | 26,111 |
| `präsentieren sich` | `sich präsentieren` | 2,673 | 2,417 | 8.35 | 0.54 | 26,099 |
| `öffnen sich` | `sich öffnen` | 2,873 | 2,369 | 7.84 | 0.51 | 25,866 |
| `gefallen gut` | `gutgefallen` | 2,017 | 1,598 | 9.00 | 0.56 | 21,341 |
| `schauen vorbei` | `vorbeischauen` | 1,329 | 1,236 | 12.87 | 0.78 | 21,271 |
| `erklären einverstanden` | `einverstandenerklären` | 1,153 | 1,049 | 14.27 | 0.85 | 20,984 |
| `tun sich` | `sich tun` | 2,941 | 2,709 | 6.39 | 0.41 | 20,372 |
| `beraten gern` | `gernberaten` | 1,352 | 1,280 | 11.27 | 0.68 | 18,596 |
| `kaufen sich` | `sich kaufen` | 2,357 | 2,007 | 6.75 | 0.43 | 17,526 |
| `denken sich` | `sich denken` | 2,436 | 2,187 | 6.53 | 0.42 | 17,357 |
| `kehrt zurück` | `zurückkehrt` | 877 | 799 | 14.77 | 0.86 | 16,878 |
| `gehen gut` | `gutgehen` | 2,540 | 2,214 | 6.14 | 0.39 | 16,672 |
| `wissen genau` | `genauwissen` | 1,501 | 1,375 | 8.84 | 0.54 | 15,467 |
| `erklären sich einverstanden` | `sich einverstandenerklären` | 1,047 | 956 | 10.80 | 0.64 | 15,174 |
| `dauern lange` | `langedauern` | 1,047 | 989 | 11.76 | 0.70 | 15,093 |
| `überzeugen sich` | `sich überzeugen` | 1,703 | 1,580 | 7.62 | 0.47 | 14,790 |
| `finden gut` | `gutfinden` | 2,216 | 1,856 | 5.85 | 0.37 | 13,652 |
| `finden unter` | `unterfinden` | 1,865 | 1,645 | 6.61 | 0.41 | 13,426 |
| `suchen sich` | `sich suchen` | 1,996 | 1,854 | 6.18 | 0.39 | 13,238 |

## Rank shifts against the live snapshot (`reference/lemmas/de.json`)

Live list 20,000 lemmas, this build 200,000; 18,562 shared. Spearman rank correlation on the shared lemmas 0.844; median rank ratio 1.16x.
Overlap of this build's top-k with the live top-k: top 1,000 84.5%, top 5,000 84.0%, top 20,000 78.1%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `achtzig` | 19620 | 1180 | -18,440 |
| `Daten` | 18710 | 533 | -18,177 |
| `sechzehn` | 18717 | 752 | -17,965 |
| `Milliliter` | 18887 | 2828 | -16,059 |
| `achtzehn` | 16468 | 709 | -15,759 |
| `aufregen` | 19193 | 4117 | -15,076 |
| `Daumen` | 19501 | 4889 | -14,612 |
| `sechzig` | 14903 | 823 | -14,080 |
| `sogenannt` | 14915 | 869 | -14,046 |
| `Ihr` | 14082 | 53 | -14,029 |
| `Onlin` | 16937 | 3227 | -13,710 |
| `Münchner` | 16894 | 3651 | -13,243 |
| `besonder` | 13451 | 344 | -13,107 |
| `jeglich` | 14642 | 1987 | -12,655 |
| `des` | 12527 | 27 | -12,500 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `Passt` | 4341 | 198153 | +193,812 |
| `frankfurter` | 3881 | 184454 | +180,573 |
| `weißen` | 1921 | 179517 | +177,596 |
| `Updat` | 2765 | 167267 | +164,502 |
| `Dein` | 2480 | 156175 | +153,695 |
| `bekommsen` | 3177 | 155621 | +152,444 |
| `passt` | 991 | 152357 | +151,366 |
| `stell` | 4950 | 154095 | +149,145 |
| `alleine` | 1180 | 141197 | +140,017 |
| `drauf` | 2127 | 141239 | +139,112 |
| `Mm` | 496 | 139339 | +138,843 |
| `kölner` | 4257 | 142764 | +138,507 |
| `erfasst` | 2532 | 138506 | +135,974 |
| `Et` | 4249 | 134953 | +130,704 |
| `Willkommen` | 4272 | 134415 | +130,143 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `das` | 7309 | 7 | -7,302 |
| `den` | 10437 | 12 | -10,425 |
| `werden + Partizip II` | - | 15 | - |
| `eine` | 8654 | 19 | -8,635 |
| `Sie` | - | 26 | - |
| `des` | 12527 | 27 | -12,500 |
| `dem` | - | 28 | - |
| `einen` | 10967 | 40 | -10,927 |
| `einem` | - | 46 | - |
| `Ihr` | 14082 | 53 | -14,029 |
| `ander` | - | 70 | - |
| `es gibt` | - | 76 | - |
| `erste` | - | 86 | - |
| `werden + Infinitiv` | - | 91 | - |
| `um … zu + Infinitiv` | - | 94 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `aller` | 53 | - | - |
| `anderer` | 56 | - | - |
| `alle` | 63 | 5337 | +5,274 |
| `vieler` | 76 | - | - |
| `Tag` | 84 | - | - |
| `erster` | 86 | 28219 | +28,133 |
| `einiger` | 151 | - | - |
| `gerne` | 175 | 28154 | +27,979 |
| `Kunde` | 180 | - | - |
| `weniger` | 192 | - | - |
| `nächster` | 229 | - | - |
| `zweiter` | 277 | 90349 | +90,072 |
| `Of` | 285 | 5475 | +5,190 |
| `daß` | 286 | - | - |
| `am` | 318 | - | - |

## Ported frequer checks

### Form-ratio outliers (392)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `und` | 13,238,066 | median form 5; `und` 13,234,024 (2646805x) |
| 2 | `die` | 13,014,758 | median form 2; `die` 13,014,736 (6507368x) |
| 3 | `der` | 11,762,890 | median form 704; `der` 11,713,960 (16639x) |
| 4 | `in` | 10,461,702 | median form 26; `in` 7,015,150 (269813x), `im` 3,261,003 (125423x), `ins` 178,133 (6851x) |
| 6 | `zu` | 6,760,352 | median form 9; `zu` 4,422,135 (491348x), `zum` 1,297,349 (144150x), `zur` 1,040,843 (115649x) |
| 7 | `das` | 4,979,369 | median form 6; `das` 4,979,356 (829893x) |
| 8 | `von` | 4,846,687 | median form 9; `von` 4,297,870 (477541x), `vom` 548,769 (60974x) |
| 9 | `werden` | 4,821,672 | median form 1852.5; `werden` 1,915,549 (1034x) |
| 10 | `mit` | 4,764,807 | median form 25; `mit` 4,764,752 (190590x) |
| 11 | `für` | 4,371,261 | median form 4; `für` 4,349,248 (1087312x), `fürs` 21,999 (5500x) |
| 12 | `den` | 4,349,492 | median form 6; `den` 4,349,224 (724871x) |
| 14 | `auf` | 3,470,743 | median form 16; `auf` 3,448,992 (215562x), `aufs` 21,709 (1357x) |
| 16 | `ein` | 3,088,053 | median form 753; `ein` 3,086,546 (4099x) |
| 17 | `es` | 3,054,222 | median form 9; `es` 3,001,025 (333447x), `’s` 53,176 (5908x) |
| 18 | `an` | 2,984,677 | median form 22; `an` 1,714,603 (77936x), `am` 1,223,319 (55605x), `a` 28,620 (1301x) |
| 19 | `eine` | 2,932,226 | median form 1; `eine` 2,932,221 (2932221x) |
| 20 | `nicht` | 2,867,786 | median form 149.5; `nicht` 2,863,467 (19154x) |
| 22 | `ich` | 2,688,652 | median form 550; `ich` 2,669,264 (4853x) |
| 23 | `auch` | 2,667,555 | median form 1.5; `auch` 2,667,539 (1778359x) |
| 25 | `bei` | 2,461,346 | median form 5; `bei` 2,023,455 (404691x), `beim` 437,873 (87575x) |
| 27 | `des` | 2,353,377 | median form 18; `des` 2,353,323 (130740x) |
| 28 | `dem` | 2,331,613 | median form 22; `dem` 2,331,588 (105981x) |
| 29 | `oder` | 2,120,507 | median form 31; `oder` 2,120,473 (68402x) |
| 30 | `sich` | 1,942,252 | median form 459; `sich` 1,687,439 (3676x) |
| 31 | `wir` | 1,937,878 | median form 3; `wir` 1,937,858 (645953x) |

_367 more not shown._

### Singular/plural mismatch (1,803)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 2 | `die` | 13,014,758 | `di` lemmatises to `di` (rank 4,539) |
| 7 | `das` | 4,979,369 | `da` lemmatises to `da` (rank 80) |
| 8 | `von` | 4,846,687 | `vo` lemmatises to `vo` (rank 23,848) |
| 12 | `den` | 4,349,492 | `de` lemmatises to `de` (rank 899) |
| 16 | `ein` | 3,088,053 | `ei` lemmatises to `ei` (rank 13,810) |
| 19 | `eine` | 2,932,226 | `ein` lemmatises to `ein` (rank 16) |
| 26 | `Sie` | 2,398,831 | `Si` lemmatises to `Si` (rank 27,545) |
| 27 | `des` | 2,353,377 | `de` lemmatises to `de` (rank 899) |
| 29 | `oder` | 2,120,507 | `od` lemmatises to `od` (rank 16,927) |
| 32 | `sie` | 1,913,128 | `si` lemmatises to `si` (rank 20,631) |
| 33 | `als` | 1,828,919 | `al` lemmatises to `al` (rank 11,121) |
| 34 | `wie` | 1,585,280 | `wi` lemmatises to `wi` (rank 33,905) |
| 36 | `dass` | 1,512,246 | `das` lemmatises to `das` (rank 7) |
| 38 | `aus` | 1,459,620 | `au` lemmatises to `au` (rank 9,415) |
| 40 | `einen` | 1,374,223 | `ein` lemmatises to `ein` (rank 16) |
| 40 | `einen` | 1,374,223 | `eine` lemmatises to `eine` (rank 19) |
| 43 | `einer` | 1,233,225 | `ein` lemmatises to `ein` (rank 16) |
| 44 | `über` | 1,224,550 | `üb` lemmatises to `üb` (rank 82,296) |
| 45 | `unser` | 1,213,007 | `uns` lemmatises to `sich` (rank 30) |
| 47 | `aber` | 1,136,839 | `ab` lemmatises to `ab` (rank 129) |
| 49 | `man` | 1,114,224 | `ma` lemmatises to `ma` (rank 9,813) |
| 51 | `wenn` | 1,107,950 | `wen` lemmatises to `wer` (rank 150) |
| 61 | `kein` | 866,874 | `kei` lemmatises to `kei` (rank 90,288) |
| 62 | `was` | 857,924 | `wa` lemmatises to `wa` (rank 25,183) |
| 64 | `müssen` | 842,656 | `müss` lemmatises to `müss` (rank 161,444) |

_1,778 more not shown._

### Lemma consistency (391)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 26 | `Sie` | 2,398,831 | alone, `Sie` lemmatises to `sie` (rank 32) |
| 53 | `Ihr` | 1,056,104 | alone, `Ihr` lemmatises to `ihr` (rank 37) |
| 62 | `was` | 857,924 | alone, `was` lemmatises to `etwas` (rank 117) |
| 75 | `uns` | 651,286 | alone, `uns` lemmatises to `sich` (rank 30) |
| 127 | `mich` | 318,923 | alone, `mich` lemmatises to `sich` (rank 30) |
| 149 | `Frage` | 270,431 | alone, `Frage` lemmatises to `fragen` (rank 461) |
| 166 | `dir` | 233,547 | alone, `dir` lemmatises to `sich` (rank 30) |
| 226 | `euch` | 182,627 | alone, `euch` lemmatises to `sich` (rank 30) |
| 305 | `lange` | 130,571 | alone, `lange` lemmatises to `lang` (rank 183) |
| 367 | `bestimmt` | 107,532 | alone, `bestimmt` lemmatises to `bestimmen` (rank 976) |
| 427 | `Stelle` | 92,643 | alone, `Stelle` lemmatises to `stellen` (rank 175) |
| 440 | `solcher` | 90,779 | alone, `solcher` lemmatises to `solch` (rank 839) |
| 533 | `Daten` | 76,878 | alone, `Daten` lemmatises to `Datum` (rank 232) |
| 667 | `vergangen` | 63,719 | alone, `vergangen` lemmatises to `vergehen` (rank 3,450) |
| 668 | `Suche` | 63,714 | alone, `Suche` lemmatises to `suchen` (rank 187) |
| 708 | `meinen` | 60,597 | alone, `meinen` lemmatises to `mein` (rank 66) |
| 753 | `Info` | 56,153 | alone, `Info` lemmatises to `info` (rank 12,399) |
| 761 | `weiß` | 55,804 | alone, `weiß` lemmatises to `wissen` (rank 145) |
| 774 | `Dank` | 54,981 | alone, `Dank` lemmatises to `dank` (rank 664) |
| 851 | `Bank#bank` | 50,348 | alone, `Bank#bank` lemmatises to `bank#bank` (rank 118,131) |
| 865 | `Mutter#mother` | 49,848 | alone, `Mutter#mother` lemmatises to `mutter#mother` (rank 24,477) |
| 943 | `Essen` | 46,106 | alone, `Essen` lemmatises to `essen` (rank 805) |
| 1029 | `Kauf` | 42,270 | alone, `Kauf` lemmatises to `kaufen` (rank 276) |
| 1110 | `Pflanze` | 38,987 | alone, `Pflanze` lemmatises to `pflanzen` (rank 4,862) |
| 1204 | `Alternative` | 35,737 | alone, `Alternative` lemmatises to `alternativ` (rank 1,483) |

_366 more not shown._

### Short lemmas (192)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4 | `in` | 10,461,702 | `in` -> `in`, `im` -> `in`, `ins` -> `in`, `i.` -> `in`, `inem` -> `in` |
| 6 | `zu` | 6,760,352 | `zum` -> `zu`, `zu` -> `zu`, `zur` -> `zu`, `zuer` -> `zu`, `zuden` -> `zu` |
| 17 | `es` | 3,054,222 | `es` -> `es`, `’s` -> `es`, `eser` -> `es`, `sen` -> `sen`, `esden` -> `esden` |
| 18 | `an` | 2,984,677 | `an` -> `an`, `am` -> `an`, `a` -> `an`, `ans` -> `an`, `ande` -> `an` |
| 41 | `um` | 1,351,747 | `um` -> `um`, `ums` -> `um` |
| 42 | `so` | 1,285,107 | `so` -> `so`, `soder` -> `so`, `soden` -> `so` |
| 54 | `er` | 1,031,039 | `er` -> `er`, `eres` -> `er`, `erden` -> `er`, `ere` -> `ere`, `eren` -> `eren` |
| 58 | `du` | 895,565 | `du` -> `du`, `dudes` -> `du`, `dues` -> `dues` |
| 80 | `da` | 609,198 | `da` -> `da` |
| 123 | `ja` | 327,293 | `ja` -> `ja`, `jaden` -> `ja` |
| 129 | `ab` | 315,174 | `ab` -> `ab`, `abs` -> `ab`, `abden` -> `abden`, `aben` -> `aben` |
| 133 | `ob` | 293,338 | `ob` -> `ob`, `obes` -> `ob`, `ober` -> `ober`, `obder` -> `ob` |
| 179 | `wo` | 217,223 | `wo` -> `wo` |
| 292 | `je` | 133,631 | `je` -> `je`, `jeen` -> `jee` |
| 424 | `B` | 92,772 | `b.` -> `?`, `b` -> `b`, `bs` -> `bs`, `be` -> `be`, `beste` -> `gut` |
| 457 | `of` | 87,515 | `of` -> `of`, `ofen` -> `ofen`, `ofer` -> `of` |
| 471 | `m` | 85,123 | `m` -> `m`, `mes` -> `m`, `mste` -> `m`, `mder` -> `m`, `mden` -> `mden` |
| 666 | `A` | 63,760 | `a` -> `an`, `a.` -> `a`, `as` -> `as`, `a#s` -> `a#s` |
| 688 | `x` | 62,245 | `x` -> `x`, `xste` -> `xste` |
| 868 | `AG` | 49,634 | `ag` -> `ag`, `ags` -> `ags` |
| 899 | `de` | 47,854 | `de` -> `de`, `dees` -> `dees`, `deer` -> `deer`, `deen` -> `deen`, `deste` -> `deste` |
| 917 | `C` | 47,050 | `c` -> `c`, `c.` -> `?`, `cs` -> `cs`, `ce` -> `ce` |
| 966 | `s` | 45,190 | `s` -> `s`, `ses` -> `s`, `sder` -> `s`, `sen` -> `sen`, `sste` -> `sste` |
| 1031 | `g` | 42,147 | `g` -> `g`, `gem` -> `g`, `ges` -> `g`, `ger` -> `ger`, `gen` -> `gen` |
| 1067 | `EU` | 40,640 | `eu` -> `eu`, `eus` -> `eus` |

_167 more not shown._

### Case merges (3,346)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 26 | `Sie` | 2,398,831 | lowercase `sie` is rank 32 (1,913,128): merge candidate |
| 53 | `Ihr` | 1,056,104 | lowercase `ihr` is rank 37 (1,502,527): merge candidate |
| 60 | `Jahr` | 869,610 | lowercase `jahr` is rank 4,832 (6,914): merge candidate |
| 103 | `Tag#day` | 416,182 | lowercase `tag#day` is rank 15,716 (1,391): merge candidate |
| 104 | `Zeit` | 401,618 | lowercase `zeit` is rank 4,496 (7,592): merge candidate |
| 113 | `Mensch` | 378,250 | lowercase `mensch` is rank 9,534 (2,727): merge candidate |
| 119 | `Prozent` | 343,092 | lowercase `prozent` is rank 39,663 (404): merge candidate |
| 120 | `Kind` | 337,656 | lowercase `kind` is rank 6,429 (4,685): merge candidate |
| 122 | `Ihnen` | 337,024 | lowercase `ihnen` is rank 407 (97,105): merge candidate |
| 141 | `Seite` | 286,859 | lowercase `seite` is rank 7,610 (3,734): merge candidate |
| 143 | `Deutschland` | 283,175 | lowercase `deutschland` is rank 7,845 (3,583): merge candidate |
| 152 | `Information` | 269,099 | lowercase `information` is rank 18,678 (1,101): merge candidate |
| 161 | `Thema` | 240,701 | lowercase `thema` is rank 16,656 (1,287): merge candidate |
| 162 | `Frau` | 240,042 | lowercase `frau` is rank 2,821 (13,823): merge candidate |
| 170 | `Unternehmen` | 226,939 | lowercase `unternehmen` is rank 2,573 (15,607): merge candidate |
| 177 | `Fall` | 217,981 | lowercase `fall` is rank 6,809 (4,329): merge candidate |
| 178 | `Leben` | 217,860 | lowercase `leben` is rank 335 (116,891): merge candidate |
| 182 | `Uhr` | 214,714 | lowercase `uhr` is rank 13,926 (1,639): merge candidate |
| 184 | `Spiel` | 212,359 | lowercase `spiel` is rank 18,339 (1,128): merge candidate |
| 188 | `Bild` | 208,522 | lowercase `bild` is rank 6,479 (4,629): merge candidate |
| 190 | `Teil` | 207,802 | lowercase `teil` is rank 3,067 (12,629): merge candidate |
| 191 | `Produkt` | 207,271 | lowercase `produkt` is rank 12,020 (2,000): merge candidate |
| 199 | `Haus` | 202,136 | lowercase `haus` is rank 14,094 (1,607): merge candidate |
| 203 | `Euro` | 201,098 | lowercase `euro` is rank 10,875 (2,277): merge candidate |
| 210 | `Woche` | 194,754 | lowercase `woche` is rank 14,482 (1,550): merge candidate |

_3,321 more not shown._

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 665 (66.5%).

Ours only: `werden + Partizip II`, `was`, `uns`, `es gibt`, `werden + Infinitiv`, `um … zu + Infinitiv`, `sein + Partizip II`, `damit`, `dabei`, `lassen + Infinitiv`, `mich`, `dazu`, `Frage`, `Information`, `natürlich`, `dir`, `Kunde#Masc`, `Produkt`, `würde + Infinitiv`, `dafür`, `beziehungsweise`, `nicht mehr`, `Bereich`, `euch`, `Datum`

wordfreq only: `menschen`, `enden`, `d`, `läuten`, `i`, `stimmen`, `e`, `reden`, `u`, `famili`, `ne`, `morgen`, `bzw`, `heraus`, `n`, `minuten`, `schul`, `ausserdem`, `woch`, `okay`, `namen`, `probl`, `halt`, `fühlen`, `h`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 35 | `all` | 1,521,355 | wordfreq zipf en 6.5 vs de 5.2 |
| 457 | `of` | 87,515 | wordfreq zipf en 7.4 vs de 5.5 |
| 666 | `A` | 63,760 | wordfreq zipf en 7.4 vs de 5.8 |
| 811 | `The` | 52,670 | wordfreq zipf en 7.7 vs de 5.6 |
| 1048 | `the` | 41,551 | wordfreq zipf en 7.7 vs de 5.6 |
| 1083 | `her` | 40,086 | wordfreq zipf en 6.3 vs de 5.2 |
| 1121 | `I` | 38,606 | wordfreq zipf en 7.1 vs de 5.5 |
| 1346 | `a` | 32,182 | wordfreq zipf en 7.4 vs de 5.8 |
| 1351 | `and` | 32,127 | wordfreq zipf en 7.4 vs de 5.2 |
| 1366 | `national` | 31,857 | wordfreq zipf en 5.5 vs de 4.3 |
| 1789 | `Business` | 23,648 | wordfreq zipf en 5.6 vs de 4.5 |
| 1911 | `to` | 21,993 | wordfreq zipf en 7.4 vs de 5.2 |
| 1938 | `for` | 21,583 | wordfreq zipf en 7.0 vs de 4.9 |
| 1964 | `Set` | 21,336 | wordfreq zipf en 5.6 vs de 4.3 |
| 2435 | `Services` | 16,654 | wordfreq zipf en 5.3 vs de 3.9 |
| 2479 | `New` | 16,274 | wordfreq zipf en 6.2 vs de 5.1 |
| 2570 | `on` | 15,648 | wordfreq zipf en 6.9 vs de 5.0 |
| 2622 | `World` | 15,278 | wordfreq zipf en 5.9 vs de 4.5 |
| 2820 | `IT` | 13,829 | wordfreq zipf en 7.0 vs de 4.9 |
| 2886 | `Level` | 13,481 | wordfreq zipf en 5.4 vs de 4.3 |
| 2898 | `Last` | 13,419 | wordfreq zipf en 5.9 vs de 4.5 |
| 2935 | `LED` | 13,264 | wordfreq zipf en 5.1 vs de 4.1 |
| 2968 | `Support` | 13,104 | wordfreq zipf en 5.5 vs de 4.2 |
| 3058 | `Book` | 12,705 | wordfreq zipf en 5.4 vs de 4.1 |
| 3059 | `Look` | 12,703 | wordfreq zipf en 5.8 vs de 4.1 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 143 | `Deutschland` | 283,175 | PROPN 100%, capitalised forms 0% |
| 274 | `Berlin` | 139,344 | PROPN 100%, capitalised forms 0% |
| 325 | `Tom` | 120,882 | PROPN 100%, capitalised forms 0% |
| 457 | `of` | 87,515 | PROPN 97%, capitalised forms 0% |
| 491 | `Europa` | 81,191 | PROPN 100%, capitalised forms 0% |
| 540 | `Google` | 76,122 | PROPN 100%, capitalised forms 0% |
| 563 | `USA` | 73,549 | PROPN 100%, capitalised forms 0% |
| 659 | `Schweiz` | 64,217 | PROPN 100%, capitalised forms 0% |
| 691 | `München` | 61,979 | PROPN 100%, capitalised forms 0% |
| 726 | `Österreich` | 58,898 | PROPN 100%, capitalised forms 0% |
| 791 | `Hamburg` | 54,030 | PROPN 100%, capitalised forms 0% |
| 811 | `The` | 52,670 | PROPN 99%, capitalised forms 0% |
| 847 | `Facebook` | 50,403 | PROPN 100%, capitalised forms 0% |
| 899 | `de` | 47,854 | PROPN 97%, capitalised forms 0% |
| 979 | `Maria` | 44,654 | PROPN 100%, capitalised forms 0% |
| 992 | `Windows` | 43,925 | PROPN 100%, capitalised forms 0% |
| 1037 | `Frankfurt` | 41,954 | PROPN 99%, capitalised forms 0% |
| 1048 | `the` | 41,551 | PROPN 92%, capitalised forms 0% |
| 1067 | `EU` | 40,640 | PROPN 100%, capitalised forms 0% |
| 1071 | `Wien` | 40,315 | PROPN 98%, capitalised forms 0% |
| 1095 | `Köln` | 39,558 | PROPN 100%, capitalised forms 0% |
| 1116 | `Michael` | 38,843 | PROPN 100%, capitalised forms 0% |
| 1135 | `EUR` | 38,118 | PROPN 100%, capitalised forms 0% |
| 1158 | `Twitter` | 37,520 | PROPN 98%, capitalised forms 0% |
| 1201 | `Thomas` | 35,859 | PROPN 100%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 93.8% | 0.958 |
| juilland_u | 99.7% | 1.000 |
| juilland_u_corrected | 99.7% | 1.000 |
| dp_adjusted | 99.1% | 0.999 |
| cd_blend | 96.7% | 0.988 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `eigens` | 5881 | 4836 | -1,045 | 5,289 | 5,056 | 0.984 | 0.061 |
| `alles andere als` | 5946 | 4903 | -1,043 | 5,219 | 4,975 | 0.987 | 0.047 |
| `dabei sein, etwas zu tun` | 5424 | 4420 | -1,004 | 5,884 | 5,710 | 0.987 | 0.052 |
| `fündig` | 5698 | 4701 | -997 | 5,502 | 5,273 | 0.986 | 0.054 |
| `verhelfen` | 5795 | 4805 | -990 | 5,385 | 5,106 | 0.984 | 0.062 |
| `Krampfader` | 3386 | 21711 | +18,325 | 11,072 | 668 | 0.928 | 0.281 |
| `raum` | 2979 | 13232 | +10,253 | 13,047 | 1,301 | 0.957 | 0.177 |
| `Beklagte` | 3317 | 11114 | +7,797 | 11,353 | 1,650 | 0.948 | 0.196 |
| `Kläger` | 3707 | 9234 | +5,527 | 9,858 | 2,116 | 0.951 | 0.191 |
| `Kryptowährung` | 4954 | 10184 | +5,230 | 6,691 | 1,846 | 0.966 | 0.135 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `seither` | 4959 | 4918 | -41 | 6,685 | 6,291 | 0.986 | 0.056 |
| `auseinander` | 5032 | 4993 | -39 | 6,567 | 6,057 | 0.987 | 0.050 |
| `eines Tages` | 4744 | 4707 | -37 | 7,086 | 6,339 | 0.988 | 0.046 |
| `hinterher` | 4725 | 4688 | -37 | 7,113 | 6,486 | 0.988 | 0.048 |
| `quer` | 4917 | 4880 | -37 | 6,756 | 6,070 | 0.988 | 0.048 |
| `Date` | 4880 | 5387 | +507 | 6,808 | 3,330 | 0.854 | 0.184 |
| `Mallorca` | 4405 | 4759 | +354 | 7,786 | 3,063 | 0.886 | 0.174 |
| `Buchstabe` | 2722 | 3031 | +309 | 14,525 | 7,006 | 0.869 | 0.169 |
| `Harry` | 2926 | 3234 | +308 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Outfit` | 3700 | 3962 | +262 | 9,875 | 6,282 | 0.896 | 0.134 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `seither` | 4959 | 4917 | -42 | 6,685 | 6,291 | 0.986 | 0.056 |
| `auseinander` | 5032 | 4993 | -39 | 6,567 | 6,057 | 0.987 | 0.050 |
| `eines Tages` | 4744 | 4706 | -38 | 7,086 | 6,339 | 0.988 | 0.046 |
| `quer` | 4917 | 4879 | -38 | 6,756 | 6,070 | 0.988 | 0.048 |
| `sich engagieren` | 4726 | 4689 | -37 | 7,113 | 6,338 | 0.987 | 0.053 |
| `Date` | 4880 | 5389 | +509 | 6,808 | 3,330 | 0.854 | 0.184 |
| `Mallorca` | 4405 | 4760 | +355 | 7,786 | 3,063 | 0.886 | 0.174 |
| `Buchstabe` | 2722 | 3033 | +311 | 14,525 | 7,006 | 0.869 | 0.169 |
| `Harry` | 2926 | 3236 | +310 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Outfit` | 3700 | 3963 | +263 | 9,875 | 6,282 | 0.896 | 0.134 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `auseinander` | 5032 | 4898 | -134 | 6,567 | 6,057 | 0.987 | 0.050 |
| `keineswegs` | 5118 | 4989 | -129 | 6,416 | 5,716 | 0.988 | 0.049 |
| `besorgt` | 5040 | 4911 | -129 | 6,554 | 5,927 | 0.987 | 0.051 |
| `quer` | 4917 | 4790 | -127 | 6,756 | 6,070 | 0.988 | 0.048 |
| `auswirken` | 5074 | 4950 | -124 | 6,483 | 5,987 | 0.988 | 0.049 |
| `Krampfader` | 3386 | 4112 | +726 | 11,072 | 668 | 0.928 | 0.281 |
| `Mitgliedstaat` | 4609 | 5216 | +607 | 7,340 | 2,881 | 0.928 | 0.223 |
| `Harry` | 2926 | 3465 | +539 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Date` | 4880 | 5333 | +453 | 6,808 | 3,330 | 0.854 | 0.184 |
| `Beklagte` | 3317 | 3724 | +407 | 11,353 | 1,650 | 0.948 | 0.196 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `dabei sein, etwas zu tun` | 5424 | 4890 | -534 | 5,884 | 5,710 | 0.987 | 0.052 |
| `kurzem` | 5335 | 4821 | -514 | 6,034 | 5,775 | 0.987 | 0.054 |
| `sich erfreuen` | 5323 | 4816 | -507 | 6,046 | 5,782 | 0.986 | 0.056 |
| `sich beschäftigen` | 5174 | 4671 | -503 | 6,310 | 5,967 | 0.985 | 0.058 |
| `sich konzentrieren` | 5169 | 4676 | -493 | 6,318 | 5,945 | 0.987 | 0.052 |
| `Krampfader` | 3386 | 8551 | +5,165 | 11,072 | 668 | 0.928 | 0.281 |
| `raum` | 2979 | 6301 | +3,322 | 13,047 | 1,301 | 0.957 | 0.177 |
| `Beklagte` | 3317 | 6057 | +2,740 | 11,353 | 1,650 | 0.948 | 0.196 |
| `Kryptowährung` | 4954 | 7116 | +2,162 | 6,691 | 1,846 | 0.966 | 0.135 |
| `Kläger` | 3707 | 5841 | +2,134 | 9,858 | 2,116 | 0.951 | 0.191 |


## Convergence

One row per counted shard: the shards counted so far, in the order they finished. Per band N: **chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement (1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each source; a source with an odd count leaves its newest shard out). Stopping rule: 3 consecutive full-mix checkpoints with split <= 5% at 20k and <= 10% at 50k.

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,858,929 | hplt-v2-de 1,858,929 | web only | - | - | 28 | - | - | - | 12 | - | - | - | 5 | - | - | - | 2 | - | 0/3 |
| 3,228,275 | hplt-v2-de 3,228,275 | web only | 6.4% | 112 | 49 | 15.4% | 10.2% | 297 | 20 | 23.5% | 14.6% | 885 | 8 | 33.5% | 21.3% | 3,391 | 3 | 50.2% | 0/3 |
| 5,035,140 | hplt-v2-de 5,035,140 | web only | 6.2% | 128 | 75 | 15.4% | 8.4% | 302 | 30 | 23.5% | 12.2% | 782 | 12 | 33.5% | 17.6% | 3,269 | 4 | 50.2% | 0/3 |
| 7,843,966 | hplt-v2-de 5,035,140, tatoeba-deu 2,808,826 | partial (lacks tatoeba-deu) | 11.1% | 398 | 103 | 15.4% | 10.2% | 687 | 40 | 23.5% | 10.1% | 1,278 | 15 | 33.5% | 9.5% | 3,267 | 5 | 50.2% | 0/3 |
| 11,145,054 | hplt-v2-de 5,035,140, tatoeba-deu 6,109,914 | full | 7.2% | 272 | 138 | 11.4% | 7.2% | 503 | 51 | 16.0% | 7.5% | 982 | 19 | 23.9% | 8.5% | 2,506 | 5 | 38.4% | 0/3 |
| 12,858,618 | hplt-v2-de 6,748,704, tatoeba-deu 6,109,914 | full | 3.0% | 104 | 165 | 10.2% | 3.5% | 203 | 61 | 13.8% | 5.1% | 433 | 23 | 20.8% | 8.0% | 1,692 | 7 | 34.0% | 0/3 |
| 14,661,404 | hplt-v2-de 8,551,490, tatoeba-deu 6,109,914 | full | 2.6% | 80 | 192 | 10.2% | 3.5% | 164 | 71 | 13.8% | 4.5% | 373 | 27 | 20.8% | 7.1% | 1,457 | 8 | 34.0% | 0/3 |
| 16,598,866 | hplt-v2-de 10,488,952, tatoeba-deu 6,109,914 | full | 2.4% | 69 | 223 | 9.0% | 3.0% | 152 | 83 | 13.2% | 4.1% | 349 | 32 | 19.3% | 6.5% | 1,294 | 9 | 30.8% | 0/3 |
| 18,137,485 | hplt-v2-de 12,027,571, tatoeba-deu 6,109,914 | full | 1.4% | 57 | 246 | 9.0% | 2.1% | 110 | 92 | 13.2% | 3.1% | 257 | 35 | 19.3% | 4.5% | 972 | 10 | 30.8% | 0/3 |
| 19,961,780 | hplt-v2-de 13,851,866, tatoeba-deu 6,109,914 | full | 1.5% | 44 | 273 | 8.2% | 2.0% | 94 | 102 | 12.3% | 2.8% | 224 | 39 | 17.8% | 4.4% | 956 | 12 | 28.4% | 0/3 |
| 21,607,573 | hplt-v2-de 15,497,659, tatoeba-deu 6,109,914 | full | 2.3% | 72 | 300 | 8.2% | 2.9% | 144 | 112 | 12.3% | 3.5% | 325 | 43 | 17.8% | 4.2% | 1,014 | 13 | 28.4% | 0/3 |
| 23,438,824 | hplt-v2-de 17,328,910, tatoeba-deu 6,109,914 | full | 1.2% | 38 | 327 | 8.6% | 1.6% | 80 | 123 | 12.3% | 2.4% | 194 | 48 | 17.5% | 3.8% | 798 | 14 | 27.2% | 0/3 |
| 30,163,693 | hplt-v2-de 24,053,779, tatoeba-deu 6,109,914 | full | 2.7% | 75 | 427 | 7.2% | 2.9% | 147 | 161 | 10.2% | 4.3% | 336 | 63 | 15.2% | 6.7% | 1,244 | 19 | 24.1% | 0/3 |
| 35,680,128 | hplt-v2-de 29,570,214, tatoeba-deu 6,109,914 | full | 1.6% | 44 | 509 | 6.8% | 1.9% | 90 | 193 | 9.7% | 2.8% | 225 | 75 | 14.1% | 4.8% | 852 | 22 | 22.7% | 0/3 |
| 37,460,081 | hplt-v2-de 31,350,167, tatoeba-deu 6,109,914 | full | 0.5% | 20 | 533 | 6.1% | 0.8% | 43 | 203 | 8.6% | 1.4% | 107 | 79 | 13.3% | 1.9% | 408 | 23 | 21.3% | 0/3 |
| 41,345,162 | hplt-v2-de 35,235,248, tatoeba-deu 6,109,914 | full | 1.0% | 24 | 590 | 6.1% | 1.3% | 55 | 225 | 8.6% | 2.0% | 143 | 88 | 12.8% | 3.0% | 585 | 26 | 20.5% | 0/3 |
| 44,367,274 | hplt-v2-de 38,257,360, tatoeba-deu 6,109,914 | full | 0.8% | 19 | 635 | 5.7% | 0.9% | 42 | 241 | 7.9% | 1.4% | 111 | 95 | 12.1% | 2.3% | 440 | 28 | 19.8% | 0/3 |
| 75,475,936 | hplt-v2-de 69,366,022, tatoeba-deu 6,109,914 | full | 3.0% | 68 | 1,077 | 5.2% | 3.3% | 140 | 416 | 7.4% | 4.6% | 334 | 164 | 10.5% | 7.3% | 1,195 | 48 | 16.8% | 0/3 |
| 107,046,033 | hplt-v2-de 100,936,119, tatoeba-deu 6,109,914 | full | 1.6% | 40 | 1,542 | 4.5% | 1.9% | 81 | 596 | 6.2% | 2.6% | 200 | 235 | 9.2% | 4.3% | 757 | 69 | 14.3% | 0/3 |
| 139,877,087 | hplt-v2-de 133,767,173, tatoeba-deu 6,109,914 | full | 1.5% | 38 | 2,020 | 4.1% | 1.7% | 73 | 778 | 5.3% | 2.4% | 168 | 306 | 8.0% | 3.5% | 614 | 91 | 12.6% | 0/3 |
| 176,047,733 | hplt-v2-de 169,937,819, tatoeba-deu 6,109,914 | full | 1.0% | 23 | 2,556 | 3.8% | 1.1% | 51 | 983 | 5.0% | 1.6% | 123 | 387 | 7.3% | 2.7% | 488 | 114 | 11.4% | 0/3 |
| 217,170,036 | hplt-v2-de 211,060,122, tatoeba-deu 6,109,914 | full | 0.7% | 16 | 3,163 | 3.3% | 0.9% | 37 | 1,215 | 4.5% | 1.4% | 98 | 481 | 6.5% | 2.2% | 395 | 141 | 10.1% | 0/3 |
| 262,241,563 | hplt-v2-de 256,131,649, tatoeba-deu 6,109,914 | full | 0.6% | 16 | 3,822 | 3.0% | 0.8% | 37 | 1,470 | 3.8% | 1.3% | 96 | 583 | 5.7% | 2.0% | 372 | 171 | 9.0% | 0/3 |
| 350,250,058 | hplt-v2-de-deep 65,690,337, hplt-v2-de 278,449,807, tatoeba-deu 6,109,914 | full | 0.9% | 18 | 5,139 | 2.6% | 0.9% | 39 | 1,974 | 3.3% | 1.5% | 102 | 779 | 5.1% | 2.2% | 403 | 229 | 7.9% | 0/3 |
| 385,935,865 | hplt-v2-de-deep 99,817,022, hplt-v2-de 280,008,929, tatoeba-deu 6,109,914 | full | 0.4% | 9 | 5,652 | 2.5% | 0.6% | 20 | 2,184 | 3.1% | 0.7% | 54 | 860 | 4.8% | 1.1% | 210 | 253 | 7.4% | 1/3 |
| 411,513,342 | hplt-v2-de-deep 125,394,499, hplt-v2-de 280,008,929, tatoeba-deu 6,109,914 | full | 0.3% | 8 | 6,029 | 2.3% | 0.3% | 17 | 2,330 | 2.9% | 0.5% | 43 | 917 | 4.5% | 0.8% | 165 | 270 | 7.1% | 2/3 |
| 440,125,254 | hplt-v2-de-deep 154,006,411, hplt-v2-de 280,008,929, tatoeba-deu 6,109,914 | full | 0.4% | 8 | 6,452 | 2.1% | 0.4% | 18 | 2,485 | 2.9% | 0.5% | 44 | 981 | 4.3% | 0.8% | 166 | 289 | 6.8% | 3/3 |

Decision: **stop** at 440,125,254 tokens.
Final list: 451,548,754 tokens (full).

### Calibration

Each checkpoint's full-data top N against the final list's top N (**vs final**: share of the final top N not in the checkpoint's), next to its split-half disagreement. If split-half estimates the remaining change, split ~ 2 x vs final.

| tokens | 5k split | 5k vs final | 5k ratio | 10k split | 10k vs final | 10k ratio | 20k split | 20k vs final | 20k ratio | 50k split | 50k vs final | 50k ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,858,929 | - | 11.0% | - | - | 16.5% | - | - | 23.9% | - | - | 36.6% | - |
| 3,228,275 | 15.4% | 9.5% | 1.62 | 23.5% | 13.0% | 1.81 | 33.5% | 19.5% | 1.72 | 50.2% | 30.5% | 1.65 |
| 5,035,140 | 15.4% | 7.1% | 2.17 | 23.5% | 10.7% | 2.19 | 33.5% | 15.7% | 2.14 | 50.2% | 25.2% | 1.99 |
| 7,843,966 | 15.4% | 12.1% | 1.27 | 23.5% | 13.2% | 1.77 | 33.5% | 16.7% | 2.01 | 50.2% | 24.5% | 2.05 |
| 11,145,054 | 11.4% | 17.8% | 0.64 | 16.0% | 17.3% | 0.92 | 23.9% | 19.5% | 1.22 | 38.4% | 25.1% | 1.53 |
| 12,858,618 | 10.2% | 15.4% | 0.66 | 13.8% | 15.1% | 0.92 | 20.8% | 17.2% | 1.21 | 34.0% | 22.6% | 1.50 |
| 14,661,404 | 10.2% | 13.9% | 0.73 | 13.8% | 13.6% | 1.02 | 20.8% | 15.7% | 1.32 | 34.0% | 21.1% | 1.61 |
| 16,598,866 | 9.0% | 12.3% | 0.74 | 13.2% | 12.3% | 1.07 | 19.3% | 14.3% | 1.35 | 30.8% | 19.4% | 1.58 |
| 18,137,485 | 9.0% | 11.3% | 0.80 | 13.2% | 11.2% | 1.18 | 19.3% | 13.2% | 1.47 | 30.8% | 18.1% | 1.70 |
| 19,961,780 | 8.2% | 10.6% | 0.78 | 12.3% | 10.3% | 1.19 | 17.8% | 12.5% | 1.43 | 28.4% | 17.2% | 1.65 |
| 21,607,573 | 8.2% | 10.3% | 0.80 | 12.3% | 10.1% | 1.22 | 17.8% | 12.4% | 1.44 | 28.4% | 17.0% | 1.67 |
| 23,438,824 | 8.6% | 9.5% | 0.90 | 12.3% | 9.3% | 1.32 | 17.5% | 11.6% | 1.51 | 27.2% | 16.0% | 1.70 |
| 30,163,693 | 7.2% | 7.6% | 0.94 | 10.2% | 7.6% | 1.33 | 15.2% | 9.6% | 1.59 | 24.1% | 13.7% | 1.75 |
| 35,680,128 | 6.8% | 6.5% | 1.06 | 9.7% | 6.7% | 1.45 | 14.1% | 8.6% | 1.65 | 22.7% | 12.2% | 1.87 |
| 37,460,081 | 6.1% | 6.2% | 0.98 | 8.6% | 6.4% | 1.35 | 13.3% | 8.3% | 1.61 | 21.3% | 11.9% | 1.80 |
| 41,345,162 | 6.1% | 5.9% | 1.03 | 8.6% | 6.0% | 1.42 | 12.8% | 7.8% | 1.64 | 20.5% | 11.4% | 1.80 |
| 44,367,274 | 5.7% | 5.4% | 1.06 | 7.9% | 5.5% | 1.43 | 12.1% | 7.3% | 1.66 | 19.8% | 10.7% | 1.85 |
| 75,475,936 | 5.2% | 3.6% | 1.45 | 7.4% | 4.1% | 1.80 | 10.5% | 5.4% | 1.95 | 16.8% | 8.0% | 2.08 |
| 107,046,033 | 4.5% | 2.4% | 1.89 | 6.2% | 3.1% | 2.03 | 9.2% | 4.1% | 2.23 | 14.3% | 6.4% | 2.23 |
| 139,877,087 | 4.1% | 2.2% | 1.82 | 5.3% | 2.6% | 2.05 | 8.0% | 3.6% | 2.25 | 12.6% | 5.5% | 2.31 |
| 176,047,733 | 3.8% | 1.7% | 2.26 | 5.0% | 2.0% | 2.48 | 7.3% | 2.9% | 2.52 | 11.4% | 4.5% | 2.53 |
| 217,170,036 | 3.3% | 1.4% | 2.41 | 4.5% | 1.7% | 2.66 | 6.5% | 2.4% | 2.68 | 10.1% | 3.7% | 2.71 |
| 262,241,563 | 3.0% | 1.0% | 2.87 | 3.8% | 1.2% | 3.10 | 5.7% | 1.9% | 3.04 | 9.0% | 2.9% | 3.09 |
| 350,250,058 | 2.6% | 0.8% | 3.30 | 3.3% | 0.9% | 3.91 | 5.1% | 1.2% | 4.33 | 7.9% | 1.8% | 4.26 |
| 385,935,865 | 2.5% | 0.7% | 3.50 | 3.1% | 0.7% | 4.59 | 4.8% | 1.0% | 4.96 | 7.4% | 1.4% | 5.20 |
| 411,513,342 | 2.3% | 0.4% | 5.23 | 2.9% | 0.4% | 6.57 | 4.5% | 0.6% | 7.16 | 7.1% | 1.0% | 7.23 |
| 440,125,254 | 2.1% | 0.1% | 26.00 | 2.9% | 0.2% | 15.83 | 4.3% | 0.2% | 17.96 | 6.8% | 0.4% | 15.45 |

