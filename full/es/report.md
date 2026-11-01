# Review report: es (full)

- Ranking score: `frequency`; 198,751 candidate lemmas ranked.
- Tokens counted: 105,726,244 in 138,221 documents, 40 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_es` 1.5.0 (sha256 `ccbd50dc900e43a8`); fallback `spacy-list`, units on; honeyeater `44220fb34e82`.

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
| `Estados Unidos` | 31,586 | 27,150 | 367 |
| `internacional` | 29,628 | 25,601 | 255 |
| `correo electrónico` | 23,988 | 20,711 | 506 |
| `convertirse` | 22,193 | 20,150 | 1980 |
| `por qué` | 21,701 | 18,212 | 574 |
| `directamente` | 19,755 | 18,142 | 616 |
| `especialmente` | 16,904 | 15,845 | 748 |
| `tratarse` | 16,335 | 15,214 | 2474 |
| `simplemente` | 16,304 | 15,259 | 773 |
| `actualmente` | 15,739 | 14,836 | 803 |
| `asegurarse` | 15,565 | 14,618 | 2380 |
| `realmente` | 14,990 | 13,945 | 846 |
| `página web` | 14,699 | 13,198 | 861 |
| `completamente` | 13,848 | 13,076 | 921 |
| `totalmente` | 13,329 | 12,557 | 949 |
| `sentirse` | 12,219 | 11,380 | 1035 |
| `quedarse` | 11,948 | 10,933 | 1175 |
| `fácilmente` | 11,559 | 11,022 | 1090 |
| `rápidamente` | 11,457 | 10,940 | 1101 |
| `solamente` | 11,186 | 10,639 | 1129 |
| `Nueva York` | 10,712 | 9,713 | 1167 |
| `ponerse` | 10,545 | 9,933 | 1328 |
| `aproximadamente` | 10,074 | 9,441 | 1219 |

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
| `más/menos … que` | 34,497 | 29,532 | 337 |
| `seguir + gerundio` | 22,054 | 19,948 | 557 |
| `volver a + infinitivo` | 13,984 | 12,888 | 912 |
| `comenzar a + infinitivo` | 12,993 | 12,191 | 976 |
| `empezar a + infinitivo` | 12,218 | 11,339 | 1036 |
| `tan … como` | 10,157 | 9,493 | 1254 |
| `dejar de + infinitivo` | 10,025 | 9,340 | 1226 |
| `soler + infinitivo` | 9,984 | 9,411 | 1228 |
| `hace + tiempo` | 9,235 | 8,758 | 1314 |
| `acabar de + infinitivo` | 6,299 | 5,481 | 1830 |
| `desde hace + tiempo` | 4,432 | 4,335 | 2420 |
| `tan … que` | 4,137 | 4,008 | 2529 |
| `qué + adjetivo/sustantivo` | 3,891 | 3,564 | 2647 |
| `hace + tiempo + que` | 3,146 | 3,019 | 3060 |
| `hacer que + subjuntivo` | 1,195 | 1,188 | 5564 |
| `menos … que` | 662 | 643 | 7926 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `a través de` | 59,644 | 46,869 | 162 |
| `después de` | 56,703 | 45,496 | 172 |
| `para que` | 54,272 | 43,859 | 181 |
| `cerca de` | 41,538 | 34,672 | 259 |
| `antes de` | 39,627 | 33,863 | 273 |
| `así como` | 39,070 | 33,633 | 281 |
| `acerca de` | 38,745 | 32,397 | 283 |
| `sin embargo` | 37,024 | 32,245 | 303 |
| `dentro de` | 31,163 | 27,155 | 372 |
| `por ejemplo` | 28,950 | 25,697 | 416 |
| `ya que` | 27,190 | 24,494 | 448 |
| `por favor` | 22,188 | 19,545 | 549 |
| `gracias a` | 21,895 | 20,055 | 560 |
| `en línea` | 21,418 | 19,462 | 575 |
| `por lo que` | 19,686 | 18,256 | 620 |
| `disfrutar de algo` | 19,565 | 18,050 | 623 |
| `además de` | 18,838 | 17,479 | 645 |
| `contar con algo` | 18,672 | 17,317 | 655 |
| `así que` | 18,491 | 17,231 | 668 |
| `debido a` | 18,042 | 16,692 | 691 |
| `a partir de` | 17,697 | 16,365 | 707 |
| `a continuación` | 17,637 | 16,445 | 713 |
| `convertirse en algo` | 17,624 | 16,334 | 716 |
| `alrededor de` | 16,331 | 15,105 | 771 |
| `fuera de` | 15,695 | 14,562 | 807 |

## Co-occurrence (association) table

103,156,662 tokens, 5,707,166 sentences. After merging and dropping items seen fewer than 5 times: 4,204,818 items (unigrams, UPOS votes, n-grams, pairs); 3,862,597 n-grams and pairs scored (n2 889,669, n3 1,699,985, n4 1,269,877, p2 3,066). Shipped: 400,000 rows, 8.4 MB gzipped (`es.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`es.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `mejor precio` |  | 63,167 | 49,386 | 7.74 | 0.73 | 606,108 |  |
| 2 | n | `respuesta rápido de personal` |  | 23,672 | 21,647 | 10.30 | 0.85 | 345,256 |  |
| 3 | n | `más barato` |  | 37,109 | 31,984 | 6.80 | 0.59 | 307,378 |  |
| 4 | n | `buscar el mejor precio` |  | 23,111 | 21,217 | 9.49 | 0.78 | 307,213 |  |
| 5 | n | `pasaje aereo` |  | 16,790 | 8,877 | 12.03 | 0.96 | 289,090 |  |
| 6 | n | `continuar con la búsqueda` |  | 17,645 | 16,556 | 11.23 | 0.90 | 280,342 |  |
| 7 | n | `personal y los huésped` |  | 19,026 | 17,693 | 10.29 | 0.83 | 275,286 |  |
| 8 | n | `manual de instrucción` |  | 17,723 | 16,299 | 11.17 | 0.89 | 271,014 |  |
| 9 | n | `no haber` |  | 67,596 | 52,586 | 4.11 | 0.39 | 270,714 |  |
| 10 | n | `ser posible` |  | 41,567 | 35,698 | 5.40 | 0.48 | 263,932 |  |
| 11 | n | `buscador de vuelo` |  | 20,861 | 19,321 | 9.18 | 0.75 | 258,514 |  |
| 12 | n | `mejor precio en jetcost` |  | 20,488 | 18,917 | 8.92 | 0.73 | 255,491 |  |
| 13 | n | `estar buscar el mejor` |  | 23,113 | 21,220 | 7.54 | 0.62 | 241,970 |  |
| 14 | n | `precio para su vuelo` |  | 18,378 | 17,161 | 9.31 | 0.75 | 239,030 |  |
| 15 | n | `vuelo regular o vuelo` |  | 17,697 | 16,517 | 9.31 | 0.74 | 230,358 |  |
| 16 | n | `alto calidad` |  | 20,708 | 18,896 | 8.45 | 0.69 | 213,545 |  |
| 17 | n | `estar buscar` |  | 31,292 | 27,910 | 6.00 | 0.51 | 212,500 |  |
| 18 | n | `vuelo low cost` |  | 17,753 | 16,562 | 8.99 | 0.72 | 209,112 |  |
| 19 | n | `que no` |  | 90,922 | 65,220 | 2.69 | 0.27 | 197,424 |  |
| 20 | n | `posible que no haber` |  | 17,660 | 16,568 | 7.39 | 0.59 | 176,696 |  |
| 21 | n | `tipo de` |  | 53,323 | 42,877 | 3.05 | 0.28 | 175,837 |  |
| 22 | n | `para encontrar los vuelo` |  | 20,057 | 18,649 | 6.22 | 0.50 | 167,744 |  |
| 23 | n | `información sobre` |  | 23,068 | 20,868 | 6.19 | 0.51 | 158,678 |  |
| 24 | n | `querer continuar con` |  | 17,662 | 16,569 | 6.50 | 0.52 | 158,470 |  |
| 25 | n | `ser posible que` |  | 27,026 | 24,489 | 4.99 | 0.42 | 157,197 |  |
| 26 | n | `pronóstico de tiempo` |  | 12,687 | 12,035 | 9.24 | 0.71 | 156,597 |  |
| 27 | n | `relacionar con` |  | 21,423 | 19,479 | 5.96 | 0.49 | 154,849 |  |
| 28 | n | `ser posible que no` |  | 18,398 | 17,229 | 6.08 | 0.49 | 151,173 |  |
| 29 | n | `ser muy` |  | 34,603 | 29,928 | 4.27 | 0.37 | 149,702 |  |
| 30 | n | `mejor precio para` |  | 25,669 | 23,335 | 4.98 | 0.42 | 139,465 |  |
| 31 | n | `creer que` |  | 24,377 | 20,825 | 4.89 | 0.41 | 136,653 |  |
| 32 | n | `que no haber resultado` |  | 17,635 | 16,545 | 5.59 | 0.45 | 134,697 |  |
| 33 | n | `a los mejor precio` |  | 22,253 | 20,404 | 4.93 | 0.40 | 130,412 |  |
| 34 | n | `billete avión` |  | 8,678 | 4,398 | 11.25 | 0.83 | 127,481 |  |
| 35 | n | `en vuelo regular` |  | 17,702 | 16,521 | 5.10 | 0.41 | 124,726 |  |
| 36 | n | `estar disponible` |  | 16,922 | 15,707 | 6.09 | 0.48 | 117,021 |  |
| 37 | n | `cosa que hacer` |  | 12,718 | 11,949 | 7.46 | 0.57 | 116,800 |  |
| 38 | n | `me gustar` |  | 11,189 | 9,409 | 8.59 | 0.65 | 116,600 |  |
| 39 | n | `decir que` |  | 34,380 | 29,088 | 3.59 | 0.31 | 116,351 |  |
| 40 | n | `obtener respuesta rápido de` |  | 23,085 | 21,152 | 3.54 | 0.29 | 113,234 |  |
| 41 | n | `acero inoxidable` |  | 6,415 | 5,717 | 12.45 | 0.89 | 111,501 |  |
| 42 | n | `política de privacidad` |  | 7,728 | 7,166 | 11.01 | 0.80 | 110,735 |  |
| 43 | n | `acceso a` |  | 22,078 | 19,832 | 4.42 | 0.36 | 105,912 |  |
| 44 | n | `dato personal` |  | 12,239 | 10,679 | 7.35 | 0.56 | 103,968 |  |
| 45 | n | `que no haber` |  | 24,029 | 21,967 | 4.11 | 0.34 | 100,857 |  |
| 46 | n | `comparar tu pasaje aereo` |  | 7,657 | 7,466 | 10.27 | 0.75 | 99,602 |  |
| 47 | n | `más información` |  | 20,913 | 19,271 | 4.70 | 0.38 | 99,545 |  |
| 48 | n | `necesario para` |  | 18,220 | 16,837 | 4.99 | 0.40 | 99,385 |  |
| 49 | n | `vuelo barato` |  | 12,288 | 9,271 | 6.97 | 0.54 | 97,945 |  |
| 50 | n | `utilizar nuestro buscador de` |  | 19,940 | 18,552 | 3.54 | 0.29 | 97,412 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `reservar se` | `reservarse` | 5,676 | 5,545 | 6.26 | 0.44 | 39,137 |
| `proporcionar se` | `proporcionarse` | 2,519 | 2,469 | 4.59 | 0.30 | 11,353 |
| `traducir se` | `traducirse` | 1,523 | 1,480 | 6.48 | 0.40 | 11,024 |
| `visualizar se` | `visualizarse` | 1,262 | 1,248 | 7.24 | 0.44 | 10,677 |

## Rank shifts against the live snapshot (`reference/lemmas/es.json`)

Live list 20,000 lemmas, this build 198,751; 18,962 shared. Spearman rank correlation on the shared lemmas 0.920; median rank ratio 1.09x.
Overlap of this build's top-k with the live top-k: top 1,000 87.4%, top 5,000 85.2%, top 20,000 85.4%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 931 | -17,524 |
| `diecinueve` | 18282 | 1361 | -16,921 |
| `dividirse` | 19076 | 3877 | -15,199 |
| `descanso` | 17625 | 2544 | -15,081 |
| `torno` | 17613 | 2674 | -14,939 |
| `respaldo` | 18269 | 3512 | -14,757 |
| `seiscientos` | 17737 | 3309 | -14,428 |
| `coco` | 18793 | 4486 | -14,307 |
| `parto` | 17982 | 4086 | -13,896 |
| `diecisiete` | 14631 | 1184 | -13,447 |
| `conforme` | 15056 | 1957 | -13,099 |
| `entregarse` | 17153 | 4092 | -13,061 |
| `quinientos` | 14749 | 1831 | -12,918 |
| `cuatrocientos` | 15401 | 2536 | -12,865 |
| `empotrar` | 17238 | 4494 | -12,744 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `obtené` | 1935 | 186670 | +184,735 |
| `feriar` | 2112 | 175836 | +173,724 |
| `del` | 11 | 144506 | +144,495 |
| `mas` | 757 | 130419 | +129,662 |
| `brusela` | 2422 | 99983 | +97,561 |
| `véase` | 3437 | 90861 | +87,424 |
| `dallar` | 3511 | 81198 | +77,687 |
| `capar` | 4795 | 76344 | +71,549 |
| `pa` | 3676 | 65044 | +61,368 |
| `sopar` | 4650 | 62971 | +58,321 |
| `marrueco` | 3509 | 60214 | +56,705 |
| `ucranio` | 3401 | 55340 | +51,939 |
| `huevar` | 4037 | 53099 | +49,062 |
| `hondura` | 3735 | 48163 | +44,428 |
| `resinar` | 4093 | 48488 | +44,395 |

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
| `del` | 11 | 144506 | +144,495 |
| `parte` | 59 | 14843 | +14,784 |
| `vario` | 265 | 15347 | +15,082 |
| `relacionado` | 386 | - | - |
| `vacación` | 390 | 28313 | +27,923 |
| `jetcost` | 494 | - | - |
| `the` | 531 | - | - |
| `cookies` | 565 | - | - |
| `aereos` | 595 | - | - |
| `u` | 628 | 5758 | +5,130 |
| `industriar` | 661 | 27562 | +26,901 |
| `frente` | 673 | - | - |
| `mas` | 757 | 130419 | +129,662 |
| `in` | 802 | - | - |
| `acondicionado` | 836 | - | - |

## Ported frequer checks

### Form-ratio outliers (224)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 8,815,852 | median form 60.5; `de` 7,602,335 (125658x), `del` 1,116,771 (18459x), `De` 66,891 (1106x) |
| 6 | `a` | 2,433,526 | median form 138.5; `a` 1,886,118 (13618x), `al` 436,540 (3152x) |
| 7 | `que` | 2,116,286 | median form 3; `que` 2,106,677 (702226x), `Que` 7,713 (2571x) |
| 8 | `los` | 1,751,679 | median form 1497.5; `los` 1,550,152 (1035x) |
| 9 | `ser` | 1,521,218 | median form 51; `es` 660,826 (12957x), `son` 168,181 (3298x), `ser` 137,795 (2702x), `fue` 86,731 (1701x) |
| 10 | `para` | 1,330,434 | median form 3; `para` 1,220,944 (406981x), `Para` 105,507 (35169x) |
| 11 | `con` | 1,137,396 | median form 13; `con` 1,089,681 (83822x), `Con` 45,616 (3509x) |
| 14 | `una` | 906,112 | median form 8.5; `una` 858,166 (100961x), `Una` 46,471 (5467x) |
| 16 | `por` | 794,052 | median form 2; `por` 719,515 (359758x), `Por` 72,313 (36156x) |
| 19 | `poder` | 639,649 | median form 36.5; `puede` 205,830 (5639x), `pueden` 98,692 (2704x), `puedes` 43,597 (1194x) |
| 21 | `haber` | 589,890 | median form 16; `ha` 167,848 (10490x), `han` 77,086 (4818x), `hay` 74,545 (4659x), `había` 38,085 (2380x) |
| 23 | `más` | 551,722 | median form 6; `más` 507,421 (84570x), `Más` 27,483 (4580x), `mas` 12,845 (2141x) |
| 24 | `estar` | 551,631 | median form 51.5; `está` 193,439 (3756x), `están` 84,176 (1634x) |
| 28 | `tener` | 422,055 | median form 20; `tiene` 117,588 (5879x), `tienen` 49,087 (2454x), `tener` 48,512 (2426x), `tienes` 20,307 (1015x) |
| 29 | `como` | 405,856 | median form 79; `como` 377,987 (4785x) |
| 31 | `lo` | 356,641 | median form 4; `lo` 331,400 (82850x), `Lo` 24,685 (6171x) |
| 32 | `hacer` | 350,537 | median form 7; `hacer` 108,209 (15458x), `hace` 49,304 (7043x), `hecho` 20,223 (2889x), `haciendo` 15,260 (2180x) |
| 38 | `sobre` | 215,779 | median form 42; `sobre` 210,352 (5008x) |
| 40 | `también` | 173,258 | median form 11; `también` 135,717 (12338x), `También` 37,396 (3400x) |
| 41 | `desde` | 167,334 | median form 115.5; `desde` 146,096 (1265x) |
| 43 | `encontrar` | 163,368 | median form 6.5; `encontrar` 63,105 (9708x), `Encuentra` 33,038 (5083x), `encontrarás` 10,693 (1645x), `encontrado` 7,270 (1118x) |
| 46 | `pero` | 159,415 | median form 1.5; `pero` 121,964 (81309x), `Pero` 37,278 (24852x) |
| 55 | `ver` | 149,747 | median form 11; `ver` 54,771 (4979x), `Ver` 21,271 (1934x) |
| 56 | `cuando` | 147,992 | median form 2; `cuando` 106,874 (53437x), `Cuando` 40,983 (20492x) |
| 60 | `deber` | 140,235 | median form 34; `debe` 46,543 (1369x) |

_199 more not shown._

### Singular/plural mismatch (192)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `los` | 1,751,679 | `lo` lemmatises to `lo` (rank 31) |
| 13 | `las` | 1,064,165 | `la` lemmatises to `la` (rank 2) |
| 23 | `más` | 551,722 | `má` lemmatises to `má` (rank 56,597) |
| 42 | `dos` | 163,483 | `do` lemmatises to `do` (rank 3,516) |
| 84 | `tres` | 99,543 | `tre` lemmatises to `tre` (rank 24,416) |
| 84 | `tres` | 99,543 | `tr` lemmatises to `tr` (rank 14,849) |
| 107 | `después` | 77,956 | `despué` lemmatises to `despué` (rank 125,041) |
| 135 | `nos` | 65,412 | `no` lemmatises to `no` (rank 17) |
| 143 | `antes` | 62,958 | `ante` lemmatises to `ante` (rank 741) |
| 143 | `antes` | 62,958 | `ant` lemmatises to `ant` (rank 26,656) |
| 161 | `dios` | 60,077 | `dio` lemmatises to `dar` (rank 70) |
| 173 | `además` | 56,335 | `ademá` lemmatises to `ademá` (rank 164,880) |
| 188 | `menos` | 52,990 | `meno` lemmatises to `meno` (rank 16,065) |
| 201 | `ellos` | 50,547 | `ello` lemmatises to `ello` (rank 683) |
| 212 | `unos` | 48,531 | `uno` lemmatises to `uno` (rank 52) |
| 217 | `nosotros` | 47,781 | `nosotro` lemmatises to `nosotro` (rank 154,791) |
| 223 | `mientras` | 46,625 | `mientra` lemmatises to `mientra` (rank 130,832) |
| 256 | `varios` | 42,303 | `vario` lemmatises to `vario` (rank 15,347) |
| 258 | `les` | 41,762 | `le` lemmatises to `le` (rank 58) |
| 269 | `mes` | 39,946 | `me` lemmatises to `me` (rank 93) |
| 302 | `seis` | 37,199 | `sei` lemmatises to `sei` (rank 37,579) |
| 336 | `entonces` | 33,876 | `entonce` lemmatises to `entonce` (rank 86,862) |
| 360 | `gracias` | 31,841 | `gracia` lemmatises to `gracia` (rank 2,939) |
| 385 | `inglés` | 30,586 | `inglé` lemmatises to `inglé` (rank 179,701) |
| 391 | `vacaciones` | 30,057 | `vacacion` lemmatises to `vacacion` (rank 136,991) |

_167 more not shown._

### Lemma consistency (334)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 99 | `te` | 86,136 | alone, `te` lemmatises to `se` (rank 18) |
| 352 | `lista` | 32,340 | alone, `lista` lemmatises to `listo` (rank 1,132) |
| 395 | `política` | 29,853 | alone, `política` lemmatises to `político` (rank 717) |
| 523 | `dicho` | 23,134 | alone, `dicho` lemmatises to `decir` (rank 61) |
| 562 | `hecho` | 21,856 | alone, `hecho` lemmatises to `hacer` (rank 32) |
| 576 | `china` | 21,397 | alone, `china` lemmatises to `chino` (rank 1,656) |
| 603 | `presente` | 19,976 | alone, `presente` lemmatises to `presentar` (rank 289) |
| 606 | `fuera` | 19,907 | alone, `fuera` lemmatises to `ser` (rank 9) |
| 611 | `abierto` | 19,826 | alone, `abierto` lemmatises to `abrir` (rank 328) |
| 642 | `ayuda` | 18,893 | alone, `ayuda` lemmatises to `ayudar` (rank 92) |
| 733 | `compra` | 17,255 | alone, `compra` lemmatises to `comprar` (rank 227) |
| 765 | `visita` | 16,592 | alone, `visita` lemmatises to `visitar` (rank 382) |
| 812 | `corto` | 15,655 | alone, `corto` lemmatises to `cortar` (rank 1,430) |
| 824 | `causa` | 15,371 | alone, `causa` lemmatises to `causar` (rank 693) |
| 843 | `carga` | 14,995 | alone, `carga` lemmatises to `cargar` (rank 1,449) |
| 880 | `pedido` | 14,360 | alone, `pedido` lemmatises to `pedir` (rank 512) |
| 883 | `os` | 14,294 | alone, `os` lemmatises to `se` (rank 18) |
| 1026 | `vivo` | 12,385 | alone, `vivo` lemmatises to `vivir` (rank 301) |
| 1093 | `deseo` | 11,540 | alone, `deseo` lemmatises to `desear` (rank 308) |
| 1116 | `empleado` | 11,325 | alone, `empleado` lemmatises to `emplear` (rank 1,677) |
| 1171 | `avanzado` | 10,605 | alone, `avanzado` lemmatises to `avanzar` (rank 2,016) |
| 1173 | `parís` | 10,600 | alone, `parís` lemmatises to `parir` (rank 14,549) |
| 1181 | `falta` | 10,483 | alone, `falta` lemmatises to `faltar` (rank 2,128) |
| 1220 | `vino` | 10,044 | alone, `vino` lemmatises to `venir` (rank 270) |
| 1230 | `aumento` | 9,973 | alone, `aumento` lemmatises to `aumentar` (rank 418) |

_309 more not shown._

### Short lemmas (166)

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
| 67 | `mi` | 121,962 | `mi` -> `mi`, `mis` -> `mi`, `Mis` -> `mi`, `Mi` -> `mi`, `MI` -> `mi` |
| 75 | `ir` | 111,740 | `fuese` -> `ir`, `iba` -> `ir`, `ir` -> `ir`, `vaya` -> `ir`, `va` -> `ir` |
| 88 | `ya` | 95,657 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya`, `-ya` -> `?` |
| 93 | `me` | 89,677 | `me` -> `me`, `Me` -> `me`, `ME` -> `me` |
| 99 | `te` | 86,136 | `te` -> `se`, `Te` -> `te`, `TE` -> `te`, `tes` -> `te` |
| 116 | `él` | 73,977 | `él` -> `él`, `Él` -> `él`, `ÉL` -> `él`, `Èl` -> `él`, `-él` -> `?` |
| 207 | `yo` | 49,631 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo`, `yas` -> `yas`, `yos` -> `yo` |
| 238 | `ni` | 44,387 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni`, `niٌos` -> `?`, `nilos` -> `nilo` |
| 366 | `sí` | 31,593 | `sí` -> `sí`, `si` -> `si`, `Sí` -> `sí`, `SÍ` -> `sí`, `SíEs` -> `sí` |
| 510 | `ti` | 23,739 | `ti` -> `ti`, `TI` -> `ti`, `Ti` -> `ti`, `Tí` -> `ti`, `TÍ` -> `ti` |

