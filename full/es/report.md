# Review report: es (full)

- Ranking score: `frequency`; 44,306 candidate lemmas ranked.
- Tokens counted: 105,726,244 in 138,221 documents, 40 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_es` 1.5.0 (sha256 `ccbd50dc900e43a8`); fallback `spacy-list`, units on; honeyeater `c07c70158590`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| paracrawl-en-es | 35 | 129,359 | 4,948,749 | 102,399,277 | alpha 39,943, exact_dup 24,266, gap 37,752, langid 1,313,943, length 100,753, near_dup 2,544 |
| tatoeba-spa | 5 | 8,862 | 441,314 | 3,326,967 | alpha 35, gap 95, length 503, near_dup 1,105 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 1,655,810. Sentences: 5,707,166.

## Units

Counted occurrences by kind: compound 708,886 (0.67%), compound1 752,894 (0.71%), construction 2,169,610 (2.05%), phrase 1,910,186 (1.81%), word 100,184,668 (94.76%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 7,235 | 1,567,444 |
| construction | 29 | 2,178,213 |
| phrase | 910 | 1,910,472 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `encontrarse` | 60,008 | 48,044 | 168 |
| `sitio web` | 45,422 | 34,327 | 228 |
| `Estados Unidos` | 31,586 | 27,150 | 366 |
| `internacional` | 29,628 | 25,601 | 255 |
| `correo electrónico` | 23,988 | 20,711 | 505 |
| `convertirse` | 22,193 | 20,150 | 1950 |
| `por qué` | 21,701 | 18,212 | 573 |
| `directamente` | 19,755 | 18,142 | 615 |
| `especialmente` | 16,904 | 15,845 | 743 |
| `tratarse` | 16,335 | 15,214 | 2427 |
| `simplemente` | 16,304 | 15,259 | 767 |
| `actualmente` | 15,739 | 14,836 | 798 |
| `asegurarse` | 15,565 | 14,618 | 2339 |
| `realmente` | 14,990 | 13,945 | 840 |
| `página web` | 14,699 | 13,198 | 855 |
| `completamente` | 13,848 | 13,076 | 916 |
| `totalmente` | 13,329 | 12,557 | 944 |
| `sentirse` | 12,219 | 11,380 | 1028 |
| `quedarse` | 11,948 | 10,933 | 1167 |
| `fácilmente` | 11,559 | 11,022 | 1083 |
| `rápidamente` | 11,457 | 10,940 | 1084 |
| `solamente` | 11,186 | 10,639 | 1123 |
| `Nueva York` | 10,712 | 9,713 | 1159 |
| `ponerse` | 10,545 | 9,933 | 1315 |
| `aproximadamente` | 10,074 | 9,441 | 1209 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `poder + infinitivo` | 601,163 | 135,314 | 20 |
| `haber + participio` | 428,311 | 129,106 | 27 |
| `se + verbo (impersonal/pasiva)` | 389,826 | 126,727 | 30 |
| `ser + participio` | 235,927 | 109,455 | 37 |
| `estar + gerundio` | 147,052 | 88,316 | 57 |
| `lo + adjetivo` | 62,070 | 48,109 | 163 |
| `al + infinitivo` | 61,539 | 48,486 | 155 |
| `tener que + infinitivo` | 52,037 | 41,858 | 193 |
| `ir a + infinitivo` | 40,403 | 31,675 | 266 |
| `más/menos … que` | 34,497 | 29,532 | 336 |
| `seguir + gerundio` | 22,054 | 19,948 | 556 |
| `volver a + infinitivo` | 13,984 | 12,888 | 906 |
| `comenzar a + infinitivo` | 12,993 | 12,191 | 969 |
| `empezar a + infinitivo` | 12,218 | 11,339 | 1029 |
| `tan … como` | 10,157 | 9,493 | 1244 |
| `dejar de + infinitivo` | 10,025 | 9,340 | 1216 |
| `soler + infinitivo` | 9,984 | 9,411 | 1218 |
| `hace + tiempo` | 9,235 | 8,758 | 1302 |
| `acabar de + infinitivo` | 6,299 | 5,481 | 1810 |
| `desde hace + tiempo` | 4,432 | 4,335 | 2376 |
| `tan … que` | 4,137 | 4,008 | 2481 |
| `qué + adjetivo/sustantivo` | 3,891 | 3,564 | 2596 |
| `hace + tiempo + que` | 3,146 | 3,019 | 2987 |
| `hacer que + subjuntivo` | 1,195 | 1,188 | 5263 |
| `menos … que` | 662 | 643 | 7245 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `a través de` | 59,644 | 46,869 | 162 |
| `después de` | 56,703 | 45,496 | 172 |
| `para que` | 54,272 | 43,859 | 181 |
| `cerca de` | 41,538 | 34,672 | 260 |
| `antes de` | 39,627 | 33,863 | 273 |
| `así como` | 39,070 | 33,633 | 281 |
| `acerca de` | 38,745 | 32,397 | 283 |
| `sin embargo` | 37,024 | 32,245 | 302 |
| `dentro de` | 31,163 | 27,155 | 371 |
| `por ejemplo` | 28,950 | 25,697 | 415 |
| `ya que` | 27,190 | 24,494 | 447 |
| `por favor` | 22,188 | 19,545 | 548 |
| `gracias a` | 21,895 | 20,055 | 558 |
| `en línea` | 21,418 | 19,462 | 574 |
| `por lo que` | 19,686 | 18,256 | 617 |
| `disfrutar de algo` | 19,565 | 18,050 | 619 |
| `además de` | 18,838 | 17,479 | 643 |
| `contar con algo` | 18,672 | 17,317 | 652 |
| `así que` | 18,491 | 17,231 | 666 |
| `debido a` | 18,042 | 16,692 | 688 |
| `a partir de` | 17,697 | 16,365 | 704 |
| `a continuación` | 17,637 | 16,445 | 709 |
| `convertirse en algo` | 17,624 | 16,334 | 712 |
| `alrededor de` | 16,331 | 15,105 | 765 |
| `fuera de` | 15,695 | 14,562 | 802 |

## Co-occurrence (association) table

100,301,060 tokens, 5,557,244 sentences. After merging and dropping items seen fewer than 5 times: 4,098,834 items (unigrams, UPOS votes, n-grams, pairs); 3,762,812 n-grams and pairs scored (n2 871,413, n3 1,657,355, n4 1,231,016, p2 3,028). Shipped: 400,000 rows, 8.4 MB gzipped (`es.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`es.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `mejor precio` |  | 61,342 | 47,945 | 7.74 | 0.73 | 588,487 |  |
| 2 | n | `respuesta rápido de personal` |  | 22,958 | 20,989 | 10.30 | 0.85 | 334,938 |  |
| 3 | n | `buscar el mejor precio` |  | 22,445 | 20,608 | 9.49 | 0.78 | 298,408 |  |
| 4 | n | `más barato` |  | 35,990 | 31,028 | 6.80 | 0.59 | 298,104 |  |
| 5 | n | `pasaje aereo` |  | 16,288 | 8,613 | 12.03 | 0.96 | 280,501 |  |
| 6 | n | `continuar con la búsqueda` |  | 17,096 | 16,047 | 11.23 | 0.90 | 271,689 |  |
| 7 | n | `personal y los huésped` |  | 18,476 | 17,179 | 10.29 | 0.83 | 267,401 |  |
| 8 | n | `no haber` |  | 65,758 | 51,148 | 4.10 | 0.39 | 262,959 |  |
| 9 | n | `manual de instrucción` |  | 17,194 | 15,818 | 11.17 | 0.89 | 262,915 |  |
| 10 | n | `ser posible` |  | 40,317 | 34,623 | 5.40 | 0.48 | 255,839 |  |
| 11 | n | `buscador de vuelo` |  | 20,212 | 18,726 | 9.18 | 0.75 | 250,580 |  |
| 12 | n | `mejor precio en jetcost` |  | 19,877 | 18,344 | 8.92 | 0.73 | 247,876 |  |
| 13 | n | `estar buscar el mejor` |  | 22,446 | 20,610 | 7.54 | 0.62 | 234,925 |  |
| 14 | n | `precio para su vuelo` |  | 17,864 | 16,687 | 9.31 | 0.75 | 232,428 |  |
| 15 | n | `vuelo regular o vuelo` |  | 17,162 | 16,014 | 9.31 | 0.74 | 223,475 |  |
| 16 | n | `alto calidad` |  | 20,099 | 18,340 | 8.45 | 0.69 | 207,227 |  |
| 17 | n | `estar buscar` |  | 30,412 | 27,133 | 6.00 | 0.51 | 206,436 |  |
| 18 | n | `vuelo low cost` |  | 17,217 | 16,058 | 9.00 | 0.72 | 202,870 |  |
| 19 | n | `que no` |  | 88,447 | 63,412 | 2.69 | 0.26 | 191,689 |  |
| 20 | n | `posible que no haber` |  | 17,111 | 16,059 | 7.39 | 0.59 | 171,174 |  |
| 21 | n | `tipo de` |  | 51,833 | 41,685 | 3.05 | 0.28 | 170,908 |  |
| 22 | n | `para encontrar los vuelo` |  | 19,433 | 18,075 | 6.22 | 0.50 | 162,515 |  |
| 23 | n | `información sobre` |  | 22,472 | 20,327 | 6.20 | 0.51 | 154,681 |  |
| 24 | n | `querer continuar con` |  | 17,113 | 16,060 | 6.50 | 0.52 | 153,526 |  |
| 25 | n | `pronóstico de tiempo` |  | 12,348 | 11,711 | 9.24 | 0.71 | 152,432 |  |
| 26 | n | `ser posible que` |  | 26,210 | 23,752 | 4.99 | 0.42 | 152,423 |  |
| 27 | n | `relacionar con` |  | 20,811 | 18,922 | 5.96 | 0.49 | 150,444 |  |
| 28 | n | `ser posible que no` |  | 17,824 | 16,699 | 6.08 | 0.49 | 146,307 |  |
| 29 | n | `ser muy` |  | 33,713 | 29,131 | 4.26 | 0.37 | 145,800 |  |
| 30 | n | `mejor precio para` |  | 24,928 | 22,661 | 4.98 | 0.42 | 135,472 |  |
| 31 | n | `creer que` |  | 23,824 | 20,316 | 4.89 | 0.41 | 133,659 |  |
| 32 | n | `que no haber resultado` |  | 17,086 | 16,036 | 5.59 | 0.45 | 130,472 |  |
| 33 | n | `a los mejor precio` |  | 21,601 | 19,799 | 4.92 | 0.40 | 126,528 |  |
| 34 | n | `billete avión` |  | 8,426 | 4,270 | 11.25 | 0.83 | 123,768 |  |
| 35 | n | `en vuelo regular` |  | 17,166 | 16,017 | 5.10 | 0.41 | 120,960 |  |
| 36 | n | `me gustar` |  | 11,015 | 9,247 | 8.59 | 0.65 | 114,796 |  |
| 37 | n | `estar disponible` |  | 16,479 | 15,301 | 6.09 | 0.48 | 113,935 |  |
| 38 | n | `decir que` |  | 33,526 | 28,331 | 3.59 | 0.31 | 113,483 |  |
| 39 | n | `cosa que hacer` |  | 12,340 | 11,593 | 7.46 | 0.57 | 113,299 |  |
| 40 | n | `obtener respuesta rápido de` |  | 22,388 | 20,507 | 3.54 | 0.29 | 109,836 |  |
| 41 | n | `acero inoxidable` |  | 6,225 | 5,546 | 12.45 | 0.89 | 108,215 |  |
| 42 | n | `política de privacidad` |  | 7,497 | 6,945 | 11.01 | 0.80 | 107,414 |  |
| 43 | n | `acceso a` |  | 21,430 | 19,251 | 4.42 | 0.36 | 102,780 |  |
| 44 | n | `dato personal` |  | 11,860 | 10,350 | 7.35 | 0.56 | 100,748 |  |
| 45 | n | `que no haber` |  | 23,316 | 21,331 | 4.11 | 0.34 | 97,709 |  |
| 46 | n | `más información` |  | 20,363 | 18,762 | 4.70 | 0.38 | 96,986 |  |
| 47 | n | `comparar tu pasaje aereo` |  | 7,425 | 7,240 | 10.28 | 0.75 | 96,595 |  |
| 48 | n | `necesario para` |  | 17,684 | 16,341 | 4.99 | 0.40 | 96,432 |  |
| 49 | n | `vuelo barato` |  | 11,903 | 8,985 | 6.98 | 0.53 | 94,905 |  |
| 50 | n | `utilizar nuestro buscador de` |  | 19,320 | 17,982 | 3.54 | 0.29 | 94,390 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `reservar se` | `reservarse` | 5,505 | 5,377 | 6.25 | 0.44 | 37,948 |
| `proporcionar se` | `proporcionarse` | 2,470 | 2,420 | 4.61 | 0.30 | 11,176 |
| `visualizar se` | `visualizarse` | 1,228 | 1,214 | 7.23 | 0.44 | 10,385 |

## Rank shifts against the live snapshot (`reference/lemmas/es.json`)

Live list 20,000 lemmas, this build 44,306; 13,346 shared. Spearman rank correlation on the shared lemmas 0.936; median rank ratio 1.14x.
Overlap of this build's top-k with the live top-k: top 1,000 87.4%, top 5,000 83.1%, top 20,000 65.7%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 925 | -17,530 |
| `diecinueve` | 18282 | 1347 | -16,935 |
| `dividirse` | 19076 | 3749 | -15,327 |
| `descanso` | 17625 | 2496 | -15,129 |
| `torno` | 17613 | 2620 | -14,993 |
| `respaldo` | 18269 | 3405 | -14,864 |
| `seiscientos` | 17737 | 3219 | -14,518 |
| `coco` | 18793 | 4311 | -14,482 |
| `secadora` | 19190 | 4926 | -14,264 |
| `parto` | 17982 | 3955 | -14,027 |
| `diecisiete` | 14631 | 1176 | -13,455 |
| `entregarse` | 17153 | 3960 | -13,193 |
| `conforme` | 15056 | 1929 | -13,127 |
| `quinientos` | 14749 | 1811 | -12,938 |
| `empotrar` | 17238 | 4318 | -12,920 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `capar` | 4795 | 43105 | +38,310 |
| `pa` | 3676 | 37957 | +34,281 |
| `sopar` | 4650 | 36951 | +32,301 |
| `marrueco` | 3509 | 35620 | +32,111 |
| `ucranio` | 3401 | 33200 | +29,799 |
| `huevar` | 4037 | 32105 | +28,068 |
| `hondura` | 3735 | 29672 | +25,937 |
| `resinar` | 4093 | 29847 | +25,754 |
| `orlar` | 2655 | 27032 | +24,377 |
| `pablar` | 2158 | 23856 | +21,698 |
| `malasio` | 4644 | 26271 | +21,627 |
| `barbar` | 3789 | 24814 | +21,025 |
| `plomar` | 4817 | 25640 | +20,823 |
| `radio` | 1086 | 21194 | +20,108 |
| `vacación` | 390 | 19430 | +19,040 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `la` | - | 2 | - |
| `los` | - | 8 | - |
| `un` | - | 12 | - |
| `las` | - | 13 | - |
| `una` | - | 14 | - |
| `poder + infinitivo` | - | 20 | - |
| `haber + participio` | - | 27 | - |
| `se + verbo (impersonal/pasiva)` | - | 30 | - |
| `ser + participio` | - | 37 | - |
| `estar + gerundio` | - | 57 | - |
| `parte#Fem` | - | 74 | - |
| `esto` | - | 111 | - |
| `al + infinitivo` | - | 155 | - |
| `a través de` | - | 162 | - |
| `lo + adjetivo` | - | 163 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `del` | 11 | - | - |
| `al` | 22 | - | - |
| `parte` | 59 | 12109 | +12,050 |
| `e` | 94 | - | - |
| `vario` | 265 | 12417 | +12,152 |
| `tripadvisor` | 384 | - | - |
| `relacionado` | 386 | - | - |
| `vacación` | 390 | 19430 | +19,040 |
| `jetcost` | 494 | - | - |
| `x` | 518 | - | - |
| `the` | 531 | - | - |
| `low` | 550 | - | - |
| `cost` | 560 | - | - |
| `cookies` | 565 | - | - |
| `google` | 576 | - | - |

## Ported frequer checks

### Form-ratio outliers (232)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 8,815,852 | median form 60.5; `de` 7,602,335 (125658x), `del` 1,116,771 (18459x), `De` 66,891 (1106x) |
| 6 | `a` | 2,433,526 | median form 138.5; `a` 1,886,118 (13618x), `al` 436,540 (3152x) |
| 7 | `que` | 2,116,286 | median form 3; `que` 2,106,677 (702226x), `Que` 7,713 (2571x) |
| 8 | `los` | 1,751,679 | median form 1497.5; `los` 1,550,152 (1035x) |
| 9 | `ser` | 1,521,558 | median form 46; `es` 660,826 (14366x), `son` 168,181 (3656x), `ser` 137,795 (2996x), `fue` 86,731 (1885x) |
| 10 | `para` | 1,330,434 | median form 3; `para` 1,220,944 (406981x), `Para` 105,507 (35169x) |
| 11 | `con` | 1,137,396 | median form 13; `con` 1,089,681 (83822x), `Con` 45,616 (3509x) |
| 14 | `una` | 906,112 | median form 8.5; `una` 858,166 (100961x), `Una` 46,471 (5467x) |
| 16 | `por` | 794,052 | median form 2; `por` 719,515 (359758x), `Por` 72,313 (36156x) |
| 19 | `poder` | 640,069 | median form 26; `puede` 205,830 (7917x), `pueden` 98,692 (3796x), `puedes` 43,597 (1677x), `poder` 32,536 (1251x) |
| 21 | `haber` | 590,037 | median form 16; `ha` 167,848 (10490x), `han` 77,086 (4818x), `hay` 74,545 (4659x), `había` 38,085 (2380x) |
| 23 | `estar` | 551,915 | median form 42; `está` 193,439 (4606x), `están` 84,176 (2004x) |
| 24 | `más` | 551,722 | median form 6; `más` 507,421 (84570x), `Más` 27,483 (4580x), `mas` 12,845 (2141x) |
| 28 | `tener` | 422,789 | median form 17; `tiene` 117,588 (6917x), `tienen` 49,087 (2887x), `tener` 48,512 (2854x), `tienes` 20,307 (1195x) |
| 29 | `como` | 405,856 | median form 79; `como` 377,987 (4785x) |
| 31 | `lo` | 356,641 | median form 4; `lo` 331,400 (82850x), `Lo` 24,685 (6171x) |
| 32 | `hacer` | 350,848 | median form 8; `hacer` 108,209 (13526x), `hace` 49,304 (6163x), `hecho` 20,223 (2528x), `haciendo` 15,260 (1908x) |
| 38 | `sobre` | 215,779 | median form 42; `sobre` 210,352 (5008x) |
| 40 | `también` | 173,258 | median form 11; `también` 135,717 (12338x), `También` 37,396 (3400x) |
| 41 | `desde` | 167,334 | median form 115.5; `desde` 146,096 (1265x) |
| 43 | `encontrar` | 163,416 | median form 6.5; `encontrar` 63,105 (9708x), `Encuentra` 33,038 (5083x), `encontrarás` 10,693 (1645x), `encontrado` 7,270 (1118x) |
| 46 | `pero` | 159,415 | median form 1.5; `pero` 121,964 (81309x), `Pero` 37,278 (24852x) |
| 55 | `ver` | 149,787 | median form 11; `ver` 54,771 (4979x), `Ver` 21,271 (1934x) |
| 56 | `cuando` | 147,992 | median form 2; `cuando` 106,874 (53437x), `Cuando` 40,983 (20492x) |
| 60 | `deber` | 140,441 | median form 27; `debe` 46,543 (1724x) |

