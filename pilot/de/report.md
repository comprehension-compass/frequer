# Review report: de (pilot)

- Ranking score: `frequency`; 200,000 candidate lemmas ranked.
- Tokens counted: 8,083,748 in 25,910 documents, 25 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_de` 1.4.0 (sha256 `502a095210e9d550`); fallback `spacy-list`, units on; honeyeater `0e1c3bbbd941`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-de | 24 | 24,311 | 324,015 | 7,496,902 | alpha 7,060, exact_dup 24,492, gap 12,434, langid 18,901, length 71,358, near_dup 5,312 |
| tatoeba-deu | 1 | 1,599 | 79,576 | 586,846 | alpha 1, gap 44, length 44, near_dup 285 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 153,276. Sentences: 750,866.

## Units

Counted occurrences by kind: compound 40,729 (0.50%), compound1 831,311 (10.28%), construction 99,770 (1.23%), phrase 87,678 (1.08%), word 7,024,260 (86.89%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 102,712 | 888,859 |
| construction | 15 | 99,977 |
| phrase | 896 | 87,768 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `damit` | 6,902 | 4,688 | 112 |
| `dabei` | 6,049 | 4,209 | 120 |
| `dazu` | 4,910 | 3,501 | 151 |
| `anbieten` | 4,494 | 2,523 | 158 |
| `natürlich` | 4,421 | 2,939 | 160 |
| `dafür` | 3,310 | 2,505 | 229 |
| `Möglichkeit` | 3,144 | 2,259 | 241 |
| `kostenlos` | 3,116 | 1,692 | 244 |
| `persönlich` | 2,944 | 2,005 | 253 |
| `darauf` | 2,750 | 2,137 | 265 |
| `bestellen` | 2,675 | 1,390 | 269 |
| `verbinden` | 2,667 | 1,914 | 271 |
| `herstellen` | 2,651 | 1,697 | 268 |
| `zusätzlich` | 2,506 | 1,831 | 289 |
| `Erfahrung` | 2,479 | 1,829 | 294 |
| `darüber` | 2,435 | 1,969 | 302 |
| `sich befinden` | 2,416 | 1,732 | 306 |
| `davon` | 2,350 | 1,866 | 312 |
| `bearbeiten` | 2,294 | 910 | 317 |
| `Leistung` | 2,236 | 1,389 | 324 |
| `anwenden` | 2,048 | 1,207 | 348 |
| `vorstellen` | 2,012 | 1,565 | 394 |
| `unterschiedlich` | 1,989 | 1,530 | 366 |
| `sich freuen` | 1,933 | 1,564 | 621 |
| `Entwicklung` | 1,924 | 1,355 | 378 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `werden + Partizip II` | 56,632 | 15,866 | 18 |
| `werden + Infinitiv` | 9,988 | 5,812 | 88 |
| `sein + Partizip II` | 9,972 | 6,166 | 89 |
| `um … zu + Infinitiv` | 9,853 | 5,827 | 91 |
| `lassen + Infinitiv` | 5,554 | 3,931 | 129 |
| `würde + Infinitiv` | 4,037 | 2,500 | 176 |
| `sein + zu + Infinitiv` | 2,355 | 1,858 | 313 |
| `gehen + Infinitiv` | 560 | 489 | 1451 |
| `ohne … zu + Infinitiv` | 498 | 445 | 1609 |
| `haben … zu + Infinitiv` | 397 | 375 | 2329 |
| `werden + Infinitiv Perfekt` | 74 | 69 | 7012 |
| `Modalverb + Infinitiv Perfekt` | 30 | 30 | 13557 |
| `statt … zu + Infinitiv` | 16 | 15 | 22661 |
| `(an)statt … zu + Infinitiv` | 9 | 9 | 33577 |
| `vorhaben + zu + Infinitiv` | 2 | 2 | 153470 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `es gibt` | 12,047 | 6,393 | 76 |
| `nicht mehr` | 3,476 | 2,462 | 219 |
| `vor allem` | 2,641 | 1,989 | 274 |
| `ein paar` | 2,043 | 1,567 | 355 |
| `für etwas sorgen` | 1,718 | 1,357 | 426 |
| `zum Beispiel` | 1,549 | 1,175 | 482 |
| `zu etwas gehören` | 1,512 | 1,245 | 493 |
| `nicht nur … sondern auch` | 1,317 | 1,135 | 580 |
| `im Rahmen` | 1,301 | 998 | 590 |
| `unter anderem` | 1,275 | 1,081 | 603 |
| `es handelt sich um etwas` | 1,251 | 906 | 626 |
| `immer wieder` | 1,251 | 1,051 | 627 |
| `über etwas verfügen` | 1,226 | 923 | 641 |
| `sowohl … als auch` | 1,202 | 1,058 | 657 |
| `immer noch` | 1,189 | 978 | 664 |
| `auch wenn` | 1,018 | 859 | 778 |
| `aus etwas bestehen` | 1,017 | 848 | 780 |
| `darüber hinaus` | 987 | 852 | 803 |
| `je nach` | 961 | 800 | 820 |
| `in der Regel` | 898 | 707 | 877 |
| `zu Hause` | 822 | 647 | 954 |
| `ein wenig` | 753 | 642 | 1037 |
| `vor Ort` | 753 | 590 | 1039 |
| `ein bisschen` | 724 | 585 | 1087 |
| `zusammen mit` | 724 | 626 | 1088 |

## Co-occurrence (association) table

7,926,010 tokens, 750,866 sentences. After merging and dropping items seen fewer than 5 times: 394,897 items (unigrams, UPOS votes, n-grams, pairs); 262,319 n-grams and pairs scored (n2 149,638, n3 85,860, n4 19,586, p2 6,781, p3 454). Shipped: 152,467 rows, 2.6 MB gzipped (`de.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`de.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `z. b` |  | 896 | 580 | 11.73 | 0.89 | 14,517 |  |
| 2 | n | `finden sie` |  | 2,871 | 1,978 | 4.35 | 0.38 | 12,551 |  |
| 3 | p | `machen sich` | `sich machen` | 1,277 | 1,068 | 7.44 | 0.59 | 10,770 |  |
| 4 | n | `personenbezogen datum` |  | 641 | 133 | 11.20 | 0.82 | 9,769 |  |
| 5 | n | `rund um` |  | 1,152 | 942 | 6.95 | 0.55 | 9,395 |  |
| 6 | n | `sehr gut` |  | 1,544 | 1,156 | 5.53 | 0.45 | 9,123 |  |
| 7 | n | `per e-mail` |  | 607 | 502 | 10.33 | 0.76 | 7,919 |  |
| 8 | n | `film auf ihr merkliste` |  | 448 | 67 | 11.87 | 0.84 | 7,456 |  |
| 9 | n | `mitglied haben dieser film` |  | 456 | 67 | 11.57 | 0.82 | 7,336 |  |
| 10 | n | `weiter information` |  | 899 | 658 | 7.05 | 0.54 | 7,258 |  |
| 11 | n | `deutsch wikipedia` |  | 447 | 79 | 9.92 | 0.70 | 5,770 |  |
| 12 | n | `noch nicht` |  | 1,722 | 1,432 | 3.62 | 0.30 | 5,646 |  |
| 13 | n | `ähnlich website` |  | 511 | 178 | 9.08 | 0.65 | 5,627 |  |
| 14 | n | `an ende` |  | 894 | 747 | 5.35 | 0.41 | 5,189 |  |
| 15 | n | `bis hin zu` |  | 592 | 541 | 6.01 | 0.44 | 4,885 |  |
| 16 | n | `original-scan der anbieten ansichtskarte` |  | 230 | 34 | 14.48 | 0.96 | 4,822 |  |
| 17 | n | `seriosität oder malware` |  | 211 | 211 | 15.04 | 0.99 | 4,708 |  |
| 18 | n | `information zu` |  | 1,176 | 913 | 4.01 | 0.32 | 4,633 |  |
| 19 | n | `kostenlos versand upc` |  | 292 | 32 | 11.31 | 0.77 | 4,606 |  |
| 20 | p | `informieren sich` | `sich informieren` | 408 | 303 | 9.10 | 0.64 | 4,469 |  |
| 21 | n | `malware sowie allgemein erfahrungsbericht` |  | 211 | 211 | 14.53 | 0.96 | 4,426 |  |
| 22 | n | `wir freuen sich` |  | 566 | 505 | 6.64 | 0.48 | 4,357 | sich freuen |
| 23 | n | `letzte jahr` |  | 627 | 552 | 6.27 | 0.46 | 4,332 |  |
| 24 | p | `finden hier` | `hierfinden` | 468 | 384 | 8.05 | 0.57 | 4,323 |  |
| 25 | n | `haben dieser film auf` |  | 462 | 67 | 6.75 | 0.48 | 4,312 |  |
| 26 | n | `million euro` |  | 400 | 230 | 8.93 | 0.63 | 4,295 |  |
| 27 | n | `egal ob` |  | 382 | 343 | 8.94 | 0.62 | 4,140 |  |
| 28 | n | `betrag enthalten die gesetzlich` |  | 230 | 34 | 12.78 | 0.85 | 4,125 |  |
| 29 | n | `webserver betreiben` |  | 283 | 197 | 11.16 | 0.76 | 4,007 |  |
| 30 | n | `ich denken` |  | 782 | 624 | 4.90 | 0.37 | 3,988 |  |
| 31 | n | `zu thema` |  | 1,038 | 821 | 3.94 | 0.31 | 3,966 |  |
| 32 | n | `in internet` |  | 832 | 627 | 4.35 | 0.33 | 3,875 |  |
| 33 | n | `enthalten die gesetzlich mehrwertsteuer` |  | 237 | 41 | 11.61 | 0.77 | 3,794 |  |
| 34 | n | `in bereich` |  | 1,005 | 815 | 3.80 | 0.29 | 3,756 |  |
| 35 | n | `jahr alt` |  | 572 | 497 | 5.97 | 0.43 | 3,696 |  |
| 36 | n | `nennen betrag enthalten` |  | 230 | 34 | 11.51 | 0.76 | 3,690 |  |
| 37 | n | `sonst gut zustand versandkosten` |  | 219 | 31 | 12.29 | 0.81 | 3,659 |  |
| 38 | n | `hinweis auf betrug` |  | 211 | 211 | 12.34 | 0.81 | 3,640 |  |
| 39 | n | `allgemein erfahrungsbericht von benutzer` |  | 211 | 211 | 12.23 | 0.80 | 3,605 |  |
| 40 | n | `erhalten sie` |  | 880 | 704 | 4.17 | 0.32 | 3,587 |  |
| 41 | n | `ich glauben` |  | 612 | 489 | 5.38 | 0.39 | 3,583 |  |
| 42 | n | `in den letzte` |  | 580 | 508 | 5.03 | 0.37 | 3,531 |  |
| 43 | n | `schülerin und schüler` |  | 196 | 103 | 12.79 | 0.84 | 3,452 |  |
| 44 | n | `bieten ihnen` |  | 491 | 423 | 6.39 | 0.46 | 3,449 |  |
| 45 | n | `hochschule für musik` |  | 208 | 14 | 12.15 | 0.80 | 3,401 |  |
| 46 | p | `nehmen sich` | `sich nehmen` | 417 | 355 | 7.17 | 0.50 | 3,354 |  |
| 47 | n | `umgang mit` |  | 432 | 363 | 6.19 | 0.44 | 3,341 |  |
| 48 | n | `noch nie` |  | 462 | 415 | 6.41 | 0.46 | 3,303 |  |
| 49 | n | `zugang zu` |  | 500 | 374 | 5.49 | 0.39 | 3,295 |  |
| 50 | n | `art und weise` |  | 218 | 203 | 11.07 | 0.73 | 3,279 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `machen sich` | `sich machen` | 1,277 | 1,068 | 7.44 | 0.59 | 10,770 |
| `informieren sich` | `sich informieren` | 408 | 303 | 9.10 | 0.64 | 4,469 |
| `finden hier` | `hierfinden` | 468 | 384 | 8.05 | 0.57 | 4,323 |
| `nehmen sich` | `sich nehmen` | 417 | 355 | 7.17 | 0.50 | 3,354 |
| `zeichnen sich` | `sich zeichnen` | 241 | 216 | 9.44 | 0.63 | 2,773 |
| `ziehen sich` | `sich ziehen` | 295 | 266 | 8.02 | 0.55 | 2,737 |
| `finden unter` | `unterfinden` | 298 | 291 | 7.79 | 0.53 | 2,639 |
| `holen sich` | `sich holen` | 207 | 165 | 8.84 | 0.58 | 2,180 |
| `schauen sich` | `sich schauen` | 230 | 210 | 7.92 | 0.53 | 2,097 |
| `zeichnen sich aus` | `sich auszeichnen` | 144 | 129 | 10.15 | 0.64 | 1,850 |
| `präsentieren sich` | `sich präsentieren` | 173 | 155 | 8.34 | 0.54 | 1,686 |
| `geben sich` | `sich geben` | 310 | 274 | 4.98 | 0.34 | 1,544 |
| `schließen sich` | `sich schließen` | 161 | 151 | 8.01 | 0.51 | 1,491 |
| `speaking costumers` | `costumersspeaking` | 46 | 3 | 21.20 | 1.22 | 1,444 |
| `öffnen sich` | `sich öffnen` | 160 | 143 | 7.53 | 0.48 | 1,368 |
| `schauen vorbei` | `vorbeischauen` | 86 | 76 | 12.78 | 0.77 | 1,366 |
| `erklären einverstanden` | `einverstandenerklären` | 72 | 65 | 14.16 | 0.85 | 1,298 |
| `gefallen gut` | `gutgefallen` | 122 | 97 | 8.92 | 0.56 | 1,278 |
| `mögen lieber` | `liebermögen` | 84 | 79 | 11.79 | 0.71 | 1,215 |
| `tun sich` | `sich tun` | 166 | 159 | 6.26 | 0.40 | 1,120 |
| `kehrt zurück` | `zurückkehrt` | 56 | 51 | 14.71 | 0.86 | 1,074 |
| `denken sich` | `sich denken` | 153 | 137 | 6.40 | 0.41 | 1,062 |
| `beraten gern` | `gernberaten` | 76 | 68 | 11.23 | 0.67 | 1,042 |
| `wissen genau` | `genauwissen` | 98 | 95 | 8.91 | 0.55 | 1,019 |
| `gehen gut` | `gutgehen` | 155 | 147 | 5.96 | 0.38 | 979 |

## Rank shifts against the live snapshot (`reference/lemmas/de.json`)

Live list 20,000 lemmas, this build 200,000; 17,861 shared. Spearman rank correlation on the shared lemmas 0.820; median rank ratio 1.24x.
Overlap of this build's top-k with the live top-k: top 1,000 81.5%, top 5,000 80.4%, top 20,000 72.3%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `achtzig` | 19620 | 1150 | -18,470 |
| `Daten` | 18710 | 760 | -17,950 |
| `sechzehn` | 18717 | 887 | -17,830 |
| `aufregen` | 19193 | 2878 | -16,315 |
| `Milliliter` | 18887 | 3011 | -15,876 |
| `anhängen` | 17461 | 1782 | -15,679 |
| `achtzehn` | 16468 | 864 | -15,604 |
| `Grosse` | 18554 | 3066 | -15,488 |
| `Krem` | 19878 | 4432 | -15,446 |
| `Daumen` | 19501 | 4502 | -14,999 |
| `Handschuh` | 19914 | 4983 | -14,931 |
| `Webserver` | 15749 | 1097 | -14,652 |
| `sechzig` | 14903 | 849 | -14,054 |
| `Ihr` | 14082 | 55 | -14,027 |
| `sogenannt` | 14915 | 942 | -13,973 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `besonderer` | 339 | 193061 | +192,722 |
| `am` | 318 | 192461 | +192,143 |
| `kommsen` | 3770 | 195888 | +192,118 |
| `erfasst` | 2532 | 194101 | +191,569 |
| `time` | 4948 | 152471 | +147,523 |
| `stell` | 4950 | 152080 | +147,130 |
| `kölner` | 4257 | 149184 | +144,927 |
| `deiner` | 2647 | 146011 | +143,364 |
| `Updat` | 2765 | 140052 | +137,287 |
| `Verteilung` | 4516 | 140937 | +136,421 |
| `Lachen` | 4154 | 121502 | +117,348 |
| `Grüße` | 2712 | 114863 | +112,151 |
| `Et` | 4249 | 110079 | +105,830 |
| `Beschreibung` | 1020 | 103725 | +102,705 |
| `Bisschen` | 2350 | 104321 | +101,971 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `das` | 7309 | 7 | -7,302 |
| `den` | 10437 | 11 | -10,426 |
| `werden + Partizip II` | - | 18 | - |
| `eine` | 8654 | 21 | -8,633 |
| `Sie` | - | 25 | - |
| `dem` | - | 27 | - |
| `des` | 12527 | 29 | -12,498 |
| `einen` | 10967 | 39 | -10,928 |
| `einem` | - | 50 | - |
| `Ihr` | 14082 | 55 | -14,027 |
| `ander` | - | 69 | - |
| `es gibt` | - | 76 | - |
| `werden + Infinitiv` | - | 88 | - |
| `sein + Partizip II` | - | 89 | - |
| `um … zu + Infinitiv` | - | 91 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `aller` | 53 | - | - |
| `anderer` | 56 | - | - |
| `alle` | 63 | 5018 | +4,955 |
| `vieler` | 76 | - | - |
| `Tag` | 84 | - | - |
| `erster` | 86 | 25087 | +25,001 |
| `einiger` | 151 | - | - |
| `gerne` | 175 | - | - |
| `Kunde` | 180 | - | - |
| `weniger` | 192 | - | - |
| `nächster` | 229 | - | - |
| `zweiter` | 277 | 99534 | +99,257 |
| `Of` | 285 | 6014 | +5,729 |
| `daß` | 286 | - | - |
| `am` | 318 | 192461 | +192,143 |

## Ported frequer checks

### Form-ratio outliers (10)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 2 | `und` | 224,804 | median form 25.5; `und` 224,752 (8814x) |
| 3 | `der` | 204,578 | median form 47; `der` 203,696 (4334x) |
| 15 | `ich` | 60,658 | median form 37; `ich` 60,307 (1630x) |
| 17 | `ein` | 56,845 | median form 16; `ein` 56,828 (3552x) |
| 60 | `mehr` | 16,283 | median form 7; `mehr` 16,266 (2324x) |
| 86 | `schon` | 10,287 | median form 1; `schon` 10,285 (10285x) |
| 118 | `gegen` | 6,121 | median form 2; `gegen` 6,118 (3059x) |
| 163 | `sondern` | 4,336 | median form 1.5; `sondern` 4,332 (2888x) |
| 312 | `davon` | 2,345 | median form 1; `davon` 2,339 (2339x) |
| 677 | `egal` | 1,166 | median form 1; `egal` 1,164 (1164x) |

### Singular/plural mismatch (1,527)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `die` | 228,205 | `di` lemmatises to `di` (rank 4,055) |
| 7 | `das` | 91,254 | `da` lemmatises to `da` (rank 79) |
| 9 | `von` | 86,628 | `vo` lemmatises to `vo` (rank 36,561) |
| 11 | `den` | 76,361 | `de` lemmatises to `de` (rank 796) |
| 17 | `ein` | 56,845 | `ei` lemmatises to `ei` (rank 13,313) |
| 21 | `eine` | 52,951 | `ein` lemmatises to `ein` (rank 17) |
| 25 | `Sie` | 44,158 | `Si` lemmatises to `Si` (rank 32,477) |
| 29 | `des` | 39,799 | `de` lemmatises to `de` (rank 796) |
| 30 | `sie` | 38,387 | `si` lemmatises to `si` (rank 17,480) |
| 31 | `oder` | 38,126 | `od` lemmatises to `od` (rank 8,712) |
| 32 | `als` | 33,603 | `al` lemmatises to `al` (rank 10,224) |
| 35 | `wie` | 28,992 | `wi` lemmatises to `wi` (rank 19,747) |
| 36 | `dass` | 27,072 | `das` lemmatises to `das` (rank 7) |
| 39 | `einen` | 25,754 | `ein` lemmatises to `ein` (rank 17) |
| 39 | `einen` | 25,754 | `eine` lemmatises to `eine` (rank 21) |
| 41 | `aus` | 25,393 | `au` lemmatises to `au` (rank 6,928) |
| 45 | `man` | 21,600 | `ma` lemmatises to `ma` (rank 14,824) |
| 46 | `über` | 21,463 | `üb` lemmatises to `üb` (rank 99,671) |
| 48 | `einer` | 21,131 | `ein` lemmatises to `ein` (rank 17) |
| 49 | `wenn` | 20,915 | `wen` lemmatises to `wer` (rank 154) |
| 51 | `aber` | 20,452 | `ab` lemmatises to `ab` (rank 133) |
| 54 | `unser` | 19,311 | `uns` lemmatises to `sich` (rank 28) |
| 56 | `mein` | 17,321 | `mei` lemmatises to `mei` (rank 97,487) |
| 62 | `was` | 15,863 | `wa` lemmatises to `wa` (rank 30,920) |
| 63 | `müssen` | 15,695 | `müss` lemmatises to `müss` (rank 149,945) |

_1,502 more not shown._

### Lemma consistency (343)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 25 | `Sie` | 44,158 | alone, `Sie` lemmatises to `sie` (rank 30) |
| 55 | `Ihr` | 17,665 | alone, `Ihr` lemmatises to `ihr` (rank 34) |
| 62 | `was` | 15,863 | alone, `was` lemmatises to `etwas` (rank 110) |
| 85 | `uns` | 10,313 | alone, `uns` lemmatises to `sich` (rank 28) |
| 117 | `mich` | 6,342 | alone, `mich` lemmatises to `sich` (rank 28) |
| 143 | `dir` | 5,103 | alone, `dir` lemmatises to `sich` (rank 28) |
| 150 | `Frage` | 4,864 | alone, `Frage` lemmatises to `fragen` (rank 410) |
| 192 | `dich` | 3,730 | alone, `dich` lemmatises to `sich` (rank 28) |
| 234 | `euch` | 3,239 | alone, `euch` lemmatises to `sich` (rank 28) |
| 270 | `lange` | 2,672 | alone, `lange` lemmatises to `lang` (rank 188) |
| 419 | `solcher` | 1,755 | alone, `solcher` lemmatises to `solch` (rank 1,096) |
| 444 | `Stelle` | 1,664 | alone, `Stelle` lemmatises to `stellen` (rank 214) |
| 560 | `Suche` | 1,365 | alone, `Suche` lemmatises to `suchen` (rank 187) |
| 661 | `meinen` | 1,195 | alone, `meinen` lemmatises to `mein` (rank 56) |
| 743 | `weiß` | 1,070 | alone, `weiß` lemmatises to `wissen` (rank 130) |
| 760 | `Daten` | 1,030 | alone, `Daten` lemmatises to `Datum` (rank 249) |
| 842 | `vergangen` | 942 | alone, `vergangen` lemmatises to `vergehen` (rank 3,293) |
| 848 | `Essen` | 933 | alone, `Essen` lemmatises to `essen` (rank 488) |
| 906 | `Kauf` | 861 | alone, `Kauf` lemmatises to `kaufen` (rank 231) |
| 947 | `Pflanze` | 826 | alone, `Pflanze` lemmatises to `pflanzen` (rank 4,138) |
| 991 | `Dank` | 795 | alone, `Dank` lemmatises to `dank` (rank 672) |
| 1141 | `Morgen` | 689 | alone, `Morgen` lemmatises to `morgen` (rank 798) |
| 1232 | `selber` | 641 | alone, `selber` lemmatises to `selbst` (rank 134) |
| 1339 | `Lauf` | 588 | alone, `Lauf` lemmatises to `laufen` (rank 263) |
| 1420 | `Alternative` | 549 | alone, `Alternative` lemmatises to `alternativ` (rank 1,455) |

_318 more not shown._

### Short lemmas (184)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 5 | `in` | 183,524 | `im` -> `in`, `in` -> `in`, `ins` -> `in`, `i.` -> `in`, `inder` -> `in` |
| 6 | `zu` | 120,872 | `zu` -> `zu`, `zur` -> `zu`, `zum` -> `zu` |
| 16 | `es` | 57,472 | `es` -> `es`, `’s` -> `es` |
| 22 | `an` | 50,960 | `an` -> `an`, `am` -> `an`, `ans` -> `an`, `a` -> `a`, `ande` -> `an` |
| 40 | `er` | 25,509 | `er` -> `er`, `eres` -> `er` |
| 42 | `um` | 24,839 | `um` -> `um`, `ums` -> `um` |
| 43 | `so` | 22,733 | `so` -> `so` |
| 44 | `du` | 21,863 | `du` -> `du` |
| 79 | `da` | 11,143 | `da` -> `da` |
| 119 | `ja` | 6,109 | `ja` -> `ja` |
| 133 | `ab` | 5,454 | `ab` -> `ab` |
| 139 | `ob` | 5,247 | `ob` -> `ob` |
| 172 | `wo` | 4,199 | `wo` -> `wo` |
| 288 | `je` | 2,509 | `je` -> `je` |
| 436 | `B` | 1,684 | `b` -> `b`, `b.` -> `?` |
| 464 | `m` | 1,602 | `m` -> `m`, `mer` -> `m` |
| 514 | `of` | 1,449 | `of` -> `of` |
| 617 | `x` | 1,265 | `x` -> `x` |
| 731 | `A` | 1,078 | `a` -> `a`, `a.` -> `a`, `as` -> `as` |
| 796 | `de` | 997 | `de` -> `de` |
| 888 | `C` | 887 | `c` -> `c`, `c.` -> `?` |
| 962 | `g` | 812 | `g` -> `g`, `ger` -> `g`, `ges` -> `g`, `g.` -> `?` |
| 1011 | `a` | 783 | `a.` -> `a`, `a` -> `a` |
| 1013 | `s` | 783 | `s` -> `s` |
| 1048 | `AG` | 750 | `ag` -> `ag`, `ags` -> `ags` |

_159 more not shown._

### Case merges (2,279)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 25 | `Sie` | 44,158 | lowercase `sie` is rank 30 (38,387): merge candidate |
| 55 | `Ihr` | 17,665 | lowercase `ihr` is rank 34 (29,132): merge candidate |
| 65 | `Jahr` | 14,842 | lowercase `jahr` is rank 4,892 (120): merge candidate |
| 100 | `Tag#day` | 7,475 | lowercase `tag#day` is rank 8,259 (59): merge candidate |
| 102 | `Zeit` | 7,349 | lowercase `zeit` is rank 4,816 (123): merge candidate |
| 116 | `Mensch` | 6,415 | lowercase `mensch` is rank 6,256 (86): merge candidate |
| 121 | `Kind` | 5,865 | lowercase `kind` is rank 7,142 (72): merge candidate |
| 122 | `Ihnen` | 5,672 | lowercase `ihnen` is rank 461 (1,604): merge candidate |
| 128 | `Deutschland` | 5,563 | lowercase `deutschland` is rank 8,834 (54): merge candidate |
| 132 | `Seite` | 5,463 | lowercase `seite` is rank 10,788 (41): merge candidate |
| 156 | `Information` | 4,703 | lowercase `information` is rank 21,508 (17): merge candidate |
| 162 | `Thema` | 4,358 | lowercase `thema` is rank 11,656 (37): merge candidate |
| 164 | `Haus` | 4,304 | lowercase `haus` is rank 22,566 (16): merge candidate |
| 168 | `Frau` | 4,227 | lowercase `frau` is rank 8,838 (54): merge candidate |
| 174 | `Stadt` | 4,054 | lowercase `stadt` is rank 16,901 (23): merge candidate |
| 178 | `Leben` | 4,024 | lowercase `leben` is rank 303 (2,434): merge candidate |
| 179 | `Bild` | 4,011 | lowercase `bild` is rank 6,809 (77): merge candidate |
| 182 | `Produkt` | 3,949 | lowercase `produkt` is rank 14,067 (29): merge candidate |
| 183 | `Unternehmen` | 3,935 | lowercase `unternehmen` is rank 2,436 (298): merge candidate |
| 186 | `Uhr` | 3,878 | lowercase `uhr` is rank 10,623 (42): merge candidate |
| 189 | `Website` | 3,788 | lowercase `website` is rank 28,707 (12): merge candidate |
| 195 | `Problem` | 3,690 | lowercase `problem` is rank 7,708 (65): merge candidate |
| 199 | `Teil` | 3,641 | lowercase `teil` is rank 3,292 (204): merge candidate |
| 203 | `Fall` | 3,622 | lowercase `fall` is rank 5,892 (93): merge candidate |
| 206 | `Land` | 3,589 | lowercase `land` is rank 15,770 (25): merge candidate |