_141 more not shown._

### Case merges (1)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4895 | `editorial#Fem` | 1,481 | capitalised but mostly ADJ; no lowercase twin |

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 682 (68.2%).

Ours only: `poder + infinitivo`, `haber + participio`, `se + verbo (impersonal/pasiva)`, `ser + participio`, `vuelo`, `hotel`, `estar + gerundio`, `te`, `archivo`, `habitación`, `barato`, `al + infinitivo`, `a través de`, `lo + adjetivo`, `encontrarse`, `después de`, `para que`, `tener que + infinitivo`, `diseño`, `alojamiento`, `disponible`, `sitio web`, `oferta`, `proporcionar`, `alquiler`

wordfreq only: `nadie`, `mal`, `dr`, `ahí`, `argentino`, `cero`, `listo`, `faltar`, `unido`, `mierda`, `the`, `i`, `c`, `viejo`, `policía`, `elección`, `juan`, `orden#Masc`, `peor`, `voz`, `hola`, `paz`, `militar`, `cargo`, `matar`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 531 | `cookie` | 22,682 | wordfreq zipf en 4.1 vs es 3.0 |
| 539 | `low` | 22,404 | wordfreq zipf en 5.3 vs es 3.6 |
| 548 | `cost` | 22,200 | wordfreq zipf en 5.2 vs es 3.3 |
| 816 | `metro#metre` | 15,508 | wordfreq zipf en 3.6 vs es 1.6 |
| 892 | `once` | 14,227 | wordfreq zipf en 5.5 vs es 4.4 |
| 1473 | `i` | 8,046 | wordfreq zipf en 7.1 vs es 5.4 |
| 1546 | `led` | 7,657 | wordfreq zipf en 5.1 vs es 3.7 |
| 1910 | `resort` | 5,992 | wordfreq zipf en 4.4 vs es 3.3 |
| 2118 | `show` | 5,305 | wordfreq zipf en 5.7 vs es 4.6 |
| 2643 | `top` | 3,882 | wordfreq zipf en 5.6 vs es 4.4 |
| 2817 | `look` | 3,581 | wordfreq zipf en 5.8 vs es 3.9 |
| 2970 | `stock` | 3,300 | wordfreq zipf en 4.9 vs es 3.8 |
| 2974 | `set` | 3,296 | wordfreq zipf en 5.6 vs es 4.1 |
| 3063 | `reserve` | 3,137 | wordfreq zipf en 4.6 vs es 3.1 |
| 3128 | `center` | 3,040 | wordfreq zipf en 5.2 vs es 4.2 |
| 3191 | `lake` | 2,939 | wordfreq zipf en 4.8 vs es 3.5 |
| 3471 | `street` | 2,572 | wordfreq zipf en 5.3 vs es 4.2 |
| 3493 | `parking` | 2,538 | wordfreq zipf en 4.5 vs es 3.1 |
| 3496 | `blue` | 2,536 | wordfreq zipf en 5.1 vs es 4.0 |
| 3509 | `cloud` | 2,522 | wordfreq zipf en 4.5 vs es 3.4 |
| 3516 | `do` | 2,515 | wordfreq zipf en 6.3 vs es 4.6 |
| 3646 | `ticket` | 2,380 | wordfreq zipf en 4.6 vs es 3.5 |
| 3701 | `green` | 2,308 | wordfreq zipf en 5.1 vs es 4.1 |
| 3750 | `as` | 2,270 | wordfreq zipf en 6.8 vs es 4.7 |
| 3754 | `port` | 2,268 | wordfreq zipf en 4.7 vs es 3.6 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 161 | `dios` | 60,077 | PROPN 0%, capitalised forms 94% |
| 294 | `tom` | 37,875 | PROPN 100%, capitalised forms 100% |
| 367 | `estados unidos` | 31,586 | PROPN 0%, capitalised forms 100% |
| 440 | `españa` | 27,603 | PROPN 100%, capitalised forms 100% |
| 499 | `san` | 24,279 | PROPN 2%, capitalised forms 96% |
| 576 | `china` | 21,397 | PROPN 100%, capitalised forms 100% |
| 622 | `tripadvisor` | 19,618 | PROPN 100%, capitalised forms 100% |
| 663 | `jesús` | 18,581 | PROPN 100%, capitalised forms 100% |
| 709 | `méxico` | 17,692 | PROPN 100%, capitalised forms 100% |
| 718 | `europa` | 17,568 | PROPN 99%, capitalised forms 100% |
| 727 | `tv` | 17,411 | PROPN 6%, capitalised forms 97% |
| 851 | `barcelona` | 14,829 | PROPN 100%, capitalised forms 100% |
| 864 | `madrid` | 14,651 | PROPN 99%, capitalised forms 99% |
| 942 | `google` | 13,390 | PROPN 98%, capitalised forms 98% |
| 1007 | `israel` | 12,587 | PROPN 100%, capitalised forms 100% |
| 1159 | `cristo` | 10,872 | PROPN 98%, capitalised forms 100% |
| 1167 | `nueva york` | 10,712 | PROPN 100%, capitalised forms 100% |
| 1173 | `parís` | 10,600 | PROPN 99%, capitalised forms 100% |
| 1194 | `francia` | 10,294 | PROPN 100%, capitalised forms 100% |
| 1196 | `windows` | 10,276 | PROPN 100%, capitalised forms 100% |
| 1255 | `londres` | 9,732 | PROPN 100%, capitalised forms 100% |
| 1303 | `mary` | 9,271 | PROPN 100%, capitalised forms 100% |
| 1346 | `wi-fi` | 9,008 | PROPN 1%, capitalised forms 97% |
| 1366 | `alemania` | 8,805 | PROPN 100%, capitalised forms 100% |
| 1369 | `inn` | 8,791 | PROPN 100%, capitalised forms 100% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 99.0% | 0.998 |
| juilland_u | 99.9% | 1.000 |
| juilland_u_corrected | 99.9% | 1.000 |
| dp_adjusted | 99.7% | 1.000 |
| cd_blend | 99.5% | 0.999 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `imprescindible` | 4376 | 4223 | -153 | 1,816 | 1,803 | 0.974 | 0.105 |
| `si bien` | 5039 | 4888 | -151 | 1,442 | 1,435 | 0.976 | 0.095 |
| `originalmente` | 4388 | 4238 | -150 | 1,809 | 1,793 | 0.978 | 0.094 |
| `estar sujeto a algo` | 4440 | 4290 | -150 | 1,775 | 1,758 | 0.975 | 0.095 |
| `triponline` | 4673 | 4526 | -147 | 1,633 | 1,626 | 0.973 | 0.105 |
| `tomás` | 4011 | 6749 | +2,738 | 2,086 | 839 | 0.930 | 0.270 |
| `love` | 3113 | 5047 | +1,934 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4500 | 6152 | +1,652 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4976 | 6346 | +1,370 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4228 | 5569 | +1,341 | 1,912 | 1,158 | 0.967 | 0.136 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `básicamente` | 4365 | 4337 | -28 | 1,825 | 1,801 | 0.981 | 0.073 |
| `desafiar` | 5006 | 4986 | -20 | 1,462 | 1,438 | 0.978 | 0.086 |
| `conectarse` | 4589 | 4569 | -20 | 1,682 | 1,647 | 0.979 | 0.089 |
| `subrayar` | 4761 | 4742 | -19 | 1,584 | 1,570 | 0.978 | 0.085 |
| `homenaje` | 4739 | 4720 | -19 | 1,593 | 1,568 | 0.980 | 0.083 |
| `tomás` | 4011 | 4108 | +97 | 2,086 | 839 | 0.930 | 0.270 |
| `canadiense` | 4292 | 4331 | +39 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1308 | 1344 | +36 | 9,271 | 3,893 | 0.966 | 0.131 |
| `casado` | 4245 | 4278 | +33 | 1,901 | 1,716 | 0.966 | 0.117 |
| `ascendente` | 4500 | 4532 | +32 | 1,733 | 975 | 0.962 | 0.160 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `escáner` | 4889 | 4878 | -11 | 1,520 | 1,390 | 0.975 | 0.102 |
| `incentivo` | 4886 | 4875 | -11 | 1,521 | 1,469 | 0.974 | 0.105 |
| `esencialmente` | 4980 | 4969 | -11 | 1,474 | 1,463 | 0.975 | 0.104 |
| `contabilidad` | 4982 | 4971 | -11 | 1,473 | 1,374 | 0.974 | 0.104 |
| `desafortunadamente` | 5005 | 4995 | -10 | 1,463 | 1,430 | 0.974 | 0.107 |
| `tomás` | 4011 | 4109 | +98 | 2,086 | 839 | 0.930 | 0.270 |
| `canadiense` | 4292 | 4329 | +37 | 1,869 | 1,677 | 0.959 | 0.130 |
| `mary` | 1308 | 1344 | +36 | 9,271 | 3,893 | 0.966 | 0.131 |
| `casado` | 4245 | 4278 | +33 | 1,901 | 1,716 | 0.966 | 0.117 |
| `ascendente` | 4500 | 4531 | +31 | 1,733 | 975 | 0.962 | 0.160 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `procurar` | 4297 | 4208 | -89 | 1,867 | 1,844 | 0.981 | 0.070 |
| `desafiar` | 5006 | 4929 | -77 | 1,462 | 1,438 | 0.978 | 0.086 |
| `básicamente` | 4365 | 4289 | -76 | 1,825 | 1,801 | 0.981 | 0.073 |
| `urgencia` | 5072 | 4997 | -75 | 1,425 | 1,385 | 0.977 | 0.089 |
| `consistente` | 4877 | 4807 | -70 | 1,522 | 1,500 | 0.978 | 0.088 |
| `tomás` | 4011 | 4558 | +547 | 2,086 | 839 | 0.930 | 0.270 |
| `ascendente` | 4500 | 4683 | +183 | 1,733 | 975 | 0.962 | 0.160 |
| `love` | 3113 | 3246 | +133 | 3,093 | 1,365 | 0.966 | 0.140 |
| `model` | 4976 | 5100 | +124 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4228 | 4344 | +116 | 1,912 | 1,158 | 0.967 | 0.136 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `caracterizarse por algo` | 4629 | 4545 | -84 | 1,661 | 1,647 | 0.976 | 0.096 |
| `en efecto` | 4998 | 4914 | -84 | 1,465 | 1,456 | 0.975 | 0.100 |
| `exquisito` | 4617 | 4534 | -83 | 1,668 | 1,655 | 0.973 | 0.109 |
| `rapidez` | 4294 | 4212 | -82 | 1,868 | 1,852 | 0.976 | 0.091 |
| `transcurso` | 4618 | 4536 | -82 | 1,668 | 1,654 | 0.977 | 0.094 |
| `tomás` | 4011 | 5222 | +1,211 | 2,086 | 839 | 0.930 | 0.270 |
| `love` | 3113 | 3975 | +862 | 3,093 | 1,365 | 0.966 | 0.140 |
| `ascendente` | 4500 | 5294 | +794 | 1,733 | 975 | 0.962 | 0.160 |
| `model` | 4976 | 5634 | +658 | 1,475 | 925 | 0.965 | 0.148 |
| `remate` | 4228 | 4866 | +638 | 1,912 | 1,158 | 0.967 | 0.136 |