_207 more not shown._

### Singular/plural mismatch (74)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `los` | 1,751,679 | `lo` lemmatises to `lo` (rank 31) |
| 13 | `las` | 1,064,165 | `la` lemmatises to `la` (rank 2) |
| 24 | `más` | 551,722 | `má` lemmatises to `má` (rank 33,846) |
| 135 | `nos` | 65,412 | `no` lemmatises to `no` (rank 17) |
| 144 | `antes` | 62,958 | `ante` lemmatises to `ante` (rank 736) |
| 161 | `dios` | 60,077 | `dio` lemmatises to `dar` (rank 70) |
| 201 | `ellos` | 50,547 | `ello` lemmatises to `ello` (rank 681) |
| 212 | `unos` | 48,531 | `uno` lemmatises to `uno` (rank 52) |
| 256 | `varios` | 42,303 | `vario` lemmatises to `vario` (rank 12,417) |
| 258 | `les` | 41,762 | `le` lemmatises to `le` (rank 58) |
| 269 | `mes` | 39,946 | `me` lemmatises to `me` (rank 93) |
| 301 | `seis` | 37,199 | `sei` lemmatises to `sei` (rank 24,197) |
| 359 | `gracias` | 31,841 | `gracia` lemmatises to `gracia` (rank 2,870) |
| 769 | `pues` | 16,297 | `pue` lemmatises to `pue` (rank 25,983) |
| 786 | `ambos` | 15,963 | `ambo` lemmatises to `ambo` (rank 41,250) |
| 1003 | `ellas` | 12,558 | `ella` lemmatises to `ella` (rank 230) |
| 1160 | `parís` | 10,667 | `parí` lemmatises to `parir` (rank 11,924) |
| 1433 | `lunes` | 8,259 | `lune` lemmatises to `lune` (rank 33,797) |
| 1860 | `alrededores` | 6,092 | `alrededor` lemmatises to `alrededor` (rank 623) |
| 1972 | `martes` | 5,662 | `marte` lemmatises to `mar` (rank 526) |
| 2150 | `quizás` | 5,097 | `quizá` lemmatises to `quizá` (rank 3,031) |
| 2186 | `apenas` | 4,983 | `apena` lemmatises to `apenar` (rank 18,230) |
| 2589 | `microondas` | 3,886 | `microonda` lemmatises to `microonda` (rank 17,563) |
| 2876 | `rines` | 3,339 | `rin` lemmatises to `rin` (rank 12,273) |
| 3034 | `tenis` | 3,069 | `teni` lemmatises to `teni` (rank 21,219) |

_49 more not shown._

### Lemma consistency (262)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 99 | `te` | 86,136 | alone, `te` lemmatises to `se` (rank 18) |
| 351 | `lista` | 32,340 | alone, `lista` lemmatises to `listo` (rank 1,125) |
| 394 | `política` | 29,853 | alone, `política` lemmatises to `político` (rank 708) |
| 522 | `dicho` | 23,134 | alone, `dicho` lemmatises to `decir` (rank 61) |
| 560 | `hecho` | 21,856 | alone, `hecho` lemmatises to `hacer` (rank 32) |
| 575 | `china` | 21,397 | alone, `china` lemmatises to `chino` (rank 1,638) |
| 601 | `presente` | 19,976 | alone, `presente` lemmatises to `presentar` (rank 290) |
| 606 | `fuera` | 19,907 | alone, `fuera` lemmatises to `ser` (rank 9) |
| 611 | `abierto` | 19,826 | alone, `abierto` lemmatises to `abrir` (rank 327) |
| 639 | `ayuda` | 18,893 | alone, `ayuda` lemmatises to `ayudar` (rank 91) |
| 728 | `compra` | 17,255 | alone, `compra` lemmatises to `comprar` (rank 227) |
| 759 | `visita` | 16,592 | alone, `visita` lemmatises to `visitar` (rank 378) |
| 807 | `corto` | 15,655 | alone, `corto` lemmatises to `cortar` (rank 1,413) |
| 818 | `causa` | 15,371 | alone, `causa` lemmatises to `causar` (rank 691) |
| 838 | `carga` | 14,995 | alone, `carga` lemmatises to `cargar` (rank 1,431) |
| 875 | `pedido` | 14,360 | alone, `pedido` lemmatises to `pedir` (rank 509) |
| 880 | `os` | 14,294 | alone, `os` lemmatises to `se` (rank 18) |
| 1019 | `vivo` | 12,385 | alone, `vivo` lemmatises to `vivir` (rank 299) |
| 1087 | `deseo` | 11,540 | alone, `deseo` lemmatises to `desear` (rank 307) |
| 1104 | `empleado` | 11,380 | alone, `empleado` lemmatises to `emplear` (rank 1,658) |
| 1160 | `parís` | 10,667 | alone, `parís` lemmatises to `parir` (rank 11,924) |
| 1164 | `avanzado` | 10,605 | alone, `avanzado` lemmatises to `avanzar` (rank 1,987) |
| 1172 | `falta` | 10,483 | alone, `falta` lemmatises to `faltar` (rank 2,098) |
| 1187 | `aumento` | 10,271 | alone, `aumento` lemmatises to `aumentar` (rank 417) |
| 1211 | `vino` | 10,044 | alone, `vino` lemmatises to `venir` (rank 270) |

_237 more not shown._

### Short lemmas (69)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 8,815,852 | `de` -> `de`, `del` -> `de`, `De` -> `de`, `DE` -> `de`, `Del` -> `de` |
| 2 | `la` | 3,455,134 | `La` -> `la`, `la` -> `la`, `LA` -> `la`, `-La` -> `?` |
| 3 | `en` | 3,008,925 | `en` -> `en`, `En` -> `en`, `EN` -> `en`, `​​en` -> `en` |
| 4 | `y` | 2,977,514 | `y` -> `y`, `Y` -> `y`, `e` -> `y`, `yes` -> `y` |
| 5 | `el` | 2,777,774 | `el` -> `el`, `El` -> `el`, `EL` -> `el`, `eL` -> `el` |
| 6 | `a` | 2,433,526 | `al` -> `a`, `a` -> `a`, `A` -> `a`, `Al` -> `a`, `AL` -> `a` |
| 12 | `un` | 1,096,752 | `un` -> `un`, `Un` -> `un`, `UN` -> `un` |
| 15 | `su` | 889,383 | `su` -> `su`, `sus` -> `su`, `Su` -> `su`, `Sus` -> `su`, `SU` -> `su` |
| 17 | `no` | 686,800 | `no` -> `no`, `No` -> `no`, `NO` -> `no`, `nas` -> `na`, `noes` -> `no` |
| 18 | `se` | 675,821 | `se` -> `se`, `Se` -> `se`, `te` -> `se`, `Te` -> `te`, `me` -> `me` |
| 25 | `o` | 545,246 | `o` -> `o`, `u` -> `o`, `O` -> `o`, `ó` -> `o`, `Ó` -> `o` |
| 31 | `lo` | 356,641 | `lo` -> `lo`, `Lo` -> `lo`, `LO` -> `lo`, `lA` -> `lo`, `lOS` -> `lo` |
| 34 | `tu` | 289,966 | `tus` -> `tu`, `tu` -> `tu`, `Tus` -> `tu`, `Tu` -> `tu`, `TU` -> `tu` |
| 35 | `si` | 268,796 | `Si` -> `si`, `si` -> `si`, `SI` -> `si`, `SiS` -> `si`, `sis` -> `si` |
| 58 | `le` | 143,923 | `le` -> `le`, `Le` -> `le`, `LE` -> `le`, `-Le` -> `le` |
| 68 | `mi` | 121,962 | `mi` -> `mi`, `mis` -> `mi`, `Mis` -> `mi`, `Mi` -> `mi`, `MI` -> `mi` |
| 75 | `ir` | 111,828 | `fuese` -> `ir`, `iba` -> `ir`, `ir` -> `ir`, `vaya` -> `ir`, `va` -> `ir` |
| 88 | `ya` | 95,657 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya`, `-ya` -> `?` |
| 93 | `me` | 89,677 | `me` -> `me`, `Me` -> `me`, `ME` -> `me` |
| 99 | `te` | 86,136 | `te` -> `se`, `Te` -> `te`, `TE` -> `te`, `tes` -> `te` |
| 117 | `él` | 73,977 | `él` -> `él`, `Él` -> `él`, `ÉL` -> `él`, `Èl` -> `él`, `-él` -> `?` |
| 207 | `yo` | 49,631 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo`, `yas` -> `yas`, `yos` -> `yo` |
| 238 | `ni` | 44,387 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni`, `niٌos` -> `?`, `nilos` -> `nilo` |
| 365 | `sí` | 31,593 | `sí` -> `sí`, `si` -> `si`, `Sí` -> `sí`, `SÍ` -> `sí`, `SíEs` -> `sí` |
| 510 | `ti` | 23,739 | `ti` -> `ti`, `TI` -> `ti`, `Ti` -> `ti`, `Tí` -> `ti`, `TÍ` -> `ti` |

_44 more not shown._

### Case merges (1)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4689 | `editorial#Fem` | 1,481 | capitalised but mostly ADJ; no lowercase twin |

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 685 (68.5%).

Ours only: `poder + infinitivo`, `haber + participio`, `se + verbo (impersonal/pasiva)`, `ser + participio`, `vuelo`, `hotel`, `estar + gerundio`, `te`, `archivo`, `habitación`, `barato`, `al + infinitivo`, `a través de`, `lo + adjetivo`, `encontrarse`, `después de`, `para que`, `tener que + infinitivo`, `diseño`, `alojamiento`, `disponible`, `sitio web`, `oferta`, `proporcionar`, `alquiler`

wordfreq only: `nadie`, `mal`, `dr`, `ahí`, `argentino`, `cero`, `listo`, `faltar`, `unido`, `mierda`, `the`, `i`, `c`, `viejo`, `policía`, `elección`, `juan`, `orden#Masc`, `peor`, `voz`, `hola`, `paz`, `militar`, `cargo`, `matar`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 530 | `cookie` | 22,682 | wordfreq zipf en 4.1 vs es 3.0 |
| 812 | `metro#metre` | 15,508 | wordfreq zipf en 3.6 vs es 1.6 |
| 888 | `once` | 14,227 | wordfreq zipf en 5.5 vs es 4.4 |
| 1524 | `led` | 7,657 | wordfreq zipf en 5.1 vs es 3.7 |
| 1883 | `resort` | 5,992 | wordfreq zipf en 4.4 vs es 3.3 |
| 2086 | `show` | 5,305 | wordfreq zipf en 5.7 vs es 4.6 |
| 2591 | `top` | 3,882 | wordfreq zipf en 5.6 vs es 4.4 |
| 2755 | `look` | 3,581 | wordfreq zipf en 5.8 vs es 3.9 |
| 2902 | `stock` | 3,300 | wordfreq zipf en 4.9 vs es 3.8 |
| 2905 | `set` | 3,296 | wordfreq zipf en 5.6 vs es 4.1 |
| 2992 | `reserve` | 3,137 | wordfreq zipf en 4.6 vs es 3.1 |
| 3389 | `parking` | 2,538 | wordfreq zipf en 4.5 vs es 3.1 |
| 3531 | `ticket` | 2,380 | wordfreq zipf en 4.6 vs es 3.5 |
| 3571 | `as` | 2,328 | wordfreq zipf en 6.8 vs es 4.7 |
| 3904 | `feed` | 2,009 | wordfreq zipf en 4.7 vs es 3.3 |
| 4004 | `test` | 1,932 | wordfreq zipf en 5.2 vs es 4.2 |
| 4250 | `bit` | 1,751 | wordfreq zipf en 5.4 vs es 3.2 |
| 4597 | `per` | 1,532 | wordfreq zipf en 5.5 vs es 4.4 |
| 4692 | `real#royal` | 1,481 | wordfreq zipf en 4.8 vs es 3.7 |
| 4844 | `film` | 1,390 | wordfreq zipf en 5.2 vs es 4.1 |
| 5005 | `stand` | 1,319 | wordfreq zipf en 5.1 vs es 3.8 |
| 5041 | `metro#railway` | 1,299 | wordfreq zipf en 4.0 vs es 2.6 |
| 5543 | `box` | 1,080 | wordfreq zipf en 5.0 vs es 3.8 |
| 5572 | `country` | 1,068 | wordfreq zipf en 5.5 vs es 3.8 |
| 5573 | `host` | 1,068 | wordfreq zipf en 4.8 vs es 3.3 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 161 | `dios` | 60,077 | PROPN 0%, capitalised forms 94% |
| 366 | `estados unidos` | 31,586 | PROPN 0%, capitalised forms 100% |
| 439 | `españa` | 27,603 | PROPN 100%, capitalised forms 100% |
| 498 | `san` | 24,279 | PROPN 2%, capitalised forms 96% |
| 575 | `china` | 21,397 | PROPN 100%, capitalised forms 100% |
| 696 | `méxico` | 17,814 | PROPN 100%, capitalised forms 100% |
| 722 | `tv` | 17,411 | PROPN 6%, capitalised forms 97% |
| 858 | `madrid` | 14,651 | PROPN 99%, capitalised forms 99% |
| 1000 | `israel` | 12,587 | PROPN 100%, capitalised forms 100% |
| 1159 | `nueva york` | 10,712 | PROPN 100%, capitalised forms 100% |
| 1160 | `parís` | 10,667 | PROPN 99%, capitalised forms 100% |
| 1186 | `francia` | 10,294 | PROPN 100%, capitalised forms 100% |
| 1245 | `londres` | 9,732 | PROPN 100%, capitalised forms 100% |
| 1334 | `wi-fi` | 9,008 | PROPN 1%, capitalised forms 97% |
| 1353 | `alemania` | 8,805 | PROPN 100%, capitalised forms 100% |
| 1404 | `italia` | 8,419 | PROPN 100%, capitalised forms 100% |
| 1411 | `colombia` | 8,364 | PROPN 100%, capitalised forms 99% |
| 1479 | `pc` | 7,912 | PROPN 11%, capitalised forms 98% |
| 1496 | `roma` | 7,810 | PROPN 99%, capitalised forms 100% |
| 1567 | `chile` | 7,418 | PROPN 93%, capitalised forms 94% |
| 1582 | `reino unido` | 7,337 | PROPN 0%, capitalised forms 100% |
| 1598 | `canadá` | 7,278 | PROPN 100%, capitalised forms 100% |
| 1641 | `japón` | 7,046 | PROPN 99%, capitalised forms 99% |
| 1648 | `usb` | 7,025 | PROPN 96%, capitalised forms 98% |
| 1651 | `ue` | 7,018 | PROPN 100%, capitalised forms 100% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 99.0% | 0.998 |
| juilland_u | 99.9% | 1.000 |
| juilland_u_corrected | 99.9% | 1.000 |
| dp_adjusted | 99.8% | 1.000 |
| cd_blend | 99.5% | 0.999 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `imprescindible` | 4386 | 4233 | -153 | 1,816 | 1,803 | 0.974 | 0.105 |
| `si bien` | 5050 | 4900 | -150 | 1,442 | 1,435 | 0.976 | 0.095 |
| `originalmente` | 4397 | 4247 | -150 | 1,809 | 1,793 | 0.978 | 0.094 |
| `en efecto` | 5008 | 4858 | -150 | 1,465 | 1,456 | 0.975 | 0.100 |
| `triponline` | 4681 | 4533 | -148 | 1,633 | 1,626 | 0.973 | 0.105 |
| `tomás` | 3894 | 6341 | +2,447 | 2,183 | 930 | 0.933 | 0.260 |
| `love` | 3119 | 5053 | +1,934 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4507 | 6168 | +1,661 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4985 | 6361 | +1,376 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4237 | 5580 | +1,343 | 1,912 | 1,158 | 0.967 | 0.136 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `desafiar` | 5016 | 4995 | -21 | 1,462 | 1,438 | 0.978 | 0.086 |
| `conectarse` | 4595 | 4575 | -20 | 1,682 | 1,647 | 0.979 | 0.089 |
| `a cargo de` | 4364 | 4345 | -19 | 1,828 | 1,808 | 0.979 | 0.082 |
| `subrayar` | 4766 | 4747 | -19 | 1,584 | 1,570 | 0.978 | 0.085 |
| `esquema` | 3838 | 3821 | -17 | 2,231 | 2,129 | 0.983 | 0.066 |
| `tomás` | 3894 | 4021 | +127 | 2,183 | 930 | 0.933 | 0.260 |
| `canadiense` | 4302 | 4339 | +37 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1310 | 1345 | +35 | 9,271 | 3,893 | 0.966 | 0.131 |
| `casado` | 4255 | 4286 | +31 | 1,901 | 1,716 | 0.966 | 0.117 |
| `remate` | 4237 | 4267 | +30 | 1,912 | 1,158 | 0.967 | 0.136 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `doctrina` | 4362 | 4351 | -11 | 1,829 | 1,727 | 0.979 | 0.082 |
| `incentivo` | 4894 | 4883 | -11 | 1,521 | 1,469 | 0.974 | 0.105 |
| `solicitante` | 4360 | 4349 | -11 | 1,830 | 1,738 | 0.977 | 0.101 |
| `silver` | 4363 | 4352 | -11 | 1,829 | 1,786 | 0.978 | 0.089 |
| `presión arterial` | 4661 | 4651 | -10 | 1,646 | 1,578 | 0.977 | 0.092 |
| `tomás` | 3894 | 4021 | +127 | 2,183 | 930 | 0.933 | 0.260 |
| `canadiense` | 4302 | 4337 | +35 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1310 | 1345 | +35 | 9,271 | 3,893 | 0.966 | 0.131 |
| `casado` | 4255 | 4287 | +32 | 1,901 | 1,716 | 0.966 | 0.117 |
| `remate` | 4237 | 4267 | +30 | 1,912 | 1,158 | 0.967 | 0.136 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `procurar` | 4307 | 4219 | -88 | 1,867 | 1,844 | 0.981 | 0.070 |
| `desafiar` | 5016 | 4939 | -77 | 1,462 | 1,438 | 0.978 | 0.086 |
| `básicamente` | 4317 | 4243 | -74 | 1,857 | 1,833 | 0.982 | 0.072 |
| `esquema` | 3838 | 3767 | -71 | 2,231 | 2,129 | 0.983 | 0.066 |
| `consistente` | 4885 | 4816 | -69 | 1,522 | 1,500 | 0.978 | 0.088 |
| `tomás` | 3894 | 4412 | +518 | 2,183 | 930 | 0.933 | 0.260 |
| `ascendente` | 4507 | 4692 | +185 | 1,733 | 975 | 0.962 | 0.160 |
| `love` | 3119 | 3252 | +133 | 3,093 | 1,365 | 0.966 | 0.140 |
| `model` | 4985 | 5109 | +124 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4237 | 4352 | +115 | 1,912 | 1,158 | 0.967 | 0.136 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `caracterizarse por algo` | 4637 | 4551 | -86 | 1,661 | 1,647 | 0.976 | 0.096 |
| `en efecto` | 5008 | 4925 | -83 | 1,465 | 1,456 | 0.975 | 0.100 |
| `comúnmente` | 4638 | 4556 | -82 | 1,661 | 1,641 | 0.974 | 0.106 |
| `comprensible` | 4932 | 4850 | -82 | 1,500 | 1,493 | 0.974 | 0.108 |
| `triponline` | 4681 | 4599 | -82 | 1,633 | 1,626 | 0.973 | 0.105 |
| `tomás` | 3894 | 5007 | +1,113 | 2,183 | 930 | 0.933 | 0.260 |
| `love` | 3119 | 3982 | +863 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4507 | 5301 | +794 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4985 | 5645 | +660 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4237 | 4874 | +637 | 1,912 | 1,158 | 0.967 | 0.136 |