_2,254 more not shown._

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 668 (66.8%).

Ours only: `werden + Partizip II`, `was`, `es gibt`, `uns`, `werden + Infinitiv`, `sein + Partizip II`, `um … zu + Infinitiv`, `damit`, `mich`, `dabei`, `lassen + Infinitiv`, `dir`, `Frage`, `dazu`, `Information`, `anbieten`, `natürlich`, `würde + Infinitiv`, `Produkt`, `dich`, `nicht mehr`, `Kunde#Masc`, `dafür`, `beziehungsweise`, `euch`

wordfreq only: `jahren`, `s`, `enden`, `d`, `läuten`, `stunden`, `i`, `stimmen`, `e`, `frauen`, `u`, `ne`, `bzw`, `heraus`, `n`, `minuten`, `polizei`, `ausserdem`, `woch`, `okay`, `namen`, `halt`, `schul`, `fühlen`, `h`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 37 | `all` | 26,924 | wordfreq zipf en 6.5 vs de 5.2 |
| 514 | `of` | 1,449 | wordfreq zipf en 7.4 vs de 5.5 |
| 731 | `A` | 1,078 | wordfreq zipf en 7.4 vs de 5.8 |
| 816 | `The` | 969 | wordfreq zipf en 7.7 vs de 5.6 |
| 1011 | `a` | 783 | wordfreq zipf en 7.4 vs de 5.8 |
| 1128 | `her` | 697 | wordfreq zipf en 6.3 vs de 5.2 |
| 1440 | `the` | 544 | wordfreq zipf en 7.7 vs de 5.6 |
| 1603 | `I` | 487 | wordfreq zipf en 7.1 vs de 5.5 |
| 1635 | `national` | 480 | wordfreq zipf en 5.5 vs de 4.3 |
| 1668 | `and` | 467 | wordfreq zipf en 7.4 vs de 5.2 |
| 1734 | `Set` | 445 | wordfreq zipf en 5.6 vs de 4.3 |
| 2089 | `Business` | 357 | wordfreq zipf en 5.6 vs de 4.5 |
| 2165 | `New` | 344 | wordfreq zipf en 6.2 vs de 5.1 |
| 2186 | `for` | 339 | wordfreq zipf en 7.0 vs de 4.9 |
| 2341 | `Held` | 313 | wordfreq zipf en 5.2 vs de 4.2 |
| 2357 | `to` | 311 | wordfreq zipf en 7.4 vs de 5.2 |
| 2387 | `World` | 306 | wordfreq zipf en 5.9 vs de 4.5 |
| 2763 | `Last` | 255 | wordfreq zipf en 5.9 vs de 4.5 |
| 2885 | `Board` | 240 | wordfreq zipf en 5.2 vs de 3.9 |
| 2920 | `Services` | 237 | wordfreq zipf en 5.3 vs de 3.9 |
| 3021 | `IT` | 227 | wordfreq zipf en 7.0 vs de 4.9 |
| 3054 | `Support` | 225 | wordfreq zipf en 5.5 vs de 4.2 |
| 3112 | `Not` | 219 | wordfreq zipf en 6.7 vs de 4.7 |
| 3209 | `Look` | 210 | wordfreq zipf en 5.8 vs de 4.1 |
| 3223 | `Performance` | 209 | wordfreq zipf en 5.2 vs de 4.2 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 128 | `Deutschland` | 5,563 | PROPN 100%, capitalised forms 0% |
| 340 | `Berlin` | 2,093 | PROPN 99%, capitalised forms 0% |
| 514 | `of` | 1,449 | PROPN 97%, capitalised forms 0% |
| 538 | `USA` | 1,411 | PROPN 100%, capitalised forms 0% |
| 543 | `Europa` | 1,404 | PROPN 100%, capitalised forms 0% |
| 630 | `Österreich` | 1,244 | PROPN 100%, capitalised forms 0% |
| 660 | `Google` | 1,196 | PROPN 100%, capitalised forms 0% |
| 679 | `Tom` | 1,163 | PROPN 100%, capitalised forms 0% |
| 785 | `München` | 1,012 | PROPN 100%, capitalised forms 0% |
| 791 | `Schweiz` | 1,005 | PROPN 100%, capitalised forms 0% |
| 796 | `de` | 997 | PROPN 97%, capitalised forms 0% |
| 812 | `Hamburg` | 973 | PROPN 100%, capitalised forms 0% |
| 816 | `The` | 969 | PROPN 97%, capitalised forms 0% |
| 876 | `Köln` | 898 | PROPN 100%, capitalised forms 0% |
| 883 | `Facebook` | 890 | PROPN 100%, capitalised forms 0% |
| 962 | `g` | 812 | PROPN 60%, capitalised forms 0% |
| 982 | `Frankreich` | 800 | PROPN 98%, capitalised forms 0% |
| 1156 | `Japan` | 679 | PROPN 100%, capitalised forms 0% |
| 1188 | `Michael` | 665 | PROPN 100%, capitalised forms 0% |
| 1216 | `Wien` | 649 | PROPN 99%, capitalised forms 0% |
| 1230 | `Windows` | 642 | PROPN 100%, capitalised forms 0% |
| 1263 | `Thomas` | 624 | PROPN 100%, capitalised forms 0% |
| 1293 | `China` | 607 | PROPN 100%, capitalised forms 0% |
| 1344 | `Wikipedia` | 587 | PROPN 100%, capitalised forms 0% |
| 1347 | `EUR` | 586 | PROPN 100%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 93.6% | 0.955 |
| juilland_u | 98.3% | 0.995 |
| juilland_u_corrected | 98.3% | 0.995 |
| dp_adjusted | 96.3% | 0.986 |
| cd_blend | 96.4% | 0.984 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `Transitional` | 5971 | 4872 | -1,099 | 91 | 91 | 0.895 | 0.402 |
| `anfragen` | 5793 | 4727 | -1,066 | 95 | 95 | 0.895 | 0.425 |
| `Suchmaschinen-Marketing` | 5661 | 4600 | -1,061 | 98 | 98 | 0.908 | 0.351 |
| `Suchaufkommen#Masc` | 5787 | 4726 | -1,061 | 95 | 95 | 0.904 | 0.366 |
| `Nachfolgende` | 5460 | 4422 | -1,038 | 103 | 103 | 0.905 | 0.369 |
| `Grosse#court` | 4982 | 118150 | +113,168 | 116 | 1 | 0.000 | 0.991 |
| `MILF` | 1743 | 46355 | +44,612 | 443 | 4 | 0.014 | 0.982 |
| `Ingbert` | 4953 | 34486 | +29,533 | 117 | 6 | 0.073 | 0.950 |
| `Ardenne` | 3583 | 27895 | +24,312 | 181 | 8 | 0.448 | 0.941 |
| `Grosse` | 3066 | 23681 | +20,615 | 224 | 10 | 0.060 | 0.951 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `konkurrierend` | 5177 | 4907 | -270 | 111 | 110 | 0.917 | 0.318 |
| `sich leisten` | 5077 | 4821 | -256 | 114 | 108 | 0.919 | 0.323 |
| `funktional` | 5218 | 4975 | -243 | 110 | 99 | 0.908 | 0.360 |
| `vermeintlich` | 5120 | 4878 | -242 | 113 | 106 | 0.909 | 0.330 |
| `mitbekommen` | 5221 | 4980 | -241 | 110 | 99 | 0.908 | 0.360 |
| `Grosse#court` | 4982 | 123696 | +118,714 | 116 | 1 | 0.000 | 0.991 |
| `MILF` | 1743 | 29654 | +27,911 | 443 | 4 | 0.014 | 0.982 |
| `Ingbert` | 4953 | 24201 | +19,248 | 117 | 6 | 0.073 | 0.950 |
| `Grosse` | 3066 | 18380 | +15,314 | 224 | 10 | 0.060 | 0.951 |
| `Krem` | 4432 | 16050 | +11,618 | 137 | 11 | 0.121 | 0.926 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `vermeintlich` | 5120 | 4878 | -242 | 113 | 106 | 0.909 | 0.330 |
| `mitbekommen` | 5221 | 4984 | -237 | 110 | 99 | 0.908 | 0.360 |
| `motiviert` | 5222 | 4985 | -237 | 110 | 101 | 0.905 | 0.355 |
| `mit der Zeit` | 5220 | 4983 | -237 | 110 | 103 | 0.906 | 0.342 |
| `funktional` | 5218 | 4982 | -236 | 110 | 99 | 0.908 | 0.360 |
| `Grosse#court` | 4982 | 120555 | +115,573 | 116 | 1 | 0.000 | 0.991 |
| `MILF` | 1743 | 37720 | +35,977 | 443 | 4 | 0.014 | 0.982 |
| `Ingbert` | 4953 | 28311 | +23,358 | 117 | 6 | 0.073 | 0.950 |
| `Grosse` | 3066 | 20998 | +17,932 | 224 | 10 | 0.060 | 0.951 |
| `Krem` | 4432 | 17750 | +13,318 | 137 | 11 | 0.121 | 0.926 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `wahnsinnig` | 5761 | 4954 | -807 | 96 | 92 | 0.907 | 0.343 |
| `streiten` | 5630 | 4864 | -766 | 99 | 95 | 0.909 | 0.343 |
| `Sorgfalt` | 5505 | 4760 | -745 | 102 | 101 | 0.899 | 0.337 |
| `Suchmaschinen-Marketing` | 5661 | 4934 | -727 | 98 | 98 | 0.908 | 0.351 |
| `konkurrierend` | 5177 | 4462 | -715 | 111 | 110 | 0.917 | 0.318 |
| `Grosse#court` | 4982 | 26322 | +21,340 | 116 | 1 | 0.000 | 0.991 |
| `MILF` | 1743 | 11936 | +10,193 | 443 | 4 | 0.014 | 0.982 |
| `Ingbert` | 4953 | 13419 | +8,466 | 117 | 6 | 0.073 | 0.950 |
| `Grosse` | 3066 | 10413 | +7,347 | 224 | 10 | 0.060 | 0.951 |
| `Ardenne` | 3583 | 10540 | +6,957 | 181 | 8 | 0.448 | 0.941 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `überstehen` | 5306 | 4735 | -571 | 108 | 107 | 0.904 | 0.361 |
| `nachfolgend` | 5300 | 4734 | -566 | 108 | 107 | 0.910 | 0.347 |
| `Nachfolgende` | 5460 | 4894 | -566 | 103 | 103 | 0.905 | 0.369 |
| `Sorgfalt` | 5505 | 4944 | -561 | 102 | 101 | 0.899 | 0.337 |
| `Registrierungsvorgang` | 5321 | 4762 | -559 | 107 | 106 | 0.896 | 0.402 |
| `Grosse#court` | 4982 | 25981 | +20,999 | 116 | 1 | 0.000 | 0.991 |
| `Ingbert` | 4953 | 13022 | +8,069 | 117 | 6 | 0.073 | 0.950 |
| `MILF` | 1743 | 9269 | +7,526 | 443 | 4 | 0.014 | 0.982 |
| `Ardenne` | 3583 | 9975 | +6,392 | 181 | 8 | 0.448 | 0.941 |
| `Suchworte` | 4963 | 11241 | +6,278 | 117 | 9 | 0.642 | 0.917 |