## Excluded lemmas

`es.tsv` (sha256 `0a673dd915041b5c`) lists 1,242 exclusions; 1,245 lemmas were dropped from the top 50,000 before cutting it (exclude-boilerplate 273, exclude-english 969, exclude-unit 3). Lower ranks moved up.

| rank before | lemma | class | reason |
|---|---|---|---|
| 477 | `jetcost` | exclude-boilerplate | flight-search site brand |
| 576 | `aereo` | exclude-boilerplate | unaccented template spelling of aéreo |
| 754 | `the` | exclude-english | English article |
| 1223 | `of` | exclude-english | English preposition |
| 1305 | `city` | exclude-english | English word in names |
| 1472 | `in` | exclude-english | English preposition |
| 1636 | `and` | exclude-english | English conjunction |
| 1793 | `beach` | exclude-english | not a Spanish loan |
| 1962 | `new` | exclude-english | English template text |
| 2122 | `home` | exclude-english | English template text |
| 2439 | `to` | exclude-english | English preposition |
| 2546 | `house` | exclude-english | English template text |
| 2689 | `by` | exclude-english | English preposition |
| 2812 | `black` | exclude-english | English colour word |
| 2905 | `grand` | exclude-english | English in brand names |
| 2916 | `airport` | exclude-english | English for aeropuerto |
| 3032 | `island` | exclude-english | English place word |
| 3057 | `on` | exclude-english | English preposition |
| 3106 | `international` | exclude-english | English for internacional |
| 3113 | `love` | exclude-english | English word |
| 3149 | `for` | exclude-english | English preposition |
| 3164 | `air` | exclude-english | English in brand names |
| 3166 | `best` | exclude-english | English word |
| 3179 | `west` | exclude-english | English place word |
| 3186 | `ltd` | exclude-boilerplate | company-name template suffix |
| 3290 | `world` | exclude-english | English word |
| 3299 | `group` | exclude-english | English word in names |
| 3476 | `english` | exclude-english | English word |
| 3521 | `car` | exclude-english | English word |
| 3556 | `one` | exclude-english | English word |
| 3660 | `white` | exclude-english | English colour word |
| 3669 | `mainland` | exclude-english | English listing text |
| 3685 | `us` | exclude-english | English pronoun/domain |
| 3696 | `am` | exclude-english | English time suffix |
| 3718 | `file` | exclude-english | English for archivo |
| 3747 | `business` | exclude-english | English word |
| 3760 | `free` | exclude-english | English word |
| 3796 | `north` | exclude-english | English place word |
| 3849 | `western` | exclude-english | English word |
| 3853 | `american` | exclude-english | English word |
| 3888 | `studio` | exclude-english | English hotel template word |
| 3947 | `office` | exclude-english | English word |
| 4025 | `county` | exclude-english | English place word |
| 4063 | `state` | exclude-english | English word |
| 4155 | `bed` | exclude-english | English word |
| 4206 | `south` | exclude-english | English place word |
| 4274 | `live` | exclude-english | English word |
| 4287 | `store` | exclude-english | English word |
| 4320 | `big` | exclude-english | English word |
| 4387 | `power` | exclude-english | English word |
| 4394 | `at` | exclude-english | English preposition |
| 4444 | `industry` | exclude-english | English template text |
| 4496 | `my` | exclude-english | English pronoun |
| 4547 | `design` | exclude-english | English for diseño |
| 4573 | `play` | exclude-english | English word |
| 4616 | `gold` | exclude-english | English word |
| 4680 | `london` | exclude-english | English form of Londres |
| 4693 | `hi` | exclude-english | English greeting |
| 4708 | `client` | exclude-english | English for cliente |
| 4721 | `east` | exclude-english | English place word |