## Excluded lemmas

`es.tsv` (sha256 `d65cd2427cf419f2`) lists 1,404 exclusions; 596 lemmas were dropped from the top 20,000 before cutting it (exclude-abbreviation 26, exclude-boilerplate 14, exclude-english 489, exclude-foreign 13, exclude-fragment 6, exclude-letter 24, exclude-numeral 24). Lower ranks moved up.

| rank before | lemma | class | reason |
|---|---|---|---|
| 477 | `jetcost` | exclude-boilerplate | flight-search site brand |
| 540 | `low` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 551 | `cost` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 578 | `aereo` | exclude-boilerplate | unaccented template spelling of aéreo |
| 754 | `the` | exclude-english | English article |
| 1035 | `x` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1184 | `á` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1225 | `of` | exclude-english | English preposition |
| 1307 | `city` | exclude-english | English word in names |
| 1359 | `b` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1449 | `c` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1475 | `in` | exclude-english | English preposition |
| 1481 | `i` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1642 | `and` | exclude-english | English conjunction |
| 1798 | `beach` | exclude-english | not a Spanish loan |
| 1809 | `d` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1847 | `ii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 1953 | `m` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1966 | `new` | exclude-english | English template text |
| 2124 | `home` | exclude-english | English template text |
| 2231 | `t` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2393 | `g` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2443 | `to` | exclude-english | English preposition |
| 2549 | `house` | exclude-english | English template text |
| 2590 | `v` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2621 | `hp` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 2694 | `by` | exclude-english | English preposition |
| 2706 | `k` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2818 | `black` | exclude-english | English colour word |
| 2835 | `n` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2838 | `e` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2889 | `r` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2910 | `grand` | exclude-english | English in brand names |
| 2919 | `airport` | exclude-english | English for aeropuerto |
| 3034 | `island` | exclude-english | English place word |
| 3045 | `f` | exclude-letter | developer 2026-11-01: single letters excluded |
| 3061 | `on` | exclude-english | English preposition |
| 3110 | `international` | exclude-english | English for internacional |
| 3119 | `love` | exclude-english | English word |
| 3136 | `iii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 3153 | `for` | exclude-english | English preposition |
| 3171 | `air` | exclude-english | English in brand names |
| 3173 | `best` | exclude-english | English word |
| 3188 | `west` | exclude-english | English place word |
| 3193 | `ltd` | exclude-boilerplate | company-name template suffix |
| 3197 | `lg` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 3293 | `di` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3295 | `world` | exclude-english | English word |
| 3302 | `group` | exclude-english | English word in names |
| 3353 | `mb` | exclude-abbreviation | abbreviation or unit symbol (developer 2026-11-01: abbreviations excluded for now) |
| 3480 | `english` | exclude-english | English word |
| 3523 | `car` | exclude-english | English word |
| 3550 | `do` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3561 | `one` | exclude-english | English word |
| 3661 | `white` | exclude-english | English colour word |
| 3671 | `mainland` | exclude-english | English listing text |
| 3687 | `us` | exclude-english | English pronoun/domain |
| 3698 | `am` | exclude-english | English time suffix |
| 3719 | `file` | exclude-english | English for archivo |
| 3752 | `business` | exclude-english | English word |

_536 more in the exclusion file._


## Junk-filter heuristics

Rules on: diversity, citation, foreign, shape, propn_band; accent merges at ratio 5.0. Window: the 29,157 ranked lemmas (after the exclusion list) that fill the top 20,000. Actions: drop 23, keep 19,235, propn-drop 6,483, review-drop 2,651, review-keep 765.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band |
|---|---:|---:|---:|---:|---:|
| diversity | 53 | 0 | 3 | 3 | 8 |
| citation | 0 | 42 | 0 | 20 | 0 |
| foreign | 3 | 0 | 1,734 | 51 | 740 |
| shape | 3 | 20 | 51 | 664 | 327 |
| propn_band | 8 | 0 | 740 | 327 | 3,106 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 6,483.

### Low diversity

Documents reached / documents expected at random, below 0.6 (frequency >= 20): 53 in the window. For comparison, each log2-frequency band's 2nd percentile: 16-31: 0.72, 32-63: 0.75, 64-127: 0.77, 128-255: 0.78, 256-511: 0.81, 512-1023: 0.83, 1024-2047: 0.84, 2048-4095: 0.85, 4096-8191: 0.86, 8192-16383: 0.86, 16384-32767: 0.87, 32768-65535: 0.85.

Examples: `tom` (294), `mary` (1301), `tiquete` (2283), `tomás` (3829), `ascendente` (4425), `pseudónimo` (5524), `pseudo` (5619), `de aquí en adelante` (5968), `netcomponents` (6332), `yanni` (8454), `tomasa` (8759), `bora` (9198), `microarea` (10321), `yahvé` (10637), `moncler` (10920), `wishtrips` (11431), `ziri` (13327), `alugom` (14964), `fpnm` (15503), `asimtap` (15585), `luge` (17333), `campings` (17543), `vbulletin` (18727), `consultores` (18753), `langa` (18849), `prorock-perforación` (19243), `invoice` (19371), `fossil` (20466), `skura` (21228), `gotesa` (21474), `pcbs` (21726), `stardoll` (22602), `idnet` (24091), `walla` (24167), `dimatra` (24220), `allover` (24318), `nopb` (24413), `edifier` (24966), `linked` (25504), `megaexit` (25510)

