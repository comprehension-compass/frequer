# Review report: es (full)

- Ranking score: `frequency`; 55,292 candidate lemmas ranked.
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
| `Estados Unidos` | 31,586 | 27,150 | 364 |
| `internacional` | 29,628 | 25,601 | 255 |
| `correo electrónico` | 23,988 | 20,711 | 505 |
| `convertirse` | 22,193 | 20,150 | 1955 |
| `por qué` | 21,701 | 18,212 | 573 |
| `directamente` | 19,755 | 18,142 | 615 |
| `especialmente` | 16,904 | 15,845 | 745 |
| `tratarse` | 16,335 | 15,214 | 2441 |
| `simplemente` | 16,304 | 15,259 | 770 |
| `actualmente` | 15,739 | 14,836 | 801 |
| `asegurarse` | 15,565 | 14,618 | 2300 |
| `realmente` | 14,990 | 13,945 | 843 |
| `página web` | 14,699 | 13,198 | 860 |
| `completamente` | 13,848 | 13,076 | 921 |
| `totalmente` | 13,329 | 12,557 | 948 |
| `sentirse` | 12,219 | 11,380 | 1020 |
| `quedarse` | 11,948 | 10,933 | 1172 |
| `fácilmente` | 11,559 | 11,022 | 1087 |
| `rápidamente` | 11,457 | 10,940 | 1088 |
| `solamente` | 11,186 | 10,639 | 1126 |
| `Nueva York` | 10,712 | 9,713 | 1163 |
| `ponerse` | 10,545 | 9,933 | 1211 |
| `aproximadamente` | 10,074 | 9,441 | 1207 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `poder + infinitivo` | 601,163 | 135,314 | 20 |
| `haber + participio` | 428,311 | 129,106 | 27 |
| `se + verbo (impersonal/pasiva)` | 389,826 | 126,727 | 30 |
| `ser + participio` | 235,927 | 109,455 | 37 |
| `estar + gerundio` | 147,052 | 88,316 | 57 |
| `lo + adjetivo` | 62,070 | 48,109 | 163 |
| `al + infinitivo` | 61,539 | 48,486 | 156 |
| `tener que + infinitivo` | 52,037 | 41,858 | 193 |
| `ir a + infinitivo` | 40,403 | 31,675 | 266 |
| `más/menos … que` | 34,497 | 29,532 | 338 |
| `seguir + gerundio` | 22,054 | 19,948 | 558 |
| `volver a + infinitivo` | 13,984 | 12,888 | 909 |
| `comenzar a + infinitivo` | 12,993 | 12,191 | 974 |
| `empezar a + infinitivo` | 12,218 | 11,339 | 1034 |
| `tan … como` | 10,157 | 9,493 | 1248 |
| `dejar de + infinitivo` | 10,025 | 9,340 | 1220 |
| `soler + infinitivo` | 9,984 | 9,411 | 1223 |
| `hace + tiempo` | 9,235 | 8,758 | 1307 |
| `acabar de + infinitivo` | 6,299 | 5,481 | 1816 |
| `desde hace + tiempo` | 4,432 | 4,335 | 2390 |
| `tan … que` | 4,137 | 4,008 | 2496 |
| `qué + adjetivo/sustantivo` | 3,891 | 3,564 | 2612 |
| `hace + tiempo + que` | 3,146 | 3,019 | 3000 |
| `hacer que + subjuntivo` | 1,195 | 1,188 | 5291 |
| `menos … que` | 662 | 643 | 7294 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `a través de` | 59,644 | 46,869 | 162 |
| `después de` | 56,703 | 45,496 | 172 |
| `para que` | 54,272 | 43,859 | 182 |
| `cerca de` | 41,538 | 34,672 | 260 |
| `antes de` | 39,627 | 33,863 | 273 |
| `así como` | 39,070 | 33,633 | 281 |
| `acerca de` | 38,745 | 32,397 | 283 |
| `sin embargo` | 37,024 | 32,245 | 302 |
| `dentro de` | 31,163 | 27,155 | 373 |
| `por ejemplo` | 28,950 | 25,697 | 417 |
| `ya que` | 27,190 | 24,494 | 447 |
| `por favor` | 22,188 | 19,545 | 546 |
| `gracias a` | 21,895 | 20,055 | 559 |
| `en línea` | 21,418 | 19,462 | 572 |
| `por lo que` | 19,686 | 18,256 | 617 |
| `disfrutar de algo` | 19,565 | 18,050 | 619 |
| `además de` | 18,838 | 17,479 | 645 |
| `contar con algo` | 18,672 | 17,317 | 655 |
| `así que` | 18,491 | 17,231 | 667 |
| `debido a` | 18,042 | 16,692 | 691 |
| `a partir de` | 17,697 | 16,365 | 707 |
| `a continuación` | 17,637 | 16,445 | 711 |
| `convertirse en algo` | 17,624 | 16,334 | 714 |
| `alrededor de` | 16,331 | 15,105 | 768 |
| `fuera de` | 15,695 | 14,562 | 805 |

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

Live list 20,000 lemmas, this build 55,292; 12,919 shared. Spearman rank correlation on the shared lemmas 0.942; median rank ratio 1.14x.
Overlap of this build's top-k with the live top-k: top 1,000 87.4%, top 5,000 83.3%, top 20,000 63.9%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 929 | -17,526 |
| `diecinueve` | 18282 | 1353 | -16,929 |
| `dividirse` | 19076 | 3763 | -15,313 |
| `descanso` | 17625 | 2512 | -15,113 |
| `torno` | 17613 | 2636 | -14,977 |
| `respaldo` | 18269 | 3416 | -14,853 |
| `seiscientos` | 17737 | 3235 | -14,502 |
| `coco` | 18793 | 4336 | -14,457 |
| `secadora` | 19190 | 4947 | -14,243 |
| `parto` | 17982 | 3971 | -14,011 |
| `diecisiete` | 14631 | 1180 | -13,451 |
| `entregarse` | 17153 | 3977 | -13,176 |
| `conforme` | 15056 | 1933 | -13,123 |
| `quinientos` | 14749 | 1817 | -12,932 |
| `cuatrocientos` | 15401 | 2505 | -12,896 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `brusela` | 2422 | 47113 | +44,691 |
| `véase` | 3437 | 43056 | +39,619 |
| `dallar` | 3511 | 38526 | +35,015 |
| `capar` | 4795 | 36272 | +31,477 |
| `pa` | 3676 | 31052 | +27,376 |
| `marrueco` | 3509 | 29331 | +25,822 |
| `sopar` | 4650 | 30215 | +25,565 |
| `ucranio` | 3401 | 27729 | +24,328 |
| `hondura` | 3735 | 25769 | +22,034 |
| `resinar` | 4093 | 25864 | +21,771 |
| `orlar` | 2655 | 24169 | +21,514 |
| `radio` | 1086 | 20412 | +19,326 |
| `malasio` | 4644 | 23724 | +19,080 |
| `vacación` | 390 | 18888 | +18,498 |
| `habano` | 3196 | 19783 | +16,587 |

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
| `al + infinitivo` | - | 156 | - |
| `a través de` | - | 162 | - |
| `lo + adjetivo` | - | 163 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `del` | 11 | - | - |
| `al` | 22 | - | - |
| `parte` | 59 | 12112 | +12,053 |
| `e` | 94 | - | - |
| `vario` | 265 | 12411 | +12,146 |
| `tripadvisor` | 384 | - | - |
| `relacionado` | 386 | - | - |
| `vacación` | 390 | 18888 | +18,498 |
| `jetcost` | 494 | - | - |
| `x` | 518 | - | - |
| `the` | 531 | - | - |
| `low` | 550 | - | - |
| `cost` | 560 | - | - |
| `cookies` | 565 | - | - |
| `google` | 576 | - | - |

## Ported frequer checks

### Form-ratio outliers (249)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 8,815,852 | median form 60.5; `de` 7,602,335 (125658x), `del` 1,116,771 (18459x), `De` 66,891 (1106x) |
| 6 | `a` | 2,433,526 | median form 138.5; `a` 1,886,118 (13618x), `al` 436,540 (3152x) |
| 7 | `que` | 2,116,286 | median form 3; `que` 2,106,677 (702226x), `Que` 7,713 (2571x) |
| 8 | `los` | 1,751,679 | median form 1497.5; `los` 1,550,152 (1035x) |
| 9 | `ser` | 1,522,295 | median form 29.5; `es` 660,826 (22401x), `son` 168,181 (5701x), `ser` 137,795 (4671x), `fue` 86,731 (2940x) |
| 10 | `para` | 1,330,434 | median form 3; `para` 1,220,944 (406981x), `Para` 105,507 (35169x) |
| 11 | `con` | 1,137,396 | median form 13; `con` 1,089,681 (83822x), `Con` 45,616 (3509x) |
| 14 | `una` | 906,112 | median form 8.5; `una` 858,166 (100961x), `Una` 46,471 (5467x) |
| 16 | `por` | 794,052 | median form 2; `por` 719,515 (359758x), `Por` 72,313 (36156x) |
| 19 | `poder` | 640,215 | median form 23; `puede` 205,830 (8949x), `pueden` 98,692 (4291x), `puedes` 43,597 (1896x), `poder` 32,536 (1415x) |
| 21 | `haber` | 590,090 | median form 16; `ha` 167,848 (10490x), `han` 77,086 (4818x), `hay` 74,545 (4659x), `había` 38,085 (2380x) |
| 23 | `estar` | 552,105 | median form 34.5; `está` 193,439 (5607x), `están` 84,176 (2440x), `estar` 40,407 (1171x) |
| 24 | `más` | 551,722 | median form 6; `más` 507,421 (84570x), `Más` 27,483 (4580x), `mas` 12,845 (2141x) |
| 28 | `tener` | 422,949 | median form 15; `tiene` 117,588 (7839x), `tienen` 49,087 (3272x), `tener` 48,512 (3234x), `tienes` 20,307 (1354x) |
| 29 | `como` | 405,856 | median form 79; `como` 377,987 (4785x) |
| 31 | `lo` | 356,641 | median form 4; `lo` 331,400 (82850x), `Lo` 24,685 (6171x) |
| 32 | `hacer` | 351,326 | median form 8; `hacer` 108,209 (13526x), `hace` 49,304 (6163x), `hecho` 20,223 (2528x), `haciendo` 15,260 (1908x) |
| 38 | `sobre` | 215,779 | median form 42; `sobre` 210,352 (5008x) |
| 40 | `también` | 173,283 | median form 9.5; `también` 135,717 (14286x), `También` 37,396 (3936x) |
| 41 | `desde` | 167,334 | median form 115.5; `desde` 146,096 (1265x) |
| 42 | `encontrar` | 163,760 | median form 6; `encontrar` 63,105 (10518x), `Encuentra` 33,038 (5506x), `encontrarás` 10,693 (1782x), `encontrado` 7,270 (1212x) |
| 45 | `año` | 162,369 | median form 86; `años` 95,103 (1106x) |
| 46 | `pero` | 159,415 | median form 1.5; `pero` 121,964 (81309x), `Pero` 37,278 (24852x) |
| 52 | `ver` | 151,210 | median form 10; `ver` 54,771 (5477x), `Ver` 21,271 (2127x), `visto` 10,272 (1027x) |
| 54 | `información` | 150,867 | median form 56.5; `información` 131,179 (2322x) |

_224 more not shown._

### Singular/plural mismatch (54)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `los` | 1,751,679 | `lo` lemmatises to `lo` (rank 31) |
| 13 | `las` | 1,064,165 | `la` lemmatises to `la` (rank 2) |
| 135 | `nos` | 65,412 | `no` lemmatises to `no` (rank 17) |
| 144 | `antes` | 62,958 | `ante` lemmatises to `ante` (rank 737) |
| 161 | `dios` | 60,077 | `dio` lemmatises to `dar` (rank 70) |
| 201 | `ellos` | 50,547 | `ello` lemmatises to `ello` (rank 683) |
| 212 | `unos` | 48,531 | `uno` lemmatises to `uno` (rank 53) |
| 256 | `varios` | 42,303 | `vario` lemmatises to `vario` (rank 12,411) |
| 258 | `les` | 41,762 | `le` lemmatises to `le` (rank 58) |
| 270 | `mes` | 39,946 | `me` lemmatises to `me` (rank 94) |
| 337 | `entonces` | 33,876 | `entonce` lemmatises to `entonce` (rank 41,276) |
| 362 | `gracias` | 31,841 | `gracia` lemmatises to `gracia` (rank 2,882) |
| 789 | `ambos` | 15,963 | `ambo` lemmatises to `ambo` (rank 34,328) |
| 1006 | `ellas` | 12,558 | `ella` lemmatises to `ella` (rank 230) |
| 1164 | `parís` | 10,667 | `parí` lemmatises to `parir` (rank 11,934) |
| 1865 | `alrededores` | 6,092 | `alrededor` lemmatises to `alrededor` (rank 620) |
| 1979 | `martes` | 5,662 | `marte` lemmatises to `mar` (rank 526) |
| 2159 | `quizás` | 5,097 | `quizá` lemmatises to `quizá` (rank 3,043) |
| 2196 | `apenas` | 4,983 | `apena` lemmatises to `apenar` (rank 17,830) |
| 2585 | `microondas` | 3,929 | `microonda` lemmatises to `microonda` (rank 17,210) |
| 2888 | `rines` | 3,339 | `rin` lemmatises to `rin` (rank 12,267) |
| 3034 | `bruselas` | 3,089 | `brusela` lemmatises to `brusela` (rank 47,113) |
| 3135 | `gafas` | 2,917 | `gafa` lemmatises to `gafa` (rank 19,662) |
| 3611 | `nervios` | 2,295 | `nervio` lemmatises to `nervio` (rank 7,295) |
| 3756 | `lavavajillas` | 2,163 | `lavavajilla` lemmatises to `lavavajilla` (rank 26,764) |

_29 more not shown._

### Lemma consistency (234)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 99 | `te` | 86,136 | alone, `te` lemmatises to `se` (rank 18) |
| 353 | `lista` | 32,340 | alone, `lista` lemmatises to `listo` (rank 1,128) |
| 392 | `política` | 30,056 | alone, `política` lemmatises to `político` (rank 710) |
| 522 | `dicho` | 23,134 | alone, `dicho` lemmatises to `decir` (rank 60) |
| 531 | `hecho` | 22,666 | alone, `hecho` lemmatises to `hacer` (rank 32) |
| 574 | `china` | 21,397 | alone, `china` lemmatises to `chino` (rank 1,643) |
| 601 | `presente` | 19,976 | alone, `presente` lemmatises to `presentar` (rank 290) |
| 606 | `fuera` | 19,907 | alone, `fuera` lemmatises to `ser` (rank 9) |
| 607 | `abierto` | 19,893 | alone, `abierto` lemmatises to `abrir` (rank 328) |
| 642 | `ayuda` | 18,893 | alone, `ayuda` lemmatises to `ayudar` (rank 91) |
| 729 | `compra` | 17,255 | alone, `compra` lemmatises to `comprar` (rank 227) |
| 761 | `visita` | 16,592 | alone, `visita` lemmatises to `visitar` (rank 375) |
| 808 | `corto` | 15,679 | alone, `corto` lemmatises to `cortar` (rank 1,419) |
| 822 | `causa` | 15,371 | alone, `causa` lemmatises to `causar` (rank 694) |
| 841 | `carga` | 14,995 | alone, `carga` lemmatises to `cargar` (rank 1,367) |
| 883 | `pedido` | 14,360 | alone, `pedido` lemmatises to `pedir` (rank 507) |
| 885 | `os` | 14,294 | alone, `os` lemmatises to `se` (rank 18) |
| 1024 | `vivo` | 12,385 | alone, `vivo` lemmatises to `vivir` (rank 299) |
| 1091 | `deseo` | 11,540 | alone, `deseo` lemmatises to `desear` (rank 307) |
| 1108 | `empleado` | 11,380 | alone, `empleado` lemmatises to `emplear` (rank 1,663) |
| 1146 | `falta` | 10,951 | alone, `falta` lemmatises to `faltar` (rank 2,108) |
| 1164 | `parís` | 10,667 | alone, `parís` lemmatises to `parir` (rank 11,934) |
| 1169 | `avanzado` | 10,605 | alone, `avanzado` lemmatises to `avanzar` (rank 1,993) |
| 1192 | `aumento` | 10,271 | alone, `aumento` lemmatises to `aumentar` (rank 419) |
| 1215 | `vino` | 10,044 | alone, `vino` lemmatises to `venir` (rank 268) |

_209 more not shown._

### Short lemmas (57)

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
| 75 | `ir` | 111,978 | `fuese` -> `ir`, `iba` -> `ir`, `ir` -> `ir`, `vaya` -> `ir`, `va` -> `ir` |
| 88 | `ya` | 95,657 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya`, `-ya` -> `?` |
| 94 | `me` | 89,677 | `me` -> `me`, `Me` -> `me`, `ME` -> `me` |
| 99 | `te` | 86,136 | `te` -> `se`, `Te` -> `te`, `TE` -> `te`, `tes` -> `te` |
| 117 | `él` | 73,977 | `él` -> `él`, `Él` -> `él`, `ÉL` -> `él`, `Èl` -> `él`, `-él` -> `?` |
| 207 | `yo` | 49,631 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo`, `yas` -> `yas`, `yos` -> `yo` |
| 239 | `ni` | 44,387 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni`, `niٌos` -> `?`, `nilos` -> `nilo` |
| 368 | `sí` | 31,593 | `sí` -> `sí`, `si` -> `si`, `Sí` -> `sí`, `SÍ` -> `sí`, `SíEs` -> `sí` |
| 510 | `ti` | 23,739 | `ti` -> `ti`, `TI` -> `ti`, `Ti` -> `ti`, `Tí` -> `ti`, `TÍ` -> `ti` |

_32 more not shown._

### Case merges (1)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4711 | `editorial#Fem` | 1,481 | capitalised but mostly ADJ; no lowercase twin |

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 686 (68.6%).

Ours only: `poder + infinitivo`, `haber + participio`, `se + verbo (impersonal/pasiva)`, `ser + participio`, `vuelo`, `hotel`, `estar + gerundio`, `te`, `archivo`, `habitación`, `barato`, `al + infinitivo`, `a través de`, `lo + adjetivo`, `encontrarse`, `después de`, `para que`, `tener que + infinitivo`, `diseño`, `alojamiento`, `disponible`, `sitio web`, `oferta`, `proporcionar`, `alquiler`

wordfreq only: `nadie`, `mal`, `dr`, `ahí`, `argentino`, `cero`, `listo`, `faltar`, `unido`, `mierda`, `the`, `i`, `c`, `viejo`, `policía`, `elección`, `juan`, `orden#Masc`, `peor`, `voz`, `hola`, `paz`, `militar`, `cargo`, `matar`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 530 | `cookie` | 22,682 | wordfreq zipf en 4.1 vs es 3.0 |
| 815 | `metro#metre` | 15,508 | wordfreq zipf en 3.6 vs es 1.6 |
| 893 | `once` | 14,227 | wordfreq zipf en 5.5 vs es 4.4 |
| 1524 | `led` | 7,685 | wordfreq zipf en 5.1 vs es 3.7 |
| 1887 | `resort` | 5,992 | wordfreq zipf en 4.4 vs es 3.3 |
| 2098 | `show` | 5,305 | wordfreq zipf en 5.7 vs es 4.6 |
| 2606 | `top` | 3,882 | wordfreq zipf en 5.6 vs es 4.4 |
| 2770 | `look` | 3,581 | wordfreq zipf en 5.8 vs es 3.9 |
| 2914 | `stock` | 3,300 | wordfreq zipf en 4.9 vs es 3.8 |
| 2918 | `set` | 3,296 | wordfreq zipf en 5.6 vs es 4.1 |
| 3403 | `parking` | 2,538 | wordfreq zipf en 4.5 vs es 3.1 |
| 3543 | `ticket` | 2,380 | wordfreq zipf en 4.6 vs es 3.5 |
| 3584 | `as` | 2,328 | wordfreq zipf en 6.8 vs es 4.7 |
| 3805 | `feed` | 2,124 | wordfreq zipf en 4.7 vs es 3.3 |
| 4021 | `test` | 1,932 | wordfreq zipf en 5.2 vs es 4.2 |
| 4276 | `bit` | 1,751 | wordfreq zipf en 5.4 vs es 3.2 |
| 4714 | `real#royal` | 1,481 | wordfreq zipf en 4.8 vs es 3.7 |
| 4862 | `film` | 1,390 | wordfreq zipf en 5.2 vs es 4.1 |
| 5028 | `stand` | 1,319 | wordfreq zipf en 5.1 vs es 3.8 |
| 5067 | `metro#railway` | 1,299 | wordfreq zipf en 4.0 vs es 2.6 |
| 5574 | `box` | 1,080 | wordfreq zipf en 5.0 vs es 3.8 |
| 5602 | `country` | 1,068 | wordfreq zipf en 5.5 vs es 3.8 |
| 5733 | `trading` | 1,026 | wordfreq zipf en 4.6 vs es 3.2 |
| 5873 | `script` | 981 | wordfreq zipf en 4.4 vs es 3.3 |
| 6079 | `check-in` | 919 | wordfreq zipf en 5.3 vs es 3.7 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 161 | `dios` | 60,077 | PROPN 0%, capitalised forms 94% |
| 364 | `estados unidos` | 31,775 | PROPN 1%, capitalised forms 100% |
| 439 | `españa` | 27,603 | PROPN 100%, capitalised forms 100% |
| 498 | `san` | 24,279 | PROPN 2%, capitalised forms 96% |
| 574 | `china` | 21,397 | PROPN 100%, capitalised forms 100% |
| 699 | `méxico` | 17,814 | PROPN 100%, capitalised forms 100% |
| 716 | `europa` | 17,568 | PROPN 99%, capitalised forms 100% |
| 723 | `tv` | 17,470 | PROPN 6%, capitalised forms 97% |
| 849 | `barcelona` | 14,829 | PROPN 100%, capitalised forms 100% |
| 865 | `madrid` | 14,651 | PROPN 99%, capitalised forms 99% |
| 1003 | `israel` | 12,587 | PROPN 100%, capitalised forms 100% |
| 1163 | `nueva york` | 10,712 | PROPN 100%, capitalised forms 100% |
| 1164 | `parís` | 10,667 | PROPN 99%, capitalised forms 100% |
| 1190 | `francia` | 10,294 | PROPN 100%, capitalised forms 100% |
| 1247 | `londres` | 9,748 | PROPN 100%, capitalised forms 100% |
| 1339 | `wi-fi` | 9,008 | PROPN 1%, capitalised forms 97% |
| 1358 | `alemania` | 8,805 | PROPN 100%, capitalised forms 100% |
| 1403 | `américa` | 8,458 | PROPN 99%, capitalised forms 99% |
| 1411 | `italia` | 8,419 | PROPN 100%, capitalised forms 100% |
| 1417 | `colombia` | 8,364 | PROPN 100%, capitalised forms 99% |
| 1486 | `pc` | 7,912 | PROPN 11%, capitalised forms 98% |
| 1500 | `roma` | 7,810 | PROPN 99%, capitalised forms 100% |
| 1573 | `chile` | 7,418 | PROPN 93%, capitalised forms 94% |
| 1588 | `reino unido` | 7,337 | PROPN 0%, capitalised forms 100% |
| 1603 | `canadá` | 7,278 | PROPN 100%, capitalised forms 100% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 99.1% | 0.998 |
| juilland_u | 99.9% | 1.000 |
| juilland_u_corrected | 100.0% | 1.000 |
| dp_adjusted | 99.8% | 1.000 |
| cd_blend | 99.6% | 0.999 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `imprescindible` | 4388 | 4233 | -155 | 1,816 | 1,803 | 0.974 | 0.105 |
| `originalmente` | 4398 | 4247 | -151 | 1,809 | 1,793 | 0.978 | 0.094 |
| `si bien` | 5057 | 4907 | -150 | 1,442 | 1,435 | 0.976 | 0.095 |
| `en efecto` | 5013 | 4863 | -150 | 1,465 | 1,456 | 0.975 | 0.100 |
| `diariamente` | 4393 | 4244 | -149 | 1,813 | 1,795 | 0.974 | 0.106 |
| `tomás` | 3890 | 6352 | +2,462 | 2,183 | 930 | 0.933 | 0.260 |
| `love` | 3118 | 5058 | +1,940 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4511 | 6175 | +1,664 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4991 | 6370 | +1,379 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4238 | 5589 | +1,351 | 1,912 | 1,158 | 0.967 | 0.136 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `subrayar` | 4769 | 4747 | -22 | 1,584 | 1,570 | 0.978 | 0.085 |
| `basarse` | 4903 | 4881 | -22 | 1,519 | 1,505 | 0.977 | 0.091 |
| `procurar` | 4308 | 4289 | -19 | 1,867 | 1,844 | 0.981 | 0.070 |
| `a cargo de` | 4366 | 4348 | -18 | 1,828 | 1,808 | 0.979 | 0.082 |
| `consistente` | 4891 | 4874 | -17 | 1,522 | 1,500 | 0.978 | 0.088 |
| `tomás` | 3890 | 4019 | +129 | 2,183 | 930 | 0.933 | 0.260 |
| `atreverse` | 4570 | 4608 | +38 | 1,696 | 1,592 | 0.964 | 0.115 |
| `canadiense` | 4302 | 4339 | +37 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1312 | 1347 | +35 | 9,271 | 3,893 | 0.966 | 0.131 |
| `ascendente` | 4511 | 4543 | +32 | 1,733 | 975 | 0.962 | 0.160 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `incentivo` | 4900 | 4888 | -12 | 1,521 | 1,469 | 0.974 | 0.105 |
| `inmobiliario` | 2769 | 2758 | -11 | 3,707 | 3,326 | 0.985 | 0.058 |
| `silver` | 4365 | 4354 | -11 | 1,829 | 1,786 | 0.978 | 0.089 |
| `doctrina` | 4364 | 4353 | -11 | 1,829 | 1,727 | 0.979 | 0.082 |
| `pelear` | 4896 | 4886 | -10 | 1,522 | 1,449 | 0.975 | 0.105 |
| `tomás` | 3890 | 4019 | +129 | 2,183 | 930 | 0.933 | 0.260 |
| `atreverse` | 4570 | 4606 | +36 | 1,696 | 1,592 | 0.964 | 0.115 |
| `canadiense` | 4302 | 4337 | +35 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1312 | 1347 | +35 | 9,271 | 3,893 | 0.966 | 0.131 |
| `ascendente` | 4511 | 4543 | +32 | 1,733 | 975 | 0.962 | 0.160 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `procurar` | 4308 | 4217 | -91 | 1,867 | 1,844 | 0.981 | 0.070 |
| `desafiar` | 5021 | 4944 | -77 | 1,462 | 1,438 | 0.978 | 0.086 |
| `básicamente` | 4317 | 4243 | -74 | 1,857 | 1,833 | 0.982 | 0.072 |
| `consistente` | 4891 | 4821 | -70 | 1,522 | 1,500 | 0.978 | 0.088 |
| `mensajero` | 4913 | 4843 | -70 | 1,514 | 1,449 | 0.977 | 0.089 |
| `tomás` | 3890 | 4416 | +526 | 2,183 | 930 | 0.933 | 0.260 |
| `ascendente` | 4511 | 4695 | +184 | 1,733 | 975 | 0.962 | 0.160 |
| `love` | 3118 | 3253 | +135 | 3,093 | 1,365 | 0.966 | 0.140 |
| `model` | 4991 | 5114 | +123 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4238 | 4354 | +116 | 1,912 | 1,158 | 0.967 | 0.136 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `exquisito` | 4628 | 4543 | -85 | 1,668 | 1,655 | 0.973 | 0.109 |
| `caracterizarse por algo` | 4639 | 4555 | -84 | 1,661 | 1,647 | 0.976 | 0.096 |
| `transcurso` | 4629 | 4545 | -84 | 1,668 | 1,654 | 0.977 | 0.094 |
| `comprensible` | 4941 | 4857 | -84 | 1,500 | 1,493 | 0.974 | 0.108 |
| `rapidez` | 4305 | 4222 | -83 | 1,868 | 1,852 | 0.976 | 0.091 |
| `tomás` | 3890 | 5012 | +1,122 | 2,183 | 930 | 0.933 | 0.260 |
| `love` | 3118 | 3981 | +863 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4511 | 5301 | +790 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4991 | 5652 | +661 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4238 | 4883 | +645 | 1,912 | 1,158 | 0.967 | 0.136 |