_1,185 more in the exclusion file._

## Convergence

One row per counted shard: the shards counted so far, in the order they finished. Per band N: **chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement (1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each source; a source with an odd count leaves its newest shard out). Stopping rule: 3 consecutive full-mix checkpoints with split <= 5% at 20k and <= 10% at 50k.

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 751,237 | tatoeba-spa 751,237 | partial (lacks paracrawl-en-es, tatoeba-spa) | - | - | 6 | - | - | - | 2 | - | - | - | - | - | - | - | - | - | 0/3 |
| 1,510,432 | tatoeba-spa 1,510,432 | partial (lacks paracrawl-en-es, tatoeba-spa) | 7.7% | 153 | 12 | 15.5% | 11.7% | 391 | 3 | 23.5% | - | 1,024 | 1 | - | - | 1,194 | - | - | 0/3 |
| 2,256,931 | tatoeba-spa 2,256,931 | partial (lacks paracrawl-en-es, tatoeba-spa) | 6.7% | 127 | 19 | 15.5% | 10.2% | 331 | 5 | 23.5% | 17.1% | 952 | 1 | - | - | 1,737 | - | - | 0/3 |
| 2,594,302 | tatoeba-spa 2,594,302 | partial (lacks paracrawl-en-es, tatoeba-spa) | 3.8% | 67 | 23 | 14.5% | 6.3% | 188 | 7 | 21.3% | 10.7% | 583 | 2 | 32.0% | - | 2,126 | - | - | 0/3 |
| 3,326,967 | tatoeba-spa 3,326,967 | partial (lacks paracrawl-en-es) | 4.7% | 86 | 31 | 14.5% | 6.6% | 234 | 10 | 21.3% | 9.9% | 651 | 2 | 32.0% | - | 2,874 | - | - | 0/3 |
| 6,254,960 | paracrawl-en-es 2,927,993, tatoeba-spa 3,326,967 | full | 18.5% | 570 | 79 | 14.5% | 19.2% | 1,084 | 24 | 21.3% | 22.1% | 2,047 | 7 | 32.0% | - | 4,786 | 1 | - | 0/3 |
| 9,178,731 | paracrawl-en-es 5,851,764, tatoeba-spa 3,326,967 | full | 5.2% | 206 | 121 | 5.8% | 5.6% | 354 | 37 | 9.0% | 7.1% | 693 | 11 | 15.7% | 14.8% | 2,004 | 2 | 35.4% | 0/3 |
| 12,101,309 | paracrawl-en-es 8,774,342, tatoeba-spa 3,326,967 | full | 2.8% | 100 | 162 | 5.8% | 3.2% | 179 | 50 | 9.0% | 4.4% | 387 | 14 | 15.7% | 9.7% | 1,368 | 3 | 35.4% | 0/3 |
| 15,026,231 | paracrawl-en-es 11,699,264, tatoeba-spa 3,326,967 | full | 1.7% | 61 | 204 | 4.2% | 2.1% | 113 | 63 | 6.6% | 3.1% | 263 | 18 | 11.7% | 7.2% | 1,000 | 4 | 26.9% | 0/3 |
| 17,951,107 | paracrawl-en-es 14,624,140, tatoeba-spa 3,326,967 | full | 1.1% | 39 | 244 | 4.2% | 1.3% | 78 | 76 | 6.6% | 2.5% | 194 | 22 | 11.7% | 5.4% | 822 | 4 | 26.9% | 0/3 |
| 20,882,602 | paracrawl-en-es 17,555,635, tatoeba-spa 3,326,967 | full | 1.0% | 30 | 287 | 3.6% | 1.3% | 61 | 88 | 5.3% | 2.0% | 158 | 26 | 9.6% | 4.7% | 675 | 5 | 22.3% | 0/3 |
| 23,810,949 | paracrawl-en-es 20,483,982, tatoeba-spa 3,326,967 | full | 1.0% | 24 | 326 | 3.6% | 1.1% | 51 | 101 | 5.3% | 1.7% | 134 | 29 | 9.6% | 4.2% | 583 | 6 | 22.3% | 0/3 |
| 26,731,666 | paracrawl-en-es 23,404,699, tatoeba-spa 3,326,967 | full | 0.6% | 19 | 366 | 3.0% | 0.9% | 42 | 113 | 4.6% | 1.6% | 113 | 33 | 8.5% | 3.5% | 494 | 6 | 19.5% | 0/3 |
| 29,659,297 | paracrawl-en-es 26,332,330, tatoeba-spa 3,326,967 | full | 0.6% | 15 | 408 | 3.0% | 0.8% | 36 | 126 | 4.6% | 1.4% | 99 | 37 | 8.5% | 3.1% | 450 | 7 | 19.5% | 0/3 |
| 32,587,144 | paracrawl-en-es 29,260,177, tatoeba-spa 3,326,967 | full | 0.5% | 14 | 449 | 2.5% | 0.7% | 31 | 139 | 4.2% | 1.3% | 90 | 40 | 7.7% | 2.9% | 413 | 8 | 17.5% | 0/3 |
| 35,512,005 | paracrawl-en-es 32,185,038, tatoeba-spa 3,326,967 | full | 0.4% | 12 | 488 | 2.5% | 0.6% | 28 | 151 | 4.2% | 1.2% | 78 | 44 | 7.7% | 2.5% | 376 | 8 | 17.5% | 0/3 |
| 38,433,077 | paracrawl-en-es 35,106,110, tatoeba-spa 3,326,967 | full | 0.3% | 11 | 530 | 2.3% | 0.5% | 25 | 164 | 3.8% | 1.0% | 69 | 48 | 7.0% | 2.3% | 337 | 9 | 15.9% | 0/3 |
| 41,363,134 | paracrawl-en-es 38,036,167, tatoeba-spa 3,326,967 | full | 0.3% | 9 | 568 | 2.3% | 0.5% | 23 | 176 | 3.8% | 0.9% | 65 | 51 | 7.0% | 2.1% | 316 | 10 | 15.9% | 0/3 |
| 44,287,245 | paracrawl-en-es 40,960,278, tatoeba-spa 3,326,967 | full | 0.3% | 9 | 607 | 2.0% | 0.5% | 21 | 189 | 3.5% | 0.8% | 61 | 55 | 6.4% | 2.0% | 289 | 10 | 14.8% | 0/3 |
| 47,218,861 | paracrawl-en-es 43,891,894, tatoeba-spa 3,326,967 | full | 0.3% | 8 | 647 | 2.0% | 0.5% | 19 | 201 | 3.5% | 0.7% | 57 | 59 | 6.4% | 1.9% | 273 | 11 | 14.8% | 0/3 |
| 50,146,705 | paracrawl-en-es 46,819,738, tatoeba-spa 3,326,967 | full | 0.3% | 7 | 687 | 2.1% | 0.4% | 18 | 214 | 3.4% | 0.7% | 54 | 62 | 5.9% | 1.8% | 274 | 12 | 13.8% | 0/3 |
| 53,076,631 | paracrawl-en-es 49,749,664, tatoeba-spa 3,326,967 | full | 0.3% | 7 | 731 | 2.1% | 0.4% | 17 | 227 | 3.4% | 0.8% | 50 | 66 | 5.9% | 1.7% | 245 | 12 | 13.8% | 0/3 |
| 55,999,851 | paracrawl-en-es 52,672,884, tatoeba-spa 3,326,967 | full | 0.3% | 6 | 772 | 2.0% | 0.4% | 16 | 240 | 3.2% | 0.6% | 48 | 69 | 5.6% | 1.5% | 238 | 13 | 13.0% | 0/3 |
| 58,918,566 | paracrawl-en-es 55,591,599, tatoeba-spa 3,326,967 | full | 0.2% | 6 | 813 | 2.0% | 0.3% | 15 | 251 | 3.2% | 0.7% | 45 | 73 | 5.6% | 1.5% | 227 | 14 | 13.0% | 0/3 |
| 61,845,621 | paracrawl-en-es 58,518,654, tatoeba-spa 3,326,967 | full | 0.2% | 5 | 853 | 1.8% | 0.4% | 13 | 264 | 3.1% | 0.6% | 42 | 77 | 5.3% | 1.4% | 207 | 14 | 12.4% | 0/3 |
| 64,770,777 | paracrawl-en-es 61,443,810, tatoeba-spa 3,326,967 | full | 0.2% | 5 | 894 | 1.8% | 0.3% | 13 | 277 | 3.1% | 0.6% | 41 | 80 | 5.3% | 1.3% | 196 | 15 | 12.4% | 0/3 |
| 67,693,928 | paracrawl-en-es 64,366,961, tatoeba-spa 3,326,967 | full | 0.2% | 5 | 934 | 1.7% | 0.3% | 12 | 290 | 3.0% | 0.6% | 38 | 84 | 5.1% | 1.3% | 193 | 16 | 11.9% | 0/3 |
| 70,618,495 | paracrawl-en-es 67,291,528, tatoeba-spa 3,326,967 | full | 0.3% | 5 | 975 | 1.7% | 0.3% | 12 | 302 | 3.0% | 0.6% | 36 | 88 | 5.1% | 1.3% | 188 | 16 | 11.9% | 0/3 |
| 73,541,302 | paracrawl-en-es 70,214,335, tatoeba-spa 3,326,967 | full | 0.3% | 4 | 1,014 | 1.7% | 0.3% | 11 | 315 | 2.8% | 0.5% | 35 | 91 | 4.8% | 1.1% | 178 | 17 | 11.3% | 0/3 |
| 76,465,894 | paracrawl-en-es 73,138,927, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 1,054 | 1.7% | 0.3% | 11 | 327 | 2.8% | 0.5% | 34 | 95 | 4.8% | 1.1% | 178 | 18 | 11.3% | 0/3 |
| 79,391,530 | paracrawl-en-es 76,064,563, tatoeba-spa 3,326,967 | full | 0.2% | 4 | 1,096 | 1.7% | 0.3% | 10 | 340 | 2.7% | 0.5% | 32 | 98 | 4.7% | 1.1% | 159 | 18 | 10.9% | 0/3 |
| 82,315,148 | paracrawl-en-es 78,988,181, tatoeba-spa 3,326,967 | full | 0.2% | 4 | 1,135 | 1.7% | 0.3% | 10 | 351 | 2.7% | 0.5% | 31 | 102 | 4.7% | 1.0% | 167 | 19 | 10.9% | 0/3 |
| 85,246,371 | paracrawl-en-es 81,919,404, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 1,176 | 1.4% | 0.3% | 9 | 364 | 2.7% | 0.4% | 30 | 106 | 4.5% | 1.0% | 153 | 20 | 10.6% | 0/3 |
| 88,172,794 | paracrawl-en-es 84,845,827, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 1,218 | 1.4% | 0.3% | 9 | 376 | 2.7% | 0.4% | 29 | 109 | 4.5% | 1.0% | 148 | 21 | 10.6% | 0/3 |
| 91,096,569 | paracrawl-en-es 87,769,602, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 1,260 | 1.5% | 0.2% | 9 | 389 | 2.6% | 0.4% | 27 | 113 | 4.4% | 0.9% | 146 | 21 | 10.1% | 0/3 |
| 94,027,050 | paracrawl-en-es 90,700,083, tatoeba-spa 3,326,967 | full | 0.2% | 3 | 1,299 | 1.5% | 0.2% | 9 | 402 | 2.6% | 0.4% | 27 | 117 | 4.4% | 0.9% | 136 | 22 | 10.1% | 0/3 |
| 96,955,802 | paracrawl-en-es 93,628,835, tatoeba-spa 3,326,967 | full | 0.1% | 3 | 1,344 | 1.5% | 0.2% | 9 | 414 | 2.5% | 0.4% | 26 | 120 | 4.3% | 0.9% | 130 | 22 | 9.8% | 1/3 |
| 99,879,342 | paracrawl-en-es 96,552,375, tatoeba-spa 3,326,967 | full | 0.1% | 3 | 1,384 | 1.5% | 0.2% | 8 | 427 | 2.5% | 0.3% | 25 | 124 | 4.3% | 0.9% | 131 | 23 | 9.8% | 2/3 |
| 102,801,568 | paracrawl-en-es 99,474,601, tatoeba-spa 3,326,967 | full | 0.1% | 3 | 1,424 | 1.4% | 0.2% | 8 | 439 | 2.5% | 0.3% | 25 | 128 | 4.3% | 0.8% | 126 | 24 | 9.5% | 3/3 |