### Accent merges (1,377)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `manager` | `mánager` | 1,903 | review: merge |
| `junior` | `júnior` | 896 | review: merge |
| `inscríbete` | `inscribir` | 717 | review: merge |
| `santa` | `santo` | 685 | review: merge |
| `vieja` | `viejo` | 631 | review: merge |
| `pixel` | `píxel` | 567 | review: merge |
| `indígeno` | `indígena` | 549 | review: merge |
| `herpe` | `herpes` | 460 | review: merge |
| `boulevard` | `bulevar` | 443 | review: merge |
| `lesbiano` | `lesbiana` | 427 | review: merge |
| `alojándote` | `alojar` | 419 | review: merge |
| `bowl` | `bol` | 414 | review: merge |
| `abagado` | `abogado` | 397 | review: merge |
| `paise` | `país` | 393 | review: merge |
| `ud` | `usted` | 393 | review: merge |
| `cappuccino` | `capuchino` | 389 | review: merge |
| `corner` | `córner` | 307 | review: merge |
| `trave` | `través` | 307 | review: merge |
| `aumentor` | `aumento` | 298 | review: merge |
| `pymes` | `pyme` | 279 | review: merge |
| `guru` | `gurú` | 276 | review: merge |
| `tragamoneda` | `tragamonedas` | 274 | review: merge |
| `drone` | `dron` | 270 | review: merge |
| `vendidor` | `vendedor` | 267 | review: merge |
| `fotocopiador` | `fotocopiadora` | 257 | review: merge |
| `champagne` | `champán` | 240 | review: merge |
| `bistro` | `bistró` | 230 | review: merge |
| `garage` | `garaje` | 222 | review: merge |
| `comisionada` | `comisionado` | 207 | review: merge |
| `cricket` | `críquet` | 206 | review: merge |
| `padel` | `pádel` | 198 | review: merge |
| `scanner` | `escáner` | 198 | review: merge |
| `sándwiche` | `sándwich` | 198 | review: merge |
| `post-venta` | `posventa` | 196 | review: merge |
| `lavaplato` | `lavaplatos` | 195 | review: merge |
| `mándano` | `mandar` | 190 | review: merge |
| `cactu` | `cactus` | 187 | review: merge |
| `sandwich` | `sándwich` | 186 | review: merge |
| `momio` | `momia` | 185 | review: merge |
| `basándono` | `basar` | 182 | review: merge |
| `derby` | `derbi` | 181 | review: merge |
| `mg` | `miligramo` | 178 | review: merge |
| `sabienda` | `sabiendas` | 171 | review: merge |
| `mir` | `mirar` | 169 | review: merge |
| `shampoo` | `champú` | 166 | review: merge |
| `euromillón` | `euromillones` | 164 | review: merge |
| `pizzeria` | `pizzería` | 163 | review: merge |
| `epidermi` | `epidermis` | 161 | review: merge |
| `tobogan` | `tobogán` | 160 | review: merge |
| `seca` | `seco` | 154 | review: merge |
| `mola` | `molar` | 152 | review: merge |
| `trio` | `trío` | 151 | review: merge |
| `escoje` | `escoger` | 150 | review: merge |
| `baccarat` | `bacarrá` | 149 | review: merge |
| `belg` | `belga` | 147 | review: merge |
| `ofreciéndol` | `ofrecer` | 144 | review: merge |
| `capitulo` | `capítulo` | 143 | review: merge |
| `pony` | `poni` | 143 | review: merge |
| `dándol` | `dar` | 140 | review: merge |
| `sha` | `sah` | 138 | review: merge |
| `directa` | `directo` | 136 | review: merge |
| `altibajo` | `altibajos` | 135 | review: merge |
| `reunion` | `reunión` | 135 | review: merge |
| `samurai` | `samurái` | 134 | review: merge |
| `pbi` | `pib` | 133 | review: merge |
| `diciéndol` | `decir` | 132 | review: merge |
| `cds` | `cd` | 131 | review: merge |
| `cubiertaa` | `cubierta` | 131 | review: merge |
| `leed` | `leer` | 130 | review: merge |
| `limonado` | `limonada` | 127 | review: merge |
| `implícitas` | `implícito` | 122 | review: merge |
| `llámeno` | `llamar` | 104 | review: merge |
| `crash` | `crac` | 120 | review: merge |
| `profilaxi` | `profilaxis` | 119 | review: merge |
| `ayúdeno` | `ayudar` | 118 | review: merge |
| `dejarno` | `dejar` | 118 | review: merge |
| `ebooks` | `ebook` | 118 | review: merge |
| `l-carnitina` | `carnitina` | 117 | review: merge |
| `apoyor` | `apoyo` | 115 | review: merge |
| `párr` | `párrafo` | 82 | review: merge |
| `permitiéndol` | `permitir` | 110 | review: merge |
| `guardabarro` | `guardabarros` | 108 | review: merge |
| `aparcacoche` | `aparcacoches` | 107 | review: merge |
| `refr` | `refrán` | 107 | review: merge |
| `fue` | `ser` | 105 | review: merge |
| `ria` | `ría` | 105 | review: merge |
| `handicap` | `hándicap` | 104 | review: merge |
| `déco` | `decó` | 103 | review: merge |
| `bicis` | `bici` | 102 | review: merge |
| `limpiaparabrisa` | `limpiaparabrisas` | 102 | review: merge |
| `esforzándono` | `esforzar` | 101 | review: merge |
| `contactándono` | `contactar` | 100 | review: merge |
| `tinnitu` | `tinnitus` | 100 | review: merge |
| `enseñándol` | `enseñar` | 99 | review: merge |
| `baseball` | `béisbol` | 98 | review: merge |
| `tablets` | `tablet` | 96 | review: merge |
| `mini-bar` | `minibar` | 95 | review: merge |
| `switche` | `switch` | 94 | review: merge |
| `watt` | `vatio` | 94 | review: merge |
| `chili` | `chile` | 92 | review: merge |
| `kung` | `kung fu` | 92 | review: merge |
| `cutter` | `cúter` | 91 | review: merge |
| `raton` | `ratón` | 91 | review: merge |
| `reposacabeza` | `reposacabezas` | 91 | review: merge |
| `tumbón` | `tumbona` | 91 | review: merge |
| `iran` | `irán` | 90 | review: merge |
| `permítano` | `permitir` | 87 | review: merge |
| `anti-envejecimiento` | `antienvejecimiento` | 86 | review: merge |
| `carótido` | `carótida` | 86 | review: merge |
| `co-fundador` | `cofundador` | 86 | review: merge |
| `haciéndol` | `hacer` | 84 | review: merge |
| `clorofilo` | `clorofila` | 82 | review: merge |
| `rodillero` | `rodillera` | 82 | review: merge |
| `sintaxi` | `sintaxis` | 82 | review: merge |
| `proporcionarno` | `proporcionar` | 80 | review: merge |
| `anti-virus` | `antivirus` | 78 | review: merge |
| `antidisturbio` | `antidisturbios` | 78 | review: merge |
| `vu` | `déjà vu` | 78 | review: merge |
| `ata` | `atar` | 76 | review: merge |
| `das` | `dar` | 75 | review: merge |
| `perrero` | `perrera` | 75 | review: merge |
| `reflex` | `réflex` | 75 | review: merge |
| `recorré` | `recorrer` | 74 | review: merge |
| `siéntete` | `sentir` | 74 | review: merge |
| `hipotecaria` | `hipotecario` | 73 | review: merge |
| `ponerno` | `poner` | 73 | review: merge |
| `proporcionándol` | `proporcionar` | 73 | review: merge |
| `rayos-x` | `rayos x` | 73 | review: merge |
| `socio-económico` | `socioeconómico` | 73 | review: merge |
| `ajur` | `ajustar` | 72 | review: merge |
| `elevaluna` | `elevalunas` | 72 | review: merge |
| `visitarno` | `visitar` | 72 | review: merge |
| `volveo` | `volver` | 72 | review: merge |
| `adentrarno` | `adentrar` | 71 | review: merge |
| `bunker` | `búnker` | 71 | review: merge |
| `portavaso` | `portavasos` | 71 | review: merge |
| `yoyo` | `yoyó` | 71 | review: merge |
| `basket` | `básquet` | 70 | review: merge |
| `chueca` | `chueco` | 69 | review: merge |
| `cuclilla` | `cuclillas` | 69 | review: merge |
| `adaptarno` | `adaptar` | 67 | review: merge |
| `albatro` | `albatros` | 67 | review: merge |
| `paris` | `parís` | 67 | review: merge |
| `roulette` | `ruleta` | 67 | review: merge |
| `notificarno` | `notificar` | 66 | review: merge |
| `antiarruga` | `antiarrugas` | 65 | review: merge |
| `busque` | `buscar` | 65 | review: merge |
| `configure` | `configurar` | 65 | review: merge |
| `maquilador` | `maquiladora` | 65 | review: merge |
| `boomerang` | `bumerán` | 64 | review: merge |
| `co-creación` | `cocreación` | 64 | review: merge |
| `reposabrazo` | `reposabrazos` | 64 | review: merge |
| `cognac` | `coñac` | 63 | review: merge |
| `gachó` | `gachas` | 63 | review: merge |
| `informacion` | `información` | 63 | review: merge |
| `magnifico` | `magnífico` | 63 | review: merge |
| `mrur` | `morir` | 63 | review: merge |
| `outlets` | `outlet` | 63 | review: merge |
| `regañadiente` | `regañadientes` | 63 | review: merge |
| `acompáñano` | `acompañar` | 62 | review: merge |
| `anti-spam` | `antispam` | 62 | review: merge |
| `ohm` | `ohmio` | 62 | review: merge |
| `brindándol` | `brindar` | 60 | review: merge |
| `anti-inflamatorio` | `antiinflamatorio` | 59 | review: merge |
| `centrándono` | `centrar` | 59 | review: merge |
| `chia` | `chía` | 59 | review: merge |
| `corticoesteroid` | `corticoesteroide` | 59 | review: merge |
| `sana` | `sano` | 59 | review: merge |
| `ase` | `as` | 58 | review: merge |
| `autocargadore` | `autocargador` | 58 | review: merge |
| `sharia` | `sharía` | 58 | review: merge |
| `lio` | `lío` | 57 | review: merge |
| `miercol` | `miércoles` | 57 | review: merge |
| `convertirno` | `convertir` | 56 | review: merge |
| `socio-cultural` | `sociocultural` | 56 | review: merge |
| `crucis` | `viacrucis` | 55 | review: merge |
| `empleados` | `empleado` | 55 | review: merge |
| `pop-ups` | `pop-up` | 55 | review: merge |
| `ad-hoc` | `ad hoc` | 54 | review: merge |
| `extension` | `extensión` | 1,476 | accented spelling 23,091 vs 1,476 |
| `america` | `américa` | 1,441 | accented spelling 12,868 vs 1,441 |
| `codigo` | `código` | 1,086 | accented spelling 32,497 vs 1,086 |
| `via` | `vía` | 930 | accented spelling 21,894 vs 930 |
| `berlin` | `berlín` | 922 | accented spelling 8,376 vs 922 |
| `union` | `unión` | 889 | accented spelling 11,821 vs 889 |
| `jose` | `josé` | 834 | accented spelling 11,508 vs 834 |
| `menu` | `menú` | 807 | accented spelling 18,863 vs 807 |
| `canada` | `canadá` | 744 | accented spelling 13,068 vs 744 |
| `panama` | `panamá` | 702 | accented spelling 7,056 vs 702 |
| `salon` | `salón` | 600 | accented spelling 22,539 vs 600 |
| `angel` | `ángel` | 589 | accented spelling 8,793 vs 589 |
| `dragon` | `dragón` | 555 | accented spelling 3,047 vs 555 |
| `record` | `récord` | 539 | accented spelling 3,306 vs 539 |
| `futbol` | `fútbol` | 501 | accented spelling 12,444 vs 501 |
| `personalizacion` | `personalización` | 484 | accented spelling 3,128 vs 484 |
| `compañia` | `compañía` | 471 | accented spelling 52,815 vs 471 |
| `pension` | `pensión` | 470 | accented spelling 4,062 vs 470 |
| `fusion` | `fusión` | 455 | accented spelling 4,506 vs 455 |
| `milan` | `milán` | 454 | accented spelling 7,210 vs 454 |
| `peru` | `perú` | 431 | accented spelling 10,456 vs 431 |
| `cordoba` | `córdoba` | 406 | accented spelling 3,647 vs 406 |
| `tenia` | `tener` | 403 | accented spelling 16,589 vs 403 |
| `television` | `televisión` | 391 | accented spelling 23,718 vs 391 |
| `region` | `región` | 361 | accented spelling 37,370 vs 361 |
| `dia` | `día` | 357 | accented spelling 241,849 vs 357 |
| `aaron` | `aarón` | 351 | accented spelling 2,694 vs 351 |
| `dublin` | `dublín` | 348 | accented spelling 4,872 vs 348 |
| `cancer` | `cáncer` | 333 | accented spelling 27,580 vs 333 |
| `napoles` | `nápoles` | 330 | accented spelling 2,108 vs 330 |
| `version` | `versión` | 329 | accented spelling 41,815 vs 329 |
| `bahia` | `bahía` | 323 | accented spelling 6,912 vs 323 |
| `busqueda` | `búsqueda` | 316 | accented spelling 79,593 vs 316 |
| `raices` | `raíz` | 308 | accented spelling 3,813 vs 308 |
| `galeria` | `galería` | 290 | accented spelling 9,631 vs 290 |
| `guardian` | `guardián` | 273 | accented spelling 1,365 vs 273 |
| `taiwan` | `taiwán` | 261 | accented spelling 2,153 vs 261 |
| `telefono` | `teléfono` | 257 | accented spelling 56,221 vs 257 |
| `comodo` | `cómodo` | 256 | accented spelling 22,248 vs 256 |
| `lopez` | `lópez` | 240 | accented spelling 2,366 vs 240 |
| `almeria` | `almería` | 237 | accented spelling 2,176 vs 237 |
| `todavia` | `todavía` | 236 | accented spelling 35,817 vs 236 |
| `corazon` | `corazón` | 234 | accented spelling 50,329 vs 234 |
| `andalucia` | `andalucía` | 232 | accented spelling 3,700 vs 232 |
| `canton` | `cantón` | 232 | accented spelling 1,523 vs 232 |
| `coctel` | `cóctel` | 232 | accented spelling 2,062 vs 232 |
| `garcia` | `garcía` | 231 | accented spelling 2,896 vs 231 |
| `linea` | `línea` | 231 | accented spelling 117,770 vs 231 |
| `nicolas` | `nicolás` | 230 | accented spelling 1,164 vs 230 |
| `malaga` | `málaga` | 230 | accented spelling 8,858 vs 230 |
| `area` | `área` | 229 | accented spelling 57,697 vs 229 |
| `vehiculo` | `vehículo` | 225 | accented spelling 28,358 vs 225 |
| `ingles` | `inglés` | 224 | accented spelling 59,331 vs 224 |
| `carbon` | `carbón` | 219 | accented spelling 3,880 vs 219 |
| `fantasia` | `fantasía` | 215 | accented spelling 3,288 vs 215 |
| `precision` | `precisión` | 212 | accented spelling 14,271 vs 212 |
| `poliester` | `poliéster` | 212 | accented spelling 3,235 vs 212 |
| `bateria` | `batería` | 209 | accented spelling 23,024 vs 209 |
| `merida` | `mérida` | 208 | accented spelling 1,168 vs 208 |
| `oir` | `oír` | 205 | accented spelling 13,101 vs 205 |
| `sidney` | `sídney` | 199 | accented spelling 1,890 vs 199 |
| `ramon` | `ramón` | 198 | accented spelling 1,168 vs 198 |
| `pelicula` | `película` | 197 | accented spelling 30,461 vs 197 |
| `rodriguez` | `rodríguez` | 194 | accented spelling 2,118 vs 194 |
| `descripcion` | `descripción` | 194 | accented spelling 47,897 vs 194 |
| `boton` | `botón` | 192 | accented spelling 32,762 vs 192 |
| `camara` | `cámara` | 189 | accented spelling 36,340 vs 189 |
| `construccion` | `construcción` | 188 | accented spelling 38,225 vs 188 |
| `martinez` | `martínez` | 187 | accented spelling 1,592 vs 187 |
| `jovenes` | `joven` | 186 | accented spelling 14,618 vs 186 |
| `album` | `álbum` | 182 | accented spelling 7,222 vs 182 |
| `tecnologia` | `tecnología` | 182 | accented spelling 60,296 vs 182 |
| `genesis` | `génesis` | 180 | accented spelling 1,906 vs 180 |
| `electrico` | `eléctrico` | 176 | accented spelling 25,392 vs 176 |
| `estacion` | `estación` | 175 | accented spelling 36,900 vs 175 |
| `perdida` | `pérdida` | 175 | accented spelling 25,622 vs 175 |
| `principe` | `príncipe` | 174 | accented spelling 4,849 vs 174 |
| `division` | `división` | 173 | accented spelling 8,681 vs 173 |
| `podria` | `poder` | 169 | accented spelling 26,364 vs 169 |
| `juarez` | `juárez` | 165 | accented spelling 1,000 vs 165 |
| `habitat` | `hábitat` | 164 | accented spelling 2,356 vs 164 |
| `mansion` | `mansión` | 163 | accented spelling 1,732 vs 163 |
| `item` | `ítem` | 157 | accented spelling 1,185 vs 157 |
| `optima` | `óptimo` | 156 | accented spelling 3,440 vs 156 |
| `replica` | `réplica` | 151 | accented spelling 1,287 vs 151 |
| `gonzalez` | `gonzález` | 150 | accented spelling 1,978 vs 150 |
| `guias` | `guía` | 149 | accented spelling 4,165 vs 149 |
| `increible` | `increíble` | 148 | accented spelling 13,430 vs 148 |
| `perez` | `pérez` | 147 | accented spelling 1,552 vs 147 |
| `hare` | `hacer` | 147 | accented spelling 1,879 vs 147 |
| `estandar` | `estándar` | 146 | accented spelling 30,084 vs 146 |
| `economico` | `económico` | 145 | accented spelling 33,275 vs 145 |
| `paraiso` | `paraíso` | 145 | accented spelling 4,648 vs 145 |
| `salomon` | `salomón` | 141 | accented spelling 2,376 vs 141 |
| `peninsula` | `península` | 141 | accented spelling 2,670 vs 141 |
| `formula` | `fórmula` | 138 | accented spelling 6,255 vs 138 |
| `opcion` | `opción` | 138 | accented spelling 69,198 vs 138 |
| `gomez` | `gómez` | 137 | accented spelling 1,120 vs 137 |
| `seran` | `ser` | 135 | accented spelling 13,941 vs 135 |
| `atico` | `ático` | 135 | accented spelling 2,565 vs 135 |
| `fotografia` | `fotografía` | 131 | accented spelling 14,535 vs 131 |
| `monaco` | `mónaco` | 130 | accented spelling 890 vs 130 |
| `garantia` | `garantía` | 129 | accented spelling 27,176 vs 129 |
| `jehova` | `jehová` | 128 | accented spelling 17,482 vs 128 |
| `cache` | `caché` | 127 | accented spelling 1,857 vs 127 |
| `credito` | `crédito` | 127 | accented spelling 14,921 vs 127 |
| `relacion` | `relación` | 125 | accented spelling 63,638 vs 125 |
| `rincon` | `rincón` | 124 | accented spelling 4,351 vs 124 |
| `modem` | `módem` | 123 | accented spelling 773 vs 123 |
| `basico` | `básico` | 122 | accented spelling 18,496 vs 122 |
| `mexico` | `méxico` | 122 | accented spelling 35,384 vs 122 |
| `aplicacion` | `aplicación` | 121 | accented spelling 93,165 vs 121 |
| `mediterraneo` | `mediterráneo` | 120 | accented spelling 7,465 vs 120 |
| `cristobal` | `cristóbal` | 119 | accented spelling 798 vs 119 |
| `frances` | `francés` | 118 | accented spelling 19,271 vs 118 |
| `neon` | `neón` | 118 | accented spelling 637 vs 118 |
| `diaz` | `díaz` | 118 | accented spelling 1,022 vs 118 |
| `banus` | `banús` | 116 | accented spelling 1,030 vs 116 |
| `dias` | `día` | 116 | accented spelling 69,098 vs 116 |
| `historico` | `histórico` | 116 | accented spelling 20,354 vs 116 |
| `distribucion` | `distribución` | 116 | accented spelling 18,876 vs 116 |
| `avila` | `ávila` | 115 | accented spelling 612 vs 115 |
| `espiritu` | `espíritu` | 115 | accented spelling 28,186 vs 115 |
| `bolivar` | `bolívar` | 115 | accented spelling 881 vs 115 |
| `turistico` | `turístico` | 114 | accented spelling 13,212 vs 114 |
| `balcon` | `balcón` | 112 | accented spelling 10,928 vs 112 |
| `policia` | `policía` | 112 | accented spelling 16,712 vs 112 |
| `automaticamente` | `automáticamente` | 112 | accented spelling 17,990 vs 112 |
| `toner` | `tóner` | 111 | accented spelling 750 vs 111 |
| `sanchez` | `sánchez` | 110 | accented spelling 1,444 vs 110 |
| `plastico` | `plástico` | 110 | accented spelling 19,772 vs 110 |
| `angulo` | `ángulo` | 109 | accented spelling 5,887 vs 109 |
| `mandarin` | `mandarín` | 109 | accented spelling 739 vs 109 |
| `grafico` | `gráfico` | 107 | accented spelling 14,386 vs 107 |
| `pokemon` | `pokémon` | 107 | accented spelling 1,567 vs 107 |
| `tecnicos` | `técnico` | 107 | accented spelling 6,623 vs 107 |
| `proximo` | `próximo` | 106 | accented spelling 31,313 vs 106 |
| `sabado` | `sábado` | 106 | accented spelling 15,146 vs 106 |
| `francfort` | `fráncfort` | 105 | accented spelling 2,028 vs 105 |
| `instalacion` | `instalación` | 105 | accented spelling 42,685 vs 105 |
| `fabricacion` | `fabricación` | 103 | accented spelling 22,708 vs 103 |
| `marmol` | `mármol` | 103 | accented spelling 3,799 vs 103 |
| `sofa` | `sofá` | 103 | accented spelling 8,635 vs 103 |
| `haiti` | `haití` | 102 | accented spelling 2,114 vs 102 |
| `dali` | `dalí` | 102 | accented spelling 636 vs 102 |
| `lucia` | `lucir` | 101 | accented spelling 843 vs 101 |
| `calefaccion` | `calefacción` | 101 | accented spelling 14,847 vs 101 |
| `opinion` | `opinión` | 101 | accented spelling 42,272 vs 101 |
| `movil` | `móvil` | 100 | accented spelling 36,368 vs 100 |
| `tia` | `tía` | 100 | accented spelling 1,170 vs 100 |
| `proximamente` | `próximamente` | 99 | accented spelling 872 vs 99 |
| `miro` | `mirar` | 99 | accented spelling 1,432 vs 99 |
| `rapidamente` | `rápidamente` | 98 | accented spelling 22,912 vs 98 |
| `tomas` | `tomás` | 97 | accented spelling 4,172 vs 97 |
| `alvaro` | `álvaro` | 95 | accented spelling 636 vs 95 |
| `situacion` | `situación` | 95 | accented spelling 39,153 vs 95 |
| `terminos` | `término` | 94 | accented spelling 21,115 vs 94 |
| `estanteria` | `estantería` | 93 | accented spelling 1,550 vs 93 |
| `informatica` | `informática` | 93 | accented spelling 3,896 vs 93 |
| `clasico` | `clásico` | 90 | accented spelling 13,318 vs 90 |
| `concepcion` | `concepción` | 90 | accented spelling 3,549 vs 90 |
| `hernandez` | `hernández` | 90 | accented spelling 1,370 vs 90 |
| `reir` | `reír` | 89 | accented spelling 1,872 vs 89 |
| `ramirez` | `ramírez` | 88 | accented spelling 706 vs 88 |
| `organo` | `órgano` | 88 | accented spelling 6,715 vs 88 |
| `aerolinea` | `aerolínea` | 88 | accented spelling 10,567 vs 88 |
| `capitan` | `capitán` | 87 | accented spelling 3,689 vs 87 |
| `economia` | `economía` | 87 | accented spelling 20,821 vs 87 |
| `judio` | `judío` | 87 | accented spelling 7,551 vs 87 |
| `pais` | `país` | 87 | accented spelling 114,187 vs 87 |
| `sera` | `ser` | 86 | accented spelling 43,354 vs 86 |
| `articulos` | `artículo` | 86 | accented spelling 19,269 vs 86 |
| `visito` | `visitar` | 86 | accented spelling 855 vs 86 |
| `facil` | `fácil` | 86 | accented spelling 58,574 vs 86 |
| `aqui` | `aquí` | 86 | accented spelling 129,460 vs 86 |
| `conexion` | `conexión` | 85 | accented spelling 45,407 vs 85 |
| `electrodomestico` | `electrodoméstico` | 85 | accented spelling 2,017 vs 85 |
| `proposito` | `propósito` | 85 | accented spelling 18,080 vs 85 |
| `veronica` | `verónica` | 85 | accented spelling 456 vs 85 |
| `raiz` | `raíz` | 84 | accented spelling 8,992 vs 84 |
| `urbanizacion` | `urbanización` | 84 | accented spelling 3,847 vs 84 |
| `produccion` | `producción` | 84 | accented spelling 51,960 vs 84 |
| `tendra` | `tener` | 83 | accented spelling 11,330 vs 83 |
| `mato` | `matar` | 83 | accented spelling 984 vs 83 |
| `queria` | `querer` | 83 | accented spelling 6,205 vs 83 |
| `educacion` | `educación` | 83 | accented spelling 35,049 vs 83 |
| `cabrio` | `cabrío` | 83 | accented spelling 433 vs 83 |
| `reparacion` | `reparación` | 82 | accented spelling 10,572 vs 82 |
| `mazatlan` | `mazatlán` | 82 | accented spelling 616 vs 82 |
| `duo` | `dúo` | 82 | accented spelling 1,020 vs 82 |
| `salmon` | `salmón` | 82 | accented spelling 1,373 vs 82 |
| `decision` | `decisión` | 82 | accented spelling 26,616 vs 82 |
| `cordon` | `cordón` | 81 | accented spelling 3,577 vs 81 |
| `fernandez` | `fernández` | 81 | accented spelling 1,270 vs 81 |
| `cadiz` | `cádiz` | 81 | accented spelling 1,440 vs 81 |
| `turistica` | `turístico` | 81 | accented spelling 2,238 vs 81 |
| `portatil` | `portátil` | 80 | accented spelling 14,289 vs 80 |
| `analisis` | `análisis` | 79 | accented spelling 39,479 vs 79 |
| `tecnico` | `técnico` | 79 | accented spelling 34,009 vs 79 |
| `atletico` | `atlético` | 79 | accented spelling 1,183 vs 79 |
| `revision` | `revisión` | 79 | accented spelling 12,756 vs 79 |
| `recien` | `recién` | 79 | accented spelling 10,261 vs 79 |
| `gestion` | `gestión` | 78 | accented spelling 47,793 vs 78 |
| `fatima` | `fátima` | 78 | accented spelling 772 vs 78 |
| `carton` | `cartón` | 78 | accented spelling 6,033 vs 78 |
| `razon` | `razón` | 77 | accented spelling 29,468 vs 77 |
| `latex` | `látex` | 77 | accented spelling 1,020 vs 77 |
| `estabamos` | `estar` | 77 | accented spelling 1,835 vs 77 |
| `coleccion` | `colección` | 76 | accented spelling 25,848 vs 76 |
| `fenix` | `fénix` | 76 | accented spelling 400 vs 76 |
| `jupiter` | `júpiter` | 76 | accented spelling 883 vs 76 |
| `ruben` | `rubén` | 76 | accented spelling 932 vs 76 |
| `tandem` | `tándem` | 76 | accented spelling 409 vs 76 |
| `jimenez` | `jiménez` | 76 | accented spelling 632 vs 76 |
| `africa` | `áfrica` | 75 | accented spelling 10,521 vs 75 |
| `mision` | `misión` | 75 | accented spelling 19,357 vs 75 |
| `dimension` | `dimensión` | 75 | accented spelling 8,810 vs 75 |
| `oman` | `omán` | 74 | accented spelling 450 vs 74 |
| `categoria` | `categoría` | 73 | accented spelling 36,901 vs 73 |
| `seleccion` | `selección` | 73 | accented spelling 26,205 vs 73 |
| `habra` | `haber` | 73 | accented spelling 5,590 vs 73 |
| `energia` | `energía` | 73 | accented spelling 56,887 vs 73 |
| `podia` | `poder` | 72 | accented spelling 7,159 vs 72 |
| `decoracion` | `decoración` | 72 | accented spelling 13,435 vs 72 |
| `ingenieria` | `ingeniería` | 72 | accented spelling 12,200 vs 72 |
| `creacion` | `creación` | 71 | accented spelling 25,638 vs 71 |
| `lampara` | `lámpara` | 71 | accented spelling 8,910 vs 71 |
| `presentacion` | `presentación` | 71 | accented spelling 19,735 vs 71 |
| `corfu` | `corfú` | 71 | accented spelling 396 vs 71 |
| `multiple` | `múltiple` | 71 | accented spelling 10,793 vs 71 |
| `salio` | `salir` | 70 | accented spelling 3,380 vs 70 |
| `tanger` | `tánger` | 70 | accented spelling 544 vs 70 |
| `especificamente` | `específicamente` | 70 | accented spelling 7,790 vs 70 |
| `teneis` | `tener` | 69 | accented spelling 1,656 vs 69 |
| `epoca` | `época` | 69 | accented spelling 15,643 vs 69 |
| `automatico` | `automático` | 69 | accented spelling 26,505 vs 69 |
| `hector` | `héctor` | 68 | accented spelling 480 vs 68 |
| `antiguedad` | `antigüedad` | 68 | accented spelling 3,128 vs 68 |
| `comparacion` | `comparación` | 68 | accented spelling 18,041 vs 68 |
| `aguila` | `águila` | 67 | accented spelling 1,274 vs 67 |
| `identico` | `idéntico` | 67 | accented spelling 1,876 vs 67 |
| `pregunto` | `preguntar` | 67 | accented spelling 2,641 vs 67 |
| `masia` | `masía` | 67 | accented spelling 386 vs 67 |
| `rene` | `rené` | 66 | accented spelling 454 vs 66 |
| `proxima` | `próximo` | 66 | accented spelling 5,634 vs 66 |
| `organizacion` | `organización` | 66 | accented spelling 43,538 vs 66 |
| `redireccion` | `redirección` | 66 | accented spelling 468 vs 66 |
| `sudan` | `sudán` | 66 | accented spelling 1,504 vs 66 |
| `envie` | `enviar` | 66 | accented spelling 3,512 vs 66 |
| `alegria` | `alegría` | 66 | accented spelling 7,737 vs 66 |
| `cafe` | `café` | 65 | accented spelling 22,309 vs 65 |
| `basilica` | `basílica` | 65 | accented spelling 1,885 vs 65 |
| `centrico` | `céntrico` | 65 | accented spelling 3,010 vs 65 |
| `joaquin` | `joaquín` | 64 | accented spelling 768 vs 64 |
| `baku` | `bakú` | 64 | accented spelling 510 vs 64 |
| `raul` | `raúl` | 63 | accented spelling 956 vs 63 |
| `ceramica` | `cerámica` | 63 | accented spelling 5,252 vs 63 |
| `oi` | `oír` | 63 | accented spelling 723 vs 63 |
| `valvula` | `válvula` | 63 | accented spelling 7,277 vs 63 |
| `electron` | `electrón` | 63 | accented spelling 728 vs 63 |
| `esten` | `estar` | 63 | accented spelling 7,988 vs 63 |
| `torreon` | `torreón` | 62 | accented spelling 384 vs 62 |
| `religion` | `religión` | 62 | accented spelling 8,461 vs 62 |
| `chavez` | `chávez` | 62 | accented spelling 1,370 vs 62 |
| `valparaiso` | `valparaíso` | 62 | accented spelling 448 vs 62 |
| `beisbol` | `béisbol` | 61 | accented spelling 2,612 vs 61 |
| `agustin` | `agustín` | 60 | accented spelling 864 vs 60 |
| `estes` | `estar` | 60 | accented spelling 2,642 vs 60 |
| `pakistan` | `pakistán` | 60 | accented spelling 2,436 vs 60 |
| `asociacion` | `asociación` | 60 | accented spelling 20,771 vs 60 |
| `fantasias` | `fantasía` | 60 | accented spelling 564 vs 60 |
| `configuracion` | `configuración` | 60 | accented spelling 30,475 vs 60 |
| `comunicacion` | `comunicación` | 59 | accented spelling 39,770 vs 59 |
| `conversion` | `conversión` | 59 | accented spelling 9,877 vs 59 |
| `metropolis` | `metrópolis` | 59 | accented spelling 484 vs 59 |
| `agricola` | `agrícola` | 59 | accented spelling 6,626 vs 59 |
| `satelite` | `satélite` | 59 | accented spelling 11,805 vs 59 |
| `megapixel` | `megapíxel` | 58 | accented spelling 301 vs 58 |
| `rustico` | `rústico` | 58 | accented spelling 1,792 vs 58 |
| `saul` | `saúl` | 58 | accented spelling 2,520 vs 58 |
| `simbolo` | `símbolo` | 58 | accented spelling 7,858 vs 58 |
| `elias` | `elías` | 57 | accented spelling 1,688 vs 57 |
| `osea` | `óseo` | 57 | accented spelling 565 vs 57 |
| `edicion` | `edición` | 57 | accented spelling 18,773 vs 57 |
| `fundacion` | `fundación` | 56 | accented spelling 13,860 vs 56 |
| `mejoro` | `mejorar` | 56 | accented spelling 437 vs 56 |
| `amen` | `amén` | 56 | accented spelling 521 vs 56 |
| `grafica` | `gráfica` | 56 | accented spelling 3,788 vs 56 |
| `sinai` | `sinaí` | 56 | accented spelling 732 vs 56 |
| `parana` | `paraná` | 56 | accented spelling 330 vs 56 |
| `inversion` | `inversión` | 56 | accented spelling 21,271 vs 56 |
| `tio` | `tío` | 55 | accented spelling 3,050 vs 55 |
| `turisticas` | `turístico` | 55 | accented spelling 1,663 vs 55 |
| `napoleon` | `napoleón` | 55 | accented spelling 669 vs 55 |
| `suarez` | `suárez` | 55 | accented spelling 570 vs 55 |
| `pajaro` | `pájaro` | 55 | accented spelling 3,637 vs 55 |
| `culiacan` | `culiacán` | 54 | accented spelling 282 vs 54 |
| `metodo` | `método` | 54 | accented spelling 27,865 vs 54 |
| `cajon` | `cajón` | 54 | accented spelling 2,370 vs 54 |
| `ayudo` | `ayudar` | 54 | accented spelling 1,846 vs 54 |
| `investigacion` | `investigación` | 53 | accented spelling 49,114 vs 53 |
| `hosteria` | `hostería` | 53 | accented spelling 452 vs 53 |
| `tomo` | `tomar` | 53 | accented spelling 4,350 vs 53 |
| `esqui` | `esquí` | 52 | accented spelling 7,976 vs 52 |
| `podrian` | `poder` | 52 | accented spelling 9,806 vs 52 |
| `joyeria` | `joyería` | 52 | accented spelling 5,759 vs 52 |
| `fantastico` | `fantástico` | 52 | accented spelling 10,364 vs 52 |
| `ocasion` | `ocasión` | 51 | accented spelling 17,571 vs 51 |
| `dario` | `darío` | 51 | accented spelling 396 vs 51 |
| `limon` | `limón` | 51 | accented spelling 3,830 vs 51 |
| `vivian` | `vivir` | 51 | accented spelling 741 vs 51 |
| `clinica` | `clínica` | 50 | accented spelling 8,035 vs 50 |
| `dire` | `decir` | 50 | accented spelling 569 vs 50 |
| `habitacion` | `habitación` | 50 | accented spelling 86,436 vs 50 |
| `joas` | `joás` | 50 | accented spelling 328 vs 50 |
| `maritimo` | `marítimo` | 50 | accented spelling 4,987 vs 50 |
| `oceania` | `oceanía` | 50 | accented spelling 876 vs 50 |
| `eliminacion` | `eliminación` | 50 | accented spelling 10,940 vs 50 |
| `asesoria` | `asesoría` | 50 | accented spelling 2,769 vs 50 |
| `vision` | `visión` | 50 | accented spelling 24,091 vs 50 |
| `actua` | `actuar` | 50 | accented spelling 2,180 vs 50 |
| `politico` | `político` | 49 | accented spelling 21,985 vs 49 |
| `centrica` | `céntrico` | 49 | accented spelling 1,414 vs 49 |
| `recepcion` | `recepción` | 49 | accented spelling 15,303 vs 49 |
| `rubi` | `rubí` | 49 | accented spelling 394 vs 49 |
| `carpinteria` | `carpintería` | 49 | accented spelling 1,214 vs 49 |
| `eleccion` | `elección` | 49 | accented spelling 18,732 vs 49 |
| `logistica` | `logística` | 48 | accented spelling 4,540 vs 48 |
| `oracion` | `oración` | 48 | accented spelling 11,583 vs 48 |
| `mana` | `maná` | 48 | accented spelling 580 vs 48 |
| `peluqueria` | `peluquería` | 48 | accented spelling 1,229 vs 48 |
| `estadia` | `estadía` | 47 | accented spelling 3,421 vs 47 |
| `ines` | `inés` | 47 | accented spelling 294 vs 47 |
| `diametro` | `diámetro` | 47 | accented spelling 7,569 vs 47 |
| `gaudi` | `gaudí` | 47 | accented spelling 990 vs 47 |
| `sotano` | `sótano` | 47 | accented spelling 2,063 vs 47 |
| `noto` | `notar` | 46 | accented spelling 297 vs 46 |
| `tenian` | `tener` | 46 | accented spelling 5,357 vs 46 |
| `amon` | `amón` | 46 | accented spelling 450 vs 46 |
| `exodo` | `éxodo` | 46 | accented spelling 914 vs 46 |
| `almacen` | `almacén` | 45 | accented spelling 5,590 vs 45 |
| `excursion` | `excursión` | 45 | accented spelling 8,234 vs 45 |
| `musculo` | `músculo` | 45 | accented spelling 5,976 vs 45 |
| `benalmadena` | `benalmádena` | 45 | accented spelling 402 vs 45 |
| `causo` | `causar` | 45 | accented spelling 871 vs 45 |
| `venia` | `venir` | 45 | accented spelling 827 vs 45 |
| `lavanderia` | `lavandería` | 45 | accented spelling 5,607 vs 45 |
| `alcala` | `alcalá` | 45 | accented spelling 932 vs 45 |
| `efectua` | `efectuar` | 44 | accented spelling 489 vs 44 |
| `consultoria` | `consultoría` | 44 | accented spelling 3,449 vs 44 |
| `salvacion` | `salvación` | 44 | accented spelling 5,335 vs 44 |
| `situa` | `situar` | 44 | accented spelling 477 vs 44 |
| `quimica` | `química` | 44 | accented spelling 5,540 vs 44 |
| `fluor` | `flúor` | 44 | accented spelling 400 vs 44 |
| `duracion` | `duración` | 44 | accented spelling 18,612 vs 44 |
| `debera` | `deber` | 44 | accented spelling 8,292 vs 44 |
| `mojacar` | `mojácar` | 44 | accented spelling 326 vs 44 |
| `nacion` | `nación` | 43 | accented spelling 12,114 vs 43 |
| `turin` | `turín` | 43 | accented spelling 1,311 vs 43 |
| `tripoli` | `trípoli` | 43 | accented spelling 248 vs 43 |
| `cañon` | `cañón` | 43 | accented spelling 3,132 vs 43 |
| `barcelo` | `barceló` | 43 | accented spelling 446 vs 43 |
| `direccion` | `dirección` | 43 | accented spelling 64,258 vs 43 |
| `capita` | `cápita` | 42 | accented spelling 906 vs 42 |
| `deberia` | `deber` | 42 | accented spelling 13,223 vs 42 |
| `periodico` | `periódico` | 42 | accented spelling 7,480 vs 42 |
| `etcetera` | `etcétera` | 42 | accented spelling 20,189 vs 42 |
| `expansion` | `expansión` | 42 | accented spelling 7,834 vs 42 |
| `comite` | `comité` | 42 | accented spelling 13,805 vs 42 |
| `automatica` | `automático` | 42 | accented spelling 7,400 vs 42 |
| `marquez` | `márquez` | 42 | accented spelling 602 vs 42 |
| `tuberia` | `tubería` | 42 | accented spelling 4,889 vs 42 |
| `sesion` | `sesión` | 42 | accented spelling 30,283 vs 42 |
| `aleman` | `alemán` | 41 | accented spelling 18,218 vs 41 |
| `paises` | `país` | 41 | accented spelling 32,806 vs 41 |
| `dominguez` | `domínguez` | 41 | accented spelling 242 vs 41 |
| `varian` | `variar` | 41 | accented spelling 1,642 vs 41 |
| `marti` | `martí` | 41 | accented spelling 494 vs 41 |
| `sonreir` | `sonreír` | 41 | accented spelling 2,212 vs 41 |
| `diversion` | `diversión` | 41 | accented spelling 7,042 vs 41 |
| `proteina` | `proteína` | 41 | accented spelling 6,722 vs 41 |
| `tes` | `té` | 41 | accented spelling 238 vs 41 |
| `dare` | `dar` | 41 | accented spelling 1,046 vs 41 |
| `generacion` | `generación` | 41 | accented spelling 19,694 vs 41 |
| `suspension` | `suspensión` | 41 | accented spelling 5,954 vs 41 |
| `tobias` | `tobías` | 40 | accented spelling 250 vs 40 |
| `exposicion` | `exposición` | 40 | accented spelling 19,225 vs 40 |
| `arabes` | `árabe` | 40 | accented spelling 1,068 vs 40 |
| `reune` | `reunir` | 40 | accented spelling 1,551 vs 40 |
| `canaan` | `canaán` | 40 | accented spelling 868 vs 40 |
| `pantalon` | `pantalón` | 40 | accented spelling 5,343 vs 40 |
| `autobus` | `autobús` | 40 | accented spelling 28,418 vs 40 |
| `latinoamerica` | `latinoamérica` | 40 | accented spelling 3,562 vs 40 |
| `algodon` | `algodón` | 40 | accented spelling 11,094 vs 40 |
| `recuperacion` | `recuperación` | 39 | accented spelling 13,101 vs 39 |
| `andres` | `andrés` | 39 | accented spelling 1,878 vs 39 |
| `fisico` | `físico` | 39 | accented spelling 19,527 vs 39 |
| `poesia` | `poesía` | 39 | accented spelling 2,093 vs 39 |
| `ambar` | `ámbar` | 39 | accented spelling 621 vs 39 |
| `acne` | `acné` | 39 | accented spelling 2,190 vs 39 |
| `caracteristicas` | `característica` | 39 | accented spelling 16,421 vs 39 |
| `nucleo` | `núcleo` | 39 | accented spelling 6,096 vs 39 |
| `marques` | `marqués` | 39 | accented spelling 620 vs 39 |
| `unico` | `único` | 39 | accented spelling 54,410 vs 39 |
| `parametro#railway` | `parámetro` | 39 | accented spelling 6,551 vs 39 |
| `calida` | `cálido` | 39 | accented spelling 1,197 vs 39 |
| `alcazar` | `alcázar` | 38 | accented spelling 524 vs 38 |
| `hindu` | `hindú` | 38 | accented spelling 753 vs 38 |
| `belgica` | `bélgica` | 38 | accented spelling 3,680 vs 38 |
| `oyo` | `oír` | 38 | accented spelling 891 vs 38 |
| `muchisimas` | `mucho` | 38 | accented spelling 559 vs 38 |
| `inspiracion` | `inspiración` | 38 | accented spelling 5,188 vs 38 |
| `rustica` | `rústico` | 38 | accented spelling 320 vs 38 |
| `termico` | `térmico` | 38 | accented spelling 5,374 vs 38 |
| `catalan` | `catalán` | 38 | accented spelling 2,612 vs 38 |
| `precaucion` | `precaución` | 38 | accented spelling 3,474 vs 38 |
| `celula` | `célula` | 38 | accented spelling 10,224 vs 38 |
| `cirugia` | `cirugía` | 38 | accented spelling 13,734 vs 38 |
| `localizacion` | `localización` | 38 | accented spelling 6,263 vs 38 |
| `nuñez` | `núñez` | 38 | accented spelling 362 vs 38 |
| `niger` | `níger` | 38 | accented spelling 518 vs 38 |
| `declaracion` | `declaración` | 38 | accented spelling 22,213 vs 38 |
| `deberian` | `deber` | 38 | accented spelling 4,247 vs 38 |
| `belen` | `belén` | 38 | accented spelling 1,481 vs 38 |
| `fundo` | `fundar` | 38 | accented spelling 960 vs 38 |
| `menton` | `mentón` | 37 | accented spelling 302 vs 37 |
| `jaen` | `jaén` | 37 | accented spelling 578 vs 37 |
| `osmosis` | `ósmosis` | 37 | accented spelling 326 vs 37 |
| `contemporaneo` | `contemporáneo` | 37 | accented spelling 6,177 vs 37 |
| `armonia` | `armonía` | 37 | accented spelling 3,660 vs 37 |
| `mercancia` | `mercancía` | 37 | accented spelling 5,022 vs 37 |
| `conte` | `contar` | 37 | accented spelling 190 vs 37 |
| `reunen` | `reunir` | 37 | accented spelling 303 vs 37 |
| `judios` | `judío` | 37 | accented spelling 3,771 vs 37 |
| `habeis` | `haber` | 37 | accented spelling 3,024 vs 37 |
| `utopia` | `utopía` | 36 | accented spelling 400 vs 36 |
| `trebol` | `trébol` | 36 | accented spelling 367 vs 36 |
| `baterias` | `batería` | 36 | accented spelling 3,260 vs 36 |
| `condicion` | `condición` | 36 | accented spelling 51,902 vs 36 |
| `romantica` | `romántico` | 36 | accented spelling 1,079 vs 36 |
| `poblacion` | `población` | 36 | accented spelling 27,261 vs 36 |
| `pondran` | `poner` | 36 | accented spelling 327 vs 36 |
| `ebola` | `ébola` | 36 | accented spelling 734 vs 36 |
| `alava` | `álava` | 36 | accented spelling 370 vs 36 |
| `ambito` | `ámbito` | 36 | accented spelling 12,777 vs 36 |
| `rapido` | `rápido` | 36 | accented spelling 77,029 vs 36 |
| `espectaculo` | `espectáculo` | 36 | accented spelling 6,786 vs 36 |
| `salon-comedor` | `salón-comedor` | 36 | accented spelling 1,898 vs 36 |
| `introduccion` | `introducción` | 36 | accented spelling 10,924 vs 36 |
| `pergola` | `pérgola` | 35 | accented spelling 388 vs 35 |
| `cientifico` | `científico` | 35 | accented spelling 13,900 vs 35 |
| `galata` | `gálata` | 35 | accented spelling 212 vs 35 |
| `sintoma` | `síntoma` | 35 | accented spelling 11,281 vs 35 |
| `celiaco` | `celíaco` | 35 | accented spelling 236 vs 35 |
| `libreria` | `librería` | 35 | accented spelling 2,031 vs 35 |
| `teoria` | `teoría` | 35 | accented spelling 8,272 vs 35 |
| `belarus` | `belarús` | 35 | accented spelling 280 vs 35 |
| `juda` | `judá` | 35 | accented spelling 4,868 vs 35 |
| `tora` | `torá` | 34 | accented spelling 796 vs 34 |
| `fotografo` | `fotógrafo` | 34 | accented spelling 3,545 vs 34 |
| `versiculo` | `versículo` | 34 | accented spelling 1,927 vs 34 |
| `ramadan` | `ramadán` | 34 | accented spelling 344 vs 34 |
| `romantico` | `romántico` | 34 | accented spelling 5,201 vs 34 |
| `huesped` | `huésped` | 34 | accented spelling 34,669 vs 34 |
| `sudamerica` | `sudamérica` | 33 | accented spelling 1,362 vs 33 |
| `reir#actual` | `reír` | 33 | accented spelling 1,872 vs 33 |
| `haran` | `hacer` | 33 | accented spelling 2,314 vs 33 |
| `millon` | `millón` | 33 | accented spelling 33,833 vs 33 |
| `peticion` | `petición` | 33 | accented spelling 13,058 vs 33 |
| `respondio` | `responder` | 33 | accented spelling 3,922 vs 33 |
| `brujula` | `brújula` | 33 | accented spelling 768 vs 33 |
| `argan` | `argán` | 33 | accented spelling 287 vs 33 |
| `reproduccion` | `reproducción` | 33 | accented spelling 10,669 vs 33 |
| `yucatan` | `yucatán` | 33 | accented spelling 666 vs 33 |
| `comision` | `comisión` | 33 | accented spelling 21,523 vs 33 |
| `catolica` | `católico` | 33 | accented spelling 1,665 vs 33 |
| `exito` | `éxito` | 33 | accented spelling 32,805 vs 33 |
| `tradicion` | `tradición` | 32 | accented spelling 10,421 vs 32 |
| `talon` | `talón` | 32 | accented spelling 1,641 vs 32 |
| `comodas` | `cómodo` | 32 | accented spelling 1,755 vs 32 |
| `encontre` | `encontrar` | 32 | accented spelling 1,666 vs 32 |
| `recibira` | `recibir` | 32 | accented spelling 2,788 vs 32 |
| `daria` | `dar` | 32 | accented spelling 666 vs 32 |
| `lamparas` | `lámpara` | 32 | accented spelling 1,739 vs 32 |
| `basicamente` | `básicamente` | 32 | accented spelling 3,650 vs 32 |
| `discipulo` | `discípulo` | 32 | accented spelling 4,502 vs 32 |
| `bavaro` | `bávaro` | 32 | accented spelling 362 vs 32 |
| `iria` | `ir` | 32 | accented spelling 295 vs 32 |
| `fantastica` | `fantástico` | 32 | accented spelling 3,129 vs 32 |
| `teniamos` | `tener` | 31 | accented spelling 1,488 vs 31 |
| `acropolis` | `acrópolis` | 31 | accented spelling 366 vs 31 |
| `quimico` | `químico` | 31 | accented spelling 7,082 vs 31 |
| `sono` | `sonar` | 31 | accented spelling 246 vs 31 |
| `vivi` | `vivir` | 31 | accented spelling 228 vs 31 |
| `mendez` | `méndez` | 31 | accented spelling 334 vs 31 |
| `sillon` | `sillón` | 31 | accented spelling 1,594 vs 31 |
| `indices` | `índice` | 31 | accented spelling 1,381 vs 31 |
| `gijon` | `gijón` | 31 | accented spelling 688 vs 31 |
| `catolicos` | `católico` | 31 | accented spelling 1,156 vs 31 |
| `jerusalen` | `jerusalén` | 31 | accented spelling 7,836 vs 31 |
| `simeon` | `simeón` | 31 | accented spelling 404 vs 31 |
| `elaboracion` | `elaboración` | 31 | accented spelling 7,167 vs 31 |
| `pekin` | `pekín` | 31 | accented spelling 2,238 vs 31 |
| `gastronomia` | `gastronomía` | 31 | accented spelling 3,999 vs 31 |
| `invasion` | `invasión` | 31 | accented spelling 2,153 vs 31 |
| `soller` | `sóller` | 31 | accented spelling 258 vs 31 |
| `manifesto` | `manifestar` | 31 | accented spelling 560 vs 31 |
| `regalia` | `regalía` | 31 | accented spelling 448 vs 31 |
| `orientacion` | `orientación` | 31 | accented spelling 9,211 vs 31 |
| `decidi` | `decidir` | 30 | accented spelling 1,247 vs 30 |
| `musee` | `musée` | 30 | accented spelling 238 vs 30 |
| `sabeis` | `saber` | 30 | accented spelling 1,003 vs 30 |
| `parr` | `párr` | 30 | accented spelling 164 vs 30 |
| `gondola` | `góndola` | 30 | accented spelling 296 vs 30 |
| `fotografias` | `fotografía` | 30 | accented spelling 4,603 vs 30 |
| `preparacion` | `preparación` | 30 | accented spelling 12,421 vs 30 |
| `deberan` | `deber` | 30 | accented spelling 3,555 vs 30 |
| `podre` | `poder` | 30 | accented spelling 465 vs 30 |
| `microscopia` | `microscopía` | 30 | accented spelling 212 vs 30 |
| `colibri` | `colibrí` | 30 | accented spelling 197 vs 30 |
| `innovacion` | `innovación` | 30 | accented spelling 16,147 vs 30 |
| `digito` | `dígito` | 30 | accented spelling 1,160 vs 30 |
| `segun` | `según` | 30 | accented spelling 77,403 vs 30 |
| `artesania` | `artesanía` | 29 | accented spelling 3,062 vs 29 |
| `filosofia` | `filosofía` | 29 | accented spelling 5,814 vs 29 |
| `aerolineas` | `aerolínea` | 29 | accented spelling 8,069 vs 29 |
| `violin` | `violín` | 29 | accented spelling 780 vs 29 |
| `mascara` | `máscara` | 29 | accented spelling 3,950 vs 29 |
| `extraible` | `extraíble` | 29 | accented spelling 1,147 vs 29 |
| `omnibus` | `ómnibus` | 29 | accented spelling 224 vs 29 |
| `tendran` | `tener` | 29 | accented spelling 4,703 vs 29 |
| `perdon` | `perdón` | 29 | accented spelling 3,386 vs 29 |
| `restauracion` | `restauración` | 29 | accented spelling 5,041 vs 29 |
| `planto` | `plantar` | 29 | accented spelling 162 vs 29 |
| `cain` | `caín` | 29 | accented spelling 538 vs 29 |
| `graficas` | `gráfico` | 29 | accented spelling 1,037 vs 29 |
| `economica` | `económico` | 29 | accented spelling 7,110 vs 29 |
| `guzman` | `guzmán` | 29 | accented spelling 603 vs 29 |
| `moises` | `moisés` | 29 | accented spelling 8,409 vs 29 |
| `maiz` | `maíz` | 29 | accented spelling 3,875 vs 29 |
| `decia` | `decir` | 28 | accented spelling 2,555 vs 28 |
| `olvido` | `olvidar` | 28 | accented spelling 586 vs 28 |
| `tropico` | `trópico` | 28 | accented spelling 317 vs 28 |
| `devolucion` | `devolución` | 28 | accented spelling 6,272 vs 28 |
| `olimpico` | `olímpico` | 28 | accented spelling 1,707 vs 28 |
| `crater` | `cráter` | 28 | accented spelling 718 vs 28 |
| `japon` | `japón` | 28 | accented spelling 13,999 vs 28 |
| `manten` | `mantener` | 28 | accented spelling 1,370 vs 28 |
| `economicas` | `económico` | 28 | accented spelling 3,098 vs 28 |
| `tension` | `tensión` | 28 | accented spelling 9,033 vs 28 |
| `navegacion` | `navegación` | 28 | accented spelling 15,756 vs 28 |
| `formo` | `formar` | 28 | accented spelling 467 vs 28 |
| `helicoptero` | `helicóptero` | 27 | accented spelling 2,208 vs 27 |
| `celiaca` | `celíaco` | 27 | accented spelling 149 vs 27 |
| `dara` | `dar` | 27 | accented spelling 3,963 vs 27 |
| `acontecio` | `acontecer` | 27 | accented spelling 568 vs 27 |
| `quizas` | `quizás` | 27 | accented spelling 10,139 vs 27 |
| `mahon` | `mahón` | 27 | accented spelling 463 vs 27 |
| `evaluacion` | `evaluación` | 27 | accented spelling 20,695 vs 27 |
| `colaboracion` | `colaboración` | 27 | accented spelling 15,554 vs 27 |
| `volo` | `volar` | 27 | accented spelling 220 vs 27 |
| `regimen` | `régimen` | 27 | accented spelling 8,980 vs 27 |
| `aragon` | `aragón` | 27 | accented spelling 841 vs 27 |
| `volcan` | `volcán` | 27 | accented spelling 2,577 vs 27 |
| `asuncion` | `asunción` | 27 | accented spelling 1,583 vs 27 |
| `delfin` | `delfín` | 27 | accented spelling 1,165 vs 27 |
| `pego` | `pegar` | 27 | accented spelling 160 vs 27 |
| `castellon` | `castellón` | 27 | accented spelling 724 vs 27 |
| `peliculas` | `película` | 27 | accented spelling 7,715 vs 27 |
| `menus` | `menú` | 27 | accented spelling 1,323 vs 27 |
| `vertigo` | `vértigo` | 27 | accented spelling 503 vs 27 |
| `lider` | `líder` | 27 | accented spelling 22,437 vs 27 |
| `sensacion` | `sensación` | 27 | accented spelling 12,212 vs 27 |
| `bastion` | `bastión` | 27 | accented spelling 382 vs 27 |
| `cacer` | `cácer` | 26 | accented spelling 252 vs 26 |
| `sindrome` | `síndrome` | 26 | accented spelling 4,849 vs 26 |
| `confia` | `confiar` | 26 | accented spelling 845 vs 26 |
| `pense` | `pensar` | 26 | accented spelling 2,274 vs 26 |
| `ibamos` | `ir` | 26 | accented spelling 360 vs 26 |
| `choco` | `chocar` | 26 | accented spelling 171 vs 26 |
| `hamster` | `hámster` | 26 | accented spelling 224 vs 26 |
| `volvera` | `volver` | 26 | accented spelling 1,146 vs 26 |
| `turquia` | `turquía` | 26 | accented spelling 6,080 vs 26 |
| `constitucion` | `constitución` | 26 | accented spelling 5,305 vs 26 |
| `grua` | `grúa` | 26 | accented spelling 2,019 vs 26 |
| `porton` | `portón` | 26 | accented spelling 451 vs 26 |
| `boletin` | `boletín` | 26 | accented spelling 6,281 vs 26 |
| `habria` | `haber` | 26 | accented spelling 3,877 vs 26 |
| `prohiben` | `prohibir` | 26 | accented spelling 251 vs 26 |
| `aerobic` | `aeróbic` | 26 | accented spelling 146 vs 26 |
| `comenzo` | `comenzar` | 26 | accented spelling 7,627 vs 26 |
| `malecon` | `malecón` | 26 | accented spelling 434 vs 26 |
| `conversacion` | `conversación` | 25 | accented spelling 8,350 vs 25 |
| `pacifica` | `pacífico` | 25 | accented spelling 688 vs 25 |
| `intencion` | `intención` | 25 | accented spelling 10,395 vs 25 |
| `beyonce` | `beyoncé` | 25 | accented spelling 138 vs 25 |
| `policiaco` | `policíaco` | 25 | accented spelling 205 vs 25 |
| `accion` | `acción` | 25 | accented spelling 49,602 vs 25 |
| `levanto` | `levantar` | 25 | accented spelling 733 vs 25 |
| `piston` | `pistón` | 25 | accented spelling 1,272 vs 25 |
| `jesus` | `jesús` | 25 | accented spelling 36,744 vs 25 |
| `artistico` | `artístico` | 25 | accented spelling 5,558 vs 25 |
| `comunion` | `comunión` | 25 | accented spelling 3,144 vs 25 |
| `dracula` | `drácula` | 25 | accented spelling 184 vs 25 |
| `decidio` | `decidir` | 25 | accented spelling 2,867 vs 25 |
| `panaderia` | `panadería` | 25 | accented spelling 1,677 vs 25 |
| `sebastien` | `sébastien` | 25 | accented spelling 174 vs 25 |
| `meson` | `mesón` | 25 | accented spelling 270 vs 25 |
| `valoracion` | `valoración` | 25 | accented spelling 7,089 vs 25 |
| `idolo` | `ídolo` | 25 | accented spelling 993 vs 25 |
| `humeda` | `húmedo` | 25 | accented spelling 682 vs 25 |
| `profecia` | `profecía` | 25 | accented spelling 1,672 vs 25 |
| `memorandum` | `memorándum` | 25 | accented spelling 286 vs 25 |
| `conduccion` | `conducción` | 25 | accented spelling 5,537 vs 25 |
| `ibañez` | `ibáñez` | 25 | accented spelling 134 vs 25 |
| `bogota` | `bogotá` | 25 | accented spelling 6,104 vs 25 |
| `aparecera` | `aparecer` | 24 | accented spelling 1,677 vs 24 |
| `estetica` | `estético` | 24 | accented spelling 2,063 vs 24 |
| `lazaro` | `lázaro` | 24 | accented spelling 885 vs 24 |
| `estais` | `estar` | 24 | accented spelling 1,421 vs 24 |
| `libano` | `líbano` | 24 | accented spelling 1,847 vs 24 |
| `iman` | `imán` | 24 | accented spelling 2,094 vs 24 |
| `hercules` | `hércules` | 24 | accented spelling 342 vs 24 |
| `calido` | `cálido` | 24 | accented spelling 6,086 vs 24 |
| `estare` | `estar` | 24 | accented spelling 1,026 vs 24 |
| `nectar` | `néctar` | 24 | accented spelling 302 vs 24 |
| `amenazo` | `amenazar` | 24 | accented spelling 221 vs 24 |
| `supresion` | `supresión` | 24 | accented spelling 1,974 vs 24 |
| `agata` | `ágata` | 24 | accented spelling 210 vs 24 |
| `frigorifico` | `frigorífico` | 24 | accented spelling 2,478 vs 24 |
| `increiblemente` | `increíblemente` | 24 | accented spelling 2,532 vs 24 |
| `incognito` | `incógnito` | 24 | accented spelling 241 vs 24 |
| `podriamos` | `poder` | 24 | accented spelling 2,224 vs 24 |
| `solido` | `sólido` | 24 | accented spelling 8,880 vs 24 |
| `reservacion` | `reservación` | 24 | accented spelling 3,371 vs 24 |
| `acustico` | `acústico` | 24 | accented spelling 2,167 vs 24 |
| `noe` | `noé` | 24 | accented spelling 1,116 vs 24 |
| `lapiz` | `lápiz` | 24 | accented spelling 3,395 vs 24 |
| `poligono` | `polígono` | 24 | accented spelling 593 vs 24 |
| `uzbekistan` | `uzbekistán` | 24 | accented spelling 528 vs 24 |
| `panoramicas` | `panorámico` | 24 | accented spelling 1,450 vs 24 |
| `subterraneo` | `subterráneo` | 24 | accented spelling 2,780 vs 24 |
| `tipico` | `típico` | 24 | accented spelling 7,496 vs 24 |
| `hungria` | `hungría` | 23 | accented spelling 2,467 vs 23 |
| `parecia` | `parecer` | 23 | accented spelling 2,977 vs 23 |
| `confeso` | `confesar` | 23 | accented spelling 245 vs 23 |
| `grabacion` | `grabación` | 23 | accented spelling 7,134 vs 23 |
| `basica` | `básico` | 23 | accented spelling 4,726 vs 23 |
| `vazquez` | `vázquez` | 23 | accented spelling 404 vs 23 |
| `multiples` | `múltiple` | 23 | accented spelling 8,653 vs 23 |
| `acido` | `ácido` | 23 | accented spelling 9,023 vs 23 |
| `recibio` | `recibir` | 23 | accented spelling 4,515 vs 23 |
| `basicas` | `básico` | 23 | accented spelling 3,490 vs 23 |
| `sabiduria` | `sabiduría` | 23 | accented spelling 6,147 vs 23 |
| `foton` | `fotón` | 23 | accented spelling 308 vs 23 |
| `samana` | `samaná` | 23 | accented spelling 218 vs 23 |
| `iberica` | `ibérico` | 23 | accented spelling 263 vs 23 |
| `tenes` | `tener` | 23 | accented spelling 521 vs 23 |
| `historica` | `histórico` | 23 | accented spelling 2,771 vs 23 |
| `publicacion` | `publicación` | 23 | accented spelling 17,342 vs 23 |
| `vitroceramica` | `vitrocerámica` | 23 | accented spelling 704 vs 23 |
| `ramses` | `ramsés` | 23 | accented spelling 142 vs 23 |
| `membresia` | `membresía` | 22 | accented spelling 2,223 vs 22 |
| `lluis` | `lluís` | 22 | accented spelling 206 vs 22 |
| `demoniaco` | `demoníaco` | 22 | accented spelling 220 vs 22 |
| `podreis` | `poder` | 22 | accented spelling 657 vs 22 |
| `escaner` | `escáner` | 22 | accented spelling 2,673 vs 22 |
| `acuatico` | `acuático` | 22 | accented spelling 4,036 vs 22 |
| `carcel` | `cárcel` | 22 | accented spelling 4,091 vs 22 |
| `magico` | `mágico` | 22 | accented spelling 4,995 vs 22 |
| `concentrate` | `concentrar` | 22 | accented spelling 132 vs 22 |
| `autovia` | `autovía` | 22 | accented spelling 535 vs 22 |
| `animacion` | `animación` | 22 | accented spelling 4,681 vs 22 |
| `mediterranea` | `mediterráneo` | 22 | accented spelling 1,637 vs 22 |
| `metalico` | `metálico` | 22 | accented spelling 3,857 vs 22 |
| `loteria` | `lotería` | 22 | accented spelling 2,687 vs 22 |
| `hara` | `hacer` | 22 | accented spelling 6,609 vs 22 |
| `señorio` | `señorío` | 22 | accented spelling 270 vs 22 |
| `piton` | `pitón` | 22 | accented spelling 122 vs 22 |
| `areas` | `área` | 22 | accented spelling 13,735 vs 22 |
| `jonatan` | `jonatán` | 22 | accented spelling 598 vs 22 |
| `noemi` | `noemí` | 22 | accented spelling 304 vs 22 |
| `perimetro` | `perímetro` | 22 | accented spelling 970 vs 22 |
| `rehabilitacion` | `rehabilitación` | 22 | accented spelling 3,436 vs 22 |
| `lei` | `leer` | 22 | accented spelling 549 vs 22 |
| `xenon` | `xenón` | 22 | accented spelling 146 vs 22 |
| `nicaraguense` | `nicaragüense` | 22 | accented spelling 549 vs 22 |
| `actualizacion` | `actualización` | 21 | accented spelling 20,914 vs 21 |
| `velazquez` | `velázquez` | 21 | accented spelling 380 vs 21 |
| `medula` | `médula` | 21 | accented spelling 300 vs 21 |
| `lujan` | `luján` | 21 | accented spelling 136 vs 21 |
| `conclusion` | `conclusión` | 21 | accented spelling 7,485 vs 21 |
| `podran` | `poder` | 21 | accented spelling 9,125 vs 21 |
| `pua` | `púa` | 21 | accented spelling 285 vs 21 |
| `acrilico` | `acrílico` | 21 | accented spelling 2,649 vs 21 |
| `identificacion` | `identificación` | 21 | accented spelling 14,034 vs 21 |
| `metalicas` | `metálico` | 21 | accented spelling 667 vs 21 |
| `valentia` | `valentía` | 21 | accented spelling 1,083 vs 21 |
| `moscu` | `moscú` | 21 | accented spelling 5,800 vs 21 |
| `definicion` | `definición` | 21 | accented spelling 10,955 vs 21 |
| `informatico` | `informático` | 21 | accented spelling 4,100 vs 21 |
| `permitira` | `permitir` | 21 | accented spelling 4,941 vs 21 |
| `adan` | `adán` | 21 | accented spelling 1,874 vs 21 |
| `reflexion` | `reflexión` | 21 | accented spelling 4,693 vs 21 |
| `satanas` | `satanás` | 21 | accented spelling 2,688 vs 21 |
| `leela` | `leer` | 21 | accented spelling 1,172 vs 21 |
| `cercania` | `cercanía` | 21 | accented spelling 1,798 vs 21 |
| `especimen` | `espécimen` | 21 | accented spelling 182 vs 21 |
| `rayon` | `rayón` | 20 | accented spelling 204 vs 20 |
| `alli` | `allí` | 20 | accented spelling 36,351 vs 20 |
| `registrese` | `regístrese` | 20 | accented spelling 2,120 vs 20 |
| `sandia` | `sandía` | 20 | accented spelling 426 vs 20 |
| `comercializacion` | `comercialización` | 20 | accented spelling 4,743 vs 20 |
| `explosion` | `explosión` | 20 | accented spelling 3,390 vs 20 |
| `libero` | `liberar` | 20 | accented spelling 142 vs 20 |
| `operacion` | `operación` | 20 | accented spelling 27,506 vs 20 |
| `cancelacion` | `cancelación` | 20 | accented spelling 6,812 vs 20 |
| `corse` | `corsé` | 20 | accented spelling 205 vs 20 |
| `automaticas` | `automático` | 20 | accented spelling 902 vs 20 |
| `lesion` | `lesión` | 20 | accented spelling 10,057 vs 20 |
| `alhaurin` | `alhaurín` | 20 | accented spelling 118 vs 20 |
| `pave` | `pavé` | 20 | accented spelling 336 vs 20 |
| `planificacion` | `planificación` | 20 | accented spelling 9,122 vs 20 |
| `jeronimo` | `jerónimo` | 20 | accented spelling 304 vs 20 |
| `poliza` | `póliza` | 20 | accented spelling 2,428 vs 20 |
| `decimo` | `décimo` | 20 | accented spelling 1,796 vs 20 |
| `formacion` | `formación` | 20 | accented spelling 28,707 vs 20 |
| `conservacion` | `conservación` | 19 | accented spelling 7,967 vs 19 |
| `maritima` | `marítimo` | 19 | accented spelling 713 vs 19 |
| `obstaculo` | `obstáculo` | 19 | accented spelling 3,796 vs 19 |
| `hebron` | `hebrón` | 19 | accented spelling 462 vs 19 |
| `liquidos` | `líquido` | 19 | accented spelling 2,264 vs 19 |
| `senti` | `sentir` | 19 | accented spelling 904 vs 19 |
| `comoda` | `cómodo` | 19 | accented spelling 5,375 vs 19 |
| `unicas` | `único` | 19 | accented spelling 2,362 vs 19 |
| `rapida` | `rápido` | 19 | accented spelling 14,006 vs 19 |
| `isaias` | `isaías` | 19 | accented spelling 1,562 vs 19 |
| `tribulacion` | `tribulación` | 19 | accented spelling 920 vs 19 |
| `humedo` | `húmedo` | 19 | accented spelling 4,409 vs 19 |
| `mecanico` | `mecánico` | 19 | accented spelling 7,357 vs 19 |
| `vivio` | `vivir` | 19 | accented spelling 1,358 vs 19 |
| `varia` | `variar` | 19 | accented spelling 1,594 vs 19 |
| `notificacion` | `notificación` | 19 | accented spelling 12,734 vs 19 |
| `bartolome` | `bartolomé` | 19 | accented spelling 402 vs 19 |
| `juridico` | `jurídico` | 19 | accented spelling 5,761 vs 19 |
| `jardineria` | `jardinería` | 19 | accented spelling 1,381 vs 19 |
| `satan` | `satán` | 19 | accented spelling 300 vs 19 |
| `atitlan` | `atitlán` | 19 | accented spelling 102 vs 19 |
| `tecnologico` | `tecnológico` | 19 | accented spelling 8,341 vs 19 |
| `cito` | `citar` | 19 | accented spelling 237 vs 19 |
| `comodamente` | `cómodamente` | 19 | accented spelling 2,552 vs 19 |
| `resurreccion` | `resurrección` | 19 | accented spelling 3,066 vs 19 |
| `caserio` | `caserío` | 19 | accented spelling 262 vs 19 |
| `atlantica` | `atlántico` | 19 | accented spelling 256 vs 19 |
| `republica` | `república` | 19 | accented spelling 10,035 vs 19 |
| `util` | `útil` | 19 | accented spelling 23,140 vs 19 |
| `irani` | `iraní` | 19 | accented spelling 1,360 vs 19 |
| `condon` | `condón` | 19 | accented spelling 478 vs 19 |
| `climax` | `clímax` | 19 | accented spelling 256 vs 19 |
| `celebracion` | `celebración` | 19 | accented spelling 7,374 vs 19 |
| `quorum` | `quórum` | 19 | accented spelling 323 vs 19 |
| `melon` | `melón` | 19 | accented spelling 513 vs 19 |
| `paginas` | `página` | 19 | accented spelling 12,137 vs 19 |
| `golan` | `golán` | 19 | accented spelling 108 vs 19 |
| `hectarea` | `hectárea` | 19 | accented spelling 2,013 vs 19 |
| `ventilacion` | `ventilación` | 19 | accented spelling 3,415 vs 19 |
| `estaria` | `estar` | 18 | accented spelling 1,647 vs 18 |
| `imaginacion` | `imaginación` | 18 | accented spelling 3,313 vs 18 |
| `difamacion` | `difamación` | 18 | accented spelling 432 vs 18 |
| `carroceria` | `carrocería` | 18 | accented spelling 2,731 vs 18 |
| `azucar` | `azúcar` | 18 | accented spelling 11,739 vs 18 |
| `simpatia` | `simpatía` | 18 | accented spelling 841 vs 18 |
| `candido` | `cándido` | 18 | accented spelling 91 vs 18 |
| `cancion` | `canción` | 18 | accented spelling 14,723 vs 18 |
| `ciudadania` | `ciudadanía` | 18 | accented spelling 3,753 vs 18 |
| `quereis` | `querer` | 18 | accented spelling 765 vs 18 |
| `categorias` | `categoría` | 18 | accented spelling 8,105 vs 18 |
| `reduccion` | `reducción` | 18 | accented spelling 14,419 vs 18 |
| `simpatica` | `simpático` | 18 | accented spelling 193 vs 18 |
| `infusion` | `infusión` | 18 | accented spelling 1,295 vs 18 |
| `hidraulico` | `hidráulico` | 18 | accented spelling 5,805 vs 18 |
| `seul` | `seúl` | 18 | accented spelling 2,076 vs 18 |
| `estan` | `estar` | 18 | accented spelling 86,888 vs 18 |
| `tunez` | `túnez` | 18 | accented spelling 1,656 vs 18 |
| `matematica` | `matemática` | 18 | accented spelling 1,146 vs 18 |
| `copan` | `copán` | 18 | accented spelling 102 vs 18 |
| `extraido` | `extraer` | 18 | accented spelling 291 vs 18 |
| `sabados` | `sábado` | 18 | accented spelling 970 vs 18 |
| `recaudo` | `recaudar` | 18 | accented spelling 112 vs 18 |
| `volumenes` | `volumen` | 18 | accented spelling 1,395 vs 18 |
| `recreacion` | `recreación` | 18 | accented spelling 1,513 vs 18 |
| `artico` | `ártico` | 18 | accented spelling 886 vs 18 |
| `leccion` | `lección` | 17 | accented spelling 5,808 vs 17 |
| `ubicacion` | `ubicación` | 17 | accented spelling 50,122 vs 17 |
| `bilingue` | `bilingüe` | 17 | accented spelling 1,318 vs 17 |
| `talisman` | `talismán` | 17 | accented spelling 125 vs 17 |
| `psicologia` | `psicología` | 17 | accented spelling 2,977 vs 17 |
| `sofa-cama` | `sofá-cama` | 17 | accented spelling 770 vs 17 |
| `toxico` | `tóxico` | 17 | accented spelling 2,311 vs 17 |
| `benitez` | `benítez` | 17 | accented spelling 168 vs 17 |
| `instruccion` | `instrucción` | 17 | accented spelling 38,070 vs 17 |
| `pidio` | `pedir` | 17 | accented spelling 2,801 vs 17 |
| `dinamico` | `dinámico` | 17 | accented spelling 8,003 vs 17 |
| `niquel` | `níquel` | 17 | accented spelling 1,273 vs 17 |
| `ilustracion` | `ilustración` | 17 | accented spelling 5,971 vs 17 |
| `tecnologias` | `tecnología` | 17 | accented spelling 8,996 vs 17 |
| `fijacion` | `fijación` | 17 | accented spelling 3,753 vs 17 |
| `interpretacion` | `interpretación` | 17 | accented spelling 6,812 vs 17 |
| `energetico` | `energético` | 17 | accented spelling 7,212 vs 17 |
| `rabi` | `rabí` | 17 | accented spelling 263 vs 17 |
| `vereis` | `ver` | 17 | accented spelling 279 vs 17 |
| `llameno` | `llámeno` | 17 | accented spelling 104 vs 17 |
| `apostol` | `apóstol` | 17 | accented spelling 3,455 vs 17 |
| `combine` | `combinar` | 17 | accented spelling 114 vs 17 |
| `autonoma` | `autónomo` | 17 | accented spelling 1,411 vs 17 |
| `liberacion` | `liberación` | 17 | accented spelling 5,938 vs 17 |
| `podian` | `poder` | 17 | accented spelling 2,265 vs 17 |
| `pagina` | `página` | 17 | accented spelling 89,306 vs 17 |
| `adriatico` | `adriático` | 17 | accented spelling 375 vs 17 |
| `sermon` | `sermón` | 17 | accented spelling 746 vs 17 |
| `munchen` | `münchen` | 17 | accented spelling 194 vs 17 |
| `musica` | `música` | 17 | accented spelling 36,840 vs 17 |
| `detras` | `detrás` | 17 | accented spelling 13,324 vs 17 |
| `stephane` | `stéphane` | 17 | accented spelling 110 vs 17 |
| `instantaneamente` | `instantáneamente` | 17 | accented spelling 1,170 vs 17 |
| `mormon` | `mormón` | 17 | accented spelling 713 vs 17 |
| `chamartin` | `chamartín` | 17 | accented spelling 98 vs 17 |
| `balsamo` | `bálsamo` | 17 | accented spelling 505 vs 17 |
| `multilingue` | `multilingüe` | 17 | accented spelling 1,361 vs 17 |
| `parabola` | `parábola` | 17 | accented spelling 1,147 vs 17 |
| `nestle` | `nestlé` | 17 | accented spelling 540 vs 17 |
| `chiita` | `chiíta` | 17 | accented spelling 144 vs 17 |
| `cuestion` | `cuestión` | 17 | accented spelling 18,742 vs 17 |
| `sali` | `salir` | 17 | accented spelling 419 vs 17 |
| `explicacion` | `explicación` | 17 | accented spelling 4,375 vs 17 |
| `confusion` | `confusión` | 17 | accented spelling 2,972 vs 17 |
| `beltran` | `beltrán` | 17 | accented spelling 178 vs 17 |
| `erotico` | `erótico` | 17 | accented spelling 1,187 vs 17 |
| `vendee` | `vendée` | 17 | accented spelling 116 vs 17 |
| `nahuatl` | `náhuatl` | 17 | accented spelling 128 vs 17 |
| `estereo` | `estéreo` | 17 | accented spelling 1,595 vs 17 |
| `optico` | `óptico` | 16 | accented spelling 4,590 vs 16 |
| `ocurrio` | `ocurrir` | 16 | accented spelling 2,117 vs 16 |
| `representacion` | `representación` | 16 | accented spelling 8,212 vs 16 |
| `santanyi` | `santanyí` | 16 | accented spelling 98 vs 16 |
| `higado` | `hígado` | 16 | accented spelling 5,057 vs 16 |
| `certificacion` | `certificación` | 16 | accented spelling 9,618 vs 16 |
| `angelus` | `ángelus` | 16 | accented spelling 96 vs 16 |
| `aerea` | `aéreo` | 16 | accented spelling 1,938 vs 16 |
| `saldra` | `salir` | 16 | accented spelling 779 vs 16 |
| `turisticos` | `turístico` | 16 | accented spelling 2,605 vs 16 |
| `hernan` | `hernán` | 16 | accented spelling 190 vs 16 |
| `espirita` | `espírita` | 16 | accented spelling 308 vs 16 |
| `fisicamente` | `físicamente` | 16 | accented spelling 1,944 vs 16 |
| `hospederia` | `hospedería` | 16 | accented spelling 148 vs 16 |
| `clasica` | `clásico` | 16 | accented spelling 2,296 vs 16 |
| `encontro` | `encontrar` | 16 | accented spelling 3,132 vs 16 |
| `boyaca` | `boyacá` | 16 | accented spelling 136 vs 16 |
| `estadistica` | `estadística` | 16 | accented spelling 7,710 vs 16 |
| `obtendra` | `obtener` | 16 | accented spelling 2,150 vs 16 |
| `importacion` | `importación` | 16 | accented spelling 5,319 vs 16 |
| `millan` | `millán` | 16 | accented spelling 90 vs 16 |
| `sueter` | `suéter` | 16 | accented spelling 846 vs 16 |
| `orgia` | `orgía` | 16 | accented spelling 268 vs 16 |
| `encantaria` | `encantar` | 16 | accented spelling 672 vs 16 |
| `buro` | `buró` | 16 | accented spelling 285 vs 16 |
| `evolucion` | `evolución` | 16 | accented spelling 12,526 vs 16 |
| `magica` | `mágico` | 16 | accented spelling 1,010 vs 16 |
| `tranvia` | `tranvía` | 16 | accented spelling 1,758 vs 16 |
| `mejia` | `mejía` | 16 | accented spelling 213 vs 16 |
| `simpatico` | `simpático` | 16 | accented spelling 1,007 vs 16 |
| `simultaneamente` | `simultáneamente` | 16 | accented spelling 2,684 vs 16 |
| `toracico` | `torácico` | 16 | accented spelling 378 vs 16 |
| `volvio` | `volver` | 16 | accented spelling 2,516 vs 16 |
| `bambu` | `bambú` | 16 | accented spelling 1,617 vs 16 |
| `ecologica` | `ecológico` | 16 | accented spelling 1,306 vs 16 |
| `computacion` | `computación` | 16 | accented spelling 2,133 vs 16 |
| `proteccion` | `protección` | 16 | accented spelling 50,985 vs 16 |
| `iras` | `ir` | 16 | accented spelling 223 vs 16 |
| `inscripcion` | `inscripción` | 16 | accented spelling 7,027 vs 16 |
| `algebra` | `álgebra` | 16 | accented spelling 265 vs 16 |
| `inmigracion` | `inmigración` | 16 | accented spelling 5,347 vs 16 |
| `anfitrion` | `anfitrión` | 15 | accented spelling 5,756 vs 15 |
| `pudin` | `pudín` | 15 | accented spelling 125 vs 15 |
| `verguenza` | `vergüenza` | 15 | accented spelling 2,059 vs 15 |
| `vehiculos` | `vehículo` | 15 | accented spelling 9,481 vs 15 |
| `periodicamente` | `periódicamente` | 15 | accented spelling 4,935 vs 15 |
| `alejandria` | `alejandría` | 15 | accented spelling 760 vs 15 |
| `cotizacion` | `cotización` | 15 | accented spelling 3,967 vs 15 |
| `merito` | `mérito` | 15 | accented spelling 1,340 vs 15 |
| `oregano` | `orégano` | 15 | accented spelling 358 vs 15 |
| `chalten` | `chaltén` | 15 | accented spelling 102 vs 15 |
| `sarten` | `sartén` | 15 | accented spelling 2,062 vs 15 |
| `debil` | `débil` | 15 | accented spelling 4,915 vs 15 |
| `micron` | `micrón` | 15 | accented spelling 116 vs 15 |
| `futon` | `futón` | 15 | accented spelling 318 vs 15 |
| `refrigeracion` | `refrigeración` | 15 | accented spelling 3,826 vs 15 |
| `balon` | `balón` | 15 | accented spelling 2,802 vs 15 |
| `pedi` | `pedir` | 15 | accented spelling 631 vs 15 |
| `avion` | `avión` | 15 | accented spelling 40,774 vs 15 |
| `josue` | `josué` | 15 | accented spelling 1,960 vs 15 |
| `indigenas` | `indígena` | 15 | accented spelling 3,296 vs 15 |
| `caracter` | `carácter` | 15 | accented spelling 20,886 vs 15 |
| `fosforo` | `fósforo` | 15 | accented spelling 1,071 vs 15 |
| `diria` | `decir` | 15 | accented spelling 905 vs 15 |
| `lexicon` | `lexicón` | 15 | accented spelling 102 vs 15 |
| `estrategicamente` | `estratégicamente` | 15 | accented spelling 924 vs 15 |
| `escribio` | `escribir` | 15 | accented spelling 3,654 vs 15 |
| `seccion` | `sección` | 15 | accented spelling 29,661 vs 15 |
| `generico` | `genérico` | 15 | accented spelling 2,625 vs 15 |
| `guie` | `guiar` | 15 | accented spelling 190 vs 15 |
| `parrafo` | `párrafo` | 15 | accented spelling 6,601 vs 15 |
| `sudafrica` | `sudáfrica` | 15 | accented spelling 3,926 vs 15 |
| `inspeccion` | `inspección` | 15 | accented spelling 6,470 vs 15 |
| `infeccion` | `infección` | 15 | accented spelling 13,201 vs 15 |
| `biblico` | `bíblico` | 15 | accented spelling 1,757 vs 15 |
| `referendum` | `referéndum` | 15 | accented spelling 915 vs 15 |
| `rapidos` | `rápido` | 15 | accented spelling 2,047 vs 15 |
| `zoster` | `zóster` | 15 | accented spelling 106 vs 15 |
| `ecologico` | `ecológico` | 15 | accented spelling 5,416 vs 15 |
| `maestria` | `maestría` | 15 | accented spelling 2,756 vs 15 |
| `tucan` | `tucán` | 15 | accented spelling 96 vs 15 |
| `mediodia` | `mediodía` | 15 | accented spelling 2,381 vs 15 |
| `energetica` | `energético` | 15 | accented spelling 2,511 vs 15 |
| `opto` | `optar` | 15 | accented spelling 230 vs 15 |
| `catolico` | `católico` | 15 | accented spelling 4,247 vs 15 |
| `aprendi` | `aprender` | 15 | accented spelling 714 vs 15 |
| `botanico` | `botánico` | 15 | accented spelling 1,625 vs 15 |
| `reaccion` | `reacción` | 15 | accented spelling 8,326 vs 15 |
| `escribi` | `escribir` | 15 | accented spelling 536 vs 15 |
| `aleron` | `alerón` | 15 | accented spelling 159 vs 15 |
| `coccion` | `cocción` | 15 | accented spelling 2,063 vs 15 |
| `velez` | `vélez` | 15 | accented spelling 240 vs 15 |
| `huracan` | `huracán` | 15 | accented spelling 2,257 vs 15 |
| `jamon` | `jamón` | 15 | accented spelling 1,821 vs 15 |
| `centimetro` | `centímetro` | 14 | accented spelling 9,422 vs 14 |
| `timon` | `timón` | 14 | accented spelling 482 vs 14 |
| `quindio` | `quindío` | 14 | accented spelling 90 vs 14 |
| `exhorto` | `exhortar` | 14 | accented spelling 110 vs 14 |
| `entrevisto` | `entrevistar` | 14 | accented spelling 139 vs 14 |
| `rapidas` | `rápido` | 14 | accented spelling 25,437 vs 14 |
| `ire` | `ir` | 14 | accented spelling 659 vs 14 |
| `lenceria` | `lencería` | 14 | accented spelling 569 vs 14 |
| `automovil` | `automóvil` | 14 | accented spelling 9,913 vs 14 |
| `laser` | `láser` | 14 | accented spelling 8,653 vs 14 |
| `medicos` | `médico` | 14 | accented spelling 8,968 vs 14 |
| `organico` | `orgánico` | 14 | accented spelling 6,085 vs 14 |
| `interes` | `interés` | 14 | accented spelling 39,240 vs 14 |
| `modificacion` | `modificación` | 14 | accented spelling 12,150 vs 14 |
| `tendria` | `tener` | 14 | accented spelling 1,989 vs 14 |
| `sentia` | `sentir` | 14 | accented spelling 909 vs 14 |
| `volvi` | `volver` | 14 | accented spelling 451 vs 14 |
| `competicion` | `competición` | 14 | accented spelling 4,681 vs 14 |
| `activacion` | `activación` | 14 | accented spelling 3,573 vs 14 |
| `itza` | `itzá` | 14 | accented spelling 136 vs 14 |
| `reputacion` | `reputación` | 14 | accented spelling 4,897 vs 14 |
| `cesareo` | `cesáreo` | 14 | accented spelling 244 vs 14 |
| `electricos` | `eléctrico` | 14 | accented spelling 3,312 vs 14 |
| `excepcion` | `excepción` | 14 | accented spelling 7,115 vs 14 |
| `nutricion` | `nutrición` | 14 | accented spelling 5,386 vs 14 |
| `olimpica` | `olímpico` | 14 | accented spelling 246 vs 14 |
| `inclusion` | `inclusión` | 14 | accented spelling 5,170 vs 14 |
| `debia` | `deber` | 14 | accented spelling 2,025 vs 14 |
| `deberias` | `deber` | 14 | accented spelling 3,063 vs 14 |
| `atlantida` | `atlántida` | 14 | accented spelling 248 vs 14 |
| `floristeria` | `floristería` | 14 | accented spelling 127 vs 14 |
| `badminton` | `bádminton` | 14 | accented spelling 250 vs 14 |
| `participo` | `participar` | 14 | accented spelling 1,293 vs 14 |
| `torsion` | `torsión` | 14 | accented spelling 823 vs 14 |
| `pulpito` | `púlpito` | 14 | accented spelling 166 vs 14 |
| `sabian` | `saber` | 14 | accented spelling 823 vs 14 |
| `tunel` | `túnel` | 14 | accented spelling 3,240 vs 14 |
| `contemporanea` | `contemporáneo` | 14 | accented spelling 1,266 vs 14 |
| `ampliacion` | `ampliación` | 14 | accented spelling 4,790 vs 14 |
| `averia` | `avería` | 14 | accented spelling 693 vs 14 |
| `freir` | `freír` | 14 | accented spelling 1,183 vs 14 |
| `optimas` | `óptimo` | 14 | accented spelling 1,857 vs 14 |
| `quisieramos` | `querer` | 14 | accented spelling 205 vs 14 |
| `oleo` | `óleo` | 14 | accented spelling 1,717 vs 14 |
| `riñon` | `riñón` | 14 | accented spelling 2,702 vs 14 |
| `compensacion` | `compensación` | 14 | accented spelling 5,556 vs 14 |
| `paramo` | `páramo` | 14 | accented spelling 285 vs 14 |
| `agradecele` | `agradécele` | 14 | accented spelling 72 vs 14 |
| `sepulveda` | `sepúlveda` | 14 | accented spelling 84 vs 14 |
| `efraim` | `efraím` | 14 | accented spelling 136 vs 14 |
| `conto` | `contar` | 14 | accented spelling 1,542 vs 14 |
| `bujia` | `bujía` | 14 | accented spelling 308 vs 14 |
| `miercoles` | `miércoles` | 14 | accented spelling 11,724 vs 14 |
| `fotografico` | `fotográfico` | 14 | accented spelling 2,715 vs 14 |
| `comprension` | `comprensión` | 14 | accented spelling 7,270 vs 14 |
| `demas` | `demás` | 14 | accented spelling 25,816 vs 14 |
| `michoacan` | `michoacán` | 14 | accented spelling 366 vs 14 |
| `angelico` | `angélico` | 14 | accented spelling 368 vs 14 |
| `utilizacion` | `utilización` | 14 | accented spelling 11,710 vs 14 |
| `sere` | `ser` | 14 | accented spelling 812 vs 14 |
| `buho` | `búho` | 14 | accented spelling 491 vs 14 |
| `eurovision` | `eurovisión` | 14 | accented spelling 252 vs 14 |
| `arabe` | `árabe` | 14 | accented spelling 5,518 vs 14 |
| `peñon` | `peñón` | 13 | accented spelling 157 vs 13 |
| `peñiscola` | `peñíscola` | 13 | accented spelling 126 vs 13 |
| `patzcuaro` | `pátzcuaro` | 13 | accented spelling 94 vs 13 |
| `calderon` | `calderón` | 13 | accented spelling 614 vs 13 |
| `oce` | `océ` | 13 | accented spelling 88 vs 13 |
| `aviles` | `avilés` | 13 | accented spelling 266 vs 13 |
| `imagenes` | `imagen` | 13 | accented spelling 26,968 vs 13 |
| `termica` | `térmico` | 13 | accented spelling 1,731 vs 13 |
| `macias` | `macías` | 13 | accented spelling 72 vs 13 |
| `inyeccion` | `inyección` | 13 | accented spelling 7,183 vs 13 |
| `bifida` | `bífido` | 13 | accented spelling 83 vs 13 |
| `crie` | `criar` | 13 | accented spelling 67 vs 13 |
| `triada` | `tríada` | 13 | accented spelling 128 vs 13 |
| `observacion` | `observación` | 13 | accented spelling 6,499 vs 13 |
| `cuadruple` | `cuádruple` | 13 | accented spelling 467 vs 13 |
| `fantasticas` | `fantástico` | 13 | accented spelling 2,163 vs 13 |
| `verificacion` | `verificación` | 13 | accented spelling 6,124 vs 13 |
| `jazmin` | `jazmín` | 13 | accented spelling 286 vs 13 |
| `tapiceria` | `tapicería` | 13 | accented spelling 731 vs 13 |
| `irun` | `irún` | 13 | accented spelling 80 vs 13 |
| `fria` | `frío` | 13 | accented spelling 2,679 vs 13 |
| `gluteo` | `glúteo` | 13 | accented spelling 295 vs 13 |
| `japones` | `japonés` | 13 | accented spelling 7,917 vs 13 |
| `geometria` | `geometría` | 13 | accented spelling 1,836 vs 13 |
| `integramente` | `íntegramente` | 13 | accented spelling 820 vs 13 |
| `adicion` | `adición` | 13 | accented spelling 2,889 vs 13 |
| `aereas` | `aéreo` | 13 | accented spelling 5,664 vs 13 |
| `traves` | `través` | 13 | accented spelling 120,656 vs 13 |
| `meditacion` | `meditación` | 13 | accented spelling 3,793 vs 13 |
| `timida` | `tímido` | 13 | accented spelling 215 vs 13 |
| `estrategica` | `estratégico` | 13 | accented spelling 1,806 vs 13 |
| `civica` | `cívico` | 13 | accented spelling 236 vs 13 |
| `serigrafia` | `serigrafía` | 13 | accented spelling 375 vs 13 |
| `marcho` | `marchar` | 13 | accented spelling 78 vs 13 |
| `debora` | `débora` | 13 | accented spelling 106 vs 13 |
| `mensajeria` | `mensajería` | 13 | accented spelling 2,989 vs 13 |
| `quimicas` | `químico` | 13 | accented spelling 1,414 vs 13 |
| `biografia` | `biografía` | 13 | accented spelling 1,411 vs 13 |
| `velasquez` | `velásquez` | 13 | accented spelling 116 vs 13 |
| `sanson` | `sansón` | 13 | accented spelling 323 vs 13 |
| `conoci` | `conocer` | 13 | accented spelling 864 vs 13 |
| `harmonia` | `harmonía` | 13 | accented spelling 95 vs 13 |
| `supervision` | `supervisión` | 13 | accented spelling 5,730 vs 13 |
| `brigida` | `brígida` | 13 | accented spelling 85 vs 13 |
| `valdes` | `valdés` | 13 | accented spelling 254 vs 13 |
| `porcion` | `porción` | 13 | accented spelling 4,581 vs 13 |
| `tendras` | `tener` | 13 | accented spelling 6,635 vs 13 |
| `mineria` | `minería` | 13 | accented spelling 3,346 vs 13 |
| `vacia` | `vacío` | 13 | accented spelling 1,043 vs 13 |
| `haras` | `hacer` | 13 | accented spelling 832 vs 13 |
| `unica` | `único` | 13 | accented spelling 13,712 vs 13 |
| `utero` | `útero` | 13 | accented spelling 2,059 vs 13 |
| `necesitabamos` | `necesitar` | 13 | accented spelling 406 vs 13 |
| `tuiteo` | `tuiteó` | 13 | accented spelling 210 vs 13 |
| `capacitacion` | `capacitación` | 13 | accented spelling 8,239 vs 13 |
| `formulas` | `fórmula` | 13 | accented spelling 777 vs 13 |
| `serguei` | `serguéi` | 13 | accented spelling 132 vs 13 |
| `protesis` | `prótesis` | 13 | accented spelling 1,244 vs 13 |
| `donacion` | `donación` | 13 | accented spelling 4,071 vs 13 |
| `debi` | `deber` | 13 | accented spelling 149 vs 13 |
| `geminis` | `géminis` | 13 | accented spelling 218 vs 13 |
| `institucion` | `institución` | 13 | accented spelling 12,843 vs 13 |
| `pudieramos` | `poder` | 13 | accented spelling 327 vs 13 |
| `evalua` | `evaluar` | 12 | accented spelling 759 vs 12 |
| `agil` | `ágil` | 12 | accented spelling 1,830 vs 12 |
| `querian` | `querer` | 12 | accented spelling 1,110 vs 12 |
| `clinico` | `clínico` | 12 | accented spelling 5,256 vs 12 |
| `carre` | `carré` | 12 | accented spelling 68 vs 12 |
| `tartan` | `tartán` | 12 | accented spelling 100 vs 12 |
| `rodo` | `rodar` | 12 | accented spelling 92 vs 12 |
| `santamaria` | `santamaría` | 12 | accented spelling 132 vs 12 |
| `remocion` | `remoción` | 12 | accented spelling 689 vs 12 |
| `naci` | `nacer` | 12 | accented spelling 475 vs 12 |
| `chandal` | `chándal` | 12 | accented spelling 159 vs 12 |
| `patron` | `patrón` | 12 | accented spelling 10,336 vs 12 |
| `esparrago` | `espárrago` | 12 | accented spelling 255 vs 12 |
| `suscribase` | `suscríbase` | 12 | accented spelling 1,456 vs 12 |
| `maori` | `maorí` | 12 | accented spelling 122 vs 12 |
| `aji` | `ají` | 12 | accented spelling 226 vs 12 |
| `reclamacion` | `reclamación` | 12 | accented spelling 4,869 vs 12 |
| `telefonico` | `telefónico` | 12 | accented spelling 5,440 vs 12 |
| `pondra` | `poner` | 12 | accented spelling 1,204 vs 12 |
| `camaras` | `cámara` | 12 | accented spelling 4,774 vs 12 |
| `proton` | `protón` | 12 | accented spelling 312 vs 12 |
| `eligio` | `elegir` | 12 | accented spelling 738 vs 12 |
| `narcotico` | `narcótico` | 12 | accented spelling 300 vs 12 |
| `academico` | `académico` | 12 | accented spelling 7,359 vs 12 |
| `graduacion` | `graduación` | 12 | accented spelling 1,709 vs 12 |
| `norteamerica` | `norteamérica` | 12 | accented spelling 1,802 vs 12 |
| `sequia` | `sequía` | 12 | accented spelling 1,503 vs 12 |
| `cooperacion` | `cooperación` | 12 | accented spelling 11,820 vs 12 |
| `epica` | `épico` | 12 | accented spelling 301 vs 12 |
| `aleacion` | `aleación` | 12 | accented spelling 9,473 vs 12 |
| `obligacion` | `obligación` | 12 | accented spelling 10,767 vs 12 |
| `exhibicion` | `exhibición` | 12 | accented spelling 4,403 vs 12 |
| `enseñe` | `enseñar` | 12 | accented spelling 125 vs 12 |
| `bailarin` | `bailarín` | 12 | accented spelling 1,034 vs 12 |
| `ascension` | `ascensión` | 12 | accented spelling 960 vs 12 |
| `aviacion` | `aviación` | 12 | accented spelling 1,929 vs 12 |
| `hacian` | `hacer` | 12 | accented spelling 920 vs 12 |
| `contribucion` | `contribución` | 12 | accented spelling 5,956 vs 12 |
| `septimo` | `séptimo` | 12 | accented spelling 3,446 vs 12 |
| `matias` | `matías` | 12 | accented spelling 324 vs 12 |
| `guell` | `güell` | 12 | accented spelling 320 vs 12 |
| `frejus` | `fréjus` | 12 | accented spelling 64 vs 12 |
| `jurgen` | `jürgen` | 12 | accented spelling 104 vs 12 |
| `cafes` | `café` | 12 | accented spelling 948 vs 12 |
| `cortesia` | `cortesía` | 12 | accented spelling 2,643 vs 12 |
| `geografica` | `geográfico` | 12 | accented spelling 1,438 vs 12 |
| `mandara` | `mandar` | 12 | accented spelling 142 vs 12 |
| `profesion` | `profesión` | 12 | accented spelling 4,011 vs 12 |
| `eucaristia` | `eucaristía` | 12 | accented spelling 1,594 vs 12 |
| `idoneo` | `idóneo` | 12 | accented spelling 1,962 vs 12 |
| `salome` | `salomé` | 12 | accented spelling 174 vs 12 |
| `tendre` | `tener` | 12 | accented spelling 578 vs 12 |
| `financiacion` | `financiación` | 12 | accented spelling 6,220 vs 12 |
| `puntuacion` | `puntuación` | 12 | accented spelling 7,470 vs 12 |
| `recibiran` | `recibir` | 12 | accented spelling 1,244 vs 12 |
| `gabon` | `gabón` | 12 | accented spelling 252 vs 12 |
| `jandia` | `jandía` | 12 | accented spelling 114 vs 12 |
| `guillen` | `guillén` | 12 | accented spelling 74 vs 12 |
| `saenz` | `sáenz` | 12 | accented spelling 98 vs 12 |
| `travesia` | `travesía` | 12 | accented spelling 1,751 vs 12 |
| `galerias` | `galería` | 12 | accented spelling 1,361 vs 12 |
| `afganistan` | `afganistán` | 12 | accented spelling 2,366 vs 12 |
| `pixeles` | `píxel` | 12 | accented spelling 868 vs 12 |
| `reposteria` | `repostería` | 12 | accented spelling 390 vs 12 |
| `continuen` | `continuar` | 12 | accented spelling 264 vs 12 |
| `microfono` | `micrófono` | 12 | accented spelling 3,437 vs 12 |
| `afin` | `afín` | 12 | accented spelling 154 vs 12 |
| `vere` | `ver` | 12 | accented spelling 223 vs 12 |
| `corrosion` | `corrosión` | 12 | accented spelling 2,497 vs 12 |
| `zocalo` | `zócalo` | 12 | accented spelling 829 vs 12 |
| `centroamerica` | `centroamérica` | 11 | accented spelling 1,278 vs 11 |
| `relajate` | `relájate` | 11 | accented spelling 608 vs 11 |
| `suscripcion` | `suscripción` | 11 | accented spelling 10,472 vs 11 |
| `geografia` | `geografía` | 11 | accented spelling 1,886 vs 11 |
| `tarantula` | `tarántula` | 11 | accented spelling 57 vs 11 |
| `caratula` | `carátula` | 11 | accented spelling 149 vs 11 |
| `biologico` | `biológico` | 11 | accented spelling 3,596 vs 11 |
| `destruccion` | `destrucción` | 11 | accented spelling 5,385 vs 11 |
| `ilusion` | `ilusión` | 11 | accented spelling 2,858 vs 11 |
| `abrio` | `abrir` | 11 | accented spelling 2,373 vs 11 |
| `tengais` | `tener` | 11 | accented spelling 341 vs 11 |
| `neumatico` | `neumático` | 11 | accented spelling 7,179 vs 11 |
| `deteccion` | `detección` | 11 | accented spelling 8,539 vs 11 |
| `necesitais` | `necesitar` | 11 | accented spelling 147 vs 11 |
| `torrejon` | `torrejón` | 11 | accented spelling 123 vs 11 |
| `elastico` | `elástico` | 11 | accented spelling 3,628 vs 11 |
| `deberas` | `deber` | 11 | accented spelling 1,366 vs 11 |
| `lejia` | `lejía` | 11 | accented spelling 282 vs 11 |
| `estadisticas` | `estadística` | 11 | accented spelling 5,096 vs 11 |
| `minusvalido` | `minusválido` | 11 | accented spelling 237 vs 11 |
| `perigord` | `périgord` | 11 | accented spelling 82 vs 11 |
| `economicamente` | `económicamente` | 11 | accented spelling 1,360 vs 11 |
| `ordene` | `ordenar` | 11 | accented spelling 83 vs 11 |
| `organica` | `orgánico` | 11 | accented spelling 1,673 vs 11 |
| `atencion` | `atención` | 11 | accented spelling 53,034 vs 11 |
| `ficcion` | `ficción` | 11 | accented spelling 3,340 vs 11 |
| `encontra` | `encontrá` | 11 | accented spelling 114 vs 11 |
| `baston` | `bastón` | 11 | accented spelling 830 vs 11 |
| `documentacion` | `documentación` | 11 | accented spelling 7,983 vs 11 |
| `regimenes` | `régimen` | 11 | accented spelling 668 vs 11 |
| `canale` | `canalé` | 11 | accented spelling 122 vs 11 |
| `ningun` | `ninguno` | 11 | accented spelling 22,796 vs 11 |
| `heroismo` | `heroísmo` | 11 | accented spelling 264 vs 11 |
| `veia` | `ver` | 11 | accented spelling 1,072 vs 11 |
| `terapeutico` | `terapéutico` | 11 | accented spelling 2,096 vs 11 |
| `visualizacion` | `visualización` | 11 | accented spelling 5,974 vs 11 |
| `creyo` | `creer` | 11 | accented spelling 434 vs 11 |
| `sanguineo` | `sanguíneo` | 11 | accented spelling 3,369 vs 11 |
| `eter` | `éter` | 11 | accented spelling 285 vs 11 |
| `trios` | `trío` | 11 | accented spelling 63 vs 11 |
| `parecio` | `parecer` | 11 | accented spelling 1,122 vs 11 |
| `vasquez` | `vásquez` | 11 | accented spelling 200 vs 11 |
| `junin` | `junín` | 11 | accented spelling 122 vs 11 |
| `proyeccion` | `proyección` | 11 | accented spelling 3,984 vs 11 |
| `panoramico` | `panorámico` | 11 | accented spelling 3,084 vs 11 |
| `cortazar` | `cortázar` | 11 | accented spelling 60 vs 11 |
| `factoria` | `factoría` | 11 | accented spelling 249 vs 11 |
| `piñon` | `piñón` | 11 | accented spelling 445 vs 11 |
| `dira` | `decir` | 11 | accented spelling 791 vs 11 |
| `ubeda` | `úbeda` | 11 | accented spelling 122 vs 11 |
| `melodia` | `melodía` | 11 | accented spelling 1,372 vs 11 |
| `composicion` | `composición` | 11 | accented spelling 7,101 vs 11 |
| `integracion` | `integración` | 11 | accented spelling 10,906 vs 11 |
| `antigeno` | `antígeno` | 11 | accented spelling 494 vs 11 |
| `arqueologico` | `arqueológico` | 11 | accented spelling 2,288 vs 11 |
| `huespedes` | `huésped` | 11 | accented spelling 31,931 vs 11 |
| `hayais` | `haber` | 11 | accented spelling 228 vs 11 |
| `piramide` | `pirámide` | 11 | accented spelling 1,431 vs 11 |
| `etnico` | `étnico` | 11 | accented spelling 1,939 vs 11 |
| `imaginate` | `imagínate` | 11 | accented spelling 354 vs 11 |
| `queriamos` | `querer` | 11 | accented spelling 759 vs 11 |
| `farmaceutico` | `farmacéutico` | 11 | accented spelling 3,836 vs 11 |
| `cehegin` | `cehegín` | 11 | accented spelling 78 vs 11 |
| `propulsion` | `propulsión` | 11 | accented spelling 693 vs 11 |
| `griferia` | `grifería` | 11 | accented spelling 450 vs 11 |
| `persecucion` | `persecución` | 11 | accented spelling 2,454 vs 11 |
| `ofrecio` | `ofrecer` | 11 | accented spelling 1,118 vs 11 |