## Excluded lemmas

`es.tsv` (sha256 `d65cd2427cf419f2`) lists 1,404 exclusions; 825 lemmas were dropped from the top 30,000 before cutting it (exclude-abbreviation 37, exclude-boilerplate 34, exclude-english 675, exclude-foreign 16, exclude-fragment 11, exclude-letter 25, exclude-numeral 27). Lower ranks moved up.

| rank before | lemma | class | reason |
|---|---|---|---|
| 479 | `jetcost` | exclude-boilerplate | flight-search site brand |
| 541 | `low` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 554 | `cost` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 578 | `aereo` | exclude-boilerplate | unaccented template spelling of aéreo |
| 755 | `the` | exclude-english | English article |
| 1038 | `x` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1187 | `á` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1227 | `of` | exclude-english | English preposition |
| 1309 | `city` | exclude-english | English word in names |
| 1361 | `b` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1453 | `c` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1479 | `in` | exclude-english | English preposition |
| 1484 | `i` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1644 | `and` | exclude-english | English conjunction |
| 1800 | `beach` | exclude-english | not a Spanish loan |
| 1811 | `d` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1849 | `ii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 1953 | `m` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1966 | `new` | exclude-english | English template text |
| 2129 | `home` | exclude-english | English template text |
| 2235 | `t` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2396 | `g` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2449 | `to` | exclude-english | English preposition |
| 2557 | `house` | exclude-english | English template text |
| 2594 | `v` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2625 | `hp` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 2700 | `by` | exclude-english | English preposition |
| 2711 | `k` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2820 | `black` | exclude-english | English colour word |
| 2838 | `n` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2841 | `e` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2893 | `r` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2913 | `grand` | exclude-english | English in brand names |
| 2922 | `airport` | exclude-english | English for aeropuerto |
| 3038 | `island` | exclude-english | English place word |
| 3051 | `f` | exclude-letter | developer 2026-11-01: single letters excluded |
| 3065 | `on` | exclude-english | English preposition |
| 3110 | `international` | exclude-english | English for internacional |
| 3118 | `love` | exclude-english | English word |
| 3135 | `iii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 3151 | `for` | exclude-english | English preposition |
| 3169 | `air` | exclude-english | English in brand names |
| 3171 | `best` | exclude-english | English word |
| 3187 | `west` | exclude-english | English place word |
| 3193 | `ltd` | exclude-boilerplate | company-name template suffix |
| 3197 | `lg` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 3293 | `di` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3295 | `world` | exclude-english | English word |
| 3302 | `group` | exclude-english | English word in names |
| 3354 | `mb` | exclude-abbreviation | abbreviation or unit symbol (developer 2026-11-01: abbreviations excluded for now) |
| 3479 | `english` | exclude-english | English word |
| 3521 | `car` | exclude-english | English word |
| 3545 | `do` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3556 | `one` | exclude-english | English word |
| 3659 | `white` | exclude-english | English colour word |
| 3668 | `mainland` | exclude-english | English listing text |
| 3683 | `us` | exclude-english | English pronoun/domain |
| 3693 | `am` | exclude-english | English time suffix |
| 3717 | `file` | exclude-english | English for archivo |
| 3751 | `business` | exclude-english | English word |

_765 more in the exclusion file._


## Junk-filter heuristics

Rules on: diversity, citation, foreign, shape, propn_band; accent merges at ratio 5.0. Window: the 59,967 ranked lemmas (after the exclusion list) that fill the top 30,000. Actions: keep 26,757, propn-drop 19,579, review-drop 10,388, review-keep 3,243.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band |
|---|---:|---:|---:|---:|---:|
| diversity | 212 | 1 | 4 | 16 | 35 |
| citation | 1 | 191 | 1 | 16 | 0 |
| foreign | 4 | 1 | 4,582 | 167 | 2,163 |
| shape | 16 | 16 | 167 | 2,013 | 907 |
| propn_band | 35 | 0 | 2,163 | 907 | 9,431 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 19,579.

### Low diversity

Documents reached / documents expected at random, below 0.6 (frequency >= 20): 212 in the window. For comparison, each log2-frequency band's 2nd percentile: 16-31: 0.71, 32-63: 0.74, 64-127: 0.77, 128-255: 0.78, 256-511: 0.81, 512-1023: 0.83, 1024-2047: 0.84, 2048-4095: 0.85, 4096-8191: 0.86, 8192-16383: 0.86, 16384-32767: 0.87, 32768-65535: 0.85.

Examples: `tom` (294), `mary` (1303), `tiquete` (2285), `tomás` (3825), `ascendente` (4429), `pseudónimo` (5530), `pseudo` (5625), `de aquí en adelante` (5974), `netcomponents` (6344), `yanni` (8455), `tomasa` (8757), `bora` (9195), `microarea` (10306), `yahvé` (10619), `moncler` (10897), `wishtrips` (11402), `ziri` (13304), `alugom` (14933), `fpnm` (15469), `asimtap` (15551), `luge` (17281), `campings` (17491), `vbulletin` (18665), `consultores` (18690), `langa` (18785), `prorock-perforación` (19173), `invoice` (19301), `fossil` (20365), `skura` (21109), `gotesa` (21350), `pcbs` (21595), `stardoll` (22447), `idnet` (23905), `walla` (23980), `dimatra` (24031), `allover` (24127), `nopb` (24221), `edifier` (24781), `linked` (25299), `megaexit` (25305)