Decision: **stop** at 102,801,568 tokens.
Final list: 105,726,244 tokens (full).

### Calibration

Each checkpoint's full-data top N against the final list's top N (**vs final**: share of the final top N not in the checkpoint's), next to its split-half disagreement. If split-half estimates the remaining change, split ~ 2 x vs final.

| tokens | 5k split | 5k vs final | 5k ratio | 10k split | 10k vs final | 10k ratio | 20k split | 20k vs final | 20k ratio | 50k split | 50k vs final | 50k ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 751,237 | - | 33.2% | - | - | 34.3% | - | - | - | - | - | - | - |
| 1,510,432 | 15.5% | 32.7% | 0.47 | 23.5% | 33.1% | 0.71 | - | 38.9% | - | - | - | - |
| 2,256,931 | 15.5% | 33.1% | 0.47 | 23.5% | 32.9% | 0.71 | - | 37.5% | - | - | - | - |
| 2,594,302 | 14.5% | 32.7% | 0.44 | 21.3% | 32.5% | 0.66 | 32.0% | 36.3% | 0.88 | - | - | - |
| 3,326,967 | 14.5% | 32.6% | 0.45 | 21.3% | 32.5% | 0.66 | 32.0% | 36.1% | 0.89 | - | - | - |
| 6,254,960 | 14.5% | 15.0% | 0.97 | 21.3% | 15.3% | 1.39 | 32.0% | 17.8% | 1.80 | - | 27.3% | - |
| 9,178,731 | 5.8% | 10.4% | 0.55 | 9.0% | 10.5% | 0.85 | 15.7% | 13.1% | 1.19 | 35.4% | 21.2% | 1.67 |
| 12,101,309 | 5.8% | 8.0% | 0.72 | 9.0% | 8.2% | 1.09 | 15.7% | 10.7% | 1.47 | 35.4% | 17.5% | 2.03 |
| 15,026,231 | 4.2% | 6.6% | 0.64 | 6.6% | 6.9% | 0.95 | 11.7% | 9.2% | 1.27 | 26.9% | 14.7% | 1.83 |
| 17,951,107 | 4.2% | 5.7% | 0.74 | 6.6% | 6.2% | 1.06 | 11.7% | 8.2% | 1.43 | 26.9% | 13.3% | 2.02 |
| 20,882,602 | 3.6% | 4.9% | 0.74 | 5.3% | 5.5% | 0.96 | 9.6% | 7.2% | 1.32 | 22.3% | 12.1% | 1.84 |
| 23,810,949 | 3.6% | 4.3% | 0.85 | 5.3% | 4.9% | 1.06 | 9.6% | 6.7% | 1.43 | 22.3% | 11.0% | 2.03 |
| 26,731,666 | 3.0% | 3.9% | 0.77 | 4.6% | 4.6% | 1.00 | 8.5% | 6.1% | 1.38 | 19.5% | 10.2% | 1.92 |
| 29,659,297 | 3.0% | 3.5% | 0.86 | 4.6% | 4.2% | 1.08 | 8.5% | 5.8% | 1.45 | 19.5% | 9.6% | 2.04 |
| 32,587,144 | 2.5% | 3.3% | 0.75 | 4.2% | 4.0% | 1.05 | 7.7% | 5.4% | 1.41 | 17.5% | 8.9% | 1.96 |
| 35,512,005 | 2.5% | 3.1% | 0.82 | 4.2% | 3.8% | 1.10 | 7.7% | 5.0% | 1.52 | 17.5% | 8.4% | 2.09 |
| 38,433,077 | 2.3% | 2.9% | 0.81 | 3.8% | 3.6% | 1.04 | 7.0% | 4.8% | 1.44 | 15.9% | 8.0% | 1.99 |
| 41,363,134 | 2.3% | 2.8% | 0.84 | 3.8% | 3.5% | 1.08 | 7.0% | 4.6% | 1.50 | 15.9% | 7.5% | 2.12 |
| 44,287,245 | 2.0% | 2.5% | 0.80 | 3.5% | 3.3% | 1.07 | 6.4% | 4.4% | 1.46 | 14.8% | 7.1% | 2.10 |
| 47,218,861 | 2.0% | 2.4% | 0.84 | 3.5% | 3.1% | 1.13 | 6.4% | 4.2% | 1.51 | 14.8% | 6.7% | 2.20 |
| 50,146,705 | 2.1% | 2.3% | 0.90 | 3.4% | 3.1% | 1.12 | 5.9% | 4.1% | 1.44 | 13.8% | 6.5% | 2.12 |
| 53,076,631 | 2.1% | 2.2% | 0.96 | 3.4% | 3.0% | 1.16 | 5.9% | 4.0% | 1.47 | 13.8% | 6.1% | 2.27 |
| 55,999,851 | 2.0% | 2.0% | 1.02 | 3.2% | 2.9% | 1.12 | 5.6% | 3.9% | 1.45 | 13.0% | 5.9% | 2.19 |
| 58,918,566 | 2.0% | 1.9% | 1.06 | 3.2% | 2.8% | 1.16 | 5.6% | 3.7% | 1.51 | 13.0% | 5.7% | 2.29 |
| 61,845,621 | 1.8% | 1.8% | 1.01 | 3.1% | 2.7% | 1.13 | 5.3% | 3.6% | 1.48 | 12.4% | 5.3% | 2.33 |
| 64,770,777 | 1.8% | 1.7% | 1.06 | 3.1% | 2.7% | 1.14 | 5.3% | 3.5% | 1.51 | 12.4% | 5.1% | 2.41 |
| 67,693,928 | 1.7% | 1.6% | 1.01 | 3.0% | 2.6% | 1.15 | 5.1% | 3.4% | 1.48 | 11.9% | 4.9% | 2.41 |
| 70,618,495 | 1.7% | 1.5% | 1.08 | 3.0% | 2.6% | 1.16 | 5.1% | 3.3% | 1.54 | 11.9% | 4.7% | 2.54 |
| 73,541,302 | 1.7% | 1.5% | 1.13 | 2.8% | 2.6% | 1.09 | 4.8% | 3.2% | 1.52 | 11.3% | 4.5% | 2.54 |
| 76,465,894 | 1.7% | 1.5% | 1.15 | 2.8% | 2.5% | 1.12 | 4.8% | 3.1% | 1.54 | 11.3% | 4.3% | 2.66 |
| 79,391,530 | 1.7% | 1.4% | 1.19 | 2.7% | 2.4% | 1.12 | 4.7% | 3.0% | 1.57 | 10.9% | 4.0% | 2.71 |
| 82,315,148 | 1.7% | 1.4% | 1.22 | 2.7% | 2.4% | 1.14 | 4.7% | 3.0% | 1.60 | 10.9% | 3.9% | 2.81 |
| 85,246,371 | 1.4% | 1.4% | 1.03 | 2.7% | 2.4% | 1.14 | 4.5% | 2.9% | 1.56 | 10.6% | 3.7% | 2.89 |
| 88,172,794 | 1.4% | 1.3% | 1.06 | 2.7% | 2.3% | 1.17 | 4.5% | 2.8% | 1.60 | 10.6% | 3.4% | 3.09 |
| 91,096,569 | 1.5% | 1.3% | 1.11 | 2.6% | 2.2% | 1.16 | 4.4% | 2.8% | 1.58 | 10.1% | 3.3% | 3.05 |
| 94,027,050 | 1.5% | 1.4% | 1.07 | 2.6% | 2.2% | 1.16 | 4.4% | 2.7% | 1.61 | 10.1% | 3.1% | 3.29 |
| 96,955,802 | 1.5% | 1.3% | 1.11 | 2.5% | 2.2% | 1.12 | 4.3% | 2.7% | 1.61 | 9.8% | 2.8% | 3.48 |
| 99,879,342 | 1.5% | 1.3% | 1.11 | 2.5% | 2.2% | 1.12 | 4.3% | 2.7% | 1.62 | 9.8% | 2.7% | 3.65 |
| 102,801,568 | 1.4% | 1.3% | 1.05 | 2.5% | 2.2% | 1.11 | 4.3% | 2.7% | 1.60 | 9.5% | 2.5% | 3.86 |