### Dropped by 2+ flags: random sample of 23 of 23 in the window

| rank | lemma | flags |
|---:|---|---|
| 7976 | `muell` | citation: spelling written 2 times as a word, against 648 occurrences; shape: ends in 'll' (cut mid-word?) |
| 10342 | `personalizabl` | citation: spelling written 0 times as a word, against 405 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 11961 | `ofrecerl` | citation: spelling written 0 times as a word, against 313 occurrences; shape: ends in 'rl' (cut mid-word?) |
| 14578 | `dobl` | citation: spelling written 1 times as a word, against 220 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 16021 | `encuentr` | citation: spelling written 0 times as a word, against 185 occurrences; shape: ends in 'tr' (cut mid-word?) |
| 17374 | `brindarl` | citation: spelling written 0 times as a word, against 159 occurrences; shape: ends in 'rl' (cut mid-word?) |
| 17630 | `puzl` | citation: spelling written 0 times as a word, against 155 occurrences; shape: ends in 'zl' (cut mid-word?) |
| 17857 | `descargabl` | citation: spelling written 0 times as a word, against 151 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 19243 | `prorock-perforación` | diversity: in 72 documents, 0.55 of the 132 occurrences' random spread (threshold 0.6); shape: hyphenated |
| 22164 | `enseñarl` | citation: spelling written 0 times as a word, against 102 occurrences; shape: ends in 'rl' (cut mid-word?) |
| 22995 | `proporcionarl` | citation: spelling written 0 times as a word, against 96 occurrences; shape: ends in 'rl' (cut mid-word?) |
| 23693 | `multipl` | citation: spelling written 0 times as a word, against 91 occurrences; shape: ends in 'pl' (cut mid-word?) |
| 23755 | `azafr` | citation: spelling written 0 times as a word, against 90 occurrences; shape: ends in 'fr' (cut mid-word?) |
| 24094 | `increibl` | citation: spelling written 0 times as a word, against 88 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 24117 | `mostrarl` | citation: spelling written 0 times as a word, against 88 occurrences; shape: ends in 'rl' (cut mid-word?) |
| 24805 | `coleccionabl` | citation: spelling written 0 times as a word, against 83 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 24909 | `start-ups` | foreign: wordfreq zipf en 4.4 vs es 3.2; shape: hyphenated |
| 26747 | `al-tec` | diversity: in 38 documents, 0.53 of the 72 occurrences' random spread (threshold 0.6); shape: hyphenated |
| 26895 | `psiquiatr` | citation: spelling written 0 times as a word, against 72 occurrences; shape: ends in 'tr' (cut mid-word?) |
| 27533 | `prevenibl` | citation: spelling written 0 times as a word, against 69 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 28094 | `hijoshijo` | citation: spelling written 0 times as a word, against 66 occurrences; shape: reduplication |
| 28116 | `jugabl` | citation: spelling written 0 times as a word, against 66 occurrences; shape: ends in 'bl' (cut mid-word?) |
| 28188 | `servirl` | citation: spelling written 0 times as a word, against 66 occurrences; shape: ends in 'rl' (cut mid-word?) |

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 3,416 (keep 765, drop 2,651); review merges: 179.
