# Review report: de (full)

- Ranking score: `frequency`; 136,985 candidate lemmas ranked.
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
| `damit` | 399,146 | 262,112 | 108 |
| `dabei` | 354,755 | 244,624 | 118 |
| `dazu` | 281,561 | 198,416 | 147 |
| `natürlich` | 255,109 | 167,778 | 158 |
| `dafür` | 194,181 | 146,054 | 211 |
| `Möglichkeit` | 181,904 | 133,424 | 226 |
| `anbieten` | 166,153 | 121,015 | 245 |
| `kostenlos` | 165,138 | 89,494 | 248 |
| `darauf` | 159,735 | 121,335 | 253 |
| `persönlich` | 151,172 | 106,551 | 262 |
| `zusätzlich` | 134,338 | 100,808 | 291 |
| `davon` | 133,218 | 103,410 | 303 |
| `darüber` | 131,140 | 103,108 | 302 |
| `Erfahrung` | 122,006 | 89,460 | 315 |
| `Verfügung` | 116,741 | 90,676 | 334 |
| `stattfinden` | 113,640 | 82,691 | 350 |
| `sich befinden` | 112,712 | 80,547 | 354 |
| `unterschiedlich` | 111,265 | 85,957 | 358 |
| `sich freuen` | 108,472 | 86,238 | 598 |
| `Entwicklung` | 105,489 | 71,904 | 379 |
| `aussehen` | 100,672 | 73,756 | 375 |
| `bearbeiten` | 99,444 | 32,282 | 403 |
| `Leistung` | 98,734 | 61,752 | 401 |
| `Mitarbeiter` | 98,287 | 58,914 | 402 |
| `Lösung` | 93,571 | 63,541 | 421 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `werden + Partizip II` | 3,110,140 | 857,694 | 15 |
| `werden + Infinitiv` | 524,971 | 300,650 | 91 |
| `um … zu + Infinitiv` | 505,505 | 290,688 | 94 |
| `sein + Partizip II` | 494,384 | 309,040 | 95 |
| `lassen + Infinitiv` | 338,656 | 225,473 | 121 |
| `würde + Infinitiv` | 201,618 | 120,250 | 205 |
| `sein + zu + Infinitiv` | 122,884 | 96,972 | 331 |
| `gehen + Infinitiv` | 21,874 | 19,147 | 2009 |
| `ohne … zu + Infinitiv` | 20,330 | 18,437 | 2087 |
| `Modalverb + Infinitiv Perfekt` | 8,217 | 7,403 | 4045 |
| `haben … zu + Infinitiv` | 6,589 | 6,233 | 5321 |
| `werden + Infinitiv Perfekt` | 3,325 | 3,159 | 7520 |
| `statt … zu + Infinitiv` | 1,040 | 1,009 | 16095 |
| `(an)statt … zu + Infinitiv` | 354 | 347 | 31998 |
| `vorhaben + zu + Infinitiv` | 37 | 37 | - |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `es gibt` | 640,096 | 342,019 | 77 |
| `nicht mehr` | 186,729 | 130,852 | 223 |
| `vor allem` | 154,312 | 116,929 | 256 |
| `ein paar` | 111,546 | 82,059 | 357 |
| `für etwas sorgen` | 97,199 | 77,472 | 411 |
| `zum Beispiel` | 86,352 | 65,419 | 469 |
| `im Rahmen` | 85,084 | 61,976 | 478 |
| `immer wieder` | 78,468 | 63,331 | 523 |
| `zu etwas gehören` | 73,163 | 61,679 | 573 |
| `immer noch` | 70,484 | 55,050 | 593 |
| `nicht nur … sondern auch` | 70,418 | 61,639 | 594 |
| `unter anderem` | 63,514 | 53,948 | 672 |
| `sowohl … als auch` | 63,274 | 55,489 | 674 |
| `über etwas verfügen` | 62,548 | 48,393 | 683 |
| `es handelt sich um etwas` | 60,839 | 49,453 | 703 |
| `auch wenn` | 60,290 | 51,090 | 709 |
| `je nach` | 53,814 | 44,684 | 792 |
| `in der Regel` | 50,320 | 38,979 | 850 |
| `darüber hinaus` | 50,092 | 42,794 | 843 |
| `aus etwas bestehen` | 49,161 | 40,162 | 875 |
| `vor Ort` | 47,160 | 37,263 | 907 |
| `ein wenig` | 47,124 | 37,010 | 910 |
| `zusammen mit` | 43,189 | 37,639 | 999 |
| `es kommt zu etwas` | 42,089 | 34,681 | 1027 |
| `zwar … aber` | 39,344 | 34,629 | 1093 |

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

Live list 20,000 lemmas, this build 136,985; 14,972 shared. Spearman rank correlation on the shared lemmas 0.888; median rank ratio 1.16x.
Overlap of this build's top-k with the live top-k: top 1,000 84.9%, top 5,000 82.3%, top 20,000 70.4%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `achtzig` | 19620 | 1163 | -18,457 |
| `Daten` | 18710 | 531 | -18,179 |
| `sechzehn` | 18717 | 752 | -17,965 |
| `Milliliter` | 18887 | 2750 | -16,137 |
| `achtzehn` | 16468 | 705 | -15,763 |
| `aufregen` | 19193 | 3920 | -15,273 |
| `Handschuh` | 19914 | 4835 | -15,079 |
| `Daumen` | 19501 | 4496 | -15,005 |
| `Schaltfläche` | 18653 | 4560 | -14,093 |
| `sechzig` | 14903 | 821 | -14,082 |
| `sogenannt` | 14915 | 859 | -14,056 |
| `Ihr` | 14082 | 53 | -14,029 |
| `Nuss` | 18810 | 4946 | -13,864 |
| `Münchner` | 16894 | 3046 | -13,848 |
| `besser` | 18013 | 4487 | -13,526 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `Dein` | 2480 | 133375 | +130,895 |
| `bekommsen` | 3177 | 132857 | +129,680 |
| `stell` | 4950 | 131430 | +126,480 |
| `drauf` | 2127 | 119313 | +117,186 |
| `Mm` | 496 | 117509 | +117,013 |
| `kölner` | 4257 | 120753 | +116,496 |
| `Et` | 4249 | 113376 | +109,127 |
| `Willkommen` | 4272 | 112870 | +108,598 |
| `Pro` | 3505 | 104852 | +101,347 |
| `Thi` | 4700 | 102091 | +97,391 |
| `km` | 1107 | 97649 | +96,542 |
| `Wandern` | 3810 | 96705 | +92,895 |
| `Lachen` | 4154 | 95498 | +91,344 |
| `min` | 2028 | 89665 | +87,637 |
| `Bien` | 4928 | 77573 | +72,645 |

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
| `es gibt` | - | 77 | - |
| `erste` | - | 86 | - |
| `werden + Infinitiv` | - | 91 | - |
| `um … zu + Infinitiv` | - | 94 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `Tom` | 50 | - | - |
| `aller` | 53 | - | - |
| `anderer` | 56 | - | - |
| `alle` | 63 | - | - |
| `vieler` | 76 | - | - |
| `Tag` | 84 | 16659 | +16,575 |
| `erster` | 86 | - | - |
| `einiger` | 151 | - | - |
| `Maria` | 165 | - | - |
| `gerne` | 175 | 22047 | +21,872 |
| `Kunde` | 180 | 9169 | +8,989 |
| `weniger` | 192 | - | - |
| `The` | 224 | - | - |
| `nächster` | 229 | - | - |
| `zweiter` | 277 | 71564 | +71,287 |

## Ported frequer checks

### Form-ratio outliers (399)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `und` | 13,262,756 | median form 5; `und` 13,252,489 (2650498x), `u` 5,549 (1110x) |
| 2 | `die` | 13,014,758 | median form 2; `die` 13,014,736 (6507368x) |
| 3 | `der` | 11,778,945 | median form 704; `der` 11,730,015 (16662x) |
| 4 | `in` | 10,471,263 | median form 22; `in` 7,024,415 (319292x), `im` 3,261,003 (148227x), `ins` 178,428 (8110x) |
| 5 | `sein` | 9,627,221 | median form 411; `ist` 4,380,075 (10657x), `sind` 1,845,048 (4489x), `war` 775,207 (1886x), `sein` 683,615 (1663x) |
| 6 | `zu` | 6,768,175 | median form 9; `zu` 4,425,801 (491756x), `zum` 1,299,707 (144412x), `zur` 1,042,642 (115849x) |
| 7 | `das` | 4,979,369 | median form 6; `das` 4,979,356 (829893x) |
| 8 | `von` | 4,851,959 | median form 9; `von` 4,303,142 (478127x), `vom` 548,769 (60974x) |
| 9 | `werden` | 4,841,435 | median form 301; `werden` 1,916,630 (6368x), `wird` 1,478,722 (4913x), `wurde` 613,620 (2039x) |
| 10 | `mit` | 4,771,436 | median form 25; `mit` 4,771,381 (190855x) |
| 11 | `für` | 4,418,203 | median form 5.5; `für` 4,360,512 (792820x), `fürs` 22,972 (4177x), `fr` 19,446 (3536x), `fuer` 8,544 (1553x) |
| 12 | `den` | 4,349,492 | median form 6; `den` 4,349,224 (724871x) |
| 13 | `haben` | 3,755,566 | median form 443; `hat` 1,307,320 (2951x), `haben` 1,105,309 (2495x), `habe` 515,482 (1164x) |
| 14 | `auf` | 3,476,345 | median form 13.5; `auf` 3,453,072 (255783x), `aufs` 22,043 (1633x) |
| 16 | `ein` | 3,089,155 | median form 27.5; `ein` 3,086,546 (112238x) |
| 17 | `es` | 3,054,222 | median form 9; `es` 3,001,025 (333447x), `’s` 53,176 (5908x) |
| 18 | `an` | 2,989,840 | median form 12.5; `an` 1,717,440 (137395x), `am` 1,225,644 (98052x), `a` 28,620 (2290x), `ans` 18,106 (1448x) |
| 19 | `eine` | 2,936,363 | median form 1; `eine` 2,932,221 (2932221x), `ner` 2,919 (2919x), `ne` 1,207 (1207x) |
| 20 | `nicht` | 2,883,741 | median form 152.5; `nicht` 2,871,899 (18832x) |
| 21 | `können` | 2,803,012 | median form 397; `kann` 1,150,733 (2899x), `können` 1,030,361 (2595x) |
| 22 | `ich` | 2,694,338 | median form 558; `ich` 2,673,366 (4791x) |
| 23 | `auch` | 2,668,734 | median form 1.5; `auch` 2,668,718 (1779145x) |
| 24 | `dieser` | 2,629,977 | median form 22; `diese` 852,080 (38731x), `dieser` 566,835 (25765x), `diesem` 354,893 (16132x), `dieses` 334,920 (15224x) |
| 25 | `bei` | 2,463,781 | median form 5; `bei` 2,025,343 (405069x), `beim` 437,873 (87575x) |
| 27 | `des` | 2,353,377 | median form 18; `des` 2,353,323 (130740x) |

_374 more not shown._

### Singular/plural mismatch (1,101)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 7 | `das` | 4,979,369 | `da` lemmatises to `da` (rank 81) |
| 19 | `eine` | 2,936,363 | `ein` lemmatises to `ein` (rank 16) |
| 36 | `dass` | 1,516,782 | `das` lemmatises to `das` (rank 7) |
| 38 | `aus` | 1,463,102 | `au` lemmatises to `au` (rank 8,455) |
| 40 | `einen` | 1,374,479 | `ein` lemmatises to `ein` (rank 16) |
| 40 | `einen` | 1,374,479 | `eine` lemmatises to `eine` (rank 19) |
| 43 | `über` | 1,239,750 | `üb` lemmatises to `üb` (rank 63,995) |
| 44 | `einer` | 1,233,225 | `ein` lemmatises to `ein` (rank 16) |
| 45 | `unser` | 1,216,257 | `uns` lemmatises to `sich` (rank 30) |
| 47 | `aber` | 1,138,660 | `ab` lemmatises to `ab` (rank 128) |
| 51 | `wenn` | 1,112,384 | `wen` lemmatises to `wer` (rank 150) |
| 61 | `kein` | 869,627 | `kei` lemmatises to `kei` (rank 71,512) |
| 76 | `uns` | 651,286 | `un` lemmatises to `und` (rank 1) |
| 78 | `weiter` | 625,188 | `weit` lemmatises to `weit` (rank 424) |
| 82 | `unter` | 606,904 | `unt` lemmatises to `unt` (rank 56,887) |
| 85 | `immer` | 585,963 | `imm` lemmatises to `imm` (rank 59,057) |
| 86 | `erste` | 585,530 | `erst` lemmatises to `erst` (rank 220) |
| 100 | `eins` | 432,896 | `ein` lemmatises to `ein` (rank 16) |
| 101 | `welcher` | 425,280 | `welch` lemmatises to `welch` (rank 7,894) |
| 102 | `eines` | 419,967 | `eine` lemmatises to `eine` (rank 19) |
| 106 | `ohne` | 401,387 | `ohn` lemmatises to `ohn` (rank 49,209) |
| 115 | `gegen` | 369,076 | `geg` lemmatises to `geg` (rank 65,502) |
| 117 | `etwas` | 358,840 | `etwa` lemmatises to `etwa` (rank 277) |
| 122 | `Ihnen` | 337,024 | `Ihn` lemmatises to `ihn` (rank 221) |
| 129 | `denn` | 316,886 | `den` lemmatises to `den` (rank 12) |

_1,076 more not shown._

### Lemma consistency (331)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 26 | `Sie` | 2,398,831 | alone, `Sie` lemmatises to `sie` (rank 32) |
| 53 | `Ihr` | 1,056,104 | alone, `Ihr` lemmatises to `ihr` (rank 37) |
| 63 | `was` | 857,924 | alone, `was` lemmatises to `etwas` (rank 117) |
| 76 | `uns` | 651,286 | alone, `uns` lemmatises to `sich` (rank 30) |
| 127 | `mich` | 318,923 | alone, `mich` lemmatises to `sich` (rank 30) |
| 152 | `Frage` | 270,859 | alone, `Frage` lemmatises to `fragen` (rank 460) |
| 167 | `dir` | 233,547 | alone, `dir` lemmatises to `sich` (rank 30) |
| 227 | `euch` | 182,627 | alone, `euch` lemmatises to `sich` (rank 30) |
| 287 | `lange` | 136,250 | alone, `lange` lemmatises to `lang` (rank 178) |
| 367 | `bestimmt` | 107,938 | alone, `bestimmt` lemmatises to `bestimmen` (rank 974) |
| 430 | `Stelle` | 92,643 | alone, `Stelle` lemmatises to `stellen` (rank 174) |
| 443 | `solcher` | 90,779 | alone, `solcher` lemmatises to `solch` (rank 839) |
| 531 | `Daten` | 77,774 | alone, `Daten` lemmatises to `Datum` (rank 232) |
| 662 | `Suche` | 63,984 | alone, `Suche` lemmatises to `suchen` (rank 190) |
| 668 | `vergangen` | 63,719 | alone, `vergangen` lemmatises to `vergehen` (rank 3,321) |
| 691 | `weiß` | 62,031 | alone, `weiß` lemmatises to `wissen` (rank 139) |
| 702 | `meinen` | 60,902 | alone, `meinen` lemmatises to `mein` (rank 66) |
| 737 | `Info` | 57,540 | alone, `Info` lemmatises to `info` (rank 10,865) |
| 770 | `Dank` | 54,981 | alone, `Dank` lemmatises to `dank` (rank 665) |
| 849 | `Bank#bank` | 50,348 | alone, `Bank#bank` lemmatises to `bank#bank` (rank 97,589) |
| 861 | `Mutter#mother` | 49,848 | alone, `Mutter#mother` lemmatises to `mutter#mother` (rank 19,602) |
| 933 | `Essen` | 46,419 | alone, `Essen` lemmatises to `essen` (rank 755) |
| 986 | `Kauf` | 43,984 | alone, `Kauf` lemmatises to `kaufen` (rank 268) |
| 1091 | `Neue` | 39,402 | alone, `Neue` lemmatises to `neu` (rank 62) |
| 1100 | `Pflanze` | 38,987 | alone, `Pflanze` lemmatises to `pflanzen` (rank 4,598) |

_306 more not shown._

### Short lemmas (53)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4 | `in` | 10,471,263 | `in` -> `in`, `im` -> `in`, `ins` -> `in`, `i.` -> `in`, `inem` -> `in` |
| 6 | `zu` | 6,768,175 | `zum` -> `zu`, `zu` -> `zu`, `zur` -> `zu`, `zuer` -> `zu`, `zuden` -> `zu` |
| 17 | `es` | 3,054,222 | `es` -> `es`, `’s` -> `es`, `eser` -> `es`, `sen` -> `sen`, `esden` -> `esden` |
| 18 | `an` | 2,989,840 | `an` -> `an`, `am` -> `an`, `a` -> `an`, `ans` -> `an`, `ande` -> `an` |
| 41 | `um` | 1,352,692 | `um` -> `um`, `ums` -> `um` |
| 42 | `so` | 1,294,580 | `so` -> `so`, `soder` -> `so`, `soden` -> `so`, `sos` -> `sos`, `sooooo` -> `sooooo` |
| 55 | `er` | 1,031,039 | `er` -> `er`, `eres` -> `er`, `erden` -> `er`, `ere` -> `ere`, `eren` -> `eren` |
| 59 | `du` | 899,537 | `du` -> `du`, `dudes` -> `du`, `dues` -> `dues` |
| 81 | `da` | 610,470 | `da` -> `da` |
| 123 | `ja` | 330,315 | `ja` -> `ja`, `jaden` -> `ja`, `jap` -> `jap`, `jas` -> `jas` |
| 128 | `ab` | 317,598 | `ab` -> `ab`, `abs` -> `ab`, `abden` -> `abden`, `aben` -> `aben` |
| 134 | `ob` | 295,514 | `ob` -> `ob`, `obes` -> `ob`, `ober` -> `ober`, `obder` -> `ob`, `obs` -> `obs` |
| 181 | `wo` | 217,777 | `wo` -> `wo` |
| 297 | `je` | 133,631 | `je` -> `je`, `jeen` -> `jee` |
| 1046 | `EU` | 41,376 | `eu` -> `eu`, `eus` -> `eus`, `euen` -> `euen`, `eue` -> `eue`, `euem` -> `euem` |
| 1168 | `PC` | 36,567 | `pc` -> `pc`, `pcs` -> `pcs` |
| 1285 | `Öl` | 33,303 | `öl` -> `öl`, `öls` -> `öls`, `öle` -> `öle`, `ölen` -> `ölen`, `öles` -> `öl` |
| 1547 | `TV` | 27,523 | `tv` -> `tv`, `tvs` -> `tvs` |
| 1592 | `ne` | 26,658 | `ne` -> `ne`, `neen` -> `ne`, `neem` -> `neem` |
| 1765 | `Ei` | 23,632 | `eier` -> `ei`, `ei` -> `ei`, `eiern` -> `eiern`, `eies` -> `eies`, `eie` -> `eie` |
| 2101 | `na` | 19,343 | `na` -> `na`, `nas` -> `nas` |
| 2270 | `CD` | 17,603 | `cds` -> `cds`, `cd` -> `cd`, `cder` -> `cd`, `cden` -> `c` |
| 2302 | `PS` | 17,340 | `ps` -> `ps` |
| 2365 | `o` | 16,734 | `o` -> `o` |
| 2651 | `oh` | 14,535 | `oh` -> `oh`, `ohen` -> `ohen`, `oher` -> `oh`, `ohem` -> `oh` |

_28 more not shown._

### Case merges (1,816)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 26 | `Sie` | 2,398,831 | lowercase `sie` is rank 32 (1,913,128): merge candidate |
| 53 | `Ihr` | 1,056,104 | lowercase `ihr` is rank 37 (1,503,723): merge candidate |
| 103 | `Tag#day` | 416,182 | lowercase `tag#day` is rank 13,385 (1,391): merge candidate |
| 104 | `Zeit` | 404,237 | lowercase `zeit` is rank 4,282 (7,592): merge candidate |
| 113 | `Mensch` | 380,280 | lowercase `mensch` is rank 8,553 (2,727): merge candidate |
| 122 | `Ihnen` | 337,024 | lowercase `ihnen` is rank 412 (97,105): merge candidate |
| 144 | `Deutschland` | 283,175 | lowercase `deutschland` is rank 7,181 (3,583): merge candidate |
| 151 | `Information` | 270,969 | lowercase `information` is rank 15,520 (1,101): merge candidate |
| 170 | `Unternehmen` | 227,644 | lowercase `unternehmen` is rank 2,515 (15,607): merge candidate |
| 180 | `Leben` | 218,918 | lowercase `leben` is rank 342 (116,891): merge candidate |
| 185 | `Bild` | 212,802 | lowercase `bild` is rank 6,026 (4,629): merge candidate |
| 191 | `Teil` | 208,601 | lowercase `teil` is rank 2,964 (12,629): merge candidate |
| 200 | `Euro` | 204,568 | lowercase `euro` is rank 9,653 (2,277): merge candidate |
| 204 | `Haus` | 203,284 | lowercase `haus` is rank 12,159 (1,607): merge candidate |
| 214 | `Stadt` | 192,230 | lowercase `stadt` is rank 13,660 (1,346): merge candidate |
| 219 | `Welt` | 189,468 | lowercase `welt` is rank 9,900 (2,194): merge candidate |
| 232 | `Datum` | 177,471 | lowercase `datum` is rank 44,063 (225): merge candidate |
| 234 | `Art` | 176,758 | lowercase `art` is rank 9,234 (2,428): merge candidate |
| 235 | `Problem` | 175,085 | lowercase `problem` is rank 7,432 (3,392): merge candidate |
| 247 | `Mann` | 166,612 | lowercase `mann` is rank 44,848 (221): merge candidate |
| 250 | `Weg` | 162,684 | lowercase `weg` is rank 1,079 (39,853): merge candidate |
| 276 | `Berlin` | 141,025 | lowercase `berlin` is rank 8,011 (3,010): merge candidate |
| 300 | `Inhalt` | 133,296 | lowercase `inhalt` is rank 25,108 (524): merge candidate |
| 325 | `Familie` | 121,749 | lowercase `familie` is rank 39,705 (252): merge candidate |
| 326 | `Team` | 121,451 | lowercase `team` is rank 12,325 (1,572): merge candidate |

_1,791 more not shown._

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 666 (66.6%).

Ours only: `werden + Partizip II`, `was`, `uns`, `es gibt`, `werden + Infinitiv`, `um … zu + Infinitiv`, `sein + Partizip II`, `damit`, `dabei`, `lassen + Infinitiv`, `mich`, `dazu`, `Information`, `Frage`, `natürlich`, `dir`, `Kunde#Masc`, `Produkt`, `würde + Infinitiv`, `beziehungsweise`, `dafür`, `Bereich`, `nicht mehr`, `euch`, `Datum`

wordfreq only: `menschen`, `s`, `enden`, `d`, `läuten`, `the`, `m`, `de`, `i`, `stimmen`, `e`, `reden`, `u`, `famili`, `b`, `ne`, `of`, `morgen`, `bzw`, `heraus`, `c`, `n`, `minuten`, `schul`, `ausserdem`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 35 | `all` | 1,530,648 | wordfreq zipf en 6.5 vs de 5.2 |
| 1042 | `her` | 41,446 | wordfreq zipf en 6.3 vs de 5.2 |
| 1356 | `national` | 31,857 | wordfreq zipf en 5.5 vs de 4.3 |
| 1678 | `Business` | 25,070 | wordfreq zipf en 5.6 vs de 4.5 |
| 1891 | `Set` | 21,839 | wordfreq zipf en 5.6 vs de 4.3 |
| 2430 | `LED` | 16,247 | wordfreq zipf en 5.1 vs de 4.1 |
| 2636 | `Level` | 14,659 | wordfreq zipf en 5.4 vs de 4.3 |
| 2696 | `Look` | 14,140 | wordfreq zipf en 5.8 vs de 4.1 |
| 2741 | `Support` | 13,830 | wordfreq zipf en 5.5 vs de 4.2 |
| 2742 | `IT` | 13,829 | wordfreq zipf en 7.0 vs de 4.9 |
| 2817 | `Last` | 13,419 | wordfreq zipf en 5.9 vs de 4.5 |
| 2925 | `Performance` | 12,890 | wordfreq zipf en 5.2 vs de 4.2 |
| 2939 | `Held` | 12,803 | wordfreq zipf en 5.2 vs de 4.2 |
| 3142 | `Not` | 11,620 | wordfreq zipf en 6.7 vs de 4.7 |
| 3239 | `Power` | 11,145 | wordfreq zipf en 5.5 vs de 4.3 |
| 3252 | `Office` | 11,098 | wordfreq zipf en 5.4 vs de 4.2 |
| 3326 | `still` | 10,815 | wordfreq zipf en 5.9 vs de 4.4 |
| 3505 | `Taste` | 9,998 | wordfreq zipf en 4.7 vs de 3.7 |
| 3929 | `Kid` | 8,521 | wordfreq zipf en 5.0 vs de 3.6 |
| 3976 | `legal` | 8,406 | wordfreq zipf en 5.1 vs de 4.0 |
| 4150 | `Board` | 7,917 | wordfreq zipf en 5.2 vs de 3.9 |
| 4204 | `Star#celebrity` | 7,776 | wordfreq zipf en 4.2 vs de 2.8 |
| 4234 | `final` | 7,712 | wordfreq zipf en 5.3 vs de 3.9 |
| 4236 | `Lack` | 7,708 | wordfreq zipf en 4.9 vs de 3.7 |
| 4272 | `Style` | 7,603 | wordfreq zipf en 5.1 vs de 4.0 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 144 | `Deutschland` | 283,175 | PROPN 100%, capitalised forms 0% |
| 276 | `Berlin` | 141,025 | PROPN 100%, capitalised forms 0% |
| 493 | `Europa` | 81,671 | PROPN 100%, capitalised forms 0% |
| 566 | `USA` | 73,867 | PROPN 100%, capitalised forms 0% |
| 656 | `Schweiz` | 64,476 | PROPN 100%, capitalised forms 0% |
| 676 | `München` | 62,820 | PROPN 99%, capitalised forms 0% |
| 711 | `Österreich` | 59,966 | PROPN 99%, capitalised forms 0% |
| 782 | `Hamburg` | 54,635 | PROPN 100%, capitalised forms 0% |
| 1017 | `Frankfurt` | 42,571 | PROPN 99%, capitalised forms 0% |
| 1046 | `EU` | 41,376 | PROPN 100%, capitalised forms 0% |
| 1059 | `Wien` | 40,877 | PROPN 98%, capitalised forms 0% |
| 1069 | `Köln` | 40,257 | PROPN 99%, capitalised forms 0% |
| 1263 | `Frankreich` | 33,917 | PROPN 99%, capitalised forms 0% |
| 1267 | `Top` | 33,894 | PROPN 60%, capitalised forms 0% |
| 1274 | `China` | 33,702 | PROPN 99%, capitalised forms 0% |
| 1404 | `Bayern` | 30,912 | PROPN 99%, capitalised forms 0% |
| 1493 | `Russland` | 28,815 | PROPN 99%, capitalised forms 0% |
| 1538 | `Stuttgart` | 27,664 | PROPN 100%, capitalised forms 0% |
| 1585 | `Italien` | 26,733 | PROPN 96%, capitalised forms 0% |
| 1645 | `SPD` | 25,636 | PROPN 100%, capitalised forms 0% |
| 1678 | `Business` | 25,070 | PROPN 53%, capitalised forms 0% |
| 1698 | `Düsseldorf` | 24,748 | PROPN 100%, capitalised forms 0% |
| 1813 | `Zürich` | 22,791 | PROPN 94%, capitalised forms 0% |
| 1897 | `Hannover` | 21,746 | PROPN 97%, capitalised forms 0% |
| 1911 | `News` | 21,558 | PROPN 68%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 94.0% | 0.960 |
| juilland_u | 99.8% | 1.000 |
| juilland_u_corrected | 99.8% | 1.000 |
| dp_adjusted | 99.2% | 0.999 |
| cd_blend | 96.9% | 0.988 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `alles andere als` | 5990 | 4943 | -1,047 | 5,219 | 4,975 | 0.987 | 0.047 |
| `eigens` | 5930 | 4885 | -1,045 | 5,289 | 5,056 | 0.984 | 0.061 |
| `dabei sein, etwas zu tun` | 5461 | 4468 | -993 | 5,884 | 5,710 | 0.987 | 0.052 |
| `verhelfen` | 5844 | 4852 | -992 | 5,385 | 5,106 | 0.984 | 0.062 |
| `fündig` | 5656 | 4672 | -984 | 5,630 | 5,382 | 0.986 | 0.053 |
| `Krampfader` | 3299 | 18767 | +15,468 | 11,570 | 773 | 0.929 | 0.279 |
| `Beklagte` | 3352 | 11054 | +7,702 | 11,353 | 1,650 | 0.948 | 0.196 |
| `Kläger` | 3729 | 9208 | +5,479 | 9,858 | 2,116 | 0.951 | 0.191 |
| `Ra` | 3797 | 8426 | +4,629 | 9,630 | 2,416 | 0.970 | 0.120 |
| `Ähnlichkeitsmerkmal` | 4594 | 9162 | +4,568 | 7,462 | 2,131 | 0.976 | 0.094 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `Charme` | 4546 | 4506 | -40 | 7,582 | 6,833 | 0.990 | 0.042 |
| `mit Hilfe von` | 4745 | 4708 | -37 | 7,147 | 6,534 | 0.988 | 0.047 |
| `anstrengend` | 4403 | 4366 | -37 | 7,898 | 7,078 | 0.988 | 0.049 |
| `konfrontieren` | 5021 | 4985 | -36 | 6,639 | 6,215 | 0.987 | 0.053 |
| `seither` | 4989 | 4953 | -36 | 6,685 | 6,291 | 0.986 | 0.056 |
| `Date` | 4480 | 4887 | +407 | 7,727 | 3,971 | 0.871 | 0.171 |
| `Mallorca` | 4450 | 4798 | +348 | 7,786 | 3,063 | 0.886 | 0.174 |
| `Harry` | 2963 | 3266 | +303 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Buchstabe` | 2764 | 3065 | +301 | 14,525 | 7,006 | 0.869 | 0.169 |
| `Outfit` | 3723 | 3992 | +269 | 9,875 | 6,282 | 0.896 | 0.134 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `Charme` | 4546 | 4508 | -38 | 7,582 | 6,833 | 0.990 | 0.042 |
| `besser` | 4775 | 4737 | -38 | 7,107 | 6,697 | 0.987 | 0.052 |
| `mit Hilfe von` | 4745 | 4708 | -37 | 7,147 | 6,534 | 0.988 | 0.047 |
| `seither` | 4989 | 4952 | -37 | 6,685 | 6,291 | 0.986 | 0.056 |
| `anstrengend` | 4403 | 4366 | -37 | 7,898 | 7,078 | 0.988 | 0.049 |
| `Date` | 4480 | 4889 | +409 | 7,727 | 3,971 | 0.871 | 0.171 |
| `Mallorca` | 4450 | 4800 | +350 | 7,786 | 3,063 | 0.886 | 0.174 |
| `Harry` | 2963 | 3268 | +305 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Buchstabe` | 2764 | 3066 | +302 | 14,525 | 7,006 | 0.869 | 0.169 |
| `Outfit` | 3723 | 3992 | +269 | 9,875 | 6,282 | 0.896 | 0.134 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `auseinander` | 5056 | 4931 | -125 | 6,567 | 6,057 | 0.987 | 0.050 |
| `gönnen` | 5067 | 4943 | -124 | 6,553 | 6,055 | 0.987 | 0.050 |
| `besorgt` | 5066 | 4945 | -121 | 6,554 | 5,927 | 0.987 | 0.051 |
| `Charme` | 4546 | 4429 | -117 | 7,582 | 6,833 | 0.990 | 0.042 |
| `auswirken` | 5103 | 4986 | -117 | 6,483 | 5,987 | 0.988 | 0.049 |
| `Krampfader` | 3299 | 4012 | +713 | 11,570 | 773 | 0.929 | 0.279 |
| `Mitgliedstaat` | 4650 | 5247 | +597 | 7,340 | 2,881 | 0.928 | 0.223 |
| `Frisur` | 4708 | 5276 | +568 | 7,221 | 2,607 | 0.944 | 0.216 |
| `Harry` | 2963 | 3495 | +532 | 13,300 | 3,481 | 0.867 | 0.241 |
| `Kläger` | 3729 | 4137 | +408 | 9,858 | 2,116 | 0.951 | 0.191 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `dabei sein, etwas zu tun` | 5461 | 4937 | -524 | 5,884 | 5,710 | 0.987 | 0.052 |
| `auseinandersetzen` | 5444 | 4941 | -503 | 5,905 | 5,682 | 0.985 | 0.059 |
| `sich erfreuen` | 5358 | 4860 | -498 | 6,046 | 5,782 | 0.986 | 0.056 |
| `widerspiegeln` | 5211 | 4717 | -494 | 6,298 | 6,013 | 0.986 | 0.056 |
| `sich beschäftigen` | 5204 | 4721 | -483 | 6,310 | 5,967 | 0.985 | 0.058 |
| `Krampfader` | 3299 | 7997 | +4,698 | 11,570 | 773 | 0.929 | 0.279 |
| `Beklagte` | 3352 | 6104 | +2,752 | 11,353 | 1,650 | 0.948 | 0.196 |
| `Kläger` | 3729 | 5893 | +2,164 | 9,858 | 2,116 | 0.951 | 0.191 |
| `Ähnlichkeitsmerkmal` | 4594 | 6493 | +1,899 | 7,462 | 2,131 | 0.976 | 0.094 |
| `Ra` | 3797 | 5665 | +1,868 | 9,630 | 2,416 | 0.970 | 0.120 |

## Excluded lemmas

`de.tsv` (sha256 `ba6d10dc1b2dc232`) lists 1,163 exclusions; 1,164 lemmas were dropped from the top 40,000 before cutting it (exclude-english 1,163, exclude-unit 1). Lower ranks moved up.

| rank before | lemma | class | reason |
|---|---|---|---|
| 681 | `A` | exclude-english | agreed: single letter |
| 825 | `The` | exclude-english | agreed: English |
| 1066 | `the` | exclude-english | agreed: English |
| 1138 | `I` | exclude-english | agreed: single letter |
| 1382 | `a` | exclude-english | agreed: single letter |
| 1383 | `and` | exclude-english | agreed: English |
| 1947 | `to` | exclude-english | agreed: English |
| 1976 | `for` | exclude-english | agreed: English |
| 2514 | `New` | exclude-english | agreed: English |
| 2609 | `on` | exclude-english | agreed: English |
| 2657 | `World` | exclude-english | agreed: English |
| 3087 | `Book` | exclude-english | agreed: English |
| 3178 | `by` | exclude-english | agreed: English |
| 3203 | `Group` | exclude-english | agreed: English |
| 3221 | `One` | exclude-english | agreed: English |
| 3361 | `Games` | exclude-english | agreed: not established |
| 3455 | `Big` | exclude-english | agreed: English |
| 3727 | `Game` | exclude-english | agreed: not established |
| 3808 | `Home` | exclude-english | agreed: English |
| 3911 | `i` | exclude-english | agreed: single letter |
| 3968 | `Play` | exclude-english | agreed: English |
| 4078 | `Player` | exclude-english | agreed: English |
| 4232 | `Data` | exclude-english | agreed: English |
| 4241 | `High` | exclude-english | agreed: English |
| 4282 | `Free` | exclude-english | agreed: English |
| 4452 | `Girl` | exclude-english | agreed: English |
| 4482 | `No` | exclude-english | agreed: English |
| 4524 | `University` | exclude-english | agreed: English |
| 4531 | `at` | exclude-english | agreed: English |
| 4532 | `it` | exclude-english | agreed: English |
| 4561 | `Read` | exclude-english | agreed: English |
| 4573 | `Best` | exclude-english | agreed: English |
| 4780 | `more` | exclude-english | agreed: English word |
| 4856 | `More` | exclude-english | agreed: English word/name |
| 4912 | `Day` | exclude-english | agreed: English word |
| 5014 | `you` | exclude-english | agreed: English word |
| 5075 | `National` | exclude-english | agreed: English name part |
| 5117 | `Life` | exclude-english | agreed: English word |
| 5126 | `Creative` | exclude-english | agreed: English word |
| 5138 | `Network` | exclude-english | agreed: English word |
| 5298 | `American` | exclude-english | agreed: English word |
| 5313 | `Security` | exclude-english | agreed: English word |
| 5433 | `House` | exclude-english | agreed: English word |
| 5514 | `Of` | exclude-english | agreed: English word |
| 5562 | `Music` | exclude-english | agreed: English word |
| 5740 | `School` | exclude-english | agreed: English word |
| 5891 | `White` | exclude-english | agreed: English surname |
| 6016 | `European` | exclude-english | agreed: English word |
| 6030 | `with` | exclude-english | agreed: English word |
| 6196 | `Up` | exclude-english | agreed: English word |
| 6235 | `IS` | exclude-english | agreed: English/junk |
| 6251 | `Hot` | exclude-english | agreed: English word |
| 6350 | `Public` | exclude-english | agreed: English word |
| 6361 | `My` | exclude-english | agreed: English word |
| 6513 | `up` | exclude-english | agreed: English word |
| 6577 | `free` | exclude-english | agreed: English word |
| 6606 | `your` | exclude-english | agreed: English word |
| 6610 | `Like` | exclude-english | agreed: English |
| 6631 | `Line` | exclude-english | agreed: English word |
| 6827 | `Food` | exclude-english | agreed: English word |

_1,104 more in the exclusion file._


## Junk-filter heuristics

Rules on: diversity, citation, foreign, shape, propn_usage; accent merges at ratio 5.0. Window: the 50,633 ranked lemmas (after the exclusion list) that fill the top 40,000. Actions: keep 31,335, review-drop 10,633, review-keep 8,665.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band | propn_usage |
|---|---:|---:|---:|---:|---:|---:|
| diversity | 448 | 14 | 4 | 16 | 0 | 161 |
| citation | 14 | 586 | 2 | 124 | 0 | 0 |
| foreign | 4 | 2 | 969 | 22 | 0 | 500 |
| shape | 16 | 124 | 22 | 1,188 | 0 | 225 |
| propn_band | 0 | 0 | 0 | 0 | 0 | 0 |
| propn_usage | 161 | 0 | 500 | 225 | 0 | 7,888 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 0.

### Low diversity

Documents reached / documents expected at random, below 0.3 (frequency >= 20): 448 in the window. For comparison, each log2-frequency band's 2nd percentile: 32-63: 0.21, 64-127: 0.25, 128-255: 0.33, 256-511: 0.36, 512-1023: 0.38, 1024-2047: 0.41, 2048-4095: 0.42, 4096-8191: 0.45, 8192-16383: 0.39, 16384-32767: 0.42, 32768-65535: 0.44, 65536-131071: 0.34.

Examples: `du` (59), `Tom` (329), `weiterlesen` (523), `Absatz` (566), `Casino` (630), `Cookie` (657), `personenbezogen` (812), `Quelltext` (1793), `Adobe` (1949), `DSGVO` (1952), `Arzneimittel` (2474), `mg` (2638), `AntwortenLöschen` (2756), `Harry` (2952), `Krampfader` (3284), `Beklagte` (3337), `lit` (3478), `Bitcoin` (3655), `Kläger` (3711), `Ra` (3779), `SAP` (3887), `Ähnlichkeitsmerkmal` (4562), `Besteller` (5009), `Klägerin` (5036), `Hermine` (5174), `Merkliste` (5215), `CEST` (5222), `TG` (5592), `CBD` (5932), `Verschlagwortet` (6025), `Ron` (6102), `gerebloggt` (6941), `CET` (7178), `speichernJob` (7858), `Schuppenflechte` (8032), `Auftragnehmer` (8111), `Lightroom` (8237), `Draco` (8402), `FRITZ` (8447), `DS-GVO` (8539)

### Accent merges (5,939)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `AB` | `ab` | 2,424 | review: merge |
| `ABER` | `aber` | 1,821 | review: merge |
| `ACHTUNG` | `Achtung` | 2,786 | review: merge |
| `AH` | `ah` | 485 | review: merge |
| `ALL` | `all` | 554 | review: merge |
| `ALS` | `als` | 1,468 | review: merge |
| `AM` | `an` | 2,326 | review: merge |
| `AN` | `an` | 2,837 | review: merge |
| `APP` | `App` | 1,148 | review: merge |
| `ARGE` | `arg` | 829 | review: merge |
| `ART` | `Art` | 1,066 | review: merge |
| `ASS` | `Ass` | 563 | review: merge |
| `AU` | `aus` | 684 | review: merge |
| `AUF` | `auf` | 4,080 | review: merge |
| `AUS` | `aus` | 2,297 | review: merge |
| `AUTO` | `Auto` | 599 | review: merge |
| `Abkühl` | `abkühlen` | 851 | review: merge |
| `Abos` | `Abo` | 677 | review: merge |
| `Absag` | `absagen` | 844 | review: merge |
| `Absetz` | `absetzen` | 717 | review: merge |
| `Absolventinn` | `Absolventin` | 662 | review: merge |
| `Adressdat` | `Adressdaten` | 883 | review: merge |
| `Aktivier` | `aktivieren` | 1,073 | review: merge |
| `AktivistInn` | `Aktivist` | 540 | review: merge |
| `Aktualisier` | `aktualisieren` | 546 | review: merge |
| `Akzeptier` | `akzeptieren` | 1,054 | review: merge |
| `Albanie` | `Albanien` | 890 | review: merge |
| `Algorithm` | `Algorithmus` | 1,416 | review: merge |
| `Algorithme` | `Algorithmus` | 775 | review: merge |
| `Allen` | `alle` | 2,713 | review: merge |
| `Allerheilig` | `Allerheiligen` | 529 | review: merge |
| `Alpin` | `alpin` | 485 | review: merge |
| `Anal` | `anal` | 1,885 | review: merge |
| `Anana` | `Ananas` | 1,697 | review: merge |
| `Anbiet` | `anbieten` | 616 | review: merge |
| `Andenke` | `Andenken` | 1,050 | review: merge |
| `Anderenfall` | `anderenfalls` | 650 | review: merge |
| `Andernfall` | `andernfalls` | 861 | review: merge |
| `Angststörunge` | `Angststörung` | 467 | review: merge |
| `Ankomm` | `ankommen` | 737 | review: merge |
| `Anmeldedat` | `Anmeldedaten` | 583 | review: merge |
| `Anschlussfrag` | `Anschlussfrage` | 484 | review: merge |
| `Ansinn` | `Ansinnen` | 477 | review: merge |
| `Anspielunge` | `Anspielung` | 557 | review: merge |
| `Aquarie` | `Aquarium` | 845 | review: merge |
| `Arabie` | `Arabien` | 521 | review: merge |
| `Arbeitnehmerinne` | `Arbeitnehmerin` | 529 | review: merge |
| `Arbeitsverhaeltnis` | `Arbeitsverhältnis` | 341 | review: merge |
| `Arbeitsverhältniss` | `Arbeitsverhältnis` | 1,438 | review: merge |
| `Armbänder` | `Armband` | 1,075 | review: merge |
| `Arztpraxen` | `Arztpraxis` | 1,223 | review: merge |
| `Atome` | `Atom` | 583 | review: merge |
| `Attack` | `Attacke` | 1,289 | review: merge |
| `Aufeinandertreff` | `aufeinandertreffen` | 708 | review: merge |
| `Aufgabenstellunge` | `Aufgabenstellung` | 1,112 | review: merge |
| `Aufhang` | `aufhängen` | 1,078 | review: merge |
| `Aufraum` | `aufräumen` | 810 | review: merge |
| `Aufsehe` | `Aufsehen` | 2,390 | review: merge |
| `Aufsichtsrät` | `Aufsichtsrat` | 481 | review: merge |
| `Auspack` | `auspacken` | 754 | review: merge |
| `Ausricht` | `ausrichten` | 533 | review: merge |
| `Aussendienst` | `Außendienst` | 533 | review: merge |
| `Aussenminister` | `Außenminister` | 308 | review: merge |
| `Ausserdem` | `außerdem` | 5,382 | review: merge |
| `Austrockn` | `austrocknen` | 632 | review: merge |
| `Auswander` | `auswandern` | 532 | review: merge |
| `Autofahre` | `Autofahren` | 673 | review: merge |
| `Automatenspiele` | `Automatenspiel` | 511 | review: merge |
| `Autonomer` | `autonom` | 708 | review: merge |
| `BANK` | `Bank` | 475 | review: merge |
| `BASE` | `Base` | 484 | review: merge |
| `BAU` | `Bau` | 703 | review: merge |
| `BEI` | `bei` | 1,888 | review: merge |
| `BERLIN` | `Berlin` | 1,681 | review: merge |
| `BESCHLUSS` | `Beschluss` | 753 | review: merge |
| `BILD` | `Bild` | 2,612 | review: merge |
| `BIS` | `bis` | 924 | review: merge |
| `BITTE` | `bitte` | 1,178 | review: merge |
| `BOSS` | `Boss` | 563 | review: merge |
| `BUND` | `Bund` | 1,588 | review: merge |
| `BUNDESGERICHTSHOF` | `Bundesgerichtshof` | 827 | review: merge |
| `Backstag` | `Backstage` | 475 | review: merge |
| `Bang` | `bang` | 1,389 | review: merge |
| `Bankdat` | `Bankdaten` | 788 | review: merge |
| `Barrier` | `Barriere` | 2,080 | review: merge |
| `Basteln` | `basteln` | 2,410 | review: merge |
| `Beamtinn` | `Beamtin` | 664 | review: merge |
| `Begrifflichkeite` | `Begrifflichkeit` | 660 | review: merge |
| `Bemerkenswert` | `bemerkenswert` | 1,162 | review: merge |
| `Benutzerdate` | `Benutzerdaten` | 530 | review: merge |
| `Beobacht` | `beobachten` | 809 | review: merge |
| `Beratungsstell` | `Beratungsstelle` | 1,425 | review: merge |
| `Berufliche` | `beruflich` | 501 | review: merge |
| `Bescheinigunge` | `Bescheinigung` | 695 | review: merge |
| `Beschleunig` | `beschleunigen` | 516 | review: merge |
| `Bestandsdat` | `Bestandsdaten` | 589 | review: merge |
| `Bestelldate` | `Bestelldaten` | 571 | review: merge |
| `Bestens` | `bestens` | 677 | review: merge |
| `Bestrebunge` | `Bestrebung` | 588 | review: merge |
| `Bestätig` | `bestätigen` | 517 | review: merge |
| `BesucherInn` | `Besucher` | 549 | review: merge |
| `Besucherinn` | `Besucherin` | 1,690 | review: merge |
| `Betriebsrät` | `Betriebsrat` | 679 | review: merge |
| `Bewerbungsschreibe` | `Bewerbungsschreiben` | 606 | review: merge |
| `Bewert` | `bewerten` | 1,045 | review: merge |
| `BewohnerInne` | `Bewohnerin` | 504 | review: merge |
| `Bewohnerinne` | `Bewohnerin` | 954 | review: merge |
| `Bikes` | `Bike` | 638 | review: merge |
| `Bin` | `sein` | 1,019 | review: merge |
| `Bitter` | `bitter` | 666 | review: merge |
| `Blank` | `blank` | 500 | review: merge |
| `Blend` | `Blender` | 511 | review: merge |
| `Bläsch` | `Bläschen` | 767 | review: merge |
| `Blümche` | `Blümchen` | 941 | review: merge |
| `Bodenbeläg` | `Bodenbelag` | 480 | review: merge |
| `Braun` | `braun` | 5,879 | review: merge |
| `Briefkast` | `Briefkasten` | 511 | review: merge |
| `Bring` | `bringen` | 1,391 | review: merge |
| `Broschierte` | `broschiert` | 683 | review: merge |
| `Browsergames` | `Browsergame` | 591 | review: merge |
| `Brutto` | `brutto` | 564 | review: merge |
| `Byt` | `Byte` | 813 | review: merge |
| `BÜNDNIS` | `Bündnis` | 755 | review: merge |
| `Bündche` | `Bündchen` | 1,127 | review: merge |
| `CHIP` | `Chip` | 544 | review: merge |
| `CPUs` | `CPU` | 521 | review: merge |
| `Chakr` | `Chakra` | 507 | review: merge |
| `Chic` | `chic` | 1,058 | review: merge |
| `Clever` | `clever` | 692 | review: merge |
| `Coaches` | `Coach` | 759 | review: merge |
| `Communitie` | `Community` | 698 | review: merge |
| `Cool` | `cool` | 2,162 | review: merge |
| `Covers` | `Cover` | 535 | review: merge |
| `Creatin` | `Kreatin` | 642 | review: merge |
| `DA` | `da` | 1,272 | review: merge |
| `DACH` | `Dach` | 532 | review: merge |
| `DANKE` | `danke` | 2,554 | review: merge |
| `DANN` | `dann` | 558 | review: merge |
| `DASS` | `dass` | 488 | review: merge |
| `DATEN` | `Daten` | 896 | review: merge |
| `DER` | `der` | 16,055 | review: merge |
| `DESIGN` | `Design` | 819 | review: merge |
| `DOWNLOAD` | `Download` | 736 | review: merge |
| `DU` | `du` | 3,972 | review: merge |
| `DURCH` | `durch` | 742 | review: merge |
| `Datenschutzbeauftragt` | `Datenschutzbeauftragte` | 2,545 | review: merge |
| `Debut` | `Debüt` | 370 | review: merge |
| `Deckenleucht` | `Deckenleuchte` | 989 | review: merge |
| `Demontag` | `Demontage` | 1,315 | review: merge |
| `Desweitere` | `desweiteren` | 2,612 | review: merge |
| `Detaillierter` | `detailliert` | 529 | review: merge |
| `Deutscher Bundestag` | `Bundestag` | 3,496 | review: merge |
| `Dick` | `dick` | 1,539 | review: merge |
| `Digital` | `digital` | 10,953 | review: merge |
| `Diskutier` | `diskutieren` | 1,853 | review: merge |
| `Doll` | `doll` | 676 | review: merge |
| `Donnerstagmorg` | `Donnerstagmorgen` | 584 | review: merge |
| `Dr` | `Doktor` | 995 | review: merge |
| `Druckdat` | `Druckdaten` | 477 | review: merge |
| `Druckstell` | `Druckstelle` | 604 | review: merge |
| `Durchblutungsstörunge` | `Durchblutungsstörung` | 586 | review: merge |
| `Dämone` | `Dämon` | 1,168 | review: merge |
| `E-Bikes` | `E-Bike` | 1,086 | review: merge |
| `E-Mailadresse` | `E-Mail-Adresse` | 1,534 | review: merge |
| `E-mail` | `E-Mail` | 1,403 | review: merge |
| `EINER` | `ein` | 822 | review: merge |
| `EINFACH` | `einfach` | 774 | review: merge |
| `ERGO` | `ergo` | 613 | review: merge |
| `ETFs` | `ETF` | 1,805 | review: merge |
| `EU-Mitgliedsstaat` | `EU-Mitgliedstaat` | 526 | review: merge |
| `EURO` | `Euro` | 2,458 | review: merge |
| `EUROPA` | `Europa` | 480 | review: merge |
| `EX` | `Ex` | 477 | review: merge |
| `Ehrlich` | `ehrlich` | 544 | review: merge |
| `Eindring` | `eindringen` | 1,516 | review: merge |
| `Einfüg` | `einfügen` | 1,663 | review: merge |
| `Email-Adresse` | `E-Mail-Adresse` | 1,600 | review: merge |
| `Englischkenntnis` | `Englischkenntnisse` | 2,221 | review: merge |
| `Enter` | `entern` | 591 | review: merge |
| `Erarbeit` | `erarbeiten` | 515 | review: merge |
| `Erlangen` | `erlangen` | 3,353 | review: merge |
| `Erlern` | `erlernen` | 541 | review: merge |
| `Ermesse` | `Ermessen` | 2,483 | review: merge |
| `Erwart` | `erwarten` | 782 | review: merge |
| `Essgewohnheite` | `Essgewohnheit` | 513 | review: merge |
| `Euro-Zone` | `Eurozone` | 706 | review: merge |
| `Evtl` | `evtl` | 1,648 | review: merge |
| `Exklusiv` | `exklusiv` | 1,987 | review: merge |
| `Extrem` | `extrem` | 5,109 | review: merge |
| `FAQs` | `FAQ` | 1,212 | review: merge |
| `FIT` | `fit` | 856 | review: merge |
| `FORUM` | `Forum` | 584 | review: merge |
| `FRANKFURT` | `Frankfurt` | 617 | review: merge |
| `Fahrradfahr` | `Fahrradfahren` | 1,022 | review: merge |
| `Fehlstellunge` | `Fehlstellung` | 481 | review: merge |
| `Fers` | `Ferse` | 1,461 | review: merge |
| `Festleg` | `festlegen` | 580 | review: merge |
| `Fettsäur` | `Fettsäure` | 3,650 | review: merge |
| `Final` | `final` | 3,052 | review: merge |
| `Finaliste` | `Finalist` | 923 | review: merge |
| `Fkk` | `FKK` | 544 | review: merge |
| `Flatrat` | `Flatrate` | 726 | review: merge |
| `Flied` | `Flieder` | 488 | review: merge |
| `Fohle` | `Fohlen` | 1,054 | review: merge |
| `Forder` | `fordern` | 1,909 | review: merge |
| `Fortschreit` | `fortschreiten` | 537 | review: merge |
| `Fossili` | `Fossil` | 488 | review: merge |
| `Fotografier` | `fotografieren` | 1,574 | review: merge |
| `Fototapet` | `Fototapete` | 557 | review: merge |
| `Fotz` | `Fotze` | 1,502 | review: merge |
| `Fröhlich` | `fröhlich` | 874 | review: merge |
| `Funktionsweis` | `Funktionsweise` | 2,003 | review: merge |
| `Fur` | `für` | 938 | review: merge |
| `Fußpfleg` | `Fußpflege` | 573 | review: merge |
| `FÜR` | `für` | 10,861 | review: merge |
| `Fältche` | `Fältchen` | 817 | review: merge |
| `Förmche` | `Förmchen` | 523 | review: merge |
| `Für` | `für` | 973 | review: merge |
| `Füs` | `Fuß` | 1,040 | review: merge |
| `GANZ` | `ganz` | 494 | review: merge |
| `GEGEN` | `gegen` | 729 | review: merge |
| `GMBH` | `GmbH` | 841 | review: merge |
| `GNU` | `Gnu` | 781 | review: merge |
| `GOLD` | `Gold` | 613 | review: merge |
| `GOTT` | `Gott` | 797 | review: merge |
| `GRATIS` | `gratis` | 1,034 | review: merge |
| `GUT` | `gut` | 1,036 | review: merge |
| `Gallen` | `Galle` | 519 | review: merge |
| `Gar` | `gar` | 1,121 | review: merge |
| `Geland` | `Geländer` | 787 | review: merge |
| `Gemeinderät` | `Gemeinderat` | 489 | review: merge |
| `Gemeinsame` | `gemeinsam` | 502 | review: merge |
| `Gemäss` | `gemäß` | 1,393 | review: merge |
| `German` | `Germane` | 6,526 | review: merge |
| `Geschenkideen` | `Geschenkidee` | 1,329 | review: merge |
| `Gesundheitsdat` | `Gesundheitsdaten` | 553 | review: merge |
| `Getreu` | `getreu` | 865 | review: merge |
| `Geweb` | `Gewebe` | 6,067 | review: merge |
| `Gewind` | `Gewinde` | 1,715 | review: merge |
| `Gewinnspiele` | `Gewinnspiel` | 499 | review: merge |
| `Gliedmaß` | `Gliedmaße` | 900 | review: merge |
| `Global` | `global` | 7,407 | review: merge |
| `Glücklicherweis` | `glücklicherweise` | 1,434 | review: merge |
| `Gmbh` | `GmbH` | 672 | review: merge |
| `Golden` | `golden` | 3,953 | review: merge |
| `Golf#Masc` | `Golf` | 723 | review: merge |
| `Gro` | `Gros` | 499 | review: merge |
| `Gross` | `groß` | 1,293 | review: merge |
| `HAMBURG` | `Hamburg` | 605 | review: merge |
| `HAUS` | `Haus` | 531 | review: merge |
| `HERRN` | `Herr` | 1,271 | review: merge |
| `HEUTE` | `heute` | 818 | review: merge |
| `HIER` | `hier` | 5,677 | review: merge |
| `HILFE` | `Hilfe` | 477 | review: merge |
| `HINWEIS` | `Hinweis` | 1,235 | review: merge |
| `HM` | `hm` | 781 | review: merge |
| `HOTEL` | `Hotel` | 511 | review: merge |
| `Halterunge` | `Halterung` | 884 | review: merge |
| `Handlungsempfehlunge` | `Handlungsempfehlung` | 1,297 | review: merge |
| `Handtaschen` | `Handtasche` | 666 | review: merge |
| `Handumdreh` | `Handumdrehen` | 2,392 | review: merge |
| `Hart` | `hart` | 1,787 | review: merge |
| `Hauptroll` | `Hauptrolle` | 2,715 | review: merge |
| `Hautpfleg` | `Hautpflege` | 1,292 | review: merge |
| `Hbf` | `Hauptbahnhof` | 653 | review: merge |
| `Heilig` | `heilig` | 686 | review: merge |
| `Helferinn` | `Helferin` | 657 | review: merge |
| `Her` | `her` | 1,360 | review: merge |
| `Heraus` | `heraus` | 527 | review: merge |
| `Herzrase` | `Herzrasen` | 523 | review: merge |
| `Herzrhythmusstörunge` | `Herzrhythmusstörung` | 774 | review: merge |
| `Hierdurch` | `hierdurch` | 2,461 | review: merge |
| `Hilfestellunge` | `Hilfestellung` | 1,470 | review: merge |
| `Hinzufüg` | `hinzufügen` | 2,726 | review: merge |
| `Hode` | `Hoden` | 975 | review: merge |
| `Hol` | `holen` | 1,553 | review: merge |
| `Homepag` | `Homepage` | 931 | review: merge |
| `Human` | `human` | 2,698 | review: merge |
| `Hyperlinks` | `Hyperlink` | 1,616 | review: merge |
| `Händche` | `Händchen` | 1,011 | review: merge |
| `Händewasch` | `Händewaschen` | 494 | review: merge |
| `Häppche` | `Häppchen` | 559 | review: merge |
| `Häusche` | `Häuschen` | 1,592 | review: merge |
| `ICH` | `ich` | 4,102 | review: merge |
| `IMMER` | `immer` | 742 | review: merge |
| `IN` | `in` | 7,390 | review: merge |
| `INFO` | `Info` | 553 | review: merge |
| `INFORMATION` | `Information` | 629 | review: merge |
| `INFORMATIONEN` | `Information` | 681 | review: merge |
| `INHALT` | `Inhalt` | 813 | review: merge |
| `INHALTSVERZEICHNIS` | `Inhaltsverzeichnis` | 631 | review: merge |
| `ISS` | `essen` | 1,064 | review: merge |
| `Importier` | `importieren` | 899 | review: merge |
| `Indian` | `Indianer` | 1,671 | review: merge |
| `Indizier` | `indizieren` | 551 | review: merge |
| `Inflationsrat` | `Inflationsrate` | 795 | review: merge |
| `Inklusive` | `inklusive` | 1,740 | review: merge |
| `Inkrafttret` | `Inkrafttreten` | 2,124 | review: merge |
| `Inmitt` | `inmitten` | 1,258 | review: merge |
| `Inner` | `Innere` | 2,988 | review: merge |
| `Inputs` | `Input` | 520 | review: merge |
| `Inserente` | `Inserent` | 769 | review: merge |
| `Institute` | `Institut` | 2,438 | review: merge |
| `Intensiv` | `intensiv` | 732 | review: merge |
| `Interessanterweis` | `interessanterweise` | 524 | review: merge |
| `International` | `international` | 14,854 | review: merge |
| `Internet-Seite` | `Internetseite` | 1,328 | review: merge |
| `Investieren` | `investieren` | 1,261 | review: merge |
| `Inwiefer` | `inwiefern` | 1,063 | review: merge |
| `JETZT` | `jetzt` | 3,229 | review: merge |
| `Jahrelang` | `jahrelang` | 945 | review: merge |
| `Jeweil` | `jeweils` | 1,364 | review: merge |
| `Jeweils` | `jeweils` | 474 | review: merge |
| `Jg` | `Jahrgang` | 913 | review: merge |
| `Jogg` | `joggen` | 1,411 | review: merge |
| `Jugendherberg` | `Jugendherberge` | 1,522 | review: merge |
| `Jung` | `jung` | 6,877 | review: merge |
| `KLICK` | `Klick` | 685 | review: merge |
| `KOSTENLOS` | `kostenlos` | 1,070 | review: merge |
| `Kapitaliste` | `Kapitalist` | 577 | review: merge |
| `Karpfe` | `Karpfen` | 770 | review: merge |
| `Kart` | `Karte` | 824 | review: merge |
| `Kartenleg` | `Kartenlegen` | 808 | review: merge |
| `Katalonie` | `Katalonien` | 729 | review: merge |
| `Kath` | `katholisch` | 534 | review: merge |
| `Kleinanzeig` | `Kleinanzeige` | 768 | review: merge |
| `Kleinanzeigen` | `Kleinanzeige` | 2,855 | review: merge |
| `Kommentier` | `kommentieren` | 646 | review: merge |
| `Kompatibel` | `kompatibel` | 1,508 | review: merge |
| `Konfitür` | `Konfitüre` | 566 | review: merge |
| `Konkurrente` | `Konkurrent` | 4,536 | review: merge |
| `Konsen` | `Konsens` | 2,073 | review: merge |
| `Kontaktanzeig` | `Kontaktanzeige` | 1,731 | review: merge |
| `Kontodate` | `Kontodaten` | 775 | review: merge |
| `Koriand` | `Koriander` | 858 | review: merge |
| `Kostengründen` | `Kostengrund` | 571 | review: merge |
| `Krankenpfleg` | `Krankenpflege` | 574 | review: merge |
| `Kreditkartendat` | `Kreditkartendaten` | 907 | review: merge |
| `Kundendate` | `Kundendaten` | 2,190 | review: merge |
| `Kunstrase` | `Kunstrasen` | 469 | review: merge |
| `Kurzer` | `kurz` | 476 | review: merge |
| `Kurzum` | `kurzum` | 1,423 | review: merge |
| `Kuvertür` | `Kuvertüre` | 609 | review: merge |
| `KÖNNEN` | `können` | 642 | review: merge |
| `Kärtche` | `Kärtchen` | 742 | review: merge |
| `Köpfch` | `Köpfchen` | 586 | review: merge |
| `Körbche` | `Körbchen` | 1,009 | review: merge |
| `KünstlerInn` | `Künstler` | 549 | review: merge |
| `LEBEN` | `Leben` | 1,058 | review: merge |
| `LESEN` | `lesen` | 466 | review: merge |
| `LINK` | `Link` | 648 | review: merge |
| `LIVE` | `live` | 1,419 | review: merge |
| `LOTTO` | `Lotto` | 737 | review: merge |
| `Lahm` | `lahm` | 931 | review: merge |
| `Lange` | `lange` | 5,679 | review: merge |
| `Leckerbisse` | `Leckerbissen` | 1,031 | review: merge |
| `Leckereie` | `Leckerei` | 2,376 | review: merge |
| `Legal` | `legal` | 1,278 | review: merge |
| `LehrerInnen` | `Lehrer` | 774 | review: merge |
| `Leistungsdate` | `Leistungsdaten` | 534 | review: merge |
| `Liebevoll` | `liebevoll` | 650 | review: merge |
| `Liegenschafte` | `Liegenschaft` | 939 | review: merge |
| `Linkshänd` | `Linkshänder` | 474 | review: merge |
| `Live` | `live` | 3,260 | review: merge |
| `Lockerunge` | `Lockerung` | 641 | review: merge |
| `Logisch` | `logisch` | 548 | review: merge |
| `Looks` | `Look` | 818 | review: merge |
| `Lustig` | `lustig` | 496 | review: merge |
| `Lymphknote` | `Lymphknoten` | 745 | review: merge |
| `MACHEN` | `machen` | 492 | review: merge |
| `MAN` | `man` | 1,652 | review: merge |
| `MEGA` | `mega` | 474 | review: merge |
| `MENSCHEN` | `Mensch` | 484 | review: merge |
| `MIT` | `mit` | 6,629 | review: merge |
| `MUSS` | `müssen` | 1,111 | review: merge |
| `Makeup` | `Make-up` | 683 | review: merge |
| `Malediv` | `Malediven` | 604 | review: merge |
| `Malwar` | `Malware` | 3,199 | review: merge |
| `Maniere` | `Manieren` | 471 | review: merge |
| `Manner` | `Mann` | 742 | review: merge |
| `Massiv` | `massiv` | 570 | review: merge |
| `Massnahme` | `Maßnahme` | 650 | review: merge |
| `Masterstudiengäng` | `Masterstudiengang` | 603 | review: merge |
| `Matt` | `matt` | 3,288 | review: merge |
| `Maxim` | `Maxime` | 1,021 | review: merge |
| `Mediadate` | `Mediadaten` | 488 | review: merge |
| `Meerschweinche` | `Meerschweinchen` | 1,047 | review: merge |
| `Mental` | `mental` | 482 | review: merge |
| `Menu` | `Menü` | 965 | review: merge |
| `Merke` | `merken` | 3,024 | review: merge |
| `Messdat` | `Messdaten` | 561 | review: merge |
| `Messia` | `Messias` | 736 | review: merge |
| `Metadat` | `Metadaten` | 1,627 | review: merge |
| `Mi` | `Mittwoch` | 1,835 | review: merge |
| `Mietverhältniss` | `Mietverhältnis` | 542 | review: merge |
| `MigrantInn` | `Migrant` | 468 | review: merge |
| `Migrantinn` | `Migrantin` | 674 | review: merge |
| `Mikroorganism` | `Mikroorganismus` | 1,695 | review: merge |
| `Miser` | `Misere` | 643 | review: merge |
| `Missständ` | `Missstand` | 1,131 | review: merge |
| `Mo` | `Montag` | 1,932 | review: merge |
| `Modern` | `modern` | 3,458 | review: merge |
| `Mormon` | `Mormone` | 2,229 | review: merge |
| `Mountainbik` | `Mountainbike` | 596 | review: merge |
| `Musikante` | `Musikant` | 626 | review: merge |
| `Musizier` | `musizieren` | 1,013 | review: merge |
| `MÜNCHEN` | `München` | 521 | review: merge |
| `Männch` | `Männchen` | 2,322 | review: merge |
| `NACH` | `nach` | 1,464 | review: merge |
| `NEIN` | `nein` | 1,937 | review: merge |
| `NEU` | `neu` | 4,675 | review: merge |
| `NICHTS` | `nichts` | 901 | review: merge |
| `NIE` | `nie` | 1,069 | review: merge |
| `NOCH` | `noch` | 1,178 | review: merge |
| `NORD` | `Nord` | 466 | review: merge |
| `NUR` | `nur` | 2,760 | review: merge |
| `Nachfrag` | `Nachfrage` | 1,610 | review: merge |
| `Nackt` | `nackt` | 1,323 | review: merge |
| `Nah` | `nah` | 671 | review: merge |
| `Navigier` | `navigieren` | 571 | review: merge |
| `Neopr` | `Neopren` | 649 | review: merge |
| `Netto` | `netto` | 1,433 | review: merge |
| `Neuer` | `neu` | 2,686 | review: merge |
| `Neuerscheinunge` | `Neuerscheinung` | 780 | review: merge |
| `Neutral` | `neutral` | 471 | review: merge |
| `Nie` | `nie` | 4,178 | review: merge |
| `Normal` | `normal` | 1,414 | review: merge |
| `Notfäll` | `Notfall` | 987 | review: merge |
| `Nov` | `November` | 1,527 | review: merge |
| `Nutzerdat` | `Nutzerdaten` | 1,442 | review: merge |
| `Nutzerinne` | `Nutzerin` | 815 | review: merge |
| `Nutzungsdate` | `Nutzungsdaten` | 810 | review: merge |
| `OB` | `ob` | 1,580 | review: merge |
| `ODER` | `oder` | 2,273 | review: merge |
| `OHNE` | `ohne` | 2,201 | review: merge |
| `ORIGINAL` | `Original` | 504 | review: merge |
| `Ochs` | `Ochse` | 469 | review: merge |
| `Oder` | `oder` | 2,900 | review: merge |
| `Onlin` | `online` | 11,775 | review: merge |
| `Oral` | `oral` | 696 | review: merge |
| `Out` | `out` | 2,437 | review: merge |
| `PI` | `Pi` | 1,376 | review: merge |
| `PIRATEN` | `Pirat` | 665 | review: merge |
| `PLUS` | `plus` | 2,071 | review: merge |
| `PREMIUM` | `Premium` | 796 | review: merge |
| `PRO` | `pro` | 2,585 | review: merge |
| `PULS` | `Puls` | 1,128 | review: merge |
| `Paillett` | `Paillette` | 594 | review: merge |
| `Panikattack` | `Panikattacke` | 638 | review: merge |
| `Paprikaschot` | `Paprikaschote` | 504 | review: merge |
| `Parties` | `Party` | 801 | review: merge |
| `Performances` | `Performance` | 618 | review: merge |
| `Personendat` | `Personendaten` | 953 | review: merge |
| `Perück` | `Perücke` | 501 | review: merge |
| `Pfingst` | `Pfingsten` | 1,803 | review: merge |
| `Pflegeheime` | `Pflegeheim` | 725 | review: merge |
| `Pfort` | `Pforte` | 2,251 | review: merge |
| `Philippine` | `Philippinen` | 923 | review: merge |
| `Photo` | `Foto` | 3,004 | review: merge |
| `Plantag#day` | `Plantage` | 847 | review: merge |
| `Plastiktüt` | `Plastiktüte` | 578 | review: merge |
| `Platzier` | `platzieren` | 485 | review: merge |
| `Plug-Ins` | `Plug-in` | 540 | review: merge |
| `Point` | `Pointe` | 4,591 | review: merge |
| `Polyethyl` | `Polyethylen` | 589 | review: merge |
| `Polypropyl` | `Polypropylen` | 646 | review: merge |
| `Populiste` | `Populist` | 468 | review: merge |
| `Postbot` | `Postbote` | 624 | review: merge |
| `Potential` | `Potenzial` | 1,822 | review: merge |
| `Praktikante` | `Praktikant` | 1,388 | review: merge |
| `Preis-Leistung` | `Preis-Leistungs-Verhältnis` | 523 | review: merge |
| `Preiswert` | `preiswert` | 534 | review: merge |
| `Prellunge` | `Prellung` | 507 | review: merge |
| `Press` | `pressen` | 2,108 | review: merge |
| `Presse-Agentur` | `Presseagentur` | 1,860 | review: merge |
| `Prima` | `prima` | 1,433 | review: merge |
| `Problemstellunge` | `Problemstellung` | 946 | review: merge |
| `Produktionsstätt` | `Produktionsstätte` | 849 | review: merge |
| `Promis` | `Promi` | 1,399 | review: merge |
| `Präsentier` | `präsentieren` | 479 | review: merge |
| `Punkto` | `puncto` | 560 | review: merge |
| `QM` | `qm` | 676 | review: merge |
| `QUALITÄT` | `Qualität` | 721 | review: merge |
| `Quasi` | `quasi` | 791 | review: merge |
| `ROM` | `Rom` | 477 | review: merge |
| `Radiesche` | `Radieschen` | 537 | review: merge |
| `Rally` | `Rallye` | 796 | review: merge |
| `Rasch` | `rasch` | 573 | review: merge |
| `Rau` | `rau` | 533 | review: merge |
| `Raus` | `raus` | 1,635 | review: merge |
| `Real` | `real` | 5,414 | review: merge |
| `Rechenzentr` | `Rechenzentrum` | 1,689 | review: merge |
| `Rechtsfolg` | `Rechtsfolge` | 524 | review: merge |
| `Rechtspopuliste` | `Rechtspopulist` | 709 | review: merge |
| `Regularie` | `Regularien` | 504 | review: merge |
| `Reichweit` | `Reichweite` | 549 | review: merge |
| `Reisedat` | `Reisedaten` | 570 | review: merge |
| `Reizunge` | `Reizung` | 666 | review: merge |
| `Reportag` | `Reportage` | 3,092 | review: merge |
| `Revolt` | `Revolte` | 551 | review: merge |
| `Rezepture` | `Rezeptur` | 916 | review: merge |
| `Rhiniti` | `Rhinitis` | 548 | review: merge |
| `Rieme` | `Riemen` | 1,561 | review: merge |
| `Rosa` | `rosa` | 4,502 | review: merge |
| `Röntg` | `Röntgen` | 768 | review: merge |
| `Rückleucht` | `Rückleuchte` | 498 | review: merge |
| `Rückstellunge` | `Rückstellung` | 593 | review: merge |
| `SEHR` | `sehr` | 1,210 | review: merge |
| `SELBST` | `selbst` | 552 | review: merge |
| `SERVICE` | `Service` | 645 | review: merge |
| `SET` | `Set` | 503 | review: merge |
| `SICH` | `sich` | 1,218 | review: merge |
| `SICHERHEIT` | `Sicherheit` | 474 | review: merge |
| `SMART` | `smart` | 608 | review: merge |
| `SO` | `so` | 1,114 | review: merge |
| `SOFORT` | `sofort` | 966 | review: merge |
| `SPA` | `Spa` | 1,075 | review: merge |
| `SPIEGEL` | `Spiegel` | 2,457 | review: merge |
| `SPORT` | `Sport` | 661 | review: merge |
| `STADT` | `Stadt` | 465 | review: merge |
| `STANDARD` | `Standard` | 1,619 | review: merge |
| `STAR` | `Star` | 561 | review: merge |
| `SUPER` | `super` | 779 | review: merge |
| `SYSTEM` | `System` | 475 | review: merge |
| `Sa` | `Samstag` | 2,086 | review: merge |
| `Sabotag` | `Sabotage` | 539 | review: merge |
| `Salafiste` | `Salafist` | 678 | review: merge |
| `Salbum` | `Salbe` | 1,300 | review: merge |
| `Saucen` | `Sauce` | 557 | review: merge |
| `Saun` | `Sauna` | 913 | review: merge |
| `Schalott` | `Schalotte` | 882 | review: merge |
| `Schlafengehe` | `Schlafengehen` | 943 | review: merge |
| `Schlafstörunge` | `Schlafstörung` | 2,667 | review: merge |
| `Schlank` | `schlank` | 577 | review: merge |
| `Schlauf` | `Schlaufe` | 804 | review: merge |
| `Schleimhäut` | `Schleimhaut` | 840 | review: merge |
| `Schlesie` | `Schlesien` | 521 | review: merge |
| `Schliessung` | `Schließung` | 332 | review: merge |
| `Schnupfe` | `Schnupfen` | 1,443 | review: merge |
| `Schreibware` | `Schreibwaren` | 486 | review: merge |
| `Schubkast` | `Schubkasten` | 477 | review: merge |
| `Schulranz` | `Schulranzen` | 721 | review: merge |
| `Schwarz` | `schwarz` | 17,192 | review: merge |
| `Schweißen` | `schweißen` | 956 | review: merge |
| `Schwellunge` | `Schwellung` | 1,700 | review: merge |
| `Schätzche` | `Schätzchen` | 601 | review: merge |
| `Schön` | `schön` | 1,697 | review: merge |
| `Scree` | `Screen` | 871 | review: merge |
| `Services` | `Service` | 16,654 | review: merge |
| `Serviett` | `Serviette` | 752 | review: merge |
| `Seychelle` | `Seychellen` | 592 | review: merge |
| `Short` | `Shorts` | 2,500 | review: merge |
| `Singen` | `singen` | 935 | review: merge |
| `Skipist` | `Skipiste` | 487 | review: merge |
| `Smart` | `smart` | 10,852 | review: merge |
| `Software-Entwicklung` | `Softwareentwicklung` | 586 | review: merge |
| `Solar` | `solar` | 3,593 | review: merge |
| `Soliste` | `Solist` | 940 | review: merge |
| `Sonnencrem` | `Sonnencreme` | 846 | review: merge |
| `Sonnenstrahle` | `Sonnenstrahl` | 2,013 | review: merge |
| `Sozialleistungen` | `Sozialleistung` | 1,081 | review: merge |
| `Spermie` | `Spermium` | 625 | review: merge |
| `Spielwar` | `Spielwaren` | 918 | review: merge |
| `Spontan` | `spontan` | 706 | review: merge |
| `Sports` | `Sport` | 4,942 | review: merge |
| `Sportstätt` | `Sportstätte` | 643 | review: merge |
| `Spots` | `Spot` | 741 | review: merge |
| `Spring` | `springen` | 2,145 | review: merge |
| `Springen` | `springen` | 928 | review: merge |
| `Stammdat` | `Stammdaten` | 950 | review: merge |
| `Standardmäßig` | `standardmäßig` | 1,468 | review: merge |
| `Start-ups` | `Start-up` | 1,480 | review: merge |
| `Std` | `Stunde` | 969 | review: merge |
| `Steh` | `stehen` | 510 | review: merge |
| `Steinche` | `Steinchen` | 551 | review: merge |
| `Stellenanzeig` | `Stellenanzeige` | 1,956 | review: merge |
| `Sternch` | `Sternchen` | 1,003 | review: merge |
| `Sternche` | `Sternchen` | 541 | review: merge |
| `Steroide` | `Steroid` | 477 | review: merge |
| `Stimmungsschwankunge` | `Stimmungsschwankung` | 631 | review: merge |
| `Stop` | `Stopp` | 2,089 | review: merge |
| `Stornierunge` | `Stornierung` | 915 | review: merge |
| `Strassenverkehr` | `Straßenverkehr` | 364 | review: merge |
| `Stromanbiet` | `Stromanbieter` | 588 | review: merge |
| `Sträng` | `Strang` | 514 | review: merge |
| `Studiengäng` | `Studiengang` | 2,750 | review: merge |
| `Stäbche` | `Stäbchen` | 1,116 | review: merge |
| `Suchergebnisse` | `Suchergebnis` | 631 | review: merge |
| `Suchworte` | `Suchwort` | 4,188 | review: merge |
| `Suit` | `Suite` | 2,827 | review: merge |
| `Synergien` | `Synergie` | 788 | review: merge |
| `SÜD` | `Süd` | 719 | review: merge |
| `TAG` | `Tag` | 987 | review: merge |
| `TEAM` | `Team` | 612 | review: merge |
| `TEIL` | `Teil` | 470 | review: merge |
| `TIPP` | `Tipp` | 988 | review: merge |
| `TOP` | `Top` | 6,091 | review: merge |
| `TU` | `tun` | 4,190 | review: merge |
| `Tauchgäng` | `Tauchgang` | 524 | review: merge |
| `TeilnehmerInn` | `Teilnehmer` | 548 | review: merge |
| `TeilnehmerInne` | `Teilnehmerin` | 1,371 | review: merge |
| `Templat` | `Template` | 711 | review: merge |
| `Textdateien` | `Textdatei` | 567 | review: merge |
| `Tierche` | `Tierchen` | 657 | review: merge |
| `Tigers` | `Tiger` | 762 | review: merge |
| `Tirols` | `Tirol` | 517 | review: merge |
| `Tischleucht` | `Tischleuchte` | 590 | review: merge |
| `Tomat` | `Tomate` | 517 | review: merge |
| `Torchancen` | `Torchance` | 588 | review: merge |
| `Total` | `total` | 2,930 | review: merge |
| `Touchscree` | `Touchscreen` | 2,003 | review: merge |
| `Tracks` | `Track` | 719 | review: merge |
| `Tunesie` | `Tunesien` | 711 | review: merge |
| `Turn` | `turnen` | 1,340 | review: merge |
| `Tv` | `TV` | 820 | review: merge |
| `Törtche` | `Törtchen` | 521 | review: merge |
| `Türche` | `Türchen` | 1,238 | review: merge |
| `Türki` | `Türkis` | 502 | review: merge |
| `UND` | `und` | 18,465 | review: merge |
| `UNTER` | `unter` | 522 | review: merge |
| `UPDATE` | `Update` | 1,040 | review: merge |
| `UPS` | `ups` | 1,412 | review: merge |
| `Umsetz` | `umsetzen` | 821 | review: merge |
| `Unkompliziert` | `unkompliziert` | 585 | review: merge |
| `Unternehmensdat` | `Unternehmensdaten` | 501 | review: merge |
| `Unternehmerinn` | `Unternehmerin` | 604 | review: merge |
| `Urban` | `urban` | 3,397 | review: merge |
| `VIDEO` | `Video` | 658 | review: merge |
| `VIEL` | `viel` | 588 | review: merge |
| `VOM` | `vom` | 718 | review: merge |
| `VON` | `von` | 5,272 | review: merge |
| `VOR` | `vor` | 1,443 | review: merge |
| `Vanilleschot` | `Vanilleschote` | 582 | review: merge |
| `Variz` | `Varize` | 1,831 | review: merge |
| `Vegan` | `vegan` | 1,776 | review: merge |
| `Veilche` | `Veilchen` | 660 | review: merge |
| `Ven` | `Vene` | 2,613 | review: merge |
| `Verbe` | `Verb` | 1,149 | review: merge |
| `Verbesser` | `verbessern` | 723 | review: merge |
| `Verbraucherinn` | `Verbraucherin` | 519 | review: merge |
| `Verfehlunge` | `Verfehlung` | 502 | review: merge |
| `Verguetung` | `Vergütung` | 346 | review: merge |
| `Versag` | `Versagen` | 580 | review: merge |
| `Verschmutzunge` | `Verschmutzung` | 1,833 | review: merge |
| `Verschuld` | `verschulden` | 1,860 | review: merge |
| `Verstrickunge` | `Verstrickung` | 490 | review: merge |
| `Vertreterinn` | `Vertreterin` | 929 | review: merge |
| `Vital` | `vital` | 909 | review: merge |
| `Vli` | `Vlies` | 754 | review: merge |
| `Voll` | `voll` | 1,930 | review: merge |
| `Vorab` | `vorab` | 1,615 | review: merge |
| `Vorlieg` | `vorliegen` | 2,344 | review: merge |
| `Vorraussetzunge` | `Voraussetzung` | 549 | review: merge |
| `Vorstoss` | `Vorstoß` | 397 | review: merge |
| `Vorwärt` | `vorwärts` | 515 | review: merge |
| `W-LAN` | `WLAN` | 937 | review: merge |
| `W-Lan` | `WLAN` | 842 | review: merge |
| `WARUM` | `warum` | 876 | review: merge |
| `WEG` | `weg` | 1,281 | review: merge |
| `WELT` | `Welt` | 1,772 | review: merge |
| `WENN` | `wenn` | 1,029 | review: merge |
| `WER` | `wer` | 678 | review: merge |
| `WERDEN` | `werden` | 1,081 | review: merge |
| `WICHTIG` | `wichtig` | 1,298 | review: merge |
| `WIE` | `wie` | 1,635 | review: merge |
| `WIEDER` | `wieder` | 484 | review: merge |
| `WIEN` | `Wien` | 562 | review: merge |
| `WILLKOMMEN` | `willkommen` | 638 | review: merge |
| `WOW` | `wow` | 1,206 | review: merge |
| `Wachstumsrat` | `Wachstumsrate` | 724 | review: merge |
| `Wandleucht` | `Wandleuchte` | 647 | review: merge |
| `Wandmontag` | `Wandmontage` | 662 | review: merge |
| `Ward` | `werden` | 659 | review: merge |
| `Web-Seite` | `Webseite` | 964 | review: merge |
| `Webcrwaler` | `Webcrawler` | 829 | review: merge |
| `Wechseljahr` | `Wechseljahre` | 1,220 | review: merge |
| `Wedel` | `wedeln` | 799 | review: merge |
| `Wegweise` | `Wegweiser` | 2,181 | review: merge |
| `Weibche` | `Weibchen` | 906 | review: merge |
| `Weisse` | `weiß` | 889 | review: merge |
| `Weisswein` | `Weißwein` | 328 | review: merge |
| `Wel` | `Wels` | 845 | review: merge |
| `Werbeanzeig` | `Werbeanzeige` | 1,197 | review: merge |
| `Wieviele` | `wie viele` | 880 | review: merge |
| `Wild` | `wild` | 6,428 | review: merge |
| `Wissenschaftlerinne` | `Wissenschaftlerin` | 768 | review: merge |
| `WoW` | `wow` | 1,142 | review: merge |
| `Wohlergehe` | `Wohlergehen` | 1,428 | review: merge |
| `Wohlwolle` | `Wohlwollen` | 526 | review: merge |
| `Wurstwar` | `Wurstware` | 493 | review: merge |
| `Youtube-Kanal` | `YouTube-Kanal` | 482 | review: merge |
| `ZEIT` | `Zeit` | 2,619 | review: merge |
| `ZUM` | `zu` | 2,357 | review: merge |
| `ZUR` | `zu` | 1,798 | review: merge |
| `Zahlungsdate` | `Zahlungsdaten` | 788 | review: merge |
| `Zahnbürst` | `Zahnbürste` | 564 | review: merge |
| `Zahnspang` | `Zahnspange` | 616 | review: merge |
| `Zertifizierunge` | `Zertifizierung` | 1,105 | review: merge |
| `Zivilcourag` | `Zivilcourage` | 508 | review: merge |
| `Zubereit` | `zubereiten` | 518 | review: merge |
| `Zufrieden` | `zufrieden` | 610 | review: merge |
| `Zugriffsdat` | `Zugriffsdaten` | 782 | review: merge |
| `Zuhör` | `zuhören` | 1,297 | review: merge |
| `Zusag` | `Zusage` | 1,037 | review: merge |
| `Zusammentreffe` | `Zusammentreffen` | 515 | review: merge |
| `Zusammenwirke` | `Zusammenwirken` | 905 | review: merge |
| `Zustandekomm` | `Zustandekommen` | 696 | review: merge |
| `Zuverlässig` | `zuverlässig` | 711 | review: merge |
| `Zähneputz` | `Zähneputzen` | 885 | review: merge |
| `abhan` | `abhanden` | 643 | review: merge |
| `action` | `Action` | 585 | review: merge |
| `alkoholisieren` | `alkoholisiert` | 553 | review: merge |
| `alle` | `all` | 6,026 | review: merge |
| `alleinerziehen` | `alleinerziehend` | 688 | review: merge |
| `allerbe` | `allerbest` | 500 | review: merge |
| `allerhoch` | `allerhöchst` | 479 | review: merge |
| `altbewähren` | `altbewährt` | 733 | review: merge |
| `andr` | `ander` | 653 | review: merge |
| `anfragend` | `anfragen` | 717 | review: merge |
| `atemberauben` | `atemberaubend` | 2,959 | review: merge |
| `aufstreben` | `aufstrebend` | 949 | review: merge |
| `aufwärt` | `aufwärts` | 1,381 | review: merge |
| `ausbleibend` | `ausbleiben` | 515 | review: merge |
| `ausserdem` | `außerdem` | 2,982 | review: merge |
| `ausserordentlich` | `außerordentlich` | 1,086 | review: merge |
| `bahnbrechen` | `bahnbrechend` | 685 | review: merge |
| `beherzig` | `beherzigen` | 508 | review: merge |
| `beieinan` | `beieinander` | 804 | review: merge |
| `bequemen` | `bequem` | 2,029 | review: merge |
| `beschliessen` | `beschließen` | 312 | review: merge |
| `beschliesst` | `beschließen` | 370 | review: merge |
| `bewertet` | `bewerten` | 925 | review: merge |
| `bewus` | `bewusst` | 1,031 | review: merge |
| `bewölken` | `bewölkt` | 1,098 | review: merge |
| `bildgeben` | `bildgebend` | 538 | review: merge |
| `bit` | `Bit` | 727 | review: merge |
| `blin` | `blind` | 843 | review: merge |
| `boomend` | `boomen` | 503 | review: merge |
| `brilliant` | `brillant` | 548 | review: merge |
| `brüst` | `Brust` | 730 | review: merge |
| `business` | `Business` | 1,001 | review: merge |
| `ca` | `circa` | 8,738 | review: merge |
| `check` | `checken` | 765 | review: merge |
| `clonen` | `klonen` | 503 | review: merge |
| `dSGVO` | `DSGVO` | 905 | review: merge |
| `deutschen` | `Deutsche` | 524 | review: merge |
| `dezidieren` | `dezidiert` | 500 | review: merge |
| `dosierung` | `Dosierung` | 1,123 | review: merge |
| `draussen` | `draußen` | 3,057 | review: merge |
| `durcheinan` | `durcheinander` | 1,475 | review: merge |
| `dünnen` | `dünn` | 699 | review: merge |
| `e-Mail` | `E-Mail` | 833 | review: merge |
| `e-mail` | `E-Mail` | 1,704 | review: merge |
| `eMail-Adresse` | `E-Mail-Adresse` | 529 | review: merge |
| `einfliessen` | `einfließen` | 311 | review: merge |
| `einigermassen` | `einigermaßen` | 554 | review: merge |
| `einladung` | `Einladung` | 1,395 | review: merge |
| `einschliesslich` | `einschließlich` | 920 | review: merge |
| `empfehlensweren` | `empfehlenswert` | 860 | review: merge |
| `entgegenstehend` | `entgegenstehen` | 528 | review: merge |
| `entlarv` | `entlarven` | 531 | review: merge |
| `entzündungshemmen` | `entzündungshemmend` | 937 | review: merge |
| `erfrag` | `erfragen` | 587 | review: merge |
| `fachgerechen` | `fachgerecht` | 587 | review: merge |
| `faulen` | `faul` | 559 | review: merge |
| `feuchen` | `feucht` | 623 | review: merge |
| `first` | `First` | 1,370 | review: merge |
| `fixen` | `fix` | 1,710 | review: merge |
| `flachen` | `flach` | 782 | review: merge |
| `fliesst` | `fließen` | 683 | review: merge |
| `folgendermaß` | `folgendermaßen` | 479 | review: merge |
| `fortwähren` | `fortwährend` | 564 | review: merge |
| `fr` | `für` | 18,036 | review: merge |
| `frisur` | `Frisur` | 656 | review: merge |
| `füreinand` | `füreinander` | 493 | review: merge |
| `generika` | `Generikum` | 1,380 | review: merge |
| `geniesst` | `genießen` | 750 | review: merge |
| `geschweig` | `geschweige` | 2,014 | review: merge |
| `gezahlt` | `zahlen` | 609 | review: merge |
| `giessen` | `gießen` | 391 | review: merge |
| `gleichberechtigen` | `gleichberechtigt` | 1,356 | review: merge |
| `gleichermassen` | `gleichermaßen` | 458 | review: merge |
| `grossem` | `groß` | 1,030 | review: merge |
| `großhandel` | `Großhandel` | 750 | review: merge |
| `handgefertigen` | `handgefertigt` | 1,637 | review: merge |
| `hiess` | `heißen` | 1,161 | review: merge |
| `hochauflösen` | `hochauflösend` | 926 | review: merge |
| `iMMER` | `immer` | 874 | review: merge |
| `initial` | `Initiale` | 495 | review: merge |
| `insid` | `Insider` | 646 | review: merge |
| `jed` | `jeder` | 2,051 | review: merge |
| `jedwed` | `jedweder` | 1,964 | review: merge |
| `karieren` | `kariert` | 781 | review: merge |
| `keinst` | `kein` | 886 | review: merge |
| `koennte` | `können` | 439 | review: merge |
| `kontrover` | `kontrovers` | 655 | review: merge |
| `krampfadern` | `Krampfader` | 498 | review: merge |
| `krausen` | `kraus` | 1,571 | review: merge |
| `köln` | `Köln` | 699 | review: merge |
| `küch` | `Küche` | 859 | review: merge |
| `langanhalten` | `langanhaltend` | 1,021 | review: merge |
| `level` | `Level` | 670 | review: merge |
| `lisen` | `List` | 622 | review: merge |
| `look` | `Look` | 619 | review: merge |
| `länderübergreifen` | `länderübergreifend` | 488 | review: merge |
| `menschenverachten` | `menschenverachtend` | 714 | review: merge |
| `most` | `Most` | 498 | review: merge |
| `multipl` | `multipel` | 575 | review: merge |
| `mutmasslich` | `mutmaßlich` | 400 | review: merge |
| `männ` | `Mann` | 2,032 | review: merge |
| `nchst` | `nächst` | 503 | review: merge |
| `nesen` | `genesen` | 728 | review: merge |
| `neuest` | `neu` | 2,162 | review: merge |
| `neust` | `neu` | 1,016 | review: merge |
| `nullen` | `null` | 509 | review: merge |
| `part` | `Part` | 956 | review: merge |
| `partn` | `Partner` | 688 | review: merge |
| `partnersuch` | `Partnersuche` | 2,557 | review: merge |
| `pdf-Datei` | `PDF-Datei` | 743 | review: merge |
| `pflegeleichen` | `pflegeleicht` | 1,783 | review: merge |
| `preisvergleich` | `Preisvergleich` | 1,002 | review: merge |
| `probi` | `probieren` | 551 | review: merge |
| `probl` | `Problem` | 1,032 | review: merge |
| `raffinieren` | `raffiniert` | 3,412 | review: merge |
| `rate` | `raten` | 623 | review: merge |
| `raum` | `Raum` | 13,047 | review: merge |
| `rechtssich` | `rechtssicher` | 533 | review: merge |
| `reichern` | `reich` | 672 | review: merge |
| `rückwärt` | `rückwärts` | 483 | review: merge |
| `sass` | `sitzen` | 503 | review: merge |
| `sauern` | `sauer` | 959 | review: merge |
| `schaltfläch` | `Schaltfläche` | 624 | review: merge |
| `schiesst` | `schießen` | 316 | review: merge |
| `schlafzimm` | `Schlafzimmer` | 1,536 | review: merge |
| `schliesslich` | `schließlich` | 1,235 | review: merge |
| `schnöd` | `schnöde` | 543 | review: merge |
| `schwanz` | `Schwanz` | 3,159 | review: merge |
| `see` | `See` | 1,133 | review: merge |
| `sehensweren` | `sehenswert` | 2,130 | review: merge |
| `selbstbestimmen` | `selbstbestimmt` | 1,077 | review: merge |
| `selbstbewus` | `selbstbewusst` | 526 | review: merge |
| `senkrechen` | `senkrecht` | 472 | review: merge |
| `serv` | `Server` | 710 | review: merge |
| `sex` | `Sex` | 13,382 | review: merge |
| `singl` | `Single` | 1,651 | review: merge |
| `softwar` | `Software` | 1,133 | review: merge |
| `somm` | `Sommer` | 810 | review: merge |
| `spielautomaen` | `Spielautomat` | 1,465 | review: merge |
| `stern` | `Stern` | 832 | review: merge |
| `stop` | `Stopp` | 546 | review: merge |
| `strengen` | `streng` | 587 | review: merge |
| `support` | `Support` | 726 | review: merge |
| `taste` | `Taste` | 480 | review: merge |
| `teilweis` | `teilweise` | 4,817 | review: merge |
| `tour` | `Tour` | 624 | review: merge |
| `tub` | `Tube` | 637 | review: merge |
| `umh` | `umher` | 1,567 | review: merge |
| `umliegen` | `umliegend` | 1,160 | review: merge |
| `umweltschonen` | `umweltschonend` | 1,569 | review: merge |
| `unberechtigen` | `unberechtigt` | 2,083 | review: merge |
| `unbewohnen` | `unbewohnt` | 535 | review: merge |
| `unbewus` | `unbewusst` | 468 | review: merge |
| `ungeheur` | `ungeheuer` | 982 | review: merge |
| `unterschätzend` | `unterschätzen` | 528 | review: merge |
| `vergünstig` | `vergünstigen` | 780 | review: merge |
| `verifiziern` | `verifizieren` | 539 | review: merge |
| `verschneien` | `verschneit` | 1,191 | review: merge |
| `vertuen` | `vertun` | 556 | review: merge |
| `verwinkeln` | `verwinkelt` | 711 | review: merge |
| `vielversprechen` | `vielversprechend` | 764 | review: merge |
| `wIE` | `wie` | 836 | review: merge |
| `waere` | `sein` | 302 | review: merge |
| `wandtattoo` | `Wandtattoo` | 1,040 | review: merge |
| `wasserabweisen` | `wasserabweisend` | 1,147 | review: merge |
| `weisse` | `weiß` | 763 | review: merge |
| `weiterentwickel` | `weiterentwickeln` | 585 | review: merge |
| `weiterles` | `weiterlesen` | 695 | review: merge |
| `weitermach` | `weitermachen` | 1,535 | review: merge |
| `who` | `WHO` | 1,141 | review: merge |
| `wohnung` | `Wohnung` | 3,296 | review: merge |
| `wohnungen` | `Wohnung` | 760 | review: merge |
| `wohnzimm` | `Wohnzimmer` | 744 | review: merge |
| `wüssen` | `wissen` | 745 | review: merge |
| `zielgerichten` | `zielgerichtet` | 2,512 | review: merge |
| `zukunftsweisen` | `zukunftsweisend` | 1,157 | review: merge |
| `zustehend` | `zustehen` | 1,278 | review: merge |
| `zweien` | `zwei` | 1,428 | review: merge |
| `Ändern` | `ändern` | 546 | review: merge |
| `Öle` | `Öl` | 567 | review: merge |
| `übereinan` | `übereinander` | 820 | review: merge |
| `übereinand` | `übereinander` | 703 | review: merge |
| `begrün` | `begrünen` | 461 | review: merge |
| `Hautreizunge` | `Hautreizung` | 460 | review: merge |
| `Reisebüros` | `Reisebüro` | 460 | review: merge |
| `Screenshots` | `Screenshot` | 460 | review: merge |
| `MANAGEMENT` | `Management` | 459 | review: merge |
| `SEITE` | `Seite` | 459 | review: merge |
| `Sozialangabe` | `Sozialabgabe` | 459 | review: merge |
| `Pigmentflecke` | `Pigmentfleck` | 458 | review: merge |
| `Päckch` | `Päckchen` | 458 | review: merge |
| `versteuernd` | `versteuern` | 458 | review: merge |
| `Jucke` | `jucken` | 457 | review: merge |
| `kontaktanzeig` | `Kontaktanzeige` | 457 | review: merge |
| `wochenen` | `Wochenende` | 457 | review: merge |
| `Arbeitsstätt` | `Arbeitsstätte` | 456 | review: merge |
| `Vorverkaufsstell` | `Vorverkaufsstelle` | 456 | review: merge |
| `ÖSTERREICH` | `Österreich` | 455 | review: merge |
| `Start-Ups` | `Start-Up` | 454 | review: merge |
| `eu` | `EU` | 454 | review: merge |
| `AntifaschistInn` | `Antifaschist` | 453 | review: merge |
| `COMPUTER` | `Computer` | 453 | review: merge |
| `Pünktch` | `Pünktchen` | 453 | review: merge |
| `Sekundarstuf` | `Sekundarstufe` | 452 | review: merge |
| `Clouds` | `Cloud` | 451 | review: merge |
| `e-Bikes` | `E-Bike` | 451 | review: merge |
| `Klug` | `klug` | 450 | review: merge |
| `Befestig` | `befestigen` | 449 | review: merge |
| `Freitagmorge` | `Freitagmorgen` | 449 | review: merge |
| `Helferinne` | `Helferin` | 449 | review: merge |
| `Nude` | `nude` | 449 | review: merge |
| `diplomieren` | `diplomiert` | 449 | review: merge |
| `siebent` | `siebte` | 449 | review: merge |
| `Kie` | `Kies` | 448 | review: merge |
| `Kinderbecke` | `Kinderbecken` | 448 | review: merge |
| `Basiswisse` | `Basiswissen` | 447 | review: merge |
| `Lehrkräfte` | `Lehrkraft` | 447 | review: merge |
| `MitarbeiterInnen` | `Mitarbeiter` | 446 | review: merge |
| `Einvernehm` | `Einvernehmen` | 445 | review: merge |
| `AktivistInnen` | `Aktivist` | 444 | review: merge |
| `Nickerche` | `Nickerchen` | 444 | review: merge |
| `Einleg` | `einlegen` | 441 | review: merge |
| `Heimtextilie` | `Heimtextilien` | 441 | review: merge |
| `RECHT` | `Recht` | 441 | review: merge |
| `Haarpfleg` | `Haarpflege` | 440 | review: merge |
| `Parodontiti` | `Parodontitis` | 440 | review: merge |
| `Schulferie` | `Schulferien` | 440 | review: merge |
| `Add-Ons` | `Add-On` | 439 | review: merge |
| `Erdnuß` | `Erdnuss` | 439 | review: merge |
| `nebenh` | `nebenher` | 439 | review: merge |
| `Exclusive` | `exklusiv` | 438 | review: merge |
| `Telefonate` | `Telefonat` | 437 | review: merge |
| `Überdie#Masc` | `überdies` | 435 | review: merge |
| `Anfahr` | `anfahren` | 434 | review: merge |
| `KundInnen` | `Kunde#Masc` | 434 | review: merge |
| `Vorbeug` | `vorbeugen` | 432 | review: merge |
| `Nierenversag` | `Nierenversagen` | 431 | review: merge |
| `Transportier` | `transportieren` | 431 | review: merge |
| `hannov` | `Hannover` | 430 | review: merge |
| `lebensretten` | `lebensrettend` | 430 | review: merge |
| `Fehlerbehebunge` | `Fehlerbehebung` | 429 | review: merge |
| `FRAGEN` | `Frage` | 428 | review: merge |
| `Hellsehe` | `Hellsehen` | 427 | review: merge |
| `START` | `Start` | 427 | review: merge |
| `Synchronisier` | `synchronisieren` | 427 | review: merge |
| `Tavern` | `Taverne` | 427 | review: merge |
| `selbstreden` | `selbstredend` | 426 | review: merge |
| `namenhaft` | `namhaft` | 425 | review: merge |
| `Überschreit` | `überschreiten` | 425 | review: merge |
| `Immobiliensuch` | `Immobiliensuche` | 424 | review: merge |
| `KINDER` | `Kind` | 424 | review: merge |
| `AutorInn` | `Autor` | 423 | review: merge |
| `herauskristallisi` | `herauskristallisieren` | 423 | review: merge |
| `Kaffeetrinke` | `Kaffeetrinken` | 422 | review: merge |
| `Memoir` | `Memoiren` | 422 | review: merge |
| `Töt` | `töten` | 422 | review: merge |
| `BUSINESS` | `Business` | 421 | review: merge |
| `Nutzungsdat` | `Nutzungsdaten` | 421 | review: merge |
| `Schuppenflecht` | `Schuppenflechte` | 421 | review: merge |
| `Eckdat` | `Eckdaten` | 420 | review: merge |
| `Älterwerde` | `Älterwerden` | 420 | review: merge |
| `Expertinn` | `Expertin` | 419 | review: merge |
| `Prüfungsfrag` | `Prüfungsfrage` | 419 | review: merge |
| `Tabellenzweit` | `Tabellenzweiter` | 419 | review: merge |
| `Würstche` | `Würstchen` | 419 | review: merge |
| `ZWEI` | `zwei` | 419 | review: merge |
| `ENDLICH` | `endlich` | 418 | review: merge |
| `Leitzin` | `Leitzins` | 418 | review: merge |
| `mind` | `mindestens` | 418 | review: merge |
| `MWST` | `Mehrwertsteuer` | 417 | review: merge |
| `Planschbecke` | `Planschbecken` | 417 | review: merge |
| `VertreterInn` | `Vertreter` | 416 | review: merge |
| `Weiters` | `weiters` | 416 | review: merge |
| `anzuwendend` | `anwenden` | 416 | review: merge |
| `büch` | `Buch` | 416 | review: merge |
| `Gefickt` | `ficken` | 415 | review: merge |
| `Scharf` | `scharf` | 415 | review: merge |
| `T-shirt` | `T-Shirt` | 415 | review: merge |
| `UNTERNEHMEN` | `Unternehmen` | 414 | review: merge |
| `Geschäftsstell` | `Geschäftsstelle` | 413 | review: merge |
| `benei` | `beneiden` | 413 | review: merge |
| `essbereich` | `Essbereich` | 413 | review: merge |
| `Aufsetz` | `aufsetzen` | 412 | review: merge |
| `Kundennutz` | `Kundennutzen` | 412 | review: merge |
| `Auschecke` | `auschecken` | 411 | review: merge |
| `Chill` | `chillen` | 411 | review: merge |
| `FREI` | `frei` | 411 | review: merge |
| `Kürbiskerne` | `Kürbiskern` | 411 | review: merge |
| `Unterstellunge` | `Unterstellung` | 411 | review: merge |
| `WIRKLICH` | `wirklich` | 411 | review: merge |
| `alia` | `alias` | 411 | review: merge |
| `Monatsrat` | `Monatsrate` | 410 | review: merge |
| `TUN` | `tun` | 410 | review: merge |
| `ExpertInn` | `Experte` | 409 | review: merge |
| `VIA` | `via` | 409 | review: merge |
| `Bilddat` | `Bilddaten` | 408 | review: merge |
| `CLUB` | `Club` | 408 | review: merge |
| `Gewerbeimmobilien` | `Gewerbeimmobilie` | 408 | review: merge |
| `Fortan` | `fortan` | 407 | review: merge |
| `Gesichtscrem` | `Gesichtscreme` | 407 | review: merge |
| `Satellite` | `Satellit` | 407 | review: merge |
| `KAUFEN` | `kaufen` | 403 | review: merge |
| `Must-have` | `Must-Have` | 403 | review: merge |
| `Web-Sit` | `Website` | 403 | review: merge |
| `Abmeld` | `abmelden` | 402 | review: merge |
| `Mazedonie` | `Mazedonien` | 402 | review: merge |
| `WOHNEN` | `wohnen` | 402 | review: merge |
| `Push-Benachrichtigungen` | `Push-Benachrichtigung` | 401 | review: merge |
| `Eislaufen` | `eislaufen` | 399 | review: merge |
| `AntifaschistInnen` | `Antifaschist` | 398 | review: merge |
| `Geodat` | `Geodaten` | 398 | review: merge |
| `Klickrat` | `Klickrate` | 398 | review: merge |
| `Spiegelunge` | `Spiegelung` | 398 | review: merge |
| `Standortdat` | `Standortdaten` | 398 | review: merge |
| `Pancakes` | `Pancake` | 397 | review: merge |
| `Pendelleucht` | `Pendelleuchte` | 397 | review: merge |
| `Brustwarz` | `Brustwarze` | 396 | review: merge |
| `portabl` | `portabel` | 396 | review: merge |
| `EFH` | `Einfamilienhaus` | 394 | review: merge |
| `IT-Services` | `IT-Service` | 394 | review: merge |
| `Frühschoppe` | `Frühschoppen` | 393 | review: merge |
| `Monitore` | `Monitor` | 389 | review: merge |
| `Rotkäppche` | `Rotkäppchen` | 389 | review: merge |
| `fü` | `für` | 389 | review: merge |
| `BAD` | `Bad` | 388 | review: merge |
| `DIGITAL` | `digital` | 388 | review: merge |
| `Kfz-Steuer#Neut` | `Kfz-Steuer` | 388 | review: merge |
| `Vorhofflimmer` | `Vorhofflimmern` | 388 | review: merge |
| `massag` | `Massage` | 388 | review: merge |
| `Diebstahls` | `Diebstahl` | 387 | review: merge |
| `Barbado` | `Barbados` | 386 | review: merge |
| `Malereie` | `Malerei` | 386 | review: merge |
| `Woraus` | `woraus` | 386 | review: merge |
| `Ziernäht` | `Ziernaht` | 386 | review: merge |
| `Drittländer` | `Drittland` | 385 | review: merge |
| `Prof` | `Professor` | 385 | review: merge |
| `Schweizerinn` | `Schweizerin` | 384 | review: merge |
| `Spielstätt` | `Spielstätte` | 383 | review: merge |
| `branchenübergreifen` | `branchenübergreifend` | 383 | review: merge |
| `vorgehalt` | `vorhalten` | 383 | review: merge |
| `Absterbe` | `Absterben` | 382 | review: merge |
| `Schneewittch` | `Schneewittchen` | 382 | review: merge |
| `ebendies` | `ebendieser` | 381 | review: merge |
| `zukunftssich` | `zukunftssicher` | 381 | review: merge |
| `Backlinks` | `Backlink` | 380 | review: merge |
| `Kügelche` | `Kügelchen` | 380 | review: merge |
| `Produzier` | `produzieren` | 380 | review: merge |
| `SPIEL` | `Spiel` | 380 | review: merge |
| `sternzeich` | `Sternzeichen` | 380 | review: merge |
| `Gliederschmerz` | `Gliederschmerzen` | 379 | review: merge |
| `Herausnehm` | `herausnehmen` | 379 | review: merge |
| `Smartwatche` | `Smartwatch` | 379 | review: merge |
| `Stickereie` | `Stickerei` | 379 | review: merge |
| `Exportier` | `exportieren` | 378 | review: merge |
| `Stichwörter` | `Stichwort` | 378 | review: merge |
| `Wdr` | `WDR` | 378 | review: merge |
| `Wunschdenke` | `Wunschdenken` | 378 | review: merge |
| `päckch` | `Päckchen` | 378 | review: merge |
| `Gesundheitsfrag` | `Gesundheitsfrage` | 377 | review: merge |
| `Installateure` | `Installateur` | 377 | review: merge |
| `nahend` | `nahen` | 377 | review: merge |
| `Produktdat` | `Produktdaten` | 376 | review: merge |
| `feuchtigkeitsspenden` | `feuchtigkeitsspendend` | 376 | review: merge |
| `KONTAKT` | `Kontakt` | 375 | review: merge |
| `Stallunge` | `Stallung` | 374 | review: merge |
| `Vergewisser` | `vergewissern` | 374 | review: merge |
| `Crews` | `Crew` | 373 | review: merge |
| `Mop` | `Mops` | 373 | review: merge |
| `Wasserbecke` | `Wasserbecken` | 373 | review: merge |
| `Eintret` | `eintreten` | 372 | review: merge |
| `Incentives` | `Incentive` | 372 | review: merge |
| `Langlebig` | `langlebig` | 372 | review: merge |
| `Mae` | `Maß` | 372 | review: merge |
| `Patientendat` | `Patientendaten` | 372 | review: merge |
| `Umwälzunge` | `Umwälzung` | 372 | review: merge |
| `Clans` | `Clan` | 371 | review: merge |
| `Mitsegel` | `mitsegeln` | 371 | review: merge |
| `unbewaffnen` | `unbewaffnet` | 371 | review: merge |
| `Übertragungsrat` | `Übertragungsrate` | 371 | review: merge |
| `nachleg` | `nachlegen` | 370 | review: merge |
| `nachreden` | `Nachrede` | 370 | review: merge |
| `Aerosole` | `Aerosol` | 369 | review: merge |
| `Rundgäng` | `Rundgang` | 369 | review: merge |
| `timelin` | `Timeline` | 369 | review: merge |
| `Bällche` | `Bällchen` | 368 | review: merge |
| `Online-Casinos` | `Online-Casino` | 368 | review: merge |
| `Streitereie` | `Streiterei` | 367 | review: merge |
| `Zusatzstoffen` | `Zusatzstoff` | 367 | review: merge |
| `selbstsich` | `selbstsicher` | 367 | review: merge |
| `Dörfche` | `Dörfchen` | 366 | review: merge |
| `Lässig` | `lässig` | 366 | review: merge |
| `Staunäs` | `Staunässe` | 366 | review: merge |
| `EXTRA` | `extra` | 365 | review: merge |
| `Gründerinne` | `Gründerin` | 365 | review: merge |
| `Membrane` | `Membran` | 365 | review: merge |
| `Zistern` | `Zisterne` | 365 | review: merge |
| `senior` | `Senior` | 365 | review: merge |
| `Renovierungsarbeite` | `Renovierungsarbeit` | 363 | review: merge |
| `URTEIL` | `Urteil` | 363 | review: merge |
| `Bindegeweb` | `Bindegewebe` | 362 | review: merge |
| `Mitsing` | `mitsingen` | 362 | review: merge |
| `POLO` | `Polo` | 362 | review: merge |
| `Rückenlehn` | `Rückenlehne` | 362 | review: merge |
| `IMMOBILIEN` | `Immobilie` | 361 | review: merge |
| `Interfaces` | `Interface` | 361 | review: merge |
| `Shops` | `Shop` | 361 | review: merge |
| `BEACHTEN` | `beachten` | 360 | review: merge |
| `LAND` | `Land` | 360 | review: merge |
| `NIEMALS` | `niemals` | 360 | review: merge |
| `Selbstmontag` | `Selbstmontage` | 360 | review: merge |
| `Vorbring` | `vorbringen` | 360 | review: merge |
| `oberfläch` | `Oberfläche` | 360 | review: merge |
| `Kartenspiele` | `Kartenspiel` | 359 | review: merge |
| `Fundstell` | `Fundstelle` | 358 | review: merge |
| `See#Fem` | `See` | 358 | review: merge |
| `untergehend` | `untergehen` | 358 | review: merge |
| `Bettwanz` | `Bettwanze` | 357 | review: merge |
| `Logfiles` | `Logfile` | 357 | review: merge |
| `Professorinn` | `Professorin` | 357 | review: merge |
| `Fundamentaliste` | `Fundamentalist` | 356 | review: merge |
| `Weibch` | `Weibchen` | 356 | review: merge |
| `Würstch` | `Würstchen` | 356 | review: merge |
| `AUCH` | `auch` | 355 | review: merge |
| `Auskühl` | `auskühlen` | 355 | review: merge |
| `Bolschewiki` | `Bolschewik` | 355 | review: merge |
| `Küssche` | `Küsschen` | 355 | review: merge |
| `MAL` | `mal` | 355 | review: merge |
| `SHOP` | `Shop` | 355 | review: merge |
| `VOLKES` | `Volk` | 355 | review: merge |
| `schwierigst` | `schwierig` | 355 | review: merge |
| `Ballerinas` | `Ballerina` | 354 | review: merge |
| `Landschaftspfleg` | `Landschaftspflege` | 354 | review: merge |
| `NA` | `na` | 354 | review: merge |
| `Leitfäde` | `Leitfaden` | 353 | review: merge |
| `Rösche` | `Röschen` | 353 | review: merge |
| `AUFGABEN` | `Aufgabe` | 352 | review: merge |
| `Flavonoide` | `Flavonoid` | 352 | review: merge |
| `RICHTIG` | `richtig` | 352 | review: merge |
| `SPAM` | `Spam` | 352 | review: merge |
| `Erwachsenwerde` | `Erwachsenwerden` | 351 | review: merge |
| `Zusammensetzunge` | `Zusammensetzung` | 351 | review: merge |
| `DREI` | `drei` | 350 | review: merge |
| `Musikhör` | `Musikhören` | 350 | review: merge |
| `Abschlussarbeite` | `Abschlussarbeit` | 349 | review: merge |
| `Stadtverordnet` | `Stadtverordnete` | 349 | review: merge |
| `review` | `Review` | 349 | review: merge |
| `Alleinreisendim` | `alleinreisend` | 348 | review: merge |
| `brows` | `Browser` | 348 | review: merge |
| `Almose` | `Almosen` | 347 | review: merge |
| `nächsthoch` | `nächsthöher` | 347 | review: merge |
| `Geiles` | `geil` | 346 | review: merge |
| `gelenkschonen` | `gelenkschonend` | 346 | review: merge |
| `Ionen` | `Ion` | 345 | review: merge |
| `Inverkehrbring` | `Inverkehrbringen` | 343 | review: merge |
| `Limett` | `Limette` | 343 | review: merge |
| `ANWENDUNG` | `Anwendung` | 342 | review: merge |
| `Pantolett` | `Pantolette` | 342 | review: merge |
| `Spülbecke` | `Spülbecken` | 342 | review: merge |
| `Weichenstellunge` | `Weichenstellung` | 342 | review: merge |
| `ARBEIT` | `Arbeit` | 340 | review: merge |
| `Einatm` | `einatmen` | 340 | review: merge |
| `Gedankengäng` | `Gedankengang` | 340 | review: merge |
| `Heade` | `Header` | 340 | review: merge |
| `Informationssysteme` | `Informationssystem` | 340 | review: merge |
| `Master-Studiengänge` | `Master-Studiengang` | 340 | review: merge |
| `Beats` | `Beat` | 339 | review: merge |
| `DIREKT` | `direkt` | 339 | review: merge |
| `TOUR` | `Tour` | 339 | review: merge |
| `Trainerinne` | `Trainerin` | 339 | review: merge |
| `rigid` | `rigide` | 339 | review: merge |
| `Citronensäure` | `Zitronensäure` | 338 | review: merge |
| `Feuchtigkeitscrem` | `Feuchtigkeitscreme` | 338 | review: merge |
| `Soldatinn` | `Soldatin` | 338 | review: merge |
| `Verwechslunge` | `Verwechslung` | 338 | review: merge |
| `überdi` | `überdies` | 338 | review: merge |
| `BESCHREIBUNG` | `Beschreibung` | 337 | review: merge |
| `Barfuß` | `barfuß` | 337 | review: merge |
| `Brasil` | `Brasilien` | 337 | review: merge |
| `Kindertagesstätt` | `Kindertagesstätte` | 337 | review: merge |
| `Autoteile` | `Autoteil` | 336 | review: merge |
| `Internetanbiete` | `Internetanbieter` | 336 | review: merge |
| `Linear` | `linear` | 336 | review: merge |
| `Netzteile` | `Netzteil` | 336 | review: merge |
| `Produktempfehlunge` | `Produktempfehlung` | 336 | review: merge |
| `Ranze` | `Ranzen` | 336 | review: merge |
| `Referentinn` | `Referentin` | 336 | review: merge |
| `Russ` | `Ruß` | 336 | review: merge |
| `VISION` | `Vision` | 336 | review: merge |
| `Zimbabwe` | `Simbabwe` | 336 | review: merge |
| `ARENA` | `Arena` | 335 | review: merge |
| `BOX` | `Box` | 335 | review: merge |
| `HERZLICH` | `herzlich` | 335 | review: merge |
| `Kinderschmink` | `Kinderschminken` | 335 | review: merge |
| `Marktdat` | `Marktdaten` | 335 | review: merge |
| `Modular` | `modular` | 335 | review: merge |
| `maschin` | `Maschine` | 335 | review: merge |
| `Barmherzige` | `barmherzig` | 334 | review: merge |
| `Fahnd` | `Fahnder` | 334 | review: merge |
| `Fickt` | `ficken` | 334 | review: merge |
| `Hint` | `hinten` | 334 | review: merge |
| `Einkaufszentr` | `Einkaufszentrum` | 333 | review: merge |
| `unbeeindrucken` | `unbeeindruckt` | 333 | review: merge |
| `GEBRAUCHSINFORMATION` | `Gebrauchsinformation` | 332 | review: merge |
| `Notebooks` | `Notebook` | 332 | review: merge |
| `INTERNATIONAL` | `international` | 331 | review: merge |
| `Waschlappe` | `Waschlappen` | 331 | review: merge |
| `Entrümpelunge` | `Entrümpelung` | 330 | review: merge |
| `Sprachreisen` | `Sprachreise` | 814 | review: merge |
| `steifen` | `steif` | 814 | review: merge |
| `motor` | `Motor` | 813 | review: merge |
| `Lehne` | `lehnen` | 812 | review: merge |
| `cod` | `Code` | 812 | review: merge |
| `fliessen` | `fließen` | 810 | review: merge |
| `verzichte` | `verzichten` | 810 | review: merge |
| `Polier` | `polieren` | 809 | review: merge |
| `poker` | `Poker` | 809 | review: merge |
| `Enthalte` | `enthalten` | 807 | review: merge |
| `Erfassen` | `erfassen` | 807 | review: merge |
| `typ` | `Typ` | 807 | review: merge |
| `einvernehmen` | `Einvernehmen` | 805 | review: merge |
| `Trad` | `Trade` | 803 | review: merge |
| `erleuchtet` | `erleuchten` | 803 | review: merge |
| `gruppe` | `Gruppe` | 803 | review: merge |
| `fitt` | `fit` | 801 | review: merge |
| `eingebracht` | `einbringen` | 799 | review: merge |
| `Kreativ` | `kreativ` | 798 | review: merge |
| `bräuchten` | `brauchen` | 798 | review: merge |
| `dargeboten` | `darbieten` | 798 | review: merge |
| `holz` | `Holz` | 798 | review: merge |
| `gescannt` | `scannen` | 797 | review: merge |
| `moment` | `Moment` | 795 | review: merge |
| `user` | `User` | 794 | review: merge |
| `Artefakte` | `Artefakt` | 793 | review: merge |
| `Liquids` | `Liquid` | 793 | review: merge |
| `gesendet` | `senden` | 793 | review: merge |
| `Echte` | `echt` | 791 | review: merge |
| `lud` | `laden` | 790 | review: merge |
| `besprochen` | `besprechen` | 789 | review: merge |
| `Geschöpfe` | `Geschöpf` | 788 | review: merge |
| `Paarim` | `Paar` | 786 | review: merge |
| `Genial` | `genial` | 785 | review: merge |
| `Robust` | `robust` | 785 | review: merge |
| `orangen` | `orange` | 785 | review: merge |
| `Univers` | `Universum` | 783 | review: merge |
| `gebracht` | `bringen` | 783 | review: merge |
| `herausgenommen` | `herausnehmen` | 783 | review: merge |
| `solls` | `sollen` | 783 | review: merge |
| `sperma` | `Sperma` | 783 | review: merge |
| `ebook` | `E-Book` | 782 | review: merge |
| `Konfiguriere` | `konfigurieren` | 781 | review: merge |
| `Tierversuche` | `Tierversuch` | 781 | review: merge |
| `Zusammengefasst` | `zusammenfassen` | 781 | review: merge |
| `verstellbaren` | `verstellbar` | 781 | review: merge |
| `Okt` | `Oktober` | 780 | review: merge |
| `ausbalanciert` | `ausbalancieren` | 780 | review: merge |
| `mchte` | `mögen` | 779 | review: merge |
| `Organisieren` | `organisieren` | 778 | review: merge |
| `ernannt` | `ernennen` | 778 | review: merge |
| `Ausszeichnungssprache` | `Auszeichnungssprache` | 777 | review: merge |
| `druck` | `Druck` | 776 | review: merge |
| `rock` | `Rock` | 775 | review: merge |
| `dellen` | `Delle` | 774 | review: merge |
| `schaun` | `schauen` | 774 | review: merge |
| `erfasste` | `erfassen` | 773 | review: merge |
| `weiber` | `Weib` | 773 | review: merge |
| `Steig` | `steigen` | 772 | review: merge |
| `begrüsst` | `begrüßen` | 771 | review: merge |
| `äusser` | `äußere` | 771 | review: merge |
| `boden` | `Boden` | 769 | review: merge |
| `Einschreibe` | `Einschreiben` | 768 | review: merge |
| `Glücklicherweise` | `glücklicherweise` | 768 | review: merge |
| `nummeriert` | `nummerieren` | 768 | review: merge |
| `weihnachten` | `Weihnachten` | 768 | review: merge |
| `Rundum` | `rundum` | 766 | review: merge |
| `schn` | `schön` | 766 | review: merge |
| `irgendw` | `irgendwer` | 765 | review: merge |
| `Bademäntel` | `Bademantel` | 705 | review: merge |
| `gedanken` | `Gedanke` | 764 | review: merge |
| `gehörend` | `gehören` | 764 | review: merge |
| `Pur` | `pur` | 763 | review: merge |
| `drück` | `drücken` | 763 | review: merge |
| `gutschein` | `Gutschein` | 763 | review: merge |
| `lsst` | `lassen` | 763 | review: merge |
| `adaptiert` | `adaptieren` | 762 | review: merge |
| `funktion` | `Funktion` | 761 | review: merge |
| `öffnend` | `öffnen` | 761 | review: merge |
| `Fünfter` | `fünfte` | 759 | review: merge |
| `regierend` | `regieren` | 759 | review: merge |
| `umgangen` | `umgehen` | 759 | review: merge |
| `umschlossen` | `umschließen` | 759 | review: merge |
| `exclusiv` | `exklusiv` | 758 | review: merge |
| `schul` | `Schule` | 758 | review: merge |
| `erwartend` | `erwarten` | 757 | review: merge |
| `stielen` | `Stiel` | 756 | review: merge |
| `Polar` | `polar` | 753 | review: merge |
| `Komisch` | `komisch` | 752 | review: merge |
| `anläßlich` | `anlässlich` | 752 | review: merge |
| `tiefst` | `tief` | 752 | review: merge |
| `Hausbesuche` | `Hausbesuch` | 750 | review: merge |
| `Musste` | `müssen` | 750 | review: merge |
| `Nee` | `nee` | 750 | review: merge |
| `recherchiert` | `recherchieren` | 749 | review: merge |
| `Sehenswert` | `sehenswert` | 748 | review: merge |
| `Wissenschaftliche` | `wissenschaftlich` | 748 | review: merge |
| `Mint` | `mint` | 747 | review: merge |
| `kämpfe` | `kämpfen` | 747 | review: merge |
| `mitversichert` | `mitversichern` | 746 | review: merge |
| `rat` | `Rat` | 746 | review: merge |
| `seiten` | `Seite` | 746 | review: merge |
| `Insoweit` | `insoweit` | 745 | review: merge |
| `Eingreifen` | `eingreifen` | 744 | review: merge |
| `Fränkische` | `fränkisch` | 744 | review: merge |
| `wirkung` | `Wirkung` | 744 | review: merge |
| `Übernacht` | `übernachten` | 740 | review: merge |
| `hund` | `Hund` | 739 | review: merge |
| `Angenehm` | `angenehm` | 737 | review: merge |
| `Bzw` | `beziehungsweise` | 737 | review: merge |
| `arzt` | `Arzt` | 736 | review: merge |
| `bitcoin` | `Bitcoin` | 736 | review: merge |
| `liste` | `Liste` | 736 | review: merge |
| `programm` | `Programm` | 736 | review: merge |
| `schlappen` | `Schlappe` | 735 | review: merge |
| `KollegIn` | `Kollegin` | 734 | review: merge |
| `beauftragt` | `Beauftragte` | 734 | review: merge |
| `famili` | `Familie` | 733 | review: merge |
| `orgasmus` | `Orgasmus` | 733 | review: merge |
| `Zertifizierte` | `zertifiziert` | 732 | review: merge |
| `Ausziehe` | `ausziehen` | 731 | review: merge |
| `fan` | `Fan` | 731 | review: merge |
| `feien` | `gefeit` | 730 | review: merge |
| `mchten` | `möchten` | 729 | review: merge |
| `Beende` | `beenden` | 728 | review: merge |
| `inkl` | `inklusive` | 728 | review: merge |
| `verfügung` | `Verfügung` | 727 | review: merge |
| `wrde` | `würde` | 727 | review: merge |
| `Weihnacht` | `Weihnachten` | 726 | review: merge |
| `ham` | `haben` | 726 | review: merge |
| `lösung` | `Lösung` | 726 | review: merge |
| `Gurk` | `Gurke` | 725 | review: merge |
| `kontakte` | `Kontakt` | 723 | review: merge |
| `gedreht` | `drehen` | 722 | review: merge |
| `Entladen` | `entladen` | 721 | review: merge |
| `kryptowährungen` | `Kryptowährung` | 720 | review: merge |
| `schiessen` | `schießen` | 720 | review: merge |
| `neuste` | `neu` | 719 | review: merge |
| `sond` | `sonder` | 719 | review: merge |
| `tablette` | `Tablette` | 719 | review: merge |
| `umschließt` | `umschließen` | 673 | review: merge |
| `Riß` | `Riss` | 718 | review: merge |
| `bestickt` | `besticken` | 718 | review: merge |
| `bissel` | `bisschen` | 718 | review: merge |
| `glas` | `Glas` | 718 | review: merge |
| `hinzugekommen` | `hinzukommen` | 718 | review: merge |
| `schoen` | `schön` | 718 | review: merge |
| `Zöger` | `zögern` | 717 | review: merge |
| `einsatz` | `Einsatz` | 717 | review: merge |
| `Birk` | `Birke` | 716 | review: merge |
| `Nachfahr` | `Nachfahre` | 716 | review: merge |
| `darber` | `darüber` | 716 | review: merge |
| `dildo` | `Dildo` | 715 | review: merge |
| `gechipt` | `chippen` | 715 | review: merge |
| `vermindert` | `vermindern` | 715 | review: merge |
| `iPads` | `iPad` | 713 | review: merge |
| `Österreichischer` | `österreichisch` | 713 | review: merge |
| `deko` | `Deko` | 712 | review: merge |
| `Treu` | `treu` | 711 | review: merge |
| `ausgeübt` | `ausüben` | 711 | review: merge |
| `infiziert` | `infizieren` | 711 | review: merge |
| `magazin` | `Magazin` | 711 | review: merge |
| `verstrickt` | `verstricken` | 711 | review: merge |
| `Kelt` | `Kelte` | 710 | review: merge |
| `solang` | `solange` | 710 | review: merge |
| `gewaschen` | `waschen` | 709 | review: merge |
| `Prüfe` | `prüfen` | 708 | review: merge |
| `abgelehnt` | `ablehnen` | 708 | review: merge |
| `aktualisiert` | `aktualisieren` | 707 | review: merge |
| `gelangt` | `gelangen` | 707 | review: merge |
| `revidiert` | `revidieren` | 707 | review: merge |
| `gepresst` | `pressen` | 706 | review: merge |
| `tasch` | `Tasche` | 706 | review: merge |
| `eingeschaltet` | `einschalten` | 704 | review: merge |
| `getreten` | `treten` | 704 | review: merge |
| `Grübel` | `grübeln` | 702 | review: merge |
| `Zapfe` | `Zapfen` | 702 | review: merge |
| `Biet` | `bieten` | 701 | review: merge |
| `blowjob` | `Blowjob` | 700 | review: merge |
| `gewicht` | `Gewicht` | 700 | review: merge |
| `stehn` | `stehen` | 700 | review: merge |
| `Phantasien` | `Phantasie` | 698 | review: merge |
| `geschicht` | `Geschichte` | 698 | review: merge |
| `gewiß` | `gewiss` | 698 | review: merge |
| `verlobt` | `Verlobte` | 698 | review: merge |
| `Lik` | `Like` | 697 | review: merge |
| `beworben` | `bewerben` | 696 | review: merge |
| `option` | `Option` | 696 | review: merge |
| `unsern` | `unser` | 696 | review: merge |
| `versch` | `verschieden` | 696 | review: merge |
| `Heb` | `heben` | 695 | review: merge |
| `content` | `Content` | 695 | review: merge |
| `zustzlich` | `zusätzlich` | 695 | review: merge |
| `kreuz` | `Kreuz` | 694 | review: merge |
| `exponieren` | `exponiert` | 693 | review: merge |
| `gleichmässig` | `gleichmäßig` | 693 | review: merge |
| `verregnen` | `verregnet` | 693 | review: merge |
| `HABEN` | `haben` | 692 | review: merge |
| `geschildert` | `schildern` | 692 | review: merge |
| `läd` | `laden` | 424 | review: merge |
| `weils` | `weil` | 691 | review: merge |
| `Füttern` | `füttern` | 690 | review: merge |
| `Charakteristisch` | `charakteristisch` | 689 | review: merge |
| `Energetische` | `energetisch` | 689 | review: merge |
| `optionen` | `Option` | 689 | review: merge |
| `sohn` | `Sohn` | 689 | review: merge |
| `unserm` | `unser` | 689 | review: merge |
| `profil` | `Profil` | 688 | review: merge |
| `öden` | `öde` | 688 | review: merge |
| `Drohn` | `Drohne` | 687 | review: merge |
| `Nö` | `nö` | 687 | review: merge |
| `aufgeladen` | `aufladen` | 687 | review: merge |
| `beleuchtet` | `beleuchten` | 687 | review: merge |
| `stein` | `Stein` | 685 | review: merge |
| `wiedermal` | `wieder` | 685 | review: merge |
| `Mitunter` | `mitunter` | 684 | review: merge |
| `Tück` | `Tücke` | 622 | review: merge |
| `beziehung` | `Beziehung` | 684 | review: merge |
| `Badische` | `badisch` | 683 | review: merge |
| `Grossteil` | `Großteil` | 683 | review: merge |
| `siehts` | `aussehen` | 682 | review: merge |
| `ausgegeben` | `ausgeben` | 681 | review: merge |
| `Eur` | `Euro` | 680 | review: merge |
| `Herrlich` | `herrlich` | 680 | review: merge |
| `Kasern` | `Kaserne` | 679 | review: merge |
| `Nirgendwo` | `nirgendwo` | 679 | review: merge |
| `modell` | `Modell` | 679 | review: merge |
| `talentierte` | `talentiert` | 679 | review: merge |
| `besuch` | `Besuch` | 677 | review: merge |
| `bevollmächtigt` | `Bevollmächtigte` | 677 | review: merge |
| `eingeleitet` | `einleiten` | 677 | review: merge |
| `geblockt` | `blocken` | 676 | review: merge |
| `geäußert` | `äußern` | 676 | review: merge |
| `massgeblich` | `maßgeblich` | 676 | review: merge |
| `unterlagen` | `Unterlage` | 676 | review: merge |
| `Permanent` | `permanent` | 675 | review: merge |
| `Anonym` | `anonym` | 674 | review: merge |
| `kredit` | `Kredit` | 674 | review: merge |
| `gekommen` | `kommen` | 673 | review: merge |
| `Cafe` | `Café` | 671 | review: merge |
| `Veröffentlich` | `veröffentlichen` | 670 | review: merge |
| `gesandt` | `Gesandter` | 670 | review: merge |
| `neuestem` | `neu` | 670 | review: merge |
| `udn` | `und` | 670 | review: merge |
| `Schnarche` | `schnarchen` | 668 | review: merge |
| `Überleg` | `überlegen` | 668 | review: merge |
| `Dez` | `Dezember` | 667 | review: merge |
| `vorteil` | `Vorteil` | 667 | review: merge |
| `zukunft` | `Zukunft` | 667 | review: merge |
| `Haha` | `haha` | 666 | review: merge |
| `werte` | `werten` | 666 | review: merge |
| `Cach` | `Cache` | 664 | review: merge |
| `fisch` | `Fisch` | 663 | review: merge |
| `name` | `Name` | 663 | review: merge |
| `unsr` | `unser` | 663 | review: merge |
| `Schreibe` | `Schreiben` | 662 | review: merge |
| `Apr` | `April` | 661 | review: merge |
| `Kalt` | `kalt` | 661 | review: merge |
| `Schwanger` | `schwanger` | 661 | review: merge |
| `webcam` | `Webcam` | 661 | review: merge |
| `Charakteristika` | `Charakteristikum` | 660 | review: merge |
| `Erneuerbare` | `erneuerbar` | 660 | review: merge |
| `guck` | `gucken` | 660 | review: merge |
| `freizuschalten` | `freischalten` | 659 | review: merge |
| `Appartment` | `Apartment` | 657 | review: merge |
| `stoff` | `Stoff` | 657 | review: merge |
| `Telefonisch` | `telefonisch` | 655 | review: merge |
| `einflussreichsten` | `einflussreich` | 655 | review: merge |
| `hän` | `Hand` | 655 | review: merge |
| `scheiss` | `Scheiß` | 655 | review: merge |
| `spielzeug` | `Spielzeug` | 655 | review: merge |
| `Golfe` | `golfen` | 654 | review: merge |
| `geilst` | `geil` | 654 | review: merge |
| `sooooo` | `so` | 654 | review: merge |
| `Auslese` | `auslesen` | 653 | review: merge |
| `Längst` | `längst` | 653 | review: merge |
| `Reflektion` | `Reflexion` | 653 | review: merge |
| `hochgeladen` | `hochladen` | 653 | review: merge |
| `veröffentlich` | `veröffentlichen` | 653 | review: merge |
| `zuwenig` | `wenig` | 652 | review: merge |
| `begriff` | `begreifen` | 651 | review: merge |
| `datei` | `Datei` | 650 | review: merge |
| `gearbeitet` | `arbeiten` | 650 | review: merge |
| `umfasst` | `umfassen` | 650 | review: merge |
| `Abhängig` | `abhängig` | 649 | review: merge |
| `Günstig` | `günstig` | 649 | review: merge |
| `Verbinde` | `verbinden` | 649 | review: merge |
| `anonymisierte` | `anonymisieren` | 648 | review: merge |
| `feinschleifen` | `Feinschliff` | 648 | review: merge |
| `Zitier` | `zitieren` | 647 | review: merge |
| `erkrankt` | `erkranken` | 647 | review: merge |
| `herangeführt` | `heranführen` | 647 | review: merge |
| `skaliert` | `skalieren` | 647 | review: merge |
| `Versende` | `versenden` | 646 | review: merge |
| `installiert` | `installieren` | 646 | review: merge |
| `nachlässt` | `nachlassen` | 646 | review: merge |
| `energie` | `Energie` | 645 | review: merge |
| `liebenswerte` | `liebenswert` | 645 | review: merge |
| `hatt` | `haben` | 644 | review: merge |
| `hinzugefügt` | `hinzufügen` | 644 | review: merge |
| `Teilnehmen` | `teilnehmen` | 643 | review: merge |
| `großgeschrieben` | `großschreiben` | 643 | review: merge |
| `beug` | `beugen` | 640 | review: merge |
| `geschmolzen` | `schmelzen` | 640 | review: merge |
| `machts` | `machen` | 639 | review: merge |
| `stil` | `Stil` | 639 | review: merge |
| `telefon` | `Telefon` | 638 | review: merge |
| `erster` | `erstere` | 637 | review: merge |
| `geparkt` | `parken` | 637 | review: merge |
| `versicherung` | `Versicherung` | 637 | review: merge |
| `vertrieben` | `vertreiben` | 637 | review: merge |
| `zerbrochen` | `zerbrechen` | 637 | review: merge |
| `Traurig` | `traurig` | 635 | review: merge |
| `reinigend` | `reinigen` | 635 | review: merge |
| `Zurücksetze` | `zurücksetzen` | 634 | review: merge |
| `Gastro` | `Gastronomie` | 633 | review: merge |
| `Spielmodi` | `Spielmodus` | 633 | review: merge |
| `dezente` | `dezent` | 633 | review: merge |
| `groe` | `groß` | 632 | review: merge |
| `Eiserne` | `eisern` | 631 | review: merge |
| `dreh` | `drehen` | 631 | review: merge |
| `gepflastert` | `pflastern` | 631 | review: merge |
| `kommentar` | `Kommentar` | 631 | review: merge |
| `login` | `Login` | 631 | review: merge |
| `subventioniert` | `subventionieren` | 631 | review: merge |
| `soetwas` | `so etwas` | 630 | review: merge |
| `ZUKUNFT` | `Zukunft` | 629 | review: merge |
| `erzähl` | `erzählen` | 629 | review: merge |
| `passten` | `passen` | 629 | review: merge |
| `twitterte` | `twittern` | 629 | review: merge |
| `Haselnuß` | `Haselnuss` | 628 | review: merge |
| `Optionale` | `optional` | 628 | review: merge |
| `beschenkt` | `Beschenkte` | 628 | review: merge |
| `Deaktivier` | `deaktivieren` | 627 | review: merge |
| `duch` | `durch` | 627 | review: merge |
| `nenn` | `nennen` | 627 | review: merge |
| `stillgelegt` | `stilllegen` | 627 | review: merge |
| `vll` | `vielleicht` | 627 | review: merge |
| `überdeckt` | `überdecken` | 627 | review: merge |
| `anleitung` | `Anleitung` | 626 | review: merge |
| `funzt` | `funzen` | 626 | review: merge |
| `abgestellt` | `abstellen` | 625 | review: merge |
| `aufgetreten` | `auftreten` | 625 | review: merge |
| `fenster` | `Fenster` | 625 | review: merge |
| `gesteckt` | `stecken` | 625 | review: merge |
| `tür` | `Tür` | 625 | review: merge |
| `ändernd` | `ändern` | 625 | review: merge |
| `einzigen` | `einzig` | 624 | review: merge |
| `Hinsehe` | `hinsehen` | 623 | review: merge |
| `Systemische` | `systemisch` | 623 | review: merge |
| `scho` | `schon` | 623 | review: merge |
| `knnt` | `können` | 622 | review: merge |
| `öfteren` | `öfter` | 622 | review: merge |
| `Entdecke` | `entdecken` | 621 | review: merge |
| `gekürzt` | `kürzen` | 621 | review: merge |
| `geschwächt` | `schwächen` | 621 | review: merge |
| `Achso` | `ach` | 620 | review: merge |
| `Aff` | `Affe` | 620 | review: merge |
| `account` | `Account` | 620 | review: merge |
| `kan` | `können` | 620 | review: merge |
| `schutz` | `Schutz` | 620 | review: merge |
| `Sonnenlieg` | `Sonnenliege` | 618 | review: merge |
| `eidg` | `eidgenössisch` | 618 | review: merge |
| `Volle` | `voll` | 617 | review: merge |
| `Vorzugsweise` | `vorzugsweise` | 617 | review: merge |
| `Wahre` | `wahr` | 617 | review: merge |
| `entwicklung` | `Entwicklung` | 616 | review: merge |
| `expertinnen` | `Expertin` | 616 | review: merge |
| `kund` | `Kunde` | 616 | review: merge |
| `Minis` | `Mini` | 615 | review: merge |
| `angeboten` | `anbieten` | 615 | review: merge |
| `wahl` | `Wahl` | 615 | review: merge |
| `Flugreisen` | `Flugreise` | 614 | review: merge |
| `Kompetent` | `kompetent` | 614 | review: merge |
| `Reif` | `reif` | 614 | review: merge |
| `gewinn` | `Gewinn` | 614 | review: merge |
| `herren` | `Herr` | 614 | review: merge |
| `Alt` | `alt` | 612 | review: merge |
| `casinos` | `Casino` | 612 | review: merge |
| `garnichts` | `nichts` | 612 | review: merge |
| `unkomplizierte` | `unkompliziert` | 612 | review: merge |
| `show` | `Show` | 611 | review: merge |
| `verschoben` | `verschieben` | 610 | review: merge |
| `Spielerisch` | `spielerisch` | 609 | review: merge |
| `ausdauern` | `ausdauernd` | 609 | review: merge |
| `hinzugezogen` | `hinzuziehen` | 609 | review: merge |
| `mama` | `Mama` | 609 | review: merge |
| `lt` | `laut` | 608 | review: merge |
| `mbh` | `GmbH` | 608 | review: merge |
| `möglichkeiten` | `Möglichkeit` | 608 | review: merge |
| `webbasierte` | `webbasiert` | 608 | review: merge |
| `episode` | `Episode` | 607 | review: merge |
| `monaten` | `Monat` | 607 | review: merge |
| `stillschweigen` | `stillschweigend` | 607 | review: merge |
| `Traumata` | `Trauma` | 606 | review: merge |
| `eingeschlagen` | `einschlagen` | 606 | review: merge |
| `filter` | `Filter` | 606 | review: merge |
| `verbindung` | `Verbindung` | 606 | review: merge |
| `Verfgung` | `Verfügung` | 605 | review: merge |
| `Kompressionsstrümpfe` | `Kompressionsstrumpf` | 604 | review: merge |
| `Rollos` | `Rollo` | 604 | review: merge |
| `Untere` | `unter` | 604 | review: merge |
| `souveräne` | `souverän` | 604 | review: merge |
| `story` | `Story` | 603 | review: merge |
| `zutun` | `tun` | 603 | review: merge |
| `Prüf` | `prüfen` | 602 | review: merge |
| `erlitten` | `erleiden` | 602 | review: merge |
| `sau` | `Sau` | 602 | review: merge |
| `Kombiniere` | `kombinieren` | 601 | review: merge |
| `Diakonische` | `diakonisch` | 600 | review: merge |
| `Verschenken` | `verschenken` | 600 | review: merge |
| `Rogg` | `Roggen` | 599 | review: merge |
| `tiefe` | `tief` | 599 | review: merge |
| `Mnner` | `Mann` | 598 | review: merge |
| `beispielweise` | `beispielsweise` | 598 | review: merge |
| `ausgerüstet` | `ausrüsten` | 597 | review: merge |
| `training` | `Training` | 597 | review: merge |
| `willigen` | `willig` | 597 | review: merge |
| `obs` | `ob` | 596 | review: merge |
| `radio` | `Radio` | 596 | review: merge |
| `Gend` | `Gender` | 595 | review: merge |
| `Reparier` | `reparieren` | 594 | review: merge |
| `Stärkere` | `stark` | 594 | review: merge |
| `ag` | `AG` | 594 | review: merge |
| `Retrospektiv` | `Retrospektive` | 593 | review: merge |
| `lesben` | `Lesbe` | 593 | review: merge |
| `vorgesetzt` | `Vorgesetzter` | 593 | review: merge |
| `Aussenbereich` | `Außenbereich` | 592 | review: merge |
| `flächendecken` | `flächendeckend` | 592 | review: merge |
| `umgebung` | `Umgebung` | 592 | review: merge |
| `vorlagen` | `Vorlage` | 592 | review: merge |
| `getränkt` | `tränken` | 591 | review: merge |
| `weile` | `Weile` | 590 | review: merge |
| `event` | `Event` | 589 | review: merge |
| `grüß` | `grüßen` | 589 | review: merge |
| `kleidung` | `Kleidung` | 589 | review: merge |
| `Gewächse` | `Gewächs` | 588 | review: merge |
| `Häkel` | `häkeln` | 588 | review: merge |
| `Schenke` | `schenken` | 588 | review: merge |
| `Zuständig` | `zuständig` | 588 | review: merge |
| `geglaubt` | `glauben` | 588 | review: merge |
| `Müsste` | `müssen` | 587 | review: merge |
| `eingespeist` | `einspeisen` | 587 | review: merge |
| `versand` | `Versand` | 587 | review: merge |
| `Aussteig` | `aussteigen` | 586 | review: merge |
| `herausgefordert` | `herausfordern` | 586 | review: merge |
| `selbstfahren` | `selbstfahrend` | 586 | review: merge |
| `anwendung` | `Anwendung` | 585 | review: merge |
| `lieferung` | `Lieferung` | 585 | review: merge |
| `ring` | `Ring` | 585 | review: merge |
| `tagesaktuellen` | `tagesaktuell` | 585 | review: merge |
| `Trennen` | `trennen` | 584 | review: merge |
| `nummer` | `Nummer` | 584 | review: merge |
| `Profitier` | `profitieren` | 583 | review: merge |
| `gehend` | `gehen` | 583 | review: merge |
| `schluss` | `Schluss` | 583 | review: merge |
| `uraufgeführt` | `uraufführen` | 583 | review: merge |
| `Augenlider` | `Augenlid` | 582 | review: merge |
| `dazugehört` | `dazugehören` | 582 | review: merge |
| `Microfaser` | `Mikrofaser` | 581 | review: merge |
| `vergrössern` | `vergrößern` | 581 | review: merge |
| `vater` | `Vater` | 580 | review: merge |
| `Dips` | `Dip` | 579 | review: merge |
| `Oberhalb` | `oberhalb` | 579 | review: merge |
| `gebissen` | `beißen` | 579 | review: merge |
| `wetter` | `Wetter` | 579 | review: merge |
| `zusammengetan` | `zusammentun` | 578 | review: merge |
| `Netzwerkes` | `Netzwerk` | 577 | review: merge |
| `Quer` | `quer` | 577 | review: merge |
| `sicht` | `Sicht` | 577 | review: merge |
| `stumpfen` | `stumpf` | 577 | review: merge |
| `Kapitalerträge` | `Kapitalertrag` | 575 | review: merge |
| `Umschalte` | `umschalten` | 575 | review: merge |
| `edition` | `Edition` | 575 | review: merge |
| `Babie` | `Baby` | 574 | review: merge |
| `warscheinlich` | `wahrscheinlich` | 574 | review: merge |
| `wellen` | `Welle` | 574 | review: merge |
| `Geiler` | `geil` | 573 | review: merge |
| `auswahl` | `Auswahl` | 573 | review: merge |
| `Aufwärme` | `aufwärmen` | 572 | review: merge |
| `Mien` | `Miene` | 572 | review: merge |
| `augen` | `Auge` | 572 | review: merge |
| `Abstell` | `abstellen` | 571 | review: merge |
| `gestreamt` | `streamen` | 571 | review: merge |
| `infos` | `Info` | 571 | review: merge |
| `leder` | `Leder` | 571 | review: merge |
| `rechnung` | `Rechnung` | 571 | review: merge |
| `vermochte` | `vermögen` | 571 | review: merge |
| `Läuferinne` | `Läuferin` | 570 | review: merge |
| `beiseit` | `beiseite` | 570 | review: merge |
| `hammer` | `Hammer` | 569 | review: merge |
| `Gemeinsamen` | `gemeinsam` | 568 | review: merge |
| `Göttliche` | `göttlich` | 568 | review: merge |
| `Steche` | `stechen` | 568 | review: merge |
| `strand` | `Strand` | 567 | review: merge |
| `gesagt` | `sagen` | 566 | review: merge |
| `kreis` | `Kreis` | 566 | review: merge |
| `sonn` | `Sonne` | 566 | review: merge |
| `ansich` | `an sich` | 565 | review: merge |
| `Färbe` | `färben` | 564 | review: merge |
| `inclusiv` | `inklusive` | 564 | review: merge |
| `Ausse` | `außen` | 563 | review: merge |
| `kino` | `Kino` | 563 | review: merge |
| `mitarbeiter` | `Mitarbeiter` | 563 | review: merge |
| `rausgesucht` | `raussuchen` | 563 | review: merge |
| `Releas` | `Release` | 562 | review: merge |
| `Vorbereiten` | `vorbereiten` | 562 | review: merge |
| `ungesättigte` | `ungesättigt` | 562 | review: merge |
| `vorraus` | `voraus` | 562 | review: merge |
| `ausgestreckt` | `ausstrecken` | 561 | review: merge |
| `geförderte` | `fördern` | 561 | review: merge |
| `tier` | `Tier` | 561 | review: merge |
| `vollgepackt` | `vollpacken` | 561 | review: merge |
| `Baudenkmäler` | `Baudenkmal` | 560 | review: merge |
| `groen` | `groß` | 560 | review: merge |
| `informationen` | `Information` | 560 | review: merge |
| `pulen` | `Pult` | 560 | review: merge |
| `Jährige` | `jährig` | 559 | review: merge |
| `Styl` | `Style` | 559 | review: merge |
| `Vorweg` | `vorweg` | 559 | review: merge |
| `schlaf` | `Schlaf` | 559 | review: merge |
| `werbung` | `Werbung` | 559 | review: merge |
| `Wiederhole` | `wiederholen` | 558 | review: merge |
| `knnte` | `können` | 558 | review: merge |
| `Denkanstöße` | `Denkanstoß` | 557 | review: merge |
| `ermäßigungen` | `Ermäßigung` | 557 | review: merge |
| `getan` | `tun` | 557 | review: merge |
| `million` | `Million` | 557 | review: merge |
| `Fallstricke` | `Fallstrick` | 556 | review: merge |
| `Fuer` | `für` | 556 | review: merge |
| `Kommunale` | `kommunal` | 556 | review: merge |
| `Shar` | `Share` | 556 | review: merge |
| `gesehn` | `sehen` | 556 | review: merge |
| `Tenside` | `Tensid` | 555 | review: merge |
| `anvisiert` | `anvisieren` | 555 | review: merge |
| `karten` | `Karte` | 555 | review: merge |
| `sofa` | `Sofa` | 555 | review: merge |
| `umwickelt` | `umwickeln` | 555 | review: merge |
| `WO` | `wo` | 554 | review: merge |
| `finger` | `Finger` | 553 | review: merge |
| `treff` | `Treff` | 553 | review: merge |
| `Pedelecs` | `Pedelec` | 552 | review: merge |
| `gerufen` | `rufen` | 552 | review: merge |
| `vorbeizuschauen` | `vorbeischauen` | 552 | review: merge |
| `wasserdichte` | `wasserdicht` | 552 | review: merge |
| `automaten` | `Automat` | 551 | review: merge |
| `Energiespar` | `Energiesparen` | 550 | review: merge |
| `PARTNER` | `Partner` | 550 | review: merge |
| `eigendlich` | `eigentlich` | 550 | review: merge |
| `schule` | `Schule` | 550 | review: merge |
| `Reissverschluss` | `Reißverschluss` | 548 | review: merge |
| `pack` | `packen` | 548 | review: merge |
| `persnlich` | `persönlich` | 548 | review: merge |
| `rauh` | `rau` | 548 | review: merge |
| `zukunftsorientierte` | `zukunftsorientiert` | 548 | review: merge |
| `Radel` | `radeln` | 547 | review: merge |
| `bauch` | `Bauch` | 547 | review: merge |
| `bey` | `bei` | 547 | review: merge |
| `bloggt` | `bloggen` | 547 | review: merge |
| `bedienend` | `bedienen` | 546 | review: merge |
| `häßlich` | `hässlich` | 546 | review: merge |
| `Marg` | `Marge` | 545 | review: merge |
| `filme` | `Film` | 545 | review: merge |
| `fördernd` | `fördern` | 545 | review: merge |
| `hülsen` | `Hülse` | 545 | review: merge |
| `netz` | `Netz` | 545 | review: merge |
| `trauernd` | `trauern` | 544 | review: merge |
| `Dauerhaft` | `dauerhaft` | 543 | review: merge |
| `Reiben` | `reiben` | 543 | review: merge |
| `kunst` | `Kunst` | 543 | review: merge |
| `wiederentdeckt` | `wiederentdecken` | 543 | review: merge |
| `Anschließe` | `anschließen` | 542 | review: merge |
| `Treibe` | `treiben` | 542 | review: merge |
| `herstell` | `Hersteller` | 542 | review: merge |
| `stream` | `Stream` | 542 | review: merge |
| `Ruh` | `Ruhe` | 541 | review: merge |
| `Westdeutsche` | `westdeutsch` | 541 | review: merge |
| `berüchtigte` | `berüchtigt` | 541 | review: merge |
| `gewonnen` | `gewinnen` | 541 | review: merge |
| `Kau` | `kauen` | 540 | review: merge |
| `hos` | `Hose` | 540 | review: merge |
| `Manch` | `manch` | 539 | review: merge |
| `Ordn` | `ordnen` | 539 | review: merge |
| `Zitter` | `zittern` | 539 | review: merge |
| `hoff` | `hoffen` | 539 | review: merge |
| `setz` | `setzen` | 538 | review: merge |
| `Fahr` | `fahren` | 537 | review: merge |
| `Britische` | `britisch` | 536 | review: merge |
| `Elektrische` | `elektrisch` | 536 | review: merge |
| `Töten` | `töten` | 536 | review: merge |
| `grins` | `grinsen` | 536 | review: merge |
| `nichtmehr` | `nicht mehr` | 536 | review: merge |
| `beginn` | `Beginn` | 535 | review: merge |
| `spießen` | `Spieß` | 475 | review: merge |
| `computer` | `Computer` | 534 | review: merge |
| `Staatlich` | `staatlich` | 533 | review: merge |
| `Zweit` | `zweite` | 533 | review: merge |
| `akku` | `Akku` | 531 | review: merge |
| `sound` | `Sound` | 531 | review: merge |
| `Ki` | `KI` | 530 | review: merge |
| `Kleben` | `kleben` | 530 | review: merge |
| `angefallen` | `anfallen` | 530 | review: merge |
| `gefunden` | `finden` | 529 | review: merge |
| `Häsch` | `Häschen` | 448 | review: merge |
| `Vorraussetzung` | `Voraussetzung` | 528 | review: merge |
| `mark` | `Marke` | 528 | review: merge |
| `maus` | `Maus` | 528 | review: merge |
| `muessen` | `müssen` | 528 | review: merge |
| `Archiviert` | `archivieren` | 527 | review: merge |
| `ausgetragen` | `austragen` | 527 | review: merge |
| `freigegeben` | `freigeben` | 527 | review: merge |
| `versierte` | `versiert` | 527 | review: merge |
| `Herstell` | `herstellen` | 526 | review: merge |
| `seperat` | `separat` | 526 | review: merge |
| `Farbiger` | `farbig` | 525 | review: merge |
| `behandlung` | `Behandlung` | 525 | review: merge |
| `wechsel` | `wechseln` | 525 | review: merge |
| `dutzende` | `Dutzend` | 524 | review: merge |
| `handel` | `Handel` | 524 | review: merge |
| `nutz` | `nutzen` | 524 | review: merge |
| `wohlgefühlt` | `sich wohlfühlen` | 524 | review: merge |
| `zahl` | `Zahl` | 524 | review: merge |
| `zeug` | `Zeug` | 524 | review: merge |
| `ö` | `öde` | 524 | review: merge |
| `Biege` | `biegen` | 523 | review: merge |
| `Kuschel` | `kuscheln` | 523 | review: merge |
| `bewertung` | `Bewertung` | 523 | review: merge |
| `moeglich` | `möglich` | 523 | review: merge |
| `meter` | `Meter` | 522 | review: merge |
| `zurck` | `zurück` | 521 | review: merge |
| `Komfortabel` | `komfortabel` | 520 | review: merge |
| `situation` | `Situation` | 520 | review: merge |
| `Kopfschüttel` | `Kopfschütteln` | 519 | review: merge |
| `gestossen` | `stoßen` | 519 | review: merge |
| `wein` | `Wein` | 519 | review: merge |
| `Brauner` | `braun` | 518 | review: merge |
| `gemobbt` | `mobben` | 518 | review: merge |
| `lizenzfreie` | `lizenzfrei` | 518 | review: merge |
| `Ausgehe` | `ausgehen` | 517 | review: merge |
| `Kratze` | `kratzen` | 517 | review: merge |
| `eingeräumt` | `einräumen` | 517 | review: merge |
| `serie` | `Serie` | 517 | review: merge |
| `tglich` | `täglich` | 517 | review: merge |
| `Geheime` | `geheim` | 516 | review: merge |
| `Außerhalb` | `außerhalb` | 515 | review: merge |
| `Kung` | `Kung-Fu` | 515 | review: merge |
| `NAMEN` | `Name` | 515 | review: merge |
| `management` | `Management` | 515 | review: merge |
| `Übersetze` | `übersetzen` | 515 | review: merge |
| `Chalets` | `Chalet` | 514 | review: merge |
| `Schwing` | `schwingen` | 514 | review: merge |
| `crem` | `Creme` | 514 | review: merge |
| `erfassten` | `erfassen` | 514 | review: merge |
| `Jogge` | `joggen` | 513 | review: merge |
| `Sing` | `singen` | 513 | review: merge |
| `wasser` | `Wasser` | 513 | review: merge |
| `Blattläuse` | `Blattlaus` | 512 | review: merge |
| `Ernste` | `Ernst` | 512 | review: merge |
| `Poppe` | `poppen` | 512 | review: merge |
| `stech` | `stechen` | 512 | review: merge |
| `Auslösen` | `auslösen` | 511 | review: merge |
| `Fremdgehe` | `fremdgehen` | 511 | review: merge |
| `griech` | `griechisch` | 511 | review: merge |
| `aufwach` | `aufwachen` | 510 | review: merge |
| `freigeschalten` | `freischalten` | 510 | review: merge |
| `masse` | `Masse` | 510 | review: merge |
| `Verschleißteile` | `Verschleißteil` | 509 | review: merge |
| `fürn` | `für` | 509 | review: merge |
| `Einzelnachweise` | `Einzelnachweis` | 508 | review: merge |
| `baust` | `bauen` | 508 | review: merge |
| `bock` | `Bock` | 508 | review: merge |
| `lvl` | `Level` | 508 | review: merge |
| `pol` | `Pol` | 508 | review: merge |
| `titel` | `Titel` | 508 | review: merge |
| `Grob` | `grob` | 507 | review: merge |
| `Tot` | `tot` | 507 | review: merge |
| `Zuschneide` | `zuschneiden` | 507 | review: merge |
| `drfen` | `dürfen` | 507 | review: merge |
| `sek` | `Sekunde` | 507 | review: merge |
| `verströmt` | `verströmen` | 507 | review: merge |
| `Ausmass` | `Ausmaß` | 506 | review: merge |
| `lautsprecher` | `Lautsprecher` | 506 | review: merge |
| `wasserfällen` | `Wasserfall` | 506 | review: merge |
| `watt` | `Watt` | 506 | review: merge |
| `büro` | `Büro` | 505 | review: merge |
| `lied` | `Lied` | 505 | review: merge |
| `loch` | `Loch` | 505 | review: merge |
| `studierend` | `Studierende` | 505 | review: merge |
| `vormontiert` | `vormontieren` | 505 | review: merge |
| `Busreisen` | `Busreise` | 504 | review: merge |
| `Verbring` | `verbringen` | 504 | review: merge |
| `Vertikal` | `vertikal` | 504 | review: merge |
| `gelscht` | `löschen` | 504 | review: merge |
| `immense` | `immens` | 504 | review: merge |
| `position` | `Position` | 504 | review: merge |
| `reaktiviert` | `reaktivieren` | 504 | review: merge |
| `Veränder` | `verändern` | 503 | review: merge |
| `herausnehmbaren` | `herausnehmbar` | 503 | review: merge |
| `Problematisch` | `problematisch` | 502 | review: merge |
| `Rüsch` | `Rüsche` | 502 | review: merge |
| `einlässt` | `einlassen` | 502 | review: merge |
| `lag` | `Lager` | 502 | review: merge |
| `vlt` | `vielleicht` | 502 | review: merge |
| `Vielseitig` | `vielseitig` | 501 | review: merge |
| `ausm` | `aus` | 501 | review: merge |
| `bekanntschaften` | `Bekanntschaft` | 501 | review: merge |
| `nocheinmal` | `noch einmal` | 501 | review: merge |
| `rde` | `werden` | 501 | review: merge |
| `reihe` | `Reihe` | 501 | review: merge |
| `wre` | `sein` | 501 | review: merge |
| `apach` | `Apache` | 500 | review: merge |
| `Chemtrails` | `Chemtrail` | 499 | review: merge |
| `darüberhinaus` | `darüber hinaus` | 499 | review: merge |
| `dreien` | `drei` | 499 | review: merge |
| `muster` | `Muster` | 499 | review: merge |
| `Müde` | `müde` | 498 | review: merge |
| `wett` | `wettmachen` | 498 | review: merge |
| `kun` | `Kunde` | 497 | review: merge |
| `aufgefasst` | `auffassen` | 496 | review: merge |
| `bildend` | `bilden` | 496 | review: merge |
| `installation` | `Installation` | 496 | review: merge |
| `Gei` | `Geier` | 495 | review: merge |
| `Versandkostenfreie` | `versandkostenfrei` | 495 | review: merge |
| `Vierte` | `vierte` | 495 | review: merge |
| `dafuer` | `dafür` | 495 | review: merge |
| `durchdring` | `durchdringen` | 495 | review: merge |
| `überwacht` | `überwachen` | 495 | review: merge |
| `Unterstütze` | `unterstützen` | 494 | review: merge |
| `abgespeckt` | `abspecken` | 494 | review: merge |
| `beigelegt` | `beilegen` | 494 | review: merge |
| `erschlossen` | `erschließen` | 494 | review: merge |
| `träg` | `träge` | 494 | review: merge |
| `Gruppenreisen` | `Gruppenreise` | 493 | review: merge |
| `Sozial` | `sozial` | 493 | review: merge |
| `Unbewusst` | `unbewusst` | 493 | review: merge |
| `erstellt` | `erstellen` | 493 | review: merge |
| `reglementiert` | `reglementieren` | 493 | review: merge |
| `Erzeuge` | `erzeugen` | 492 | review: merge |
| `Lesen` | `lesen` | 492 | review: merge |
| `bewussten` | `bewusst` | 492 | review: merge |
| `freude` | `Freude` | 492 | review: merge |
| `twitter` | `twittern` | 492 | review: merge |
| `umringt` | `umringen` | 492 | review: merge |
| `überlegt` | `überlegen` | 492 | review: merge |
| `Dreißigjährige` | `dreißigjährig` | 491 | review: merge |
| `Toxine` | `Toxin` | 491 | review: merge |
| `jap` | `ja` | 491 | review: merge |
| `Freske` | `Fresko` | 490 | review: merge |
| `Sauge` | `saugen` | 490 | review: merge |
| `bezwungen` | `bezwingen` | 490 | review: merge |
| `flasch` | `Flasche` | 490 | review: merge |
| `geschlagen` | `schlagen` | 490 | review: merge |
| `hälfte` | `Hälfte` | 490 | review: merge |
| `regel` | `Regel` | 490 | review: merge |
| `Breit` | `breit` | 489 | review: merge |
| `Lernprozeß` | `Lernprozess` | 489 | review: merge |
| `Traditionelle` | `traditionell` | 489 | review: merge |
| `gegn` | `Gegner` | 489 | review: merge |
| `kalibriert` | `kalibrieren` | 489 | review: merge |
| `zunchst` | `zunächst` | 489 | review: merge |
| `getarnt` | `tarnen` | 488 | review: merge |
| `punkt` | `Punkt` | 488 | review: merge |
| `Kommende` | `kommend` | 487 | review: merge |
| `Scheiss` | `Scheiß` | 487 | review: merge |
| `gebastelt` | `basteln` | 487 | review: merge |
| `gemahl` | `mahlen` | 487 | review: merge |
| `arbeitend` | `arbeiten` | 486 | review: merge |
| `gegossen` | `gießen` | 486 | review: merge |
| `gespendet` | `spenden` | 486 | review: merge |
| `tochter` | `Tochter` | 486 | review: merge |
| `treiber` | `Treiber` | 486 | review: merge |
| `Benutzerdefinierte` | `benutzerdefiniert` | 485 | review: merge |
| `Hierin` | `hierin` | 485 | review: merge |
| `abgewandelt` | `abwandeln` | 485 | review: merge |
| `ausgesetzt` | `aussetzen` | 485 | review: merge |
| `dusch` | `Dusche` | 485 | review: merge |
| `ordnung` | `Ordnung` | 485 | review: merge |
| `eintretend` | `eintreten` | 484 | review: merge |
| `heikle` | `heikel` | 484 | review: merge |
| `tod` | `Tod` | 484 | review: merge |
| `waer` | `sein` | 484 | review: merge |
| `Exakt` | `exakt` | 483 | review: merge |
| `Wär` | `sein` | 483 | review: merge |
| `automatenspiele` | `Automatenspiel` | 483 | review: merge |
| `erteilt` | `erteilen` | 483 | review: merge |
| `gesundheitsfördern` | `gesundheitsfördernd` | 483 | review: merge |
| `Fetz` | `Fetzen` | 482 | review: merge |
| `Hobbies` | `Hobby` | 482 | review: merge |
| `apps` | `App` | 482 | review: merge |
| `essentiellen` | `essentiell` | 482 | review: merge |
| `meld` | `melden` | 482 | review: merge |
| `destilliert` | `destillieren` | 481 | review: merge |
| `kindern` | `Kind` | 481 | review: merge |
| `lehne` | `lehnen` | 481 | review: merge |
| `lichtdurchflutete` | `lichtdurchflutet` | 481 | review: merge |
| `fing` | `fangen` | 480 | review: merge |
| `grausame` | `grausam` | 480 | review: merge |
| `möbel` | `Möbel` | 480 | review: merge |
| `nachgebessert` | `nachbessern` | 480 | review: merge |
| `übermässig` | `übermäßig` | 480 | review: merge |
| `Anhebe` | `anheben` | 479 | review: merge |
| `Industrieller` | `industriell` | 479 | review: merge |
| `aktion` | `Aktion` | 479 | review: merge |
| `angeguckt` | `angucken` | 479 | review: merge |
| `familiengeführte` | `familiengeführt` | 479 | review: merge |
| `gelinkten` | `linken` | 479 | review: merge |
| `gestorben` | `sterben` | 479 | review: merge |
| `Metastasen` | `Metastase` | 478 | review: merge |
| `erreicht` | `erreichen` | 478 | review: merge |
| `kunststoff` | `Kunststoff` | 478 | review: merge |
| `politik` | `Politik` | 478 | review: merge |
| `sms` | `SMS` | 478 | review: merge |
| `Grosshandel` | `Großhandel` | 477 | review: merge |
| `Reig` | `Reigen` | 477 | review: merge |
| `code` | `Code` | 477 | review: merge |
| `nebenwirkungen` | `Nebenwirkung` | 477 | review: merge |
| `sympatisch` | `sympathisch` | 477 | review: merge |
| `validiert` | `validieren` | 477 | review: merge |
| `Orga` | `Organisation` | 476 | review: merge |
| `abgerieben` | `abreiben` | 476 | review: merge |
| `flauen` | `Flaute` | 475 | review: merge |
| `sportwetten` | `Sportwette` | 475 | review: merge |
| `gewissenhafte` | `gewissenhaft` | 474 | review: merge |
| `sodaß` | `sodass` | 474 | review: merge |
| `Gulde` | `Gulden` | 473 | review: merge |
| `Lehe` | `Lehen` | 473 | review: merge |
| `Spate` | `Spaten` | 473 | review: merge |
| `gelschte` | `löschen` | 473 | review: merge |
| `tricks` | `Trick` | 473 | review: merge |
| `Anhören` | `anhören` | 472 | review: merge |
| `Richt` | `richten` | 472 | review: merge |
| `Schicksalsschläge` | `Schicksalsschlag` | 472 | review: merge |
| `herausragender` | `herausragend` | 471 | review: merge |
| `Barrierefreie` | `barrierefrei` | 470 | review: merge |
| `Konservativer` | `Konservative` | 470 | review: merge |
| `Lupin` | `Lupine` | 470 | review: merge |
| `Stecklinge` | `Steckling` | 470 | review: merge |
| `Verschluß` | `Verschluss` | 470 | review: merge |
| `Dehne` | `dehnen` | 469 | review: merge |
| `Märkische` | `märkisch` | 469 | review: merge |
| `Pr` | `PR` | 469 | review: merge |
| `feinste` | `fein` | 469 | review: merge |
| `Einchecke` | `einchecken` | 468 | review: merge |
| `Schieb` | `schieben` | 468 | review: merge |
| `einstellung` | `Einstellung` | 468 | review: merge |
| `gaaanz` | `ganz` | 468 | review: merge |
| `getaggt` | `taggen` | 468 | review: merge |
| `kleinanzeigen` | `Kleinanzeige` | 468 | review: merge |
| `Cranberries` | `Cranberry` | 467 | review: merge |
| `Traumhaft` | `traumhaft` | 467 | review: merge |
| `Wörtche` | `Wörtchen` | 467 | review: merge |
| `sing` | `singen` | 467 | review: merge |
| `stösst` | `stoßen` | 467 | review: merge |
| `Stck` | `Stück` | 466 | review: merge |
| `detailiert` | `detailliert` | 465 | review: merge |
| `eich` | `Eiche` | 465 | review: merge |
| `erscheinend` | `erscheinen` | 465 | review: merge |
| `wiederholend` | `wiederholen` | 465 | review: merge |
| `zugeteilt` | `zuteilen` | 465 | review: merge |
| `Duale` | `dual` | 464 | review: merge |
| `Jage` | `jagen` | 464 | review: merge |
| `katze` | `Katze` | 464 | review: merge |
| `manag` | `Manager` | 464 | review: merge |
| `Integrierte` | `integriert` | 463 | review: merge |
| `Renovier` | `renovieren` | 463 | review: merge |
| `unterrichte` | `unterrichten` | 463 | review: merge |
| `verwendung` | `Verwendung` | 463 | review: merge |
| `Betätige` | `betätigen` | 462 | review: merge |
| `Blöd` | `blöd` | 462 | review: merge |
| `Weit` | `weit` | 462 | review: merge |
| `hintergrund` | `Hintergrund` | 462 | review: merge |
| `leuten` | `Leute` | 462 | review: merge |
| `sal` | `Sale` | 462 | review: merge |
| `whlen` | `wählen` | 462 | review: merge |
| `ersteinmal` | `erst einmal` | 461 | review: merge |
| `intakte` | `intakt` | 461 | review: merge |
| `trau` | `trauen` | 461 | review: merge |
| `Liegestütze` | `Liegestütz` | 460 | review: merge |
| `Ihrem` | `ihr` | 459 | review: merge |
| `model` | `Model` | 459 | review: merge |
| `Indigen` | `Indigene` | 458 | review: merge |
| `album` | `Album` | 458 | review: merge |
| `fetisch` | `Fetisch` | 458 | review: merge |
| `konstante` | `konstant` | 458 | review: merge |
| `projekt` | `Projekt` | 458 | review: merge |
| `moechte` | `möchte` | 457 | review: merge |
| `ebendiese` | `ebendieser` | 456 | review: merge |
| `verliehen` | `verleihen` | 456 | review: merge |
| `Deppe` | `Depp` | 455 | review: merge |
| `pediküren` | `Pediküre` | 455 | review: merge |
| `schwester` | `Schwester` | 455 | review: merge |
| `zeitgemäss` | `zeitgemäß` | 455 | review: merge |
| `Bolze` | `Bolzen` | 454 | review: merge |
| `Trese` | `Tresen` | 454 | review: merge |
| `eingeblendet` | `einblenden` | 454 | review: merge |
| `tourt` | `touren` | 454 | review: merge |
| `Niese` | `niesen` | 453 | review: merge |
| `gesellschaft` | `Gesellschaft` | 453 | review: merge |
| `handgefertigten` | `handgefertigt` | 453 | review: merge |
| `montag` | `Montag` | 453 | review: merge |
| `nachricht` | `Nachricht` | 453 | review: merge |
| `tantra` | `Tantra` | 453 | review: merge |
| `unterstützung` | `Unterstützung` | 453 | review: merge |
| `Mittendrin` | `mittendrin` | 452 | review: merge |
| `aufwarts` | `aufwärts` | 452 | review: merge |
| `brig` | `übrig` | 452 | review: merge |
| `nehmend` | `nehmen` | 452 | review: merge |
| `Beispielhaft` | `beispielhaft` | 451 | review: merge |
| `Pflegeleicht` | `pflegeleicht` | 451 | review: merge |
| `Presets` | `Preset` | 451 | review: merge |
| `WISSEN` | `wissen` | 451 | review: merge |
| `ausbildung` | `Ausbildung` | 451 | review: merge |
| `Rit` | `Ritus` | 450 | review: merge |
| `medium` | `Medium` | 450 | review: merge |
| `mist` | `Mist` | 450 | review: merge |
| `satz` | `Satz` | 450 | review: merge |
| `Deutschlandweit` | `deutschlandweit` | 449 | review: merge |
| `Staud` | `Staude` | 449 | review: merge |
| `adresse` | `Adresse` | 449 | review: merge |
| `hren` | `hören` | 449 | review: merge |
| `Überhole` | `überholen` | 449 | review: merge |
| `Cas` | `Case` | 448 | review: merge |
| `produziert` | `produzieren` | 448 | review: merge |
| `Abweichende` | `abweichend` | 447 | review: merge |
| `Zusammenschluß` | `Zusammenschluss` | 447 | review: merge |
| `fünfjährigen` | `fünfjährig` | 447 | review: merge |
| `gebrauch` | `Gebrauch` | 447 | review: merge |
| `Hau` | `hauen` | 446 | review: merge |
| `Saniere` | `sanieren` | 446 | review: merge |
| `Südland` | `Südländer` | 446 | review: merge |
| `reissen` | `reißen` | 446 | review: merge |
| `Kostenfrei` | `kostenfrei` | 445 | review: merge |
| `Persönlich` | `persönlich` | 445 | review: merge |
| `Stabil` | `stabil` | 445 | review: merge |
| `fabelhafte` | `fabelhaft` | 445 | review: merge |
| `mitgelesen` | `mitlesen` | 445 | review: merge |
| `zugesagt` | `zusagen` | 445 | review: merge |
| `Relativ` | `relativ` | 444 | review: merge |
| `eingemacht` | `Eingemachte` | 444 | review: merge |
| `haette` | `haben` | 444 | review: merge |
| `stade` | `stad` | 444 | review: merge |
| `angegeben` | `angeben` | 443 | review: merge |
| `angelockt` | `anlocken` | 443 | review: merge |
| `bin` | `sein` | 443 | review: merge |
| `gerendert` | `rendern` | 443 | review: merge |
| `Anfänglich` | `anfänglich` | 442 | review: merge |
| `beratung` | `Beratung` | 442 | review: merge |
| `extravaganten` | `extravagant` | 442 | review: merge |
| `hnlich` | `ähnlich` | 442 | review: merge |
| `Dunkelblau` | `dunkelblau` | 441 | review: merge |
| `MEHR` | `mehr` | 441 | review: merge |
| `ala` | `à la` | 441 | review: merge |
| `leg` | `leger` | 441 | review: merge |
| `trag` | `tragen` | 441 | review: merge |
| `Behältnisse` | `Behältnis` | 440 | review: merge |
| `Minusgrade` | `Minusgrad` | 440 | review: merge |
| `Unglaublich` | `unglaublich` | 440 | review: merge |
| `angefragt` | `anfragen` | 440 | review: merge |
| `bedurfte` | `bedürfen` | 440 | review: merge |
| `gefassten` | `fassen` | 440 | review: merge |
| `pool` | `Pool` | 440 | review: merge |
| `studio` | `Studio` | 440 | review: merge |
| `wiederrum` | `wiederum` | 440 | review: merge |
| `Schwer` | `schwer` | 439 | review: merge |
| `schlag` | `schlagen` | 439 | review: merge |
| `Benötige` | `benötigen` | 438 | review: merge |
| `termin` | `Termin` | 438 | review: merge |
| `Bedrucke` | `bedrucken` | 437 | review: merge |
| `Verlinke` | `verlinken` | 437 | review: merge |
| `ffentlich` | `öffentlich` | 437 | review: merge |
| `geförderten` | `fördern` | 437 | review: merge |
| `lösungsorientierte` | `lösungsorientiert` | 437 | review: merge |
| `Besucherströme` | `Besucherstrom` | 436 | review: merge |
| `Breitengrade` | `Breitengrad` | 436 | review: merge |
| `Leichte` | `leicht` | 436 | review: merge |
| `Nom` | `Nomen` | 436 | review: merge |
| `Trockene` | `trocken` | 436 | review: merge |
| `blogge` | `bloggen` | 436 | review: merge |
| `dargelegt` | `darlegen` | 436 | review: merge |
| `eloxiert` | `eloxieren` | 436 | review: merge |
| `gekoppelt` | `koppeln` | 436 | review: merge |
| `laptop` | `Laptop` | 436 | review: merge |
| `produkte` | `Produkt` | 436 | review: merge |
| `Faszinierende` | `faszinierend` | 435 | review: merge |
| `ehr` | `eher` | 435 | review: merge |
| `handvoll` | `Handvoll` | 435 | review: merge |
| `Essstörungen` | `Essstörung` | 434 | review: merge |
| `Schlecht` | `schlecht` | 434 | review: merge |
| `Sonnenblumenkerne` | `Sonnenblumenkern` | 434 | review: merge |
| `bemisst` | `bemessen` | 434 | review: merge |
| `rausgekommen` | `rauskommen` | 434 | review: merge |
| `technik` | `Technik` | 434 | review: merge |
| `Hauf` | `Haufen` | 433 | review: merge |
| `Mitwirke` | `mitwirken` | 433 | review: merge |
| `Schütte` | `schütten` | 433 | review: merge |
| `Toben` | `toben` | 433 | review: merge |
| `eingelassen` | `einlassen` | 433 | review: merge |
| `wichtigst` | `wichtig` | 433 | review: merge |
| `angeklagt` | `Angeklagte` | 432 | review: merge |
| `gestützt` | `stützen` | 432 | review: merge |
| `scheisse` | `Scheiße` | 432 | review: merge |
| `wusstest` | `wissen` | 432 | review: merge |
| `Finanzinstitute` | `Finanzinstitut` | 431 | review: merge |
| `Paß` | `Pass` | 431 | review: merge |
| `mattiert` | `mattieren` | 431 | review: merge |
| `wertgeschätzt` | `wertschätzen` | 431 | review: merge |
| `Falsche` | `falsch` | 430 | review: merge |
| `Parabene` | `Paraben` | 430 | review: merge |
| `aufjedenfall` | `auf jeden Fall` | 430 | review: merge |
| `edelstahl` | `Edelstahl` | 430 | review: merge |
| `einsetzend` | `einsetzen` | 430 | review: merge |
| `marketing` | `Marketing` | 430 | review: merge |
| `miteinbezogen` | `miteinbeziehen` | 430 | review: merge |
| `Fabrikate` | `Fabrikat` | 429 | review: merge |
| `Hierunter` | `hierunter` | 429 | review: merge |
| `brand` | `Brand` | 429 | review: merge |
| `gelaufen` | `laufen` | 429 | review: merge |
| `verortet` | `verorten` | 429 | review: merge |
| `Affiliat` | `Affiliate` | 428 | review: merge |
| `Fak` | `Fake` | 428 | review: merge |
| `Füll` | `füllen` | 428 | review: merge |
| `Psychopathen` | `Psychopath` | 428 | review: merge |
| `Bildende` | `bilden` | 427 | review: merge |
| `Glasflächen` | `Glasfläche` | 427 | review: merge |
| `Bewahr` | `bewahren` | 426 | review: merge |
| `Abhebe` | `abheben` | 425 | review: merge |
| `Dicht` | `dicht` | 425 | review: merge |
| `Evangelien` | `Evangelium` | 425 | review: merge |
| `Privat` | `privat` | 425 | review: merge |
| `Vegetarisch` | `vegetarisch` | 425 | review: merge |
| `berhaupt` | `überhaupt` | 425 | review: merge |
| `bestrichen` | `bestreichen` | 425 | review: merge |
| `Speis` | `Speise` | 424 | review: merge |
| `appliziert` | `applizieren` | 424 | review: merge |
| `zubehör` | `Zubehör` | 424 | review: merge |
| `Über` | `über` | 424 | review: merge |
| `Blutergüsse` | `Bluterguss` | 423 | review: merge |
| `Familieim` | `Familie` | 423 | review: merge |
| `Geb` | `geboren` | 423 | review: merge |
| `Vs` | `versus` | 423 | review: merge |
| `beschieden` | `bescheiden` | 423 | review: merge |
| `verpackung` | `Verpackung` | 423 | review: merge |
| `wurd` | `werden` | 423 | review: merge |
| `Interessanterweise` | `interessanterweise` | 422 | review: merge |
| `fnf` | `fünf` | 422 | review: merge |
| `naturnahe` | `naturnah` | 422 | review: merge |
| `roulette` | `Roulette` | 422 | review: merge |
| `verletzten` | `verletzen` | 422 | review: merge |
| `vorgenannten` | `vorgenannt` | 422 | review: merge |
| `Quell` | `Quelle` | 421 | review: merge |
| `Verfolge` | `verfolgen` | 421 | review: merge |
| `hinzubekommen` | `hinbekommen` | 421 | review: merge |
| `hochglanz` | `Hochglanz` | 421 | review: merge |
| `vertrag` | `Vertrag` | 421 | review: merge |
| `zurueck` | `zurück` | 421 | review: merge |
| `aufgegeben` | `aufgeben` | 420 | review: merge |
| `cookies` | `Cookie` | 420 | review: merge |
| `eingepflegt` | `einpflegen` | 420 | review: merge |
| `geschmiedet` | `schmieden` | 420 | review: merge |
| `Knacken` | `knacken` | 419 | review: merge |
| `Pdf` | `PDF` | 419 | review: merge |
| `gespeichert` | `speichern` | 419 | review: merge |
| `kostüm` | `Kostüm` | 419 | review: merge |
| `seufz` | `seufzen` | 419 | review: merge |
| `sonntag` | `Sonntag` | 419 | review: merge |
| `tip` | `Tipp` | 419 | review: merge |
| `Offizielle` | `offiziell` | 418 | review: merge |
| `elektr` | `elektrisch` | 418 | review: merge |
| `hauptsache` | `Hauptsache` | 418 | review: merge |
| `zugeführt` | `zuführen` | 418 | review: merge |
| `Berühmt` | `berühmt` | 417 | review: merge |
| `grösst` | `groß` | 417 | review: merge |
| `hufig` | `häufig` | 417 | review: merge |
| `mai` | `Mai` | 417 | review: merge |
| `park` | `Park` | 417 | review: merge |
| `Deg` | `Degen` | 416 | review: merge |
| `Erinnern` | `erinnern` | 416 | review: merge |
| `Spazierengehe` | `spazierengehen` | 416 | review: merge |
| `angedeutet` | `andeuten` | 416 | review: merge |
| `befassten` | `sich befassen` | 416 | review: merge |
| `beschleunigt` | `beschleunigen` | 416 | review: merge |
| `bewegung` | `Bewegung` | 416 | review: merge |
| `einzuloggen` | `einloggen` | 416 | review: merge |
| `sekunden` | `Sekunde` | 416 | review: merge |
| `visualisiert` | `visualisieren` | 416 | review: merge |
| `Erlerne` | `erlernen` | 415 | review: merge |
| `Psycholog` | `Psychologe` | 415 | review: merge |
| `Selbstständiger` | `Selbstständige` | 415 | review: merge |
| `geschmack` | `Geschmack` | 415 | review: merge |
| `vorlage` | `Vorlage` | 415 | review: merge |
| `Rechtsextrem` | `rechtsextrem` | 414 | review: merge |
| `dauer` | `Dauer` | 414 | review: merge |
| `firma` | `Firma` | 414 | review: merge |
| `ih` | `ihr` | 414 | review: merge |
| `versierten` | `versiert` | 414 | review: merge |
| `zeichen` | `Zeichen` | 414 | review: merge |
| `sicherzugehen` | `sichergehen` | 413 | review: merge |
| `werbeflächen` | `Werbefläche` | 413 | review: merge |
| `Entsprechende` | `entsprechend` | 412 | review: merge |
| `Feucht` | `feucht` | 412 | review: merge |
| `Gallerie` | `Galerie` | 412 | review: merge |
| `lampe` | `Lampe` | 412 | review: merge |
| `samstag` | `Samstag` | 412 | review: merge |
| `stehts` | `stets` | 412 | review: merge |
| `vorallem` | `vor allem` | 412 | review: merge |
| `Unbeschadet` | `unbeschadet` | 411 | review: merge |
| `angesammelt` | `ansammeln` | 411 | review: merge |
| `ARTIKEL` | `Artikel` | 410 | review: merge |
| `Antifaschistische` | `antifaschistisch` | 410 | review: merge |
| `Wett` | `wettmachen` | 410 | review: merge |
| `begünstigt` | `begünstigen` | 410 | review: merge |
| `bescheidene` | `bescheiden` | 410 | review: merge |
| `erzeugt` | `erzeugen` | 410 | review: merge |
| `gewährt` | `gewähren` | 410 | review: merge |
| `Hochladen` | `hochladen` | 409 | review: merge |
| `bestell` | `bestellen` | 409 | review: merge |
| `geschenkt` | `schenken` | 409 | review: merge |
| `hervorgerufen` | `hervorrufen` | 409 | review: merge |
| `hälst` | `halten` | 409 | review: merge |
| `lern` | `lernen` | 409 | review: merge |
| `minute` | `Minute` | 409 | review: merge |
| `upgrade` | `Upgrade` | 409 | review: merge |
| `Kaufmännische` | `kaufmännisch` | 408 | review: merge |
| `kuchen` | `Kuchen` | 408 | review: merge |
| `lage` | `Lage` | 408 | review: merge |
| `BHs` | `BH` | 407 | review: merge |
| `FreundIn` | `Freundin` | 407 | review: merge |
| `abgeschnitten` | `abschneiden` | 407 | review: merge |
| `fermentiert` | `fermentieren` | 407 | review: merge |
| `nachhinein` | `Nachhinein` | 407 | review: merge |
| `Bestimmte` | `bestimmt` | 406 | review: merge |
| `Chatt` | `chatten` | 406 | review: merge |
| `Ergonomisch` | `ergonomisch` | 406 | review: merge |
| `Vorraus` | `Voraus` | 406 | review: merge |
| `Weblinks` | `Weblink` | 406 | review: merge |
| `gelingend` | `gelingen` | 406 | review: merge |
| `kampf` | `Kampf` | 406 | review: merge |
| `modifiziert` | `modifizieren` | 406 | review: merge |
| `nachrichten` | `Nachrichten` | 406 | review: merge |
| `nr` | `Nummer` | 406 | review: merge |
| `pornofilm` | `Pornofilm` | 406 | review: merge |
| `stattgefunden` | `stattfinden` | 406 | review: merge |
| `verein` | `Verein` | 406 | review: merge |
| `bestellung` | `Bestellung` | 405 | review: merge |
| `frh` | `früh` | 405 | review: merge |
| `Anomali` | `Anomalie` | 404 | review: merge |
| `Challeng` | `Challenge` | 404 | review: merge |
| `Murr` | `murren` | 404 | review: merge |
| `abspritz` | `abspritzen` | 404 | review: merge |
| `prozent` | `Prozent` | 404 | review: merge |
| `schaff` | `schaffen` | 404 | review: merge |
| `Rubbellose` | `Rubbellos` | 403 | review: merge |
| `Verkleben` | `verkleben` | 403 | review: merge |
| `eingeschüchtert` | `einschüchtern` | 403 | review: merge |
| `fÜr` | `für` | 403 | review: merge |
| `gesundheit` | `Gesundheit` | 403 | review: merge |
| `mittag` | `Mittag` | 403 | review: merge |
| `Effizient` | `effizient` | 402 | review: merge |
| `Erinner` | `erinnern` | 402 | review: merge |
| `Mißbrauch` | `Missbrauch` | 402 | review: merge |
| `Wenigste` | `wenig` | 402 | review: merge |
| `angehäuft` | `anhäufen` | 402 | review: merge |
| `angereist` | `anreisen` | 402 | review: merge |
| `merkur` | `Merkur` | 402 | review: merge |
| `vordefinierte` | `vordefiniert` | 402 | review: merge |
| `Hautirritationen` | `Hautirritation` | 401 | review: merge |
| `Vorteilhaft` | `vorteilhaft` | 401 | review: merge |
| `größen` | `Größe` | 401 | review: merge |
| `heranzuziehen` | `heranziehen` | 401 | review: merge |
| `individualisierte` | `individualisieren` | 401 | review: merge |
| `maß` | `Maß` | 401 | review: merge |
| `wahrscheinlicher` | `wahrscheinlich` | 401 | review: merge |
| `zugreifend` | `zugreifen` | 401 | review: merge |
| `Bange` | `bange` | 400 | review: merge |
| `Eiweiss` | `Eiweiß` | 400 | review: merge |
| `Erwähnenswert` | `erwähnenswert` | 400 | review: merge |
| `Primär` | `primär` | 400 | review: merge |
| `austretend` | `austreten` | 400 | review: merge |
| `vibriert` | `vibrieren` | 400 | review: merge |
| `vol` | `voll` | 400 | review: merge |
| `Inhaltstoff` | `Inhaltsstoff` | 399 | review: merge |
| `SUVs` | `SUV` | 399 | review: merge |
| `anbieter` | `Anbieter` | 399 | review: merge |
| `Sanft` | `sanft` | 398 | review: merge |
| `doofe` | `doof` | 398 | review: merge |
| `eingescannt` | `einscannen` | 398 | review: merge |
| `kuratiert` | `kuratieren` | 398 | review: merge |
| `sähen` | `sehen` | 398 | review: merge |
| `titelte` | `titeln` | 398 | review: merge |
| `Pflanzenextrakte` | `Pflanzenextrakt` | 397 | review: merge |
| `heist` | `heißen` | 397 | review: merge |
| `konto` | `Konto` | 397 | review: merge |
| `Ergänzende` | `ergänzend` | 396 | review: merge |
| `Mem` | `Meme` | 396 | review: merge |
| `Osmanische` | `osmanisch` | 396 | review: merge |
| `Trocke` | `trocken` | 396 | review: merge |
| `Verschließe` | `verschließen` | 396 | review: merge |
| `hintern` | `Hintern` | 396 | review: merge |
| `müll` | `Müll` | 396 | review: merge |
| `Barrierefrei` | `barrierefrei` | 395 | review: merge |
| `Querverweise` | `Querverweis` | 395 | review: merge |
| `Sozialpädagog` | `Sozialpädagoge` | 395 | review: merge |
| `Wenn` | `wenn` | 395 | review: merge |
| `erstenmal` | `Mal` | 395 | review: merge |
| `gelegenheit` | `Gelegenheit` | 395 | review: merge |
| `spter` | `später` | 395 | review: merge |
| `dvd` | `DVD` | 394 | review: merge |
| `heruntergefahren` | `herunterfahren` | 394 | review: merge |
| `registrierung` | `Registrierung` | 394 | review: merge |
| `verfassten` | `verfassen` | 394 | review: merge |
| `wald` | `Wald` | 394 | review: merge |
| `weiterverwendet` | `weiterverwenden` | 394 | review: merge |
| `Kassenärztliche` | `kassenärztlich` | 393 | review: merge |
| `Nasch` | `Naschen` | 393 | review: merge |
| `bewahrheitet` | `sich bewahrheiten` | 393 | review: merge |
| `machend` | `machen` | 393 | review: merge |
| `werk` | `Werk` | 393 | review: merge |
| `Flüchtlingsunterkünfte` | `Flüchtlingsunterkunft` | 392 | review: merge |
| `Intensive` | `intensiv` | 392 | review: merge |
| `Werfen` | `werfen` | 392 | review: merge |
| `beleuchtung` | `Beleuchtung` | 392 | review: merge |
| `bemehlten` | `bemehlen` | 392 | review: merge |
| `mutt` | `Mutter` | 392 | review: merge |
| `nutzerfreundlicher` | `nutzerfreundlich` | 392 | review: merge |
| `rechten` | `recht` | 392 | review: merge |
| `Blockieren` | `blockieren` | 391 | review: merge |
| `MWSt` | `Mehrwertsteuer` | 391 | review: merge |
| `Süss` | `süß` | 391 | review: merge |
| `ergebnis` | `Ergebnis` | 391 | review: merge |
| `papier` | `Papier` | 391 | review: merge |
| `Tätige` | `tätigen` | 390 | review: merge |
| `bericht` | `Bericht` | 390 | review: merge |
| `erde` | `Erde` | 390 | review: merge |
| `kaffee` | `Kaffee` | 390 | review: merge |
| `unterbrochen` | `unterbrechen` | 390 | review: merge |
| `Antragsstellung` | `Antragstellung` | 389 | review: merge |
| `Ausdrücken` | `ausdrücken` | 389 | review: merge |
| `Singleborse` | `Singlebörse` | 389 | review: merge |
| `Domän` | `Domäne` | 388 | review: merge |
| `hippen` | `hip` | 388 | review: merge |
| `Innehalte` | `innehalten` | 387 | review: merge |
| `einzigste` | `einzig` | 387 | review: merge |
| `hygienischen` | `hygienisch` | 387 | review: merge |
| `meer` | `Meer` | 387 | review: merge |
| `paket` | `Paket` | 387 | review: merge |
| `stress` | `Stress` | 387 | review: merge |
| `umrissen` | `umreißen` | 387 | review: merge |
| `balkon` | `Balkon` | 386 | review: merge |
| `freitag` | `Freitag` | 386 | review: merge |
| `gegensatz` | `Gegensatz` | 386 | review: merge |
| `sep` | `September` | 386 | review: merge |
| `Hellblau` | `hellblau` | 385 | review: merge |
| `Unsicher` | `unsicher` | 385 | review: merge |
| `mitzuführen` | `mitführen` | 385 | review: merge |
| `ball` | `Ball` | 384 | review: merge |
| `beigeordnet` | `Beigeordnete` | 384 | review: merge |
| `fabrik` | `Fabrik` | 384 | review: merge |
| `gespräch` | `Gespräch` | 384 | review: merge |
| `Fa` | `Firma` | 383 | review: merge |
| `grossen` | `groß` | 383 | review: merge |
| `smartphon` | `Smartphone` | 383 | review: merge |
| `technologie` | `Technologie` | 383 | review: merge |
| `Wirre` | `wirr` | 382 | review: merge |
| `jobs` | `Job` | 382 | review: merge |
| `reisst` | `reißen` | 382 | review: merge |
| `schränkt` | `einschränken` | 382 | review: merge |
| `stick` | `Stick` | 382 | review: merge |
| `verstossen` | `verstoßen` | 382 | review: merge |
| `Kahl` | `kahl` | 381 | review: merge |
| `Luch` | `Luchs` | 381 | review: merge |
| `akzeptiert` | `akzeptieren` | 381 | review: merge |
| `gerettet` | `retten` | 381 | review: merge |
| `herangetragen` | `herantragen` | 381 | review: merge |
| `nebensachlich` | `nebensächlich` | 381 | review: merge |
| `streamt` | `streamen` | 381 | review: merge |
| `Ausbleibe` | `ausbleiben` | 380 | review: merge |
| `aufgezeichnet` | `aufzeichnen` | 380 | review: merge |
| `ecke` | `Ecke` | 380 | review: merge |
| `eingeklemmt` | `einklemmen` | 380 | review: merge |
| `verantwortungsbewussten` | `verantwortungsbewusst` | 380 | review: merge |
| `Anwende` | `anwenden` | 379 | review: merge |
| `Sechste` | `sechste` | 379 | review: merge |
| `datenblatt` | `Datenblatt` | 379 | review: merge |
| `herstellung` | `Herstellung` | 379 | review: merge |
| `sehbehinderte` | `sehbehindert` | 379 | review: merge |
| `sekundar` | `sekundär` | 379 | review: merge |
| `metall` | `Metall` | 378 | review: merge |
| `neig` | `neigen` | 378 | review: merge |
| `waehrend` | `während` | 378 | review: merge |
| `Abspritz` | `abspritzen` | 377 | review: merge |
| `Nachschlage` | `nachschlagen` | 377 | review: merge |
| `Ultras` | `Ultra` | 377 | review: merge |
| `befragt` | `Befragte` | 377 | review: merge |
| `brief` | `Brief` | 377 | review: merge |
| `gewinnbringen` | `gewinnbringend` | 377 | review: merge |
| `Christliche` | `christlich` | 376 | review: merge |
| `Fer` | `fern` | 376 | review: merge |
| `Glck` | `Glück` | 376 | review: merge |
| `Hierüber` | `hierüber` | 376 | review: merge |
| `berg` | `Berg` | 376 | review: merge |
| `geschossen` | `schießen` | 376 | review: merge |
| `teilzuhaben` | `teilhaben` | 376 | review: merge |
| `vorkommend` | `vorkommen` | 376 | review: merge |
| `zurückzulegen` | `zurücklegen` | 376 | review: merge |
| `Blütenstände` | `Blütenstand` | 375 | review: merge |
| `Brownies` | `Brownie` | 375 | review: merge |
| `Dateianhänge` | `Dateianhang` | 375 | review: merge |
| `Druckerzeugnisse` | `Druckerzeugnis` | 375 | review: merge |
| `bemerkenswerte` | `bemerkenswert` | 375 | review: merge |
| `ideen` | `Idee` | 375 | review: merge |
| `Überzeuge` | `überzeugen` | 375 | review: merge |
| `Frühe` | `früh` | 374 | review: merge |
| `Hooligans` | `Hooligan` | 374 | review: merge |
| `Umsteige` | `umsteigen` | 374 | review: merge |
| `kerl` | `Kerl` | 374 | review: merge |
| `verringert` | `verringern` | 374 | review: merge |
| `Gebrauchte` | `gebraucht` | 373 | review: merge |
| `Mysteri` | `Mysterium` | 373 | review: merge |
| `Philosophische` | `philosophisch` | 373 | review: merge |
| `Sextreffe` | `Sextreffen` | 373 | review: merge |
| `anschluss` | `Anschluss` | 373 | review: merge |
| `events` | `Event` | 373 | review: merge |
| `gaaaanz` | `ganz` | 373 | review: merge |
| `glitzert` | `glitzern` | 373 | review: merge |
| `lter` | `alt` | 373 | review: merge |
| `sprach` | `Sprache` | 373 | review: merge |
| `verarbeitung` | `Verarbeitung` | 373 | review: merge |
| `verlinkter` | `verlinken` | 373 | review: merge |
| `Ablege` | `ablegen` | 372 | review: merge |
| `Arbeitnehmende` | `Arbeitnehmer` | 372 | review: merge |
| `Ausschluß` | `Ausschluss` | 372 | review: merge |
| `fahrzeug` | `Fahrzeug` | 372 | review: merge |
| `gesetz` | `Gesetz` | 372 | review: merge |
| `kindgerechten` | `kindgerecht` | 372 | review: merge |
| `Abg` | `Abgeordnete` | 371 | review: merge |
| `Stör` | `stören` | 371 | review: merge |
| `Vorbeigehe` | `vorbeigehen` | 371 | review: merge |
| `badezimmer` | `Badezimmer` | 371 | review: merge |
| `brave` | `brav` | 371 | review: merge |
| `erreichend` | `erreichen` | 371 | review: merge |
| `ingesamt` | `insgesamt` | 371 | review: merge |
| `seeehr` | `sehr` | 371 | review: merge |
| `spezial` | `speziell` | 371 | review: merge |
| `vorneherein` | `vornherein` | 371 | review: merge |
| `Atmungsaktiv` | `atmungsaktiv` | 370 | review: merge |
| `Intern` | `intern` | 370 | review: merge |
| `Profiteure` | `Profiteur` | 370 | review: merge |
| `firmiert` | `firmieren` | 370 | review: merge |
| `gebloggt` | `bloggen` | 370 | review: merge |
| `rutsch` | `rutschen` | 370 | review: merge |
| `tanz` | `tanzen` | 370 | review: merge |
| `Erweiter` | `erweitern` | 369 | review: merge |
| `Installiere` | `installieren` | 369 | review: merge |
| `Op` | `Operation` | 369 | review: merge |
| `netzwerk` | `Netzwerk` | 369 | review: merge |
| `systems` | `System` | 369 | review: merge |
| `teppich` | `Teppich` | 369 | review: merge |
| `Dt` | `deutsch` | 368 | review: merge |
| `Langweilig` | `langweilig` | 368 | review: merge |
| `entsandt` | `entsenden` | 368 | review: merge |
| `gehegt` | `hegen` | 368 | review: merge |
| `roulett` | `Roulette` | 368 | review: merge |
| `Akademische` | `akademisch` | 367 | review: merge |
| `Baß` | `Bass` | 367 | review: merge |
| `Erhitz` | `erhitzen` | 367 | review: merge |
| `Koenig` | `König` | 367 | review: merge |
| `ausgelö` | `auslösen` | 367 | review: merge |
| `einladungskarten` | `Einladungskarte` | 367 | review: merge |
| `ti` | `Tier` | 367 | review: merge |
| `Meditier` | `meditieren` | 366 | review: merge |
| `Universelle` | `universell` | 366 | review: merge |
| `Zeitlos` | `zeitlos` | 366 | review: merge |
| `blut` | `Blut` | 366 | review: merge |
| `Fünfte` | `fünfte` | 365 | review: merge |
| `GELD` | `Geld` | 365 | review: merge |
| `Grundlegend` | `grundlegend` | 365 | review: merge |
| `recyceltem` | `recyceln` | 365 | review: merge |
| `schränken` | `einschränken` | 365 | review: merge |
| `Forsch` | `forschen` | 364 | review: merge |
| `Luftfeucht` | `Luftfeuchte` | 364 | review: merge |
| `Sera` | `Serum` | 364 | review: merge |
| `abgesagt` | `absagen` | 363 | review: merge |
| `angaben` | `Angabe` | 363 | review: merge |
| `beigesteuert` | `beisteuern` | 363 | review: merge |
| `entstanden` | `entstehen` | 363 | review: merge |
| `hlt` | `halten` | 363 | review: merge |
| `Bort` | `Borte` | 362 | review: merge |
| `Rieg` | `Riege` | 362 | review: merge |
| `kognitive` | `kognitiv` | 362 | review: merge |
| `rasante` | `rasant` | 362 | review: merge |
| `saturn` | `Saturn` | 362 | review: merge |
| `straße` | `Straße` | 362 | review: merge |
| `techn` | `technisch` | 362 | review: merge |
| `Parcour` | `Parcours` | 361 | review: merge |
| `Wische` | `wischen` | 361 | review: merge |
| `Zuschau` | `zuschauen` | 361 | review: merge |
| `dutzend` | `Dutzend` | 361 | review: merge |
| `hasste` | `hassen` | 361 | review: merge |
| `kommunikation` | `Kommunikation` | 361 | review: merge |
| `schwächelt` | `schwächeln` | 361 | review: merge |
| `sehnlichst` | `sehnlich` | 361 | review: merge |
| `tuen` | `tun` | 361 | review: merge |
| `Bolz` | `bolzen` | 360 | review: merge |
| `Inh` | `Inhaber` | 360 | review: merge |
| `JAHRE` | `Jahr` | 360 | review: merge |
| `Mopped` | `Moped` | 360 | review: merge |
| `Unbekannt` | `unbekannt` | 360 | review: merge |
| `beschreibung` | `Beschreibung` | 360 | review: merge |
| `mißbrauchen` | `missbrauchen` | 360 | review: merge |
| `transfer` | `Transfer` | 360 | review: merge |
| `verstanden` | `verstehen` | 360 | review: merge |
| `wieg` | `wiegen` | 360 | review: merge |
| `Außergewöhnlich` | `außergewöhnlich` | 359 | review: merge |
| `Irgendwas` | `irgendwas` | 359 | review: merge |
| `Problemlos` | `problemlos` | 359 | review: merge |
| `deal` | `Deal` | 359 | review: merge |
| `moderne` | `modern` | 359 | review: merge |
| `ohr` | `Ohr` | 359 | review: merge |
| `sexualisierte` | `sexualisieren` | 359 | review: merge |
| `Üben` | `üben` | 359 | review: merge |
| `Aufgepasst` | `aufpassen` | 358 | review: merge |
| `Aufkleben` | `aufkleben` | 358 | review: merge |
| `geburt` | `Geburt` | 358 | review: merge |
| `traum` | `Traum` | 358 | review: merge |
| `vhs` | `Volkshochschule` | 358 | review: merge |
| `Pädophil` | `pädophil` | 357 | review: merge |
| `dekoration` | `Dekoration` | 357 | review: merge |
| `Hinten` | `hinten` | 356 | review: merge |
| `Teuer` | `teuer` | 356 | review: merge |
| `Verstellbarer` | `verstellbar` | 356 | review: merge |
| `bestätigt` | `bestätigen` | 356 | review: merge |
| `kicker` | `Kicker` | 356 | review: merge |
| `linie` | `Linie` | 356 | review: merge |
| `Donuts` | `Donut` | 355 | review: merge |
| `Idealerweise` | `idealerweise` | 355 | review: merge |
| `ausgestrahlt` | `ausstrahlen` | 355 | review: merge |
| `bordell` | `Bordell` | 355 | review: merge |
| `dermassen` | `dermaßen` | 355 | review: merge |
| `mindesten` | `mindest` | 355 | review: merge |
| `thun` | `tun` | 355 | review: merge |
| `Cd` | `CD` | 354 | review: merge |
| `Lenke` | `lenken` | 354 | review: merge |
| `Persische` | `persisch` | 354 | review: merge |
| `Preußische` | `preußisch` | 354 | review: merge |
| `Saarländische` | `saarländisch` | 354 | review: merge |
| `display` | `Display` | 354 | review: merge |
| `Berufsbildende` | `berufsbildend` | 353 | review: merge |
| `Fernreisen` | `Fernreise` | 353 | review: merge |
| `Gleit` | `gleiten` | 353 | review: merge |
| `begleitet` | `begleiten` | 353 | review: merge |
| `errettet` | `erretten` | 353 | review: merge |
| `loszulegen` | `loslegen` | 353 | review: merge |
| `medikament` | `Medikament` | 353 | review: merge |
| `verfgbar` | `verfügbar` | 353 | review: merge |
| `zugeschaltet` | `zuschalten` | 353 | review: merge |
| `Brandenburgische` | `brandenburgisch` | 352 | review: merge |
| `Geringste` | `gering` | 352 | review: merge |
| `Kampfjets` | `Kampfjet` | 352 | review: merge |
| `grundiert` | `grundieren` | 352 | review: merge |
| `missglückt` | `missglücken` | 352 | review: merge |
| `mässig` | `mäßig` | 352 | review: merge |
| `orginal` | `original` | 352 | review: merge |
| `populärst` | `populär` | 352 | review: merge |
| `reisend` | `reisen` | 352 | review: merge |
| `wiki` | `Wiki` | 352 | review: merge |
| `Geistige` | `geistig` | 351 | review: merge |
| `PatientIn` | `Patientin` | 351 | review: merge |
| `geliehen` | `leihen` | 351 | review: merge |
| `gesenkt` | `senken` | 351 | review: merge |
| `heranzukommen` | `herankommen` | 351 | review: merge |
| `lippen` | `Lippe` | 351 | review: merge |
| `migriert` | `migrieren` | 351 | review: merge |
| `schwerbehinderte` | `schwerbehindert` | 351 | review: merge |
| `selbstbewussten` | `selbstbewusst` | 351 | review: merge |
| `zuck` | `Zucker` | 351 | review: merge |
| `Bestehende` | `bestehend` | 350 | review: merge |
| `MÜSSEN` | `müssen` | 350 | review: merge |
| `Sideboards` | `Sideboard` | 350 | review: merge |
| `beilaufig` | `beiläufig` | 350 | review: merge |
| `vergrößert` | `vergrößern` | 350 | review: merge |
| `Bandbreit` | `Bandbreite` | 349 | review: merge |
| `Einmalig` | `einmalig` | 349 | review: merge |
| `Himbeer` | `Himbeere` | 349 | review: merge |
| `detail` | `Detail` | 349 | review: merge |
| `drinne` | `drinnen` | 349 | review: merge |
| `herbst` | `Herbst` | 349 | review: merge |
| `steifer` | `steif` | 349 | review: merge |
| `FeWo` | `Ferienwohnung` | 348 | review: merge |
| `IDs` | `ID` | 348 | review: merge |
| `Rech` | `Rechen` | 348 | review: merge |
| `Schneeschuhwander` | `Schneeschuhwandern` | 348 | review: merge |
| `VIER` | `vier` | 348 | review: merge |
| `beteiligten` | `beteiligen` | 348 | review: merge |
| `dreissig` | `dreißig` | 348 | review: merge |
| `getrieben` | `treiben` | 348 | review: merge |
| `gruppen` | `Gruppe` | 348 | review: merge |
| `pulverbeschichtetem` | `pulverbeschichtet` | 348 | review: merge |
| `saison` | `Saison` | 348 | review: merge |
| `Grüß` | `grüßen` | 347 | review: merge |
| `Handlungsstränge` | `Handlungsstrang` | 347 | review: merge |
| `abgetreten` | `abtreten` | 347 | review: merge |
| `ebenholz` | `Ebenholz` | 347 | review: merge |
| `portal` | `Portal` | 347 | review: merge |
| `restaurant` | `Restaurant` | 347 | review: merge |
| `tee` | `Tee` | 347 | review: merge |
| `änderung` | `Änderung` | 347 | review: merge |
| `Klack` | `Klacks` | 346 | review: merge |
| `Prompt` | `prompt` | 346 | review: merge |
| `award` | `Award` | 346 | review: merge |
| `center` | `Center` | 346 | review: merge |
| `eingeloggte` | `einloggen` | 346 | review: merge |
| `kreiert` | `kreieren` | 346 | review: merge |
| `Investier` | `investieren` | 345 | review: merge |
| `Schnapp` | `schnappen` | 345 | review: merge |
| `Sozialistische` | `sozialistisch` | 345 | review: merge |
| `Wunderbares` | `wunderbar` | 345 | review: merge |
| `dessous` | `Dessous` | 345 | review: merge |
| `esst` | `essen` | 345 | review: merge |
| `frites` | `Pommes` | 345 | review: merge |
| `sechst` | `sechste` | 345 | review: merge |
| `twittert` | `twittern` | 345 | review: merge |
| `übern` | `über` | 345 | review: merge |
| `Emotional` | `emotional` | 344 | review: merge |
| `Tyrannen` | `Tyrann` | 344 | review: merge |
| `bersicht` | `Übersicht` | 344 | review: merge |
| `boot` | `Boot` | 344 | review: merge |
| `bus` | `Bus` | 344 | review: merge |
| `erlernt` | `erlernen` | 344 | review: merge |
| `klassich` | `klassisch` | 344 | review: merge |
| `sieg` | `Sieg` | 344 | review: merge |
| `Gnome` | `Gnom` | 343 | review: merge |
| `Markier` | `markieren` | 343 | review: merge |
| `Wfl` | `Wohnfläche` | 343 | review: merge |
| `fhrt` | `führen` | 343 | review: merge |
| `imag` | `Image` | 343 | review: merge |
| `selbstkleben` | `selbstklebend` | 343 | review: merge |
| `Abhole` | `abholen` | 342 | review: merge |
| `Dachgeschoß` | `Dachgeschoss` | 342 | review: merge |
| `Krper` | `Körper` | 342 | review: merge |
| `Mic` | `Mikrofon` | 342 | review: merge |
| `Wurz` | `Wurzel` | 342 | review: merge |
| `aufnahmen` | `Aufnahme` | 342 | review: merge |
| `besucht` | `besuchen` | 342 | review: merge |
| `gestärkt` | `stärken` | 342 | review: merge |
| `medien` | `Medien` | 342 | review: merge |
| `sexfilme` | `Sexfilm` | 342 | review: merge |
| `zeitung` | `Zeitung` | 342 | review: merge |
| `balance` | `Balance` | 341 | review: merge |
| `laesst` | `lassen` | 341 | review: merge |
| `selbsternannte` | `selbsternannt` | 341 | review: merge |
| `wunsch` | `Wunsch` | 341 | review: merge |
| `Minimal` | `minimal` | 340 | review: merge |
| `gehört` | `hören` | 340 | review: merge |
| `heile` | `heil` | 340 | review: merge |
| `latex` | `Latex` | 340 | review: merge |
| `wärend` | `während` | 340 | review: merge |
| `Atlantische` | `atlantisch` | 339 | review: merge |
| `Mecklenburgische` | `mecklenburgisch` | 339 | review: merge |
| `festgehalten` | `festhalten` | 339 | review: merge |
| `geist` | `Geist` | 339 | review: merge |
| `mitglied` | `Mitglied` | 339 | review: merge |
| `saug` | `saugen` | 339 | review: merge |
| `startend` | `starten` | 339 | review: merge |
| `Editier` | `editieren` | 338 | review: merge |
| `Einsteig` | `einsteigen` | 338 | review: merge |
| `Hindus` | `Hindu` | 338 | review: merge |
| `Pfefferkörner` | `Pfefferkorn` | 338 | review: merge |
| `Thal` | `Tal` | 338 | review: merge |
| `diplomarbeit` | `Diplomarbeit` | 338 | review: merge |
| `ergebnisse` | `Ergebnis` | 338 | review: merge |
| `fahrrad` | `Fahrrad` | 338 | review: merge |
| `gelösten` | `lösen` | 338 | review: merge |
| `hall` | `Halle` | 338 | review: merge |
| `interactiv` | `interaktiv` | 338 | review: merge |
| `lizensiert` | `lizenzieren` | 338 | review: merge |
| `pornokino` | `Pornokino` | 338 | review: merge |
| `vergrössert` | `vergrößern` | 338 | review: merge |
| `werd` | `werden` | 338 | review: merge |
| `zahlung` | `Zahlung` | 338 | review: merge |
| `Auflege` | `auflegen` | 337 | review: merge |
| `Ausschlaggebend` | `ausschlaggebend` | 337 | review: merge |
| `Begrüssung` | `Begrüßung` | 337 | review: merge |
| `Erotisch` | `erotisch` | 337 | review: merge |
| `Mountainbikes` | `Mountainbike` | 337 | review: merge |
| `Vot` | `Vote` | 337 | review: merge |
| `alliierte` | `alliiert` | 337 | review: merge |
| `jeans` | `Jeans` | 337 | review: merge |
| `polizei` | `Polizei` | 337 | review: merge |
| `schuh` | `Schuh` | 337 | review: merge |
| `übung` | `Übung` | 337 | review: merge |
| `Diss` | `Dissertation` | 336 | review: merge |
| `Muck` | `Mucks` | 336 | review: merge |
| `Sach` | `Sache` | 336 | review: merge |
| `Verf` | `Verfasser` | 336 | review: merge |
| `block` | `Block` | 336 | review: merge |
| `consulting` | `Consulting` | 336 | review: merge |
| `existireren` | `existieren` | 336 | review: merge |
| `fleisch` | `Fleisch` | 336 | review: merge |
| `gegner` | `Gegner` | 336 | review: merge |
| `herausgeholt` | `herausholen` | 336 | review: merge |
| `mio` | `Million` | 336 | review: merge |
| `ruck` | `Ruck` | 336 | review: merge |
| `status` | `Status` | 336 | review: merge |
| `widern` | `anwidern` | 336 | review: merge |
| `Abschicke` | `abschicken` | 335 | review: merge |
| `Auf` | `auf` | 335 | review: merge |
| `Ausweiche` | `ausweichen` | 335 | review: merge |
| `Eßplatz` | `Essplatz` | 335 | review: merge |
| `Sämlinge` | `Sämling` | 335 | review: merge |
| `april` | `April` | 335 | review: merge |
| `stars` | `Star` | 335 | review: merge |
| `zielgerichteten` | `zielgerichtet` | 335 | review: merge |
| `Atla` | `Atlas` | 334 | review: merge |
| `Maritime` | `maritim` | 334 | review: merge |
| `Orginal` | `Original` | 334 | review: merge |
| `produktion` | `Produktion` | 334 | review: merge |
| `Empfehl` | `empfehlen` | 333 | review: merge |
| `Parallel` | `parallel` | 333 | review: merge |
| `Pfr` | `Pfarrer` | 333 | review: merge |
| `rissen` | `reißen` | 333 | review: merge |
| `tank` | `Tank` | 333 | review: merge |
| `Sechster` | `sechste` | 332 | review: merge |
| `ausgehebelt` | `aushebeln` | 332 | review: merge |
| `gekannt` | `kennen` | 332 | review: merge |
| `grösstenteils` | `größtenteils` | 332 | review: merge |
| `kombination` | `Kombination` | 332 | review: merge |
| `sterreich` | `Österreich` | 332 | review: merge |
| `trink` | `trinken` | 332 | review: merge |
| `wun` | `Wunde` | 332 | review: merge |
| `Krass` | `krass` | 331 | review: merge |
| `Verwandel` | `verwandeln` | 331 | review: merge |
| `htte` | `haben` | 331 | review: merge |
| `tatschlich` | `tatsächlich` | 331 | review: merge |
| `ton` | `Ton` | 331 | review: merge |
| `Aufnehmen` | `aufnehmen` | 330 | review: merge |
| `Benehme` | `Benehmen` | 330 | review: merge |
| `Identifizier` | `identifizieren` | 330 | review: merge |
| `Sondern` | `sondern` | 330 | review: merge |
| `Thür` | `Tür` | 276 | review: merge |
| `aufgaben` | `Aufgabe` | 330 | review: merge |
| `gönn` | `gönnen` | 330 | review: merge |
| `hrt` | `hören` | 330 | review: merge |
| `selbigen` | `selbig` | 330 | review: merge |
| `Ander` | `ander` | 329 | review: merge |
| `AG` | `Aktiengesellschaft` | 49,634 | review: merge |
| `ober` | `obere` | 22,167 | review: merge |
| `mittler` | `mittlere` | 21,926 | review: merge |
| `selb` | `selbe` | 19,288 | review: merge |
| `Super` | `super` | 18,786 | review: merge |
| `Prozeß` | `Prozess` | 16,517 | review: merge |
| `Neues` | `Neue` | 14,495 | review: merge |
| `frau` | `Frau` | 13,823 | review: merge |
| `Weitere` | `weiter` | 13,345 | review: merge |
| `Tools` | `Tool` | 11,400 | review: merge |
| `Würde` | `werden` | 11,282 | review: merge |
| `casino` | `Casino` | 10,663 | review: merge |
| `Spass` | `Spaß` | 9,559 | review: merge |
| `ber` | `über` | 9,121 | review: merge |
| `Große` | `groß` | 9,046 | review: merge |
| `Klein` | `klein` | 8,780 | review: merge |
| `Gleiche` | `gleich` | 8,628 | review: merge |
| `WM` | `Weltmeisterschaft` | 8,615 | review: merge |
| `NICHT` | `nicht` | 8,432 | review: merge |
| `eingesetzt` | `einsetzen` | 7,531 | review: merge |
| `dar` | `darstellen` | 7,417 | review: merge |
| `Kurze` | `kurz` | 7,397 | review: merge |
| `fuer` | `für` | 7,140 | review: merge |
| `editiert` | `editieren` | 7,121 | review: merge |
| `besseres` | `besser` | 7,107 | review: merge |
| `Voraus` | `voraus` | 7,105 | review: merge |
| `Keywords` | `Keyword` | 6,986 | review: merge |
| `jahr` | `Jahr` | 6,914 | review: merge |
| `bzw` | `beziehungsweise` | 6,814 | review: merge |
| `Schöne` | `schön` | 6,686 | review: merge |
| `nich` | `nicht` | 6,570 | review: merge |
| `kurzem` | `kurz` | 6,034 | review: merge |
| `geniessen` | `genießen` | 5,964 | review: merge |
| `schonmal` | `schon` | 5,611 | review: merge |
| `gross` | `groß` | 5,602 | review: merge |
| `u` | `und` | 5,555 | review: merge |
| `grösser` | `groß` | 5,554 | review: merge |
| `gestellt` | `stellen` | 5,440 | review: merge |
| `Andere` | `andere` | 5,437 | review: merge |
| `Mögliche` | `möglich` | 5,280 | review: merge |
| `präzis` | `präzise` | 5,171 | review: merge |
| `Wichtigste` | `wichtig` | 5,131 | review: merge |
| `porno` | `Porno` | 5,110 | review: merge |
| `kehrt` | `kehren` | 5,042 | review: merge |
| `zuviel` | `viel` | 5,032 | review: merge |
| `Buche` | `buchen` | 5,003 | review: merge |
| `nem` | `einem` | 4,896 | review: merge |
| `Busse` | `Bus` | 4,869 | review: merge |
| `Frei` | `frei` | 4,828 | review: merge |
| `Becke` | `Becken` | 4,805 | review: merge |
| `gekauft` | `kaufen` | 4,781 | review: merge |
| `bereitgestellt` | `bereitstellen` | 4,777 | review: merge |
| `erworben` | `erwerben` | 4,733 | review: merge |
| `FH` | `Fachhochschule` | 4,725 | review: merge |
| `kind` | `Kind` | 4,685 | review: merge |
| `geliefert` | `liefern` | 4,639 | review: merge |
| `fur` | `für` | 4,601 | review: merge |
| `hergestellt` | `herstellen` | 4,591 | review: merge |
| `EM` | `Europameisterschaft` | 4,583 | review: merge |
| `Interessant` | `interessant` | 4,570 | review: merge |
| `ausgenommen` | `ausnehmen` | 4,540 | review: merge |
| `gesammelt` | `sammeln` | 4,529 | review: merge |
| `email` | `E-Mail` | 4,526 | review: merge |
| `vorgestellt` | `vorstellen` | 4,396 | review: merge |
| `Tip` | `Tipp` | 4,356 | review: merge |
| `dating` | `Dating` | 4,334 | review: merge |
| `geschnitten` | `schneiden` | 4,282 | review: merge |
| `geprägt` | `prägen` | 4,265 | review: merge |
| `vorgeschrieben` | `vorschreiben` | 4,215 | review: merge |
| `erschienen` | `erscheinen` | 4,181 | review: merge |
| `geld` | `Geld` | 4,172 | review: merge |
| `Grösse` | `Größe` | 4,150 | review: merge |
| `getrocknet` | `trocknen` | 4,133 | review: merge |
| `anmeldung` | `Anmeldung` | 4,076 | review: merge |
| `Knote` | `Knoten` | 4,070 | review: merge |
| `Kleiner` | `klein` | 4,065 | review: merge |
| `Dass` | `dass` | 4,048 | review: merge |
| `gemäss` | `gemäß` | 4,047 | review: merge |
| `personenbezogene` | `personenbezogen` | 4,031 | review: merge |
| `knnen` | `können` | 4,008 | review: merge |
| `Einzige` | `einzig` | 3,975 | review: merge |
| `gezeigt` | `zeigen` | 3,956 | review: merge |
| `Aktuelle` | `aktuell` | 3,947 | review: merge |
| `gefordert` | `fordern` | 3,926 | review: merge |
| `preis` | `Preis` | 3,863 | review: merge |
| `Anlaß` | `Anlass` | 3,577 | review: merge |
| `ausschliesslich` | `ausschließlich` | 3,848 | review: merge |
| `übermittelt` | `übermitteln` | 3,820 | review: merge |
| `benannt` | `benennen` | 3,819 | review: merge |
| `gebucht` | `buchen` | 3,806 | review: merge |
| `seite` | `Seite` | 3,734 | review: merge |
| `Fit` | `fit` | 3,692 | review: merge |
| `Sichere` | `sicher` | 3,675 | review: merge |
| `ZU` | `zu` | 3,668 | review: merge |
| `heissen` | `heißen` | 3,642 | review: merge |
| `schliessen` | `schließen` | 3,602 | review: merge |
| `CA` | `circa` | 3,583 | review: merge |
| `Beliebe` | `Belieben` | 3,514 | review: merge |
| `Schwarze` | `schwarz` | 3,488 | review: merge |
| `Gerichte` | `Gericht` | 3,478 | review: merge |
| `iM` | `im` | 3,477 | review: merge |
| `resultierend` | `resultieren` | 3,379 | review: merge |
| `frauen` | `Frau` | 3,319 | review: merge |
| `mittel` | `Mittel` | 3,271 | review: merge |
| `Mio` | `Million` | 3,263 | review: merge |
| `gesünder` | `gesund` | 3,259 | review: merge |
| `Awards` | `Award` | 3,166 | review: merge |
| `Universal` | `universal` | 3,138 | review: merge |
| `Absolut` | `absolut` | 3,096 | review: merge |
| `Neueste` | `neu` | 3,075 | review: merge |
| `geschrieben` | `schreiben` | 3,059 | review: merge |
| `Längere` | `lang` | 3,034 | review: merge |
| `funktionierend` | `funktionieren` | 3,022 | review: merge |
| `zugeschnitten` | `zuschneiden` | 3,020 | review: merge |
| `wenns` | `wenn` | 3,010 | review: merge |
| `Passende` | `passend` | 3,007 | review: merge |
| `sohlen` | `Sohle` | 2,987 | review: merge |
| `LEDs` | `LED` | 2,983 | review: merge |
| `eingeloggt` | `einloggen` | 2,974 | review: merge |
| `sooo` | `so` | 2,958 | review: merge |
| `gegründet` | `gründen` | 2,954 | review: merge |
| `ner` | `eine` | 2,930 | review: merge |
| `gehalt` | `halten` | 2,928 | review: merge |
| `Kompromiß` | `Kompromiss` | 2,924 | review: merge |
| `wachsend` | `wachsen` | 2,924 | review: merge |
| `ausgebildet` | `ausbilden` | 2,914 | review: merge |
| `weiteres` | `weiter` | 2,900 | review: merge |
| `mEHR` | `mehr` | 2,897 | review: merge |
| `nähere` | `nah` | 2,882 | review: merge |
| `mädchen` | `Mädchen` | 2,881 | review: merge |
| `wars` | `sein` | 2,881 | review: merge |
| `knn` | `können` | 2,861 | review: merge |
| `freund` | `Freund` | 2,844 | review: merge |
| `mäßigen` | `mäßig` | 2,844 | review: merge |
| `herangezogen` | `heranziehen` | 2,840 | review: merge |
| `aussen` | `außen` | 2,802 | review: merge |
| `Fussball` | `Fußball` | 2,778 | review: merge |
| `beid` | `beide` | 2,775 | review: merge |
| `Inkl` | `inklusive` | 2,772 | review: merge |
| `eingegeben` | `eingeben` | 2,771 | review: merge |
| `Fair` | `fair` | 2,767 | review: merge |
| `vorgeschlagen` | `vorschlagen` | 2,754 | review: merge |
| `zulässt` | `zulassen` | 2,746 | review: merge |
| `letzt` | `letzte` | 2,738 | review: merge |
| `Optional` | `optional` | 2,733 | review: merge |
| `Konkret` | `konkret` | 2,726 | review: merge |
| `Anschluß` | `Anschluss` | 2,718 | review: merge |
| `erbracht` | `erbringen` | 2,706 | review: merge |
| `Ficke` | `ficken` | 2,635 | review: merge |
| `Script` | `Skript` | 2,595 | review: merge |
| `Mobil` | `mobil` | 2,574 | review: merge |
| `gutgeschrieben` | `gutschreiben` | 2,567 | review: merge |
| `weis` | `wissen` | 2,554 | review: merge |
| `engen` | `eng` | 2,553 | review: merge |
| `Schwitz` | `schwitzen` | 2,547 | review: merge |
| `SchülerIn` | `Schülerin` | 2,540 | review: merge |
| `Verweile` | `verweilen` | 2,536 | review: merge |
| `JA` | `ja` | 2,531 | review: merge |
| `ONLINE` | `online` | 2,529 | review: merge |
| `Palm` | `Palme` | 2,512 | review: merge |
| `verblieben` | `verbleiben` | 2,507 | review: merge |
| `Schluß` | `Schluss` | 2,498 | review: merge |
| `seh` | `sehen` | 2,489 | review: merge |
| `anschliessend` | `anschließend` | 2,469 | review: merge |
| `Mega` | `mega` | 2,436 | review: merge |
| `ueber` | `über` | 2,433 | review: merge |
| `film` | `Film` | 2,428 | review: merge |
| `getroffen` | `treffen` | 2,419 | review: merge |
| `Frisch` | `frisch` | 2,399 | review: merge |
| `spitze` | `spitz` | 2,384 | review: merge |
| `Gesund` | `gesund` | 2,368 | review: merge |
| `läng` | `lang` | 2,364 | review: merge |
| `Via` | `via` | 2,355 | review: merge |
| `mitgeliefert` | `mitliefern` | 2,353 | review: merge |
| `heiss` | `heiß` | 2,344 | review: merge |
| `Höchste` | `hoch` | 2,337 | review: merge |
| `angestellt` | `Angestellter` | 2,334 | review: merge |
| `bonus` | `Bonus` | 2,324 | review: merge |
| `nächstes` | `nächst` | 2,321 | review: merge |
| `Gruss` | `Gruß` | 2,320 | review: merge |
| `Ausbild` | `Ausbilder` | 2,314 | review: merge |
| `zertifizierten` | `zertifizieren` | 2,303 | review: merge |
| `eingereicht` | `einreichen` | 2,297 | review: merge |
| `inne` | `innehaben` | 2,291 | review: merge |
| `verlinkt` | `verlinken` | 2,287 | review: merge |
| `festgelegt` | `festlegen` | 2,285 | review: merge |
| `eingeführt` | `einführen` | 2,284 | review: merge |
| `Mass` | `Maß` | 2,279 | review: merge |
| `Zurück` | `zurück` | 2,275 | review: merge |
| `Hin` | `hin` | 2,271 | review: merge |
| `gemacht` | `machen` | 2,271 | review: merge |
| `durchgeführt` | `durchführen` | 2,261 | review: merge |
| `bräuchen` | `brauchen` | 2,260 | review: merge |
| `eingebaut` | `einbauen` | 2,259 | review: merge |
| `Fahn` | `Fahne` | 2,246 | review: merge |
| `erfahrung` | `Erfahrung` | 2,234 | review: merge |
| `Startups` | `Startup` | 2,215 | review: merge |
| `videos` | `Video` | 2,215 | review: merge |
| `schi` | `schier` | 2,212 | review: merge |
| `weiden` | `Weide` | 2,211 | review: merge |
| `liess` | `lassen` | 2,209 | review: merge |
| `geworden` | `werden` | 2,208 | review: merge |
| `hand` | `Hand` | 2,207 | review: merge |
| `Schweizerische` | `schweizerisch` | 2,205 | review: merge |
| `geschaffen` | `schaffen` | 2,200 | review: merge |
| `dahingehen` | `dahingehend` | 2,198 | review: merge |
| `Abschluß` | `Abschluss` | 2,196 | review: merge |
| `weissen` | `wissen` | 2,195 | review: merge |
| `gestiegen` | `steigen` | 2,184 | review: merge |
| `ding` | `Ding` | 2,181 | review: merge |
| `vornherein` | `von vornherein` | 2,176 | review: merge |
| `gabs` | `geben` | 2,168 | review: merge |
| `Strasse` | `Straße` | 2,155 | review: merge |
| `Kopiere` | `kopieren` | 2,154 | review: merge |
| `stationäre` | `stationär` | 2,146 | review: merge |
| `rezept` | `Rezept` | 2,137 | review: merge |
| `Letzt` | `letzt` | 2,129 | review: merge |
| `Jahrtausende` | `Jahrtausend` | 2,124 | review: merge |
| `weiss` | `weiß` | 2,124 | review: merge |
| `bewußt` | `bewusst` | 2,118 | review: merge |
| `Änder` | `ändern` | 2,103 | review: merge |
| `Vgl` | `vergleichen` | 2,101 | review: merge |
| `Anklicke` | `anklicken` | 2,096 | review: merge |
| `internet` | `Internet` | 2,088 | review: merge |
| `Münchener` | `Münchner` | 2,068 | review: merge |
| `äusserst` | `äußerst` | 2,066 | review: merge |
| `herunterzuladen` | `herunterladen` | 2,062 | review: merge |
| `arbeit` | `Arbeit` | 2,056 | review: merge |
| `Balk` | `Balken` | 2,045 | review: merge |
| `Weiter` | `weiter` | 2,040 | review: merge |
| `satte` | `satt` | 2,026 | review: merge |
| `Shoppe` | `shoppen` | 2,009 | review: merge |
| `Sträucher` | `Strauch` | 2,004 | review: merge |
| `einzige` | `einzig` | 2,004 | review: merge |
| `produkt` | `Produkt` | 2,000 | review: merge |
| `Km` | `Kilometer` | 1,998 | review: merge |
| `habs` | `haben` | 1,995 | review: merge |
| `Rühr` | `rühren` | 1,989 | review: merge |
| `Komplett` | `komplett` | 1,978 | review: merge |
| `gr` | `groß` | 1,962 | review: merge |
| `irgendeiner` | `irgendein` | 1,961 | review: merge |
| `wirds` | `werden` | 1,960 | review: merge |
| `facebook` | `Facebook` | 1,954 | review: merge |
| `stück` | `Stück` | 1,950 | review: merge |
| `Geschäftsprozesse` | `Geschäftsprozess` | 1,942 | review: merge |
| `Fel` | `Fels` | 1,939 | review: merge |
| `Grosse` | `groß` | 1,929 | review: merge |
| `erfolgt` | `erfolgen` | 1,917 | review: merge |
| `Regelmäßig` | `regelmäßig` | 1,912 | review: merge |
| `woch` | `Woche` | 1,909 | review: merge |
| `krieg` | `Krieg` | 1,908 | review: merge |
| `Probier` | `probieren` | 1,903 | review: merge |
| `Positiv` | `positiv` | 1,900 | review: merge |
| `Virtuelle` | `virtuell` | 1,892 | review: merge |
| `Heiz` | `heizen` | 1,889 | review: merge |
| `erotik` | `Erotik` | 1,870 | review: merge |
| `Schlei` | `Schleier` | 1,863 | review: merge |
| `wünsch` | `wünschen` | 1,853 | review: merge |
| `mitgelieferten` | `mitliefern` | 1,850 | review: merge |
| `renommierte` | `renommiert` | 1,849 | review: merge |
| `lust` | `Lust` | 1,838 | review: merge |
| `NÖ` | `nö` | 1,831 | review: merge |
| `Unabhängige` | `unabhängig` | 1,831 | review: merge |
| `zweitgrößte` | `zweitgrößt` | 1,824 | review: merge |
| `regelmässig` | `regelmäßig` | 1,816 | review: merge |
| `max` | `maximal` | 1,805 | review: merge |
| `nunmal` | `nun mal` | 1,805 | review: merge |
| `größ` | `Größe` | 1,780 | review: merge |
| `lach` | `lachen` | 1,771 | review: merge |
| `Modi` | `Modus` | 1,769 | review: merge |
| `ausgeführt` | `ausführen` | 1,769 | review: merge |
| `kleid` | `Kleid` | 1,769 | review: merge |
| `geleistet` | `leisten` | 1,754 | review: merge |
| `spaß` | `Spaß` | 1,752 | review: merge |
| `Frames` | `Frame` | 1,750 | review: merge |
| `Kolbe` | `Kolben` | 1,748 | review: merge |
| `meinung` | `Meinung` | 1,744 | review: merge |
| `vorgegeben` | `vorgeben` | 1,739 | review: merge |
| `koennen` | `können` | 1,737 | review: merge |
| `Kat` | `Katalysator` | 1,732 | review: merge |
| `beig` | `beige` | 1,731 | review: merge |
| `angeführt` | `anführen` | 1,728 | review: merge |
| `gezogen` | `ziehen` | 1,728 | review: merge |
| `Brennen` | `brennen` | 1,726 | review: merge |
| `steh` | `stehen` | 1,722 | review: merge |
| `ausgelegt` | `auslegen` | 1,721 | review: merge |
| `slots` | `Slot` | 1,721 | review: merge |
| `auseinanderzusetzen` | `auseinandersetzen` | 1,718 | review: merge |
| `kauf` | `Kauf` | 1,714 | review: merge |
| `gefertigt` | `fertigen` | 1,710 | review: merge |
| `mail` | `Mail` | 1,710 | review: merge |
| `Azubis` | `Azubi` | 1,707 | review: merge |
| `Typisch` | `typisch` | 1,704 | review: merge |
| `zertifizierter` | `zertifizieren` | 1,703 | review: merge |
| `Lade` | `laden` | 1,700 | review: merge |
| `sach` | `Sache` | 1,696 | review: merge |
| `Absende` | `absenden` | 1,695 | review: merge |
| `bekanntwerden` | `Bekanntwerden` | 1,686 | review: merge |
| `Nuß` | `Nuss` | 1,685 | review: merge |
| `Telefoniere` | `telefonieren` | 1,681 | review: merge |
| `muschi` | `Muschi` | 1,678 | review: merge |
| `Technisch` | `technisch` | 1,671 | review: merge |
| `Emailadresse` | `E-Mail-Adresse` | 1,667 | review: merge |
| `plan` | `Plan` | 1,666 | review: merge |
| `Aufl` | `Auflage` | 1,663 | review: merge |
| `bett` | `Bett` | 1,662 | review: merge |
| `personal` | `Personal` | 1,661 | review: merge |
| `platz` | `Platz` | 1,661 | review: merge |
| `Faste` | `fasten` | 1,657 | review: merge |
| `ei` | `Ei` | 1,657 | review: merge |
| `reg` | `rege` | 1,652 | review: merge |
| `IM` | `im` | 1,651 | review: merge |
| `dam` | `Dame` | 1,651 | review: merge |
| `soooo` | `so` | 1,651 | review: merge |
| `jahren` | `Jahr` | 1,646 | review: merge |
| `Kleinste` | `klein` | 1,640 | review: merge |
| `Kongreß` | `Kongress` | 1,639 | review: merge |
| `archiviert` | `archivieren` | 1,627 | review: merge |
| `Studier` | `studieren` | 1,623 | review: merge |
| `dritt` | `dritte` | 1,623 | review: merge |
| `chat` | `Chat` | 1,620 | review: merge |
| `Optimal` | `optimal` | 1,614 | review: merge |
| `monat` | `Monat` | 1,610 | review: merge |
| `stunden` | `Stunde` | 1,610 | review: merge |
| `HERR` | `Herr` | 1,605 | review: merge |
| `natur` | `Natur` | 1,601 | review: merge |
| `Spezielle` | `speziell` | 1,599 | review: merge |
| `kopf` | `Kopf` | 1,598 | review: merge |
| `Jederzeit` | `jederzeit` | 1,597 | review: merge |
| `Wohlfühle` | `wohlfühlen` | 1,593 | review: merge |
| `gro` | `groß` | 1,586 | review: merge |
| `google` | `Google` | 1,585 | review: merge |
| `ichs` | `ich` | 1,584 | review: merge |
| `test` | `Test` | 1,584 | review: merge |
| `freundin` | `Freundin` | 1,582 | review: merge |
| `Putze` | `putzen` | 1,581 | review: merge |
| `anfang` | `Anfang` | 1,578 | review: merge |
| `einzahlung` | `Einzahlung` | 1,575 | review: merge |
| `arsch` | `Arsch` | 1,571 | review: merge |
| `Eindrücken` | `Eindruck` | 1,570 | review: merge |
| `KEIN` | `kein` | 1,570 | review: merge |
| `süss` | `süß` | 1,569 | review: merge |
| `nichtmal` | `mal` | 1,557 | review: merge |
| `bloss` | `bloß` | 1,555 | review: merge |
| `letz` | `letzt` | 1,552 | review: merge |
| `Alleine` | `alleine` | 1,551 | review: merge |
| `Wichtige` | `wichtig` | 1,551 | review: merge |
| `woche` | `Woche` | 1,550 | review: merge |
| `zieh` | `ziehen` | 1,550 | review: merge |
| `Wilder` | `wild` | 1,548 | review: merge |
| `Eigen` | `eigen` | 1,545 | review: merge |
| `Kaufleute` | `Kaufmann` | 1,542 | review: merge |
| `Ausscheide` | `ausscheiden` | 1,540 | review: merge |
| `Tapet` | `Tapete` | 1,537 | review: merge |
| `Ziff` | `Ziffer` | 1,535 | review: merge |
| `äussern` | `äußern` | 1,534 | review: merge |
| `zurückgelegen` | `zurücklegen` | 1,533 | review: merge |
| `Davor` | `davor` | 1,525 | review: merge |
| `Hop` | `Hip-Hop` | 1,525 | review: merge |
| `smarte` | `smart` | 1,517 | review: merge |
| `platzsparen` | `platzsparend` | 1,516 | review: merge |
| `vergleich` | `Vergleich` | 1,516 | review: merge |
| `Polle` | `Pollen` | 1,515 | review: merge |
| `viert` | `vierte` | 1,510 | review: merge |
| `MitarbeiterIn` | `Mitarbeiterin` | 1,502 | review: merge |
| `text` | `Text` | 1,502 | review: merge |
| `Hur` | `Hure` | 1,500 | review: merge |
| `buch` | `Buch` | 1,496 | review: merge |
| `Keiner` | `keiner` | 1,494 | review: merge |
| `nasse` | `nass` | 1,493 | review: merge |
| `ÜBER` | `über` | 1,488 | review: merge |
| `haar` | `Haar` | 1,484 | review: merge |
| `Stolle` | `Stollen` | 1,477 | review: merge |
| `NEUE` | `neu` | 1,475 | review: merge |
| `website` | `Website` | 1,474 | review: merge |
| `stammend` | `stammen` | 1,469 | review: merge |
| `Mischen` | `mischen` | 1,468 | review: merge |
| `grund` | `Grund` | 1,468 | review: merge |
| `Kg` | `Kilogramm` | 1,465 | review: merge |
| `Klare` | `klar` | 1,465 | review: merge |
| `Optisch` | `optisch` | 1,464 | review: merge |
| `Niederland` | `Niederländer` | 1,460 | review: merge |
| `pornos` | `Porno` | 1,459 | review: merge |
| `gings` | `gehen` | 1,457 | review: merge |
| `ambitionierte` | `ambitioniert` | 1,455 | review: merge |
| `bisch` | `bisschen` | 1,455 | review: merge |
| `drückt` | `drücken` | 1,452 | review: merge |
| `mitgebracht` | `mitbringen` | 1,447 | review: merge |
| `Bohr` | `bohren` | 1,446 | review: merge |
| `Schönste` | `schön` | 1,444 | review: merge |
| `signiert` | `signieren` | 1,439 | review: merge |
| `vorangetrieben` | `vorantreiben` | 1,439 | review: merge |
| `Versandkostenfrei` | `versandkostenfrei` | 1,438 | review: merge |
| `mssen` | `müssen` | 1,438 | review: merge |
| `gesehen` | `sehen` | 1,437 | review: merge |
| `bewusste` | `bewusst` | 1,436 | review: merge |
| `wass` | `Wasser` | 1,435 | review: merge |
| `Regional` | `regional` | 1,429 | review: merge |
| `Scheiß` | `Scheiße` | 1,429 | review: merge |
| `gestohlen` | `stehlen` | 1,429 | review: merge |
| `sachen` | `Sache` | 1,429 | review: merge |
| `vllt` | `vielleicht` | 1,429 | review: merge |
| `loszuwerden` | `loswerden` | 1,428 | review: merge |
| `nachgewiesen` | `nachweisen` | 1,428 | review: merge |
| `inneren` | `innert` | 1,427 | review: merge |
| `respektiv` | `respektive` | 1,424 | review: merge |
| `Blaue` | `blau` | 1,423 | review: merge |
| `frag` | `fragen` | 1,423 | review: merge |
| `club` | `Club` | 1,419 | review: merge |
| `Zin` | `Zins` | 1,417 | review: merge |
| `bilder` | `Bild` | 1,416 | review: merge |
| `iss` | `essen` | 1,416 | review: merge |
| `Misstraue` | `Misstrauen` | 1,415 | review: merge |
| `FR` | `für` | 1,412 | review: merge |
| `Einfluß` | `Einfluss` | 1,407 | review: merge |
| `Schlitt` | `Schlitten` | 1,403 | review: merge |
| `handy` | `Handy` | 1,403 | review: merge |
| `bestanden` | `bestehen` | 1,392 | review: merge |
| `whrend` | `während` | 1,392 | review: merge |
| `farbe` | `Farbe` | 1,390 | review: merge |
| `beleg` | `belegen` | 1,386 | review: merge |
| `versuch` | `versuchen` | 1,386 | review: merge |
| `aufgesetzt` | `aufsetzen` | 1,385 | review: merge |
| `angezeigt` | `anzeigen` | 1,384 | review: merge |
| `stehend` | `stehen` | 1,384 | review: merge |
| `klingend` | `klingen` | 1,383 | review: merge |
| `Kalte` | `kalt` | 1,379 | review: merge |
| `beschlossen` | `beschließen` | 1,379 | review: merge |
| `Beschluß` | `Beschluss` | 1,378 | review: merge |
| `Radikaler` | `Radikale` | 1,378 | review: merge |
| `Größte` | `groß` | 1,376 | review: merge |
| `Blogg` | `bloggen` | 1,375 | review: merge |
| `eMail` | `E-Mail` | 1,372 | review: merge |
| `Lappe` | `Lappen` | 1,371 | review: merge |
| `material` | `Material` | 1,369 | review: merge |
| `zimmer` | `Zimmer` | 1,366 | review: merge |
| `Guides` | `Guide` | 1,365 | review: merge |
| `geimpft` | `impfen` | 1,365 | review: merge |
| `Ambient` | `Ambiente` | 1,364 | review: merge |
| `Missverständnisse` | `Missverständnis` | 1,362 | review: merge |
| `Offen` | `offen` | 1,360 | review: merge |
| `idee` | `Idee` | 1,360 | review: merge |
| `gam` | `Game` | 1,359 | review: merge |
| `rest` | `Rest` | 1,354 | review: merge |
| `zugedeckt` | `zudecken` | 1,353 | review: merge |
| `beispiel` | `Beispiel` | 1,352 | review: merge |
| `frohe` | `froh` | 1,352 | review: merge |
| `beste` | `gut` | 1,350 | review: merge |
| `form` | `Form` | 1,349 | review: merge |
| `grossartig` | `großartig` | 1,349 | review: merge |
| `Geile` | `geil` | 1,347 | review: merge |
| `partnervermittlung` | `Partnervermittlung` | 1,347 | review: merge |
| `Hip` | `hip` | 1,346 | review: merge |
| `Mitnehme` | `mitnehmen` | 1,345 | review: merge |
| `fängt` | `fangen` | 1,345 | review: merge |
| `bad` | `Bad` | 1,339 | review: merge |
| `vorgenommen` | `vornehmen` | 1,329 | review: merge |
| `anpasst` | `anpassen` | 1,328 | review: merge |
| `Ausfülle` | `ausfüllen` | 1,326 | review: merge |
| `Schlechte` | `schlecht` | 1,325 | review: merge |
| `bein` | `Bein` | 1,323 | review: merge |
| `Hüte` | `Hut` | 1,322 | review: merge |
| `shop` | `Shop` | 1,322 | review: merge |
| `Funktioniere` | `funktionieren` | 1,321 | review: merge |
| `hats` | `haben` | 1,320 | review: merge |
| `statten` | `ausstatten` | 1,320 | review: merge |
| `fick` | `ficken` | 1,319 | review: merge |
| `slot` | `Slot` | 1,318 | review: merge |
| `Installieren` | `installieren` | 1,317 | review: merge |
| `baby` | `Baby` | 1,315 | review: merge |
| `schrägen` | `schräg` | 1,312 | review: merge |
| `Klickt` | `klicken` | 1,310 | review: merge |
| `aufgepasst` | `aufpassen` | 1,310 | review: merge |
| `geblieben` | `bleiben` | 1,308 | review: merge |
| `ggf` | `gegebenenfalls` | 1,308 | review: merge |
| `fange` | `fangen` | 1,306 | review: merge |
| `Blind` | `blind` | 1,298 | review: merge |
| `version` | `Version` | 1,298 | review: merge |
| `angepassten` | `angepasst` | 1,296 | review: merge |
| `natrlich` | `natürlich` | 1,291 | review: merge |
| `land` | `Land` | 1,290 | review: merge |
| `liessen` | `lassen` | 1,290 | review: merge |
| `menschen` | `Mensch` | 1,285 | review: merge |
| `titten` | `Titte` | 1,285 | review: merge |
| `schritt` | `Schritt` | 1,284 | review: merge |
| `fahr` | `fahren` | 1,281 | review: merge |
| `person` | `Person` | 1,281 | review: merge |
| `jen` | `jener` | 1,279 | review: merge |
| `Vibrationen` | `Vibration` | 1,277 | review: merge |
| `herausgekommen` | `herauskommen` | 1,269 | review: merge |
| `Pilat` | `Pilates` | 1,266 | review: merge |
| `geschenk` | `Geschenk` | 1,264 | review: merge |
| `KM` | `Kilometer` | 1,262 | review: merge |
| `Lecker` | `lecker` | 1,262 | review: merge |
| `bescheid` | `Bescheid` | 1,257 | review: merge |
| `od` | `oder` | 1,257 | review: merge |
| `Toke` | `Token` | 1,256 | review: merge |
| `begonnen` | `beginnen` | 1,253 | review: merge |
| `genommen` | `nehmen` | 1,253 | review: merge |
| `kontrolliert` | `kontrollieren` | 1,250 | review: merge |
| `berichte` | `berichten` | 1,247 | review: merge |
| `dichter` | `dicht` | 1,245 | review: merge |
| `Theoretisch` | `theoretisch` | 1,244 | review: merge |
| `Einstelle` | `einstellen` | 1,243 | review: merge |
| `Empfehlenswert` | `empfehlenswert` | 1,240 | review: merge |
| `Therm` | `Therme` | 1,239 | review: merge |
| `Nass` | `nass` | 1,237 | review: merge |
| `befüllt` | `befüllen` | 1,237 | review: merge |
| `Beig` | `beige` | 1,236 | review: merge |
| `Schuß` | `Schuss` | 1,235 | review: merge |
| `mglich` | `möglich` | 1,235 | review: merge |
| `sO` | `so` | 1,234 | review: merge |
| `schweizer` | `Schweizer` | 1,230 | review: merge |
| `Zentral` | `zentral` | 1,228 | review: merge |
| `Individuell` | `individuell` | 1,226 | review: merge |
| `blog` | `Blog` | 1,225 | review: merge |
| `fleissig` | `fleißig` | 1,222 | review: merge |
| `ausgeschieden` | `ausscheiden` | 1,221 | review: merge |
| `eingegangen` | `eingehen` | 1,221 | review: merge |
| `aufgerufen` | `aufrufen` | 1,218 | review: merge |
| `minuten` | `Minute` | 1,216 | review: merge |
| `Faß` | `Fass` | 1,215 | review: merge |
| `resp` | `respektive` | 1,209 | review: merge |
| `naß` | `nass` | 1,208 | review: merge |
| `Ne` | `eine` | 1,207 | review: merge |
| `anschliessen` | `anschließen` | 1,207 | review: merge |
| `naht` | `nahen` | 1,207 | review: merge |
| `angst` | `Angst` | 1,205 | review: merge |
| `glück` | `Glück` | 1,205 | review: merge |
| `blick` | `Blick` | 1,201 | review: merge |
| `konnen` | `können` | 1,201 | review: merge |
| `übernahmen` | `übernehmen` | 1,201 | review: merge |
| `Anm` | `Anmerkung` | 1,200 | review: merge |
| `bereich` | `Bereich` | 1,200 | review: merge |
| `mitgelieferte` | `mitliefern` | 1,200 | review: merge |
| `jetz` | `jetzt` | 1,198 | review: merge |
| `mund` | `Mund` | 1,198 | review: merge |
| `Ziehe` | `ziehen` | 1,194 | review: merge |
| `angebot` | `Angebot` | 1,194 | review: merge |
| `angefochten` | `anfechten` | 1,193 | review: merge |
| `MwSt` | `Mehrwertsteuer` | 1,191 | review: merge |
| `auseinandergesetzt` | `auseinandersetzen` | 1,191 | review: merge |
| `gehn` | `gehen` | 1,190 | review: merge |
| `hätt` | `haben` | 1,188 | review: merge |
| `menge` | `Menge` | 1,188 | review: merge |
| `Upgrad` | `Upgrade` | 1,185 | review: merge |
| `versteh` | `verstehen` | 1,184 | review: merge |
| `Analog` | `analog` | 1,183 | review: merge |
| `Sicher` | `sichern` | 1,182 | review: merge |
| `gefühl` | `Gefühl` | 1,178 | review: merge |
| `Öfter` | `oft` | 1,178 | review: merge |
| `gesicht` | `Gesicht` | 1,174 | review: merge |
| `wei` | `weiß` | 1,174 | review: merge |
| `Schießen` | `schießen` | 1,168 | review: merge |
| `Abspiel` | `abspielen` | 1,166 | review: merge |
| `Elegant` | `elegant` | 1,166 | review: merge |
| `Versage` | `Versagen` | 1,165 | review: merge |
| `gebaut` | `bauen` | 1,164 | review: merge |
| `verbündet` | `Verbündeter` | 1,162 | review: merge |
| `updat` | `Update` | 1,160 | review: merge |
| `Lokomotiv` | `Lokomotive` | 1,158 | review: merge |
| `aug` | `Auge` | 1,158 | review: merge |
| `ergebend` | `ergeben` | 1,156 | review: merge |
| `Krypto` | `Kryptowährung` | 1,154 | review: merge |
| `Mglichkeit` | `Möglichkeit` | 1,154 | review: merge |
| `Staatliche` | `staatlich` | 1,152 | review: merge |
| `Rheinische` | `rheinisch` | 1,150 | review: merge |
| `erfahrungen` | `Erfahrung` | 1,145 | review: merge |
| `Üblicherweise` | `üblicherweise` | 1,145 | review: merge |
| `leser` | `Leser` | 1,144 | review: merge |
| `Historische` | `historisch` | 1,143 | review: merge |
| `Sauber` | `sauber` | 1,142 | review: merge |
| `körper` | `Körper` | 1,135 | review: merge |
| `scheiß` | `Scheiß` | 1,135 | review: merge |
| `gehostet` | `hosten` | 1,134 | review: merge |
| `Brocke` | `Brocken` | 1,133 | review: merge |
| `Stk` | `Stück` | 1,131 | review: merge |
| `sexkontakte` | `Sexkontakt` | 1,131 | review: merge |
| `suchaufkommen` | `Suchaufkommen` | 1,130 | review: merge |
| `interviewt` | `interviewen` | 1,129 | review: merge |
| `soo` | `so` | 1,128 | review: merge |
| `spiel` | `Spieler` | 1,128 | review: merge |
| `NGOs` | `NGO` | 1,127 | review: merge |
| `Bemühe` | `Bemühen` | 1,125 | review: merge |
| `Flexibel` | `flexibel` | 1,125 | review: merge |
| `fu` | `für` | 1,124 | review: merge |
| `ide` | `Idee` | 1,121 | review: merge |
| `Inwieweit` | `inwieweit` | 1,120 | review: merge |
| `erhoben` | `erheben` | 1,119 | review: merge |
| `dargestellt` | `darstellen` | 1,118 | review: merge |
| `Rinder` | `Rind` | 1,116 | review: merge |
| `kastriert` | `kastrieren` | 1,114 | review: merge |
| `AGBs` | `AGB` | 1,112 | review: merge |
| `getätigt` | `tätigen` | 1,111 | review: merge |
| `hochzuladen` | `hochladen` | 1,111 | review: merge |
| `Warm` | `warm` | 1,110 | review: merge |
| `flirt` | `Flirt` | 1,110 | review: merge |
| `fotos` | `Foto` | 1,110 | review: merge |
| `Chinesische` | `chinesisch` | 1,108 | review: merge |
| `Superlative` | `Superlativ` | 1,108 | review: merge |
| `Beweg` | `bewegen` | 1,106 | review: merge |
| `nam` | `Name` | 1,106 | review: merge |
| `tisch` | `Tisch` | 1,105 | review: merge |
| `apotheke` | `Apotheke` | 1,102 | review: merge |
| `oma` | `Oma` | 1,102 | review: merge |
| `swing` | `Swing` | 1,102 | review: merge |
| `Wasserdicht` | `wasserdicht` | 1,101 | review: merge |
| `musik` | `Musik` | 1,101 | review: merge |
| `escort` | `Escort` | 1,100 | review: merge |
| `verkauf` | `Verkauf` | 1,100 | review: merge |
| `damen` | `Dame` | 1,097 | review: merge |
| `kryptowährung` | `Kryptowährung` | 1,097 | review: merge |
| `Kompakt` | `kompakt` | 1,096 | review: merge |
| `zeig` | `zeigen` | 1,096 | review: merge |
| `benutzerdefinierte` | `benutzerdefiniert` | 1,094 | review: merge |
| `Anschreibe` | `Anschreiben` | 1,093 | review: merge |
| `spass` | `Spaß` | 1,092 | review: merge |
| `sinn` | `Sinn` | 1,089 | review: merge |
| `Anpasse` | `anpassen` | 1,087 | review: merge |
| `müsstest` | `müssen` | 1,087 | review: merge |
| `Anschaue` | `anschauen` | 1,085 | review: merge |
| `ergangen` | `ergehen` | 1,085 | review: merge |
| `uber` | `über` | 1,084 | review: merge |
| `Auffällig` | `auffällig` | 1,082 | review: merge |
| `lanciert` | `lancieren` | 1,082 | review: merge |
| `Werbezwecke` | `Werbezweck` | 1,079 | review: merge |
| `möglichkeit` | `Möglichkeit` | 1,079 | review: merge |
| `einher` | `einhergehen` | 1,076 | review: merge |
| `magern` | `mager` | 1,076 | review: merge |
| `jedenfall` | `jedenfalls` | 1,075 | review: merge |
| `eig` | `eigentlich` | 1,073 | review: merge |
| `amateur` | `Amateur` | 1,071 | review: merge |
| `Stor` | `Store` | 1,068 | review: merge |
| `Gastronomen` | `Gastronom` | 1,067 | review: merge |
| `urlaub` | `Urlaub` | 1,067 | review: merge |
| `energiesparen` | `energiesparend` | 1,065 | review: merge |
| `Einsetze` | `einsetzen` | 1,061 | review: merge |
| `start` | `Start` | 1,059 | review: merge |
| `massage` | `Massage` | 1,057 | review: merge |
| `Genuß` | `Genuss` | 1,054 | review: merge |
| `wg` | `Wohngemeinschaft` | 1,051 | review: merge |
| `Streams` | `Stream` | 1,050 | review: merge |
| `Lebende` | `lebend` | 1,049 | review: merge |
| `Aug` | `Auge` | 1,045 | review: merge |
| `Ficht` | `Fichte` | 1,043 | review: merge |
| `artikel` | `Artikel` | 1,041 | review: merge |
| `unterlegt` | `unterlegen` | 1,038 | review: merge |
| `Bewußtsein` | `Bewusstsein` | 1,036 | review: merge |
| `kanns` | `können` | 1,036 | review: merge |
| `antwort` | `Antwort` | 1,033 | review: merge |
| `hänge` | `hängen` | 1,031 | review: merge |
| `Offene` | `offen` | 1,028 | review: merge |
| `kunden` | `Kunde` | 1,028 | review: merge |
| `bissl` | `bisschen` | 1,026 | review: merge |
| `Trainiere` | `trainieren` | 1,024 | review: merge |
| `hochzeit` | `Hochzeit` | 1,024 | review: merge |
| `Erlernen` | `erlernen` | 1,022 | review: merge |
| `Starke` | `stark` | 1,022 | review: merge |
| `exkl` | `exklusive` | 1,020 | review: merge |
| `fallend` | `fallen` | 1,018 | review: merge |
| `schuhe` | `Schuh` | 1,016 | review: merge |
| `Di` | `Dienstag` | 1,014 | review: merge |
| `mitgeteilt` | `mitteilen` | 1,014 | review: merge |
| `web` | `Web` | 1,014 | review: merge |
| `Psych` | `Psyche` | 1,013 | review: merge |
| `ect` | `etc` | 1,013 | review: merge |
| `mitte` | `Mitte` | 1,013 | review: merge |
| `Kollage` | `Collage` | 1,011 | review: merge |
| `Informieren` | `informieren` | 1,006 | review: merge |
| `Mrz` | `März` | 1,006 | review: merge |
| `benötigt` | `benötigen` | 1,004 | review: merge |
| `Ausschalte` | `ausschalten` | 1,003 | review: merge |
| `dr` | `Doktor` | 1,001 | review: merge |
| `nennenswerte` | `nennenswert` | 1,001 | review: merge |
| `Relaxen` | `relaxen` | 1,000 | review: merge |
| `entscheide` | `entscheiden` | 1,000 | review: merge |
| `Indische` | `indisch` | 999 | review: merge |
| `Hilfreich` | `hilfreich` | 998 | review: merge |
| `transparente` | `transparent` | 998 | review: merge |
| `namen` | `Name` | 996 | review: merge |
| `unterhaltsame` | `unterhaltsam` | 990 | review: merge |
| `Bik` | `Bike` | 989 | review: merge |
| `Vorn` | `vorn` | 987 | review: merge |
| `rückblicken` | `rückblickend` | 987 | review: merge |
| `Schloß` | `Schloss` | 986 | review: merge |
| `fühl` | `fühlen` | 986 | review: merge |
| `Pauschalreisen` | `Pauschalreise` | 985 | review: merge |
| `begrüssen` | `begrüßen` | 983 | review: merge |
| `zarte` | `zart` | 983 | review: merge |
| `Ame` | `Amen` | 982 | review: merge |
| `Fühle` | `fühlen` | 982 | review: merge |
| `Cupcakes` | `Cupcake` | 981 | review: merge |
| `detaillierter` | `detailliert` | 980 | review: merge |
| `Bänder` | `Band` | 978 | review: merge |
| `gefahren` | `fahren` | 978 | review: merge |
| `kontakt` | `Kontakt` | 978 | review: merge |
| `Goldene` | `golden` | 977 | review: merge |
| `Gültig` | `gültig` | 976 | review: merge |
| `fahrt` | `Fahrt` | 976 | review: merge |
| `Automatisch` | `automatisch` | 975 | review: merge |
| `Schmunzel` | `schmunzeln` | 975 | review: merge |
| `Klassisch` | `klassisch` | 972 | review: merge |
| `stossen` | `stoßen` | 972 | review: merge |
| `Sortier` | `sortieren` | 971 | review: merge |
| `gelegt` | `legen` | 968 | review: merge |
| `erhälst` | `erhalten` | 966 | review: merge |
| `markt` | `Markt` | 966 | review: merge |
| `Außergewöhnliche` | `außergewöhnlich` | 965 | review: merge |
| `beidem` | `beide` | 964 | review: merge |
| `gesetzl` | `gesetzlich` | 964 | review: merge |
| `Verleg` | `verlegen` | 962 | review: merge |
| `Pflegebedürftiger` | `Pflegebedürftige` | 960 | review: merge |
| `richtung` | `Richtung` | 957 | review: merge |
| `Nachlaß` | `Nachlass` | 955 | review: merge |
| `feuchten` | `feucht` | 955 | review: merge |
| `übernommen` | `übernehmen` | 955 | review: merge |
| `nciht` | `nicht` | 953 | review: merge |
| `Zuschuß` | `Zuschuss` | 952 | review: merge |
| `Anfasse` | `anfassen` | 950 | review: merge |
| `Nicht` | `Nichte` | 947 | review: merge |
| `grosszügig` | `großzügig` | 946 | review: merge |
| `Bürgerliche` | `bürgerlich` | 945 | review: merge |
| `UM` | `um` | 945 | review: merge |
| `gefördert` | `fördern` | 945 | review: merge |
| `ort` | `Ort` | 945 | review: merge |
| `Lach` | `Lachs` | 944 | review: merge |
| `unterschrieben` | `unterschreiben` | 944 | review: merge |
| `jungs` | `Junge` | 943 | review: merge |
| `Zand` | `Zander` | 941 | review: merge |
| `singlebörse` | `Singlebörse` | 935 | review: merge |
| `Bedien` | `bedienen` | 931 | review: merge |
| `Gelernte` | `gelernt` | 931 | review: merge |
| `einzelnen` | `einzeln` | 931 | review: merge |
| `Briefumschläge` | `Briefumschlag` | 930 | review: merge |
| `eltern` | `Eltern` | 930 | review: merge |
| `Fluß` | `Fluss` | 929 | review: merge |
| `Offensichtlich` | `offensichtlich` | 929 | review: merge |
| `Vierter` | `vierte` | 928 | review: merge |
| `geburtstag` | `Geburtstag` | 928 | review: merge |
| `Maser` | `Masern` | 927 | review: merge |
| `farben` | `Farbe` | 927 | review: merge |
| `nimm` | `nimmer` | 927 | review: merge |
| `teilnahmen` | `teilnehmen` | 927 | review: merge |
| `praxisnahe` | `praxisnah` | 926 | review: merge |
| `Intelligent` | `intelligent` | 925 | review: merge |
| `Treibhausgase` | `Treibhausgas` | 925 | review: merge |
| `interesse` | `Interesse` | 925 | review: merge |
| `Geschenkgutscheine` | `Geschenkgutschein` | 923 | review: merge |
| `Sep` | `September` | 921 | review: merge |
| `echtgeld` | `Echtgeld` | 921 | review: merge |
| `gang` | `Gang` | 921 | review: merge |
| `Ausprobieren` | `ausprobieren` | 920 | review: merge |
| `Betreibe` | `betreiben` | 920 | review: merge |
| `hei` | `heiß` | 919 | review: merge |
| `gegangen` | `gehen` | 916 | review: merge |
| `Lösen` | `lösen` | 915 | review: merge |
| `Selbstständig` | `selbstständig` | 914 | review: merge |
| `Erdgeschoß` | `Erdgeschoss` | 913 | review: merge |
| `dafr` | `dafür` | 911 | review: merge |
| `Kommunistische` | `kommunistisch` | 907 | review: merge |
| `gehandelt` | `handeln` | 907 | review: merge |
| `geilen` | `geil` | 906 | review: merge |
| `beitrag` | `Beitrag` | 905 | review: merge |
| `Ausschuß` | `Ausschuss` | 904 | review: merge |
| `mitgeführt` | `mitführen` | 904 | review: merge |
| `wort` | `Wort` | 904 | review: merge |
| `kabel` | `Kabel` | 903 | review: merge |
| `unsre` | `unser` | 899 | review: merge |
| `Abschalte` | `abschalten` | 898 | review: merge |
| `Terasse` | `Terrasse` | 898 | review: merge |
| `erlebt` | `erleben` | 898 | review: merge |
| `populäre` | `populär` | 898 | review: merge |
| `Experimentier` | `experimentieren` | 896 | review: merge |
| `einschl` | `einschließlich` | 896 | review: merge |
| `vieleicht` | `vielleicht` | 895 | review: merge |
| `zeitnahe` | `zeitnah` | 894 | review: merge |
| `stunde` | `Stunde` | 893 | review: merge |
| `box` | `Box` | 892 | review: merge |
| `job` | `Job` | 892 | review: merge |
| `Bunt` | `bunt` | 891 | review: merge |
| `Gefall` | `Gefälle` | 890 | review: merge |
| `Jüdische` | `jüdisch` | 890 | review: merge |
| `roll` | `Rolle` | 890 | review: merge |
| `Sele` | `Selen` | 888 | review: merge |
| `Freu` | `sich freuen` | 885 | review: merge |
| `Zang` | `Zange` | 884 | review: merge |
| `leistung` | `Leistung` | 884 | review: merge |
| `Tschechische` | `tschechisch` | 883 | review: merge |
| `Anziehe` | `anziehen` | 882 | review: merge |
| `wärs` | `sein` | 882 | review: merge |
| `Servieren` | `servieren` | 880 | review: merge |
| `Gibts` | `geben` | 878 | review: merge |
| `poste` | `posten` | 877 | review: merge |
| `Geil` | `geil` | 876 | review: merge |
| `Herberg` | `Herberge` | 876 | review: merge |
| `Programmieren` | `programmieren` | 876 | review: merge |
| `lik` | `Like` | 876 | review: merge |
| `orang` | `orange` | 876 | review: merge |
| `Anbringe` | `anbringen` | 875 | review: merge |
| `admin` | `Admin` | 875 | review: merge |
| `geschichte` | `Geschichte` | 875 | review: merge |
| `charmante` | `charmant` | 872 | review: merge |
| `Quo` | `Status quo` | 871 | review: merge |
| `ziel` | `Ziel` | 871 | review: merge |
| `Außen` | `außen` | 870 | review: merge |
| `zurückgeschickt` | `zurückschicken` | 870 | review: merge |
| `ahnung` | `Ahnung` | 869 | review: merge |
| `evt` | `eventuell` | 869 | review: merge |
| `höhe` | `Höhe` | 867 | review: merge |
| `Katz` | `Katze` | 865 | review: merge |
| `Westfälische` | `westfälisch` | 865 | review: merge |
| `luft` | `Luft` | 862 | review: merge |
| `aufm` | `auf` | 858 | review: merge |
| `erneuerbaren` | `erneuerbar` | 858 | review: merge |
| `Trete` | `treten` | 857 | review: merge |
| `Programmier` | `programmieren` | 856 | review: merge |
| `angesteuert` | `ansteuern` | 856 | review: merge |
| `umgesetzt` | `umsetzen` | 856 | review: merge |
| `Ambulante` | `ambulant` | 855 | review: merge |
| `Pc` | `PC` | 852 | review: merge |
| `Rach` | `Rachen` | 852 | review: merge |
| `vgl` | `vergleichen` | 852 | review: merge |
| `angetrieben` | `antreiben` | 851 | review: merge |
| `gestartet` | `starten` | 851 | review: merge |
| `ists` | `sein` | 851 | review: merge |
| `kannste` | `können` | 851 | review: merge |
| `wuerde` | `würde` | 851 | review: merge |
| `Höchst` | `höchst` | 850 | review: merge |
| `erfolg` | `Erfolg` | 849 | review: merge |
| `pass` | `Pass` | 849 | review: merge |
| `zoll` | `Zoll` | 849 | review: merge |
| `Mwst` | `Mehrwertsteuer` | 847 | review: merge |
| `bezug` | `Bezug` | 847 | review: merge |
| `begangen` | `begehen` | 846 | review: merge |
| `Botanische` | `botanisch` | 844 | review: merge |
| `Ruhig` | `ruhig` | 844 | review: merge |
| `Vorlese` | `vorlesen` | 844 | review: merge |
| `gehren` | `gehören` | 844 | review: merge |
| `gelinkt` | `linken` | 844 | review: merge |
| `fang` | `fangen` | 842 | review: merge |
| `fernzuhalten` | `fernhalten` | 841 | review: merge |
| `vereinigt` | `vereinigen` | 839 | review: merge |
| `Loslasse` | `loslassen` | 838 | review: merge |
| `finds` | `finden` | 838 | review: merge |
| `irgendeinen` | `irgendein` | 838 | review: merge |
| `Selber` | `selber` | 836 | review: merge |
| `Fein` | `fein` | 835 | review: merge |
| `Mrd` | `Milliarde` | 835 | review: merge |
| `abschliessen` | `abschließen` | 835 | review: merge |
| `gestaltet` | `gestalten` | 835 | review: merge |
| `Verfügbar` | `verfügbar` | 833 | review: merge |
| `kraß` | `krass` | 831 | review: merge |
| `natuerlich` | `natürlich` | 831 | review: merge |
| `Kribbel` | `Kribbeln` | 830 | review: merge |
| `genutzt` | `nutzen` | 830 | review: merge |
| `entwurmt` | `entwurmen` | 828 | review: merge |
| `getötet` | `töten` | 828 | review: merge |
| `vereinbart` | `vereinbaren` | 828 | review: merge |
| `Befülle` | `befüllen` | 826 | review: merge |
| `aUCH` | `auch` | 824 | review: merge |
| `potenziellen` | `potenziell` | 824 | review: merge |
| `Dumme` | `dumm` | 823 | review: merge |
| `bekomm` | `bekommen` | 822 | review: merge |
| `cd` | `CD` | 821 | review: merge |
| `Füsse` | `Fuß` | 819 | review: merge |
| `herausgegeben` | `herausgeben` | 819 | review: merge |
| `jmd` | `jemand` | 819 | review: merge |
| `multipliziert` | `multiplizieren` | 819 | review: merge |
| `zulieb` | `zuliebe` | 818 | review: merge |
| `Bünde` | `Bund` | 817 | review: merge |
| `Förder` | `fördern` | 815 | review: merge |
| `Knowhow` | `Know-how` | 814 | review: merge |
| `m` | `M` | 85,123 | review: merge |
| `x` | `X` | 62,245 | review: merge |
| `s` | `S` | 45,190 | review: merge |
| `g` | `G` | 42,147 | review: merge |
| `Gern` | `gern` | 22,569 | review: merge |
| `Online` | `online` | 21,201 | review: merge |
| `b` | `B` | 19,977 | review: merge |
| `e` | `E` | 14,515 | review: merge |
| `l` | `L` | 11,795 | review: merge |
| `c` | `C` | 11,581 | review: merge |
| `t` | `T` | 10,447 | review: merge |
| `Erste` | `erste` | 7,176 | review: merge |
| `Highlights` | `Highlight` | 6,818 | review: merge |
| `Mag` | `mögen` | 6,773 | review: merge |
| `Nächste` | `nächste` | 6,011 | review: merge |
| `eBook` | `Ebook` | 5,516 | review: merge |
| `Lieber` | `lieber` | 4,623 | review: merge |
| `fall` | `Fall` | 4,329 | review: merge |
| `Arme` | `Arm` | 4,170 | review: merge |
| `Mehr` | `mehr` | 4,118 | review: merge |
| `Profitieren` | `profitieren` | 3,852 | review: merge |
| `Grille` | `grillen` | 3,744 | review: merge |
| `Werkstätte` | `Werkstatt` | 3,708 | review: merge |
| `Tablets` | `Tablet` | 3,694 | review: merge |
| `Praktische` | `praktisch` | 3,540 | review: merge |
| `Perfekt` | `perfekt` | 3,276 | review: merge |
| `Französische` | `französisch` | 3,255 | review: merge |
| `Letzte` | `letzte` | 2,978 | review: merge |
| `DVDs` | `DVD` | 2,976 | review: merge |
| `Plakate` | `Plakat` | 2,905 | review: merge |
| `hellen` | `hell` | 2,768 | review: merge |
| `Potenziale` | `Potenzial` | 2,744 | review: merge |
| `Personenbezogene` | `personenbezogen` | 2,513 | review: merge |
| `Gewürze` | `Gewürz` | 2,442 | review: merge |
| `Handeln` | `handeln` | 2,386 | review: merge |
| `Dinger` | `Ding` | 2,384 | review: merge |
| `Displays` | `Display` | 2,326 | review: merge |
| `Überzeugen` | `überzeugen` | 2,220 | review: merge |
| `Tweets` | `Tweet` | 2,176 | review: merge |
| `Lassen` | `lassen` | 2,103 | review: merge |
| `Tippen` | `tippen` | 2,065 | review: merge |
| `Module` | `Modul` | 2,058 | review: merge |
| `samen` | `Samen` | 2,003 | review: merge |
| `Aktiv` | `aktiv` | 1,957 | review: merge |
| `Angeblich` | `angeblich` | 1,888 | review: merge |
| `Völlig` | `völlig` | 1,879 | review: merge |
| `iN` | `in` | 1,876 | review: merge |
| `Medizinische` | `medizinisch` | 1,861 | review: merge |
| `klamm` | `Klammer` | 1,812 | review: merge |
| `Mods` | `Mod` | 1,788 | review: merge |
| `Größere` | `groß` | 1,784 | review: merge |
| `Pools` | `Pool` | 1,782 | review: merge |
| `Kürzlich` | `kürzlich` | 1,779 | review: merge |
| `Negativ` | `negativ` | 1,759 | review: merge |
| `Prüfen` | `prüfen` | 1,672 | review: merge |
| `nächste` | `nächst` | 1,653 | review: merge |
| `uhr` | `Uhr` | 1,639 | review: merge |
| `Hierzu` | `hierzu` | 1,611 | review: merge |
| `Felsen` | `Fels` | 1,582 | review: merge |
| `Jährlich` | `jährlich` | 1,569 | review: merge |
| `Tattoos` | `Tattoo` | 1,517 | review: merge |
| `Grabe` | `Graben` | 1,466 | review: merge |
| `rüde` | `Rüde` | 1,428 | review: merge |
| `Muslime` | `Muslim` | 1,421 | review: merge |
| `Studiengänge` | `Studiengang` | 1,385 | review: merge |
| `Kreditinstitute` | `Kreditinstitut` | 1,374 | review: merge |
| `wii` | `Wii` | 1,367 | review: merge |
| `nm` | `Nm` | 1,318 | review: merge |
| `thema` | `Thema` | 1,287 | review: merge |
| `Scannen` | `scannen` | 1,260 | review: merge |
| `Gräber` | `Grab` | 1,051 | review: merge |
| `Workflows` | `Workflow` | 1,251 | review: merge |
| `pc` | `PC` | 1,240 | review: merge |
| `Buse` | `Busen` | 1,226 | review: merge |
| `Wohnmobile` | `Wohnmobil` | 1,213 | review: merge |
| `Zelte` | `Zelt` | 1,189 | review: merge |
| `Onlineshops` | `Onlineshop` | 1,159 | review: merge |
| `Testen` | `testen` | 1,158 | review: merge |
| `Grüsse` | `Gruss` | 1,154 | review: merge |
| `Bildschirme` | `Bildschirm` | 1,148 | review: merge |
| `Rausche` | `rauschen` | 1,144 | review: merge |
| `Wunderbar` | `wunderbar` | 1,141 | review: merge |
| `Staun` | `staunen` | 1,129 | review: merge |
| `Automobile` | `Automobil` | 1,128 | review: merge |
| `Digitale` | `digital` | 1,115 | review: merge |
| `Maßgeblich` | `maßgeblich` | 1,108 | review: merge |
| `ex` | `Ex` | 1,104 | review: merge |
| `Labore` | `Labor` | 1,092 | review: merge |
| `Gass` | `Gasse` | 1,089 | review: merge |
| `Anschliessend` | `anschließend` | 1,078 | review: merge |
| `Downloade` | `downloaden` | 1,071 | review: merge |
| `Pedale` | `Pedal` | 1,060 | review: merge |
| `Schals` | `Schal` | 1,058 | review: merge |
| `Neugierig` | `neugierig` | 1,055 | review: merge |
| `Kindertagesstätten` | `Kindertagesstätte` | 1,049 | review: merge |
| `Wendungen` | `Wendung` | 1,044 | review: merge |
| `Sonnenschirme` | `Sonnenschirm` | 1,038 | review: merge |
| `Vorgehensweisen` | `Vorgehensweise` | 1,032 | review: merge |
| `Grüße` | `Gruß` | 1,031 | review: merge |
| `Schwierigkeitsgrade` | `Schwierigkeitsgrad` | 1,025 | review: merge |
| `Jackpots` | `Jackpot` | 1,015 | review: merge |
| `herz` | `Herz` | 1,003 | review: merge |
| `Urlaube` | `Urlaub` | 1,001 | review: merge |
| `Achja` | `achja` | 1,000 | review: merge |
| `Nahezu` | `nahezu` | 995 | review: merge |
| `ibiza` | `Ibiza` | 993 | review: merge |
| `Wahlweise` | `wahlweise` | 983 | review: merge |
| `Rote` | `rot` | 979 | review: merge |
| `Tutorials` | `Tutorial` | 963 | review: merge |
| `Musikalisch` | `musikalisch` | 956 | review: merge |
| `Patche` | `Patch` | 936 | review: merge |
| `Webinare` | `Webinar` | 931 | review: merge |
| `Schnitte` | `Schnitt` | 930 | review: merge |
| `Willen` | `Wille` | 929 | review: merge |
| `Materiale` | `Material` | 927 | review: merge |
| `Dates` | `Date` | 919 | review: merge |
| `wichtigste` | `Wichtigste` | 914 | review: merge |
| `Extrakte` | `Extrakt` | 905 | review: merge |
| `gend` | `Gender` | 899 | review: merge |
| `rauen` | `rau` | 893 | review: merge |
| `ausser` | `außer` | 889 | review: merge |
| `Bergische` | `bergisch` | 885 | review: merge |
| `ps` | `PS` | 878 | review: merge |
| `PDFs` | `PDF` | 877 | review: merge |
| `Backups` | `Backup` | 867 | review: merge |
| `Auslaufen` | `auslaufen` | 855 | review: merge |
| `iPhon` | `iPhone` | 850 | review: merge |
| `icloud` | `iCloud` | 849 | review: merge |
| `Gelbe` | `gelb` | 847 | review: merge |
| `Allein` | `allein` | 834 | review: merge |
| `kamera` | `Kamera` | 823 | review: merge |
| `Vintage` | `vintage` | 818 | review: merge |
| `Kombinieren` | `kombinieren` | 816 | review: merge |
| `Fingerabdrücke` | `Fingerabdruck` | 813 | review: merge |
| `Nr` | `Nummer` | 810 | review: merge |
| `Mikrofone` | `Mikrofon` | 809 | review: merge |
| `Rechtzeitig` | `rechtzeitig` | 806 | review: merge |
| `Etikette` | `Etikett` | 804 | review: merge |
| `Deutlich` | `deutlich` | 800 | review: merge |
| `Schleimhäute` | `Schleimhaut` | 788 | review: merge |
| `Erneuerbar` | `erneuerbar` | 787 | review: merge |
| `Transparente` | `Transparent` | 786 | review: merge |
| `Ü` | `ü` | 783 | review: merge |
| `Unikate` | `Unikat` | 782 | review: merge |
| `Vertragsverhältniss` | `Vertragsverhältnis` | 774 | review: merge |
| `anm` | `Anmerkung` | 764 | review: merge |
| `Geldbörsen` | `Geldbörse` | 763 | review: merge |
| `Felse` | `Fels` | 758 | review: merge |
| `Kreative` | `kreativ` | 758 | review: merge |
| `Selfies` | `Selfie` | 746 | review: merge |
| `Wandtattoos` | `Wandtattoo` | 738 | review: merge |
| `Shampoos` | `Shampoo` | 737 | review: merge |
| `So` | `so` | 734 | review: merge |
| `Kontaktformulars` | `Kontaktformular` | 733 | review: merge |
| `Politische` | `politisch` | 731 | review: merge |
| `Träume` | `Traum` | 729 | review: merge |
| `LKWs` | `LKW` | 728 | review: merge |
| `Eigene` | `eigen` | 727 | review: merge |
| `Definitiv` | `definitiv` | 721 | review: merge |
| `Spitäler` | `Spital` | 710 | review: merge |
| `chance` | `Chance` | 710 | review: merge |
| `Passe` | `passen` | 702 | review: merge |
| `Städtereisen` | `Städtereise` | 694 | review: merge |
| `examen` | `Examen` | 690 | review: merge |
| `gute` | `gut` | 687 | review: merge |
| `lumen` | `Lumen` | 680 | review: merge |
| `Rundreisen` | `Rundreise` | 669 | review: merge |
| `Passen` | `passen` | 667 | review: merge |
| `Todesfälle` | `Todesfall` | 664 | review: merge |
| `Terminals` | `Terminal` | 660 | review: merge |
| `Nachhaltig` | `nachhaltig` | 650 | review: merge |
| `Winde` | `Wind` | 650 | review: merge |
| `Kaffees` | `Kaffee` | 649 | review: merge |
| `Faxe` | `Fax` | 644 | review: merge |
| `Wusstest` | `wissen` | 640 | review: merge |
| `Bewusst` | `bewusst` | 637 | review: merge |
| `Wunderschön` | `wunderschön` | 635 | review: merge |
| `Delfine` | `Delfin` | 634 | review: merge |
| `eau` | `Eau` | 630 | review: merge |
| `Hmmm` | `hmmm` | 629 | review: merge |
| `Ihrerseits` | `ihrerseits` | 626 | review: merge |
| `Künftig` | `künftig` | 625 | review: merge |
| `dasMehr` | `Mehr` | 625 | review: merge |
| `Perücken` | `Perücke` | 621 | review: merge |
| `eckdaten` | `Eckdaten` | 618 | review: merge |
| `Mitteldeutsch` | `mitteldeutsch` | 609 | review: merge |
| `lego` | `LEGO` | 609 | review: merge |
| `Verstellbare` | `verstellbar` | 608 | review: merge |
| `Campe` | `campen` | 607 | review: merge |
| `Optimieren` | `optimieren` | 604 | review: merge |
| `Ähm` | `ähm` | 602 | review: merge |
| `selbermachen` | `Selbermachen` | 594 | review: merge |
| `Tribute` | `Tribut` | 593 | review: merge |
| `Sonderanfertigungen` | `Sonderanfertigung` | 591 | review: merge |
| `Arbeiten` | `arbeiten` | 589 | review: merge |
| `Headsets` | `Headset` | 589 | review: merge |
| `Zähle` | `zählen` | 589 | review: merge |
| `Schlagworte` | `Schlagwort` | 584 | review: merge |
| `autofahren` | `Autofahren` | 583 | review: merge |
| `details` | `Detail` | 582 | review: merge |
| `Historisch` | `historisch` | 579 | review: merge |
| `Objektive` | `Objektiv` | 576 | review: merge |
| `Schreie` | `Schrei` | 574 | review: merge |
| `ai` | `AI` | 566 | review: merge |
| `Pulse` | `Puls` | 565 | review: merge |
| `Lang` | `lang` | 564 | review: merge |
| `Graphen` | `Graph` | 559 | review: merge |
| `Griechische` | `Griechisch` | 554 | review: merge |
| `Lippenstifte` | `Lippenstift` | 550 | review: merge |
| `penis` | `Penis` | 549 | review: merge |
| `Rotweine` | `Rotwein` | 547 | review: merge |
| `Spanische` | `Spanisch` | 545 | review: merge |
| `Vegane` | `vegan` | 542 | review: merge |
| `Whirlpools` | `Whirlpool` | 540 | review: merge |
| `Puzzles` | `Puzzle` | 539 | review: merge |
| `schmerz` | `Schmerz` | 538 | review: merge |
| `Verweisen` | `Verweis` | 533 | review: merge |
| `ggmbH` | `gGmbH` | 533 | review: merge |
| `Dampfen` | `dampfen` | 532 | review: merge |
| `KMUs` | `KMU` | 532 | review: merge |
| `Veränderungsprozesse` | `Veränderungsprozess` | 528 | review: merge |
| `Bundesamts` | `Bundesamt` | 526 | review: merge |
| `Hämorrhoiden` | `Hämorrhoide` | 524 | review: merge |
| `Zertifiziert` | `zertifiziert` | 524 | review: merge |
| `Produktionsprozesse` | `Produktionsprozess` | 519 | review: merge |
| `Verbinden` | `verbinden` | 517 | review: merge |
| `Japanische` | `Japanisch` | 513 | review: merge |
| `davis` | `Davis` | 507 | review: merge |
| `Hotspots` | `Hotspot` | 505 | review: merge |
| `PKWs` | `PKW` | 503 | review: merge |
| `Audits` | `Audit` | 501 | review: merge |
| `Hoodies` | `Hoodie` | 501 | review: merge |
| `Erweitern` | `erweitern` | 499 | review: merge |
| `Lagerbestände` | `Lagerbestand` | 495 | review: merge |
| `Tanke` | `tanken` | 495 | review: merge |
| `Gewänder` | `Gewand` | 493 | review: merge |
| `Schlafsäcke` | `Schlafsack` | 492 | review: merge |
| `Grosser` | `groß` | 490 | review: merge |
| `Huhu` | `huhu` | 487 | review: merge |
| `Neuerscheinungen` | `Neuerscheinung` | 487 | review: merge |
| `Livestreams` | `Livestream` | 486 | review: merge |
| `Öffentlich` | `öffentlich` | 486 | review: merge |
| `Gräbern` | `Grab` | 485 | review: merge |
| `Arbeitsprozesse` | `Arbeitsprozess` | 484 | review: merge |
| `Halb` | `halb` | 483 | review: merge |
| `Räucher` | `räuchern` | 480 | review: merge |
| `Slogans` | `Slogan` | 480 | review: merge |
| `Dienstleistern` | `Dienstleister` | 479 | review: merge |
| `Balladen` | `Ballade` | 478 | review: merge |
| `kurs` | `Kurs` | 478 | review: merge |
| `oz` | `Oz` | 478 | review: merge |
| `Balle` | `Ballen` | 477 | review: merge |
| `Derivate` | `Derivat` | 476 | review: merge |
| `Interessieren` | `interessieren` | 476 | review: merge |
| `Patente` | `Patent` | 474 | review: merge |
| `Staune` | `staunen` | 473 | review: merge |
| `Seltsam` | `seltsam` | 472 | review: merge |
| `Paneele` | `Paneel` | 471 | review: merge |
| `Kuscheln` | `kuscheln` | 468 | review: merge |
| `Solide` | `solide` | 468 | review: merge |
| `Horden` | `Horde` | 467 | review: merge |
| `Herausragend` | `herausragend` | 466 | review: merge |
| `Königreiche` | `Königreich` | 466 | review: merge |
| `Ausschließlich` | `ausschließlich` | 465 | review: merge |
| `Unfassbar` | `unfassbar` | 462 | review: merge |
| `Gesuche` | `Gesuch` | 460 | review: merge |
| `Heile` | `heilen` | 460 | review: merge |
| `Aufklebern` | `Aufkleber` | 459 | review: merge |
| `Bewerbe` | `Bewerb` | 458 | review: merge |
| `Geldscheine` | `Geldschein` | 458 | review: merge |
| `einkaufszentren` | `Einkaufszentrum` | 457 | review: merge |
| `Sicherheitslücken` | `Sicherheitslücke` | 456 | review: merge |
| `Preisnachlässe` | `Preisnachlass` | 455 | review: merge |
| `Sonnenuntergänge` | `Sonnenuntergang` | 455 | review: merge |
| `Gewiss` | `gewiss` | 454 | review: merge |
| `Sinnvoll` | `sinnvoll` | 454 | review: merge |
| `Probieren` | `probieren` | 453 | review: merge |
| `Qualitativ` | `qualitativ` | 453 | review: merge |
| `Ratschläge` | `Ratschlag` | 453 | review: merge |
| `Moduls` | `Modul` | 451 | review: merge |
| `Wichtig` | `wichtig` | 451 | review: merge |
| `Weißweine` | `Weißwein` | 450 | review: merge |
| `Messestände` | `Messestand` | 449 | review: merge |
| `Wehre` | `Wehr` | 449 | review: merge |
| `gb` | `GB` | 445 | review: merge |
| `Ferienunterkünfte` | `Ferienunterkunft` | 444 | review: merge |
| `Konstrukteure` | `Konstrukteur` | 443 | review: merge |
| `Poloshirts` | `Poloshirt` | 443 | review: merge |
| `Dashboards` | `Dashboard` | 442 | review: merge |
| `Balke` | `Balken` | 441 | review: merge |
| `Anhalte` | `anhalten` | 439 | review: merge |
| `Denkweisen` | `Denkweise` | 438 | review: merge |
| `Bedarfe` | `Bedarf` | 437 | review: merge |
| `Altenheime` | `Altenheim` | 435 | review: merge |
| `Spielotheke` | `Spielothek` | 432 | review: merge |
| `Ausbildungsberufe` | `Ausbildungsberuf` | 427 | review: merge |
| `Smileys` | `Smiley` | 427 | review: merge |
| `Stadträte` | `Stadtrat` | 427 | review: merge |
| `Innovativ` | `innovativ` | 423 | review: merge |
| `Superfoods` | `Superfood` | 422 | review: merge |
| `Urlaubsreisen` | `Urlaubsreise` | 421 | review: merge |
| `Wollen` | `wollen` | 421 | review: merge |
| `Baumstämme` | `Baumstamm` | 419 | review: merge |
| `Buchs` | `Buchse` | 419 | review: merge |
| `Teilnahmeberechtigt` | `teilnahmeberechtigt` | 419 | review: merge |
| `q` | `Q` | 419 | review: merge |
| `Lande` | `landen` | 417 | review: merge |
| `Leckerlis` | `Leckerli` | 417 | review: merge |
| `basiswissen` | `Basiswissen` | 417 | review: merge |
| `Jugendämter` | `Jugendamt` | 416 | review: merge |
| `zunge` | `Zunge` | 416 | review: merge |
| `Hochwertig` | `hochwertig` | 415 | review: merge |
| `Reisemobile` | `Reisemobil` | 412 | review: merge |
| `Entscheidungsprozesse` | `Entscheidungsprozess` | 410 | review: merge |
| `Hande` | `Hand` | 410 | review: merge |
| `Revolutionäre` | `Revolutionär` | 410 | review: merge |
| `Geldgebern` | `Geldgeber` | 409 | review: merge |
| `Synonyme` | `Synonym` | 407 | review: merge |
| `Persönliche` | `persönlich` | 402 | review: merge |
| `Dritten` | `drittens` | 400 | review: merge |
| `Faire` | `fair` | 400 | review: merge |
| `Gehölze` | `Gehölz` | 400 | review: merge |
| `Sichtweisen` | `Sichtweise` | 399 | review: merge |
| `Diebstähle` | `Diebstahl` | 398 | review: merge |
| `Fahren` | `fahren` | 397 | review: merge |
| `Spielen` | `spielen` | 397 | review: merge |
| `walther` | `Walther` | 397 | review: merge |
| `Wegen` | `wegen` | 396 | review: merge |
| `Heut` | `heute` | 394 | review: merge |
| `Pellets` | `Pellet` | 394 | review: merge |
| `Wünsch` | `wünschen` | 393 | review: merge |
| `Reisen` | `reisen` | 392 | review: merge |
| `Jahresabschlüsse` | `Jahresabschluss` | 391 | review: merge |
| `Hübsch` | `hübsch` | 390 | review: merge |
| `erspart` | `Ersparte` | 390 | review: merge |
| `Langlaufen` | `langlaufen` | 389 | review: merge |
| `Schilde` | `Schild` | 388 | review: merge |
| `Playliste` | `Playlist` | 386 | review: merge |
| `Beete` | `Beet` | 385 | review: merge |
| `Äußerlich` | `äußerlich` | 384 | review: merge |
| `Ärgerlich` | `ärgerlich` | 381 | review: merge |
| `Tannen` | `Tanne` | 380 | review: merge |
| `kw` | `kW` | 380 | review: merge |
| `Jedesmal` | `jedesmal` | 379 | review: merge |
| `demo` | `Demo` | 377 | review: merge |
| `Bellen` | `bellen` | 376 | review: merge |
| `Übertrage` | `übertragen` | 376 | review: merge |
| `Farbtöne` | `Farbton` | 375 | review: merge |
| `Schwärme` | `Schwarm` | 374 | review: merge |
| `cent` | `Cent` | 374 | review: merge |
| `Sommerabende` | `Sommerabend` | 373 | review: merge |
| `Geschosse` | `Geschoss` | 372 | review: merge |
| `Wirtschafts` | `Wirtschaft` | 372 | review: merge |
| `Anbringen` | `anbringen` | 369 | review: merge |
| `Gesunde` | `gesund` | 369 | review: merge |
| `Talkshows` | `Talkshow` | 369 | review: merge |
| `Trau` | `trauen` | 369 | review: merge |
| `xy` | `XY` | 369 | review: merge |
| `Ergebniss` | `Ergebnis` | 368 | review: merge |
| `Finanziell` | `finanziell` | 367 | review: merge |
| `mb` | `MB` | 367 | review: merge |
| `Lecke` | `lecken` | 366 | review: merge |
| `Demnächst` | `demnächst` | 365 | review: merge |
| `Löte` | `löten` | 365 | review: merge |
| `Verstecke` | `Versteck` | 365 | review: merge |
| `auerdem` | `außerdem` | 365 | review: merge |
| `Ödeme` | `Ödem` | 363 | review: merge |
| `Brokern` | `Broker` | 362 | review: merge |
| `Mamis` | `Mami` | 361 | review: merge |
| `Diagramme` | `Diagramm` | 360 | review: merge |
| `amen` | `Amen` | 360 | review: merge |
| `hopfen` | `Hopfen` | 360 | review: merge |
| `Fraglich` | `fraglich` | 357 | review: merge |
| `Zaubern` | `zaubern` | 356 | review: merge |
| `Pioniere` | `Pionier` | 355 | review: merge |
| `Lattenroste` | `Lattenrost` | 354 | review: merge |
| `Antifas` | `Antifa` | 353 | review: merge |
| `Importeure` | `Importeur` | 353 | review: merge |
| `Regionale` | `regional` | 353 | review: merge |
| `Bauen` | `bauen` | 352 | review: merge |
| `Pseudonyme` | `Pseudonym` | 352 | review: merge |
| `würstchen` | `Würstchen` | 352 | review: merge |
| `Ökologisch` | `ökologisch` | 352 | review: merge |
| `Deiche` | `Deich` | 351 | review: merge |
| `Mixen` | `mixen` | 350 | review: merge |
| `Eigelbe` | `Eigelb` | 349 | review: merge |
| `Elternabende` | `Elternabend` | 348 | review: merge |
| `Auslandsaufenthalte` | `Auslandsaufenthalt` | 347 | review: merge |
| `Treffe` | `Treffen` | 347 | review: merge |
| `hefe` | `Hefe` | 346 | review: merge |
| `pr` | `PR` | 344 | review: merge |
| `Elektronische` | `elektronisch` | 343 | review: merge |
| `Herzlichst` | `herzlichst` | 343 | review: merge |
| `Tragegriffe` | `Tragegriff` | 343 | review: merge |
| `Vllt` | `vielleicht` | 342 | review: merge |
| `Kupplunge` | `Kupplung` | 341 | review: merge |
| `Rassisten` | `Rassist` | 341 | review: merge |
| `Stickern` | `Sticker` | 341 | review: merge |
| `winter` | `Winter` | 339 | review: merge |
| `Datenbestände` | `Datenbestand` | 337 | review: merge |
| `Süsse` | `süß` | 337 | review: merge |
| `Widgets` | `Widget` | 337 | review: merge |
| `Sorgfältig` | `sorgfältig` | 336 | review: merge |
| `Wraps` | `Wrap` | 336 | review: merge |
| `Dokus` | `Doku` | 335 | review: merge |
| `Erfolgreich` | `erfolgreich` | 334 | review: merge |
| `Blutgefäßen` | `Blutgefäß` | 333 | review: merge |
| `Gatten` | `Gatte` | 333 | review: merge |
| `Wärmepumpen` | `Wärmepumpe` | 333 | review: merge |
| `Dekore` | `Dekor` | 332 | review: merge |
| `Euronen` | `Euro` | 332 | review: merge |
| `Circa` | `circa` | 331 | review: merge |
| `Glätten` | `glätten` | 331 | review: merge |
| `Hochdeutsche` | `hochdeutsch` | 331 | review: merge |
| `Wettervorhersag` | `Wettervorhersage` | 329 | review: merge |
| `kids` | `Kid` | 329 | review: merge |
| `Ableg` | `ablegen` | 328 | review: merge |
| `dresd` | `Dresden` | 328 | review: merge |
| `gestres` | `gestresst` | 328 | review: merge |
| `Anfertig` | `anfertigen` | 327 | review: merge |
| `Sneakers` | `Sneaker` | 327 | review: merge |
| `füreinan` | `füreinander` | 326 | review: merge |
| `BLOG` | `Blog` | 325 | review: merge |
| `institutionalisiere` | `institutionalisieren` | 325 | review: merge |
| `Silhouett` | `Silhouette` | 324 | review: merge |
| `FOTO` | `Foto` | 323 | review: merge |
| `Wassereinlagerunge` | `Wassereinlagerung` | 323 | review: merge |
| `Zäpfche` | `Zäpfchen` | 323 | review: merge |
| `Intensivpfleg` | `Intensivpflege` | 322 | review: merge |
| `Lebensgemeinschafte` | `Lebensgemeinschaft` | 322 | review: merge |
| `Rollenspiele` | `Rollenspiel` | 322 | review: merge |
| `Verschwörungstheorien` | `Verschwörungstheorie` | 322 | review: merge |
| `WERBUNG` | `Werbung` | 321 | review: merge |
| `Audiodat` | `Audiodaten` | 320 | review: merge |
| `Aufzeichn` | `aufzeichnen` | 320 | review: merge |
| `GESUNDHEIT` | `Gesundheit` | 320 | review: merge |
| `MitarbeiterInn` | `Mitarbeiter` | 320 | review: merge |
| `Scene` | `Szene` | 320 | review: merge |
| `Werbeeinblendunge` | `Werbeeinblendung` | 320 | review: merge |
| `Agier` | `agieren` | 319 | review: merge |
| `Malerarbeite` | `Malerarbeit` | 319 | review: merge |
| `NATUR` | `Natur` | 319 | review: merge |
| `ROCK` | `Rock` | 319 | review: merge |
| `filmtabletten` | `Filmtablette` | 319 | review: merge |
| `klaren` | `klar` | 319 | review: merge |
| `ÜBERBLICK` | `Überblick` | 319 | review: merge |
| `Augencrem` | `Augencreme` | 318 | review: merge |
| `CASINO` | `Casino` | 318 | review: merge |
| `Usa` | `USA` | 318 | review: merge |
| `up-to-dat` | `up-to-date` | 318 | review: merge |
| `Fantastisch` | `fantastisch` | 317 | review: merge |
| `HIT` | `Hit` | 317 | review: merge |
| `KUNDEN` | `Kunde` | 317 | review: merge |
| `Verhandel` | `verhandeln` | 317 | review: merge |
| `sprüch` | `Spruch` | 317 | review: merge |
| `BLICK` | `Blick` | 316 | review: merge |
| `Fettnäpfche` | `Fettnäpfchen` | 316 | review: merge |
| `Kunterbunt` | `kunterbunt` | 316 | review: merge |
| `Sardinie` | `Sardinien` | 316 | review: merge |
| `amtsblatt` | `Amtsblatt` | 316 | review: merge |
| `FINDEN` | `finden` | 315 | review: merge |
| `maßgeben` | `maßgebend` | 315 | review: merge |
| `Bauspare` | `Bausparen` | 314 | review: merge |
| `Gewinnerinn` | `Gewinnerin` | 314 | review: merge |
| `Hängeleucht` | `Hängeleuchte` | 314 | review: merge |
| `Nebenan` | `nebenan` | 314 | review: merge |
| `allerhöch` | `allerhöchst` | 314 | review: merge |
| `schwin` | `schwinden` | 314 | review: merge |
| `ESSEN` | `Essen` | 313 | review: merge |
| `Gläsche` | `Gläschen` | 313 | review: merge |
| `Kerzenstände` | `Kerzenständer` | 313 | review: merge |
| `Nistkast` | `Nistkasten` | 313 | review: merge |
| `Rundfunkanstalte` | `Rundfunkanstalt` | 313 | review: merge |
| `Sandstränd` | `Sandstrand` | 313 | review: merge |
| `Zahncrem` | `Zahncreme` | 313 | review: merge |
| `excellent` | `exzellent` | 313 | review: merge |
| `meinerein` | `meinereiner` | 313 | review: merge |
| `Affiliate-Links` | `Affiliate-Link` | 312 | review: merge |
| `Glöckche` | `Glöckchen` | 312 | review: merge |
| `Messlatt` | `Messlatte` | 312 | review: merge |
| `VORTEILE` | `Vorteil` | 312 | review: merge |
| `Angepasst` | `angepasst` | 311 | review: merge |
| `E-Bik` | `E-Bike` | 311 | review: merge |
| `Textstell` | `Textstelle` | 311 | review: merge |
| `lack` | `Lack` | 311 | review: merge |
| `ENERGIE` | `Energie` | 310 | review: merge |
| `Mdche` | `Mädchen` | 310 | review: merge |
| `anfäng` | `Anfänger` | 310 | review: merge |
| `held` | `Held` | 310 | review: merge |
| `Abdicht` | `abdichten` | 309 | review: merge |
| `DOCH` | `doch` | 309 | review: merge |
| `Druckerpatron` | `Druckerpatrone` | 309 | review: merge |
| `Dörr` | `dörren` | 309 | review: merge |
| `GPS-Dat` | `GPS-Daten` | 309 | review: merge |
| `Jasminute` | `Jasmin` | 309 | review: merge |
| `Laboruntersuchunge` | `Laboruntersuchung` | 309 | review: merge |
| `Lesenswert` | `lesenswert` | 309 | review: merge |
| `SONNTAG` | `Sonntag` | 309 | review: merge |
| `marktführen` | `marktführend` | 309 | review: merge |
| `Getaggt` | `taggen` | 308 | review: merge |
| `SOFTWARE` | `Software` | 308 | review: merge |
| `STOP` | `Stopp` | 308 | review: merge |
| `Suchbegriffe` | `Suchbegriff` | 308 | review: merge |
| `fachübergreifen` | `fachübergreifend` | 308 | review: merge |
| `Aktienfond` | `Aktienfonds` | 307 | review: merge |
| `Aktivistinn` | `Aktivistin` | 307 | review: merge |
| `Denkspiele` | `Denkspiel` | 307 | review: merge |
| `Nachkoch` | `nachkochen` | 307 | review: merge |
| `Parkfläch` | `Parkfläche` | 307 | review: merge |
| `Äusserunge` | `Äußerung` | 307 | review: merge |
| `Kündigungsschreibe` | `Kündigungsschreiben` | 306 | review: merge |
| `gebrauchtwar` | `Gebrauchtware` | 306 | review: merge |
| `ArbeiterInne` | `Arbeiter` | 305 | review: merge |
| `Chilischot` | `Chilischote` | 305 | review: merge |
| `Edelweiss` | `Edelweiß` | 305 | review: merge |
| `Erfreulicherweis` | `erfreulicherweise` | 305 | review: merge |
| `Gelenkbeschwerde` | `Gelenkbeschwerden` | 305 | review: merge |
| `Gebietskörperschafte` | `Gebietskörperschaft` | 304 | review: merge |
| `Nasenblut` | `Nasenbluten` | 304 | review: merge |
| `Bändche` | `Bändchen` | 303 | review: merge |
| `Fellpfleg` | `Fellpflege` | 303 | review: merge |
| `Kurzerhand` | `kurzerhand` | 303 | review: merge |
| `Naturgewalte` | `Naturgewalt` | 303 | review: merge |
| `Unwägbarkeite` | `Unwägbarkeit` | 303 | review: merge |
| `ZOOM` | `Zoom` | 303 | review: merge |
| `teenag` | `Teenager` | 303 | review: merge |
| `ALT` | `alt` | 302 | review: merge |
| `scroll` | `scrollen` | 302 | review: merge |
| `BEIM` | `beim` | 301 | review: merge |
| `Halbe` | `halb` | 301 | review: merge |
| `TVs` | `TV` | 301 | review: merge |
| `Zusammenstell` | `zusammenstellen` | 301 | review: merge |
| `Badeseen` | `Badesee` | 300 | review: merge |
| `Landeszentral` | `Landeszentrale` | 300 | review: merge |
| `loszuwer` | `loswerden` | 300 | review: merge |
| `Brilliant` | `Brillant` | 299 | review: merge |
| `FAZIT` | `Fazit` | 299 | review: merge |
| `Innengewind` | `Innengewinde` | 299 | review: merge |
| `Juniorinn` | `Juniorin` | 299 | review: merge |
| `KUNST` | `Kunst` | 299 | review: merge |
| `KURIER` | `Kurier` | 299 | review: merge |
| `Vans` | `Van` | 299 | review: merge |
| `schwänz` | `Schwanz` | 299 | review: merge |
| `Bürgerinitiativen` | `Bürgerinitiative` | 298 | review: merge |
| `ERFOLG` | `Erfolg` | 298 | review: merge |
| `FREIE` | `frei` | 298 | review: merge |
| `GEMEINSAM` | `gemeinsam` | 298 | review: merge |
| `Meßgerät` | `Messgerät` | 298 | review: merge |
| `innenliegen` | `innenliegend` | 298 | review: merge |
| `Betriebsstätt` | `Betriebsstätte` | 297 | review: merge |
| `Gateways` | `Gateway` | 297 | review: merge |
| `Login-Dat` | `Login-Daten` | 297 | review: merge |
| `Stöckche` | `Stöckchen` | 297 | review: merge |
| `Tapes` | `Tape` | 297 | review: merge |
| `Hiernach` | `hiernach` | 296 | review: merge |
| `Komischerweis` | `komischerweise` | 296 | review: merge |
| `Wasserschäden` | `Wasserschaden` | 296 | review: merge |
| `erfas` | `erfassen` | 296 | review: merge |
| `i-Tüpfelch` | `i-Tüpfelchen` | 296 | review: merge |
| `Bäumche` | `Bäumchen` | 295 | review: merge |
| `Hochzeitsreportag` | `Hochzeitsreportage` | 295 | review: merge |
| `INS` | `in` | 295 | review: merge |
| `Livewett` | `Livewette` | 295 | review: merge |
| `Gentleme` | `Gentleman` | 294 | review: merge |
| `SEHEN` | `sehen` | 294 | review: merge |
| `Treppche` | `Treppchen` | 294 | review: merge |
| `UNI` | `Uni` | 294 | review: merge |
| `darnach` | `danach` | 294 | review: merge |
| `vormach` | `vormachen` | 294 | review: merge |
| `Hilfslinien` | `Hilfslinie` | 293 | review: merge |
| `MITMACHEN` | `mitmachen` | 293 | review: merge |
| `MÖGLICH` | `möglich` | 293 | review: merge |
| `WANN` | `wann` | 293 | review: merge |
| `wahlberechtigen` | `wahlberechtigt` | 293 | review: merge |
| `BERATUNG` | `Beratung` | 292 | review: merge |
| `KLEINE` | `klein` | 292 | review: merge |
| `VERSAND` | `Versand` | 292 | review: merge |
| `Wetterdat` | `Wetterdaten` | 292 | review: merge |
| `Antioxidan` | `Antioxidans` | 291 | review: merge |
| `Gastriti` | `Gastritis` | 291 | review: merge |
| `Keinesfall` | `keinesfalls` | 291 | review: merge |
| `Problemch` | `Problemchen` | 291 | review: merge |
| `Verbindungsdat` | `Verbindungsdaten` | 291 | review: merge |
| `vorsitzend` | `Vorsitzende` | 291 | review: merge |
| `Aufspür` | `aufspüren` | 290 | review: merge |
| `Erdbeer` | `Erdbeere` | 290 | review: merge |
| `Kleidche` | `Kleidchen` | 290 | review: merge |
| `Motivationsschreibe` | `Motivationsschreiben` | 290 | review: merge |
| `Südost` | `Südosten` | 290 | review: merge |
| `Tauziehe` | `Tauziehen` | 290 | review: merge |
| `Verhaltensauffälligkeite` | `Verhaltensauffälligkeit` | 290 | review: merge |
| `Villas` | `Villa` | 290 | review: merge |
| `FRAU` | `Frau` | 289 | review: merge |
| `Lichtstrahle` | `Lichtstrahl` | 289 | review: merge |
| `Mecklenburg-Vorpommerns` | `Mecklenburg-Vorpommern` | 289 | review: merge |
| `Protokolldat` | `Protokolldaten` | 289 | review: merge |
| `ANWENDER` | `Anwender` | 288 | review: merge |
| `Kantat` | `Kantate` | 288 | review: merge |
| `Pauschal` | `pauschal` | 288 | review: merge |
| `Plastike` | `Plastik` | 288 | review: merge |
| `Wohlfahrtspfleg` | `Wohlfahrtspflege` | 288 | review: merge |
| `FAST` | `fast` | 287 | review: merge |
| `Kurzzeitpfleg` | `Kurzzeitpflege` | 287 | review: merge |
| `POP` | `Pop` | 287 | review: merge |
| `WEISS` | `weiß` | 287 | review: merge |
| `Auflös` | `auflösen` | 286 | review: merge |
| `Ausbildungsstell` | `Ausbildungsstelle` | 286 | review: merge |
| `Buttercrem` | `Buttercreme` | 286 | review: merge |
| `PolitikerInn` | `Politiker` | 286 | review: merge |
| `zielführen` | `zielführend` | 286 | review: merge |
| `Bierhef` | `Bierhefe` | 285 | review: merge |
| `Bloggerinne` | `Bloggerin` | 285 | review: merge |
| `Existenzgründunge` | `Existenzgründung` | 285 | review: merge |
| `Ohrenschmerz` | `Ohrenschmerzen` | 285 | review: merge |
| `Satte` | `satt` | 285 | review: merge |
| `TIPPS` | `Tipp` | 285 | review: merge |
| `Beraterinne` | `Beraterin` | 284 | review: merge |
| `Durchblatt` | `durchblättern` | 284 | review: merge |
| `Fahrzeugdat` | `Fahrzeugdaten` | 284 | review: merge |
| `AKTUELL` | `aktuell` | 283 | review: merge |
| `Behandlungspfleg` | `Behandlungspflege` | 283 | review: merge |
| `Eckdate` | `Eckdaten` | 283 | review: merge |
| `Freitagmorg` | `Freitagmorgen` | 283 | review: merge |
| `Kernbuch` | `Kernbuche` | 283 | review: merge |
| `Samples` | `Sample` | 283 | review: merge |
| `Seepferdche` | `Seepferdchen` | 283 | review: merge |
| `Sicherheitsfrag` | `Sicherheitsfrage` | 283 | review: merge |
| `these` | `These` | 283 | review: merge |
| `AHA` | `aha` | 282 | review: merge |
| `ANGEBOT` | `Angebot` | 282 | review: merge |
| `Antihistaminika` | `Antihistaminikum` | 282 | review: merge |
| `Blu-rays` | `Blu-ray` | 282 | review: merge |
| `Eu` | `EU` | 282 | review: merge |
| `FREIHEIT` | `Freiheit` | 282 | review: merge |
| `NAME` | `Name` | 282 | review: merge |
| `Quäntche` | `Quäntchen` | 282 | review: merge |
| `ABO` | `Abo` | 281 | review: merge |
| `Blumentöpf` | `Blumentopf` | 281 | review: merge |
| `Östrog` | `Östrogen` | 281 | review: merge |
| `Ausbildungsstätt` | `Ausbildungsstätte` | 280 | review: merge |
| `ENDE` | `Ende` | 280 | review: merge |
| `Firmendat` | `Firmendaten` | 280 | review: merge |
| `GENAU` | `genau` | 279 | review: merge |
| `Girland` | `Girlande` | 279 | review: merge |
| `Idealerweis` | `idealerweise` | 279 | review: merge |
| `Karrierechancen` | `Karrierechance` | 279 | review: merge |
| `Taktrat` | `Taktrate` | 279 | review: merge |
| `Webservices` | `Webservice` | 279 | review: merge |
| `Wirtschaftsjuniore` | `Wirtschaftsjunior` | 279 | review: merge |
| `verdünn` | `verdünnen` | 279 | review: merge |
| `BUCHEN` | `buchen` | 278 | review: merge |
| `Grün-weiß` | `grün-weiß` | 278 | review: merge |
| `HANNOVER` | `Hannover` | 278 | review: merge |
| `Hitzewallunge` | `Hitzewallung` | 278 | review: merge |
| `POST` | `Post` | 278 | review: merge |
| `Stehleucht` | `Stehleuchte` | 278 | review: merge |
| `Diplome` | `Diplom` | 277 | review: merge |
| `Geldverdien` | `Geldverdienen` | 277 | review: merge |
| `Optimier` | `optimieren` | 277 | review: merge |
| `Ponyreit` | `Ponyreiten` | 277 | review: merge |
| `ROT` | `rot` | 277 | review: merge |
| `Abtaste` | `abtasten` | 276 | review: merge |
| `Aufnehm` | `aufnehmen` | 276 | review: merge |
| `EINFÜHRUNG` | `Einführung` | 276 | review: merge |
| `Forscherinn` | `Forscherin` | 276 | review: merge |
| `Gastgeberinne` | `Gastgeberin` | 276 | review: merge |
| `Kehren` | `kehren` | 276 | review: merge |
| `PRAXIS` | `Praxis` | 276 | review: merge |
| `Rasenfläch` | `Rasenfläche` | 276 | review: merge |
| `STERN` | `Stern` | 276 | review: merge |
| `Styliste` | `Stylist` | 276 | review: merge |
| `Zuallererst` | `zuallererst` | 276 | review: merge |
| `DUO` | `Duo` | 275 | review: merge |
| `FRAUEN` | `Frau` | 275 | review: merge |
| `Fahnenstang` | `Fahnenstange` | 275 | review: merge |
| `Kräftemesse` | `Kräftemessen` | 275 | review: merge |
| `LICHT` | `Licht` | 275 | review: merge |
| `Regatt` | `Regatta` | 275 | review: merge |
| `Röhrch` | `Röhrchen` | 275 | review: merge |
| `blinde` | `blind` | 300 | review: merge |
| `geleakt` | `leaken` | 300 | review: merge |
| `handumdreh` | `Handumdrehen` | 300 | review: merge |
| `himmel` | `Himmel` | 300 | review: merge |
| `personen` | `Person` | 300 | review: merge |
| `umrundet` | `umrunden` | 300 | review: merge |
| `Bd` | `Band` | 299 | review: merge |
| `Rechtsakte` | `Rechtsakt` | 299 | review: merge |
| `ausschliessen` | `ausschließen` | 299 | review: merge |
| `effekt` | `Effekt` | 299 | review: merge |
| `frühstück` | `Frühstück` | 299 | review: merge |
| `girocard` | `Girocard` | 299 | review: merge |
| `losgefahren` | `losfahren` | 299 | review: merge |
| `persoenlich` | `persönlich` | 299 | review: merge |
| `vintag` | `vintage` | 299 | review: merge |
| `weitern` | `weiter` | 299 | review: merge |
| `Definiere` | `definieren` | 298 | review: merge |
| `Dien` | `dienen` | 298 | review: merge |
| `Gleichgesinnt` | `gleichgesinnt` | 298 | review: merge |
| `Modellier` | `modellieren` | 298 | review: merge |
| `Niedrig` | `niedrig` | 298 | review: merge |
| `Ran` | `heran` | 298 | review: merge |
| `Rechtsbehelfe` | `Rechtsbehelf` | 298 | review: merge |
| `Shak` | `Shake` | 298 | review: merge |
| `funktionsstörungen` | `Funktionsstörung` | 298 | review: merge |
| `miete` | `mieten` | 298 | review: merge |
| `minut` | `Minute` | 298 | review: merge |
| `saft` | `Saft` | 298 | review: merge |
| `Attraktiv` | `attraktiv` | 297 | review: merge |
| `Fliegende` | `fliegend` | 297 | review: merge |
| `Handgefertigt` | `handgefertigt` | 297 | review: merge |
| `Weihnachtsgrüße` | `Weihnachtsgruß` | 297 | review: merge |
| `dutzen` | `Dutzend` | 297 | review: merge |
| `garkein` | `kein` | 297 | review: merge |
| `geeignetsten` | `geeignet` | 297 | review: merge |
| `verlässlicher` | `verlässlich` | 297 | review: merge |
| `Durchhalte` | `durchhalten` | 296 | review: merge |
| `Glückliche` | `glücklich` | 296 | review: merge |
| `Knochenbrüche` | `Knochenbruch` | 296 | review: merge |
| `Osteopathen` | `Osteopath` | 296 | review: merge |
| `Sehen` | `sehen` | 296 | review: merge |
| `Thais` | `Thai` | 296 | review: merge |
| `Wässer` | `Wasser` | 296 | review: merge |
| `abstand` | `Abstand` | 296 | review: merge |
| `aloe` | `Aloe` | 296 | review: merge |
| `blockt` | `blocken` | 296 | review: merge |
| `chef` | `Chef` | 296 | review: merge |
| `deckel` | `Deckel` | 296 | review: merge |
| `diesesmal` | `diesmal` | 296 | review: merge |
| `konzept` | `Konzept` | 296 | review: merge |
| `letztemal` | `Mal` | 296 | review: merge |
| `lückenlosen` | `lückenlos` | 296 | review: merge |
| `vergoren` | `vergären` | 296 | review: merge |
| `videokonferenzen` | `Videokonferenz` | 296 | review: merge |
| `Eidg` | `eidgenössisch` | 295 | review: merge |
| `Staubsauge` | `staubsaugen` | 295 | review: merge |
| `Wetterfest` | `wetterfest` | 295 | review: merge |
| `auszahlung` | `Auszahlung` | 295 | review: merge |
| `bekannten` | `bekannt` | 295 | review: merge |
| `duell` | `Duell` | 295 | review: merge |
| `hoffnung` | `Hoffnung` | 295 | review: merge |
| `MARKETING` | `Marketing` | 294 | review: merge |
| `Netzbetreibern` | `Netzbetreiber` | 294 | review: merge |
| `Scirocco` | `Schirokko` | 294 | review: merge |
| `Vergleichbar` | `vergleichbar` | 294 | review: merge |
| `Wm` | `WM` | 294 | review: merge |
| `aue` | `Aue` | 294 | review: merge |
| `delux` | `deluxe` | 294 | review: merge |
| `generation` | `Generation` | 294 | review: merge |
| `Darstellende` | `darstellend` | 293 | review: merge |
| `Freiheitliche` | `freiheitlich` | 293 | review: merge |
| `Kakerlaken` | `Kakerlake` | 293 | review: merge |
| `Leit` | `leiten` | 293 | review: merge |
| `Qualitt` | `Qualität` | 293 | review: merge |
| `Reiß` | `reißen` | 293 | review: merge |
| `Schultergurte` | `Schultergurt` | 293 | review: merge |
| `beeinflussten` | `beeinflussen` | 293 | review: merge |
| `benutz` | `benutzen` | 293 | review: merge |
| `binäre` | `binär` | 293 | review: merge |
| `händl` | `Händler` | 293 | review: merge |
| `inspiration` | `Inspiration` | 293 | review: merge |
| `sonde` | `Sonde` | 293 | review: merge |
| `Berate` | `beraten` | 292 | review: merge |
| `Bespiel` | `Beispiel` | 292 | review: merge |
| `Buß` | `Buße` | 292 | review: merge |
| `Fachspezifische` | `fachspezifisch` | 292 | review: merge |
| `Kürz` | `kürzen` | 292 | review: merge |
| `Pazifische` | `pazifisch` | 292 | review: merge |
| `Reagier` | `reagieren` | 292 | review: merge |
| `Relevant` | `relevant` | 292 | review: merge |
| `coloriert` | `kolorieren` | 292 | review: merge |
| `element` | `Element` | 292 | review: merge |
| `grenzend` | `grenzen` | 292 | review: merge |
| `herauszufordern` | `herausfordern` | 292 | review: merge |
| `männern` | `Mann` | 292 | review: merge |
| `märchenhafte` | `märchenhaft` | 292 | review: merge |
| `parallele` | `parallel` | 292 | review: merge |
| `zähne` | `Zahn` | 292 | review: merge |
| `Öbung` | `Übung` | 292 | review: merge |
| `Einpark` | `einparken` | 291 | review: merge |
| `Elektrisch` | `elektrisch` | 291 | review: merge |
| `Happ` | `Happen` | 291 | review: merge |
| `Leckerlie` | `Leckerli` | 291 | review: merge |
| `Montier` | `montieren` | 291 | review: merge |
| `Stellvertretend` | `stellvertretend` | 291 | review: merge |
| `Tränensäcke` | `Tränensack` | 291 | review: merge |
| `UnternehmenMehr` | `Unternehmen` | 291 | review: merge |
| `Vieleicht` | `vielleicht` | 291 | review: merge |
| `schrank` | `Schrank` | 291 | review: merge |
| `shirt` | `Shirt` | 291 | review: merge |
| `versierter` | `versiert` | 291 | review: merge |
| `Hhe` | `Höhe` | 290 | review: merge |
| `Klettersteige` | `Klettersteig` | 290 | review: merge |
| `Liefer` | `liefern` | 290 | review: merge |
| `Mehrfach` | `mehrfach` | 290 | review: merge |
| `aufgezeigt` | `aufzeigen` | 290 | review: merge |
| `prägnante` | `prägnant` | 290 | review: merge |
| `Blinke` | `blinken` | 289 | review: merge |
| `Kannen` | `Kanne` | 289 | review: merge |
| `Strandkörbe` | `Strandkorb` | 289 | review: merge |
| `abzuschliessen` | `abschließen` | 289 | review: merge |
| `batterie` | `Batterie` | 289 | review: merge |
| `brillanter` | `brillant` | 289 | review: merge |
| `daumen` | `Daumen` | 289 | review: merge |
| `grafik` | `Grafik` | 289 | review: merge |
| `mitfinanziert` | `mitfinanzieren` | 289 | review: merge |
| `stuhl` | `Stuhl` | 289 | review: merge |
| `vollzogen` | `vollziehen` | 289 | review: merge |
| `Freiwillig` | `freiwillig` | 288 | review: merge |
| `Heiligtümer` | `Heiligtum` | 288 | review: merge |
| `Pseudonyms` | `Pseudonym` | 288 | review: merge |
| `Psychologische` | `psychologisch` | 288 | review: merge |
| `bestenfall` | `bestenfalls` | 288 | review: merge |
| `geklaut` | `klauen` | 288 | review: merge |
| `gerät` | `Gerät` | 288 | review: merge |
| `geschäftsbereich` | `Geschäftsbereich` | 288 | review: merge |
| `materialien` | `Material` | 288 | review: merge |
| `mitlerweil` | `mittlerweile` | 288 | review: merge |
| `steig` | `steigen` | 288 | review: merge |
| `wacher` | `wach` | 288 | review: merge |
| `wartend` | `warten` | 288 | review: merge |
| `Flaniere` | `flanieren` | 287 | review: merge |
| `Forschungsinstitute` | `Forschungsinstitut` | 287 | review: merge |
| `Klatschen` | `klatschen` | 287 | review: merge |
| `Lockerungen` | `Lockerung` | 287 | review: merge |
| `Mißverständnis` | `Missverständnis` | 287 | review: merge |
| `ausbreitend` | `ausbreiten` | 287 | review: merge |
| `diät` | `Diät` | 287 | review: merge |
| `fabriziert` | `fabrizieren` | 287 | review: merge |
| `parkplatz` | `Parkplatz` | 287 | review: merge |
| `rausgeholt` | `rausholen` | 287 | review: merge |
| `überweisung` | `Überweisung` | 287 | review: merge |
| `MO` | `Montag` | 286 | review: merge |
| `Verkaufen` | `verkaufen` | 286 | review: merge |
| `ausstellung` | `Ausstellung` | 286 | review: merge |
| `blaß` | `blass` | 286 | review: merge |
| `börsennotierte` | `börsennotiert` | 286 | review: merge |
| `draufsteht` | `draufstehen` | 286 | review: merge |
| `fachausweis` | `Fachausweis` | 286 | review: merge |
| `kundgetan` | `kundtun` | 286 | review: merge |
| `lebensmittel` | `Lebensmittel` | 286 | review: merge |
| `wüsstest` | `wissen` | 286 | review: merge |
| `Anspreche` | `ansprechen` | 285 | review: merge |
| `Berechn` | `berechnen` | 285 | review: merge |
| `Einnehmen` | `einnehmen` | 285 | review: merge |
| `Lsung` | `Lösung` | 285 | review: merge |
| `Mitbringen` | `mitbringen` | 285 | review: merge |
| `Vieren` | `Vier` | 285 | review: merge |
| `Wohlgemerkt` | `wohlgemerkt` | 285 | review: merge |
| `bedaure` | `bedauern` | 285 | review: merge |
| `bluetooth` | `Bluetooth` | 285 | review: merge |
| `button` | `Button` | 285 | review: merge |
| `charakter` | `Charakter` | 285 | review: merge |
| `ders` | `derselbe` | 285 | review: merge |
| `durchsagen` | `Durchsage` | 285 | review: merge |
| `erklär` | `erklären` | 285 | review: merge |
| `erlei` | `erleiden` | 285 | review: merge |
| `genehmigt` | `genehmigen` | 285 | review: merge |
| `neugestaltet` | `neugestalten` | 285 | review: merge |
| `verffentlicht` | `veröffentlichen` | 285 | review: merge |
| `Inhaltlich` | `inhaltlich` | 284 | review: merge |
| `Kopier` | `kopieren` | 284 | review: merge |
| `Krapf` | `Krapfen` | 284 | review: merge |
| `Paritätische` | `paritätisch` | 284 | review: merge |
| `ausgezahlt` | `auszahlen` | 284 | review: merge |
| `behandelnd` | `behandeln` | 284 | review: merge |
| `bier` | `Bier` | 284 | review: merge |
| `delegiert` | `Delegierte` | 284 | review: merge |
| `einnahmen` | `Einnahmen` | 284 | review: merge |
| `erpresst` | `erpressen` | 284 | review: merge |
| `jacke` | `Jacke` | 284 | review: merge |
| `verschliessen` | `verschließen` | 284 | review: merge |
| `vertretend` | `vertreten` | 284 | review: merge |
| `Bunte` | `bunt` | 283 | review: merge |
| `Matche` | `Match` | 283 | review: merge |
| `geheiligt` | `heiligen` | 283 | review: merge |
| `hingekommen` | `hinkommen` | 283 | review: merge |
| `rad` | `Rad` | 283 | review: merge |
| `schoene` | `schön` | 283 | review: merge |
| `vorgebracht` | `vorbringen` | 283 | review: merge |
| `werkzeug` | `Werkzeug` | 283 | review: merge |
| `Arbeitsgerichts` | `Arbeitsgericht` | 282 | review: merge |
| `Bergsteige` | `bergsteigen` | 282 | review: merge |
| `Garniere` | `garnieren` | 282 | review: merge |
| `Jahrzehntelang` | `jahrzehntelang` | 282 | review: merge |
| `Potenzielle` | `potenziell` | 282 | review: merge |
| `Unterstützende` | `unterstützen` | 282 | review: merge |
| `abgeschottet` | `abschotten` | 282 | review: merge |
| `anforderungen` | `Anforderung` | 282 | review: merge |
| `bezwang` | `bezwingen` | 282 | review: merge |
| `blos` | `bloß` | 282 | review: merge |
| `ensteht` | `entstehen` | 282 | review: merge |
| `farb` | `Farbe` | 282 | review: merge |
| `gespart` | `sparen` | 282 | review: merge |
| `werdende` | `werden` | 282 | review: merge |
| `Klöße` | `Kloß` | 281 | review: merge |
| `Personenbezogen` | `personenbezogen` | 281 | review: merge |
| `Spät` | `spät` | 281 | review: merge |
| `allerbeste` | `allerbest` | 281 | review: merge |
| `anzusteuern` | `ansteuern` | 281 | review: merge |
| `austria` | `Österreich` | 281 | review: merge |
| `garanti` | `Garantie` | 281 | review: merge |
| `norden` | `Norden` | 281 | review: merge |
| `schlaffen` | `schlaff` | 281 | review: merge |
| `verschrieben` | `verschreiben` | 281 | review: merge |
| `Ausnahmsweise` | `ausnahmsweise` | 280 | review: merge |
| `Bastel` | `basteln` | 280 | review: merge |
| `Hamburgische` | `hamburgisch` | 280 | review: merge |
| `Lipide` | `Lipid` | 280 | review: merge |
| `Reißverschlüssen` | `Reißverschluss` | 280 | review: merge |
| `Smilies` | `Smiley` | 280 | review: merge |
| `ain` | `ein` | 280 | review: merge |
| `gestapelt` | `stapeln` | 280 | review: merge |
| `wahrzeichen` | `Wahrzeichen` | 280 | review: merge |
| `zurückgelegt` | `zurücklegen` | 280 | review: merge |
| `Adaptive` | `adaptiv` | 279 | review: merge |
| `Einspiel` | `einspielen` | 279 | review: merge |
| `Kenn` | `kennen` | 279 | review: merge |
| `aufgehend` | `aufgehen` | 279 | review: merge |
| `aufgeschaltet` | `aufschalten` | 279 | review: merge |
| `partnerbörse` | `Partnerbörse` | 279 | review: merge |
| `spröd` | `spröde` | 279 | review: merge |
| `wrden` | `werden` | 279 | review: merge |
| `Empfind` | `empfinden` | 278 | review: merge |
| `Zeitabständen` | `Zeitabstand` | 278 | review: merge |
| `dämonen` | `Dämon` | 278 | review: merge |
| `ersteres` | `erste` | 278 | review: merge |
| `verwirkt` | `verwirken` | 278 | review: merge |
| `Durchstöbern` | `durchstöbern` | 277 | review: merge |
| `Erster` | `erste` | 277 | review: merge |
| `Geldbußen` | `Geldbuße` | 277 | review: merge |
| `THEMA` | `Thema` | 277 | review: merge |
| `Volum` | `Volumen` | 277 | review: merge |
| `WLANs` | `WLAN` | 277 | review: merge |
| `brok` | `Broker` | 277 | review: merge |
| `haftend` | `haften` | 277 | review: merge |
| `ibis` | `Ibis` | 277 | review: merge |
| `motorrad` | `Motorrad` | 277 | review: merge |
| `ndern` | `ändern` | 277 | review: merge |
| `Beladen` | `beladen` | 276 | review: merge |
| `Hompage` | `Homepage` | 276 | review: merge |
| `Pesos` | `Peso` | 276 | review: merge |
| `Wenige` | `wenig` | 276 | review: merge |
| `dagewesenen` | `dagewesen` | 276 | review: merge |
| `durchgesickert` | `durchsickern` | 276 | review: merge |
| `fernseh` | `fernsehen` | 276 | review: merge |
| `hosen` | `Hose` | 276 | review: merge |
| `mietwagen` | `Mietwagen` | 276 | review: merge |
| `Ausblende` | `ausblenden` | 275 | review: merge |
| `Erfasst` | `erfassen` | 275 | review: merge |
| `Gurus` | `Guru` | 275 | review: merge |
| `Klonen` | `klonen` | 275 | review: merge |
| `Lebensstile` | `Lebensstil` | 275 | review: merge |
| `Nachladen` | `nachladen` | 275 | review: merge |
| `Puzzleteile` | `Puzzleteil` | 275 | review: merge |
| `abgedunkelt` | `abdunkeln` | 275 | review: merge |
| `gekreuzt` | `kreuzen` | 275 | review: merge |
| `tools` | `Tool` | 275 | review: merge |
| `unterschätzt` | `unterschätzen` | 275 | review: merge |
| `verzögert` | `verzögern` | 275 | review: merge |
| `vorangekommen` | `vorankommen` | 275 | review: merge |
| `Abhör` | `abhören` | 274 | review: merge |
| `Aufhöre` | `aufhören` | 274 | review: merge |
| `Erhöhe` | `erhöhen` | 274 | review: merge |
| `Kommunikationsdat` | `Kommunikationsdaten` | 274 | review: merge |
| `Rosett` | `Rosette` | 274 | review: merge |
| `SERVICES` | `Service` | 274 | review: merge |
| `Selbstbewusst` | `selbstbewusst` | 274 | review: merge |
| `Softdrinks` | `Softdrink` | 274 | review: merge |
| `VERARBEITUNG` | `Verarbeitung` | 274 | review: merge |
| `Betrügereie` | `Betrügerei` | 273 | review: merge |
| `Chilli` | `Chili` | 273 | review: merge |
| `TECHNISCHE` | `technisch` | 273 | review: merge |
| `ranghoh` | `ranghoch` | 273 | review: merge |
| `Formulardat` | `Formulardaten` | 272 | review: merge |
| `Fotomontag` | `Fotomontage` | 272 | review: merge |
| `WEBSITE` | `Website` | 272 | review: merge |
| `Zealand` | `Neuseeland` | 272 | review: merge |
| `Zuschauerinn` | `Zuschauerin` | 272 | review: merge |
| `nebenstehen` | `nebenstehend` | 272 | review: merge |
| `Achillessehn` | `Achillessehne` | 271 | review: merge |
| `Apart` | `apart` | 271 | review: merge |
| `ArbeitnehmerInne` | `Arbeitnehmer` | 271 | review: merge |
| `Aufzeig` | `aufzeigen` | 271 | review: merge |
| `Clevere` | `clever` | 271 | review: merge |
| `Farbtö` | `Farbton` | 271 | review: merge |
| `Ferienhaeuser` | `Ferienhaus` | 271 | review: merge |
| `LOS` | `los` | 271 | review: merge |
| `Pankreatiti` | `Pankreatitis` | 271 | review: merge |
| `Projektteams` | `Projektteam` | 271 | review: merge |
| `RADIO` | `Radio` | 271 | review: merge |
| `Syphili` | `Syphilis` | 271 | review: merge |
| `Toscana` | `Toskana` | 271 | review: merge |
| `grenzüberschreiten` | `grenzüberschreitend` | 271 | review: merge |
| `AGENDA` | `Agenda` | 270 | review: merge |
| `Fernab` | `fernab` | 270 | review: merge |
| `Kartonag` | `Kartonage` | 270 | review: merge |
| `SUCHE` | `Suche` | 270 | review: merge |
| `Wüst` | `wüst` | 270 | review: merge |
| `Communities` | `Community` | 269 | review: merge |
| `Einmalein` | `Einmaleins` | 269 | review: merge |
| `Fauxpa` | `Fauxpas` | 269 | review: merge |
| `Landingpag` | `Landingpage` | 269 | review: merge |
| `Nachtesse` | `Nachtessen` | 269 | review: merge |
| `SCHRITT` | `Schritt` | 269 | review: merge |
| `ingam` | `ingame` | 269 | review: merge |
| `Abspeicher` | `abspeichern` | 268 | review: merge |
| `EINLEITUNG` | `Einleitung` | 268 | review: merge |
| `EXPRESS` | `Express` | 268 | review: merge |
| `Hautbarrier` | `Hautbarriere` | 268 | review: merge |
| `Konjunkturdat` | `Konjunkturdaten` | 268 | review: merge |
| `PLAYMOBIL` | `Playmobil` | 268 | review: merge |
| `PRODUKTE` | `Produkt` | 268 | review: merge |
| `Spezialwisse` | `Spezialwissen` | 268 | review: merge |
| `Verkehrsdat` | `Verkehrsdaten` | 268 | review: merge |
| `Verwicklunge` | `Verwicklung` | 268 | review: merge |
| `tips` | `Tipp` | 268 | review: merge |
| `Bisweile` | `bisweilen` | 267 | review: merge |
| `GRÜN` | `grün` | 267 | review: merge |
| `Samtpfot` | `Samtpfote` | 267 | review: merge |
| `Starr` | `starr` | 267 | review: merge |
| `Wurzelballe` | `Wurzelballen` | 267 | review: merge |
| `jenig` | `derjenige` | 267 | review: merge |
| `spring` | `springen` | 267 | review: merge |
| `wohnwagen` | `Wohnwagen` | 267 | review: merge |
| `Aphorisme` | `Aphorismus` | 266 | review: merge |
| `Leistungsbeschreibunge` | `Leistungsbeschreibung` | 266 | review: merge |
| `Schwarz-wissen` | `Schwarz-Weiß` | 266 | review: merge |
| `Zigarettenanzünd` | `Zigarettenanzünder` | 266 | review: merge |
| `Bestelldat` | `Bestelldatum` | 265 | review: merge |
| `Holzbalk` | `Holzbalken` | 265 | review: merge |
| `Skispring` | `Skispringen` | 265 | review: merge |
| `VERLAG` | `Verlag` | 265 | review: merge |
| `Vertragsdate` | `Vertragsdatum` | 265 | review: merge |
| `Outlets` | `Outlet` | 264 | review: merge |
| `Schlagober` | `Schlagobers` | 264 | review: merge |
| `western` | `Western` | 264 | review: merge |
| `Ansammlunge` | `Ansammlung` | 263 | review: merge |
| `INFOS` | `Info` | 263 | review: merge |
| `JAHR` | `Jahr` | 263 | review: merge |
| `Sardini` | `Sardinien` | 263 | review: merge |
| `Schäfche` | `Schäfchen` | 263 | review: merge |
| `StudentInne` | `Student` | 263 | review: merge |
| `WOLLEN` | `wollen` | 263 | review: merge |
| `infrag` | `infrage` | 263 | review: merge |
| `Gartenpfleg` | `Gartenpflege` | 262 | review: merge |
| `MESSE` | `Messe` | 262 | review: merge |
| `Meteorite` | `Meteorit` | 262 | review: merge |
| `Schaltfläch` | `Schaltfläche` | 262 | review: merge |
| `Textile` | `textil` | 262 | review: merge |
| `allergrößt` | `groß` | 262 | review: merge |
| `Ausschneid` | `ausschneiden` | 261 | review: merge |
| `MENSCH` | `Mensch` | 261 | review: merge |
| `Tagsüber` | `tagsüber` | 271 | review: merge |
| `Trink` | `trinken` | 271 | review: merge |
| `aufbau` | `Aufbau` | 271 | review: merge |
| `gepostet` | `posten` | 271 | review: merge |
| `geschaltet` | `schalten` | 271 | review: merge |
| `Übergewichtig` | `übergewichtig` | 271 | review: merge |
| `Überraschenderweise` | `überraschenderweise` | 271 | review: merge |
| `Auße` | `außen` | 270 | review: merge |
| `Typischerweise` | `typischerweise` | 270 | review: merge |
| `frieden` | `Frieden` | 270 | review: merge |
| `maßen` | `messen` | 270 | review: merge |
| `zurückgegeben` | `zurückgeben` | 270 | review: merge |
| `Drinn` | `drinnen` | 269 | review: merge |
| `Nhe` | `Nähe` | 269 | review: merge |
| `drapiert` | `drapieren` | 269 | review: merge |
| `eingeschweißt` | `einschweißen` | 269 | review: merge |
| `frühlingshaften` | `frühlingshaft` | 269 | review: merge |
| `fussball` | `Fußball` | 269 | review: merge |
| `fänd` | `finden` | 269 | review: merge |
| `gelauncht` | `launchen` | 269 | review: merge |
| `sog` | `sogenannt` | 269 | review: merge |
| `untern` | `unter` | 269 | review: merge |
| `verbrauch` | `Verbrauch` | 269 | review: merge |
| `zurückgeschnitten` | `zurückschneiden` | 269 | review: merge |
| `Übrig` | `übrig` | 269 | review: merge |
| `Bestenfall` | `bestenfalls` | 268 | review: merge |
| `Flurförderzeuge` | `Flurförderzeug` | 268 | review: merge |
| `Milliardäre` | `Milliardär` | 268 | review: merge |
| `Patter` | `Pattern` | 268 | review: merge |
| `Sedcards` | `Sedcard` | 268 | review: merge |
| `aufgehübscht` | `aufhübschen` | 268 | review: merge |
| `feedback` | `Feedback` | 268 | review: merge |
| `gewidmet` | `widmen` | 268 | review: merge |
| `kissen` | `Kissen` | 268 | review: merge |
| `koloriert` | `kolorieren` | 268 | review: merge |
| `nippel` | `Nippel` | 268 | review: merge |
| `singles` | `Single` | 268 | review: merge |
| `unterhalte` | `unterhalten` | 268 | review: merge |
| `verhassten` | `verhasst` | 268 | review: merge |
| `verstehn` | `verstehen` | 268 | review: merge |
| `Gefolgsleute` | `Gefolgsmann` | 267 | review: merge |
| `Pamper` | `Pampers` | 267 | review: merge |
| `Schwangerschaftsabbrüche` | `Schwangerschaftsabbruch` | 267 | review: merge |
| `Silberne` | `silbern` | 267 | review: merge |
| `Skalieren` | `skalieren` | 267 | review: merge |
| `Spik` | `Spike` | 267 | review: merge |
| `Vegetarische` | `vegetarisch` | 267 | review: merge |
| `Worum` | `worum` | 267 | review: merge |
| `Zweigstellen` | `Zweigstelle` | 267 | review: merge |
| `aufgefunden` | `auffinden` | 267 | review: merge |
| `aufgeteilt` | `aufteilen` | 267 | review: merge |
| `dis` | `dieser` | 267 | review: merge |
| `ehefrau` | `Ehefrau` | 267 | review: merge |
| `entgültig` | `endgültig` | 267 | review: merge |
| `gestreut` | `streuen` | 267 | review: merge |
| `kontroverse` | `kontrovers` | 267 | review: merge |
| `oxidativem` | `oxidativ` | 267 | review: merge |
| `süsse` | `süß` | 267 | review: merge |
| `Dynamiken` | `Dynamik` | 266 | review: merge |
| `Gadgets` | `Gadget` | 266 | review: merge |
| `Gynäkolog` | `Gynäkologe` | 266 | review: merge |
| `Heimlich` | `heimlich` | 266 | review: merge |
| `Rötel` | `Röteln` | 266 | review: merge |
| `Selbige` | `selbig` | 266 | review: merge |
| `Zahnarztpraxen` | `Zahnarztpraxis` | 266 | review: merge |
| `agressiv` | `aggressiv` | 266 | review: merge |
| `gepusht` | `pushen` | 266 | review: merge |
| `gestiftet` | `stiften` | 266 | review: merge |
| `lancierte` | `lancieren` | 266 | review: merge |
| `massgebend` | `maßgebend` | 266 | review: merge |
| `zugesetzt` | `zusetzen` | 266 | review: merge |
| `Antippe` | `antippen` | 265 | review: merge |
| `Hochs` | `Hoch` | 265 | review: merge |
| `Reimen` | `Reim` | 265 | review: merge |
| `Servier` | `servieren` | 265 | review: merge |
| `Vorstösse` | `Vorstoß` | 265 | review: merge |
| `Wasserhähne` | `Wasserhahn` | 265 | review: merge |
| `aufgespannt` | `aufspannen` | 265 | review: merge |
| `ausland` | `Ausland` | 265 | review: merge |
| `blackjack` | `Blackjack` | 265 | review: merge |
| `relativiert` | `relativieren` | 265 | review: merge |
| `räume` | `räumen` | 265 | review: merge |
| `schlüssel` | `Schlüssel` | 265 | review: merge |
| `Abrolle` | `abrollen` | 264 | review: merge |
| `Lokale` | `lokal` | 264 | review: merge |
| `Retweets` | `Retweet` | 264 | review: merge |
| `Ungeimpft` | `ungeimpft` | 264 | review: merge |
| `Vermiete` | `vermieten` | 264 | review: merge |
| `burg` | `Burg` | 264 | review: merge |
| `erzieher` | `Erzieher` | 264 | review: merge |
| `gaming` | `Gaming` | 264 | review: merge |
| `gegebenfalls` | `gegebenenfalls` | 264 | review: merge |
| `merk` | `merken` | 264 | review: merge |
| `wiedereröffnet` | `wiedereröffnen` | 264 | review: merge |
| `Fingerabdrücken` | `Fingerabdruck` | 263 | review: merge |
| `GenossInnen` | `Genosse` | 263 | review: merge |
| `Heuschrecken` | `Heuschrecke` | 263 | review: merge |
| `Maßgebend` | `maßgebend` | 263 | review: merge |
| `Oel` | `Öl` | 263 | review: merge |
| `berall` | `überall` | 263 | review: merge |
| `enthaltend` | `enthalten` | 263 | review: merge |
| `ersatz` | `Ersatz` | 263 | review: merge |
| `fliessend` | `fließend` | 263 | review: merge |
| `heuschnupfen` | `Heuschnupfen` | 263 | review: merge |
| `minimum` | `Minimum` | 263 | review: merge |
| `nachbearbeitet` | `nachbearbeiten` | 263 | review: merge |
| `silikon` | `Silikon` | 263 | review: merge |
| `wohlschmecken` | `wohlschmeckend` | 263 | review: merge |
| `Kulturdenkmäler` | `Kulturdenkmal` | 262 | review: merge |
| `Motorsports` | `Motorsport` | 262 | review: merge |
| `Provisionsfrei` | `provisionsfrei` | 262 | review: merge |
| `Synchro` | `Synchronisation` | 262 | review: merge |
| `Verschiedene` | `verschieden` | 262 | review: merge |
| `Verschlucke` | `verschlucken` | 262 | review: merge |
| `eingepasst` | `einpassen` | 262 | review: merge |
| `verlaufend` | `verlaufen` | 262 | review: merge |
| `wasserlassen` | `Wasserlassen` | 262 | review: merge |
| `Gürtelschlaufen` | `Gürtelschlaufe` | 261 | review: merge |
| `Herzkranzgefäße` | `Herzkranzgefäß` | 261 | review: merge |
| `Menstruationsbeschwerde` | `Menstruationsbeschwerden` | 261 | review: merge |
| `Wehwehche` | `Wehwehchen` | 261 | review: merge |
| `Arse` | `Arsen` | 260 | review: merge |
| `Auswert` | `auswerten` | 260 | review: merge |
| `Heerschare` | `Heerschar` | 260 | review: merge |
| `Hiergeg` | `hiergegen` | 260 | review: merge |
| `LEICHT` | `leicht` | 260 | review: merge |
| `Schleswig-Holsteinische` | `schleswig-holsteinisch` | 260 | review: merge |
| `Strumpfhosen` | `Strumpfhose` | 260 | review: merge |
| `schiefgeh` | `schiefgehen` | 260 | review: merge |
| `Bundesministerie` | `Bundesministerium` | 259 | review: merge |
| `KFW` | `KfW` | 259 | review: merge |
| `Lebensläuf` | `Lebenslauf` | 259 | review: merge |
| `SCHWEIZ` | `Schweiz` | 259 | review: merge |
| `Derart` | `derart` | 258 | review: merge |
| `GARANTIE` | `Garantie` | 258 | review: merge |
| `GESCHÄFTSBEDINGUNGEN` | `Geschäftsbedingung` | 258 | review: merge |
| `LERNEN` | `lernen` | 258 | review: merge |
| `MORGEN` | `morgen` | 258 | review: merge |
| `Manschettenknöpfe` | `Manschettenknopf` | 258 | review: merge |
| `Präsen` | `Präsens` | 258 | review: merge |
| `LIEFERUNG` | `Lieferung` | 257 | review: merge |
| `LÖSUNGEN` | `Lösung` | 257 | review: merge |
| `Lähmunge` | `Lähmung` | 257 | review: merge |
| `Selig` | `selig` | 261 | review: merge |
| `Uploads` | `Upload` | 261 | review: merge |
| `ermglicht` | `ermöglichen` | 261 | review: merge |
| `heranzuführen` | `heranführen` | 261 | review: merge |
| `insg` | `insgesamt` | 261 | review: merge |
| `steten` | `stet` | 261 | review: merge |
| `temperatur` | `Temperatur` | 261 | review: merge |
| `wenigkeit` | `Wenigkeit` | 261 | review: merge |
| `Behördengänge` | `Behördengang` | 260 | review: merge |
| `Erneuerbarer` | `erneuerbar` | 260 | review: merge |
| `Gedanken` | `Gedanke` | 260 | review: merge |
| `Grooves` | `Groove` | 260 | review: merge |
| `Sträuchern` | `Strauch` | 260 | review: merge |
| `darueber` | `darüber` | 260 | review: merge |
| `februar` | `Februar` | 260 | review: merge |
| `guenstig` | `günstig` | 260 | review: merge |
| `kit` | `Kit` | 260 | review: merge |
| `kurze` | `kurz` | 260 | review: merge |
| `schmeckend` | `schmecken` | 260 | review: merge |
| `schwangerschaft` | `Schwangerschaft` | 260 | review: merge |
| `sklavin` | `Sklavin` | 260 | review: merge |
| `startguthaben` | `Startguthaben` | 260 | review: merge |
| `vorwissen` | `Vorwissen` | 260 | review: merge |
| `Aufsteig` | `aufsteigen` | 259 | review: merge |
| `Dünge` | `düngen` | 259 | review: merge |
| `Fingernägel` | `Fingernagel` | 259 | review: merge |
| `Geschriebene` | `schreiben` | 259 | review: merge |
| `Nachrüst` | `nachrüsten` | 259 | review: merge |
| `Passier` | `passieren` | 259 | review: merge |
| `Pflegegrade` | `Pflegegrad` | 259 | review: merge |
| `Psychosomatisch` | `psychosomatisch` | 259 | review: merge |
| `Scheuen` | `scheuen` | 259 | review: merge |
| `Sprösslinge` | `Sprössling` | 259 | review: merge |
| `Sulfite` | `Sulfit` | 259 | review: merge |
| `denkmals` | `Denkmal` | 259 | review: merge |
| `enstehen` | `entstehen` | 259 | review: merge |
| `entwässert` | `entwässern` | 259 | review: merge |
| `fitness` | `Fitness` | 259 | review: merge |
| `nutzung` | `Nutzung` | 259 | review: merge |
| `rüberkommt` | `rüberkommen` | 259 | review: merge |
| `zurich` | `Zürich` | 259 | review: merge |
| `Behandel` | `behandeln` | 258 | review: merge |
| `Fühl` | `fühlen` | 258 | review: merge |
| `Negative` | `negativ` | 258 | review: merge |
| `Providern` | `Provider` | 258 | review: merge |
| `Unglücklicherweise` | `unglücklicherweise` | 258 | review: merge |
| `Virtuell` | `virtuell` | 258 | review: merge |
| `Werd` | `werden` | 258 | review: merge |
| `ernährung` | `Ernährung` | 258 | review: merge |
| `partei` | `Partei` | 258 | review: merge |
| `rhodiniert` | `rhodinieren` | 258 | review: merge |
| `Leggin` | `Leggings` | 257 | review: merge |
| `Preisvergleiche` | `Preisvergleich` | 257 | review: merge |
| `Verhinder` | `verhindern` | 257 | review: merge |
| `BAYERN` | `Bayern` | 256 | review: merge |
| `Blockflöt` | `Blockflöte` | 256 | review: merge |
| `Razzien` | `Razzia` | 256 | review: merge |
| `horren` | `horrend` | 256 | review: merge |
| `Allenfall` | `allenfalls` | 255 | review: merge |
| `alkohol` | `Alkohol` | 257 | review: merge |
| `drinn` | `drinnen` | 257 | review: merge |
| `ess` | `essen` | 257 | review: merge |
| `führ` | `führen` | 257 | review: merge |
| `innehatte` | `innehaben` | 257 | review: merge |
| `katz` | `Katze` | 257 | review: merge |
| `papa` | `Papa` | 257 | review: merge |
| `patient` | `Patient` | 257 | review: merge |
| `rauszuholen` | `rausholen` | 257 | review: merge |
| `trainer` | `Trainer` | 257 | review: merge |
| `wirksamste` | `wirksam` | 257 | review: merge |
| `zielorientierte` | `zielorientiert` | 257 | review: merge |
| `zusammenarbeit` | `Zusammenarbeit` | 257 | review: merge |
| `Aufstehe` | `aufstehen` | 256 | review: merge |
| `Grossbank` | `Großbank` | 256 | review: merge |
| `Kaiserliche` | `kaiserlich` | 256 | review: merge |
| `Klumpe` | `Klumpen` | 256 | review: merge |
| `Themenbereiche` | `Themenbereich` | 256 | review: merge |
| `Unendlich` | `unendlich` | 256 | review: merge |
| `Volumina` | `Volumen` | 256 | review: merge |
| `ausserhalb` | `außerhalb` | 256 | review: merge |
| `leistungsgerechte` | `leistungsgerecht` | 256 | review: merge |
| `medizin` | `Medizin` | 256 | review: merge |
| `prinzip` | `Prinzip` | 256 | review: merge |
| `referenziert` | `referenzieren` | 256 | review: merge |
| `remis` | `Remis` | 256 | review: merge |
| `ueberhaupt` | `überhaupt` | 256 | review: merge |
| `Abfüll` | `abfüllen` | 255 | review: merge |
| `Coutur` | `Couture` | 255 | review: merge |
| `Ignorier` | `ignorieren` | 255 | review: merge |
| `Praktikern` | `Praktiker` | 255 | review: merge |
| `Rouladen` | `Roulade` | 255 | review: merge |
| `Sprachenlerne` | `Sprachenlernen` | 255 | review: merge |
| `Wiederherstellen` | `wiederherstellen` | 255 | review: merge |
| `aufgeboten` | `aufbieten` | 255 | review: merge |
| `beispielhafte` | `beispielhaft` | 255 | review: merge |
| `singend` | `singen` | 395 | review: merge |
| `gesungen` | `singen` | 394 | review: merge |
| `riechend` | `riechen` | 393 | review: merge |
| `vollstreckt` | `vollstrecken` | 393 | review: merge |
| `gehäkelt` | `häkeln` | 391 | review: merge |
| `eingefroren` | `einfrieren` | 389 | review: merge |
| `stimulierend` | `stimulieren` | 389 | review: merge |
| `Ausruhen` | `ausruhen` | 383 | review: merge |
| `Mähen` | `mähen` | 382 | review: merge |
| `Hui` | `hui` | 381 | review: merge |
| `Lehrbeauftragter` | `Lehrbeauftragte` | 377 | review: merge |
| `grassierend` | `grassieren` | 375 | review: merge |
| `knisternd` | `knistern` | 375 | review: merge |
| `nachgefragt` | `nachfragen` | 374 | review: merge |
| `gleichgestellt` | `gleichstellen` | 373 | review: merge |
| `dampfend` | `dampfen` | 372 | review: merge |
| `allerletzte` | `allerletzt` | 367 | review: merge |
| `praxisorientierte` | `praxisorientiert` | 367 | review: merge |
| `signierte` | `signieren` | 367 | review: merge |
| `eingezogen` | `einziehen` | 366 | review: merge |
| `lesend` | `lesen` | 364 | review: merge |
| `anzulocken` | `anlocken` | 362 | review: merge |
| `eingenäht` | `einnähen` | 362 | review: merge |
| `entgegengebracht` | `entgegenbringen` | 362 | review: merge |
| `massgeschneidert` | `maßgeschneidert` | 362 | review: merge |
| `karamellisiert` | `karamellisieren` | 361 | review: merge |
| `mitgereist` | `mitreisen` | 361 | review: merge |
| `allzuviel` | `viel` | 360 | review: merge |
| `eingefärbt` | `einfärben` | 360 | review: merge |
| `kodiert` | `kodieren` | 360 | review: merge |
| `beglaubigt` | `beglaubigen` | 359 | review: merge |
| `gepackt` | `packen` | 359 | review: merge |
| `gegart` | `garen` | 358 | review: merge |
| `schließend` | `schließen` | 358 | review: merge |
| `eingespart` | `einsparen` | 356 | review: merge |
| `abgestuft` | `abstufen` | 354 | review: merge |
| `festgeschrieben` | `festschreiben` | 354 | review: merge |
| `feuerverzinkt` | `feuerverzinken` | 353 | review: merge |
| `nährend` | `nähren` | 352 | review: merge |
| `angemietet` | `anmieten` | 346 | review: merge |
| `einfallend` | `einfallen` | 346 | review: merge |
| `zubereitet` | `zubereiten` | 345 | review: merge |
| `unbewußt` | `unbewusst` | 344 | review: merge |
| `abgedeckt` | `abdecken` | 343 | review: merge |
| `Kleck` | `Klecks` | 342 | review: merge |
| `verschmutzt` | `verschmutzen` | 342 | review: merge |
| `geschmort` | `schmoren` | 336 | review: merge |
| `gesplittet` | `splitten` | 336 | review: merge |
| `angepeilt` | `anpeilen` | 335 | review: merge |
| `abgeflacht` | `abflachen` | 333 | review: merge |
| `angebrochen` | `anbrechen` | 333 | review: merge |
| `sachte` | `sacht` | 333 | review: merge |
| `zerstört` | `zerstören` | 333 | review: merge |
| `angefeuchtet` | `anfeuchten` | 332 | review: merge |
| `ausgeschnitten` | `ausschneiden` | 332 | review: merge |
| `initiiert` | `initiieren` | 332 | review: merge |
| `angezogen` | `anziehen` | 331 | review: merge |
| `entnommen` | `entnehmen` | 331 | review: merge |
| `Nebenerzeugnisse` | `Nebenerzeugnis` | 329 | review: merge |
| `Setups` | `Setup` | 329 | review: merge |
| `Sicherstelle` | `sicherstellen` | 329 | review: merge |
| `Säubern` | `säubern` | 329 | review: merge |
| `Theil` | `Teil` | 329 | review: merge |
| `Wichsen` | `wichsen` | 329 | review: merge |
| `auff` | `auf` | 329 | review: merge |
| `basis` | `Basis` | 329 | review: merge |
| `verfasst` | `verfassen` | 329 | review: merge |
| `zukunftsorientierten` | `zukunftsorientiert` | 329 | review: merge |
| `Gestelle` | `Gestell` | 328 | review: merge |
| `Kartuschen` | `Kartusche` | 328 | review: merge |
| `Landstriche` | `Landstrich` | 328 | review: merge |
| `Männlich` | `männlich` | 328 | review: merge |
| `Selbe` | `selbe` | 328 | review: merge |
| `Strateg` | `Stratege` | 328 | review: merge |
| `Tobe` | `toben` | 328 | review: merge |
| `ausgelösten` | `auslösen` | 328 | review: merge |
| `bewusster` | `bewusst` | 328 | review: merge |
| `definitv` | `definitiv` | 328 | review: merge |
| `favorisierte` | `favorisieren` | 328 | review: merge |
| `kommts` | `kommen` | 328 | review: merge |
| `rausgenommen` | `rausnehmen` | 328 | review: merge |
| `zeitpunkt` | `Zeitpunkt` | 328 | review: merge |
| `Bugfixes` | `Bugfix` | 327 | review: merge |
| `aufgezählt` | `aufzählen` | 327 | review: merge |
| `deck` | `decken` | 327 | review: merge |
| `einzuschüchtern` | `einschüchtern` | 327 | review: merge |
| `inclusive` | `inklusive` | 327 | review: merge |
| `kämpfend` | `kämpfen` | 327 | review: merge |
| `song` | `Song` | 327 | review: merge |
| `Auftraggebern` | `Auftraggeber` | 326 | review: merge |
| `Elben` | `Elb` | 326 | review: merge |
| `Inlays` | `Inlay` | 326 | review: merge |
| `abgefragt` | `abfragen` | 326 | review: merge |
| `fhren` | `führen` | 326 | review: merge |
| `hausfrau` | `Hausfrau` | 326 | review: merge |
| `kfz` | `Kfz` | 326 | review: merge |
| `Anbraten` | `anbraten` | 325 | review: merge |
| `Beschaeftigungsverhaeltnis` | `Beschäftigungsverhältnis` | 325 | review: merge |
| `Integrieren` | `integrieren` | 325 | review: merge |
| `Kickbox` | `Kickboxen` | 325 | review: merge |
| `Mitochondrien` | `Mitochondrium` | 325 | review: merge |
| `Polstern` | `Polster` | 325 | review: merge |
| `Reine` | `rein` | 325 | review: merge |
| `Sextoys` | `Sextoy` | 325 | review: merge |
| `eingesandt` | `einsenden` | 325 | review: merge |
| `favorit` | `Favorit` | 325 | review: merge |
| `stellung` | `Stellung` | 325 | review: merge |
| `Bereitstelle` | `bereitstellen` | 324 | review: merge |
| `Scherg` | `Scherge` | 324 | review: merge |
| `Warten` | `warten` | 324 | review: merge |
| `Wirkliche` | `wirklich` | 324 | review: merge |
| `angeraut` | `anrauen` | 324 | review: merge |
| `geschäft` | `Geschäft` | 324 | review: merge |
| `kundenorientierte` | `kundenorientiert` | 324 | review: merge |
| `milch` | `Milch` | 324 | review: merge |
| `wikipedia` | `Wikipedia` | 324 | review: merge |
| `überstanden` | `überstehen` | 324 | review: merge |
| `Arbeitszeugnisse` | `Arbeitszeugnis` | 323 | review: merge |
| `Chatte` | `chatten` | 323 | review: merge |
| `Ihrer` | `ihr` | 323 | review: merge |
| `Maximal` | `maximal` | 323 | review: merge |
| `Rauchen` | `rauchen` | 323 | review: merge |
| `UFOs` | `UFO` | 323 | review: merge |
| `Würd` | `werden` | 323 | review: merge |
| `geflasht` | `flashen` | 323 | review: merge |
| `kultur` | `Kultur` | 323 | review: merge |
| `mutte` | `Mutter` | 323 | review: merge |
| `püriert` | `pürieren` | 323 | review: merge |
| `schaft` | `Schaft` | 323 | review: merge |
| `Fll` | `Fall` | 322 | review: merge |
| `Gat` | `Gate` | 322 | review: merge |
| `Konsequent` | `konsequent` | 322 | review: merge |
| `Nordische` | `nordisch` | 322 | review: merge |
| `adapter` | `Adapter` | 322 | review: merge |
| `format` | `Format` | 322 | review: merge |
| `gehoert` | `gehören` | 322 | review: merge |
| `markiert` | `markieren` | 322 | review: merge |
| `satiniert` | `satinieren` | 322 | review: merge |
| `verdickt` | `verdicken` | 322 | review: merge |
| `Übersichtlich` | `übersichtlich` | 322 | review: merge |
| `Antik` | `antik` | 321 | review: merge |
| `Höchsten` | `höchstens` | 321 | review: merge |
| `hals` | `Hals` | 321 | review: merge |
| `sprüh` | `sprühen` | 321 | review: merge |
| `zuen` | `zuende` | 321 | review: merge |
| `Bevölkerungsdicht` | `Bevölkerungsdichte` | 320 | review: merge |
| `Greifen` | `greifen` | 320 | review: merge |
| `InhaltsverzeichnisMehr` | `Inhaltsverzeichnis` | 320 | review: merge |
| `Mnchen` | `München` | 320 | review: merge |
| `Professionell` | `professionell` | 320 | review: merge |
| `Schärfste` | `scharf` | 320 | review: merge |
| `abgepackt` | `abpacken` | 320 | review: merge |
| `alpha` | `Alpha` | 320 | review: merge |
| `bewerbung` | `Bewerbung` | 320 | review: merge |
| `geerntet` | `ernten` | 320 | review: merge |
| `mädels` | `Mädel` | 320 | review: merge |
| `wüssten` | `wissen` | 320 | review: merge |
| `Betriebliche` | `betrieblich` | 319 | review: merge |
| `Fecht` | `fechten` | 319 | review: merge |
| `Lackier` | `lackieren` | 319 | review: merge |
| `Münde` | `münden` | 319 | review: merge |
| `Schüttel` | `schütteln` | 319 | review: merge |
| `Spikes` | `Spike` | 319 | review: merge |
| `Wünschenswert` | `wünschenswert` | 319 | review: merge |
| `Zeitreisen` | `Zeitreise` | 319 | review: merge |
| `auszieh` | `ausziehen` | 319 | review: merge |
| `deutschlandweite` | `deutschlandweit` | 319 | review: merge |
| `hochgezogen` | `hochziehen` | 319 | review: merge |
| `rabatt` | `Rabatt` | 319 | review: merge |
| `ros` | `rosé` | 319 | review: merge |
| `titelt` | `titeln` | 319 | review: merge |
| `Asiatisch` | `asiatisch` | 318 | review: merge |
| `Grnde` | `Grund` | 318 | review: merge |
| `bissen` | `beißen` | 318 | review: merge |
| `rechn` | `Rechner` | 318 | review: merge |
| `region` | `Region` | 318 | review: merge |
| `schnapp` | `schnappen` | 318 | review: merge |
| `umfasste` | `umfassen` | 318 | review: merge |
| `Übe` | `üben` | 318 | review: merge |
| `Ernsthaft` | `ernsthaft` | 317 | review: merge |
| `Quitt` | `quitt` | 317 | review: merge |
| `Testern` | `Tester` | 317 | review: merge |
| `angegliedert` | `angliedern` | 317 | review: merge |
| `anzahl` | `Anzahl` | 317 | review: merge |
| `heilsame` | `heilsam` | 317 | review: merge |
| `schein` | `Schein` | 317 | review: merge |
| `veröffentlicht` | `veröffentlichen` | 317 | review: merge |
| `wahrheit` | `Wahrheit` | 317 | review: merge |
| `Codecs` | `Codec` | 316 | review: merge |
| `Energieeffizient` | `energieeffizient` | 316 | review: merge |
| `Forschen` | `forschen` | 316 | review: merge |
| `Glutenfrei` | `glutenfrei` | 316 | review: merge |
| `Mediatheken` | `Mediathek` | 316 | review: merge |
| `Mobs` | `Mob` | 316 | review: merge |
| `angeleitet` | `anleiten` | 316 | review: merge |
| `bestückt` | `bestücken` | 316 | review: merge |
| `inszeniert` | `inszenieren` | 316 | review: merge |
| `notwenig` | `notwendig` | 316 | review: merge |
| `pferd` | `Pferd` | 316 | review: merge |
| `voranzukommen` | `vorankommen` | 316 | review: merge |
| `wiedergegeben` | `wiedergeben` | 316 | review: merge |
| `wiederspiegelt` | `widerspiegeln` | 316 | review: merge |
| `Flüstern` | `flüstern` | 315 | review: merge |
| `Fuss` | `Fuß` | 315 | review: merge |
| `Kufen` | `Kufe` | 315 | review: merge |
| `Präsentieren` | `präsentieren` | 315 | review: merge |
| `Spannen` | `spannen` | 315 | review: merge |
| `angelehnt` | `anlehnen` | 315 | review: merge |
| `angerichtet` | `anrichten` | 315 | review: merge |
| `geschichten` | `Geschichte` | 315 | review: merge |
| `getaktet` | `takten` | 315 | review: merge |
| `komprimiert` | `komprimieren` | 315 | review: merge |
| `nachteil` | `Nachteil` | 315 | review: merge |
| `reichend` | `reichen` | 315 | review: merge |
| `Antragssteller` | `Antragsteller` | 314 | review: merge |
| `Archäologische` | `archäologisch` | 314 | review: merge |
| `Pflanzenöle` | `Pflanzenöl` | 314 | review: merge |
| `Pharaon` | `Pharao` | 314 | review: merge |
| `Umfalle` | `umfallen` | 314 | review: merge |
| `Umziehe` | `umziehen` | 314 | review: merge |
| `Wellensittiche` | `Wellensittich` | 314 | review: merge |
| `alters` | `Alter` | 314 | review: merge |
| `dachen` | `denken` | 314 | review: merge |
| `lschen` | `löschen` | 314 | review: merge |
| `stock` | `Stock` | 314 | review: merge |
| `switch` | `switchen` | 314 | review: merge |
| `vordefinierten` | `vordefiniert` | 314 | review: merge |
| `Peinlich` | `peinlich` | 313 | review: merge |
| `Recherchier` | `recherchieren` | 313 | review: merge |
| `Schnupper` | `schnuppern` | 313 | review: merge |
| `Verlier` | `verlieren` | 313 | review: merge |
| `aggregiert` | `aggregieren` | 313 | review: merge |
| `liebend` | `lieben` | 313 | review: merge |
| `zuMehr` | `mehr` | 313 | review: merge |
| `Lider` | `Lid` | 312 | review: merge |
| `Theologische` | `theologisch` | 312 | review: merge |
| `Zarg` | `Zarge` | 312 | review: merge |
| `diskussion` | `Diskussion` | 312 | review: merge |
| `stk` | `Stück` | 312 | review: merge |
| `ungewiß` | `ungewiss` | 312 | review: merge |
| `untergebracht` | `unterbringen` | 312 | review: merge |
| `Abdecke` | `abdecken` | 311 | review: merge |
| `Febr` | `Februar` | 311 | review: merge |
| `Jobbörsen` | `Jobbörse` | 311 | review: merge |
| `Korrekt` | `korrekt` | 311 | review: merge |
| `Normale` | `normal` | 311 | review: merge |
| `Runter` | `runter` | 311 | review: merge |
| `Verfasse` | `verfassen` | 311 | review: merge |
| `Vorallem` | `vor allem` | 311 | review: merge |
| `bedeutung` | `Bedeutung` | 311 | review: merge |
| `dazugehörend` | `dazugehören` | 311 | review: merge |
| `gemanagt` | `managen` | 311 | review: merge |
| `hause` | `Haus` | 311 | review: merge |
| `tituliert` | `titulieren` | 311 | review: merge |
| `verfolgt` | `verfolgen` | 311 | review: merge |
| `Aufwache` | `aufwachen` | 310 | review: merge |
| `Bergsteig` | `bergsteigen` | 310 | review: merge |
| `Gesetzliche` | `gesetzlich` | 310 | review: merge |
| `Größenordnungen` | `Größenordnung` | 310 | review: merge |
| `angeliefert` | `anliefern` | 310 | review: merge |
| `couch` | `Couch` | 310 | review: merge |
| `lizenzierten` | `lizenzieren` | 310 | review: merge |
| `nachfrag` | `nachfragen` | 310 | review: merge |
| `überschüttet` | `überschütten` | 310 | review: merge |
| `Allerg` | `Allergen` | 309 | review: merge |
| `Funkel` | `funkeln` | 309 | review: merge |
| `Krücken` | `Krücke` | 309 | review: merge |
| `Neuronen` | `Neuron` | 309 | review: merge |
| `Niederländische` | `niederländisch` | 309 | review: merge |
| `Rett` | `retten` | 309 | review: merge |
| `ambulante` | `ambulant` | 309 | review: merge |
| `cleverer` | `clever` | 309 | review: merge |
| `gas` | `Gas` | 309 | review: merge |
| `gegenteil` | `Gegenteil` | 309 | review: merge |
| `loslässt` | `loslassen` | 309 | review: merge |
| `nurnoch` | `nur` | 309 | review: merge |
| `symbol` | `Symbol` | 309 | review: merge |
| `verweise` | `verweisen` | 309 | review: merge |
| `zweck` | `Zweck` | 309 | review: merge |
| `GIFs` | `GIF` | 308 | review: merge |
| `Klassische` | `klassisch` | 308 | review: merge |
| `Manuell` | `manuell` | 308 | review: merge |
| `Multipler` | `multipel` | 308 | review: merge |
| `Singlebörsen` | `Singlebörse` | 308 | review: merge |
| `elch` | `Elch` | 308 | review: merge |
| `iQ` | `IQ` | 308 | review: merge |
| `lady` | `Lady` | 308 | review: merge |
| `männer` | `Mann` | 308 | review: merge |
| `retourniert` | `retournieren` | 308 | review: merge |
| `worte` | `Wort` | 308 | review: merge |
| `Allround` | `allround` | 307 | review: merge |
| `Betreuerinn` | `Betreuerin` | 307 | review: merge |
| `Offert` | `Offerte` | 307 | review: merge |
| `Vermittel` | `vermitteln` | 307 | review: merge |
| `erz` | `Erz` | 307 | review: merge |
| `kritik` | `Kritik` | 307 | review: merge |
| `teams` | `Team` | 307 | review: merge |
| `willkommener` | `willkommen` | 307 | review: merge |
| `zugesandt` | `zusenden` | 307 | review: merge |
| `Überschuß` | `Überschuss` | 307 | review: merge |
| `öffentlichkeit` | `Öffentlichkeit` | 307 | review: merge |
| `Auftaue` | `auftauen` | 306 | review: merge |
| `Austattung` | `Ausstattung` | 306 | review: merge |
| `Beitrge` | `Beitrag` | 306 | review: merge |
| `Bios` | `Bio` | 306 | review: merge |
| `Bisschen` | `bisschen` | 306 | review: merge |
| `Ermittel` | `ermitteln` | 306 | review: merge |
| `Hause` | `Haus` | 306 | review: merge |
| `Norddeutsch` | `norddeutsch` | 306 | review: merge |
| `PREIS` | `Preis` | 306 | review: merge |
| `Sparr` | `Sparren` | 306 | review: merge |
| `Treppensteig` | `treppensteigen` | 306 | review: merge |
| `etw` | `etwas` | 306 | review: merge |
| `hausfrauen` | `Hausfrau` | 306 | review: merge |
| `herausgebildet` | `sich herausbilden` | 306 | review: merge |
| `iwie` | `irgendwie` | 306 | review: merge |
| `neuer` | `neu` | 306 | review: merge |
| `tren` | `Trend` | 306 | review: merge |
| `zeitlang` | `Zeitlang` | 306 | review: merge |
| `Aborigines` | `Aborigine` | 305 | review: merge |
| `Microfasertuch` | `Mikrofasertuch` | 305 | review: merge |
| `Platziert` | `platzieren` | 305 | review: merge |
| `Rechtssprechung` | `Rechtsprechung` | 305 | review: merge |
| `Schmökern` | `schmökern` | 305 | review: merge |
| `Streichel` | `streicheln` | 305 | review: merge |
| `Swimmingpools` | `Swimmingpool` | 305 | review: merge |
| `bruder` | `Bruder` | 305 | review: merge |
| `gemeint` | `meinen` | 305 | review: merge |
| `häkchen` | `Häkchen` | 305 | review: merge |
| `staat` | `Staat` | 305 | review: merge |
| `stiess` | `stoßen` | 305 | review: merge |
| `übergewichtigen` | `übergewichtig` | 305 | review: merge |
| `überm` | `über` | 305 | review: merge |
| `ArbeiterInnen` | `Arbeiter` | 304 | review: merge |
| `Durchaus` | `durchaus` | 304 | review: merge |
| `Gesamte` | `gesamt` | 304 | review: merge |
| `Melass` | `Melasse` | 304 | review: merge |
| `Zweifelsfalle` | `Zweifelsfall` | 304 | review: merge |
| `auszuschliessen` | `ausschließen` | 304 | review: merge |
| `emittiert` | `emittieren` | 304 | review: merge |
| `entscheidung` | `Entscheidung` | 304 | review: merge |
| `ffnen` | `öffnen` | 304 | review: merge |
| `firmeneinträge` | `Firmeneintrag` | 304 | review: merge |
| `Brumme` | `brummen` | 303 | review: merge |
| `Jhdt` | `Jahrhundert` | 303 | review: merge |
| `auftrag` | `Auftrag` | 303 | review: merge |
| `eingeschickt` | `einschicken` | 303 | review: merge |
| `nmlich` | `nämlich` | 303 | review: merge |
| `ser` | `unser` | 303 | review: merge |
| `ungeschlagenen` | `ungeschlagen` | 303 | review: merge |
| `verscheiden` | `verschieden` | 303 | review: merge |
| `vielzahl` | `Vielzahl` | 303 | review: merge |
| `Beantrage` | `beantragen` | 302 | review: merge |
| `Globale` | `global` | 302 | review: merge |
| `Grosses` | `groß` | 302 | review: merge |
| `Interkulturelle` | `interkulturell` | 302 | review: merge |
| `Lebensentwürfe` | `Lebensentwurf` | 302 | review: merge |
| `artgerechten` | `artgerecht` | 302 | review: merge |
| `derselb` | `derselbe` | 302 | review: merge |
| `gebiet` | `Gebiet` | 302 | review: merge |
| `risiko` | `Risiko` | 302 | review: merge |
| `Anzünde` | `anzünden` | 301 | review: merge |
| `Beginne` | `beginnen` | 301 | review: merge |
| `Dreijährig` | `dreijährig` | 301 | review: merge |
| `Entwickel` | `entwickeln` | 301 | review: merge |
| `Followern` | `Follower` | 301 | review: merge |
| `Homöopathen` | `Homöopath` | 301 | review: merge |
| `Hüft` | `Hüfte` | 301 | review: merge |
| `Lnder` | `Land` | 301 | review: merge |
| `Wasserfest` | `wasserfest` | 301 | review: merge |
| `Zubettgehe` | `zubettgehen` | 301 | review: merge |
| `brill` | `Brille` | 301 | review: merge |
| `domina` | `Domina` | 301 | review: merge |
| `freigesetzt` | `freisetzen` | 301 | review: merge |
| `insbes` | `insbesondere` | 301 | review: merge |
| `kirch` | `Kirche` | 301 | review: merge |
| `lächelnd` | `lächeln` | 301 | review: merge |
| `quatsch` | `Quatsch` | 301 | review: merge |
| `gerahmt` | `rahmen` | 300 | review: merge |
| `hinausgehend` | `hinausgehen` | 300 | review: merge |
| `runderneuert` | `runderneuern` | 300 | review: merge |
| `staunend` | `staunen` | 300 | review: merge |
| `auferstanden` | `auferstehen` | 299 | review: merge |
| `explodierend` | `explodieren` | 299 | review: merge |
| `trocknend` | `trocknen` | 298 | review: merge |
| `aufgebläht` | `aufblähen` | 297 | review: merge |
| `erdacht` | `erdenken` | 297 | review: merge |
| `weinend` | `weinen` | 297 | review: merge |
| `angespart` | `ansparen` | 296 | review: merge |
| `gestrandet` | `stranden` | 295 | review: merge |
| `ausgelöst` | `auslösen` | 293 | review: merge |
| `WLan` | `WLAN` | 292 | review: merge |
| `Keinerlei` | `keinerlei` | 289 | review: merge |
| `Neunte` | `neunte` | 288 | review: merge |
| `flackernd` | `flackern` | 286 | review: merge |
| `dringendst` | `dringend` | 285 | review: merge |
| `gebleicht` | `bleichen` | 284 | review: merge |
| `Gyro` | `Gyros` | 282 | review: merge |
| `Grafisch` | `grafisch` | 274 | review: merge |
| `Mantras` | `Mantra` | 274 | review: merge |
| `Slaw` | `Slawe` | 274 | review: merge |
| `Sukkulent` | `Sukkulente` | 274 | review: merge |
| `Versteh` | `verstehen` | 274 | review: merge |
| `agentur` | `Agentur` | 274 | review: merge |
| `bildergalerie` | `Bildergalerie` | 274 | review: merge |
| `seyn` | `sein` | 274 | review: merge |
| `stattfindend` | `stattfinden` | 274 | review: merge |
| `strategie` | `Strategie` | 274 | review: merge |
| `transnationalen` | `transnational` | 274 | review: merge |
| `warn` | `sein` | 274 | review: merge |
| `Bloß` | `bloß` | 273 | review: merge |
| `Evang` | `evangelisch` | 273 | review: merge |
| `Umkleiden` | `Umkleide` | 273 | review: merge |
| `dahintersteckt` | `dahinterstecken` | 273 | review: merge |
| `eichel` | `Eichel` | 273 | review: merge |
| `eis` | `Eis` | 273 | review: merge |
| `liebsen` | `lieb` | 273 | review: merge |
| `montiert` | `montieren` | 273 | review: merge |
| `std` | `Stunde` | 273 | review: merge |
| `unger` | `ungern` | 273 | review: merge |
| `verfgt` | `verfügen` | 273 | review: merge |
| `zuschau` | `zuschauen` | 273 | review: merge |
| `überhand` | `überhandnehmen` | 273 | review: merge |
| `Familienfreundliche` | `familienfreundlich` | 272 | review: merge |
| `Goodies` | `Goodie` | 272 | review: merge |
| `Heimwerk` | `heimwerken` | 272 | review: merge |
| `Röm` | `römisch` | 272 | review: merge |
| `Sportfreunde` | `Sportfreund` | 272 | review: merge |
| `Unternehmensprozesse` | `Unternehmensprozess` | 272 | review: merge |
| `Verzieren` | `verzieren` | 272 | review: merge |
| `blumen` | `Blume` | 272 | review: merge |
| `gehobelt` | `hobeln` | 272 | review: merge |
| `hippe` | `hip` | 272 | review: merge |
| `hunde` | `Hund` | 272 | review: merge |
| `mix` | `Mix` | 272 | review: merge |
| `moglich` | `möglich` | 272 | review: merge |
| `reinigung` | `Reinigung` | 272 | review: merge |
| `rohr` | `Rohr` | 272 | review: merge |
| `slip` | `Slip` | 272 | review: merge |
| `Ggf` | `gegebenenfalls` | 271 | review: merge |
| `Ländliche` | `ländlich` | 271 | review: merge |
| `Pressen` | `pressen` | 271 | review: merge |
| `anstehend` | `anstehen` | 271 | review: merge |
| `Dolmetschen` | `dolmetschen` | 270 | review: merge |
| `mitreisend` | `mitreisen` | 270 | review: merge |
| `aufgewachsen` | `aufwachsen` | 269 | review: merge |
| `schreibend` | `schreiben` | 266 | review: merge |
| `aufbereitet` | `aufbereiten` | 265 | review: merge |
| `bemehlt` | `bemehlen` | 265 | review: merge |
| `gefräst` | `fräsen` | 265 | review: merge |
| `parkend` | `parken` | 265 | review: merge |
| `versucht` | `versuchen` | 264 | review: merge |
| `Äh` | `äh` | 264 | review: merge |
| `aufkeimend` | `aufkeimen` | 263 | review: merge |
| `eingeweicht` | `einweichen` | 263 | review: merge |
| `gezapft` | `zapfen` | 263 | review: merge |
| `Joa` | `joa` | 260 | review: merge |
| `Einlesen` | `einlesen` | 259 | review: merge |
| `Erweiterte` | `erweitern` | 256 | review: merge |
| `ausgelagert` | `auslagern` | 256 | review: merge |
| `geeint` | `einen` | 256 | review: merge |
| `tiefgefroren` | `tiefgefrieren` | 256 | review: merge |
| `fassten` | `fassen` | 255 | review: merge |
| `gleichkommt` | `gleichkommen` | 255 | review: merge |
| `gramm` | `Gramm` | 255 | review: merge |
| `Aussetz` | `aussetzen` | 254 | review: merge |
| `Endmontag` | `Endmontage` | 254 | review: merge |
| `Farbtön` | `Farbton` | 254 | review: merge |
| `Festsetzunge` | `Festsetzung` | 254 | review: merge |
| `GROSSE` | `groß` | 254 | review: merge |
| `Magnolia` | `Magnolie` | 254 | review: merge |
| `Publizier` | `publizieren` | 254 | review: merge |
| `dahinterstehend` | `dahinterstehen` | 254 | review: merge |
| `durchring` | `durchringen` | 254 | review: merge |
| `gemeinden` | `Gemeinde` | 254 | review: merge |
| `richtungsweisen` | `richtungsweisend` | 254 | review: merge |
| `Animes` | `Anime` | 253 | review: merge |
| `Beschrift` | `beschriften` | 253 | review: merge |
| `EDITION` | `Edition` | 253 | review: merge |
| `KLICKEN` | `klicken` | 253 | review: merge |
| `Tagescrem` | `Tagescreme` | 253 | review: merge |
| `Transformier` | `transformieren` | 253 | review: merge |
| `UNIVERSITÄT` | `Universität` | 253 | review: merge |
| `WASSER` | `Wasser` | 253 | review: merge |
| `zurückzusendend` | `zurücksenden` | 253 | review: merge |
| `AWARD` | `Award` | 252 | review: merge |
| `Baden-Wrttemberg` | `Baden-Württemberg` | 252 | review: merge |
| `Buchempfehlunge` | `Buchempfehlung` | 252 | review: merge |
| `DÜSSELDORF` | `Düsseldorf` | 252 | review: merge |
| `GLOBAL` | `global` | 252 | review: merge |
| `Kohort` | `Kohorte` | 252 | review: merge |
| `Rechtspfleg` | `Rechtspflege` | 252 | review: merge |
| `Büchereie` | `Bücherei` | 251 | review: merge |
| `Datenrat` | `Datenrate` | 251 | review: merge |
| `FAX` | `Fax` | 251 | review: merge |
| `Gerst` | `Gerste` | 251 | review: merge |
| `Kleiderstang` | `Kleiderstange` | 251 | review: merge |
| `Körperpfleg` | `Körperpflege` | 251 | review: merge |
| `Praxisbeispiele` | `Praxisbeispiel` | 251 | review: merge |
| `RUNDSCHAU` | `Rundschau` | 251 | review: merge |
| `Stickereien` | `Stickerei` | 251 | review: merge |
| `Webcams` | `Webcam` | 251 | review: merge |
| `Böhmische` | `böhmisch` | 252 | review: merge |
| `Einsteigen` | `einsteigen` | 252 | review: merge |
| `Est` | `Este` | 252 | review: merge |
| `Fantastische` | `fantastisch` | 252 | review: merge |
| `Gabion` | `Gabione` | 252 | review: merge |
| `Pflanzgefäße` | `Pflanzgefäß` | 252 | review: merge |
| `Rezi` | `Rezension` | 252 | review: merge |
| `Spazier` | `spazieren` | 252 | review: merge |
| `allermeisten` | `meist` | 252 | review: merge |
| `ausgerufen` | `ausrufen` | 252 | review: merge |
| `biedern` | `bieder` | 252 | review: merge |
| `bildern` | `Bild` | 252 | review: merge |
| `gegenber` | `gegenüber` | 252 | review: merge |
| `gehypt` | `hypen` | 252 | review: merge |
| `letzlich` | `letztlich` | 252 | review: merge |
| `mails` | `Mail` | 252 | review: merge |
| `müsstet` | `müssen` | 252 | review: merge |
| `vorsicht` | `Vorsicht` | 252 | review: merge |
| `wollend` | `wollen` | 252 | review: merge |
| `zweckmässig` | `zweckmäßig` | 252 | review: merge |
| `Buggys` | `Buggy` | 251 | review: merge |
| `Fertigungsprozesse` | `Fertigungsprozess` | 251 | review: merge |
| `Kontrakte` | `Kontrakt` | 251 | review: merge |
| `Käpt` | `Kapitän` | 251 | review: merge |
| `Mainboards` | `Mainboard` | 251 | review: merge |
| `Nachteilig` | `nachteilig` | 251 | review: merge |
| `Rtl` | `RTL` | 251 | review: merge |
| `Sparfüchse` | `Sparfuchs` | 251 | review: merge |
| `UHR` | `Uhr` | 251 | review: merge |
| `Verfassen` | `verfassen` | 251 | review: merge |
| `abgesperrt` | `absperren` | 251 | review: merge |
| `ausgeliehen` | `ausleihen` | 251 | review: merge |
| `durchzuführen` | `durchführen` | 251 | review: merge |
| `flankierend` | `flankieren` | 251 | review: merge |
| `katzen` | `Katze` | 251 | review: merge |
| `vorhänge` | `Vorhang` | 251 | review: merge |
| `Devot` | `devot` | 250 | review: merge |
| `Diuretika` | `Diuretikum` | 250 | review: merge |
| `Fußsohl` | `Fußsohle` | 250 | review: merge |
| `Kundenwünsch` | `Kundenwunsch` | 250 | review: merge |
| `SUCHEN` | `suchen` | 250 | review: merge |
| `Herunterfahre` | `herunterfahren` | 249 | review: merge |
| `Meckern` | `meckern` | 250 | review: merge |
| `Moeglichkeit` | `Möglichkeit` | 250 | review: merge |
| `anspruch` | `Anspruch` | 250 | review: merge |
| `aufragend` | `aufragen` | 250 | review: merge |
| `ausgelaufen` | `auslaufen` | 250 | review: merge |
| `einzuhauchen` | `einhauchen` | 250 | review: merge |
| `gefütterte` | `gefüttert` | 250 | review: merge |
| `gestrafft` | `straffen` | 250 | review: merge |
| `gestuft` | `stufen` | 250 | review: merge |
| `inkludiert` | `inkludieren` | 250 | review: merge |
| `regal` | `Regal` | 250 | review: merge |
| `revitalisiert` | `revitalisieren` | 250 | review: merge |
| `salz` | `Salz` | 250 | review: merge |
| `spielend` | `spielen` | 250 | review: merge |
| `umjubelt` | `umjubeln` | 250 | review: merge |
| `unbefugtem` | `unbefugt` | 250 | review: merge |
| `wiederaufgebaut` | `wiederaufbauen` | 250 | review: merge |
| `ziehn` | `ziehen` | 250 | review: merge |
| `zwickt` | `zwicken` | 250 | review: merge |
| `Boß` | `Boss` | 249 | review: merge |
| `Kajaks` | `Kajak` | 249 | review: merge |
| `Karnevaliste` | `Karnevalist` | 249 | review: merge |
| `Kommunistisch` | `kommunistisch` | 249 | review: merge |
| `Königlich` | `königlich` | 249 | review: merge |
| `Lkr` | `Landkreis` | 249 | review: merge |
| `Objekte` | `Objekt` | 249 | review: merge |
| `Pris` | `Prise` | 249 | review: merge |
| `Sitzbänk` | `Sitzbank` | 249 | review: merge |
| `Südliche` | `südlich` | 249 | review: merge |
| `Traden` | `traden` | 249 | review: merge |
| `angerufen` | `anrufen` | 249 | review: merge |
| `blondin` | `Blondine` | 249 | review: merge |
| `gewalt` | `Gewalt` | 249 | review: merge |
| `cover` | `Cover` | 249 | review: merge |
| `hamm` | `haben` | 249 | review: merge |
| `Gunter` | `Günter` | 691 | accented spelling 9,395 vs 691 |
| `Gartner` | `Gärtner` | 643 | accented spelling 6,048 vs 643 |
| `Lucke` | `Lücke` | 520 | accented spelling 12,605 vs 520 |
| `Kohler` | `Köhler` | 512 | accented spelling 3,870 vs 512 |
| `Gunther` | `Günther` | 483 | accented spelling 8,814 vs 483 |
| `OVP` | `ÖVP` | 433 | accented spelling 5,088 vs 433 |
| `Gruner` | `grün` | 431 | accented spelling 5,556 vs 431 |
| `Bader` | `Bad` | 409 | accented spelling 2,936 vs 409 |
| `Giessen` | `gießen` | 310 | accented spelling 19,402 vs 310 |
| `Jaeger` | `Jäger` | 307 | accented spelling 12,184 vs 307 |
| `massgeschneiderte` | `maßgeschneidert` | 295 | accented spelling 3,949 vs 295 |
| `beschworen` | `beschwören` | 288 | accented spelling 1,942 vs 288 |
| `anlassen` | `Anlaß` | 277 | accented spelling 2,665 vs 277 |
| `Schroeder` | `Schröder` | 277 | accented spelling 7,229 vs 277 |
| `Grossmutter#mother` | `Großmutter` | 277 | accented spelling 5,784 vs 277 |
| `Tribune` | `Tribüne` | 274 | accented spelling 2,362 vs 274 |
| `gewahr` | `Gewähr` | 273 | accented spelling 16,174 vs 273 |
| `heissem` | `heiß` | 261 | accented spelling 2,213 vs 261 |
| `naechsten` | `nächst` | 260 | accented spelling 101,314 vs 260 |
| `Fussballspiel` | `Fußballspiel` | 259 | accented spelling 2,409 vs 259 |
| `mittelgross` | `mittelgroß` | 254 | accented spelling 3,494 vs 254 |
| `weissem` | `weiß` | 252 | accented spelling 2,778 vs 252 |
| `erhalt` | `erhalten` | 252 | accented spelling 35,204 vs 252 |
| `frueh` | `früh` | 251 | accented spelling 70,206 vs 251 |
| `SPO` | `SPÖ` | 249 | accented spelling 4,804 vs 249 |
| `verfugen` | `verfügen` | 243 | accented spelling 98,662 vs 243 |
| `laeng` | `läng` | 241 | accented spelling 2,371 vs 241 |
| `Lugner` | `Lügner` | 239 | accented spelling 1,977 vs 239 |
| `Weissen` | `weiß` | 236 | accented spelling 16,250 vs 236 |
| `Dune` | `Düne` | 236 | accented spelling 2,528 vs 236 |
| `walzen` | `wälzen` | 235 | accented spelling 2,006 vs 235 |
| `Preussen` | `Preußen` | 234 | accented spelling 4,438 vs 234 |
| `Aussenpolitik` | `Außenpolitik` | 232 | accented spelling 3,198 vs 232 |
| `Goetz` | `Götz` | 229 | accented spelling 3,289 vs 229 |
| `Gmund` | `Gmünd` | 228 | accented spelling 1,796 vs 228 |
| `Massstab` | `Maßstab` | 228 | accented spelling 12,310 vs 228 |
| `sassen` | `sitzen` | 226 | accented spelling 3,107 vs 226 |
| `Sass` | `sitzen` | 225 | accented spelling 6,907 vs 225 |
| `Grosseltern` | `Großeltern` | 225 | accented spelling 6,872 vs 225 |
| `Anstoss` | `Anstoß` | 221 | accented spelling 3,747 vs 221 |
| `Kraemer` | `Krämer` | 220 | accented spelling 1,844 vs 220 |
| `Weisser` | `weiß` | 219 | accented spelling 5,466 vs 219 |
| `Verstoss` | `Verstoß` | 218 | accented spelling 13,889 vs 218 |
| `mUSS` | `müssen` | 217 | accented spelling 23,618 vs 217 |
| `Kruger` | `Krüger` | 215 | accented spelling 3,977 vs 215 |
| `aehnlich` | `ähnlich` | 212 | accented spelling 112,017 vs 212 |
| `Blaser` | `Bläser` | 211 | accented spelling 1,257 vs 211 |
| `GROSS` | `groß` | 208 | accented spelling 687,180 vs 208 |
| `Grossraum` | `Großraum` | 208 | accented spelling 4,677 vs 208 |
| `daruber` | `darüber` | 206 | accented spelling 256,011 vs 206 |
| `erschliessen` | `erschließen` | 206 | accented spelling 8,949 vs 206 |
| `Strassburg` | `Straßburg` | 205 | accented spelling 3,533 vs 205 |
| `Grossvater` | `Großvater` | 204 | accented spelling 5,229 vs 204 |
| `Erschliessung` | `Erschließung` | 203 | accented spelling 3,633 vs 203 |
| `fahig` | `fähig` | 201 | accented spelling 6,984 vs 201 |
| `Schoss` | `schießen` | 199 | accented spelling 1,694 vs 199 |
| `verliess` | `verlassen` | 199 | accented spelling 3,503 vs 199 |
| `gabe` | `geben` | 198 | accented spelling 7,483 vs 198 |
| `blosse` | `bloß` | 196 | accented spelling 2,028 vs 196 |
| `Fussboden` | `Fußboden` | 192 | accented spelling 3,985 vs 192 |
| `zusaetzlich` | `zusätzlich` | 192 | accented spelling 203,159 vs 192 |
| `zusatzlich` | `zusätzlich` | 190 | accented spelling 203,159 vs 190 |
| `Buchner` | `Büchner` | 190 | accented spelling 1,046 vs 190 |
| `Schoner` | `schön` | 188 | accented spelling 20,704 vs 188 |
| `Grossstadt` | `Großstadt` | 186 | accented spelling 8,318 vs 186 |
| `BADER` | `Bad` | 183 | accented spelling 2,936 vs 183 |
| `Worth` | `Wörth` | 182 | accented spelling 1,677 vs 182 |
| `Ara` | `Ära` | 182 | accented spelling 6,242 vs 182 |
| `koennt` | `können` | 182 | accented spelling 55,166 vs 182 |
| `Strassenbahn` | `Straßenbahn` | 180 | accented spelling 5,253 vs 180 |
| `Fussweg` | `Fußweg` | 178 | accented spelling 3,514 vs 178 |
| `Wolfe` | `Wolf` | 177 | accented spelling 2,248 vs 177 |
| `Walder` | `Wald` | 176 | accented spelling 4,948 vs 176 |
| `weisser` | `weiß` | 173 | accented spelling 5,466 vs 173 |
| `Aussenseiter` | `Außenseiter` | 172 | accented spelling 2,706 vs 172 |
| `Spielspass` | `Spielspaß` | 171 | accented spelling 3,422 vs 171 |
| `Duster` | `düster` | 171 | accented spelling 5,731 vs 171 |
| `ARA` | `Ära` | 170 | accented spelling 6,242 vs 170 |
| `wuerden` | `werden` | 169 | accented spelling 62,603 vs 169 |
| `zugange` | `Zugang` | 169 | accented spelling 1,676 vs 169 |
| `anzuschliessen` | `anschließen` | 168 | accented spelling 1,150 vs 168 |
| `Topfen` | `Topf` | 165 | accented spelling 838 vs 165 |
| `Fussbodenheizung` | `Fußbodenheizung` | 165 | accented spelling 3,877 vs 165 |
| `Verschleiss` | `Verschleiß` | 164 | accented spelling 4,461 vs 164 |
| `Rachen` | `rächen` | 164 | accented spelling 1,181 vs 164 |
| `Aussenseite` | `Außenseite` | 163 | accented spelling 2,931 vs 163 |
| `lad` | `läd` | 163 | accented spelling 818 vs 163 |
| `verliessen` | `verlassen` | 160 | accented spelling 1,601 vs 160 |
| `Oeko-Tex` | `Öko-Tex` | 159 | accented spelling 914 vs 159 |
| `Jah` | `jäh` | 159 | accented spelling 1,000 vs 159 |
| `Weissensee` | `Weißensee` | 158 | accented spelling 1,048 vs 158 |
| `Waren` | `sein` | 158 | accented spelling 27,946 vs 158 |
| `Aussenanlage` | `Außenanlage` | 157 | accented spelling 1,633 vs 157 |
| `Goebel` | `Göbel` | 157 | accented spelling 937 vs 157 |
| `bader` | `Bad` | 156 | accented spelling 2,936 vs 156 |
| `uebrigens` | `übrigens` | 156 | accented spelling 79,828 vs 156 |
| `erschliesst` | `erschließen` | 156 | accented spelling 1,567 vs 156 |
| `gespurt` | `spüren` | 155 | accented spelling 1,179 vs 155 |
| `russ` | `Ruß` | 155 | accented spelling 1,134 vs 155 |
| `spassig` | `spaßig` | 154 | accented spelling 1,693 vs 154 |
| `gewissermassen` | `gewissermaßen` | 154 | accented spelling 3,200 vs 154 |
| `Weissrussland` | `Weißrussland` | 154 | accented spelling 2,003 vs 154 |
| `Muench` | `Münch` | 153 | accented spelling 1,190 vs 153 |
| `Hansel` | `Hänsel` | 153 | accented spelling 1,052 vs 153 |
| `Geniesse` | `genießen` | 151 | accented spelling 3,809 vs 151 |
| `Grunwald` | `Grünwald` | 150 | accented spelling 1,044 vs 150 |
| `Strassenrand` | `Straßenrand` | 146 | accented spelling 2,243 vs 146 |
| `heisst` | `heißen` | 145 | accented spelling 73,587 vs 145 |
| `Joerg` | `Jörg` | 145 | accented spelling 16,655 vs 145 |
| `Fussballfan` | `Fußballfan` | 144 | accented spelling 1,443 vs 144 |
| `hoeher` | `hoch` | 144 | accented spelling 26,456 vs 144 |
| `naemlich` | `nämlich` | 144 | accented spelling 93,195 vs 144 |
| `tatsaechlich` | `tatsächlich` | 143 | accented spelling 122,579 vs 143 |
| `Weissgold` | `Weißgold` | 140 | accented spelling 965 vs 140 |
| `anschliessender` | `anschließend` | 139 | accented spelling 1,748 vs 139 |
| `fande` | `finden` | 139 | accented spelling 1,774 vs 139 |
| `Grosskonzern` | `Großkonzern` | 138 | accented spelling 1,014 vs 138 |
| `Wurmer` | `Wurm` | 138 | accented spelling 2,730 vs 138 |
| `Laufer` | `Läufer` | 137 | accented spelling 8,180 vs 137 |
| `Anlasse` | `Anlass` | 136 | accented spelling 3,860 vs 136 |
| `Grossprojekt` | `Großprojekt` | 136 | accented spelling 1,755 vs 136 |
| `waeren` | `sein` | 136 | accented spelling 27,946 vs 136 |
| `Wachter` | `Wächter` | 135 | accented spelling 3,445 vs 135 |
| `EPU` | `EPÜ` | 134 | accented spelling 929 vs 134 |
| `Beschlage` | `Beschlag` | 133 | accented spelling 836 vs 133 |
| `tatsachlich` | `tatsächlich` | 133 | accented spelling 122,579 vs 133 |
| `anschliessendem` | `anschließend` | 133 | accented spelling 1,128 vs 133 |
| `Oekonomie` | `Ökonomie` | 132 | accented spelling 5,198 vs 132 |
| `Menus` | `Menü` | 132 | accented spelling 2,614 vs 132 |
| `haufig` | `häufig` | 131 | accented spelling 153,011 vs 131 |
| `hinreissen` | `hinreißen` | 131 | accented spelling 1,407 vs 131 |
| `gunther` | `Günther` | 131 | accented spelling 8,814 vs 131 |
| `Foerster` | `Förster` | 131 | accented spelling 2,544 vs 131 |
| `Grossunternehmen` | `Großunternehmen` | 130 | accented spelling 1,919 vs 130 |
| `Fussball-Weltmeisterschaft` | `Fußball-Weltmeisterschaft` | 130 | accented spelling 1,600 vs 130 |
| `Grusskarte` | `Grußkarte` | 130 | accented spelling 1,682 vs 130 |
| `fruh` | `früh` | 129 | accented spelling 70,206 vs 129 |
| `Graber` | `Gräber` | 129 | accented spelling 2,099 vs 129 |
| `verhangen` | `verhängen` | 129 | accented spelling 4,123 vs 129 |
| `fundig` | `fündig` | 128 | accented spelling 10,998 vs 128 |
| `aussenpolitisch` | `außenpolitisch` | 128 | accented spelling 974 vs 128 |
| `Unfalle` | `Unfall` | 126 | accented spelling 3,759 vs 126 |
| `Moerser` | `Mörser` | 125 | accented spelling 1,212 vs 125 |
| `topfen` | `Topf` | 124 | accented spelling 838 vs 124 |
| `Massgabe` | `Maßgabe` | 124 | accented spelling 6,824 vs 124 |
| `Fussball-WM` | `Fußball-WM` | 123 | accented spelling 2,192 vs 123 |
| `Debutalbum` | `Debütalbum` | 123 | accented spelling 1,950 vs 123 |
| `Fleiss` | `Fleiß` | 123 | accented spelling 2,202 vs 123 |
| `Freistoss` | `Freistoß` | 122 | accented spelling 2,901 vs 122 |
| `offnen` | `öffnen` | 122 | accented spelling 118,270 vs 122 |
| `Kammerer` | `Kämmerer` | 121 | accented spelling 790 vs 121 |
| `Fahrspass` | `Fahrspaß` | 121 | accented spelling 2,358 vs 121 |
| `Fussmatte` | `Fußmatte` | 120 | accented spelling 949 vs 120 |
| `antragen` | `Antrag` | 119 | accented spelling 1,269 vs 119 |
| `Aussenwelt` | `Außenwelt` | 119 | accented spelling 2,124 vs 119 |
| `Aussenministerium` | `Außenministerium` | 117 | accented spelling 1,961 vs 117 |
| `mitreissen` | `mitreißen` | 117 | accented spelling 2,023 vs 117 |
| `Geissler` | `Geißler` | 115 | accented spelling 794 vs 115 |
| `Strassenseite` | `Straßenseite` | 112 | accented spelling 1,861 vs 112 |
| `Koehler` | `Köhler` | 112 | accented spelling 3,870 vs 112 |
| `koennten` | `können` | 112 | accented spelling 49,157 vs 112 |
| `Proll` | `Pröll` | 112 | accented spelling 738 vs 112 |
| `Aussenspiegel` | `Außenspiegel` | 112 | accented spelling 1,540 vs 112 |
| `stiessen` | `stoßen` | 111 | accented spelling 977 vs 111 |
| `Tucher` | `Tuch` | 111 | accented spelling 2,018 vs 111 |
| `Juerg` | `Jürg` | 111 | accented spelling 1,661 vs 111 |
| `weisses` | `weiß` | 110 | accented spelling 3,272 vs 110 |
| `Lunette` | `Lünette` | 110 | accented spelling 805 vs 110 |
| `masslos` | `maßlos` | 109 | accented spelling 1,173 vs 109 |
| `besass` | `besitzen` | 109 | accented spelling 1,831 vs 109 |
| `Umfasst` | `umfassen` | 107 | accented spelling 934 vs 107 |
| `dufte` | `Duft` | 106 | accented spelling 2,370 vs 106 |
| `riesengross` | `riesengroß` | 105 | accented spelling 1,802 vs 105 |
| `Preuss` | `Preuß` | 105 | accented spelling 690 vs 105 |
| `Lad` | `läd` | 104 | accented spelling 818 vs 104 |
| `Fussballverein` | `Fußballverein` | 102 | accented spelling 1,503 vs 102 |
| `Aussentemperatur` | `Außentemperatur` | 102 | accented spelling 1,613 vs 102 |
| `Ausmasse` | `Ausmaß` | 101 | accented spelling 927 vs 101 |
| `Aussenwand` | `Außenwand` | 100 | accented spelling 1,770 vs 100 |
| `ahnlich` | `ähnlich` | 99 | accented spelling 112,017 vs 99 |
| `Fussabdruck` | `Fußabdruck` | 99 | accented spelling 1,445 vs 99 |
| `Fussballplatz` | `Fußballplatz` | 99 | accented spelling 1,310 vs 99 |
| `Dorfer` | `Dorf` | 99 | accented spelling 3,943 vs 99 |
| `aufklaren` | `aufklären` | 98 | accented spelling 9,434 vs 98 |
| `Fussballverband` | `Fußballverband` | 98 | accented spelling 879 vs 98 |
| `rachen` | `rächen` | 97 | accented spelling 1,181 vs 97 |
| `Krueger` | `Krüger` | 97 | accented spelling 3,977 vs 97 |
| `Taufer` | `Täufer` | 97 | accented spelling 927 vs 97 |
| `behalt` | `behalten` | 96 | accented spelling 4,069 vs 96 |
| `Moeller` | `Möller` | 95 | accented spelling 2,648 vs 95 |
| `abgiessen` | `abgießen` | 94 | accented spelling 2,094 vs 94 |
| `grossformatig` | `großformatig` | 94 | accented spelling 1,248 vs 94 |
| `Fuhre` | `führen` | 93 | accented spelling 3,248 vs 93 |
| `Kuch` | `küch` | 93 | accented spelling 859 vs 93 |
| `Ruediger` | `Rüdiger` | 93 | accented spelling 4,531 vs 93 |
| `Trummer` | `Trümmer` | 92 | accented spelling 1,764 vs 92 |
| `Boehm` | `Böhm` | 92 | accented spelling 2,196 vs 92 |
| `Odem` | `Ödem` | 91 | accented spelling 692 vs 91 |
| `aussergerichtlich` | `außergerichtlich` | 91 | accented spelling 3,378 vs 91 |
| `AUSSCHLIESSLICHER` | `ausschließlich` | 90 | accented spelling 789 vs 90 |
| `Munch` | `Münch` | 90 | accented spelling 1,190 vs 90 |
| `Jager` | `Jäger` | 90 | accented spelling 12,184 vs 90 |
| `Fusspfleg` | `Fußpfleg` | 90 | accented spelling 574 vs 90 |
| `haeufig` | `häufig` | 90 | accented spelling 153,011 vs 90 |
| `Badespass` | `Badespaß` | 89 | accented spelling 1,078 vs 89 |
| `Fussmarsch` | `Fußmarsch` | 88 | accented spelling 884 vs 88 |
| `ploetzlich` | `plötzlich` | 88 | accented spelling 60,277 vs 88 |
| `Vertrage` | `Vertrag` | 88 | accented spelling 9,403 vs 88 |
| `Strassenbau` | `Straßenbau` | 88 | accented spelling 1,861 vs 88 |
| `Meisse` | `Meiße` | 88 | accented spelling 921 vs 88 |
| `fon` | `fönen` | 87 | accented spelling 1,498 vs 87 |
| `Floss` | `fließen` | 87 | accented spelling 500 vs 87 |
| `Fussnote` | `Fußnote` | 86 | accented spelling 1,425 vs 86 |
| `ware` | `sein` | 85 | accented spelling 144,636 vs 85 |
| `Ausstoss` | `Ausstoß` | 85 | accented spelling 1,428 vs 85 |
| `statte` | `Stätte` | 85 | accented spelling 3,043 vs 85 |
| `Menupunkt` | `Menüpunkt` | 85 | accented spelling 5,724 vs 85 |
| `Ausserirdisch` | `außerirdisch` | 85 | accented spelling 1,581 vs 85 |
| `abschliessbar` | `abschließbar` | 84 | accented spelling 1,445 vs 84 |
| `Strassennetz` | `Straßennetz` | 83 | accented spelling 1,792 vs 83 |
| `MUSS#Neut` | `müssen` | 82 | accented spelling 23,618 vs 82 |
| `Spassfaktor` | `Spaßfaktor` | 82 | accented spelling 1,068 vs 82 |
| `ausserirdisch` | `außerirdisch` | 82 | accented spelling 1,581 vs 82 |
| `verschliessbar` | `verschließbar` | 82 | accented spelling 1,097 vs 82 |
| `Gaertner` | `Gärtner` | 82 | accented spelling 6,048 vs 82 |
| `ODP` | `ÖDP` | 82 | accented spelling 492 vs 82 |
| `hinterliess` | `hinterlassen` | 81 | accented spelling 1,048 vs 81 |
| `PASST` | `passen` | 81 | accented spelling 1,346 vs 81 |
| `samtliche` | `sämtlich` | 80 | accented spelling 26,556 vs 80 |
| `verrat` | `verraten` | 80 | accented spelling 5,720 vs 80 |
| `Zuschlage` | `Zuschlag` | 80 | accented spelling 1,339 vs 80 |
| `entschliessen` | `entschließen` | 80 | accented spelling 2,803 vs 80 |
| `haschen` | `Häsch` | 80 | accented spelling 444 vs 80 |
| `Tischfussball` | `Tischfußball` | 80 | accented spelling 433 vs 80 |
| `selbstverstaendlich` | `selbstverständlich` | 80 | accented spelling 74,679 vs 80 |
| `Hauptstrasse` | `Hauptstraße` | 80 | accented spelling 6,523 vs 80 |
| `unabhaengig` | `unabhängig` | 80 | accented spelling 74,170 vs 80 |
| `Linkshand` | `Linkshänd` | 79 | accented spelling 474 vs 79 |
| `Blumenstrauss` | `Blumenstrauß` | 78 | accented spelling 1,736 vs 78 |
| `lastig` | `lästig` | 78 | accented spelling 7,000 vs 78 |
| `hiessen` | `heißen` | 78 | accented spelling 562 vs 78 |
| `wuenschen` | `wünschen` | 78 | accented spelling 145,435 vs 78 |
| `Mohring` | `Möhring` | 78 | accented spelling 444 vs 78 |
| `Statte` | `Stätte` | 77 | accented spelling 3,043 vs 77 |
| `aelter` | `alt` | 77 | accented spelling 9,446 vs 77 |
| `tanze` | `Tanz` | 76 | accented spelling 1,171 vs 76 |
| `Graeber` | `Gräber` | 75 | accented spelling 2,099 vs 75 |
| `LASS` | `lassen` | 75 | accented spelling 1,522 vs 75 |
| `Geniesst` | `genießen` | 75 | accented spelling 6,733 vs 75 |
| `erfasst` | `erfassen` | 74 | accented spelling 468 vs 74 |
| `Heisst` | `heißen` | 74 | accented spelling 73,587 vs 74 |
| `zahnen` | `Zahn` | 74 | accented spelling 2,866 vs 74 |
| `Fussballstadion` | `Fußballstadion` | 74 | accented spelling 699 vs 74 |
| `Rander` | `Rand` | 74 | accented spelling 1,751 vs 74 |
| `namlich` | `nämlich` | 73 | accented spelling 93,195 vs 73 |
| `zellular` | `zellulär` | 73 | accented spelling 438 vs 73 |
| `verschliesst` | `verschließen` | 73 | accented spelling 665 vs 73 |
| `range` | `Rang` | 73 | accented spelling 675 vs 73 |
| `Bussgeld` | `Bußgeld` | 73 | accented spelling 4,401 vs 73 |
| `Fluechtling` | `Flüchtling` | 73 | accented spelling 25,761 vs 73 |
| `Neustadter` | `Neustädter` | 72 | accented spelling 947 vs 72 |
| `Gebusch` | `Gebüsch` | 72 | accented spelling 1,197 vs 72 |
| `Drucken` | `drücken` | 72 | accented spelling 48,434 vs 72 |
| `Ganzkoerpermassage` | `Ganzkörpermassage` | 72 | accented spelling 618 vs 72 |
| `Grafe` | `Gräfe` | 71 | accented spelling 432 vs 71 |
| `grundsaetzlich` | `grundsätzlich` | 71 | accented spelling 86,688 vs 71 |
| `spriessen` | `sprießen` | 71 | accented spelling 1,337 vs 71 |
| `Mariae` | `Maria` | 71 | accented spelling 464 vs 71 |
| `Huter` | `Hüter` | 71 | accented spelling 1,823 vs 71 |
| `ermoeglicht` | `ermöglichen` | 71 | accented spelling 51,979 vs 71 |
| `ruber` | `rüber` | 70 | accented spelling 4,104 vs 70 |
| `emporen` | `empören` | 70 | accented spelling 2,336 vs 70 |
| `Hor` | `hören` | 70 | accented spelling 1,959 vs 70 |
| `Schroder` | `Schröder` | 70 | accented spelling 7,229 vs 70 |
| `gegenwartig` | `gegenwärtig` | 69 | accented spelling 13,188 vs 69 |
| `Fussballclub` | `Fußballclub` | 69 | accented spelling 425 vs 69 |
| `Massnahmenpaket` | `Maßnahmenpaket` | 69 | accented spelling 681 vs 69 |
| `enthalt` | `enthalten` | 69 | accented spelling 49,946 vs 69 |
| `anschliesst` | `anschließen` | 69 | accented spelling 421 vs 69 |
| `Aussenpool` | `Außenpool` | 69 | accented spelling 2,356 vs 69 |
| `anhalt` | `anhalten` | 69 | accented spelling 1,265 vs 69 |
| `massvoll` | `maßvoll` | 68 | accented spelling 525 vs 68 |
| `Karcher` | `Kärcher` | 68 | accented spelling 1,603 vs 68 |
| `Debut-Album` | `Debüt-Album` | 68 | accented spelling 365 vs 68 |
| `Schiesserei` | `Schießerei` | 68 | accented spelling 1,128 vs 68 |
| `zunaechst` | `zunächst` | 68 | accented spelling 131,571 vs 68 |
| `Durkheim` | `Dürkheim` | 68 | accented spelling 760 vs 68 |
| `erschiessen` | `erschießen` | 68 | accented spelling 4,456 vs 68 |
| `scheissegal` | `scheißegal` | 67 | accented spelling 494 vs 67 |
| `Parfumerie` | `Parfümerie` | 67 | accented spelling 1,018 vs 67 |
| `Draeger` | `Dräger` | 67 | accented spelling 1,112 vs 67 |
| `Aussendienstmitarbeiter` | `Außendienstmitarbeiter` | 67 | accented spelling 1,049 vs 67 |
| `Uebernachtung` | `Übernachtung` | 67 | accented spelling 19,899 vs 67 |
| `abzuglich` | `abzüglich` | 66 | accented spelling 2,694 vs 66 |
| `Weissbier` | `Weißbier` | 66 | accented spelling 615 vs 66 |
| `ueblich` | `üblich` | 66 | accented spelling 37,426 vs 66 |
| `Fussballfeld` | `Fußballfeld` | 65 | accented spelling 584 vs 65 |
| `vielfaltig` | `vielfältig` | 65 | accented spelling 42,791 vs 65 |
| `aufreissen` | `aufreißen` | 65 | accented spelling 1,859 vs 65 |
| `passt` | `passen` | 65 | accented spelling 1,346 vs 65 |
| `fussballerisch` | `fußballerisch` | 65 | accented spelling 554 vs 65 |
| `Grusswort` | `Grußwort` | 65 | accented spelling 2,810 vs 65 |
| `Sunder` | `Sünder` | 65 | accented spelling 1,709 vs 65 |
| `oeffnen` | `öffnen` | 64 | accented spelling 118,270 vs 64 |
| `Bohm` | `Böhm` | 64 | accented spelling 2,196 vs 64 |
| `Fussbad` | `Fußbad` | 64 | accented spelling 766 vs 64 |
| `einschliessen` | `einschließen` | 64 | accented spelling 6,941 vs 64 |
| `Zollner` | `Zöllner` | 64 | accented spelling 1,091 vs 64 |
| `praesentiert` | `präsentieren` | 64 | accented spelling 29,000 vs 64 |
| `Dobel` | `Döbel` | 64 | accented spelling 568 vs 64 |
| `Resumee` | `Resümee` | 63 | accented spelling 1,762 vs 63 |
| `Waechter` | `Wächter` | 63 | accented spelling 3,445 vs 63 |
| `Menuepunkt` | `Menüpunkt` | 63 | accented spelling 5,724 vs 63 |
| `Aufzahlung` | `Aufzählung` | 63 | accented spelling 2,228 vs 63 |
| `Druse` | `Drüse` | 63 | accented spelling 804 vs 63 |
| `anschliessenden` | `anschließend` | 63 | accented spelling 3,873 vs 63 |
| `abschliesst` | `abschließen` | 63 | accented spelling 1,409 vs 63 |
| `Eheschliessung` | `Eheschließung` | 63 | accented spelling 2,208 vs 63 |
| `Boller` | `Böller` | 62 | accented spelling 1,004 vs 62 |
| `Daruber` | `darüber` | 62 | accented spelling 256,011 vs 62 |
| `worth` | `Wörth` | 62 | accented spelling 1,677 vs 62 |
| `Verheissung` | `Verheißung` | 62 | accented spelling 1,627 vs 62 |
| `Gauss` | `Gauß` | 62 | accented spelling 380 vs 62 |
| `zugegebenermassen` | `zugegebenermaßen` | 62 | accented spelling 1,744 vs 62 |
| `Graser` | `Gras` | 62 | accented spelling 897 vs 62 |
| `wegschmeissen` | `wegschmeißen` | 62 | accented spelling 726 vs 62 |
| `Tuck` | `Tück` | 62 | accented spelling 629 vs 62 |
| `Berat` | `beraten` | 62 | accented spelling 5,865 vs 62 |
| `Oesterreichischen` | `österreichisch` | 62 | accented spelling 12,950 vs 62 |
| `Gruenwald` | `Grünwald` | 62 | accented spelling 1,044 vs 62 |
| `zukunftig` | `zukünftig` | 61 | accented spelling 37,879 vs 61 |
| `Heisser` | `heiß` | 61 | accented spelling 2,917 vs 61 |
| `ungefaehr` | `ungefähr` | 61 | accented spelling 32,918 vs 61 |
| `urspruenglich` | `ursprünglich` | 61 | accented spelling 49,415 vs 61 |
| `assen` | `essen` | 61 | accented spelling 749 vs 61 |
| `gunter` | `Günter` | 61 | accented spelling 9,395 vs 61 |
| `Zuechter` | `Züchter` | 61 | accented spelling 4,938 vs 61 |
| `KOEHLER` | `Köhler` | 61 | accented spelling 3,870 vs 61 |

### Dropped by 2+ flags: random sample of 0 of 0 in the window

| rank | lemma | flags |
|---:|---|---|

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 19,298 (keep 8,665, drop 10,633); review merges: 5,601.

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
| 1,858,929 | - | 14.0% | - | - | 22.1% | - | - | 32.0% | - | - | 46.5% | - |
| 3,228,275 | 15.4% | 12.8% | 1.21 | 23.5% | 19.1% | 1.23 | 33.5% | 28.3% | 1.18 | 50.2% | 41.8% | 1.20 |
| 5,035,140 | 15.4% | 10.9% | 1.41 | 23.5% | 17.9% | 1.32 | 33.5% | 25.9% | 1.30 | 50.2% | 38.9% | 1.29 |
| 7,843,966 | 15.4% | 14.8% | 1.04 | 23.5% | 18.4% | 1.28 | 33.5% | 24.9% | 1.35 | 50.2% | 36.8% | 1.36 |
| 11,145,054 | 11.4% | 19.4% | 0.59 | 16.0% | 20.9% | 0.76 | 23.9% | 26.3% | 0.91 | 38.4% | 36.2% | 1.06 |
| 12,858,618 | 10.2% | 17.3% | 0.59 | 13.8% | 19.4% | 0.71 | 20.8% | 24.8% | 0.84 | 34.0% | 34.8% | 0.98 |
| 14,661,404 | 10.2% | 16.3% | 0.63 | 13.8% | 18.6% | 0.75 | 20.8% | 24.2% | 0.86 | 34.0% | 34.3% | 0.99 |
| 16,598,866 | 9.0% | 15.2% | 0.59 | 13.2% | 17.9% | 0.74 | 19.3% | 23.7% | 0.81 | 30.8% | 33.6% | 0.92 |
| 18,137,485 | 9.0% | 14.5% | 0.62 | 13.2% | 17.2% | 0.77 | 19.3% | 23.1% | 0.84 | 30.8% | 33.1% | 0.93 |
| 19,961,780 | 8.2% | 13.8% | 0.59 | 12.3% | 16.4% | 0.75 | 17.8% | 22.7% | 0.79 | 28.4% | 32.5% | 0.87 |
| 21,607,573 | 8.2% | 13.3% | 0.62 | 12.3% | 16.2% | 0.76 | 17.8% | 22.5% | 0.79 | 28.4% | 32.3% | 0.88 |
| 23,438,824 | 8.6% | 12.8% | 0.67 | 12.3% | 15.8% | 0.78 | 17.5% | 22.1% | 0.79 | 27.2% | 31.9% | 0.85 |
| 30,163,693 | 7.2% | 11.4% | 0.63 | 10.2% | 14.8% | 0.69 | 15.2% | 21.4% | 0.71 | 24.1% | 30.9% | 0.78 |
| 35,680,128 | 6.8% | 10.6% | 0.64 | 9.7% | 14.4% | 0.67 | 14.1% | 21.0% | 0.67 | 22.7% | 30.5% | 0.75 |
| 37,460,081 | 6.1% | 10.4% | 0.58 | 8.6% | 14.3% | 0.61 | 13.3% | 20.8% | 0.64 | 21.3% | 30.2% | 0.71 |
| 41,345,162 | 6.1% | 10.1% | 0.60 | 8.6% | 13.9% | 0.62 | 12.8% | 20.7% | 0.62 | 20.5% | 30.0% | 0.68 |
| 44,367,274 | 5.7% | 9.7% | 0.59 | 7.9% | 13.7% | 0.58 | 12.1% | 20.5% | 0.59 | 19.8% | 29.8% | 0.67 |
| 75,475,936 | 5.2% | 8.3% | 0.63 | 7.4% | 13.5% | 0.55 | 10.5% | 20.2% | 0.52 | 16.8% | 29.4% | 0.57 |
| 107,046,033 | 4.5% | 8.0% | 0.56 | 6.2% | 13.1% | 0.48 | 9.2% | 20.0% | 0.46 | 14.3% | 29.1% | 0.49 |
| 139,877,087 | 4.1% | 8.0% | 0.51 | 5.3% | 13.0% | 0.41 | 8.0% | 20.3% | 0.39 | 12.6% | 29.3% | 0.43 |
| 176,047,733 | 3.8% | 7.8% | 0.49 | 5.0% | 12.9% | 0.39 | 7.3% | 20.0% | 0.36 | 11.4% | 29.3% | 0.39 |
| 217,170,036 | 3.3% | 7.7% | 0.43 | 4.5% | 12.9% | 0.35 | 6.5% | 20.0% | 0.33 | 10.1% | 29.3% | 0.35 |
| 262,241,563 | 3.0% | 7.7% | 0.39 | 3.8% | 12.9% | 0.30 | 5.7% | 20.0% | 0.29 | 9.0% | 29.3% | 0.31 |
| 350,250,058 | 2.6% | 7.8% | 0.34 | 3.3% | 12.9% | 0.26 | 5.1% | 20.0% | 0.25 | 7.9% | 29.6% | 0.27 |
| 385,935,865 | 2.5% | 7.8% | 0.32 | 3.1% | 13.0% | 0.24 | 4.8% | 20.0% | 0.24 | 7.4% | 29.6% | 0.25 |
| 411,513,342 | 2.3% | 7.7% | 0.30 | 2.9% | 12.9% | 0.22 | 4.5% | 20.0% | 0.22 | 7.1% | 29.5% | 0.24 |
| 440,125,254 | 2.1% | 7.6% | 0.27 | 2.9% | 12.9% | 0.22 | 4.3% | 19.9% | 0.22 | 6.8% | 29.5% | 0.23 |