### Accent merges (3,905)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `halar` | `hala` | 24 | review: split (Hala, Halas, hala) |
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
| `eua` | `estados unidos` | 189 | review: merge |
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
| `cdmx` | `ciudad de méxico` | 139 | review: merge |
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
| `contáctano` | `contactar` | 51 | review: merge |
| `tio` | `tío` | 55 | review: merge |
| `coupon` | `cupón` | 53 | review: merge |
| `decirno` | `decir` | 53 | review: merge |
| `hornea` | `hornear` | 53 | review: merge |
| `hosteria` | `hostería` | 53 | review: merge |
| `ovnis` | `ovni` | 53 | review: merge |
| `publico` | `publicar` | 53 | review: merge |
| `implícita` | `implícito` | 52 | review: merge |
| `apresúrate` | `apresurarse` | 51 | review: merge |
| `djs` | `dj` | 51 | review: merge |
| `espacio-temporal` | `espaciotemporal` | 51 | review: merge |
| `facilitarno` | `facilitar` | 51 | review: merge |
| `oceano` | `océano` | 51 | review: merge |
| `pre-venta` | `preventa` | 51 | review: merge |
| `pídel` | `pedir` | 51 | review: merge |
| `silicone` | `silicona` | 51 | review: merge |
| `actua` | `actuar` | 50 | review: merge |
| `catalog` | `catálogo` | 50 | review: merge |
| `escribiéndono` | `escribir` | 50 | review: merge |
| `eucarioto` | `eucariota` | 50 | review: merge |
| `pidiéndol` | `pedir` | 50 | review: merge |
| `sweater` | `suéter` | 50 | review: merge |
| `ying` | `yin` | 50 | review: merge |
| `apartaos` | `apartar` | 49 | review: merge |
| `condominiums` | `condominio` | 49 | review: merge |
| `l-arginina` | `arginina` | 49 | review: merge |
| `meta-análisis` | `metaanálisis` | 49 | review: merge |
| `sur-oeste` | `suroeste` | 49 | review: merge |
| `vitamin` | `vitamina` | 49 | review: merge |
| `yogi` | `yogui` | 49 | review: merge |
| `zloty` | `esloti` | 49 | review: merge |
| `adaptándono` | `adaptar` | 48 | review: merge |
| `cabriolet` | `cabriolé` | 48 | review: merge |
| `khmer` | `jemer` | 48 | review: merge |
| `orad` | `orar` | 48 | review: merge |
| `aluminium` | `aluminio` | 47 | review: merge |
| `polyester` | `poliéster` | 47 | review: merge |
| `boricuo` | `boricua` | 46 | review: merge |
| `prediabete` | `prediabetes` | 46 | review: merge |
| `rondo` | `ronda` | 46 | review: merge |
| `vegan` | `vegano` | 46 | review: merge |
| `negarno` | `negar` | 45 | review: merge |
| `pro-vida` | `provida` | 45 | review: merge |
| `rna` | `arn` | 45 | review: merge |
| `smoking` | `esmoquin` | 45 | review: merge |
| `tendr` | `tener` | 45 | review: merge |
| `controle` | `controlar` | 44 | review: merge |
| `escapatorio` | `escapatoria` | 44 | review: merge |
| `espantapájaro` | `espantapájaros` | 44 | review: merge |
| `euromillone` | `euromillones` | 44 | review: merge |
| `moverno` | `mover` | 44 | review: merge |
| `blazers` | `blazer` | 43 | review: merge |
| `budas` | `buda` | 43 | review: merge |
| `entr` | `entre` | 43 | review: merge |
| `habea` | `habeas` | 43 | review: merge |
| `micro-ondas` | `microondas` | 43 | review: merge |
| `nautico` | `náutico` | 43 | review: merge |
| `disyuntivo` | `disyuntiva` | 42 | review: merge |
| `elimine` | `eliminar` | 42 | review: merge |
| `ruégote` | `rogar` | 42 | review: merge |
| `aluminum` | `aluminio` | 41 | review: merge |
| `anti-inmigrante` | `antiinmigrante` | 41 | review: merge |
| `bistrot` | `bistró` | 41 | review: merge |
| `co-autor` | `coautor` | 41 | review: merge |
| `cuentacuento` | `cuentacuentos` | 41 | review: merge |
| `en-línea` | `en línea` | 35 | review: merge |
| `freak` | `friki` | 41 | review: merge |
| `masai` | `masái` | 41 | review: merge |
| `no-violencia` | `no violencia` | 41 | review: merge |
| `paises` | `países` | 41 | review: merge |
| `quiénes` | `quién` | 41 | review: merge |
| `shogun` | `sogún` | 41 | review: merge |
| `burdeo` | `burdeos` | 40 | review: merge |
| `díjol` | `decir` | 40 | review: merge |
| `ephod` | `efod` | 40 | review: merge |
| `portaobjeto` | `portaobjetos` | 40 | review: merge |
| `sentaos` | `sentar` | 40 | review: merge |
| `sur-este` | `sureste` | 40 | review: merge |
| `ayudándono` | `ayudar` | 39 | review: merge |
| `biomarcadore` | `biomarcador` | 39 | review: merge |
| `co-creador` | `cocreador` | 39 | review: merge |
| `lactobacillus` | `lactobacilo` | 39 | review: merge |
| `magister` | `magíster` | 39 | review: merge |
| `nro` | `número` | 39 | review: merge |
| `portapapel` | `portapapeles` | 39 | review: merge |
| `youtubers` | `youtuber` | 39 | review: merge |
| `afro-americano` | `afroamericano` | 38 | review: merge |
| `calculo` | `calcular` | 38 | review: merge |
| `casuístico` | `casuística` | 38 | review: merge |
| `expresas` | `expresar` | 38 | review: merge |
| `beta-caroteno` | `betacaroteno` | 37 | review: merge |
| `centr` | `centrar` | 37 | review: merge |
| `electronica` | `electrónica` | 37 | review: merge |
| `gabion` | `gavión` | 37 | review: merge |
| `mares` | `mar` | 37 | review: merge |
| `muselino` | `muselina` | 37 | review: merge |
| `paratiroid` | `paratiroides` | 37 | review: merge |
| `portapape` | `portapapeles` | 37 | review: merge |
| `totem` | `tótem` | 37 | review: merge |
| `unidas` | `unido` | 37 | review: merge |
| `virolo` | `virola` | 37 | review: merge |
| `acercándono` | `acercar` | 36 | review: merge |
| `adicionale` | `adicional` | 36 | review: merge |
| `ctra` | `carretera` | 36 | review: merge |
| `enséñano` | `enseñar` | 36 | review: merge |
| `extragrand` | `extragrande` | 36 | review: merge |
| `mecena` | `mecenas` | 36 | review: merge |
| `ocuparno` | `ocupar` | 36 | review: merge |
| `poleras` | `polera` | 36 | review: merge |
| `post-producción` | `posproducción` | 36 | review: merge |
| `telex` | `télex` | 36 | review: merge |
| `tipográficos` | `tipográfico` | 36 | review: merge |
| `auto-realización` | `autorrealización` | 35 | review: merge |
| `catalogo` | `catálogo` | 35 | review: merge |
| `sofás-cama` | `sofá cama` | 35 | review: merge |
| `trafico` | `tráfico` | 35 | review: merge |
| `apartao` | `apartar` | 34 | review: merge |
| `ciencia-ficción` | `ciencia ficción` | 34 | review: merge |
| `contacteno` | `contactar` | 34 | review: merge |
| `cortex` | `córtex` | 34 | review: merge |
| `expresso` | `expreso` | 34 | review: merge |
| `khaki` | `caqui` | 34 | review: merge |
| `microfiber` | `microfibra` | 34 | review: merge |
| `plegador` | `plegadora` | 34 | review: merge |
| `pre-escolar` | `preescolar` | 34 | review: merge |
| `subid` | `subir` | 34 | review: merge |
| `ajustándono` | `ajustar` | 33 | review: merge |
| `auditorium` | `auditorio` | 33 | review: merge |
| `excreto` | `excretar` | 33 | review: merge |
| `investiga` | `investigar` | 33 | review: merge |
| `pavimentador` | `pavimentadora` | 33 | review: merge |
| `pintalabio` | `pintalabios` | 33 | review: merge |
| `plantas` | `planta` | 33 | review: merge |
| `portabicicleta` | `portabicicletas` | 33 | review: merge |
| `pre-producción` | `preproducción` | 33 | review: merge |
| `proxie` | `proxy` | 33 | review: merge |
| `reggaeton` | `reguetón` | 33 | review: merge |
| `sumergirno` | `sumergir` | 33 | review: merge |
| `verl` | `ver` | 33 | review: merge |
| `actualice` | `actualizar` | 32 | review: merge |
| `anti-polvo` | `antipolvo` | 32 | review: merge |
| `cuentagota` | `cuentagotas` | 32 | review: merge |
| `distribuidores` | `distribuidor` | 32 | review: merge |
| `etica` | `ética` | 32 | review: merge |
| `gramíneo` | `gramínea` | 32 | review: merge |
| `otror` | `otrora` | 32 | review: merge |
| `pendienteo` | `pendiente` | 32 | review: merge |
| `quads` | `quad` | 32 | review: merge |
| `quasar` | `cuásar` | 32 | review: merge |
| `ame` | `amar` | 31 | review: merge |
| `condominium` | `condominio` | 31 | review: merge |
| `dejándol` | `dejar` | 31 | review: merge |
| `dermatiti` | `dermatitis` | 31 | review: merge |
| `después-venta` | `posventa` | 31 | review: merge |
| `in-situ` | `in situ` | 31 | review: merge |
| `multifor` | `multiforme` | 31 | review: merge |
| `plexiglas` | `plexiglás` | 31 | review: merge |
| `spirulina` | `espirulina` | 31 | review: merge |
| `vegana` | `vegano` | 31 | review: merge |
| `yo-yo` | `yoyó` | 31 | review: merge |
| `apocalypse` | `apocalipsis` | 30 | review: merge |
| `bendecida` | `bendecir` | 30 | review: merge |
| `cañado` | `cañada` | 30 | review: merge |
| `comprometiéndono` | `comprometer` | 30 | review: merge |
| `dra` | `doctor` | 30 | review: merge |
| `epsilon` | `épsilon` | 30 | review: merge |
| `imprime` | `imprimir` | 30 | review: merge |
| `intramuro` | `intramuros` | 30 | review: merge |
| `multi-función` | `multifunción` | 30 | review: merge |
| `mándeno` | `mandar` | 30 | review: merge |
| `raglan` | `raglán` | 30 | review: merge |
| `bóia` | `boya` | 29 | review: merge |
| `correo-e` | `correo electrónico` | 29 | review: merge |
| `estr` | `estrés` | 29 | review: merge |
| `incidentales` | `incidental` | 29 | review: merge |
| `magnesium` | `magnesio` | 29 | review: merge |
| `moka` | `moca` | 29 | review: merge |
| `omnibus` | `ómnibus` | 29 | review: merge |
| `post-it` | `pósit` | 29 | review: merge |
| `preparándono` | `preparar` | 29 | review: merge |
| `rizada` | `rizado` | 29 | review: merge |
| `anti-inflamatorias` | `antiinflamatorio` | 28 | review: merge |
| `bloq` | `bloqueo` | 28 | review: merge |
| `crayon` | `crayón` | 28 | review: merge |
| `cyan` | `cian` | 28 | review: merge |
| `deposito` | `depósito` | 28 | review: merge |
| `hablándol` | `hablar` | 28 | review: merge |
| `hobbie` | `hobby` | 28 | review: merge |
| `inexactitudes` | `inexactitud` | 28 | review: merge |
| `leds` | `led` | 28 | review: merge |
| `naif` | `naíf` | 28 | review: merge |
| `patche` | `parche` | 28 | review: merge |
| `patr` | `patrón` | 28 | review: merge |
| `senora` | `señora` | 28 | review: merge |
| `tutu` | `tutú` | 28 | review: merge |
| `volleyball` | `voleibol` | 28 | review: merge |
| `barbecue` | `barbacoa` | 27 | review: merge |
| `borrados` | `borrar` | 27 | review: merge |
| `centro-izquierda` | `centroizquierda` | 27 | review: merge |
| `doxycycline` | `doxiciclina` | 27 | review: merge |
| `ejercito` | `ejército` | 27 | review: merge |
| `enséñel` | `enseñar` | 27 | review: merge |
| `filmador` | `filmadora` | 27 | review: merge |
| `gir` | `girar` | 27 | review: merge |
| `mini-juego` | `minijuego` | 27 | review: merge |
| `minibuse` | `minibús` | 27 | review: merge |
| `nickel` | `níquel` | 27 | review: merge |
| `pasamontaña` | `pasamontañas` | 27 | review: merge |
| `perderno` | `perder` | 27 | review: merge |
| `re-enfocar` | `reenfocar` | 27 | review: merge |
| `volley` | `vóley` | 27 | review: merge |
| `acuérdate` | `acordarse` | 26 | review: merge |
| `afrikaans` | `afrikáans` | 26 | review: merge |
| `apart-hotel` | `apartahotel` | 26 | review: merge |
| `años-luz` | `año luz` | 26 | review: merge |
| `bazooka` | `bazuca` | 26 | review: merge |
| `brasileiro` | `brasileño` | 26 | review: merge |
| `chassis` | `chasis` | 26 | review: merge |
| `enviándol` | `enviar` | 26 | review: merge |
| `escribirno` | `escribir` | 26 | review: merge |
| `fakir` | `faquir` | 26 | review: merge |
| `garifuna` | `garífuna` | 26 | review: merge |
| `indústria` | `industria` | 26 | review: merge |
| `jajajaja` | `jaja` | 26 | review: merge |
| `metformin` | `metformina` | 26 | review: merge |
| `minibu` | `minibús` | 26 | review: merge |
| `máquina-herramienta` | `máquina herramienta` | 26 | review: merge |
| `pyrex` | `pírex` | 26 | review: merge |
| `sudadero` | `sudadera` | 26 | review: merge |
| `anti-estrés` | `antiestrés` | 25 | review: merge |
| `codero` | `cordero` | 25 | review: merge |
| `cuidados` | `cuidado` | 25 | review: merge |
| `dob` | `doble` | 25 | review: merge |
| `encuenstra` | `encontrar` | 25 | review: merge |
| `euskara` | `euskera` | 25 | review: merge |
| `gilipolla` | `gilipollas` | 25 | review: merge |
| `golem` | `gólem` | 25 | review: merge |
| `grátis` | `gratis` | 25 | review: merge |
| `llamarno` | `llamar` | 25 | review: merge |
| `magyar` | `magiar` | 25 | review: merge |
| `materno-infantil` | `maternoinfantil` | 25 | review: merge |
| `mostraro` | `mostrar` | 25 | review: merge |
| `multi-funcional` | `multifuncional` | 25 | review: merge |
| `notícias` | `noticia` | 25 | review: merge |
| `olvidarno` | `olvidar` | 25 | review: merge |
| `planifique` | `planificar` | 25 | review: merge |
| `posavaso` | `posavasos` | 25 | review: merge |
| `rechazan` | `rechazar` | 25 | review: merge |
| `reconociendo` | `reconocer` | 25 | review: merge |
| `spanglish` | `espanglish` | 25 | review: merge |
| `superventa` | `superventas` | 25 | review: merge |
| `unisexo` | `unisex` | 25 | review: merge |
| `abrelata` | `abrelatas` | 24 | review: merge |
| `acercaos` | `acercar` | 24 | review: merge |
| `adem` | `además` | 24 | review: merge |
| `alejarno` | `alejar` | 24 | review: merge |
| `barberos` | `barbero` | 24 | review: merge |
| `centro-derecha` | `centroderecha` | 24 | review: merge |
| `corta` | `corto` | 24 | review: merge |
| `e-cigarrillo` | `cigarrillo electrónico` | 24 | review: merge |
| `finasteride` | `finasterida` | 24 | review: merge |
| `guardacosta` | `guardacostas` | 24 | review: merge |
| `mea` | `mear` | 24 | review: merge |
| `muell` | `muelle` | 648 | review: merge |
| `personalizabl` | `personalizable` | 405 | review: merge |
| `ofrecerl` | `ofrecer` | 313 | review: merge |
| `dobl` | `doble` | 220 | review: merge |
| `encuentr` | `encontrar` | 185 | review: merge |
| `brindarl` | `brindar` | 159 | review: merge |
| `puzl` | `puzle` | 155 | review: merge |
| `descargabl` | `descargable` | 151 | review: merge |
| `enseñarl` | `enseñar` | 102 | review: merge |
| `proporcionarl` | `proporcionar` | 96 | review: merge |
| `multipl` | `múltiple` | 91 | review: merge |
| `azafr` | `azafrán` | 90 | review: merge |
| `increibl` | `increíble` | 88 | review: merge |
| `mostrarl` | `mostrar` | 88 | review: merge |
| `coleccionabl` | `coleccionable` | 83 | review: merge |
| `psiquiatr` | `psiquiatría` | 72 | review: merge |
| `prevenibl` | `prevenible` | 69 | review: merge |
| `jugabl` | `jugable` | 66 | review: merge |
| `servirl` | `servir` | 66 | review: merge |
| `waffl` | `wafle` | 57 | review: merge |
| `masticabl` | `masticable` | 55 | review: merge |
| `invaluabl` | `invaluable` | 52 | review: merge |
| `agradecerl` | `agradecer` | 43 | review: merge |
| `otorgarl` | `otorgar` | 37 | review: merge |
| `permitirl` | `permitir` | 36 | review: merge |
| `descartabl` | `descartable` | 33 | review: merge |
| `transmitirl` | `transmitir` | 32 | review: merge |
| `enviarl` | `enviar` | 31 | review: merge |
| `espectrometr` | `espectrometría` | 30 | review: merge |
| `idolatr` | `idolatría` | 29 | review: merge |
| `liposolubl` | `liposoluble` | 28 | review: merge |
| `causarl` | `causar` | 25 | review: merge |
| `compartirl` | `compartir` | 25 | review: merge |
| `hablarl` | `hablar` | 25 | review: merge |
| `llevarl` | `llevar` | 25 | review: merge |
| `hazl` | `hacer` | 24 | review: merge |
| `portacabl` | `portacables` | 24 | review: merge |
| `psiquiátra` | `psiquiatra` | 24 | review: merge |
| `quitanieve` | `quitanieves` | 24 | review: merge |
| `roast` | `rosbif` | 24 | review: merge |
| `superf` | `superficie` | 24 | review: merge |
| `veintitanto` | `veintitantos` | 24 | review: merge |
| `agrocombustibl` | `agrocombustible` | 23 | review: merge |
| `aparcamento` | `aparcamiento` | 23 | review: merge |
| `arrepentío` | `arrepentirse` | 23 | review: merge |
| `auto-ayuda` | `autoayuda` | 23 | review: merge |
| `concordancias` | `concordancia` | 23 | review: merge |
| `curcumin` | `curcumina` | 23 | review: merge |
| `deleitarno` | `deleitarse` | 23 | review: merge |
| `desbloqueabl` | `desbloqueable` | 23 | review: merge |
| `despedirno` | `despedirse` | 23 | review: merge |
| `diciéndono` | `decir` | 23 | review: merge |
| `e-books` | `e-book` | 23 | review: merge |
| `emulator` | `emulador` | 23 | review: merge |
| `enfocándo` | `enfocar` | 23 | review: merge |
| `enséñal` | `enseñar` | 23 | review: merge |
| `ex-presidente` | `expresidente` | 23 | review: merge |
| `fueron` | `ser` | 23 | review: merge |
| `l-glutamina` | `glutamina` | 23 | review: merge |
| `l-teanina` | `teanina` | 23 | review: merge |
| `legionella` | `legionela` | 23 | review: merge |
| `muéstral` | `mostrar` | 23 | review: merge |
| `neuroendocrinos` | `neuroendocrino` | 23 | review: merge |
| `off-line` | `offline` | 23 | review: merge |
| `pancakes` | `panqueque` | 23 | review: merge |
| `polyimide` | `poliimida` | 23 | review: merge |
| `redon` | `redondo` | 23 | review: merge |
| `teka` | `teca` | 23 | review: merge |
| `vendo` | `vender` | 23 | review: merge |
| `vice-presidente` | `vicepresidente` | 23 | review: merge |
| `zig-zag` | `zigzag` | 23 | review: merge |
| `abrebotella` | `abrebotellas` | 22 | review: merge |
| `alf` | `alfa` | 22 | review: merge |
| `bajero` | `bajera` | 22 | review: merge |
| `boomers` | `boomer` | 22 | review: merge |
| `cazafantasma` | `cazafantasmas` | 22 | review: merge |
| `co-fundadora` | `cofundador` | 22 | review: merge |
| `conserve` | `conservar` | 22 | review: merge |
| `eufrate` | `éufrates` | 22 | review: merge |
| `gangster` | `gánster` | 22 | review: merge |
| `hurtadilla` | `hurtadillas` | 22 | review: merge |
| `informándol` | `informar` | 22 | review: merge |
| `kilate` | `quilate` | 22 | review: merge |
| `mamás` | `mamá` | 22 | review: merge |
| `poniéndono` | `poner` | 22 | review: merge |
| `quedarno` | `quedar` | 22 | review: merge |
| `reumatoideo` | `reumatoide` | 22 | review: merge |
| `taca` | `taza` | 22 | review: merge |
| `talleres` | `taller` | 22 | review: merge |
| `aymara` | `aimara` | 21 | review: merge |
| `bacterial` | `bacteriano` | 21 | review: merge |
| `bautisto` | `bautista` | 21 | review: merge |
| `catamaran` | `catamarán` | 21 | review: merge |
| `centrarno` | `centrar` | 21 | review: merge |
| `desconocidas` | `desconocido` | 21 | review: merge |
| `doma` | `domar` | 21 | review: merge |
| `enseñándono` | `enseñar` | 21 | review: merge |
| `ex-novia` | `exnovia` | 21 | review: merge |
| `hryvnia` | `grivna` | 21 | review: merge |
| `intimo` | `íntimo` | 21 | review: merge |
| `kilométro` | `kilómetro` | 21 | review: merge |
| `lapis` | `lapislázuli` | 21 | review: merge |
| `lic` | `licenciado` | 21 | review: merge |
| `mesquita` | `mezquita` | 21 | review: merge |
| `mitzvot` | `mitzvá` | 21 | review: merge |
| `otorgándol` | `otorgar` | 21 | review: merge |
| `portadocumento` | `portadocumentos` | 21 | review: merge |
| `portatarjeta` | `portatarjetas` | 21 | review: merge |
| `post-procesamiento` | `posprocesamiento` | 21 | review: merge |
| `prepárese` | `preparar` | 21 | review: merge |
| `quran` | `corán` | 21 | review: merge |
| `quórume` | `quórum` | 21 | review: merge |
| `recopilamos` | `recopilar` | 21 | review: merge |
| `requiem` | `réquiem` | 21 | review: merge |
| `retinoid` | `retinoide` | 21 | review: merge |
| `sheij` | `jeque` | 21 | review: merge |
| `socio-económica` | `socioeconómico` | 21 | review: merge |
| `subtitu` | `subtítulo` | 21 | review: merge |
| `sur-oriental` | `suroriental` | 21 | review: merge |
| `telemetr` | `telemetría` | 21 | review: merge |
| `zircon` | `circón` | 21 | review: merge |
| `acabé` | `acabar` | 20 | review: merge |
| `animo` | `animar` | 20 | review: merge |
| `apocal` | `apocalipsis` | 20 | review: merge |
| `asumí` | `asumir` | 20 | review: merge |
| `audio-visual` | `audiovisual` | 20 | review: merge |
| `berebere` | `bereber` | 20 | review: merge |
| `co-director` | `codirector` | 20 | review: merge |
| `cosmetica` | `cosmética` | 20 | review: merge |
| `explicaro` | `explicar` | 20 | review: merge |
| `filiales` | `filial` | 20 | review: merge |
| `gul` | `gules` | 20 | review: merge |
| `interoperabl` | `interoperable` | 20 | review: merge |
| `invitarl` | `invitar` | 20 | review: merge |
| `limousine` | `limusina` | 20 | review: merge |
| `megapixels` | `megapíxel` | 20 | review: merge |
| `muertos` | `muerto` | 20 | review: merge |
| `multimedio` | `multimedia` | 20 | review: merge |
| `niacin` | `niacina` | 20 | review: merge |
| `optimice` | `optimizar` | 20 | review: merge |
| `perjuicios` | `perjuicio` | 20 | review: merge |
| `polka` | `polca` | 20 | review: merge |
| `ponerl` | `poner` | 20 | review: merge |
| `portapapele` | `portapapeles` | 20 | review: merge |
| `pre-instalación` | `preinstalación` | 20 | review: merge |
| `pregúntel` | `preguntar` | 20 | review: merge |
| `proactiva` | `proactivo` | 20 | review: merge |
| `socio-político` | `sociopolítico` | 20 | review: merge |
| `spin-offs` | `spin-off` | 20 | review: merge |
| `tamoxifen` | `tamoxifeno` | 20 | review: merge |
| `taser` | `táser` | 20 | review: merge |
| `tretinoin` | `tretinoína` | 20 | review: merge |
| `univ` | `universidad` | 20 | review: merge |
| `albume` | `álbum` | 19 | review: merge |
| `ansiso` | `ansioso` | 19 | review: merge |
| `apoyándono` | `apoyar` | 19 | review: merge |
| `atrave` | `atravesar` | 19 | review: merge |
| `auto-conocimiento` | `autoconocimiento` | 19 | review: merge |
| `ayúdano` | `ayudar` | 19 | review: merge |
| `benchmarks` | `benchmark` | 19 | review: merge |
| `co-crear` | `cocrear` | 19 | review: merge |
| `co-presidente` | `copresidente` | 19 | review: merge |
| `convertío` | `convertir` | 19 | review: merge |
| `freelancers` | `freelance` | 19 | review: merge |
| `gral` | `general` | 19 | review: merge |
| `inclina` | `inclinar` | 19 | review: merge |
| `inmobiliarias` | `inmobiliaria` | 19 | review: merge |
| `inserte` | `insertar` | 19 | review: merge |
| `jiu-jitsu` | `yiu-yitsu` | 19 | review: merge |
| `lame` | `lamer` | 19 | review: merge |
| `lanzallama` | `lanzallamas` | 19 | review: merge |
| `liquitación` | `liquidación` | 19 | review: merge |
| `mantenerl` | `mantener` | 19 | review: merge |
| `menonitas` | `menonita` | 19 | review: merge |
| `minicargadore` | `minicargador` | 19 | review: merge |
| `mostrándol` | `mostrar` | 19 | review: merge |
| `penalty` | `penalti` | 19 | review: merge |
| `portabroca` | `portabrocas` | 19 | review: merge |
| `pre-existentes` | `preexistente` | 19 | review: merge |
| `click` | `clic` | 3,788 | review: merge |
| `reserve` | `reservar` | 3,137 | review: merge |
| `jul` | `julio` | 2,654 | review: merge |
| `busca` | `buscar` | 2,638 | review: merge |
| `descargue` | `descargar` | 2,556 | review: merge |
| `clara` | `claro` | 2,154 | review: merge |
| `poker` | `póker` | 1,622 | review: merge |
| `atrever` | `atreverse` | 1,467 | review: merge |
| `familiarízate` | `familiarizarse` | 1,424 | review: merge |
| `alta` | `alto` | 1,325 | review: merge |
| `visto` | `ver` | 1,205 | review: merge |
| `administrativa` | `administrativo` | 1,173 | review: merge |
| `reyes` | `rey` | 1,163 | review: merge |
| `arar` | `aro` | 1,157 | review: merge |
| `regístrese` | `registrarse` | 1,060 | review: merge |
| `guárdela` | `guardar` | 1,064 | review: merge |
| `campos` | `campo` | 907 | review: merge |
| `flores` | `flor` | 889 | review: merge |
| `almohadillar` | `almohadilla` | 871 | review: merge |
| `ponte` | `ponerse` | 830 | review: merge |
| `iglesias` | `iglesia` | 776 | review: merge |
| `hechos` | `hecho` | 763 | review: merge |
| `consultá` | `consultar` | 752 | review: merge |
| `suscríbase` | `suscribirse` | 728 | review: merge |
| `explore` | `explorar` | 706 | review: merge |
| `derechar` | `derecho` | 699 | review: merge |
| `roturar` | `rotura` | 671 | review: merge |
| `reales` | `real` | 665 | review: merge |
| `fallir` | `fallido` | 636 | review: merge |
| `oct` | `octubre` | 636 | review: merge |
| `jun` | `junio` | 632 | review: merge |
| `ejecutiva` | `ejecutivo` | 627 | review: merge |
| `turbinar` | `turbina` | 606 | review: merge |
| `incensar` | `incienso` | 599 | review: merge |
| `ref` | `referencia` | 594 | review: merge |
| `máx` | `máximo` | 582 | review: merge |
| `dino` | `decir` | 577 | review: merge |
| `forjado` | `forjar` | 575 | review: merge |
| `escalonar` | `escalón` | 544 | review: merge |
| `tributar` | `tributo` | 544 | review: merge |
| `llamadas` | `llamada` | 542 | review: merge |
| `nov` | `noviembre` | 540 | review: merge |
| `bridar` | `brida` | 533 | review: merge |
| `esterar` | `estera` | 528 | review: merge |
| `tintar` | `tinte` | 527 | review: merge |
| `versar` | `verso` | 514 | review: merge |
| `eclipsar` | `eclipse` | 513 | review: merge |
| `cargue` | `cargar` | 508 | review: merge |
| `magnificar` | `magnífico` | 503 | review: merge |
| `mantente` | `mantenerse` | 501 | review: merge |
| `azufrar` | `azufre` | 499 | review: merge |
| `guión` | `guion` | 486 | review: merge |
| `seguida` | `seguir` | 484 | review: merge |
| `sobretodo` | `sobre todo` | 472 | review: merge |
| `charter` | `chárter` | 468 | review: merge |
| `falto` | `falta` | 468 | review: merge |
| `dic` | `diciembre` | 461 | review: merge |
| `plugins` | `plugin` | 455 | review: merge |
| `manuscribir` | `manuscrito` | 452 | review: merge |
| `frita` | `frito` | 442 | review: merge |
| `cabalá` | `cábala` | 440 | review: merge |
| `fuiste` | `ser` | 436 | review: merge |
| `introcuzca` | `introducir` | 436 | review: merge |
| `arroyar` | `arroyo` | 432 | review: merge |
| `ozonar` | `ozono` | 432 | review: merge |
| `diafragmar` | `diafragma` | 430 | review: merge |
| `trailer` | `tráiler` | 430 | review: merge |
| `timbrar` | `timbre` | 429 | review: merge |
| `olear` | `oleada` | 428 | review: merge |
| `diríjase` | `dirigirse` | 420 | review: merge |
| `llagar` | `llaga` | 425 | review: merge |
| `cariar` | `caries` | 421 | review: merge |
| `status` | `estatus` | 419 | review: merge |
| `chefs` | `chef` | 414 | review: merge |
| `pigmentar` | `pigmento` | 413 | review: merge |
| `posts` | `post` | 403 | review: merge |
| `yodar` | `yodo` | 393 | review: merge |
| `duplex` | `dúplex` | 392 | review: merge |
| `relájese` | `relajarse` | 385 | review: merge |
| `gifs` | `gif` | 386 | review: merge |
| `providenciar` | `providencia` | 380 | review: merge |
| `solarium` | `solárium` | 376 | review: merge |
| `cargada` | `cargado` | 375 | review: merge |
| `ajuster` | `ajustar` | 374 | review: merge |
| `limpia` | `limpio` | 369 | review: merge |
| `redirigido` | `redirigir` | 369 | review: merge |
| `ene` | `enero` | 367 | review: merge |
| `cosmo` | `cosmos` | 361 | review: merge |
| `escamar` | `escama` | 361 | review: merge |
| `dile` | `decir` | 355 | review: merge |
| `ping` | `ping-pong` | 354 | review: merge |
| `alójate` | `alojarse` | 349 | review: merge |
| `espigar` | `espiga` | 349 | review: merge |
| `macizar` | `macizo` | 349 | review: merge |
| `escucha` | `escuchar` | 348 | review: merge |
| `levar` | `leva` | 347 | review: merge |
| `mazar` | `mazo` | 344 | review: merge |
| `cocar` | `coca` | 342 | review: merge |
| `felpar` | `felpa` | 339 | review: merge |
| `ven` | `venir` | 334 | review: merge |
| `startups` | `startup` | 332 | review: merge |
| `dirigiéndose` | `dirigirse` | 324 | review: merge |
| `enviado` | `enviar` | 327 | review: merge |
| `manir` | `maní` | 326 | review: merge |
| `sic` | `siclo` | 322 | review: merge |
| `herniar` | `hernia` | 317 | review: merge |
| `broker` | `bróker` | 316 | review: merge |
| `relájate` | `relajarse` | 304 | review: merge |
| `sorprendase` | `sorprenderse` | 309 | review: merge |
| `clorurar` | `cloruro` | 308 | review: merge |
| `computarizada` | `computarizado` | 304 | review: merge |
| `tragaperra` | `tragaperras` | 304 | review: merge |
| `moldurar` | `moldura` | 303 | review: merge |
| `ortografiar` | `ortografía` | 292 | review: merge |
| `hip` | `hip hop` | 288 | review: merge |
| `magento` | `magenta` | 288 | review: merge |
| `cartografiar` | `cartografía` | 285 | review: merge |
| `cuantiar` | `cuantía` | 285 | review: merge |
| `penitenciar` | `penitencia` | 285 | review: merge |
| `mirá` | `mirar` | 278 | review: merge |
| `condonar` | `condón` | 275 | review: merge |
| `cluster` | `clúster` | 271 | review: merge |
| `expensar` | `expensas` | 269 | review: merge |
| `substanciar` | `sustancia` | 267 | review: merge |
| `escobillar` | `escobilla` | 266 | review: merge |
| `poster` | `póster` | 261 | review: merge |
| `cielos` | `cielo` | 258 | review: merge |
| `comic` | `cómic` | 257 | review: merge |
| `refiriéndose` | `referirse` | 255 | review: merge |
| `cesáreo` | `cesárea` | 240 | review: merge |
| `sumérgete` | `sumergirse` | 252 | review: merge |
| `carburar` | `carburo` | 249 | review: merge |
| `hamburgués` | `hamburguesa` | 246 | review: merge |
| `banners` | `banner` | 242 | review: merge |
| `estelarizadas` | `estelarizar` | 242 | review: merge |
| `escorts` | `escort` | 241 | review: merge |
| `dele` | `dar` | 239 | review: merge |
| `souvenirs` | `souvenir` | 239 | review: merge |
| `curriculum` | `currículum` | 238 | review: merge |
| `carbonatar` | `carbonato` | 233 | review: merge |
| `cortocircuitar` | `cortocircuito` | 231 | review: merge |
| `rallye` | `rally` | 227 | review: merge |
| `sulfatar` | `sulfato` | 223 | review: merge |
| `avellanar` | `avellana` | 221 | review: merge |
| `ecommerce` | `e-commerce` | 214 | review: merge |
| `desplácese` | `desplazarse` | 213 | review: merge |
| `pilate` | `pilates` | 213 | review: merge |
| `fosar` | `fosa` | 212 | review: merge |
| `cadmiar` | `cadmio` | 211 | review: merge |
| `totál` | `total` | 209 | review: merge |
| `bitcoins` | `bitcoin` | 205 | review: merge |
| `toldar` | `toldo` | 205 | review: merge |
| `buscá` | `buscar` | 204 | review: merge |
| `especímenes` | `espécimen` | 202 | review: merge |
| `daro` | `dar` | 201 | review: merge |
| `lujuriar` | `lujuria` | 201 | review: merge |
| `podcasts` | `podcast` | 200 | review: merge |
| `subscríbete` | `suscribirse` | 200 | review: merge |
| `arpar` | `arpa` | 199 | review: merge |
| `explorá` | `explorar` | 198 | review: merge |
| `petar` | `peto` | 197 | review: merge |
| `reacondicionados` | `reacondicionar` | 197 | review: merge |
| `coupé` | `cupé` | 192 | review: merge |
| `necesitás` | `necesitar` | 189 | review: merge |
| `imagínate` | `imaginarse` | 177 | review: merge |
| `únete` | `unirse` | 188 | review: merge |
| `espanol` | `español` | 187 | review: merge |
| `spas` | `spa` | 187 | review: merge |
| `fosfatar` | `fosfato` | 185 | review: merge |
| `runo` | `runa` | 182 | review: merge |
| `políticas` | `política` | 179 | review: merge |
| `elije` | `elegir` | 178 | review: merge |
| `buffer` | `búfer` | 176 | review: merge |
| `incluído` | `incluir` | 176 | review: merge |
| `inox` | `inoxidable` | 175 | review: merge |
| `pulg` | `pulgada` | 175 | review: merge |
| `empiece` | `empezar` | 173 | review: merge |
| `embudar` | `embudo` | 172 | review: merge |
| `resor` | `resorte` | 172 | review: merge |
| `cocktail` | `cóctel` | 170 | review: merge |
| `webcams` | `webcam` | 170 | review: merge |
| `cassette` | `casete` | 169 | review: merge |
| `conciente` | `consciente` | 168 | review: merge |
| `estampillar` | `estampilla` | 168 | review: merge |
| `avispar` | `avispa` | 167 | review: merge |
| `vistar` | `vista` | 166 | review: merge |
| `imagínese` | `imaginarse` | 164 | review: merge |
| `tranzar` | `trance` | 164 | review: merge |
| `autobu` | `autobús` | 163 | review: merge |
| `indumentario` | `indumentaria` | 163 | review: merge |
| `laudar` | `laudo` | 163 | review: merge |
| `reale` | `real` | 163 | review: merge |
| `mocar` | `moco` | 162 | review: merge |
| `ojalar` | `ojal` | 162 | review: merge |
| `traders` | `trader` | 162 | review: merge |
| `caligrafiar` | `caligrafía` | 160 | review: merge |
| `candar` | `candado` | 160 | review: merge |
| `indulgenciar` | `indulgencia` | 157 | review: merge |
| `llegarí` | `llegar` | 156 | review: merge |
| `trinchero` | `trinchera` | 156 | review: merge |
| `uds` | `ustedes` | 156 | review: merge |
| `escoriar` | `escoria` | 155 | review: merge |
| `usá` | `usar` | 154 | review: merge |
| `demando` | `demanda` | 153 | review: merge |
| `ej` | `ejemplo` | 153 | review: merge |
| `correar` | `correa` | 152 | review: merge |
| `está` | `estar` | 150 | review: merge |
| `vol` | `volumen` | 149 | review: merge |
| `buscás` | `buscar` | 148 | review: merge |
| `resúmen` | `resumen` | 148 | review: merge |
| `desigualar` | `desigual` | 147 | review: merge |
| `pallet` | `palé` | 147 | review: merge |
| `paracaída` | `paracaídas` | 147 | review: merge |
| `balar` | `bala` | 141 | review: merge |
| `desesperanzar` | `desesperanza` | 141 | review: merge |
| `extrañir` | `extraño` | 141 | review: merge |
| `millennials` | `millennial` | 141 | review: merge |
| `ato` | `atar` | 140 | review: merge |
| `enserar` | `enseres` | 140 | review: merge |
| `acércate` | `acercarse` | 139 | review: merge |
| `bugs` | `bug` | 139 | review: merge |
| `gratar` | `grato` | 139 | review: merge |
| `recamar` | `recámara` | 139 | review: merge |
| `tajar` | `tajada` | 138 | review: merge |
| `atópica` | `atópico` | 136 | review: merge |
| `bizcochar` | `bizcocho` | 136 | review: merge |
| `gofrar` | `gofre` | 136 | review: merge |
| `ponter` | `ponerse` | 136 | review: merge |
| `sintiéndose` | `sentirse` | 136 | review: merge |
| `ampere` | `amperio` | 135 | review: merge |
| `maliciar` | `malicia` | 135 | review: merge |
| `motora` | `motor` | 135 | review: merge |
| `fuer` | `ser` | 134 | review: merge |
| `carnicer` | `carnicería` | 133 | review: merge |
| `planificá` | `planificar` | 133 | review: merge |
| `primas` | `prima` | 133 | review: merge |
| `deshabilita` | `deshabilitar` | 132 | review: merge |
| `flavonoid` | `flavonoide` | 132 | review: merge |
| `softwar` | `software` | 132 | review: merge |
| `víver` | `víveres` | 125 | review: merge |
| `úsalas` | `usar` | 132 | review: merge |
| `resacar` | `resaca` | 131 | review: merge |
| `técnicar` | `técnica` | 131 | review: merge |
| `intimar` | `íntimo` | 130 | review: merge |
| `bloggers` | `blogger` | 129 | review: merge |
| `catapultar` | `catapulta` | 129 | review: merge |
| `chateo` | `chatear` | 129 | review: merge |
| `cripto` | `criptomoneda` | 129 | review: merge |
| `faenar` | `faena` | 129 | review: merge |
| `fórum` | `foro` | 129 | review: merge |
| `hashtags` | `hashtag` | 129 | review: merge |
| `mander` | `mando` | 129 | review: merge |
| `siembrir` | `siembra` | 129 | review: merge |
| `clica` | `clicar` | 128 | review: merge |
| `columpiar` | `columpio` | 128 | review: merge |
| `odenador` | `ordenador` | 128 | review: merge |
| `arenisco` | `arenisca` | 127 | review: merge |
| `cupcakes` | `cupcake` | 127 | review: merge |
| `electrónicar` | `electrónica` | 127 | review: merge |
| `hacé` | `hacer` | 127 | review: merge |
| `racks` | `rack` | 127 | review: merge |
| `cachar` | `cacho` | 126 | review: merge |
| `papar` | `papada` | 126 | review: merge |
| `refiérase` | `referirse` | 117 | review: merge |
| `listonar` | `listón` | 125 | review: merge |
| `visitá` | `visitar` | 125 | review: merge |
| `burritos` | `burrito` | 124 | review: merge |
| `folklore` | `folclore` | 124 | review: merge |
| `newsletters` | `newsletter` | 124 | review: merge |
| `desfasar` | `desfase` | 123 | review: merge |
| `muerta` | `muerto` | 123 | review: merge |
| `endurar` | `enduro` | 122 | review: merge |
| `tuits` | `tuit` | 122 | review: merge |
| `laptops` | `laptop` | 121 | review: merge |
| `muelles` | `muelle` | 121 | review: merge |
| `suelta` | `suelto` | 121 | review: merge |
| `redireccionado` | `redireccionar` | 120 | review: merge |
| `nitratar` | `nitrato` | 119 | review: merge |
| `pellets` | `pellet` | 119 | review: merge |
| `plug-ins` | `plug-in` | 119 | review: merge |
| `bendecido` | `bendecir` | 118 | review: merge |
| `colorar` | `colorado` | 118 | review: merge |
| `desusar` | `desuso` | 118 | review: merge |
| `iner` | `inerte` | 118 | review: merge |
| `tuiteó` | `tuitear` | 105 | review: merge |
| `cizañar` | `cizaña` | 117 | review: merge |
| `emojis` | `emoji` | 117 | review: merge |
| `hocicar` | `hocico` | 117 | review: merge |
| `pesquisar` | `pesquisa` | 116 | review: merge |
| `feeds` | `feed` | 115 | review: merge |
| `codec` | `códec` | 114 | review: merge |
| `flagelar` | `flagelo` | 114 | review: merge |
| `lavada` | `lavar` | 114 | review: merge |
| `lazar` | `lazada` | 114 | review: merge |
| `torna` | `tornar` | 114 | review: merge |
| `parafinar` | `parafina` | 113 | review: merge |
| `querellar` | `querella` | 113 | review: merge |
| `twittear` | `tuitear` | 113 | review: merge |
| `capsular` | `cápsula` | 112 | review: merge |
| `likes` | `like` | 112 | review: merge |
| `remachar` | `remache` | 112 | review: merge |
| `emulsionar` | `emulsión` | 111 | review: merge |
| `estufar` | `estufa` | 111 | review: merge |
| `expandiéndose` | `expandirse` | 111 | review: merge |
| `inmersiva` | `inmersivo` | 111 | review: merge |
| `maderar` | `madera` | 111 | review: merge |
| `veintiún` | `veintiuno` | 111 | review: merge |
| `boyar` | `boya` | 110 | review: merge |
| `stress` | `estrés` | 110 | review: merge |
| `clicks` | `clic` | 109 | review: merge |
| `dermi` | `dermis` | 109 | review: merge |
| `nótese` | `notar` | 109 | review: merge |
| `cintar` | `cinto` | 108 | review: merge |
| `ve` | `ver` | 108 | review: merge |
| `adjetivar` | `adjetivo` | 107 | review: merge |
| `gadgets` | `gadget` | 107 | review: merge |
| `rastrillar` | `rastrillo` | 107 | review: merge |
| `asegurese` | `asegurarse` | 106 | review: merge |
| `catastrar` | `catastro` | 106 | review: merge |
| `wikis` | `wiki` | 106 | review: merge |
| `anímate` | `animarse` | 105 | review: merge |
| `cobaltar` | `cobalto` | 105 | review: merge |
| `accesar` | `acceder` | 104 | review: merge |
| `abastar` | `abasto` | 103 | review: merge |
| `apartmento` | `apartamento` | 103 | review: merge |
| `cambiá` | `cambiar` | 103 | review: merge |
| `enjambrar` | `enjambre` | 103 | review: merge |
| `hisopar` | `hisopo` | 103 | review: merge |
| `microfinanza` | `microfinanzas` | 103 | review: merge |
| `rendido` | `rendir` | 103 | review: merge |
| `últma` | `último` | 103 | review: merge |
| `blister` | `blíster` | 102 | review: merge |
| `desinstale` | `desinstalar` | 102 | review: merge |
| `laparoscópica` | `laparoscópico` | 102 | review: merge |
| `llámano` | `llamar` | 93 | review: merge |
| `páde` | `pádel` | 102 | review: merge |
| `snorkeling` | `esnórquel` | 102 | review: merge |
| `brumar` | `bruma` | 101 | review: merge |
| `chalar` | `chalé` | 101 | review: merge |
| `primarias` | `primario` | 101 | review: merge |
| `adolecente` | `adolescente` | 100 | review: merge |
| `basta` | `bastar` | 100 | review: merge |
| `envia` | `enviar` | 100 | review: merge |
| `podeis` | `poder` | 100 | review: merge |
| `sufijar` | `sufijo` | 100 | review: merge |
| `atalayar` | `atalaya` | 99 | review: merge |
| `hab` | `habitación` | 99 | review: merge |
| `majar` | `majo` | 99 | review: merge |
| `granar` | `grana` | 98 | review: merge |
| `sumérjase` | `sumergirse` | 98 | review: merge |
| `cilindrar` | `cilindrada` | 97 | review: merge |
| `defendido` | `defender` | 97 | review: merge |
| `malabar` | `malabares` | 97 | review: merge |
| `oprobiar` | `oprobio` | 97 | review: merge |
| `precintar` | `precinto` | 97 | review: merge |
| `suscríbete` | `suscribirse` | 97 | review: merge |
| `variz` | `várice` | 97 | review: merge |
| `atla` | `atlas` | 96 | review: merge |
| `dema` | `demás` | 96 | review: merge |
| `indultar` | `indulto` | 96 | review: merge |
| `preludiar` | `preludio` | 96 | review: merge |
| `remolinar` | `remolino` | 96 | review: merge |
| `sulfurar` | `sulfuro` | 96 | review: merge |
| `alfalfar` | `alfalfa` | 95 | review: merge |
| `ceniciento` | `cenicienta` | 95 | review: merge |
| `deshelar` | `deshielo` | 95 | review: merge |
| `huespede` | `huésped` | 95 | review: merge |
| `incluída` | `incluir` | 95 | review: merge |
| `reestablecer` | `restablecer` | 95 | review: merge |
| `suba` | `subir` | 95 | review: merge |
| `trajar` | `traje` | 95 | review: merge |
| `capotar` | `capota` | 94 | review: merge |
| `cómpralo` | `comprar` | 94 | review: merge |
| `entrepernar` | `entrepierna` | 94 | review: merge |
| `envió` | `enviar` | 94 | review: merge |
| `lofts` | `loft` | 94 | review: merge |
| `muertar` | `muerto` | 94 | review: merge |
| `piercings` | `piercing` | 93 | review: merge |
| `prediseñadas` | `prediseñado` | 93 | review: merge |
| `strass` | `estrás` | 93 | review: merge |
| `cavo` | `cava` | 92 | review: merge |
| `escaramuzar` | `escaramuza` | 92 | review: merge |
| `murmullar` | `murmullo` | 92 | review: merge |
| `remansar` | `remanso` | 92 | review: merge |
| `erar` | `ser` | 91 | review: merge |
| `garzo` | `garza` | 91 | review: merge |
| `lacrar` | `lacre` | 91 | review: merge |
| `platinar` | `platina` | 91 | review: merge |
| `trocar` | `trueque` | 91 | review: merge |
| `cizallar` | `cizalla` | 90 | review: merge |
| `guindar` | `guinda` | 90 | review: merge |
| `hojaldrar` | `hojaldre` | 90 | review: merge |
| `lavamano` | `lavamanos` | 90 | review: merge |
| `leída` | `leer` | 90 | review: merge |
| `mezclo` | `mezclar` | 90 | review: merge |
| `androgénica` | `androgénico` | 89 | review: merge |
| `apostillar` | `apostilla` | 89 | review: merge |
| `comprometiéndose` | `comprometerse` | 89 | review: merge |
| `dejá` | `dejar` | 89 | review: merge |
| `rededor` | `alrededor` | 89 | review: merge |
| `webmasters` | `webmaster` | 89 | review: merge |
| `bichar` | `bicho` | 88 | review: merge |
| `construída` | `construir` | 88 | review: merge |
| `modus` | `modus operandi` | 88 | review: merge |
| `palés` | `palé` | 88 | review: merge |
| `sneakers` | `sneaker` | 88 | review: merge |
| `stickers` | `sticker` | 88 | review: merge |
| `adéntrate` | `adentrarse` | 87 | review: merge |
| `gruesa` | `grueso` | 87 | review: merge |
| `royo` | `roya` | 87 | review: merge |
| `buzar` | `buzo` | 86 | review: merge |
| `folklórico` | `folclórico` | 86 | review: merge |
| `alójese` | `alojarse` | 85 | review: merge |
| `catamar` | `catamarán` | 85 | review: merge |
| `cetogénica` | `cetogénico` | 85 | review: merge |
| `desapegar` | `desapego` | 85 | review: merge |
| `mecanografiar` | `mecanografía` | 85 | review: merge |
| `outfits` | `outfit` | 85 | review: merge |
| `sabés` | `saber` | 85 | review: merge |
| `tertulio` | `tertulia` | 85 | review: merge |
| `carenar` | `carenado` | 84 | review: merge |
| `jacuzzis` | `jacuzzi` | 84 | review: merge |
| `peder` | `pedo` | 84 | review: merge |
| `antiinflamatorios` | `antiinflamatorio` | 83 | review: merge |
| `cubiertar` | `cubierta` | 83 | review: merge |
| `altercar` | `altercado` | 82 | review: merge |
| `plomer` | `plomería` | 82 | review: merge |
| `tarar` | `tara` | 82 | review: merge |
| `cerciórese` | `cerciorarse` | 81 | review: merge |
| `fui` | `ir` | 81 | review: merge |
| `llamadar` | `llamada` | 81 | review: merge |
| `medidar` | `medida` | 81 | review: merge |
| `pósters` | `póster` | 81 | review: merge |
| `repe` | `repeler` | 81 | review: merge |
| `salve` | `salvar` | 81 | review: merge |
| `bellísima` | `bellísimo` | 80 | review: merge |
| `dejarlo` | `dejar` | 80 | review: merge |
| `firewalls` | `firewall` | 80 | review: merge |
| `logs` | `log` | 80 | review: merge |
| `prepagada` | `prepagado` | 80 | review: merge |
| `clicando` | `clicar` | 79 | review: merge |
| `cosquillar` | `cosquillas` | 79 | review: merge |
| `dismiuye` | `disminuir` | 79 | review: merge |
| `electrica` | `eléctrico` | 79 | review: merge |
| `encintar` | `encinta` | 79 | review: merge |
| `fúngicas` | `fúngico` | 79 | review: merge |
| `guárdelo` | `guardar` | 79 | review: merge |
| `solidar` | `sólido` | 79 | review: merge |
| `sáb` | `sábado` | 79 | review: merge |
| `bariátrica` | `bariátrico` | 78 | review: merge |
| `bor` | `borla` | 78 | review: merge |
| `jonrones` | `jonrón` | 78 | review: merge |
| `kármica` | `kármico` | 78 | review: merge |
| `leé` | `leer` | 78 | review: merge |
| `protegiéndolo` | `proteger` | 78 | review: merge |
| `volt` | `voltio` | 78 | review: merge |
| `carillo` | `carilla` | 77 | review: merge |
| `códecs` | `códec` | 77 | review: merge |
| `dese` | `dar` | 77 | review: merge |
| `disfrutá` | `disfrutar` | 77 | review: merge |
| `valiéndose` | `valerse` | 77 | review: merge |
| `mantenlo` | `mantener` | 76 | review: merge |
| `proporcionándole` | `proporcionar` | 76 | review: merge |
| `torrents` | `torrent` | 76 | review: merge |
| `trolls` | `troll` | 76 | review: merge |
| `arcoiris` | `arcoíris` | 75 | review: merge |
| `contrapuntar` | `contrapunto` | 75 | review: merge |
| `electricas` | `eléctrico` | 75 | review: merge |
| `reservá` | `reservar` | 75 | review: merge |
| `toquar` | `tocar` | 75 | review: merge |
| `webinars` | `webinar` | 75 | review: merge |
| `avezar` | `avezado` | 74 | review: merge |
| `carpir` | `carpa` | 74 | review: merge |
| `conecciones` | `conexión` | 74 | review: merge |
| `cotar` | `cota` | 74 | review: merge |
| `engranar` | `engrane` | 74 | review: merge |
| `mampar` | `mampara` | 74 | review: merge |
| `nuesto` | `nuestro` | 74 | review: merge |
| `purpurino` | `purpurina` | 74 | review: merge |
| `chances` | `chance` | 73 | review: merge |
| `metaboliza` | `metabolizar` | 73 | review: merge |
| `tapiar` | `tapia` | 73 | review: merge |
| `workshops` | `workshop` | 73 | review: merge |
| `compasar` | `compás` | 72 | review: merge |
| `eslingar` | `eslinga` | 72 | review: merge |
| `invasiva` | `invasivo` | 72 | review: merge |
| `cierne` | `cernerse` | 71 | review: merge |
| `discrección` | `discreción` | 71 | review: merge |
| `físicar` | `física` | 71 | review: merge |
| `hacedlo` | `hacer` | 71 | review: merge |
| `lucho` | `lucha` | 71 | review: merge |
| `márketing` | `marketing` | 71 | review: merge |
| `videocámar` | `videocámara` | 71 | review: merge |
| `antibacteriana` | `antibacteriano` | 70 | review: merge |
| `antiinflamatoria` | `antiinflamatorio` | 70 | review: merge |
| `cristaler` | `cristalería` | 70 | review: merge |
| `cucar` | `cuco` | 70 | review: merge |
| `desmesurar` | `desmesurado` | 70 | review: merge |
| `feminizada` | `feminizado` | 70 | review: merge |
| `hippy` | `hippie` | 70 | review: merge |
| `oid` | `oír` | 70 | review: merge |
| `estomagar` | `estómago` | 69 | review: merge |
| `família` | `familia` | 69 | review: merge |
| `fuir` | `ir` | 69 | review: merge |
| `minibus` | `minibús` | 69 | review: merge |
| `pizzer` | `pizzería` | 69 | review: merge |
| `encontrá` | `encontrar` | 57 | review: merge |
| `ghetto` | `gueto` | 68 | review: merge |
| `hazle` | `hacer` | 68 | review: merge |
| `importantísima` | `importantísimo` | 68 | review: merge |
| `monitoree` | `monitorear` | 68 | review: merge |
| `muera` | `morir` | 68 | review: merge |
| `vente` | `venirse` | 68 | review: merge |
| `aproximamente` | `aproximadamente` | 67 | review: merge |
| `litografiar` | `litografía` | 67 | review: merge |
| `posteado` | `postear` | 67 | review: merge |
| `secuestrado` | `secuestrar` | 67 | review: merge |
| `abordo` | `a bordo` | 66 | review: merge |
| `acaudalar` | `acaudalado` | 66 | review: merge |
| `contenian` | `contener` | 66 | review: merge |
| `descripto` | `describir` | 66 | review: merge |
| `grillar` | `grilla` | 66 | review: merge |
| `hacerlo` | `hacer` | 66 | review: merge |
| `illustración` | `ilustración` | 66 | review: merge |
| `obten` | `obtener` | 66 | review: merge |
| `porfavor` | `por favor` | 66 | review: merge |
| `baldar` | `balda` | 65 | review: merge |
| `contraído` | `contraer` | 65 | review: merge |
| `contínua` | `continuo` | 65 | review: merge |
| `ingresá` | `ingresar` | 65 | review: merge |
| `macar` | `maca` | 65 | review: merge |
| `acérquese` | `acercarse` | 64 | review: merge |
| `gavillar` | `gavilla` | 64 | review: merge |
| `hipertrofiar` | `hipertrofia` | 64 | review: merge |
| `acidar` | `ácido` | 63 | review: merge |
| `aleatorizados` | `aleatorizar` | 63 | review: merge |
| `carbonar` | `carbón` | 63 | review: merge |
| `compártalo` | `compartir` | 63 | review: merge |
| `corresponderle` | `corresponder` | 63 | review: merge |
| `dejadme` | `dejar` | 63 | review: merge |
| `harmonía` | `armonía` | 50 | review: merge |
| `antibacterianas` | `antibacteriano` | 62 | review: merge |
| `antiinflamatorias` | `antiinflamatorio` | 62 | review: merge |
| `contrapar` | `contraparte` | 62 | review: merge |
| `dadme` | `dar` | 62 | review: merge |
| `danados` | `dañar` | 62 | review: merge |
| `desconéctate` | `desconectarse` | 62 | review: merge |
| `nausear` | `náusea` | 62 | review: merge |
| `percutánea` | `percutáneo` | 62 | review: merge |
| `sociodemográficas` | `sociodemográfico` | 62 | review: merge |
| `sálvame` | `salvar` | 62 | review: merge |
| `tardo` | `tardar` | 62 | review: merge |
| `autocaravanas` | `autocaravana` | 61 | review: merge |
| `créanme` | `creer` | 61 | review: merge |
| `estilismos` | `estilismo` | 61 | review: merge |
| `hosteler` | `hostelería` | 61 | review: merge |
| `hubs` | `hub` | 61 | review: merge |
| `izq` | `izquierda` | 61 | review: merge |
| `manténgalo` | `mantener` | 61 | review: merge |
| `masajea` | `masajear` | 61 | review: merge |
| `restructuración` | `reestructuración` | 61 | review: merge |
| `retenida` | `retener` | 61 | review: merge |
| `seleccioná` | `seleccionar` | 61 | review: merge |
| `déle` | `dar` | 60 | review: merge |
| `diviértase` | `divertirse` | 59 | review: merge |
| `entérese` | `enterarse` | 59 | review: merge |
| `envíelo` | `enviar` | 59 | review: merge |
| `informaciónes` | `información` | 59 | review: merge |
| `tvs` | `tv` | 59 | review: merge |
| `panorámicar` | `panorámica` | 58 | review: merge |
| `routers` | `router` | 58 | review: merge |
| `acogido` | `acoger` | 57 | review: merge |
| `innings` | `inning` | 57 | review: merge |
| `izquierdar` | `izquierda` | 57 | review: merge |
| `posmenopáusicas` | `posmenopáusico` | 57 | review: merge |
| `reinterpreta` | `reinterpretar` | 57 | review: merge |
| `vd` | `usted` | 57 | review: merge |
| `almenar` | `almena` | 56 | review: merge |
| `amplísima` | `amplísimo` | 56 | review: merge |
| `esplender` | `espléndido` | 56 | review: merge |
| `lagrimar` | `lágrima` | 56 | review: merge |
| `perfumer` | `perfumería` | 56 | review: merge |
| `reuniéndose` | `reunirse` | 56 | review: merge |
| `rocio` | `rocío` | 56 | review: merge |
| `ultralenta` | `ultralento` | 56 | review: merge |
| `absortar` | `absorto` | 55 | review: merge |
| `bienvenidar` | `bienvenido` | 55 | review: merge |
| `catálago` | `catálogo` | 55 | review: merge |
| `excrementar` | `excremento` | 55 | review: merge |
| `muffins` | `muffin` | 55 | review: merge |
| `novelar` | `novel` | 55 | review: merge |
| `posters` | `póster` | 55 | review: merge |
| `seleccciones` | `selección` | 55 | review: merge |
| `titulo` | `título` | 55 | review: merge |
| `altísimos` | `altísimo` | 54 | review: merge |
| `bungalós` | `bungaló` | 54 | review: merge |
| `concéntrese` | `concentrarse` | 54 | review: merge |
| `dpto` | `departamento` | 54 | review: merge |
| `empodera` | `empoderar` | 54 | review: merge |
| `esperándote` | `esperar` | 54 | review: merge |
| `figuro` | `figura` | 54 | review: merge |
| `véanse` | `ver` | 54 | review: merge |
| `whiskey` | `whisky` | 54 | review: merge |
| `yihadistas` | `yihadista` | 54 | review: merge |
| `colaborativa` | `colaborativo` | 53 | review: merge |
| `entendiéndose` | `entender` | 53 | review: merge |
| `hachar` | `hacha` | 53 | review: merge |
| `hipoalergénica` | `hipoalergénico` | 53 | review: merge |
| `imagínense` | `imaginarse` | 53 | review: merge |
| `recámar` | `recámara` | 53 | review: merge |
| `teni` | `tener` | 53 | review: merge |
| `arencar` | `arenque` | 52 | review: merge |
| `desarollo` | `desarrollo` | 52 | review: merge |
| `estilosa` | `estiloso` | 52 | review: merge |
| `flexográfica` | `flexográfico` | 52 | review: merge |
| `ictu` | `ictus` | 52 | review: merge |
| `kármicas` | `kármico` | 52 | review: merge |
| `monitorea` | `monitorear` | 52 | review: merge |
| `musicar` | `músico` | 52 | review: merge |
| `perfiladora` | `perfilador` | 52 | review: merge |
| `regulatoria` | `regulatorio` | 52 | review: merge |
| `usario` | `usuario` | 52 | review: merge |
| `apártate` | `apartarse` | 51 | review: merge |
| `armadar` | `armada` | 51 | review: merge |
| `bollar` | `bollo` | 51 | review: merge |
| `cnel` | `coronel` | 51 | review: merge |
| `dura` | `duro` | 51 | review: merge |
| `díselo` | `decir` | 51 | review: merge |
| `embárcate` | `embarcarse` | 51 | review: merge |
| `ferrar` | `fierro` | 51 | review: merge |
| `pequeñita` | `pequeñito` | 51 | review: merge |
| `pormás` | `por más` | 51 | review: merge |
| `péguelo` | `pegar` | 51 | review: merge |
| `reinicie` | `reiniciar` | 51 | review: merge |
| `tarífas` | `tarifa` | 51 | review: merge |
| `agradécele` | `agradecer` | 36 | review: merge |
| `alhajar` | `alhaja` | 50 | review: merge |
| `computarizadas` | `computarizado` | 50 | review: merge |
| `dinos` | `decir` | 50 | review: merge |
| `mismísima` | `mismísimo` | 50 | review: merge |
| `notebooks` | `notebook` | 50 | review: merge |
| `pelis` | `peli` | 50 | review: merge |
| `projecto` | `proyecto` | 50 | review: merge |
| `surfea` | `surfear` | 50 | review: merge |
| `adecue` | `adecuar` | 49 | review: merge |
| `commentario` | `comentario` | 49 | review: merge |
| `deléitese` | `deleitarse` | 49 | review: merge |
| `formadora` | `formador` | 49 | review: merge |
| `playlists` | `playlist` | 49 | review: merge |
| `psicoactivas` | `psicoactivo` | 49 | review: merge |
| `translado` | `traslado` | 49 | review: merge |
| `através` | `a través` | 48 | review: merge |
| `enlistado` | `enlistar` | 48 | review: merge |
| `feminizadas` | `feminizado` | 48 | review: merge |
| `glamurosa` | `glamuroso` | 48 | review: merge |
| `hno` | `hermano` | 48 | review: merge |
| `levántese` | `levantarse` | 48 | review: merge |
| `mostrándote` | `mostrar` | 48 | review: merge |
| `softball` | `sóftbol` | 48 | review: merge |
| `sálvate` | `salvarse` | 48 | review: merge |
| `acuéstate` | `acostarse` | 47 | review: merge |
| `cocino` | `cocina` | 47 | review: merge |
| `dales` | `dar` | 47 | review: merge |
| `deslízate` | `deslizarse` | 47 | review: merge |
| `endechar` | `endecha` | 47 | review: merge |
| `hechor` | `hecho` | 47 | review: merge |
| `hiperenlaces` | `hiperenlace` | 47 | review: merge |
| `multifacética` | `multifacético` | 47 | review: merge |
| `postrer` | `postrero` | 47 | review: merge |
| `redirecciona` | `redireccionar` | 47 | review: merge |
| `semipreciosas` | `semiprecioso` | 47 | review: merge |
| `sintiéndote` | `sentir` | 47 | review: merge |
| `smatphone` | `smartphone` | 47 | review: merge |
| `tenida` | `tener` | 47 | review: merge |
| `texturizada` | `texturizado` | 47 | review: merge |
| `todxs` | `todo` | 47 | review: merge |
| `arrástrelo` | `arrastrar` | 46 | review: merge |
| `añádelo` | `añadir` | 46 | review: merge |
| `bromar` | `bromo` | 46 | review: merge |
| `caricaturar` | `caricatura` | 46 | review: merge |
| `dadle` | `dar` | 46 | review: merge |
| `disenado` | `diseñar` | 46 | review: merge |
| `finar` | `finado` | 46 | review: merge |
| `funcionabilidad` | `funcionalidad` | 46 | review: merge |
| `fín` | `fin` | 46 | review: merge |
| `muchísimos` | `muchísimo` | 46 | review: merge |
| `pensás` | `pensar` | 46 | review: merge |
| `pequena` | `pequeño` | 46 | review: merge |
| `purísima` | `purísimo` | 46 | review: merge |
| `abiertas` | `abierto` | 45 | review: merge |
| `comisariada` | `comisariar` | 45 | review: merge |
| `conocés` | `conocer` | 45 | review: merge |
| `despúes` | `después` | 45 | review: merge |
| `enséñame` | `enseñar` | 45 | review: merge |
| `espíritas` | `espírita` | 45 | review: merge |
| `experiéncia` | `experiencia` | 45 | review: merge |
| `incluídas` | `incluir` | 45 | review: merge |
| `pallets` | `palé` | 45 | review: merge |
| `pruébalo` | `probar` | 45 | review: merge |
| `actualizá` | `actualizar` | 44 | review: merge |
| `bagels` | `bagel` | 44 | review: merge |
| `cliquee` | `cliquear` | 44 | review: merge |
| `cúal` | `cuál` | 44 | review: merge |
| `haciéndolo` | `hacer` | 44 | review: merge |
| `prensadora` | `prensador` | 44 | review: merge |
| `sunnah` | `sunna` | 44 | review: merge |
| `bautizándolo` | `bautizar` | 43 | review: merge |
| `botulínica` | `botulínico` | 43 | review: merge |
| `cardigan` | `cárdigan` | 43 | review: merge |
| `deléitate` | `deleitarse` | 43 | review: merge |
| `extesión` | `extensión` | 43 | review: merge |
| `ponis` | `poni` | 43 | review: merge |
| `reinicia` | `reiniciar` | 43 | review: merge |
| `responsar` | `responso` | 43 | review: merge |
| `sarmentar` | `sarmiento` | 43 | review: merge |
| `vidéo` | `vídeo` | 43 | review: merge |
| `accesso` | `acceso` | 42 | review: merge |
| `amenudo` | `a menudo` | 42 | review: merge |
| `analíticar` | `analítica` | 42 | review: merge |
| `andá` | `andar` | 42 | review: merge |
| `asintomática` | `asintomático` | 42 | review: merge |
| `avda` | `avenida` | 42 | review: merge |
| `bellísimas` | `bello` | 42 | review: merge |
| `deshazte` | `deshacerse` | 42 | review: merge |
| `equipamento` | `equipamiento` | 42 | review: merge |
| `glamouroso` | `glamuroso` | 42 | review: merge |
| `guapísima` | `guapo` | 42 | review: merge |
| `maltear` | `malteada` | 42 | review: merge |
| `modulo` | `módulo` | 42 | review: merge |
| `preoperatoria` | `preoperatorio` | 42 | review: merge |
| `promos` | `promo` | 42 | review: merge |
| `regálate` | `regalar` | 42 | review: merge |
| `vencida` | `vencer` | 42 | review: merge |
| `acordás` | `acordar` | 41 | review: merge |
| `decidme` | `decir` | 41 | review: merge |
| `districto` | `distrito` | 41 | review: merge |
| `estrogénica` | `estrogénico` | 41 | review: merge |
| `glamorosa` | `glamuroso` | 41 | review: merge |
| `iro` | `irse` | 41 | review: merge |
| `jihad` | `yihad` | 41 | review: merge |
| `lechar` | `lechada` | 41 | review: merge |
| `porfolio` | `portafolio` | 41 | review: merge |
| `volúmen` | `volumen` | 41 | review: merge |
| `ópticar` | `óptica` | 41 | review: merge |
| `añadiéndole` | `añadir` | 40 | review: merge |
| `basándome` | `basarse` | 40 | review: merge |
| `bulldozer` | `buldócer` | 40 | review: merge |
| `comentatios` | `comentario` | 40 | review: merge |
| `dur` | `durar` | 40 | review: merge |
| `envíenme` | `enviar` | 40 | review: merge |
| `guardarlo` | `guardar` | 40 | review: merge |
| `indisciplinar` | `indisciplinado` | 40 | review: merge |
| `insolentar` | `insolente` | 40 | review: merge |
| `milimétrica` | `milimétrico` | 40 | review: merge |
| `panty` | `panti` | 40 | review: merge |
| `pasados` | `pasado` | 40 | review: merge |
| `plante` | `plantar` | 40 | review: merge |
| `reproductora` | `reproductor` | 40 | review: merge |
| `abróchate` | `abrocharse` | 39 | review: merge |
| `ammonita` | `amonita` | 39 | review: merge |
| `centellar` | `centella` | 39 | review: merge |
| `grandísima` | `grande` | 39 | review: merge |
| `introdúzca` | `introducir` | 39 | review: merge |
| `mancornar` | `mancuerna` | 39 | review: merge |
| `oponiéndose` | `oponerse` | 39 | review: merge |
| `ranciar` | `rancio` | 39 | review: merge |
| `sintiéndome` | `sentirse` | 39 | review: merge |
| `videollamadas` | `videollamada` | 39 | review: merge |
| `virtualizados` | `virtualizar` | 39 | review: merge |
| `acordao` | `acordarse` | 38 | review: merge |
| `afrutados` | `afrutado` | 38 | review: merge |
| `basándote` | `basarse` | 38 | review: merge |
| `bésame` | `besar` | 38 | review: merge |
| `enséñale` | `enseñar` | 38 | review: merge |
| `intersex` | `intersexual` | 38 | review: merge |
| `introducí` | `introducir` | 38 | review: merge |
| `absténgase` | `abstenerse` | 37 | review: merge |
| `agárrate` | `agarrarse` | 37 | review: merge |
| `amplísimo` | `amplio` | 37 | review: merge |
| `avísenme` | `avisar` | 37 | review: merge |
| `añádele` | `añadir` | 37 | review: merge |
| `bájate` | `bajarse` | 30 | review: merge |
| `conocé` | `conocer` | 37 | review: merge |
| `creedme` | `creer` | 37 | review: merge |
| `esfuérzate` | `esforzarse` | 37 | review: merge |
| `gais` | `gay` | 37 | review: merge |
| `paprika` | `páprika` | 37 | review: merge |
| `preinstaladas` | `preinstalado` | 37 | review: merge |
| `prepárense` | `prepararse` | 37 | review: merge |
| `rappel` | `rápel` | 37 | review: merge |
| `sustituta` | `sustituto` | 37 | review: merge |
| `termográfica` | `termográfico` | 37 | review: merge |
| `tiar` | `tiara` | 37 | review: merge |
| `ajustir` | `ajuste` | 36 | review: merge |
| `caballer` | `caballería` | 36 | review: merge |
| `dad` | `dar` | 36 | review: merge |
| `fíjense` | `fijarse` | 36 | review: merge |
| `hacés` | `hacer` | 36 | review: merge |
| `infrastructura` | `infraestructura` | 36 | review: merge |
| `precancerosas` | `precanceroso` | 36 | review: merge |
| `quintaesenciar` | `quintaesencia` | 36 | review: merge |
| `sinó` | `sino` | 36 | review: merge |
| `vávula` | `válvula` | 36 | review: merge |
| `amadísimos` | `amado` | 35 | review: merge |
| `cuídense` | `cuidarse` | 35 | review: merge |
| `decidle` | `decir` | 35 | review: merge |
| `facilísimo` | `fácil` | 35 | review: merge |
| `flore` | `flor` | 35 | review: merge |
| `fúngica` | `fúngico` | 35 | review: merge |
| `hiperbárica` | `hiperbárico` | 35 | review: merge |
| `huída` | `huida` | 35 | review: merge |
| `manténganse` | `mantenerse` | 35 | review: merge |
| `mesía` | `mesías` | 29 | review: merge |
| `muellir` | `muelle` | 35 | review: merge |
| `octavar` | `octava` | 35 | review: merge |
| `plomar` | `plomada` | 35 | review: merge |
| `pregrabada` | `pregrabado` | 35 | review: merge |
| `sueñar` | `sueño` | 35 | review: merge |
| `cliquea` | `cliquear` | 34 | review: merge |
| `debés` | `deber` | 34 | review: merge |
| `eligir` | `elegir` | 34 | review: merge |
| `espontanear` | `espontáneo` | 34 | review: merge |
| `familiarícese` | `familiarizarse` | 34 | review: merge |
| `húerfano` | `huérfano` | 34 | review: merge |
| `nosotrxs` | `nosotros` | 34 | review: merge |
| `permitidme` | `permitir` | 34 | review: merge |
| `remítase` | `remitirse` | 34 | review: merge |
| `windsurfing` | `windsurf` | 34 | review: merge |
| `úsala` | `usar` | 34 | review: merge |
| `anonimizada` | `anonimizar` | 33 | review: merge |
| `aprovéchese` | `aprovecharse` | 33 | review: merge |
| `artesonar` | `artesonado` | 33 | review: merge |
| `asintomáticas` | `asintomático` | 33 | review: merge |
| `aymar` | `aymara` | 33 | review: merge |
| `ayurvédica` | `ayurvédico` | 33 | review: merge |
| `cerciórate` | `cerciorarse` | 33 | review: merge |
| `daos` | `darse` | 33 | review: merge |
| `descaregar` | `descargar` | 33 | review: merge |
| `ferrys` | `ferri` | 33 | review: merge |
| `fresquita` | `fresquito` | 33 | review: merge |
| `masajee` | `masajear` | 33 | review: merge |
| `millenials` | `milenial` | 33 | review: merge |
| `miocárdica` | `miocárdico` | 33 | review: merge |
| `netbooks` | `netbook` | 33 | review: merge |
| `prononciación` | `pronunciación` | 33 | review: merge |
| `recuéstate` | `recostarse` | 33 | review: merge |
| `salvífica` | `salvífico` | 33 | review: merge |
| `semiáridas` | `semiárido` | 33 | review: merge |
| `valido` | `valer` | 33 | review: merge |
| `ahorrá` | `ahorrar` | 32 | review: merge |
| `asegúrense` | `asegurarse` | 32 | review: merge |
| `clausular` | `cláusula` | 32 | review: merge |
| `computarizados` | `computarizado` | 32 | review: merge |
| `correción` | `corrección` | 32 | review: merge |
| `cristiana` | `cristiano` | 32 | review: merge |
| `decile` | `decir` | 32 | review: merge |
| `dejándola` | `dejar` | 32 | review: merge |
| `escollar` | `escollo` | 32 | review: merge |
| `mantenla` | `mantener` | 32 | review: merge |
| `metabolizan` | `metabolizar` | 32 | review: merge |
| `niéguese` | `negarse` | 32 | review: merge |
| `numerológicas` | `numerológico` | 32 | review: merge |
| `obro` | `obra` | 32 | review: merge |
| `pirater` | `piratería` | 32 | review: merge |
| `prepagadas` | `prepagado` | 32 | review: merge |
| `prémium` | `premium` | 32 | review: merge |
| `quijar` | `quijada` | 32 | review: merge |
| `remítale` | `remitir` | 32 | review: merge |
| `savoir` | `savoir faire` | 32 | review: merge |
| `sujección` | `sujeción` | 32 | review: merge |
| `sáltese` | `saltarse` | 32 | review: merge |
| `són` | `ser` | 32 | review: merge |
| `alegraos` | `alegrarse` | 31 | review: merge |
| `bruzar` | `bruces` | 31 | review: merge |
| `colocándola` | `colocar` | 31 | review: merge |
| `conectándote` | `conectarse` | 31 | review: merge |
| `crayones` | `crayón` | 31 | review: merge |
| `crio` | `criar` | 31 | review: merge |
| `cómprate` | `comprarse` | 31 | review: merge |
| `decimotercer` | `decimotercero` | 31 | review: merge |
| `depués` | `después` | 31 | review: merge |
| `destruído` | `destruir` | 31 | review: merge |
| `determinadar` | `determinado` | 31 | review: merge |
| `dáselo` | `dar` | 31 | review: merge |
| `energizado` | `energizar` | 31 | review: merge |
| `estereotáctica` | `estereotáctico` | 31 | review: merge |
| `extraña` | `extraño` | 31 | review: merge |
| `llamadme` | `llamar` | 31 | review: merge |
| `miente` | `mentir` | 31 | review: merge |
| `poned` | `poner` | 31 | review: merge |
| `preconfigurados` | `preconfigurado` | 31 | review: merge |
| `traillar` | `traílla` | 31 | review: merge |
| `transformándola` | `transformar` | 31 | review: merge |
| `balinesas` | `balinés` | 30 | review: merge |
| `contracto` | `contrato` | 30 | review: merge |
| `coriónica` | `coriónico` | 30 | review: merge |
| `céntrese` | `centrarse` | 30 | review: merge |
| `diclofenac` | `diclofenaco` | 30 | review: merge |
| `dto` | `descuento` | 30 | review: merge |
| `envíar` | `enviar` | 30 | review: merge |
| `identitaria` | `identitario` | 30 | review: merge |
| `inmersivas` | `inmersivo` | 30 | review: merge |
| `mobilidad` | `movilidad` | 30 | review: merge |
| `museística` | `museístico` | 30 | review: merge |
| `operarador` | `operador` | 30 | review: merge |
| `proveído` | `proveer` | 30 | review: merge |
| `sheik` | `jeque` | 30 | review: merge |
| `siguente` | `siguiente` | 30 | review: merge |
| `snowboarding` | `snowboard` | 30 | review: merge |
| `súmate` | `sumarse` | 30 | review: merge |
| `telclado` | `teclado` | 30 | review: merge |
| `aléjese` | `alejarse` | 29 | review: merge |
| `carísimos` | `caro` | 29 | review: merge |
| `ceno` | `cenar` | 29 | review: merge |
| `chillout` | `chill-out` | 29 | review: merge |
| `cúbrase` | `cubrirse` | 29 | review: merge |
| `encuntre` | `encontrar` | 29 | review: merge |
| `enjuáguese` | `enjuagarse` | 29 | review: merge |
| `enséñele` | `enseñar` | 29 | review: merge |
| `entreabierta` | `entreabierto` | 29 | review: merge |
| `entreguerra` | `entreguerras` | 29 | review: merge |
| `escuchadme` | `escuchar` | 29 | review: merge |
| `habito` | `hábito` | 29 | review: merge |
| `inclínate` | `inclinarse` | 29 | review: merge |
| `indicá` | `indicar` | 29 | review: merge |
| `informándole` | `informar` | 29 | review: merge |
| `inmunohistoquímica` | `inmunohistoquímico` | 29 | review: merge |
| `michoacana` | `michoacano` | 29 | review: merge |
| `musculoesqueléticas` | `musculoesquelético` | 29 | review: merge |
| `notifíquenme` | `notificar` | 29 | review: merge |
| `pequeñísima` | `pequeño` | 29 | review: merge |
| `podium` | `podio` | 29 | review: merge |
| `psoriásica` | `psoriásico` | 29 | review: merge |
| `rapidísimo` | `rápido` | 29 | review: merge |
| `regocijaos` | `regocijarse` | 29 | review: merge |
| `remasterizada` | `remasterizar` | 29 | review: merge |
| `termográficas` | `termográfico` | 29 | review: merge |
| `tíralo` | `tirar` | 29 | review: merge |
| `abrázame` | `abrazar` | 20 | review: merge |
| `baluar` | `baluarte` | 28 | review: merge |
| `bioregión` | `biorregión` | 28 | review: merge |
| `compañerxs` | `compañero` | 28 | review: merge |
| `dale` | `dar` | 28 | review: merge |
| `diaconar` | `diaconado` | 28 | review: merge |
| `fontaner` | `fontanería` | 28 | review: merge |
| `fíjese` | `fijarse` | 28 | review: merge |
| `grabados` | `grabado` | 28 | review: merge |
| `habitaciónes` | `habitación` | 28 | review: merge |
| `hematoencefálica` | `hematoencefálico` | 28 | review: merge |
| `hydráulica` | `hidráulico` | 28 | review: merge |
| `ibíd` | `ibídem` | 28 | review: merge |
| `instálelo` | `instalar` | 28 | review: merge |
| `levántense` | `levantarse` | 28 | review: merge |
| `muchisimos` | `muchísimo` | 28 | review: merge |
| `mutatis` | `mutatis mutandis` | 28 | review: merge |
| `objectivo` | `objetivo` | 28 | review: merge |
| `prediseñados` | `prediseñado` | 28 | review: merge |
| `protegerla` | `proteger` | 28 | review: merge |
| `remixes` | `remix` | 28 | review: merge |
| `retroiluminada` | `retroiluminado` | 28 | review: merge |
| `superalimentar` | `superalimento` | 28 | review: merge |
| `tediar` | `tedio` | 28 | review: merge |
| `abducido` | `abducir` | 27 | review: merge |
| `acompáñenos` | `acompañar` | 27 | review: merge |
| `acordaos` | `acordarse` | 27 | review: merge |
| `acuícolas` | `acuícola` | 27 | review: merge |
| `anonimizados` | `anonimizar` | 27 | review: merge |
| `ayduar` | `ayudar` | 27 | review: merge |
| `bacar` | `bacará` | 27 | review: merge |
| `cannábica` | `cannábico` | 27 | review: merge |
| `celiaca` | `celíaco` | 27 | review: merge |
| `compruébelo` | `comprobar` | 27 | review: merge |
| `conserjer` | `conserjería` | 27 | review: merge |
| `contínuamente` | `continuamente` | 27 | review: merge |
| `durísimo` | `duro` | 27 | review: merge |
| `enjuágate` | `enjuagarse` | 27 | review: merge |
| `esper` | `esperar` | 27 | review: merge |
| `exelente` | `excelente` | 27 | review: merge |
| `kilometrar` | `kilómetro` | 27 | review: merge |
| `logueado` | `loguearse` | 27 | review: merge |
| `metalmecánica` | `metalmecánico` | 27 | review: merge |
| `nitrurar` | `nitruro` | 27 | review: merge |
| `objecto` | `objeto` | 27 | review: merge |
| `prevee` | `prever` | 27 | review: merge |
| `redar` | `red` | 27 | review: merge |
| `restraso` | `retraso` | 27 | review: merge |
| `semiestructuradas` | `semiestructurado` | 27 | review: merge |
| `suéltalo` | `soltar` | 27 | review: merge |
| `travez` | `través` | 27 | review: merge |
| `trizar` | `triza` | 27 | review: merge |
| `walkie` | `walkie-talkie` | 27 | review: merge |
| `yodurar` | `yoduro` | 27 | review: merge |
| `úsalo` | `usar` | 27 | review: merge |
| `alelar` | `alelo` | 26 | review: merge |
| `antiquísima` | `antiguo` | 26 | review: merge |
| `bellísimos` | `bello` | 26 | review: merge |
| `bioclimática` | `bioclimático` | 26 | review: merge |
| `brindándole` | `brindar` | 26 | review: merge |
| `compuestar` | `compuesto` | 26 | review: merge |
| `construído` | `construido` | 26 | review: merge |
| `cuídese` | `cuidarse` | 26 | review: merge |
| `descripta` | `describir` | 26 | review: merge |
| `destruída` | `destruido` | 26 | review: merge |
| `documentario` | `documental` | 26 | review: merge |
| `déjala` | `dejar` | 26 | review: merge |
| `dése` | `darse` | 26 | review: merge |
| `energizada` | `energizar` | 26 | review: merge |
| `estambrar` | `estambre` | 26 | review: merge |
| `interesantísimo` | `interesante` | 26 | review: merge |
| `invasivas` | `invasivo` | 26 | review: merge |
| `marketplaces` | `marketplace` | 26 | review: merge |
| `misionario` | `misionero` | 26 | review: merge |
| `morenita` | `moreno` | 26 | review: merge |
| `multiplicaos` | `multiplicarse` | 26 | review: merge |
| `nuevos` | `nuevo` | 26 | review: merge |
| `obsérvese` | `observar` | 26 | review: merge |
| `preconfiguradas` | `preconfigurado` | 26 | review: merge |
| `pónte` | `ponerse` | 26 | review: merge |
| `redirija` | `redirigir` | 26 | review: merge |
| `reintroduzca` | `reintroducir` | 26 | review: merge |
| `sobrescribe` | `sobrescribir` | 26 | review: merge |
| `sumergiéndose` | `sumergirse` | 26 | review: merge |
| `alfarer` | `alfarería` | 25 | review: merge |
| `alguién` | `alguien` | 25 | review: merge |
| `almazar` | `almazara` | 25 | review: merge |
| `añádela` | `añadir` | 25 | review: merge |
| `bautícese` | `bautizar` | 25 | review: merge |
| `biofarmacéutica` | `biofarmacéutico` | 25 | review: merge |
| `centrándose` | `centrarse` | 25 | review: merge |
| `comodísima` | `cómodo` | 25 | review: merge |
| `comprá` | `comprar` | 25 | review: merge |
| `constituyéndose` | `constituirse` | 25 | review: merge |
| `deshágase` | `deshacerse` | 25 | review: merge |
| `divertidísimo` | `divertido` | 25 | review: merge |
| `eliminarlo` | `eliminar` | 25 | review: merge |
| `esforzaos` | `esforzarse` | 25 | review: merge |
| `inspírese` | `inspirarse` | 25 | review: merge |
| `keratina` | `queratina` | 25 | review: merge |
| `larguísimo` | `largo` | 25 | review: merge |
| `madurita` | `maduro` | 25 | review: merge |
| `muestreados` | `muestrear` | 25 | review: merge |
| `noviolenta` | `noviolento` | 25 | review: merge |
| `permitirle` | `permitir` | 25 | review: merge |
| `proprietario` | `propietario` | 25 | review: merge |
| `redirigiendo` | `redirigir` | 25 | review: merge |
| `seminueva` | `seminuevo` | 25 | review: merge |
| `showrooms` | `showroom` | 25 | review: merge |
| `sálvano` | `salvar` | 25 | review: merge |
| `sándwiches` | `sándwich` | 25 | review: merge |
| `tambíen` | `también` | 25 | review: merge |
| `trabajadorxs` | `trabajador` | 25 | review: merge |
| `traedme` | `traer` | 25 | review: merge |
| `triage` | `triaje` | 25 | review: merge |
| `ultraperiféricas` | `ultraperiférico` | 25 | review: merge |
| `vestío` | `vestirse` | 25 | review: merge |
| `virtualizadas` | `virtualizar` | 25 | review: merge |
| `accessorio` | `accesorio` | 24 | review: merge |
| `acuérdese` | `acordarse` | 24 | review: merge |
| `acérquense` | `acercarse` | 24 | review: merge |
| `adio` | `adiós` | 24 | review: merge |
| `aerotransportada` | `aerotransportado` | 24 | review: merge |
| `antinflamatorio` | `antiinflamatorio` | 24 | review: merge |
| `aplícalo` | `aplicar` | 24 | review: merge |
| `arrástralo` | `arrastrar` | 24 | review: merge |
| `asegurándote` | `asegurar` | 24 | review: merge |
| `años` | `año` | 24 | review: merge |
| `balinesa` | `balinés` | 24 | review: merge |
| `bitcóin` | `bitcoin` | 24 | review: merge |
| `colocándolo` | `colocar` | 24 | review: merge |
| `cómprame` | `comprar` | 24 | review: merge |
| `debatar` | `debate` | 24 | review: merge |
| `dinamica` | `dinámica` | 24 | review: merge |
| `felíz` | `feliz` | 24 | review: merge |
| `finísima` | `fino` | 24 | review: merge |
| `hablás` | `hablar` | 24 | review: merge |
| `hemodinámica` | `hemodinámico` | 24 | review: merge |
| `imaginer` | `imaginería` | 24 | review: merge |
| `infanter` | `infantería` | 24 | review: merge |
| `insurreccionar` | `insurrección` | 24 | review: merge |
| `maritimas` | `marítimo` | 24 | review: merge |
| `meningocócica` | `meningocócico` | 24 | review: merge |
| `mielógena` | `mielógeno` | 24 | review: merge |
| `nasogástrica` | `nasogástrico` | 24 | review: merge |
| `naútico` | `náutico` | 24 | review: merge |
| `nuesta` | `nuestro` | 24 | review: merge |
| `oídme` | `oír` | 24 | review: merge |
| `panoramicas` | `panorámico` | 24 | review: merge |
| `particionado` | `particionar` | 24 | review: merge |
| `políticar` | `política` | 24 | review: merge |
| `pontar` | `ponerse` | 24 | review: merge |
| `recatar` | `recato` | 24 | review: merge |
| `repito` | `repetir` | 24 | review: merge |
| `samuráis` | `samurái` | 24 | review: merge |
| `shoppings` | `shopping` | 24 | review: merge |
| `sobrasar` | `sobrasada` | 24 | review: merge |
| `sometiéndose` | `someterse` | 24 | review: merge |
| `tomá` | `tomar` | 24 | review: merge |
| `ámense` | `amar` | 24 | review: merge |
| `éso` | `eso` | 24 | review: merge |
| `adecuen` | `adecuar` | 23 | review: merge |
| `adéntrese` | `adentrarse` | 23 | review: merge |
| `asique` | `así que` | 23 | review: merge |
| `bájese` | `bajarse` | 23 | review: merge |
| `carteler` | `cartelería` | 23 | review: merge |
| `cepíllate` | `cepillarse` | 23 | review: merge |
| `cerchar` | `cercha` | 23 | review: merge |
| `comarcar` | `comarca` | 23 | review: merge |
| `comprarlo` | `comprar` | 23 | review: merge |
| `contribuído` | `contribuido` | 23 | review: merge |
| `conéctor` | `conector` | 23 | review: merge |
| `desarollar` | `desarrollar` | 23 | review: merge |
| `develado` | `develar` | 23 | review: merge |
| `dándote` | `dar` | 23 | review: merge |
| `enlista` | `enlistar` | 23 | review: merge |
| `escúchenme` | `escuchar` | 23 | review: merge |
| `etérica` | `etéreo` | 23 | review: merge |
| `facetados` | `facetado` | 23 | review: merge |
| `famosísima` | `famoso` | 23 | review: merge |
| `finísimo` | `fino` | 23 | review: merge |
| `fuése` | `irse` | 23 | review: merge |
| `gaditas` | `gaditano` | 23 | review: merge |
| `geeks` | `geek` | 23 | review: merge |
| `informaión` | `información` | 23 | review: merge |
| `interaccionan` | `interaccionar` | 23 | review: merge |
| `límpiela` | `limpiar` | 23 | review: merge |
| `milliones` | `millón` | 23 | review: merge |
| `minis` | `mini` | 23 | review: merge |
| `monoinsaturadas` | `monoinsaturado` | 23 | review: merge |
| `muriéndose` | `morirse` | 23 | review: merge |
| `neuropsicológica` | `neuropsicológico` | 23 | review: merge |
| `nostro` | `nosotros` | 23 | review: merge |
| `piénselo` | `pensar` | 23 | review: merge |
| `públicado` | `publicado` | 23 | review: merge |
| `recodar` | `recodo` | 23 | review: merge |
| `reinterpretado` | `reinterpretar` | 23 | review: merge |
| `representaciónes` | `representación` | 23 | review: merge |
| `shéij` | `jeque` | 23 | review: merge |
| `spaghetti` | `espagueti` | 23 | review: merge |
| `sírvanse` | `servirse` | 23 | review: merge |
| `taz` | `taza` | 23 | review: merge |
| `tecnicas` | `técnico` | 23 | review: merge |
| `testeado` | `testear` | 23 | review: merge |
| `triar` | `tríada` | 23 | review: merge |
| `tántrica` | `tántrico` | 23 | review: merge |
| `tírate` | `tirarse` | 23 | review: merge |
| `ultrabaja` | `ultrabajo` | 23 | review: merge |
| `virtualizada` | `virtualizar` | 23 | review: merge |
| `únanse` | `unirse` | 23 | review: merge |
| `abierta` | `abierto` | 22 | review: merge |
| `aburrer` | `aburrido` | 22 | review: merge |
| `albar` | `albarán` | 22 | review: merge |
| `amiotrófica` | `amiotrófico` | 22 | review: merge |
| `auror` | `aurora` | 22 | review: merge |
| `bioenergética` | `bioenergético` | 22 | review: merge |
| `comuniquese` | `comunicarse` | 22 | review: merge |
| `conspirativas` | `conspirativo` | 22 | review: merge |
| `coupage` | `cupaje` | 22 | review: merge |
| `depto` | `departamento` | 22 | review: merge |
| `dialógica` | `dialógico` | 22 | review: merge |
| `dres` | `doctor` | 22 | review: merge |
| `enlistados` | `enlistar` | 22 | review: merge |
| `enséñaselo` | `enseñar` | 22 | review: merge |
| `erotica` | `erótico` | 22 | review: merge |
| `famila` | `familia` | 22 | review: merge |
| `frote` | `frotar` | 22 | review: merge |
| `genómicas` | `genómico` | 22 | review: merge |
| `lasaliana` | `lasaliano` | 22 | review: merge |
| `límpielo` | `limpiar` | 22 | review: merge |
| `medecina` | `medicina` | 22 | review: merge |
| `multiplíquense` | `multiplicarse` | 22 | review: merge |
| `novísimo` | `nuevo` | 22 | review: merge |
| `pedigree` | `pedigrí` | 22 | review: merge |
| `ponchó` | `ponchar` | 22 | review: merge |
| `poniéndote` | `poner` | 22 | review: merge |
| `posbilidad` | `posibilidad` | 22 | review: merge |
| `preinstalada` | `preinstalar` | 22 | review: merge |
| `prepaga` | `prepago` | 22 | review: merge |
| `probá` | `probar` | 22 | review: merge |
| `riffs` | `riff` | 22 | review: merge |
| `ráton` | `ratón` | 22 | review: merge |
| `sotaventar` | `sotavento` | 22 | review: merge |
| `trasparentar` | `trasparente` | 22 | review: merge |
| `weblog` | `blog` | 22 | review: merge |
| `acomódate` | `acomodarse` | 21 | review: merge |
| `adolorida` | `adolorido` | 21 | review: merge |
| `brio` | `brío` | 21 | review: merge |
| `clickea` | `clickear` | 21 | review: merge |
| `cofinanciada` | `cofinanciar` | 21 | review: merge |
| `cojiendo` | `coger` | 21 | review: merge |
| `comúnes` | `común` | 21 | review: merge |
| `contáctese` | `contactar` | 21 | review: merge |
| `cria` | `cría` | 21 | review: merge |
| `dejadlo` | `dejar` | 21 | review: merge |
| `encontar` | `encontrar` | 21 | review: merge |
| `enjuáguelo` | `enjuagar` | 21 | review: merge |
| `esfuércense` | `esforzarse` | 21 | review: merge |
| `evolucionaria` | `evolucionario` | 21 | review: merge |
| `exilar` | `exiliado` | 21 | review: merge |
| `facetada` | `facetado` | 21 | review: merge |
| `finanza` | `finanzas` | 21 | review: merge |
| `firmwar` | `firmware` | 21 | review: merge |
| `fotogáfico` | `fotográfico` | 21 | review: merge |
| `frikis` | `friki` | 21 | review: merge |
| `hadices` | `hadiz` | 21 | review: merge |
| `hipoalergénicas` | `hipoalergénico` | 21 | review: merge |
| `huevar` | `hueva` | 21 | review: merge |
| `huído` | `huido` | 21 | review: merge |
| `identificarlas` | `identificar` | 21 | review: merge |
| `interacciona` | `interaccionar` | 21 | review: merge |
| `intranets` | `intranet` | 21 | review: merge |
| `jameos` | `jameo` | 21 | review: merge |
| `maloláctica` | `maloláctico` | 21 | review: merge |
| `malísimo` | `malo` | 21 | review: merge |
| `masterizado` | `masterizar` | 21 | review: merge |
| `metalica` | `metálico` | 21 | review: merge |
| `microfinanciera` | `microfinanciero` | 21 | review: merge |
| `ministrando` | `ministrar` | 21 | review: merge |
| `nuestrxs` | `nuestro` | 21 | review: merge |
| `permeado` | `permear` | 21 | review: merge |
| `precargadas` | `precargado` | 21 | review: merge |
| `preparaos` | `prepararse` | 21 | review: merge |
| `purpurar` | `púrpura` | 21 | review: merge |
| `pza` | `pieza` | 21 | review: merge |
| `quitándole` | `quitar` | 21 | review: merge |
| `redimensiona` | `redimensionar` | 21 | review: merge |
| `subsanarlo` | `subsanar` | 21 | review: merge |
| `technología` | `tecnología` | 15 | review: merge |
| `uff` | `uf` | 21 | review: merge |
| `utilizá` | `utilizar` | 21 | review: merge |
| `vacar` | `vacada` | 21 | review: merge |
| `voodoo` | `vudú` | 21 | review: merge |
| `abilidad` | `habilidad` | 20 | review: merge |
| `adaptándola` | `adaptar` | 20 | review: merge |
| `adhiriéndose` | `adherirse` | 20 | review: merge |
| `antialérgicas` | `antialérgico` | 20 | review: merge |
| `antiquísimo` | `antiguo` | 20 | review: merge |
| `antocianinas` | `antocianina` | 20 | review: merge |
| `aplíquelo` | `aplicar` | 20 | review: merge |
| `besame` | `besar` | 20 | review: merge |
| `buenísimos` | `bueno` | 20 | review: merge |
| `codeine` | `codeína` | 20 | review: merge |
| `cofinanciados` | `cofinanciar` | 20 | review: merge |
| `dalo` | `dar` | 20 | review: merge |
| `descriptas` | `describir` | 20 | review: merge |
| `empoderando` | `empoderar` | 20 | review: merge |
| `enamórate` | `enamorarse` | 20 | review: merge |
| `energizados` | `energizar` | 20 | review: merge |
| `específicado` | `especificado` | 20 | review: merge |
| `explíqueles` | `explicar` | 20 | review: merge |
| `fanzines` | `fanzine` | 20 | review: merge |
| `habérsele` | `haber` | 20 | review: merge |
| `haciéndola` | `hacer` | 20 | review: merge |
| `hermosísima` | `hermoso` | 20 | review: merge |
| `incorpórese` | `incorporarse` | 20 | review: merge |
| `indizado` | `indizar` | 20 | review: merge |
| `larguísima` | `largo` | 20 | review: merge |
| `linck` | `link` | 20 | review: merge |
| `losar` | `losa` | 20 | review: merge |
| `marrónes` | `marrón` | 20 | review: merge |
| `metida` | `meter` | 20 | review: merge |
| `ministran` | `ministrar` | 20 | review: merge |
| `mixturar` | `mixtura` | 20 | review: merge |
| `multiétnica` | `multiétnico` | 20 | review: merge |
| `sikh` | `sij` | 19 | review: merge |
| `socio-ambiental` | `socioambiental` | 19 | review: merge |
| `standar` | `estándar` | 19 | review: merge |
| `triathlon` | `triatlón` | 19 | review: merge |
| `apoyarno` | `apoyar` | 18 | review: merge |
| `auto-evaluación` | `autoevaluación` | 18 | review: merge |
| `auto-servicio` | `autoservicio` | 18 | review: merge |
| `autobúse` | `autobús` | 18 | review: merge |
| `bisuteria` | `bisutería` | 18 | review: merge |
| `chi-cuadrado` | `chi cuadrado` | 18 | review: merge |
| `contraofensivo` | `contraofensiva` | 18 | review: merge |
| `culinaria` | `culinario` | 18 | review: merge |
| `disconfor` | `disconforme` | 18 | review: merge |
| `dándono` | `dar` | 18 | review: merge |
| `ex-alumno` | `exalumno` | 18 | review: merge |
| `explicarl` | `explicar` | 18 | review: merge |
| `fintechs` | `fintech` | 18 | review: merge |
| `monástica` | `monástico` | 18 | review: merge |
| `muggl` | `muggle` | 18 | review: merge |
| `multi-capa` | `multicapa` | 18 | review: merge |
| `multi-color` | `multicolor` | 18 | review: merge |
| `nupcia` | `nupcias` | 18 | review: merge |
| `optimal` | `óptimo` | 18 | review: merge |
| `penthous` | `penthouse` | 18 | review: merge |
| `permitirno` | `permitir` | 18 | review: merge |
| `post-conflicto` | `posconflicto` | 18 | review: merge |
| `praxi` | `praxis` | 18 | review: merge |
| `pre-instalación#hunt` | `preinstalación` | 18 | review: merge |
| `pre-pago` | `prepago` | 18 | review: merge |
| `pregúntal` | `preguntar` | 18 | review: merge |
| `proporcionándono` | `proporcionar` | 18 | review: merge |
| `psico-social` | `psicosocial` | 18 | review: merge |
| `puños` | `puño` | 18 | review: merge |
| `re-edición` | `reedición` | 18 | review: merge |
| `rias` | `ría` | 18 | review: merge |
| `socio-económicas` | `socioeconómico` | 18 | review: merge |
| `stakeholders` | `stakeholder` | 18 | review: merge |
| `ultra-delgado` | `ultradelgado` | 18 | review: merge |
| `vaping` | `vapeo` | 18 | review: merge |
| `vigila` | `vigilar` | 18 | review: merge |
| `acompáñeno` | `acompañar` | 17 | review: merge |
| `amémono` | `amar` | 17 | review: merge |
| `anti-estrógeno` | `antiestrógeno` | 17 | review: merge |
| `apoyarl` | `apoyar` | 17 | review: merge |
| `arq` | `arquitecto` | 17 | review: merge |
| `auto-control` | `autocontrol` | 17 | review: merge |
| `auto-estima` | `autoestima` | 17 | review: merge |
| `autoalineabl` | `autoalineable` | 17 | review: merge |
| `bebed` | `beber` | 17 | review: merge |
| `berber` | `bereber` | 17 | review: merge |
| `calefactabl` | `calefactable` | 17 | review: merge |
| `carraco` | `carraca` | 17 | review: merge |
| `co-pago` | `copago` | 17 | review: merge |
| `consecuentes` | `consecuente` | 17 | review: merge |
| `cruza` | `cruzar` | 17 | review: merge |
| `cucharadit#Maac` | `cucharadita` | 17 | review: merge |
| `despojarno` | `despojar` | 17 | review: merge |
| `dirigirno` | `dirigir` | 17 | review: merge |
| `fisica` | `física` | 17 | review: merge |
| `garantizarl` | `garantizar` | 17 | review: merge |
| `hashe` | `hash` | 17 | review: merge |
| `influencers` | `influencer` | 17 | review: merge |
| `informacióne` | `información` | 17 | review: merge |
| `jesu` | `jesús` | 17 | review: merge |
| `jovene` | `joven` | 17 | review: merge |
| `lanzacohete` | `lanzacohetes` | 17 | review: merge |
| `licenciantes` | `licenciante` | 17 | review: merge |
| `llevándol` | `llevar` | 17 | review: merge |
| `oxímor` | `oxímoron` | 17 | review: merge |
| `parótido` | `parótida` | 17 | review: merge |
| `pic-nic` | `picnic` | 17 | review: merge |
| `ponero` | `poner` | 17 | review: merge |
| `sintiéndono` | `sentirse` | 17 | review: merge |
| `socio-política` | `sociopolítico` | 17 | review: merge |
| `testers` | `tester` | 17 | review: merge |
| `tupper` | `táper` | 17 | review: merge |
| `utilizadore` | `utilizador` | 17 | review: merge |
| `acerquémono` | `acercarse` | 16 | review: merge |
| `anti-corrupción` | `anticorrupción` | 16 | review: merge |
| `anti-robo` | `antirrobo` | 16 | review: merge |
| `arrepiéntanse` | `arrepentirse` | 16 | review: merge |
| `auto-expresión` | `autoexpresión` | 16 | review: merge |
| `depilada` | `depilado` | 16 | review: merge |
| `dígal` | `decir` | 16 | review: merge |
| `educa` | `educar` | 16 | review: merge |
| `encontr` | `encontrar` | 16 | review: merge |
| `esforzándo` | `esforzarse` | 16 | review: merge |
| `esperad` | `esperar` | 16 | review: merge |
| `galeon` | `galeón` | 16 | review: merge |
| `guiándo` | `guiar` | 16 | review: merge |
| `implantabl` | `implantable` | 16 | review: merge |
| `lanzamisil` | `lanzamisiles` | 16 | review: merge |
| `lapsu` | `lapsus` | 16 | review: merge |
| `londr` | `londres` | 16 | review: merge |
| `macrame` | `macramé` | 16 | review: merge |
| `mandarl` | `mandar` | 16 | review: merge |
| `manteneo` | `mantenerse` | 16 | review: merge |
| `nosostro` | `nosotros` | 16 | review: merge |
| `notifíqueno` | `notificar` | 16 | review: merge |
| `okay` | `okey` | 16 | review: merge |
| `pagarl` | `pagar` | 16 | review: merge |
| `post-traumático` | `postraumático` | 16 | review: merge |
| `provea` | `proveer` | 16 | review: merge |
| `puedr` | `poder` | 16 | review: merge |
| `rompeola` | `rompeolas` | 16 | review: merge |
| `semi-nuevo` | `seminuevo` | 16 | review: merge |
| `suministrarl` | `suministrar` | 16 | review: merge |
| `anti-arruga` | `antiarrugas` | 15 | review: merge |
| `aros` | `aro` | 15 | review: merge |
| `arrepentirno` | `arrepentirse` | 15 | review: merge |
| `auto-determinación` | `autodeterminación` | 15 | review: merge |
| `añadiéndol` | `añadir` | 15 | review: merge |
| `confetti` | `confeti` | 15 | review: merge |
| `confíen` | `confiar` | 15 | review: merge |
| `contactado` | `contactar` | 15 | review: merge |
| `contáctanos` | `contactar` | 15 | review: merge |
| `crean` | `crear` | 15 | review: merge |
| `dejándono` | `dejar` | 15 | review: merge |
| `despertarno` | `despertarse` | 15 | review: merge |
| `halar` | `halo` | 325 | review: merge |
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
| `comodo` | `cómodo` | 256 | accented spelling 22,248 vs 256 |
| `lopez` | `lópez` | 240 | accented spelling 2,366 vs 240 |
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
| `osea` | `óseo` | 57 | accented spelling 565 vs 57 |
| `edicion` | `edición` | 57 | accented spelling 18,773 vs 57 |
| `fundacion` | `fundación` | 56 | accented spelling 13,860 vs 56 |
| `mejoro` | `mejorar` | 56 | accented spelling 437 vs 56 |
| `amen` | `amén` | 56 | accented spelling 521 vs 56 |
| `grafica` | `gráfica` | 56 | accented spelling 3,788 vs 56 |
| `sinai` | `sinaí` | 56 | accented spelling 732 vs 56 |
| `parana` | `paraná` | 56 | accented spelling 330 vs 56 |
| `inversion` | `inversión` | 56 | accented spelling 21,271 vs 56 |
| `turisticas` | `turístico` | 55 | accented spelling 1,663 vs 55 |
| `suarez` | `suárez` | 55 | accented spelling 570 vs 55 |
| `pajaro` | `pájaro` | 55 | accented spelling 3,637 vs 55 |
| `culiacan` | `culiacán` | 54 | accented spelling 282 vs 54 |
| `metodo` | `método` | 54 | accented spelling 27,865 vs 54 |
| `cajon` | `cajón` | 54 | accented spelling 2,370 vs 54 |
| `ayudo` | `ayudar` | 54 | accented spelling 1,846 vs 54 |
| `investigacion` | `investigación` | 53 | accented spelling 49,114 vs 53 |
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
| `tripoli` | `trípoli` | 43 | accented spelling 248 vs 43 |
| `cañon` | `cañón` | 43 | accented spelling 3,132 vs 43 |
| `barcelo` | `barceló` | 43 | accented spelling 446 vs 43 |
| `direccion` | `dirección` | 43 | accented spelling 64,258 vs 43 |
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
| `registrese` | `registrarse` | 20 | accented spelling 2,120 vs 20 |
| `sandia` | `sandía` | 20 | accented spelling 426 vs 20 |
| `comercializacion` | `comercialización` | 20 | accented spelling 4,743 vs 20 |
| `explosion` | `explosión` | 20 | accented spelling 3,390 vs 20 |
| `libero` | `liberar` | 20 | accented spelling 142 vs 20 |
| `operacion` | `operación` | 20 | accented spelling 27,506 vs 20 |
| `cancelacion` | `cancelación` | 20 | accented spelling 6,812 vs 20 |
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
| `fijacion` | `fijación` | 17 | accented spelling 3,753 vs 17 |
| `interpretacion` | `interpretación` | 17 | accented spelling 6,812 vs 17 |
| `energetico` | `energético` | 17 | accented spelling 7,212 vs 17 |
| `rabi` | `rabí` | 17 | accented spelling 263 vs 17 |
| `vereis` | `ver` | 17 | accented spelling 279 vs 17 |
| `llameno` | `llamar` | 17 | accented spelling 104 vs 17 |
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
| `cesareo` | `cesárea` | 14 | accented spelling 244 vs 14 |
| `electricos` | `eléctrico` | 14 | accented spelling 3,312 vs 14 |
| `excepcion` | `excepción` | 14 | accented spelling 7,115 vs 14 |
| `nutricion` | `nutrición` | 14 | accented spelling 5,386 vs 14 |
| `olimpica` | `olímpico` | 14 | accented spelling 246 vs 14 |
| `inclusion` | `inclusión` | 14 | accented spelling 5,170 vs 14 |
| `debia` | `deber` | 14 | accented spelling 2,025 vs 14 |
| `deberias` | `deber` | 14 | accented spelling 3,063 vs 14 |
| `atlantida` | `atlántida` | 14 | accented spelling 248 vs 14 |
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
| `agradecele` | `agradecer` | 14 | accented spelling 72 vs 14 |
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
| `harmonia` | `armonía` | 13 | accented spelling 95 vs 13 |
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
| `tuiteo` | `tuitear` | 13 | accented spelling 210 vs 13 |
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
| `suscribase` | `suscribirse` | 12 | accented spelling 1,456 vs 12 |
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
| `relajate` | `relajarse` | 11 | accented spelling 608 vs 11 |
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
| `encontra` | `encontrar` | 11 | accented spelling 114 vs 11 |
| `baston` | `bastón` | 11 | accented spelling 830 vs 11 |
| `documentacion` | `documentación` | 11 | accented spelling 7,983 vs 11 |
| `regimenes` | `régimen` | 11 | accented spelling 668 vs 11 |
| `canale` | `canalé` | 11 | accented spelling 122 vs 11 |
| `ningun` | `ninguno` | 11 | accented spelling 22,796 vs 11 |
| `heroismo` | `heroísmo` | 11 | accented spelling 264 vs 11 |
| `veia` | `ver` | 11 | accented spelling 1,072 vs 11 |
| `visualizacion` | `visualización` | 11 | accented spelling 5,974 vs 11 |
| `creyo` | `creer` | 11 | accented spelling 434 vs 11 |
| `sanguineo` | `sanguíneo` | 11 | accented spelling 3,369 vs 11 |
| `eter` | `éter` | 11 | accented spelling 285 vs 11 |
| `parecio` | `parecer` | 11 | accented spelling 1,122 vs 11 |
| `vasquez` | `vásquez` | 11 | accented spelling 200 vs 11 |
| `junin` | `junín` | 11 | accented spelling 122 vs 11 |
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
| `imaginate` | `imaginarse` | 11 | accented spelling 354 vs 11 |
| `queriamos` | `querer` | 11 | accented spelling 759 vs 11 |
| `cehegin` | `cehegín` | 11 | accented spelling 78 vs 11 |
| `propulsion` | `propulsión` | 11 | accented spelling 693 vs 11 |
| `griferia` | `grifería` | 11 | accented spelling 450 vs 11 |
| `persecucion` | `persecución` | 11 | accented spelling 2,454 vs 11 |
| `ofrecio` | `ofrecer` | 11 | accented spelling 1,118 vs 11 |
| `fertil` | `fértil` | 11 | accented spelling 916 vs 11 |
| `divan` | `diván` | 11 | accented spelling 118 vs 11 |
| `alumina` | `alúmina` | 11 | accented spelling 107 vs 11 |
| `auna` | `aunar` | 11 | accented spelling 122 vs 11 |
| `acepto` | `aceptar` | 11 | accented spelling 772 vs 11 |
| `septima` | `séptimo` | 11 | accented spelling 526 vs 11 |
| `platano` | `plátano` | 11 | accented spelling 1,428 vs 11 |
| `alla` | `allá` | 11 | accented spelling 19,864 vs 11 |
| `galactica` | `galáctico` | 11 | accented spelling 232 vs 11 |
| `espia` | `espía` | 11 | accented spelling 886 vs 11 |
| `confirmacion` | `confirmación` | 11 | accented spelling 7,367 vs 11 |
| `callejon` | `callejón` | 11 | accented spelling 903 vs 11 |
| `cupula` | `cúpula` | 11 | accented spelling 1,275 vs 11 |
| `instantanea` | `instantáneo` | 11 | accented spelling 1,256 vs 11 |
| `remodelacion` | `remodelación` | 11 | accented spelling 795 vs 11 |
| `convertira` | `convertir` | 11 | accented spelling 794 vs 11 |
| `encia` | `encía` | 11 | accented spelling 909 vs 11 |
| `enfermeria` | `enfermería` | 11 | accented spelling 2,271 vs 11 |
| `segui` | `seguir` | 11 | accented spelling 251 vs 11 |
| `moreton` | `moretón` | 11 | accented spelling 190 vs 11 |
| `insolito` | `insólito` | 11 | accented spelling 344 vs 11 |
| `lineas` | `línea` | 11 | accented spelling 9,680 vs 11 |
| `fermin` | `fermín` | 11 | accented spelling 170 vs 11 |
| `preocupacion` | `preocupación` | 11 | accented spelling 8,067 vs 11 |
| `mios` | `mío` | 10 | accented spelling 971 vs 10 |
| `psicologico` | `psicológico` | 10 | accented spelling 2,574 vs 10 |
| `alienigena` | `alienígena` | 10 | accented spelling 725 vs 10 |
| `habiamos` | `haber` | 10 | accented spelling 993 vs 10 |
| `corporacion` | `corporación` | 10 | accented spelling 2,694 vs 10 |
| `revelacion` | `revelación` | 10 | accented spelling 3,039 vs 10 |
| `prestacion` | `prestación` | 10 | accented spelling 7,013 vs 10 |
| `cancerigenas` | `cancerígeno` | 10 | accented spelling 125 vs 10 |
| `extraccion` | `extracción` | 10 | accented spelling 4,445 vs 10 |
| `corrupcion` | `corrupción` | 10 | accented spelling 4,451 vs 10 |
| `projimo` | `prójimo` | 10 | accented spelling 1,758 vs 10 |
| `tetuan` | `tetuán` | 10 | accented spelling 140 vs 10 |
| `roldan` | `roldán` | 10 | accented spelling 94 vs 10 |
| `proporcion` | `proporción` | 10 | accented spelling 5,019 vs 10 |
| `deficit` | `déficit` | 10 | accented spelling 2,126 vs 10 |
| `arcangel` | `arcángel` | 10 | accented spelling 414 vs 10 |
| `alqueria` | `alquería` | 10 | accented spelling 56 vs 10 |
| `recibi` | `recibir` | 10 | accented spelling 780 vs 10 |
| `manipulacion` | `manipulación` | 10 | accented spelling 3,521 vs 10 |
| `platon` | `platón` | 10 | accented spelling 344 vs 10 |
| `siguio` | `seguir` | 10 | accented spelling 1,625 vs 10 |
| `satisfaccion` | `satisfacción` | 10 | accented spelling 7,613 vs 10 |
| `magnifica` | `magnífico` | 10 | accented spelling 1,945 vs 10 |
| `cerrajeria` | `cerrajería` | 10 | accented spelling 134 vs 10 |
| `gastronomico` | `gastronómico` | 10 | accented spelling 2,131 vs 10 |
| `comodos` | `cómodo` | 10 | accented spelling 1,614 vs 10 |
| `aceleracion` | `aceleración` | 10 | accented spelling 2,040 vs 10 |
| `jardin` | `jardín` | 10 | accented spelling 33,427 vs 10 |
| `civico` | `cívico` | 10 | accented spelling 906 vs 10 |
| `yasuni` | `yasuní` | 10 | accented spelling 58 vs 10 |
| `abri` | `abrir` | 10 | accented spelling 193 vs 10 |
| `tacita` | `tácito` | 10 | accented spelling 56 vs 10 |
| `exportacion` | `exportación` | 10 | accented spelling 8,591 vs 10 |
| `busquedas` | `búsqueda` | 10 | accented spelling 2,883 vs 10 |
| `iberico` | `ibérico` | 10 | accented spelling 1,064 vs 10 |
| `podra` | `poder` | 10 | accented spelling 19,625 vs 10 |
| `arnes` | `arnés` | 10 | accented spelling 901 vs 10 |
| `orquideas` | `orquídea` | 10 | accented spelling 204 vs 10 |
| `marron` | `marrón` | 10 | accented spelling 3,858 vs 10 |
| `tabernaculo` | `tabernáculo` | 10 | accented spelling 1,808 vs 10 |
| `pasion` | `pasión` | 10 | accented spelling 8,079 vs 10 |
| `ideo` | `idear` | 10 | accented spelling 54 vs 10 |
| `juridica` | `jurídico` | 10 | accented spelling 1,735 vs 10 |
| `exotico` | `exótico` | 10 | accented spelling 1,524 vs 10 |
| `legislacion` | `legislación` | 10 | accented spelling 9,907 vs 10 |
| `parasito` | `parásito` | 10 | accented spelling 846 vs 10 |
| `sintomas` | `síntoma` | 10 | accented spelling 9,395 vs 10 |
| `menciono` | `mencionar` | 10 | accented spelling 793 vs 10 |
| `anibal` | `aníbal` | 10 | accented spelling 146 vs 10 |
| `pate` | `paté` | 10 | accented spelling 123 vs 10 |
| `pucon` | `pucón` | 10 | accented spelling 188 vs 10 |
| `atletica` | `atlético` | 10 | accented spelling 91 vs 10 |
| `botin` | `botín` | 10 | accented spelling 1,165 vs 10 |
| `jalon` | `jalón` | 10 | accented spelling 90 vs 10 |
| `olvideis` | `olvidar` | 10 | accented spelling 119 vs 10 |
| `colchon` | `colchón` | 10 | accented spelling 2,357 vs 10 |
| `explicitamente` | `explícitamente` | 10 | accented spelling 1,144 vs 10 |
| `biceps` | `bíceps` | 10 | accented spelling 176 vs 10 |
| `guarderia` | `guardería` | 10 | accented spelling 1,637 vs 10 |
| `fotografa` | `fotógrafa` | 10 | accented spelling 396 vs 10 |
| `meti` | `meter` | 10 | accented spelling 69 vs 10 |
| `autorizacion` | `autorización` | 10 | accented spelling 7,701 vs 10 |
| `afrodisiaco` | `afrodisíaco` | 10 | accented spelling 132 vs 10 |
| `anticipacion` | `anticipación` | 10 | accented spelling 5,057 vs 10 |
| `subcategoria` | `subcategoría` | 10 | accented spelling 374 vs 10 |
| `mostoles` | `móstoles` | 10 | accented spelling 132 vs 10 |
| `climatico` | `climático` | 10 | accented spelling 3,290 vs 10 |
| `retencion` | `retención` | 10 | accented spelling 4,150 vs 10 |
| `amazonico` | `amazónico` | 10 | accented spelling 400 vs 10 |
| `abadia` | `abadía` | 10 | accented spelling 858 vs 10 |
| `jabon` | `jabón` | 10 | accented spelling 3,643 vs 10 |
| `podrias` | `poder` | 10 | accented spelling 2,282 vs 10 |
| `biologia` | `biología` | 10 | accented spelling 2,053 vs 10 |
| `ejecucion` | `ejecución` | 10 | accented spelling 12,499 vs 10 |
| `matara` | `matar` | 10 | accented spelling 123 vs 10 |
| `transportacion` | `transportación` | 10 | accented spelling 588 vs 10 |
| `limites` | `límite` | 10 | accented spelling 4,901 vs 10 |
| `cantico` | `cántico` | 10 | accented spelling 344 vs 10 |
| `colocacion` | `colocación` | 10 | accented spelling 3,512 vs 10 |
| `solia` | `soler` | 10 | accented spelling 1,466 vs 10 |
| `diogenes` | `diógenes` | 10 | accented spelling 58 vs 10 |
| `caloria` | `caloría` | 10 | accented spelling 2,316 vs 10 |
| `homilia` | `homilía` | 10 | accented spelling 466 vs 10 |
| `prision` | `prisión` | 10 | accented spelling 5,174 vs 10 |
| `exclusion` | `exclusión` | 10 | accented spelling 3,202 vs 10 |
| `camboriu` | `camboriú` | 10 | accented spelling 54 vs 10 |
| `curcuma` | `cúrcuma` | 10 | accented spelling 334 vs 10 |
| `tiburon` | `tiburón` | 10 | accented spelling 1,222 vs 10 |
| `turo` | `turó` | 10 | accented spelling 62 vs 10 |
| `penetracion` | `penetración` | 10 | accented spelling 1,633 vs 10 |
| `podiamos` | `poder` | 10 | accented spelling 537 vs 10 |
| `comio` | `comer` | 10 | accented spelling 587 vs 10 |
| `estaran` | `estar` | 10 | accented spelling 3,782 vs 10 |
| `limitacion` | `limitación` | 10 | accented spelling 7,230 vs 10 |
| `traera` | `traer` | 10 | accented spelling 593 vs 10 |
| `polimero` | `polímero` | 10 | accented spelling 1,484 vs 10 |
| `sabra` | `saber` | 10 | accented spelling 556 vs 10 |
| `lerida` | `lérida` | 10 | accented spelling 104 vs 10 |
| `eloisa` | `eloísa` | 10 | accented spelling 56 vs 10 |
| `veria` | `ver` | 10 | accented spelling 199 vs 10 |
| `mancora` | `máncora` | 10 | accented spelling 78 vs 10 |
| `telefonia` | `telefonía` | 10 | accented spelling 2,438 vs 10 |
| `alimentacion` | `alimentación` | 10 | accented spelling 19,936 vs 10 |
| `caiman` | `caimán` | 10 | accented spelling 819 vs 10 |
| `termometro` | `termómetro` | 10 | accented spelling 1,183 vs 10 |
| `medicamente` | `médicamente` | 10 | accented spelling 244 vs 10 |
| `eslabon` | `eslabón` | 10 | accented spelling 522 vs 10 |
| `garantias` | `garantía` | 10 | accented spelling 2,814 vs 10 |
| `melendez` | `meléndez` | 10 | accented spelling 68 vs 10 |
| `envianos` | `enviar` | 10 | accented spelling 527 vs 10 |
| `astrologia` | `astrología` | 10 | accented spelling 890 vs 10 |
| `coyoacan` | `coyoacán` | 10 | accented spelling 112 vs 10 |
| `aprobacion` | `aprobación` | 10 | accented spelling 7,187 vs 10 |
| `alora` | `álora` | 9 | accented spelling 46 vs 9 |
| `tipica` | `típico` | 9 | accented spelling 1,343 vs 9 |
| `protegera` | `proteger` | 9 | accented spelling 237 vs 9 |
| `mispa` | `mispá` | 9 | accented spelling 70 vs 9 |
| `buzon` | `buzón` | 9 | accented spelling 1,888 vs 9 |
| `aparecio` | `aparecer` | 9 | accented spelling 1,841 vs 9 |
| `araucania` | `araucanía` | 9 | accented spelling 94 vs 9 |
| `estuvieramos` | `estar` | 9 | accented spelling 113 vs 9 |
| `caia` | `caer` | 9 | accented spelling 182 vs 9 |
| `atraido` | `atraer` | 9 | accented spelling 444 vs 9 |
| `lipolisis` | `lipólisis` | 9 | accented spelling 82 vs 9 |
| `colera` | `cólera#Masc` | 9 | accented spelling 842 vs 9 |
| `extraidos` | `extraer` | 9 | accented spelling 215 vs 9 |
| `campeon` | `campeón` | 9 | accented spelling 3,994 vs 9 |
| `apurimac` | `apurímac` | 9 | accented spelling 70 vs 9 |
| `toco` | `tocar` | 9 | accented spelling 768 vs 9 |
| `parametro` | `parámetro` | 9 | accented spelling 6,551 vs 9 |
| `tacon` | `tacón` | 9 | accented spelling 1,475 vs 9 |
| `bendicion` | `bendición` | 9 | accented spelling 3,931 vs 9 |
| `osnabruck` | `osnabrück` | 9 | accented spelling 58 vs 9 |
| `implementacion` | `implementación` | 9 | accented spelling 9,525 vs 9 |
| `guio` | `guiar` | 9 | accented spelling 127 vs 9 |
| `adis` | `adís` | 9 | accented spelling 600 vs 9 |
| `perdi` | `perder` | 9 | accented spelling 540 vs 9 |
| `erevan` | `ereván` | 9 | accented spelling 276 vs 9 |
| `llamano` | `llamar` | 9 | accented spelling 94 vs 9 |
| `agradeceria` | `agradecer` | 9 | accented spelling 85 vs 9 |
| `mistico` | `místico` | 9 | accented spelling 893 vs 9 |
| `pelicano` | `pelícano` | 9 | accented spelling 109 vs 9 |
| `pinto` | `pintar` | 9 | accented spelling 222 vs 9 |
| `futbolin` | `futbolín` | 9 | accented spelling 166 vs 9 |
| `extrusion` | `extrusión` | 9 | accented spelling 932 vs 9 |
| `frio-calor` | `frío-calor` | 9 | accented spelling 70 vs 9 |
| `refierase` | `referirse` | 9 | accented spelling 234 vs 9 |
| `permitio` | `permitir` | 9 | accented spelling 2,179 vs 9 |
| `zoologico` | `zoológico` | 9 | accented spelling 1,530 vs 9 |
| `artistica` | `artístico` | 9 | accented spelling 1,546 vs 9 |
| `tecnologica` | `tecnológico` | 9 | accented spelling 1,791 vs 9 |
| `heroina` | `heroína` | 9 | accented spelling 777 vs 9 |
| `odontologia` | `odontología` | 9 | accented spelling 928 vs 9 |
| `envios` | `envío` | 9 | accented spelling 2,763 vs 9 |
| `esteli` | `estelí` | 9 | accented spelling 70 vs 9 |
| `hepatica` | `hepático` | 9 | accented spelling 536 vs 9 |
| `natan` | `natán` | 9 | accented spelling 260 vs 9 |
| `anulacion` | `anulación` | 9 | accented spelling 1,016 vs 9 |
| `envien` | `enviar` | 9 | accented spelling 413 vs 9 |
| `ocupacion` | `ocupación` | 9 | accented spelling 4,067 vs 9 |
| `motivacion` | `motivación` | 9 | accented spelling 3,297 vs 9 |
| `tactil` | `táctil` | 9 | accented spelling 4,507 vs 9 |
| `darsena` | `dársena` | 9 | accented spelling 70 vs 9 |
| `clasicas` | `clásico` | 9 | accented spelling 851 vs 9 |
| `golpeo` | `golpear` | 9 | accented spelling 510 vs 9 |
| `simulacion` | `simulación` | 9 | accented spelling 3,175 vs 9 |
| `biogas` | `biogás` | 9 | accented spelling 403 vs 9 |
| `egoista` | `egoísta` | 9 | accented spelling 1,029 vs 9 |
| `proximos` | `próximo` | 9 | accented spelling 6,416 vs 9 |
| `federacion` | `federación` | 9 | accented spelling 4,307 vs 9 |
| `negueb` | `négueb` | 9 | accented spelling 54 vs 9 |
| `telefonicas` | `telefónico` | 9 | accented spelling 855 vs 9 |
| `perdio` | `perder` | 9 | accented spelling 1,726 vs 9 |
| `broto` | `brotar` | 9 | accented spelling 60 vs 9 |
| `jamas` | `jamás` | 9 | accented spelling 7,806 vs 9 |
| `cosmetico` | `cosmético` | 9 | accented spelling 3,108 vs 9 |
| `concentracion` | `concentración` | 9 | accented spelling 6,809 vs 9 |
| `cafeteria` | `cafetería` | 9 | accented spelling 4,378 vs 9 |
| `anonimo` | `anónimo` | 9 | accented spelling 3,801 vs 9 |
| `teologia` | `teología` | 9 | accented spelling 1,343 vs 9 |
| `volveran` | `volver` | 9 | accented spelling 411 vs 9 |
| `terminacion` | `terminación` | 9 | accented spelling 2,212 vs 9 |
| `regulacion` | `regulación` | 9 | accented spelling 6,133 vs 9 |
| `primogenito` | `primogénito` | 9 | accented spelling 1,036 vs 9 |
| `arcon` | `arcón` | 9 | accented spelling 65 vs 9 |
| `deberiamos` | `deber` | 9 | accented spelling 1,480 vs 9 |
| `miquelon` | `miquelón` | 9 | accented spelling 72 vs 9 |
| `transicion` | `transición` | 9 | accented spelling 6,207 vs 9 |
| `vigia` | `vigía` | 9 | accented spelling 51 vs 9 |
| `mataro` | `mataró` | 9 | accented spelling 226 vs 9 |
| `bazan` | `bazán` | 9 | accented spelling 50 vs 9 |
| `examenes` | `examen` | 9 | accented spelling 2,924 vs 9 |
| `comi` | `comer` | 9 | accented spelling 310 vs 9 |
| `violacion` | `violación` | 9 | accented spelling 7,670 vs 9 |
| `gimenez` | `giménez` | 9 | accented spelling 124 vs 9 |
| `telefonos` | `teléfono` | 9 | accented spelling 4,736 vs 9 |
| `traduccion` | `traducción` | 9 | accented spelling 15,204 vs 9 |
| `prospera` | `próspero` | 9 | accented spelling 191 vs 9 |
| `rubeola` | `rubéola` | 9 | accented spelling 144 vs 9 |
| `mitica` | `mítico` | 9 | accented spelling 244 vs 9 |
| `peron` | `perón` | 9 | accented spelling 120 vs 9 |
| `antiguedades` | `antigüedad` | 9 | accented spelling 543 vs 9 |
| `manabi` | `manabí` | 9 | accented spelling 162 vs 9 |
| `odontologico` | `odontológico` | 9 | accented spelling 241 vs 9 |
| `orquidea` | `orquídea` | 9 | accented spelling 492 vs 9 |
| `renovacion` | `renovación` | 9 | accented spelling 4,724 vs 9 |
| `seais` | `ser` | 9 | accented spelling 395 vs 9 |
| `gosen` | `gosén` | 9 | accented spelling 110 vs 9 |
| `palida` | `pálido` | 9 | accented spelling 175 vs 9 |
| `farallon` | `farallón` | 9 | accented spelling 71 vs 9 |
| `florez` | `flórez` | 9 | accented spelling 62 vs 9 |
| `dominacion` | `dominación` | 9 | accented spelling 1,065 vs 9 |
| `gutierrez` | `gutiérrez` | 9 | accented spelling 972 vs 9 |
| `tripode` | `trípode` | 9 | accented spelling 686 vs 9 |
| `ateismo` | `ateísmo` | 8 | accented spelling 174 vs 8 |
| `intimamente` | `íntimamente` | 8 | accented spelling 495 vs 8 |
| `alcoholicas` | `alcohólico` | 8 | accented spelling 573 vs 8 |
| `armagedon` | `armagedón` | 8 | accented spelling 156 vs 8 |
| `nomada` | `nómada` | 8 | accented spelling 395 vs 8 |
| `inmunologico` | `inmunológico` | 8 | accented spelling 1,703 vs 8 |
| `leganes` | `leganés` | 8 | accented spelling 164 vs 8 |
| `pasantia` | `pasantía` | 8 | accented spelling 523 vs 8 |
| `fundicion` | `fundición` | 8 | accented spelling 2,038 vs 8 |
| `panico` | `pánico` | 8 | accented spelling 1,650 vs 8 |
| `camaron` | `camarón` | 8 | accented spelling 973 vs 8 |
| `uria` | `uría` | 8 | accented spelling 67 vs 8 |
| `sabras` | `saber` | 8 | accented spelling 1,797 vs 8 |
| `pirolisis` | `pirólisis` | 8 | accented spelling 114 vs 8 |
| `nordico` | `nórdico` | 8 | accented spelling 671 vs 8 |
| `raba` | `rabá` | 8 | accented spelling 48 vs 8 |
| `afiliacion` | `afiliación` | 8 | accented spelling 1,587 vs 8 |
| `dispondra` | `disponer` | 8 | accented spelling 285 vs 8 |
| `elevacion` | `elevación` | 8 | accented spelling 4,386 vs 8 |
| `explotacion` | `explotación` | 8 | accented spelling 8,403 vs 8 |
| `paralisis` | `parálisis` | 8 | accented spelling 860 vs 8 |
| `caera` | `caer` | 8 | accented spelling 319 vs 8 |
| `dedicacion` | `dedicación` | 8 | accented spelling 2,733 vs 8 |
| `invitacion` | `invitación` | 8 | accented spelling 4,546 vs 8 |
| `provision` | `provisión` | 8 | accented spelling 2,274 vs 8 |
| `enos` | `enós` | 8 | accented spelling 54 vs 8 |
| `volveria` | `volver` | 8 | accented spelling 418 vs 8 |
| `diafano` | `diáfano` | 8 | accented spelling 351 vs 8 |
| `minimamente` | `mínimamente` | 8 | accented spelling 488 vs 8 |
| `habias` | `haber` | 8 | accented spelling 416 vs 8 |
| `menorquin` | `menorquín` | 8 | accented spelling 77 vs 8 |
| `afliccion` | `aflicción` | 8 | accented spelling 962 vs 8 |
| `metodologia` | `metodología` | 8 | accented spelling 5,616 vs 8 |
| `decada` | `década` | 8 | accented spelling 12,565 vs 8 |
| `tarapaca` | `tarapacá` | 8 | accented spelling 46 vs 8 |
| `azaria` | `azaría` | 8 | accented spelling 113 vs 8 |
| `arbol` | `árbol` | 8 | accented spelling 15,422 vs 8 |
| `marroqui` | `marroquí` | 8 | accented spelling 1,094 vs 8 |
| `magnetica` | `magnético` | 8 | accented spelling 1,085 vs 8 |
| `estrategico` | `estratégico` | 8 | accented spelling 6,586 vs 8 |
| `estarian` | `estar` | 8 | accented spelling 553 vs 8 |
| `repatriacion` | `repatriación` | 8 | accented spelling 298 vs 8 |
| `demografico` | `demográfico` | 8 | accented spelling 1,448 vs 8 |
| `recomendacion` | `recomendación` | 8 | accented spelling 9,606 vs 8 |
| `taxon` | `taxón` | 8 | accented spelling 101 vs 8 |
| `actue` | `actuar` | 8 | accented spelling 404 vs 8 |
| `azoto` | `azotar` | 8 | accented spelling 81 vs 8 |
| `chaman` | `chamán` | 8 | accented spelling 270 vs 8 |
| `extasis` | `éxtasis` | 8 | accented spelling 504 vs 8 |
| `atraccion` | `atracción` | 8 | accented spelling 8,678 vs 8 |
| `versatil` | `versátil` | 8 | accented spelling 3,029 vs 8 |
| `vivia` | `vivir` | 8 | accented spelling 1,117 vs 8 |
| `esau` | `esaú` | 8 | accented spelling 784 vs 8 |
| `benicarlo` | `benicarló` | 8 | accented spelling 104 vs 8 |
| `agrupacion` | `agrupación` | 8 | accented spelling 1,395 vs 8 |
| `epidemiologia` | `epidemiología` | 8 | accented spelling 341 vs 8 |
| `purificacion` | `purificación` | 8 | accented spelling 1,424 vs 8 |
| `inflacion` | `inflación` | 8 | accented spelling 2,515 vs 8 |
| `menendez` | `menéndez` | 8 | accented spelling 206 vs 8 |
| `sauco` | `saúco` | 8 | accented spelling 48 vs 8 |
| `estevez` | `estévez` | 8 | accented spelling 42 vs 8 |
| `electrolisis` | `electrólisis` | 8 | accented spelling 120 vs 8 |
| `fistula` | `fístula` | 8 | accented spelling 169 vs 8 |
| `cuadriceps` | `cuádriceps` | 8 | accented spelling 78 vs 8 |
| `efrain` | `efraín` | 8 | accented spelling 690 vs 8 |
| `recobro` | `recobrar` | 8 | accented spelling 61 vs 8 |
| `cedula` | `cédula` | 8 | accented spelling 225 vs 8 |
| `sintesis` | `síntesis` | 8 | accented spelling 2,874 vs 8 |
| `tunica` | `túnica` | 8 | accented spelling 641 vs 8 |
| `zarate` | `zárate` | 8 | accented spelling 50 vs 8 |
| `ojen` | `ojén` | 8 | accented spelling 48 vs 8 |
| `variacion` | `variación` | 8 | accented spelling 4,511 vs 8 |
| `quejo` | `quejar` | 8 | accented spelling 108 vs 8 |
| `efectuan` | `efectuar` | 8 | accented spelling 179 vs 8 |
| `fronton` | `frontón` | 8 | accented spelling 97 vs 8 |
| `graficos` | `gráfico` | 8 | accented spelling 4,921 vs 8 |
| `conocia` | `conocer` | 8 | accented spelling 1,038 vs 8 |
| `egoismo` | `egoísmo` | 8 | accented spelling 839 vs 8 |
| `tuvieramos` | `tener` | 8 | accented spelling 195 vs 8 |
| `efectue` | `efectuar` | 8 | accented spelling 206 vs 8 |
| `iluminacion` | `iluminación` | 8 | accented spelling 10,737 vs 8 |
| `interactuan` | `interactuar` | 8 | accented spelling 410 vs 8 |
| `hermon` | `hermón` | 8 | accented spelling 72 vs 8 |
| `tematicas` | `temática` | 8 | accented spelling 818 vs 8 |
| `derribo` | `derribar` | 8 | accented spelling 163 vs 8 |
| `haceis` | `hacer` | 8 | accented spelling 304 vs 8 |
| `malvasia` | `malvasía` | 8 | accented spelling 61 vs 8 |
| `ofreciendol` | `ofrecer` | 8 | accented spelling 144 vs 8 |
| `indicacion` | `indicación` | 8 | accented spelling 6,258 vs 8 |
| `bucerias` | `bucerías` | 8 | accented spelling 56 vs 8 |
| `historicas` | `histórico` | 8 | accented spelling 983 vs 8 |
| `cojin` | `cojín` | 8 | accented spelling 1,757 vs 8 |
| `particion` | `partición` | 8 | accented spelling 1,905 vs 8 |
| `cupon` | `cupón` | 8 | accented spelling 2,198 vs 8 |
| `transaccion` | `transacción` | 8 | accented spelling 7,682 vs 8 |
| `cafarnaum` | `cafarnaúm` | 8 | accented spelling 50 vs 8 |
| `abrazame` | `abrazar` | 8 | accented spelling 40 vs 8 |
| `consegui` | `conseguir` | 8 | accented spelling 339 vs 8 |
| `utiles` | `útil` | 8 | accented spelling 4,650 vs 8 |
| `solidamente` | `sólidamente` | 8 | accented spelling 144 vs 8 |
| `convencion` | `convención` | 8 | accented spelling 8,958 vs 8 |
| `confeccion` | `confección` | 8 | accented spelling 1,016 vs 8 |
| `horoscopo` | `horóscopo` | 8 | accented spelling 634 vs 8 |
| `paez` | `páez` | 8 | accented spelling 62 vs 8 |
| `goias` | `goiás` | 8 | accented spelling 86 vs 8 |
| `formaldehido` | `formaldehído` | 8 | accented spelling 203 vs 8 |
| `clitoris` | `clítoris` | 8 | accented spelling 516 vs 8 |
| `lacteo` | `lácteo` | 8 | accented spelling 1,256 vs 8 |
| `orbita` | `órbita` | 8 | accented spelling 1,374 vs 8 |
| `atraidos` | `atraer` | 8 | accented spelling 273 vs 8 |
| `laban` | `labán` | 8 | accented spelling 412 vs 8 |
| `medano` | `médano` | 8 | accented spelling 105 vs 8 |
| `turkmenistan` | `turkmenistán` | 8 | accented spelling 202 vs 8 |
| `sanacion` | `sanación` | 8 | accented spelling 1,901 vs 8 |
| `nacar` | `nácar` | 8 | accented spelling 192 vs 8 |
| `narro` | `narrar` | 8 | accented spelling 84 vs 8 |
| `confio` | `confiar` | 8 | accented spelling 571 vs 8 |
| `peten` | `petén` | 8 | accented spelling 90 vs 8 |
| `catedra` | `cátedra` | 8 | accented spelling 701 vs 8 |
| `leidos` | `leer` | 8 | accented spelling 481 vs 8 |
| `cumplio` | `cumplir` | 8 | accented spelling 487 vs 8 |
| `aisla` | `aislar` | 8 | accented spelling 82 vs 8 |
| `respondera` | `responder` | 8 | accented spelling 479 vs 8 |
| `seguira` | `seguir` | 8 | accented spelling 1,558 vs 8 |
| `triangulo` | `triángulo` | 8 | accented spelling 1,887 vs 8 |
| `evasion` | `evasión` | 8 | accented spelling 579 vs 8 |
| `transgenero` | `transgénero` | 8 | accented spelling 578 vs 8 |
| `resolucion` | `resolución` | 8 | accented spelling 15,722 vs 8 |
| `sanlucar` | `sanlúcar` | 8 | accented spelling 136 vs 8 |
| `natacion` | `natación` | 8 | accented spelling 2,318 vs 8 |
| `emocion` | `emoción` | 8 | accented spelling 6,006 vs 8 |
| `aaiun` | `aaiún` | 8 | accented spelling 76 vs 8 |
| `prestamo` | `préstamo` | 8 | accented spelling 7,411 vs 8 |
| `habrian` | `haber` | 8 | accented spelling 960 vs 8 |
| `floreria` | `florería` | 8 | accented spelling 74 vs 8 |
| `raco` | `racó` | 8 | accented spelling 70 vs 8 |
| `situan` | `situar` | 8 | accented spelling 104 vs 8 |
| `tematica` | `temática` | 8 | accented spelling 2,990 vs 8 |
| `consul` | `cónsul` | 8 | accented spelling 261 vs 8 |
| `creia` | `creer` | 8 | accented spelling 1,153 vs 8 |
| `pabellon` | `pabellón` | 8 | accented spelling 2,213 vs 8 |
| `cañamo` | `cáñamo` | 8 | accented spelling 824 vs 8 |
| `guarana` | `guaraná` | 8 | accented spelling 124 vs 8 |
| `magnetico` | `magnético` | 8 | accented spelling 3,931 vs 8 |
| `tripulacion` | `tripulación` | 8 | accented spelling 2,107 vs 8 |
| `iniciacion` | `iniciación` | 8 | accented spelling 1,254 vs 8 |
| `intervencion` | `intervención` | 8 | accented spelling 9,133 vs 8 |
| `danes` | `danés` | 8 | accented spelling 1,222 vs 8 |
| `proximas` | `próximo` | 8 | accented spelling 3,331 vs 8 |
| `guarani` | `guaraní` | 8 | accented spelling 251 vs 8 |
| `analogica` | `analógico` | 8 | accented spelling 329 vs 8 |
| `contaminacion` | `contaminación` | 8 | accented spelling 6,825 vs 8 |
| `proteinas` | `proteína` | 8 | accented spelling 2,723 vs 8 |
| `discrecion` | `discreción` | 8 | accented spelling 4,377 vs 8 |
| `aprendera` | `aprender` | 8 | accented spelling 619 vs 8 |
| `politecnico` | `politécnico` | 8 | accented spelling 349 vs 8 |
| `teheran` | `teherán` | 8 | accented spelling 1,126 vs 8 |
| `oposicion` | `oposición` | 8 | accented spelling 6,403 vs 8 |
| `pequeñin` | `pequeñín` | 8 | accented spelling 58 vs 8 |
| `maraton` | `maratón` | 7 | accented spelling 1,011 vs 7 |
| `vastago` | `vástago` | 7 | accented spelling 576 vs 7 |
| `descubri` | `descubrir` | 7 | accented spelling 545 vs 7 |
| `relajese` | `relajarse` | 7 | accented spelling 770 vs 7 |
| `obsesion` | `obsesión` | 7 | accented spelling 724 vs 7 |
| `peonia` | `peonía` | 7 | accented spelling 91 vs 7 |
| `alarcon` | `alarcón` | 7 | accented spelling 228 vs 7 |
| `compro` | `comprar` | 7 | accented spelling 1,476 vs 7 |
| `erronea` | `erróneo` | 7 | accented spelling 491 vs 7 |
| `dorico` | `dórico` | 7 | accented spelling 35 vs 7 |
| `portugues` | `portugués` | 7 | accented spelling 3,819 vs 7 |
| `ponton` | `pontón` | 7 | accented spelling 166 vs 7 |
| `trilogia` | `trilogía` | 7 | accented spelling 487 vs 7 |
| `tellez` | `téllez` | 7 | accented spelling 36 vs 7 |
| `hipotesis` | `hipótesis` | 7 | accented spelling 2,280 vs 7 |
| `adoracion` | `adoración` | 7 | accented spelling 1,746 vs 7 |
| `respiracion` | `respiración` | 7 | accented spelling 3,248 vs 7 |
| `fabula` | `fábula` | 7 | accented spelling 261 vs 7 |
| `instantaneo` | `instantáneo` | 7 | accented spelling 3,955 vs 7 |
| `clarin` | `clarín` | 7 | accented spelling 111 vs 7 |
| `marañon` | `marañón` | 7 | accented spelling 60 vs 7 |
| `canonica` | `canónico` | 7 | accented spelling 93 vs 7 |
| `creian` | `creer` | 7 | accented spelling 437 vs 7 |
| `anahuac` | `anáhuac` | 7 | accented spelling 38 vs 7 |
| `cadi` | `cadí` | 7 | accented spelling 40 vs 7 |
| `gano` | `ganar` | 7 | accented spelling 2,514 vs 7 |
| `romanticas` | `romántico` | 7 | accented spelling 360 vs 7 |
| `estara` | `estar` | 7 | accented spelling 8,486 vs 7 |
| `cardiologia` | `cardiología` | 7 | accented spelling 514 vs 7 |
| `codigos` | `código` | 7 | accented spelling 3,093 vs 7 |
| `arguelles` | `argüelles` | 7 | accented spelling 40 vs 7 |
| `heladerias` | `heladería` | 7 | accented spelling 212 vs 7 |
| `toxica` | `tóxico` | 7 | accented spelling 237 vs 7 |
| `competa` | `cómpeta` | 7 | accented spelling 96 vs 7 |
| `asiatico` | `asiático` | 7 | accented spelling 3,660 vs 7 |
| `aclaracion` | `aclaración` | 7 | accented spelling 644 vs 7 |
| `associacio` | `associació` | 7 | accented spelling 40 vs 7 |
| `crepusculo` | `crepúsculo` | 7 | accented spelling 757 vs 7 |
| `antologia` | `antología` | 7 | accented spelling 251 vs 7 |
| `chiloe` | `chiloé` | 7 | accented spelling 120 vs 7 |
| `climatizacion` | `climatización` | 7 | accented spelling 1,560 vs 7 |
| `exotica` | `exótico` | 7 | accented spelling 216 vs 7 |
| `jurisdiccion` | `jurisdicción` | 7 | accented spelling 4,787 vs 7 |
| `arquitectonico` | `arquitectónico` | 7 | accented spelling 3,166 vs 7 |
| `albaicin` | `albaicín` | 7 | accented spelling 120 vs 7 |
| `britanico` | `británico` | 7 | accented spelling 7,122 vs 7 |
| `bufalo` | `búfalo` | 7 | accented spelling 582 vs 7 |
| `vater` | `váter` | 7 | accented spelling 72 vs 7 |
| `origenes` | `origen` | 7 | accented spelling 1,621 vs 7 |
| `purpura` | `púrpura` | 7 | accented spelling 1,961 vs 7 |
| `hicieramos` | `hacer` | 7 | accented spelling 67 vs 7 |
| `seguia` | `seguir` | 7 | accented spelling 878 vs 7 |
| `determinacion` | `determinación` | 7 | accented spelling 4,248 vs 7 |
| `adquisicion` | `adquisición` | 7 | accented spelling 5,984 vs 7 |
| `atmosfera` | `atmósfera` | 7 | accented spelling 5,498 vs 7 |
| `maniaco` | `maníaco` | 7 | accented spelling 103 vs 7 |
| `tomaria` | `tomar` | 7 | accented spelling 206 vs 7 |
| `boveda` | `bóveda` | 7 | accented spelling 995 vs 7 |
| `aparicion` | `aparición` | 7 | accented spelling 5,908 vs 7 |
| `geometrico` | `geométrico` | 7 | accented spelling 1,137 vs 7 |
| `historicamente` | `históricamente` | 7 | accented spelling 1,259 vs 7 |
| `moron` | `morón` | 7 | accented spelling 135 vs 7 |
| `e-liquido` | `e-líquido` | 7 | accented spelling 81 vs 7 |
| `establecio` | `establecer` | 7 | accented spelling 1,239 vs 7 |
| `dinastia` | `dinastía` | 7 | accented spelling 970 vs 7 |
| `montgo` | `montgó` | 7 | accented spelling 84 vs 7 |
| `plasticos` | `plástico` | 7 | accented spelling 1,461 vs 7 |
| `induccion` | `inducción` | 7 | accented spelling 1,575 vs 7 |
| `numerico` | `numérico` | 7 | accented spelling 1,910 vs 7 |
| `gavilan` | `gavilán` | 7 | accented spelling 56 vs 7 |
| `facturacion` | `facturación` | 7 | accented spelling 4,186 vs 7 |
| `apareceran` | `aparecer` | 7 | accented spelling 646 vs 7 |
| `veais` | `ver` | 7 | accented spelling 104 vs 7 |
| `tendreis` | `tener` | 7 | accented spelling 386 vs 7 |
| `pinguino` | `pingüino` | 7 | accented spelling 550 vs 7 |
| `humedas` | `húmedo` | 7 | accented spelling 365 vs 7 |
| `atomo` | `átomo` | 7 | accented spelling 1,087 vs 7 |
| `abbe` | `abbé` | 7 | accented spelling 41 vs 7 |
| `perdida#Masc` | `pérdida` | 7 | accented spelling 25,622 vs 7 |
| `democratica` | `democrático` | 7 | accented spelling 1,167 vs 7 |
| `giron` | `girón` | 7 | accented spelling 110 vs 7 |
| `calificacion` | `calificación` | 7 | accented spelling 6,742 vs 7 |
| `rehuso` | `rehusar` | 7 | accented spelling 150 vs 7 |
| `autonomia` | `autonomía` | 7 | accented spelling 2,964 vs 7 |
| `cateter` | `catéter` | 7 | accented spelling 909 vs 7 |
| `ionica` | `iónico` | 7 | accented spelling 47 vs 7 |
| `tematico` | `temático` | 7 | accented spelling 1,862 vs 7 |
| `narracion` | `narración` | 7 | accented spelling 1,053 vs 7 |
| `comence` | `comenzar` | 7 | accented spelling 777 vs 7 |
| `querais` | `querer` | 7 | accented spelling 235 vs 7 |
| `camaleon` | `camaleón` | 7 | accented spelling 162 vs 7 |
| `popurri` | `popurrí` | 7 | accented spelling 43 vs 7 |
| `consagracion` | `consagración` | 7 | accented spelling 558 vs 7 |
| `sucedio` | `suceder` | 7 | accented spelling 1,640 vs 7 |
| `jugue` | `jugar` | 7 | accented spelling 109 vs 7 |
| `posesion` | `posesión` | 7 | accented spelling 4,013 vs 7 |
| `enfasis` | `énfasis` | 7 | accented spelling 3,017 vs 7 |
| `katmandu` | `katmandú` | 7 | accented spelling 400 vs 7 |
| `traian` | `traer` | 7 | accented spelling 117 vs 7 |
| `dolar` | `dólar` | 7 | accented spelling 14,859 vs 7 |
| `cubico` | `cúbico` | 7 | accented spelling 425 vs 7 |
| `jonico` | `jónico` | 7 | accented spelling 100 vs 7 |
| `echeverria` | `echeverría` | 7 | accented spelling 50 vs 7 |
| `automata` | `autómata` | 7 | accented spelling 159 vs 7 |
| `etico` | `ético` | 7 | accented spelling 1,869 vs 7 |
| `coreografia` | `coreografía` | 7 | accented spelling 353 vs 7 |
| `ravena` | `rávena` | 7 | accented spelling 106 vs 7 |
| `cienaga` | `ciénaga` | 7 | accented spelling 126 vs 7 |
| `valida` | `válido` | 7 | accented spelling 1,971 vs 7 |
| `chavon` | `chavón` | 7 | accented spelling 254 vs 7 |
| `gedeon` | `gedeón` | 7 | accented spelling 390 vs 7 |
| `antibiotico` | `antibiótico` | 7 | accented spelling 1,832 vs 7 |
| `tentacion` | `tentación` | 7 | accented spelling 1,694 vs 7 |
| `indole` | `índole` | 7 | accented spelling 1,106 vs 7 |
| `practicamente` | `prácticamente` | 7 | accented spelling 7,312 vs 7 |
| `ofrecera` | `ofrecer` | 7 | accented spelling 1,432 vs 7 |
| `inutil` | `inútil` | 7 | accented spelling 1,591 vs 7 |
| `nisan` | `nisán` | 7 | accented spelling 42 vs 7 |
| `interaccion` | `interacción` | 7 | accented spelling 7,314 vs 7 |
| `tactico` | `táctico` | 7 | accented spelling 1,257 vs 7 |
| `etiopia` | `etiopía` | 7 | accented spelling 1,042 vs 7 |
| `fenomeno` | `fenómeno` | 7 | accented spelling 5,507 vs 7 |
| `expres` | `exprés` | 7 | accented spelling 792 vs 7 |
| `sentira` | `sentir` | 7 | accented spelling 200 vs 7 |
| `escandalo` | `escándalo` | 7 | accented spelling 1,527 vs 7 |
| `actuacion` | `actuación` | 7 | accented spelling 5,915 vs 7 |
| `bejar` | `béjar` | 7 | accented spelling 88 vs 7 |
| `haria` | `hacer` | 7 | accented spelling 1,580 vs 7 |
| `automoviles` | `automóvil` | 7 | accented spelling 3,304 vs 7 |
| `anonima` | `anónimo` | 7 | accented spelling 1,180 vs 7 |
| `tarzan` | `tarzán` | 7 | accented spelling 68 vs 7 |
| `metodos` | `método` | 7 | accented spelling 7,809 vs 7 |
| `viver` | `víveres` | 7 | accented spelling 125 vs 7 |
| `hanan` | `hanán` | 7 | accented spelling 44 vs 7 |
| `afirmacion` | `afirmación` | 7 | accented spelling 2,461 vs 7 |
| `optimo` | `óptimo` | 7 | accented spelling 8,739 vs 7 |
| `lamina` | `lámina` | 7 | accented spelling 2,561 vs 7 |
| `caidas` | `caída` | 7 | accented spelling 899 vs 7 |
| `patina` | `pátina` | 7 | accented spelling 179 vs 7 |
| `kefir` | `kéfir` | 7 | accented spelling 110 vs 7 |
| `hubieramos` | `haber` | 7 | accented spelling 296 vs 7 |
| `emblematico` | `emblemático` | 7 | accented spelling 2,203 vs 7 |
| `fallecio` | `fallecer` | 7 | accented spelling 628 vs 7 |
| `intima` | `íntimo` | 7 | accented spelling 567 vs 7 |
| `solucion` | `solución` | 7 | accented spelling 53,744 vs 7 |
| `acustica` | `acústico` | 7 | accented spelling 662 vs 7 |
| `pedagogico` | `pedagógico` | 7 | accented spelling 890 vs 7 |
| `prostata` | `próstata` | 7 | accented spelling 2,353 vs 7 |
| `emision` | `emisión` | 7 | accented spelling 8,572 vs 7 |
| `curriculo` | `currículo` | 7 | accented spelling 926 vs 7 |
| `criquet` | `críquet` | 7 | accented spelling 136 vs 7 |
| `pequeñin#Fem` | `pequeñín` | 7 | accented spelling 58 vs 7 |
| `dramaticas` | `dramático` | 7 | accented spelling 131 vs 7 |
| `adhesion` | `adhesión` | 7 | accented spelling 2,284 vs 7 |
| `venian` | `venir` | 7 | accented spelling 439 vs 7 |
| `tampon` | `tampón` | 7 | accented spelling 277 vs 7 |
| `serrania` | `serranía` | 7 | accented spelling 120 vs 7 |
| `antelacion` | `antelación` | 7 | accented spelling 4,706 vs 7 |
| `oira` | `oír` | 7 | accented spelling 124 vs 7 |
| `pilon` | `pilón` | 7 | accented spelling 73 vs 7 |
| `desvelo` | `desvelar` | 7 | accented spelling 40 vs 7 |
| `rendon` | `rendón` | 7 | accented spelling 38 vs 7 |
| `taino` | `taíno` | 7 | accented spelling 43 vs 7 |
| `albedrio` | `albedrío` | 7 | accented spelling 586 vs 7 |
| `calorias` | `caloría` | 7 | accented spelling 2,270 vs 7 |
| `pipi` | `pipí` | 7 | accented spelling 56 vs 7 |
| `paladin` | `paladín` | 7 | accented spelling 107 vs 7 |
| `auditoria` | `auditoría` | 7 | accented spelling 4,225 vs 7 |
| `basquet` | `básquet` | 7 | accented spelling 76 vs 7 |
| `normandia` | `normandía` | 7 | accented spelling 496 vs 7 |
| `peco` | `pecar` | 7 | accented spelling 83 vs 7 |
| `bajate` | `bajarse` | 7 | accented spelling 60 vs 7 |
| `patagonica` | `patagónico` | 6 | accented spelling 51 vs 6 |
| `vudu` | `vudú` | 6 | accented spelling 100 vs 6 |
| `vendio` | `vender` | 6 | accented spelling 570 vs 6 |
| `boqueron` | `boquerón` | 6 | accented spelling 57 vs 6 |
| `citrico` | `cítrico` | 6 | accented spelling 920 vs 6 |
| `redencion` | `redención` | 6 | accented spelling 1,208 vs 6 |
| `discriminacion` | `discriminación` | 6 | accented spelling 4,749 vs 6 |
| `liston` | `listón` | 6 | accented spelling 324 vs 6 |
| `sinfonia` | `sinfonía` | 6 | accented spelling 349 vs 6 |
| `ortopedico` | `ortopédico` | 6 | accented spelling 474 vs 6 |
| `titere` | `títere` | 6 | accented spelling 476 vs 6 |
| `olia` | `oler` | 6 | accented spelling 87 vs 6 |
| `sereis` | `ser` | 6 | accented spelling 485 vs 6 |
| `vegetacion` | `vegetación` | 6 | accented spelling 2,548 vs 6 |
| `rele` | `relé` | 6 | accented spelling 684 vs 6 |
| `sinonimo` | `sinónimo` | 6 | accented spelling 1,622 vs 6 |
| `edificacion` | `edificación` | 6 | accented spelling 1,673 vs 6 |
| `lubricacion` | `lubricación` | 6 | accented spelling 1,432 vs 6 |
| `querubin` | `querubín` | 6 | accented spelling 405 vs 6 |
| `traccion` | `tracción` | 6 | accented spelling 4,139 vs 6 |
| `quirurgico` | `quirúrgico` | 6 | accented spelling 3,513 vs 6 |
| `dudeis` | `dudar` | 6 | accented spelling 80 vs 6 |
| `unisono` | `unísono` | 6 | accented spelling 203 vs 6 |
| `cronicas` | `crónica` | 6 | accented spelling 1,143 vs 6 |
| `subtitulos` | `subtítulo` | 6 | accented spelling 665 vs 6 |
| `erroneo` | `erróneo` | 6 | accented spelling 1,421 vs 6 |
| `midio` | `medir` | 6 | accented spelling 160 vs 6 |
| `impresion` | `impresión` | 6 | accented spelling 19,854 vs 6 |
| `aspero` | `áspero` | 6 | accented spelling 547 vs 6 |
| `tomare` | `tomar` | 6 | accented spelling 196 vs 6 |
| `mantendra` | `mantener` | 6 | accented spelling 983 vs 6 |
| `hondon` | `hondón` | 6 | accented spelling 38 vs 6 |
| `maracuya` | `maracuyá` | 6 | accented spelling 67 vs 6 |
| `estiercol` | `estiércol` | 6 | accented spelling 477 vs 6 |
| `microdermabrasion` | `microdermabrasión` | 6 | accented spelling 30 vs 6 |
| `carpinterias` | `carpintería` | 6 | accented spelling 32 vs 6 |
| `chavin` | `chavín` | 6 | accented spelling 34 vs 6 |
| `adquirio` | `adquirir` | 6 | accented spelling 569 vs 6 |
| `recamaras` | `recámara` | 6 | accented spelling 152 vs 6 |
| `societe` | `société` | 6 | accented spelling 59 vs 6 |
| `elegi` | `elegir` | 6 | accented spelling 371 vs 6 |
| `penso` | `pensar` | 6 | accented spelling 1,024 vs 6 |
| `cesped` | `césped` | 6 | accented spelling 2,665 vs 6 |
| `dirijase` | `dirigirse` | 6 | accented spelling 840 vs 6 |
| `lavapies` | `lavapiés` | 6 | accented spelling 76 vs 6 |
| `petropolis` | `petrópolis` | 6 | accented spelling 48 vs 6 |
| `promocion` | `promoción` | 6 | accented spelling 15,069 vs 6 |
| `calendula` | `caléndula` | 6 | accented spelling 150 vs 6 |
| `mesia` | `mesías` | 6 | accented spelling 30 vs 6 |
| `herreria` | `herrería` | 6 | accented spelling 110 vs 6 |
| `capto` | `captar` | 6 | accented spelling 89 vs 6 |
| `conoceis` | `conocer` | 6 | accented spelling 250 vs 6 |
| `maximo` | `máximo` | 6 | accented spelling 38,797 vs 6 |
| `almaden` | `almadén` | 6 | accented spelling 32 vs 6 |
| `onu-habitat` | `onu-hábitat` | 6 | accented spelling 36 vs 6 |
| `alergeno` | `alérgeno` | 6 | accented spelling 466 vs 6 |
| `aprendio` | `aprender` | 6 | accented spelling 589 vs 6 |
| `querria` | `querer` | 6 | accented spelling 470 vs 6 |
| `manifestacion` | `manifestación` | 6 | accented spelling 4,193 vs 6 |
| `asesorias` | `asesoría` | 6 | accented spelling 125 vs 6 |
| `epocas` | `época` | 6 | accented spelling 823 vs 6 |
| `mitzva` | `mitzvá` | 6 | accented spelling 78 vs 6 |
| `aligator` | `aligátor` | 6 | accented spelling 36 vs 6 |
| `radon` | `radón` | 6 | accented spelling 170 vs 6 |
| `gondolas` | `góndola` | 6 | accented spelling 70 vs 6 |
| `espontaneamente` | `espontáneamente` | 6 | accented spelling 403 vs 6 |
| `en-linea` | `en línea` | 6 | accented spelling 70 vs 6 |
| `mamifero` | `mamífero` | 6 | accented spelling 756 vs 6 |
| `coqui` | `coquí` | 6 | accented spelling 40 vs 6 |
| `contactano` | `contactar` | 6 | accented spelling 51 vs 6 |
| `encarnacion` | `encarnación` | 6 | accented spelling 1,092 vs 6 |
| `alcorcon` | `alcorcón` | 6 | accented spelling 112 vs 6 |
| `montgri` | `montgrí` | 6 | accented spelling 58 vs 6 |
| `colico` | `cólico` | 6 | accented spelling 210 vs 6 |
| `triceps` | `tríceps` | 6 | accented spelling 112 vs 6 |
| `ecologia` | `ecología` | 6 | accented spelling 1,301 vs 6 |
| `arcen` | `arcén` | 6 | accented spelling 48 vs 6 |
| `tintin` | `tintín` | 6 | accented spelling 84 vs 6 |
| `lengueta` | `lengüeta` | 6 | accented spelling 434 vs 6 |
| `estimulacion` | `estimulación` | 6 | accented spelling 1,479 vs 6 |
| `halcon` | `halcón` | 6 | accented spelling 461 vs 6 |
| `arrojo` | `arrojar` | 6 | accented spelling 335 vs 6 |
| `gines` | `ginés` | 6 | accented spelling 64 vs 6 |
| `lesbico` | `lésbico` | 6 | accented spelling 162 vs 6 |
| `exploracion` | `exploración` | 6 | accented spelling 4,348 vs 6 |
| `fragil` | `frágil` | 6 | accented spelling 1,398 vs 6 |
| `autenticacion` | `autenticación` | 6 | accented spelling 2,442 vs 6 |
| `cuauhtemoc` | `cuauhtémoc` | 6 | accented spelling 100 vs 6 |
| `benares` | `benarés` | 6 | accented spelling 52 vs 6 |
| `diplomatico` | `diplomático` | 6 | accented spelling 1,851 vs 6 |
| `incognita` | `incógnito` | 6 | accented spelling 54 vs 6 |
| `recopilacion` | `recopilación` | 6 | accented spelling 3,090 vs 6 |
| `superheroe` | `superhéroe` | 6 | accented spelling 495 vs 6 |
| `dirigiendose` | `dirigirse` | 6 | accented spelling 648 vs 6 |
| `cronico` | `crónico` | 6 | accented spelling 3,048 vs 6 |
| `pensais` | `pensar` | 6 | accented spelling 162 vs 6 |
| `bermudez` | `bermúdez` | 6 | accented spelling 112 vs 6 |
| `karite` | `karité` | 6 | accented spelling 268 vs 6 |
| `piramides` | `pirámide` | 6 | accented spelling 355 vs 6 |
| `esteis` | `estar` | 6 | accented spelling 217 vs 6 |
| `repeticion` | `repetición` | 6 | accented spelling 1,964 vs 6 |
| `desearia` | `desear` | 6 | accented spelling 493 vs 6 |
| `placet` | `plácet` | 6 | accented spelling 58 vs 6 |
| `israeli` | `israelí` | 6 | accented spelling 2,640 vs 6 |
| `retorica` | `retórico` | 6 | accented spelling 381 vs 6 |
| `almoradi` | `almoradí` | 6 | accented spelling 36 vs 6 |
| `bolson` | `bolsón` | 6 | accented spelling 91 vs 6 |
| `clasificacion` | `clasificación` | 6 | accented spelling 9,516 vs 6 |
| `semisotano` | `semisótano` | 6 | accented spelling 98 vs 6 |
| `dejeis` | `dejar` | 6 | accented spelling 128 vs 6 |
| `pondre` | `poner` | 6 | accented spelling 473 vs 6 |
| `tajin` | `tajín` | 6 | accented spelling 36 vs 6 |
| `calcomania` | `calcomanía` | 6 | accented spelling 187 vs 6 |
| `cercanias` | `cercanías` | 6 | accented spelling 1,284 vs 6 |
| `tipologia` | `tipología` | 6 | accented spelling 832 vs 6 |
| `asia-pacifico` | `asia-pacífico` | 6 | accented spelling 364 vs 6 |
| `videografo` | `videógrafo` | 6 | accented spelling 33 vs 6 |
| `habil` | `hábil` | 6 | accented spelling 1,796 vs 6 |
| `oceanico` | `oceánico` | 6 | accented spelling 380 vs 6 |
| `obtencion` | `obtención` | 6 | accented spelling 3,391 vs 6 |
| `permanecera` | `permanecer` | 6 | accented spelling 724 vs 6 |
| `volvere` | `volver` | 6 | accented spelling 574 vs 6 |
| `admision` | `admisión` | 6 | accented spelling 2,898 vs 6 |
| `naaman` | `naamán` | 6 | accented spelling 148 vs 6 |
| `ganaderia` | `ganadería` | 6 | accented spelling 855 vs 6 |
| `indice` | `índice` | 6 | accented spelling 17,383 vs 6 |
| `isotopo` | `isótopo` | 6 | accented spelling 108 vs 6 |
| `pedagogia` | `pedagogía` | 6 | accented spelling 627 vs 6 |
| `tipografia` | `tipografía` | 6 | accented spelling 587 vs 6 |
| `veian` | `ver` | 6 | accented spelling 308 vs 6 |
| `impio` | `impío` | 6 | accented spelling 870 vs 6 |
| `desesperacion` | `desesperación` | 6 | accented spelling 1,104 vs 6 |
| `zuñiga` | `zúñiga` | 6 | accented spelling 70 vs 6 |
| `ratan` | `ratán` | 6 | accented spelling 156 vs 6 |
| `caucaso` | `cáucaso` | 6 | accented spelling 286 vs 6 |
| `pildora` | `píldora` | 6 | accented spelling 2,395 vs 6 |
| `lucida` | `lúcido` | 6 | accented spelling 31 vs 6 |
| `hablabamos` | `hablar` | 6 | accented spelling 101 vs 6 |
| `pornografia` | `pornografía` | 6 | accented spelling 1,032 vs 6 |
| `almidon` | `almidón` | 6 | accented spelling 742 vs 6 |
| `compilacion` | `compilación` | 6 | accented spelling 1,056 vs 6 |
| `erase` | `ser` | 6 | accented spelling 69 vs 6 |
| `magicas` | `mágico` | 6 | accented spelling 400 vs 6 |
| `cronografo` | `cronógrafo` | 6 | accented spelling 953 vs 6 |
| `estefania` | `estefanía` | 6 | accented spelling 82 vs 6 |
| `galvan` | `galván` | 6 | accented spelling 68 vs 6 |
| `mitico` | `mítico` | 6 | accented spelling 963 vs 6 |
| `marroquineria` | `marroquinería` | 6 | accented spelling 108 vs 6 |
| `tepoztlan` | `tepoztlán` | 6 | accented spelling 38 vs 6 |
| `fanatico` | `fanático` | 6 | accented spelling 1,372 vs 6 |
| `subio` | `subir` | 6 | accented spelling 1,191 vs 6 |
| `varon` | `varón` | 6 | accented spelling 3,621 vs 6 |
| `existia` | `existir` | 6 | accented spelling 825 vs 6 |
| `albumina` | `albúmina` | 6 | accented spelling 155 vs 6 |
| `pelaez` | `peláez` | 6 | accented spelling 32 vs 6 |
| `trencadis` | `trencadís` | 6 | accented spelling 46 vs 6 |
| `formulacion` | `formulación` | 6 | accented spelling 2,415 vs 6 |
| `paradisiaca` | `paradisíaco` | 6 | accented spelling 75 vs 6 |
| `technologia` | `tecnología` | 6 | accented spelling 30 vs 6 |
| `escorpion` | `escorpión` | 6 | accented spelling 398 vs 6 |
| `dedan` | `dedán` | 6 | accented spelling 30 vs 6 |
| `adaptacion` | `adaptación` | 6 | accented spelling 5,075 vs 6 |
| `muchisima` | `mucho` | 6 | accented spelling 205 vs 6 |
| `mogan` | `mogán` | 6 | accented spelling 134 vs 6 |
| `transportin#Fem` | `transportín` | 6 | accented spelling 50 vs 6 |

### Dropped by 2+ flags: random sample of 0 of 0 in the window

| rank | lemma | flags |
|---:|---|---|

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 13,631 (keep 3,243, drop 10,388); review merges: 2,007.
