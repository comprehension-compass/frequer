# Review report: es (full)

- Ranking score: `frequency`; 54,796 candidate lemmas ranked.
- Tokens counted: 1,382,684,047 in 1,750,930 documents, 482 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_es` 1.5.0 (sha256 `ccbd50dc900e43a8`); fallback `spacy-list`, units on; honeyeater `c07c70158590`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| paracrawl-en-es | 477 | 1,742,068 | 66,648,121 | 1,379,357,080 | alpha 537,007, exact_dup 326,631, gap 513,405, langid 17,683,853, length 1,359,719, near_dup 34,664 |
| tatoeba-spa | 5 | 8,862 | 441,314 | 3,326,967 | alpha 35, gap 95, length 503, near_dup 1,105 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 22,239,571. Sentences: 71,197,188.

## Units

Counted occurrences by kind: compound 9,110,518 (0.66%), compound1 9,871,938 (0.71%), construction 27,736,991 (2.01%), phrase 24,920,793 (1.80%), word 1,311,043,807 (94.82%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 26,726 | 20,350,421 |
| construction | 29 | 27,845,508 |
| phrase | 936 | 24,924,161 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `encontrarse` | 793,315 | 633,688 | 168 |
| `sitio web` | 612,105 | 462,957 | 224 |
| `Estados Unidos` | 413,968 | 356,639 | 362 |
| `internacional` | 396,176 | 343,465 | 245 |
| `correo electrónico` | 325,008 | 279,492 | 489 |
| `convertirse` | 291,062 | 265,105 | 1917 |
| `directamente` | 264,262 | 243,498 | 600 |
| `especialmente` | 226,421 | 211,645 | 729 |
| `por qué` | 221,518 | 202,964 | 758 |
| `tratarse` | 216,314 | 201,722 | 2436 |
| `simplemente` | 212,415 | 199,255 | 782 |
| `actualmente` | 207,736 | 195,594 | 801 |
| `asegurarse` | 207,695 | 194,868 | 2236 |
| `página web` | 198,674 | 177,925 | 831 |
| `realmente` | 189,465 | 177,371 | 889 |
| `completamente` | 182,283 | 172,016 | 914 |
| `totalmente` | 175,734 | 165,683 | 947 |
| `fácilmente` | 152,007 | 145,085 | 1087 |
| `rápidamente` | 151,479 | 144,394 | 1073 |
| `solamente` | 147,648 | 140,383 | 1119 |
| `sentirse` | 146,606 | 138,473 | 1101 |
| `Nueva York` | 139,207 | 126,576 | 1157 |
| `aproximadamente` | 133,823 | 125,438 | 1186 |
| `ponerse` | 128,939 | 123,648 | 1267 |
| `quedarse` | 127,568 | 121,542 | 1402 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `poder + infinitivo` | 7,794,814 | 1,727,266 | 20 |
| `haber + participio` | 5,406,531 | 1,640,185 | 27 |
| `se + verbo (impersonal/pasiva)` | 5,134,698 | 1,641,404 | 30 |
| `ser + participio` | 3,094,052 | 1,424,049 | 37 |
| `estar + gerundio` | 1,797,797 | 1,108,313 | 59 |
| `al + infinitivo` | 813,126 | 640,713 | 154 |
| `lo + adjetivo` | 801,731 | 622,089 | 166 |
| `tener que + infinitivo` | 622,315 | 514,533 | 221 |
| `ir a + infinitivo` | 436,573 | 370,022 | 346 |
| `más/menos … que` | 414,693 | 363,992 | 377 |
| `seguir + gerundio` | 284,588 | 258,913 | 559 |
| `volver a + infinitivo` | 174,090 | 161,702 | 954 |
| `comenzar a + infinitivo` | 166,999 | 157,239 | 990 |
| `empezar a + infinitivo` | 148,723 | 140,285 | 1114 |
| `dejar de + infinitivo` | 119,473 | 113,463 | 1332 |
| `soler + infinitivo` | 118,849 | 113,511 | 1338 |
| `tan … como` | 116,179 | 110,904 | 1401 |
| `hace + tiempo` | 114,251 | 109,032 | 1373 |
| `acabar de + infinitivo` | 69,556 | 61,391 | 2093 |
| `desde hace + tiempo` | 56,893 | 55,739 | 2422 |
| `tan … que` | 49,193 | 48,259 | 2669 |
| `qué + adjetivo/sustantivo` | 39,161 | 37,868 | 3105 |
| `hace + tiempo + que` | 36,403 | 35,879 | 3239 |
| `hacer que + subjuntivo` | 15,290 | 15,200 | 5364 |
| `menos … que` | 8,782 | 8,648 | 7191 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `a través de` | 794,042 | 625,011 | 157 |
| `después de` | 743,182 | 597,656 | 173 |
| `para que` | 721,057 | 581,734 | 178 |
| `cerca de` | 548,282 | 456,824 | 255 |
| `así como` | 522,732 | 449,491 | 268 |
| `antes de` | 520,584 | 444,503 | 270 |
| `acerca de` | 514,844 | 430,727 | 274 |
| `sin embargo` | 495,495 | 431,988 | 288 |
| `dentro de` | 413,852 | 360,708 | 367 |
| `por ejemplo` | 392,551 | 347,077 | 401 |
| `ya que` | 360,120 | 324,083 | 443 |
| `gracias a` | 291,397 | 266,887 | 550 |
| `en línea` | 290,881 | 263,026 | 551 |
| `disfrutar de algo` | 260,850 | 240,677 | 610 |
| `por lo que` | 260,469 | 241,185 | 611 |
| `por favor` | 253,940 | 233,365 | 626 |
| `además de` | 251,300 | 233,445 | 634 |
| `contar con algo` | 248,426 | 230,713 | 642 |
| `así que` | 241,386 | 224,924 | 674 |
| `a partir de` | 239,270 | 221,090 | 680 |
| `debido a` | 238,417 | 220,925 | 683 |
| `a continuación` | 237,104 | 221,130 | 689 |
| `convertirse en algo` | 230,310 | 214,054 | 713 |
| `alrededor de` | 214,247 | 198,758 | 773 |
| `mientras que` | 210,195 | 197,450 | 791 |

## Co-occurrence (association) table

174,563,854 tokens, 9,456,976 sentences. After merging and dropping items seen fewer than 5 times: 6,794,411 items (unigrams, UPOS votes, n-grams, pairs); 6,309,127 n-grams and pairs scored (n2 1,313,042, n3 2,726,298, n4 2,266,120, p2 3,667). Shipped: 400,000 rows, 8.7 MB gzipped (`es.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`es.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `mejor precio` |  | 108,168 | 84,680 | 7.74 | 0.73 | 1,037,557 |  |
| 2 | n | `respuesta rápido de personal` |  | 40,426 | 36,991 | 10.28 | 0.85 | 588,566 |  |
| 3 | n | `más barato` |  | 63,395 | 54,639 | 6.81 | 0.60 | 525,869 |  |
| 4 | n | `buscar el mejor precio` |  | 39,452 | 36,231 | 9.47 | 0.78 | 523,439 |  |
| 5 | n | `pasaje aereo` |  | 28,760 | 15,223 | 12.01 | 0.96 | 494,169 |  |
| 6 | n | `continuar con la búsqueda` |  | 30,312 | 28,395 | 11.21 | 0.90 | 480,901 |  |
| 7 | n | `personal y los huésped` |  | 32,454 | 30,226 | 10.27 | 0.83 | 468,531 |  |
| 8 | n | `manual de instrucción` |  | 30,146 | 27,795 | 11.16 | 0.89 | 460,284 |  |
| 9 | n | `no haber` |  | 112,681 | 87,913 | 4.16 | 0.39 | 459,822 |  |
| 10 | n | `ser posible` |  | 70,920 | 60,903 | 5.42 | 0.48 | 452,710 |  |
| 11 | n | `buscador de vuelo` |  | 35,792 | 33,100 | 9.16 | 0.75 | 442,847 |  |
| 12 | n | `mejor precio en jetcost` |  | 35,143 | 32,506 | 8.92 | 0.73 | 438,071 |  |
| 13 | n | `estar buscar el mejor` |  | 39,454 | 36,234 | 7.58 | 0.63 | 415,149 |  |
| 14 | n | `precio para su vuelo` |  | 31,377 | 29,305 | 9.29 | 0.75 | 407,259 |  |
| 15 | n | `vuelo regular o vuelo` |  | 30,376 | 28,391 | 9.29 | 0.74 | 394,737 |  |
| 16 | n | `alto calidad` |  | 35,655 | 32,497 | 8.45 | 0.69 | 367,977 |  |
| 17 | n | `estar buscar` |  | 53,163 | 47,446 | 6.04 | 0.52 | 363,784 |  |
| 18 | n | `vuelo low cost` |  | 30,470 | 28,466 | 8.98 | 0.72 | 358,508 |  |
| 19 | n | `que no` |  | 151,503 | 109,054 | 2.73 | 0.27 | 336,317 |  |
| 20 | n | `posible que no haber` |  | 30,343 | 28,422 | 7.42 | 0.59 | 304,937 |  |
| 21 | n | `tipo de` |  | 91,087 | 73,167 | 3.04 | 0.28 | 300,057 |  |
| 22 | n | `para encontrar los vuelo` |  | 34,390 | 31,932 | 6.21 | 0.50 | 287,086 |  |
| 23 | n | `querer continuar con` |  | 30,343 | 28,420 | 6.49 | 0.52 | 271,675 |  |
| 24 | n | `información sobre` |  | 39,469 | 35,707 | 6.18 | 0.51 | 270,837 |  |
| 25 | n | `pronóstico de tiempo` |  | 21,841 | 20,741 | 9.25 | 0.71 | 270,035 |  |
| 26 | n | `ser posible que` |  | 46,213 | 41,805 | 5.00 | 0.42 | 269,516 |  |
| 27 | n | `relacionar con` |  | 36,902 | 33,469 | 5.95 | 0.49 | 266,299 |  |
| 28 | n | `ser posible que no` |  | 31,551 | 29,507 | 6.10 | 0.49 | 261,985 |  |
| 29 | n | `ser muy` |  | 56,476 | 49,216 | 4.27 | 0.37 | 243,955 |  |
| 30 | n | `mejor precio para` |  | 43,908 | 39,928 | 4.97 | 0.42 | 237,835 |  |
| 31 | n | `que no haber resultado` |  | 30,303 | 28,386 | 5.59 | 0.45 | 231,517 |  |
| 32 | n | `a los mejor precio` |  | 38,270 | 35,167 | 4.93 | 0.41 | 224,819 |  |
| 33 | n | `billete avión` |  | 14,934 | 7,579 | 11.27 | 0.83 | 220,137 |  |
| 34 | n | `en vuelo regular` |  | 30,385 | 28,398 | 5.09 | 0.41 | 213,746 |  |
| 35 | n | `creer que` |  | 37,939 | 33,334 | 4.87 | 0.40 | 210,831 |  |
| 36 | n | `cosa que hacer` |  | 21,656 | 20,374 | 7.49 | 0.58 | 199,937 |  |
| 37 | n | `estar disponible` |  | 28,716 | 26,716 | 6.12 | 0.49 | 199,538 |  |
| 38 | n | `obtener respuesta rápido de` |  | 39,429 | 36,161 | 3.53 | 0.29 | 192,879 |  |
| 39 | n | `acero inoxidable` |  | 10,971 | 9,737 | 12.44 | 0.89 | 190,661 |  |
| 40 | n | `política de privacidad` |  | 13,321 | 12,339 | 10.99 | 0.80 | 190,540 |  |
| 41 | n | `decir que` |  | 55,017 | 47,287 | 3.56 | 0.31 | 184,034 |  |
| 42 | n | `acceso a` |  | 37,790 | 33,979 | 4.42 | 0.36 | 181,285 |  |
| 43 | n | `dato personal` |  | 21,166 | 18,410 | 7.34 | 0.56 | 179,599 |  |
| 44 | n | `que no haber` |  | 41,044 | 37,513 | 4.16 | 0.34 | 174,978 |  |
| 45 | n | `me gustar` |  | 16,367 | 14,273 | 8.69 | 0.65 | 172,559 |  |
| 46 | n | `necesario para` |  | 31,548 | 29,128 | 5.00 | 0.40 | 172,402 |  |
| 47 | n | `más información` |  | 35,962 | 33,077 | 4.70 | 0.38 | 171,354 |  |
| 48 | n | `comparar tu pasaje aereo` |  | 13,116 | 12,785 | 10.26 | 0.75 | 170,368 |  |
| 49 | n | `utilizar nuestro buscador de` |  | 34,188 | 31,758 | 3.53 | 0.29 | 166,553 |  |
| 50 | n | `alquiler vacacional` |  | 12,346 | 11,600 | 10.46 | 0.76 | 165,887 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `reservar se` | `reservarse` | 9,701 | 9,477 | 6.27 | 0.44 | 67,023 |
| `traducir se` | `traducirse` | 2,593 | 2,522 | 6.56 | 0.41 | 19,073 |
| `proporcionar se` | `proporcionarse` | 4,245 | 4,155 | 4.58 | 0.30 | 19,039 |
| `visualizar se` | `visualizarse` | 2,134 | 2,109 | 7.21 | 0.44 | 17,948 |

## Rank shifts against the live snapshot (`reference/lemmas/es.json`)

Live list 20,000 lemmas, this build 54,796; 12,843 shared. Spearman rank correlation on the shared lemmas 0.945; median rank ratio 1.14x.
Overlap of this build's top-k with the live top-k: top 1,000 88.0%, top 5,000 83.4%, top 20,000 63.6%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 916 | -17,539 |
| `diecinueve` | 18282 | 1331 | -16,951 |
| `dividirse` | 19076 | 3671 | -15,405 |
| `descanso` | 17625 | 2563 | -15,062 |
| `torno` | 17613 | 2630 | -14,983 |
| `respaldo` | 18269 | 3368 | -14,901 |
| `seiscientos` | 17737 | 3258 | -14,479 |
| `coco` | 18793 | 4386 | -14,407 |
| `secadora` | 19190 | 4905 | -14,285 |
| `parto` | 17982 | 3952 | -14,030 |
| `diecisiete` | 14631 | 1159 | -13,472 |
| `entregarse` | 17153 | 3941 | -13,212 |
| `conforme` | 15056 | 1910 | -13,146 |
| `quinientos` | 14749 | 1794 | -12,955 |
| `cuatrocientos` | 15401 | 2481 | -12,920 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `freemeteo` | 3092 | 53801 | +50,709 |
| `golfo` | 4927 | 45898 | +40,971 |
| `papa` | 2314 | 30181 | +27,867 |
| `matear` | 4446 | 30642 | +26,196 |
| `considerarse` | 4306 | 30321 | +26,015 |
| `cola` | 3106 | 28660 | +25,554 |
| `capar` | 4795 | 28983 | +24,188 |
| `ucranio` | 3401 | 26037 | +22,636 |
| `hondura` | 3735 | 25354 | +21,619 |
| `radio` | 1086 | 21228 | +20,142 |
| `orlar` | 2655 | 22706 | +20,051 |
| `habano` | 3196 | 21513 | +18,317 |
| `malasio` | 4644 | 22608 | +17,964 |
| `alfombrar` | 3354 | 20085 | +16,731 |
| `vario` | 265 | 13025 | +12,760 |

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
| `estar + gerundio` | - | 59 | - |
| `parte#Fem` | - | 70 | - |
| `esto` | - | 113 | - |
| `al + infinitivo` | - | 154 | - |
| `a través de` | - | 157 | - |
| `lo + adjetivo` | - | 166 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `del` | 11 | - | - |
| `al` | 22 | - | - |
| `parte` | 59 | 11820 | +11,761 |
| `e` | 94 | - | - |
| `vario` | 265 | 13025 | +12,760 |
| `tripadvisor` | 384 | - | - |
| `relacionado` | 386 | - | - |
| `vacación` | 390 | - | - |
| `jetcost` | 494 | - | - |
| `x` | 518 | - | - |
| `the` | 531 | - | - |
| `low` | 550 | - | - |
| `cost` | 560 | - | - |
| `cookies` | 565 | - | - |
| `google` | 576 | - | - |

## Ported frequer checks

### Form-ratio outliers (1,850)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 117,110,842 | median form 23.5; `de` 100,971,951 (4296679x), `del` 14,861,887 (632421x), `De` 875,541 (37257x), `DE` 267,890 (11400x) |
| 3 | `en` | 39,737,565 | median form 4; `en` 36,986,460 (9246615x), `En` 2,670,314 (667578x), `EN` 80,778 (20194x) |
| 5 | `el` | 36,417,194 | median form 18; `el` 30,786,721 (1710373x), `El` 5,551,201 (308400x), `EL` 79,249 (4403x) |
| 6 | `a` | 31,604,184 | median form 156.5; `a` 24,513,234 (156634x), `al` 5,697,407 (36405x), `A` 955,033 (6102x), `Al` 418,159 (2672x) |
| 7 | `que` | 27,419,001 | median form 4.5; `que` 27,296,595 (6065910x), `Que` 97,692 (21709x), `QUE` 24,128 (5362x) |
| 8 | `los` | 23,165,439 | median form 7; `los` 20,562,353 (2937479x), `Los` 2,562,793 (366113x), `LOS` 40,256 (5751x) |
| 9 | `ser` | 19,258,222 | median form 27.5; `es` 8,318,364 (302486x), `son` 2,164,277 (78701x), `ser` 1,793,432 (65216x), `fue` 1,100,329 (40012x) |
| 10 | `para` | 17,698,473 | median form 4; `para` 16,235,802 (4058950x), `Para` 1,411,267 (352817x), `PARA` 33,712 (8428x), `PA` 12,182 (3046x) |
| 11 | `con` | 15,046,745 | median form 10.5; `con` 14,419,245 (1373261x), `Con` 600,237 (57165x), `CON` 23,978 (2284x) |
| 12 | `un` | 14,225,152 | median form 8821; `un` 13,619,808 (1544x) |
| 13 | `las` | 14,058,132 | median form 3.5; `las` 12,649,726 (3614207x), `Las` 1,383,811 (395375x), `LAS` 24,545 (7013x) |
| 14 | `una` | 11,843,457 | median form 2.5; `una` 11,207,374 (4482950x), `Una` 615,982 (246393x), `UNA` 12,707 (5083x), `Únase` 5,753 (2301x) |
| 15 | `su` | 11,658,602 | median form 3808.5; `su` 7,574,189 (1989x) |
| 16 | `por` | 10,401,488 | median form 4; `por` 9,446,151 (2361538x), `Por` 925,852 (231463x), `POR` 22,553 (5638x), `poros` 6,134 (1534x) |
| 18 | `poder` | 8,291,300 | median form 35; `puede` 2,700,125 (77146x), `pueden` 1,311,661 (37476x), `puedes` 565,980 (16171x), `poder` 427,619 (12218x) |
| 19 | `no` | 8,242,668 | median form 7; `no` 6,918,354 (988336x), `No` 1,281,983 (183140x), `NO` 42,171 (6024x) |
| 21 | `este` | 7,596,971 | median form 21; `este` 2,398,823 (114230x), `esta` 1,883,816 (89706x), `Este` 876,028 (41716x), `estos` 705,840 (33611x) |
| 22 | `haber` | 7,449,656 | median form 23; `ha` 2,164,211 (94096x), `han` 1,008,412 (43844x), `hay` 948,329 (41232x), `haya` 489,958 (21303x) |
| 23 | `o` | 7,288,134 | median form 167; `o` 6,926,598 (41477x), `u` 239,447 (1434x) |
| 24 | `más` | 7,231,854 | median form 3.5; `más` 6,638,283 (1896652x), `Más` 366,485 (104710x), `mas` 173,430 (49551x), `Mas` 35,774 (10221x) |
| 25 | `estar` | 6,809,840 | median form 26; `está` 2,405,043 (92502x), `están` 1,088,962 (41883x), `estar` 517,157 (19891x), `Estás` 380,849 (14648x) |
| 26 | `todo` | 5,603,104 | median form 2; `todos` 1,710,597 (855298x), `todo` 1,650,272 (825136x), `todas` 920,693 (460346x), `toda` 496,167 (248084x) |
| 28 | `como` | 5,370,435 | median form 6.5; `como` 5,005,199 (770031x), `Como` 358,518 (55157x) |
| 29 | `tener` | 5,257,806 | median form 11; `tiene` 1,478,517 (134411x), `tienen` 637,715 (57974x), `tener` 629,715 (57247x), `tienes` 251,985 (22908x) |
| 31 | `lo` | 4,479,155 | median form 4; `lo` 4,186,282 (1046570x), `Lo` 285,651 (71413x), `LO` 7,174 (1794x) |

_1,825 more not shown._

### Singular/plural mismatch (56)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `los` | 23,165,439 | `lo` lemmatises to `lo` (rank 31) |
| 13 | `las` | 14,058,132 | `la` lemmatises to `la` (rank 2) |
| 104 | `después` | 1,022,337 | `despué` lemmatises to `despué` (rank 44,499) |
| 137 | `nos` | 832,284 | `no` lemmatises to `no` (rank 19) |
| 147 | `antes` | 814,843 | `ante` lemmatises to `ante` (rank 726) |
| 151 | `través` | 808,186 | `travé` lemmatises to `travé` (rank 54,315) |
| 160 | `dios` | 789,043 | `dio` lemmatises to `dar` (rank 69) |
| 169 | `además` | 752,802 | `ademá` lemmatises to `ademá` (rank 50,811) |
| 213 | `unos` | 633,283 | `uno` lemmatises to `uno` (rank 52) |
| 215 | `ellos` | 631,490 | `ello` lemmatises to `ello` (rank 688) |
| 220 | `nosotros` | 623,548 | `nosotro` lemmatises to `nosotro` (rank 42,307) |
| 252 | `varios` | 558,067 | `vario` lemmatises to `vario` (rank 13,025) |
| 265 | `les` | 525,566 | `le` lemmatises to `le` (rank 61) |
| 271 | `mes` | 515,755 | `me` lemmatises to `me` (rank 122) |
| 370 | `gracias` | 412,938 | `gracia` lemmatises to `gracia` (rank 2,836) |
| 802 | `ambos` | 207,613 | `ambo` lemmatises to `ambo` (rank 33,909) |
| 1032 | `ellas` | 158,128 | `ella` lemmatises to `ella` (rank 339) |
| 1153 | `parís` | 140,166 | `parí` lemmatises to `parir` (rank 11,673) |
| 1827 | `alrededores` | 82,062 | `alrededor` lemmatises to `alrededor` (rank 622) |
| 2022 | `martes` | 73,118 | `marte` lemmatises to `mar` (rank 522) |
| 2172 | `quizás` | 66,318 | `quizá` lemmatises to `quizá` (rank 3,156) |
| 2313 | `apenas` | 60,483 | `apena` lemmatises to `apenar` (rank 18,115) |
| 2562 | `microondas` | 52,485 | `microonda` lemmatises to `microonda` (rank 17,551) |
| 2853 | `rines` | 44,425 | `rin` lemmatises to `rin` (rank 11,523) |
| 3246 | `cumpleaños` | 36,269 | `cumpleaño` lemmatises to `cumpleaño` (rank 44,485) |

_31 more not shown._

### Lemma consistency (226)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 103 | `te` | 1,024,233 | alone, `te` lemmatises to `se` (rank 17) |
| 350 | `lista` | 433,739 | alone, `lista` lemmatises to `listo` (rank 1,151) |
| 381 | `política` | 405,354 | alone, `política` lemmatises to `político` (rank 715) |
| 512 | `dicho` | 311,464 | alone, `dicho` lemmatises to `decir` (rank 64) |
| 526 | `hecho` | 300,363 | alone, `hecho` lemmatises to `hacer` (rank 32) |
| 566 | `china` | 282,034 | alone, `china` lemmatises to `chino` (rank 1,688) |
| 586 | `presente` | 270,656 | alone, `presente` lemmatises to `presentar` (rank 276) |
| 609 | `abierto` | 261,095 | alone, `abierto` lemmatises to `abrir` (rank 330) |
| 617 | `fuera` | 258,117 | alone, `fuera` lemmatises to `ser` (rank 9) |
| 664 | `ayuda` | 243,896 | alone, `ayuda` lemmatises to `ayudar` (rank 93) |
| 724 | `compra` | 226,999 | alone, `compra` lemmatises to `comprar` (rank 247) |
| 732 | `visita` | 225,853 | alone, `visita` lemmatises to `visitar` (rank 375) |
| 800 | `corto` | 209,037 | alone, `corto` lemmatises to `cortar` (rank 1,454) |
| 815 | `causa` | 202,256 | alone, `causa` lemmatises to `causar` (rank 684) |
| 824 | `carga` | 200,790 | alone, `carga` lemmatises to `cargar` (rank 1,362) |
| 858 | `pedido` | 194,376 | alone, `pedido` lemmatises to `pedir` (rank 544) |
| 943 | `os` | 176,499 | alone, `os` lemmatises to `se` (rank 17) |
| 1023 | `vivo` | 160,147 | alone, `vivo` lemmatises to `vivir` (rank 331) |
| 1076 | `deseo` | 153,138 | alone, `deseo` lemmatises to `desear` (rank 296) |
| 1115 | `empleado` | 148,701 | alone, `empleado` lemmatises to `emplear` (rank 1,648) |
| 1138 | `avanzado` | 143,084 | alone, `avanzado` lemmatises to `avanzar` (rank 2,020) |
| 1153 | `parís` | 140,166 | alone, `parís` lemmatises to `parir` (rank 11,673) |
| 1156 | `falta` | 139,513 | alone, `falta` lemmatises to `faltar` (rank 2,209) |
| 1174 | `aumento` | 137,030 | alone, `aumento` lemmatises to `aumentar` (rank 408) |
| 1234 | `muestra` | 128,229 | alone, `muestra` lemmatises to `mostrar` (rank 188) |

_201 more not shown._

### Short lemmas (56)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 117,110,842 | `de` -> `de`, `del` -> `de`, `De` -> `de`, `DE` -> `de`, `Del` -> `de` |
| 2 | `la` | 45,398,286 | `La` -> `la`, `la` -> `la`, `LA` -> `la`, `-La` -> `?`, `lita` -> `lo` |
| 3 | `en` | 39,737,565 | `en` -> `en`, `En` -> `en`, `EN` -> `en`, `Én` -> `en`, `en-` -> `?` |
| 4 | `y` | 39,720,599 | `y` -> `y`, `Y` -> `y`, `e` -> `y`, `yes` -> `y`, `y.` -> `?` |
| 5 | `el` | 36,417,194 | `el` -> `el`, `El` -> `el`, `EL` -> `el`, `eL` -> `el`, `lO` -> `el` |
| 6 | `a` | 31,604,184 | `al` -> `a`, `a` -> `a`, `A` -> `a`, `Al` -> `a`, `AL` -> `a` |
| 12 | `un` | 14,225,152 | `un` -> `un`, `Un` -> `un`, `UN` -> `un`, `-un` -> `?`, `un--` -> `un` |
| 15 | `su` | 11,658,602 | `su` -> `su`, `sus` -> `su`, `Su` -> `su`, `Sus` -> `su`, `SU` -> `su` |
| 17 | `se` | 8,737,681 | `se` -> `se`, `Se` -> `se`, `te` -> `se`, `Te` -> `te`, `me` -> `me` |
| 19 | `no` | 8,242,668 | `no` -> `no`, `No` -> `no`, `NO` -> `no`, `nas` -> `na`, `noes` -> `no` |
| 23 | `o` | 7,288,134 | `o` -> `o`, `u` -> `o`, `O` -> `o`, `ó` -> `o`, `Ó` -> `o` |
| 31 | `lo` | 4,479,155 | `lo` -> `lo`, `Lo` -> `lo`, `LO` -> `lo`, `lA` -> `lo`, `lOS` -> `lo` |
| 34 | `tu` | 3,760,519 | `tus` -> `tu`, `tu` -> `tu`, `Tus` -> `tu`, `Tu` -> `tu`, `TU` -> `tu` |
| 35 | `si` | 3,516,540 | `Si` -> `si`, `si` -> `si`, `SI` -> `si`, `SiS` -> `si`, `sis` -> `si` |
| 61 | `le` | 1,748,957 | `le` -> `le`, `Le` -> `le`, `LE` -> `le`, `-Le` -> `le`, `lE` -> `le` |
| 78 | `mi` | 1,357,714 | `mi` -> `mi`, `mis` -> `mi`, `Mis` -> `mi`, `Mi` -> `mi`, `MI` -> `mi` |
| 88 | `ir` | 1,249,253 | `fuese` -> `ir`, `iba` -> `ir`, `ir` -> `ir`, `vaya` -> `ir`, `va` -> `ir` |
| 91 | `ya` | 1,194,630 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya`, `-ya` -> `?` |
| 103 | `te` | 1,024,233 | `te` -> `se`, `Te` -> `te`, `TE` -> `te`, `tes` -> `te`, `tE` -> `te` |
| 122 | `me` | 890,601 | `me` -> `me`, `Me` -> `me`, `ME` -> `me`, `mE` -> `me` |
| 167 | `él` | 765,680 | `él` -> `él`, `Él` -> `él`, `ÉL` -> `él`, `Èl` -> `él`, `-él` -> `?` |
| 242 | `ni` | 569,538 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni`, `niٌos` -> `?`, `nilos` -> `nilo` |
| 258 | `yo` | 542,104 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo`, `yas` -> `yas`, `yos` -> `yo` |
| 386 | `sí` | 400,150 | `sí` -> `sí`, `si` -> `si`, `Sí` -> `sí`, `SÍ` -> `sí`, `SíEs` -> `sí` |
| 537 | `ti` | 296,603 | `ti` -> `ti`, `TI` -> `ti`, `Ti` -> `ti`, `Tí` -> `ti`, `TÍ` -> `ti` |

_31 more not shown._

### Case merges (1)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4717 | `editorial#Fem` | 19,275 | capitalised but mostly ADJ; no lowercase twin |

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 678 (67.8%).

Ours only: `poder + infinitivo`, `haber + participio`, `se + verbo (impersonal/pasiva)`, `ser + participio`, `vuelo`, `hotel`, `estar + gerundio`, `te`, `archivo`, `barato`, `habitación`, `al + infinitivo`, `a través de`, `lo + adjetivo`, `encontrarse`, `después de`, `para que`, `diseño`, `alojamiento`, `disponible`, `tener que + infinitivo`, `sitio web`, `oferta`, `proporcionar`, `alquiler`

wordfreq only: `alguien`, `nadie`, `mal`, `dr`, `ahí`, `argentino`, `cero`, `malo`, `listo`, `faltar`, `unido`, `mierda`, `the`, `i`, `quién`, `c`, `viejo`, `morir`, `policía`, `elección`, `juan`, `hermano`, `orden#Masc`, `peor`, `voz`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 510 | `cookie` | 312,071 | wordfreq zipf en 4.1 vs es 3.0 |
| 805 | `metro#metre` | 206,997 | wordfreq zipf en 3.6 vs es 1.6 |
| 887 | `once` | 190,278 | wordfreq zipf en 5.5 vs es 4.4 |
| 1480 | `led` | 104,153 | wordfreq zipf en 5.1 vs es 3.7 |
| 1843 | `resort` | 81,147 | wordfreq zipf en 4.4 vs es 3.3 |
| 2085 | `show` | 70,098 | wordfreq zipf en 5.7 vs es 4.6 |
| 2602 | `top` | 51,386 | wordfreq zipf en 5.6 vs es 4.4 |
| 2729 | `look` | 47,698 | wordfreq zipf en 5.8 vs es 3.9 |
| 2882 | `set` | 43,725 | wordfreq zipf en 5.6 vs es 4.1 |
| 2910 | `stock` | 43,026 | wordfreq zipf en 4.9 vs es 3.8 |
| 3276 | `parking` | 35,557 | wordfreq zipf en 4.5 vs es 3.1 |
| 3521 | `ticket` | 31,541 | wordfreq zipf en 4.6 vs es 3.5 |
| 3599 | `as` | 30,390 | wordfreq zipf en 6.8 vs es 4.7 |
| 3726 | `feed` | 28,688 | wordfreq zipf en 4.7 vs es 3.3 |
| 3992 | `test` | 25,589 | wordfreq zipf en 5.2 vs es 4.2 |
| 4210 | `bit` | 23,485 | wordfreq zipf en 5.4 vs es 3.2 |
| 4682 | `real#royal` | 19,508 | wordfreq zipf en 4.8 vs es 3.7 |
| 4815 | `film` | 18,477 | wordfreq zipf en 5.2 vs es 4.1 |
| 4858 | `metro#railway` | 18,227 | wordfreq zipf en 4.0 vs es 2.6 |
| 5035 | `stand` | 17,168 | wordfreq zipf en 5.1 vs es 3.8 |
| 5464 | `box` | 14,651 | wordfreq zipf en 5.0 vs es 3.8 |
| 5520 | `country` | 14,352 | wordfreq zipf en 5.5 vs es 3.8 |
| 5531 | `trading` | 14,263 | wordfreq zipf en 4.6 vs es 3.2 |
| 5705 | `script` | 13,541 | wordfreq zipf en 4.4 vs es 3.3 |
| 5815 | `check-in` | 13,045 | wordfreq zipf en 5.3 vs es 3.7 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 160 | `dios` | 789,043 | PROPN 0%, capitalised forms 94% |
| 362 | `estados unidos` | 416,601 | PROPN 1%, capitalised forms 100% |
| 441 | `españa` | 361,243 | PROPN 100%, capitalised forms 100% |
| 485 | `san` | 327,029 | PROPN 2%, capitalised forms 96% |
| 566 | `china` | 282,034 | PROPN 100%, capitalised forms 100% |
| 693 | `méxico` | 236,286 | PROPN 100%, capitalised forms 100% |
| 699 | `tv` | 234,979 | PROPN 6%, capitalised forms 97% |
| 708 | `europa` | 231,507 | PROPN 99%, capitalised forms 100% |
| 844 | `barcelona` | 197,214 | PROPN 100%, capitalised forms 100% |
| 854 | `madrid` | 195,159 | PROPN 99%, capitalised forms 99% |
| 992 | `israel` | 166,602 | PROPN 100%, capitalised forms 100% |
| 1153 | `parís` | 140,166 | PROPN 99%, capitalised forms 100% |
| 1157 | `nueva york` | 139,207 | PROPN 100%, capitalised forms 100% |
| 1203 | `francia` | 133,309 | PROPN 99%, capitalised forms 100% |
| 1241 | `londres` | 127,449 | PROPN 100%, capitalised forms 100% |
| 1326 | `wi-fi` | 119,729 | PROPN 1%, capitalised forms 97% |
| 1365 | `alemania` | 114,964 | PROPN 100%, capitalised forms 100% |
| 1397 | `italia` | 111,823 | PROPN 100%, capitalised forms 100% |
| 1408 | `colombia` | 110,652 | PROPN 100%, capitalised forms 99% |
| 1411 | `américa` | 110,485 | PROPN 99%, capitalised forms 99% |
| 1453 | `pc` | 106,451 | PROPN 11%, capitalised forms 98% |
| 1503 | `roma` | 102,910 | PROPN 100%, capitalised forms 100% |
| 1543 | `chile` | 99,973 | PROPN 93%, capitalised forms 94% |
| 1580 | `reino unido` | 97,204 | PROPN 0%, capitalised forms 100% |
| 1608 | `canadá` | 95,502 | PROPN 100%, capitalised forms 100% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 99.1% | 0.998 |
| juilland_u | 100.0% | 1.000 |
| juilland_u_corrected | 100.0% | 1.000 |
| dp_adjusted | 99.9% | 1.000 |
| cd_blend | 99.6% | 1.000 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `por consiguiente` | 4836 | 4686 | -150 | 20,323 | 20,200 | 0.993 | 0.030 |
| `si bien` | 5076 | 4927 | -149 | 18,742 | 18,653 | 0.993 | 0.028 |
| `esencialmente` | 4841 | 4695 | -146 | 20,309 | 20,162 | 0.992 | 0.030 |
| `en otras palabras` | 4917 | 4772 | -145 | 19,818 | 19,686 | 0.994 | 0.024 |
| `proponerse` | 4856 | 4711 | -145 | 20,211 | 20,063 | 0.994 | 0.026 |
| `tom` | 2649 | 4660 | +2,011 | 51,687 | 20,384 | 0.985 | 0.056 |
| `love` | 3142 | 5056 | +1,914 | 40,001 | 17,899 | 0.991 | 0.037 |
| `ascendente` | 4360 | 6106 | +1,746 | 23,968 | 13,151 | 0.989 | 0.045 |
| `remate` | 4265 | 5627 | +1,362 | 24,804 | 15,084 | 0.990 | 0.039 |
| `tiquete` | 2263 | 3439 | +1,176 | 63,988 | 32,780 | 0.995 | 0.021 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `gradualmente` | 4823 | 4815 | -8 | 20,402 | 20,200 | 0.994 | 0.024 |
| `notable` | 3883 | 3875 | -8 | 28,683 | 28,367 | 0.995 | 0.021 |
| `suscribirse` | 4260 | 4253 | -7 | 24,845 | 24,603 | 0.994 | 0.022 |
| `divertirse` | 4974 | 4968 | -6 | 19,410 | 19,230 | 0.993 | 0.027 |
| `neto` | 3943 | 3937 | -6 | 28,079 | 26,352 | 0.995 | 0.021 |
| `mary` | 4935 | 4957 | +22 | 19,701 | 13,754 | 0.982 | 0.067 |
| `tom` | 2649 | 2669 | +20 | 51,687 | 20,384 | 0.985 | 0.056 |
| `itunes` | 4747 | 4759 | +12 | 20,811 | 18,165 | 0.990 | 0.040 |
| `ascendente` | 4360 | 4372 | +12 | 23,968 | 13,151 | 0.989 | 0.045 |
| `phoenix` | 4795 | 4804 | +9 | 20,500 | 17,968 | 0.991 | 0.036 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `retratar` | 4368 | 4363 | -5 | 23,923 | 22,978 | 0.994 | 0.025 |
| `ética` | 4367 | 4362 | -5 | 23,925 | 22,718 | 0.994 | 0.024 |
| `singapur` | 4181 | 4176 | -5 | 25,578 | 22,641 | 0.994 | 0.025 |
| `michael` | 3970 | 3965 | -5 | 27,688 | 26,454 | 0.994 | 0.025 |
| `retroceso` | 4065 | 4060 | -5 | 26,531 | 26,156 | 0.994 | 0.024 |
| `tom` | 2649 | 2669 | +20 | 51,687 | 20,384 | 0.985 | 0.056 |
| `mary` | 4935 | 4954 | +19 | 19,701 | 13,754 | 0.982 | 0.067 |
| `itunes` | 4747 | 4759 | +12 | 20,811 | 18,165 | 0.990 | 0.040 |
| `ascendente` | 4360 | 4372 | +12 | 23,968 | 13,151 | 0.989 | 0.045 |
| `phoenix` | 4795 | 4803 | +8 | 20,500 | 17,968 | 0.991 | 0.036 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `gradualmente` | 4823 | 4796 | -27 | 20,402 | 20,200 | 0.994 | 0.024 |
| `eco` | 4838 | 4816 | -22 | 20,321 | 19,600 | 0.994 | 0.024 |
| `en otras palabras` | 4917 | 4897 | -20 | 19,818 | 19,686 | 0.994 | 0.024 |
| `hallazgo` | 4786 | 4767 | -19 | 20,558 | 20,244 | 0.994 | 0.024 |
| `casual` | 4839 | 4821 | -18 | 20,318 | 19,640 | 0.994 | 0.025 |
| `mary` | 4935 | 5043 | +108 | 19,701 | 13,754 | 0.982 | 0.067 |
| `tom` | 2649 | 2717 | +68 | 51,687 | 20,384 | 0.985 | 0.056 |
| `ascendente` | 4360 | 4409 | +49 | 23,968 | 13,151 | 0.989 | 0.045 |
| `itunes` | 4747 | 4786 | +39 | 20,811 | 18,165 | 0.990 | 0.040 |
| `phoenix` | 4795 | 4829 | +34 | 20,500 | 17,968 | 0.991 | 0.036 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `la mayor parte de` | 4552 | 4472 | -80 | 22,391 | 22,216 | 0.993 | 0.030 |
| `profundizar` | 4928 | 4851 | -77 | 19,766 | 19,609 | 0.993 | 0.029 |
| `familiarizarse` | 4983 | 4907 | -76 | 19,362 | 19,274 | 0.992 | 0.032 |
| `orbitz` | 4949 | 4873 | -76 | 19,570 | 19,454 | 0.992 | 0.031 |
| `en otras palabras` | 4917 | 4842 | -75 | 19,818 | 19,686 | 0.994 | 0.024 |
| `tom` | 2649 | 3528 | +879 | 51,687 | 20,384 | 0.985 | 0.056 |
| `love` | 3142 | 3983 | +841 | 40,001 | 17,899 | 0.991 | 0.037 |
| `ascendente` | 4360 | 5166 | +806 | 23,968 | 13,151 | 0.989 | 0.045 |
| `remate` | 4265 | 4901 | +636 | 24,804 | 15,084 | 0.990 | 0.039 |
| `tiquete` | 2263 | 2819 | +556 | 63,988 | 32,780 | 0.995 | 0.021 |

## Excluded lemmas

`es.tsv` (sha256 `d65cd2427cf419f2`) lists 1,404 exclusions; 1,028 lemmas were dropped from the top 40,000 before cutting it (exclude-abbreviation 47, exclude-boilerplate 56, exclude-english 841, exclude-foreign 16, exclude-fragment 13, exclude-letter 25, exclude-numeral 30). Lower ranks moved up.

| rank before | lemma | class | reason |
|---|---|---|---|
| 468 | `jetcost` | exclude-boilerplate | flight-search site brand |
| 527 | `low` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 538 | `cost` | exclude-fragment | developer 2026-11-01: fragment of a loan phrase or plural form, excluded |
| 560 | `aereo` | exclude-boilerplate | unaccented template spelling of aéreo |
| 727 | `the` | exclude-english | English article |
| 1011 | `x` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1146 | `á` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1187 | `of` | exclude-english | English preposition |
| 1282 | `city` | exclude-english | English word in names |
| 1324 | `b` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1432 | `c` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1451 | `in` | exclude-english | English preposition |
| 1454 | `i` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1625 | `and` | exclude-english | English conjunction |
| 1722 | `beach` | exclude-english | not a Spanish loan |
| 1786 | `d` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1799 | `ii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 1915 | `m` | exclude-letter | developer 2026-11-01: single letters excluded |
| 1938 | `new` | exclude-english | English template text |
| 2089 | `home` | exclude-english | English template text |
| 2214 | `t` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2308 | `g` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2378 | `to` | exclude-english | English preposition |
| 2469 | `house` | exclude-english | English template text |
| 2575 | `hp` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 2592 | `v` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2679 | `by` | exclude-english | English preposition |
| 2691 | `k` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2759 | `e` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2788 | `black` | exclude-english | English colour word |
| 2794 | `n` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2855 | `grand` | exclude-english | English in brand names |
| 2861 | `r` | exclude-letter | developer 2026-11-01: single letters excluded |
| 2928 | `airport` | exclude-english | English for aeropuerto |
| 2933 | `f` | exclude-letter | developer 2026-11-01: single letters excluded |
| 3000 | `island` | exclude-english | English place word |
| 3025 | `on` | exclude-english | English preposition |
| 3056 | `iii` | exclude-numeral | developer 2026-11-01: roman numerals excluded |
| 3070 | `international` | exclude-english | English for internacional |
| 3087 | `best` | exclude-english | English word |
| 3109 | `for` | exclude-english | English preposition |
| 3130 | `west` | exclude-english | English place word |
| 3131 | `air` | exclude-english | English in brand names |
| 3142 | `love` | exclude-english | English word |
| 3173 | `ltd` | exclude-boilerplate | company-name template suffix |
| 3208 | `lg` | exclude-foreign | developer 2026-11-01: brand acronym excluded |
| 3248 | `di` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3249 | `world` | exclude-english | English word |
| 3288 | `group` | exclude-english | English word in names |
| 3368 | `mb` | exclude-abbreviation | abbreviation or unit symbol (developer 2026-11-01: abbreviations excluded for now) |
| 3405 | `english` | exclude-english | English word |
| 3492 | `do` | exclude-foreign | developer 2026-11-01: foreign name particle excluded |
| 3507 | `white` | exclude-english | English colour word |
| 3547 | `car` | exclude-english | English word |
| 3575 | `one` | exclude-english | English word |
| 3580 | `us` | exclude-english | English pronoun/domain |
| 3613 | `am` | exclude-english | English time suffix |
| 3622 | `file` | exclude-english | English for archivo |
| 3661 | `mainland` | exclude-english | English listing text |
| 3707 | `business` | exclude-english | English word |

_968 more in the exclusion file._


## Junk-filter heuristics

Rules on: diversity, citation, foreign, shape, propn_band; accent merges at ratio 5.0. Window: the 114,944 ranked lemmas (after the exclusion list) that fill the top 40,000. Actions: keep 29,724, propn-drop 48,825, review-drop 26,119, review-keep 10,276.

### Hits and overlap (window)

Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.

| | diversity | citation | foreign | shape | propn_band |
|---|---:|---:|---:|---:|---:|
| diversity | 458 | 3 | 4 | 42 | 125 |
| citation | 3 | 391 | 1 | 45 | 0 |
| foreign | 4 | 1 | 8,275 | 478 | 4,171 |
| shape | 42 | 45 | 478 | 5,142 | 1,830 |
| propn_band | 125 | 0 | 4,171 | 1,830 | 20,967 |

Proper nouns dropped alone (capitalised in >= 90% of running text): 48,825.

### Low diversity

Documents reached / documents expected at random, below 0.6 (frequency >= 20): 458 in the window. For comparison, each log2-frequency band's 2nd percentile: 32-63: 0.76, 64-127: 0.76, 128-255: 0.78, 256-511: 0.78, 512-1023: 0.78, 1024-2047: 0.78, 2048-4095: 0.8, 4096-8191: 0.82, 8192-16383: 0.83, 16384-32767: 0.84, 32768-65535: 0.85, 65536-131071: 0.86, 131072-262143: 0.87, 262144-524287: 0.87.

Examples: `tiquete` (2242), `tom` (2623), `ascendente` (4280), `pseudónimo` (5642), `pseudo` (5687), `de aquí en adelante` (5846), `netcomponents` (6393), `bora` (8980), `microarea` (9672), `moncler` (10601), `wishtrips` (11675), `alugom` (14732), `fpnm` (16205), `luge` (16726), `vbulletin` (16727), `caja de música` (17714), `invoice` (18162), `langa` (19889), `pcbs` (21798), `idnet` (22000), `fossil` (22108), `allover` (22370), `nopb` (22508), `stardoll` (22701), `megaexit` (22713), `subiza` (22738), `dimatra` (23309), `prorock-perforación` (23711), `walla` (24055), `tradingview` (24427), `gotesa` (24772), `tudanca` (24896), `cinvestav` (24993), `naf` (25060), `al-tec` (26892), `linked` (27755), `whaly` (27944), `kendu` (28028), `jovees` (28678), `mectrol` (30391)

### Accent merges (9,404)

| from | into | frequency moved | evidence |
|---|---|---:|---|
| `halar` | `hala` | 177 | review: split (HALA, Hala, Halas, hala) |
| `esponjar` | `esponja` | 1,179 | review: split (Esponjas, esponjas) |
| `despechar` | `despecho` | 361 | review: split (Despecho, despecho) |
| `chinchar` | `chinche` | 194 | review: split (Chinche, chinche) |
| `telegrafiar` | `telegrafía` | 151 | review: split (telegrafía) |
| `opacar` | `opaco` | 3,538 | review: split (opaca, opaco) |
| `alarmar` | `alarma` | 7,818 | review: split (Alarmas, alarmas) |
| `capitular` | `capítulo` | 1,699 | review: split (Capitulo, capitulo) |
| `cimbrar` | `cimbra` | 146 | review: split (cimbra, cimbras) |
| `mediar` | `mediados` | 28,368 | review: split (Mediados, mediados) |
| `hombr` | `hombre` | 51 | review: split (Hombr, hombr, hombrse) |
| `trasuntar` | `trasunto` | 91 | review: split (Trasunto, trasunto) |
| `ufanar` | `ufano` | 29 | review: split (ufano) |
| `empachar` | `empacho` | 82 | review: split (Empacho, empacho) |
| `afijar` | `afijo` | 96 | review: split (afijo) |
| `desparejar` | `desparejo` | 58 | review: split (desparejo) |
| `emplomar` | `emplomado` | 54 | review: split (Emplomado, emplomado, emplomados) |
| `mahonés` | `mahonesa` | 69 | review: split (Mahonesa, mahonesa) |
| `bazucar` | `bazuco` | 15 | review: split (bazuco) |
| `cubicar` | `cúbico` | 59 | review: split (cubicas, cubico) |
| `mariscar` | `mariscada` | 83 | review: split (Mariscada, Mariscadas, mariscada, mariscadas) |
| `amurar` | `amura` | 27 | review: split (amura, amuras) |
| `hoster` | `hostería` | 31 | review: split (hostería) |
| `desplantar` | `desplante` | 67 | review: split (Desplante, desplante) |
| `salariar` | `salariado` | 47 | review: split (salariado, salariados) |
| `acamar` | `acamado` | 3 | review: split (acamados) |
| `trajinero` | `trajinera` | 76 | review: split (Trajinera, Trajineras, trajinera, trajineras) |
| `importuno` | `importunar` | 48 | review: split (importuna) |
| `escorzar` | `escorzo` | 63 | review: split (escorzo) |
| `faldear` | `faldeo` | 59 | review: split (Faldeo, faldeo) |
| `verdear` | `verdeo` | 37 | review: split (Verdeo, verdeo) |
| `miniar` | `minio` | 27 | review: split (Minio, minio) |
| `canana` | `cananeo` | 33 | review: split (cananita) |
| `recebar` | `recebo` | 34 | review: split (Recebo, recebo) |
| `emplastar` | `emplasto` | 64 | review: split (Emplaste, Emplasto, emplaste, emplasto) |
| `albardar` | `albarda` | 61 | review: split (Albarda, albarda, albardas) |
| `manager` | `mánager` | 25,019 | review: merge |
| `junior` | `júnior` | 12,397 | review: merge |
| `inscríbete` | `inscribir` | 9,648 | review: merge |
| `santa` | `santo` | 9,145 | review: merge |
| `vieja` | `viejo` | 8,308 | review: merge |
| `pixel` | `píxel` | 7,345 | review: merge |
| `indígeno` | `indígena` | 7,311 | review: merge |
| `herpe` | `herpes` | 6,002 | review: merge |
| `boulevard` | `bulevar` | 6,337 | review: merge |
| `lesbiano` | `lesbiana` | 5,584 | review: merge |
| `alojándote` | `alojarse` | 5,586 | review: merge |
| `bowl` | `bol` | 5,143 | review: merge |
| `abagado` | `abogado` | 5,335 | review: merge |
| `paise` | `país` | 5,221 | review: merge |
| `ud` | `usted` | 5,191 | review: merge |
| `cappuccino` | `capuchino` | 5,006 | review: merge |
| `corner` | `córner` | 3,761 | review: merge |
| `trave` | `través` | 4,260 | review: merge |
| `aumentor` | `aumento` | 4,256 | review: merge |
| `pymes` | `pyme` | 3,651 | review: merge |
| `guru` | `gurú` | 3,716 | review: merge |
| `tragamoneda` | `tragamonedas` | 3,545 | review: merge |
| `drone` | `dron` | 3,349 | review: merge |
| `vendidor` | `vendedor` | 3,357 | review: merge |
| `fotocopiador` | `fotocopiadora` | 3,196 | review: merge |
| `champagne` | `champán` | 3,218 | review: merge |
| `bistro` | `bistró` | 3,103 | review: merge |
| `garage` | `garaje` | 2,766 | review: merge |
| `carita` | `cara` | 3,193 | review: merge |
| `comisionada` | `comisionado` | 2,543 | review: merge |
| `cricket` | `críquet` | 3,004 | review: merge |
| `padel` | `pádel` | 2,390 | review: merge |
| `scanner` | `escáner` | 2,308 | review: merge |
| `sándwiche` | `sándwich` | 2,533 | review: merge |
| `post-venta` | `posventa` | 2,734 | review: merge |
| `lavaplato` | `lavaplatos` | 2,706 | review: merge |
| `mándano` | `mandar` | 2,481 | review: merge |
| `eua` | `estados unidos` | 2,633 | review: merge |
| `cactu` | `cactus` | 2,595 | review: merge |
| `sandwich` | `sándwich` | 2,305 | review: merge |
| `momio` | `momia` | 2,175 | review: merge |
| `basándono` | `basarse` | 2,527 | review: merge |
| `derby` | `derbi` | 2,620 | review: merge |
| `mg` | `miligramo` | 2,278 | review: merge |
| `sabienda` | `sabiendas` | 1,947 | review: merge |
| `mir` | `mirar` | 2,224 | review: merge |
| `shampoo` | `champú` | 2,520 | review: merge |
| `euromillón` | `euromillones` | 2,237 | review: merge |
| `pizzeria` | `pizzería` | 2,012 | review: merge |
| `epidermi` | `epidermis` | 2,282 | review: merge |
| `tobogan` | `tobogán` | 2,247 | review: merge |
| `seca` | `seco` | 2,054 | review: merge |
| `mola` | `molar` | 1,635 | review: merge |
| `trio` | `trío` | 1,949 | review: merge |
| `escoje` | `escoger` | 1,932 | review: merge |
| `baccarat` | `bacarrá` | 2,053 | review: merge |
| `belg` | `belga` | 1,832 | review: merge |
| `ofreciéndol` | `ofrecer` | 1,920 | review: merge |
| `capitulo` | `capítulo` | 1,805 | review: merge |
| `pony` | `poni` | 1,977 | review: merge |
| `dándol` | `dar` | 1,701 | review: merge |
| `cdmx` | `ciudad de méxico` | 1,844 | review: merge |
| `sha` | `sah` | 1,714 | review: merge |
| `directa` | `directo` | 1,998 | review: merge |
| `altibajo` | `altibajos` | 1,757 | review: merge |
| `reunion` | `reunión` | 2,031 | review: merge |
| `samurai` | `samurái` | 2,004 | review: merge |
| `pbi` | `pib` | 1,759 | review: merge |
| `diciéndol` | `decir` | 1,592 | review: merge |
| `cds` | `cd` | 1,904 | review: merge |
| `cubiertaa` | `cubierta` | 1,831 | review: merge |
| `leed` | `leer` | 1,611 | review: merge |
| `limonado` | `limonada` | 1,208 | review: merge |
| `implícitas` | `implícito` | 1,398 | review: merge |
| `llámeno` | `llamar` | 1,123 | review: merge |
| `crash` | `crac` | 1,547 | review: merge |
| `profilaxi` | `profilaxis` | 1,342 | review: merge |
| `ayúdeno` | `ayudar` | 1,444 | review: merge |
| `dejarno` | `dejar` | 1,529 | review: merge |
| `ebooks` | `ebook` | 1,446 | review: merge |
| `l-carnitina` | `carnitina` | 1,595 | review: merge |
| `apoyor` | `apoyo` | 1,490 | review: merge |
| `permitiéndol` | `permitir` | 1,728 | review: merge |
| `guardabarro` | `guardabarros` | 1,560 | review: merge |
| `aparcacoche` | `aparcacoches` | 1,580 | review: merge |
| `refr` | `refrán` | 1,385 | review: merge |
| `fue` | `ser` | 1,327 | review: merge |
| `ria` | `ría` | 1,290 | review: merge |
| `handicap` | `hándicap` | 1,363 | review: merge |
| `déco` | `decó` | 1,514 | review: merge |
| `bicis` | `bici` | 1,139 | review: merge |
| `limpiaparabrisa` | `limpiaparabrisas` | 1,282 | review: merge |
| `esforzándono` | `esforzarse` | 1,236 | review: merge |
| `sildenafil` | `sildenafilo` | 1,403 | review: merge |
| `contactándono` | `contactar` | 1,279 | review: merge |
| `tinnitu` | `tinnitus` | 1,304 | review: merge |
| `enseñándol` | `enseñar` | 1,117 | review: merge |
| `baseball` | `béisbol` | 1,098 | review: merge |
| `tablets` | `tablet` | 1,429 | review: merge |
| `mini-bar` | `minibar` | 1,317 | review: merge |
| `switche` | `switch` | 1,435 | review: merge |
| `watt` | `vatio` | 1,351 | review: merge |
| `chili` | `chile` | 1,216 | review: merge |
| `kung` | `kung fu` | 1,106 | review: merge |
| `cutter` | `cúter` | 1,153 | review: merge |
| `raton` | `ratón` | 1,203 | review: merge |
| `reposacabeza` | `reposacabezas` | 1,127 | review: merge |
| `tumbón` | `tumbona` | 977 | review: merge |
| `iran` | `irán` | 1,008 | review: merge |
| `permítano` | `permitir` | 1,066 | review: merge |
| `anti-envejecimiento` | `antienvejecimiento` | 1,252 | review: merge |
| `carótido` | `carótida` | 911 | review: merge |
| `co-fundador` | `cofundador` | 1,137 | review: merge |
| `haciéndol` | `hacer` | 1,114 | review: merge |
| `clorofilo` | `clorofila` | 1,260 | review: merge |
| `rodillero` | `rodillera` | 928 | review: merge |
| `sintaxi` | `sintaxis` | 1,026 | review: merge |
| `proporcionarno` | `proporcionar` | 935 | review: merge |
| `anti-virus` | `antivirus` | 1,002 | review: merge |
| `antidisturbio` | `antidisturbios` | 795 | review: merge |
| `vu` | `déjà vu` | 1,062 | review: merge |
| `ata` | `atar` | 1,068 | review: merge |
| `das` | `dar` | 1,108 | review: merge |
| `perrero` | `perrera` | 1,022 | review: merge |
| `reflex` | `réflex` | 879 | review: merge |
| `recorré` | `recorrer` | 988 | review: merge |
| `siéntete` | `sentir` | 865 | review: merge |
| `hipotecaria` | `hipotecario` | 976 | review: merge |
| `ponerno` | `ponerse` | 965 | review: merge |
| `proporcionándol` | `proporcionar` | 1,016 | review: merge |
| `rayos-x` | `rayos x` | 851 | review: merge |
| `socio-económico` | `socioeconómico` | 1,057 | review: merge |
| `ajur` | `ajustar` | 922 | review: merge |
| `elevaluna` | `elevalunas` | 860 | review: merge |
| `visitarno` | `visitar` | 958 | review: merge |
| `volveo` | `volver` | 873 | review: merge |
| `adentrarno` | `adentrarse` | 816 | review: merge |
| `bunker` | `búnker` | 1,104 | review: merge |
| `portavaso` | `portavasos` | 832 | review: merge |
| `yoyo` | `yoyó` | 1,093 | review: merge |
| `basket` | `básquet` | 1,075 | review: merge |
| `candida` | `cándida` | 1,023 | review: merge |
| `chueca` | `chueco` | 952 | review: merge |
| `cuclilla` | `cuclillas` | 847 | review: merge |
| `adaptarno` | `adaptarse` | 925 | review: merge |
| `albatro` | `albatros` | 1,035 | review: merge |
| `paris` | `parís` | 1,021 | review: merge |
| `roulette` | `ruleta` | 883 | review: merge |
| `notificarno` | `notificar` | 770 | review: merge |
| `antiarruga` | `antiarrugas` | 755 | review: merge |
| `busque` | `buscar` | 984 | review: merge |
| `configure` | `configurar` | 945 | review: merge |
| `maquilador` | `maquiladora` | 886 | review: merge |
| `boomerang` | `bumerán` | 830 | review: merge |
| `co-creación` | `cocreación` | 786 | review: merge |
| `reposabrazo` | `reposabrazos` | 845 | review: merge |
| `cognac` | `coñac` | 733 | review: merge |
| `gachó` | `gachas` | 688 | review: merge |
| `informacion` | `información` | 781 | review: merge |
| `magnifico` | `magnífico` | 799 | review: merge |
| `mrur` | `morir` | 957 | review: merge |
| `outlets` | `outlet` | 903 | review: merge |
| `regañadiente` | `regañadientes` | 685 | review: merge |
| `acompáñano` | `acompañar` | 720 | review: merge |
| `anti-spam` | `antispam` | 618 | review: merge |
| `ohm` | `ohmio` | 860 | review: merge |
| `brindándol` | `brindar` | 683 | review: merge |
| `anti-inflamatorio` | `antiinflamatorio` | 738 | review: merge |
| `centrándono` | `centrarse` | 853 | review: merge |
| `chia` | `chía` | 711 | review: merge |
| `corticoesteroid` | `corticoesteroide` | 718 | review: merge |
| `sana` | `sano` | 815 | review: merge |
| `ase` | `as` | 591 | review: merge |
| `autocargadore` | `autocargador` | 660 | review: merge |
| `sharia` | `sharía` | 705 | review: merge |
| `lio` | `lío` | 652 | review: merge |
| `miercol` | `miércoles` | 703 | review: merge |
| `convertirno` | `convertirse` | 690 | review: merge |
| `socio-cultural` | `sociocultural` | 721 | review: merge |
| `crucis` | `viacrucis` | 753 | review: merge |
| `empleados` | `empleado` | 606 | review: merge |
| `pop-ups` | `pop-up` | 790 | review: merge |
| `ad-hoc` | `ad hoc` | 645 | review: merge |
| `contáctano` | `contactar` | 672 | review: merge |
| `tio` | `tío` | 588 | review: merge |
| `coupon` | `cupón` | 557 | review: merge |
| `decirno` | `decir` | 553 | review: merge |
| `hornea` | `hornear` | 666 | review: merge |
| `hosteria` | `hostería` | 854 | review: merge |
| `ovnis` | `ovni` | 501 | review: merge |
| `publico` | `publicar` | 694 | review: merge |
| `implícita` | `implícito` | 750 | review: merge |
| `apresúrate` | `apresurarse` | 372 | review: merge |
| `djs` | `dj` | 627 | review: merge |
| `espacio-temporal` | `espaciotemporal` | 648 | review: merge |
| `facilitarno` | `facilitar` | 585 | review: merge |
| `oceano` | `océano` | 588 | review: merge |
| `pre-venta` | `preventa` | 577 | review: merge |
| `pídel` | `pedir` | 546 | review: merge |
| `silicone` | `silicona` | 560 | review: merge |
| `actua` | `actuar` | 616 | review: merge |
| `catalog` | `catálogo` | 689 | review: merge |
| `escribiéndono` | `escribir` | 679 | review: merge |
| `eucarioto` | `eucariota` | 433 | review: merge |
| `pidiéndol` | `pedir` | 589 | review: merge |
| `sweater` | `suéter` | 598 | review: merge |
| `ying` | `yin` | 481 | review: merge |
| `apartaos` | `apartarse` | 498 | review: merge |
| `condominiums` | `condominio` | 650 | review: merge |
| `l-arginina` | `arginina` | 730 | review: merge |
| `meta-análisis` | `metaanálisis` | 671 | review: merge |
| `sur-oeste` | `suroeste` | 612 | review: merge |
| `vitamin` | `vitamina` | 698 | review: merge |
| `yogi` | `yogui` | 842 | review: merge |
| `zloty` | `esloti` | 668 | review: merge |
| `adaptándono` | `adaptarse` | 685 | review: merge |
| `cabriolet` | `cabriolé` | 578 | review: merge |
| `khmer` | `jemer` | 493 | review: merge |
| `orad` | `orar` | 678 | review: merge |
| `aluminium` | `aluminio` | 479 | review: merge |
| `polyester` | `poliéster` | 697 | review: merge |
| `boricuo` | `boricua` | 676 | review: merge |
| `prediabete` | `prediabetes` | 736 | review: merge |
| `rondo` | `ronda` | 645 | review: merge |
| `vegan` | `vegano` | 722 | review: merge |
| `negarno` | `negarse` | 631 | review: merge |
| `pro-vida` | `provida` | 647 | review: merge |
| `rna` | `arn` | 611 | review: merge |
| `smoking` | `esmoquin` | 481 | review: merge |
| `tendr` | `tener` | 562 | review: merge |
| `controle` | `controlar` | 596 | review: merge |
| `escapatorio` | `escapatoria` | 523 | review: merge |
| `espantapájaro` | `espantapájaros` | 464 | review: merge |
| `euromillone` | `euromillones` | 478 | review: merge |
| `moverno` | `moverse` | 557 | review: merge |
| `blazers` | `blazer` | 682 | review: merge |
| `budas` | `buda` | 535 | review: merge |
| `costillita` | `costilla` | 662 | review: merge |
| `entr` | `entre` | 404 | review: merge |
| `habea` | `habeas` | 479 | review: merge |
| `micro-ondas` | `microondas` | 519 | review: merge |
| `nautico` | `náutico` | 468 | review: merge |
| `disyuntivo` | `disyuntiva` | 494 | review: merge |
| `elimine` | `eliminar` | 373 | review: merge |
| `ruégote` | `rogar` | 398 | review: merge |
| `aluminum` | `aluminio` | 677 | review: merge |
| `anti-inmigrante` | `antiinmigrante` | 488 | review: merge |
| `bistrot` | `bistró` | 489 | review: merge |
| `co-autor` | `coautor` | 589 | review: merge |
| `cuentacuento` | `cuentacuentos` | 434 | review: merge |
| `en-línea` | `en línea` | 430 | review: merge |
| `freak` | `friki` | 603 | review: merge |
| `masai` | `masái` | 532 | review: merge |
| `no-violencia` | `no violencia` | 442 | review: merge |
| `paises` | `países` | 542 | review: merge |
| `quiénes` | `quién` | 549 | review: merge |
| `shogun` | `sogún` | 548 | review: merge |
| `burdeo` | `burdeos` | 465 | review: merge |
| `díjol` | `decir` | 428 | review: merge |
| `ephod` | `efod` | 324 | review: merge |
| `portaobjeto` | `portaobjetos` | 739 | review: merge |
| `sentaos` | `sentarse` | 269 | review: merge |
| `sur-este` | `sureste` | 507 | review: merge |
| `ayudándono` | `ayudar` | 475 | review: merge |
| `biomarcadore` | `biomarcador` | 449 | review: merge |
| `co-creador` | `cocreador` | 383 | review: merge |
| `lactobacillus` | `lactobacilo` | 543 | review: merge |
| `magister` | `magíster` | 487 | review: merge |
| `nro` | `número` | 502 | review: merge |
| `portapapel` | `portapapeles` | 529 | review: merge |
| `youtubers` | `youtuber` | 365 | review: merge |
| `afro-americano` | `afroamericano` | 453 | review: merge |
| `calculo` | `calcular` | 308 | review: merge |
| `casuístico` | `casuística` | 497 | review: merge |
| `expresas` | `expresar` | 418 | review: merge |
| `beta-caroteno` | `betacaroteno` | 472 | review: merge |
| `centr` | `centrar` | 503 | review: merge |
| `electronica` | `electrónica` | 539 | review: merge |
| `gabion` | `gavión` | 408 | review: merge |
| `mares` | `mar` | 400 | review: merge |
| `muselino` | `muselina` | 460 | review: merge |
| `paratiroid` | `paratiroides` | 551 | review: merge |
| `portapape` | `portapapeles` | 519 | review: merge |
| `totem` | `tótem` | 485 | review: merge |
| `unidas` | `unido` | 514 | review: merge |
| `virolo` | `virola` | 370 | review: merge |
| `acercándono` | `acercarse` | 392 | review: merge |
| `adicionale` | `adicional` | 451 | review: merge |
| `ctra` | `carretera` | 435 | review: merge |
| `enséñano` | `enseñar` | 324 | review: merge |
| `extragrand` | `extragrande` | 436 | review: merge |
| `mecena` | `mecenas` | 408 | review: merge |
| `ocuparno` | `ocuparse` | 441 | review: merge |
| `poleras` | `polera` | 503 | review: merge |
| `post-producción` | `posproducción` | 539 | review: merge |
| `telex` | `télex` | 464 | review: merge |
| `tipográficos` | `tipográfico` | 532 | review: merge |
| `auto-realización` | `autorrealización` | 355 | review: merge |
| `catalogo` | `catálogo` | 433 | review: merge |
| `sofás-cama` | `sofá cama` | 422 | review: merge |
| `trafico` | `tráfico` | 269 | review: merge |
| `apartao` | `apartar` | 448 | review: merge |
| `ciencia-ficción` | `ciencia ficción` | 521 | review: merge |
| `contacteno` | `contactar` | 477 | review: merge |
| `cortex` | `córtex` | 441 | review: merge |
| `expresso` | `expreso` | 425 | review: merge |
| `khaki` | `caqui` | 398 | review: merge |
| `microfiber` | `microfibra` | 454 | review: merge |
| `plegador` | `plegadora` | 589 | review: merge |
| `pre-escolar` | `preescolar` | 448 | review: merge |
| `subid` | `subir` | 482 | review: merge |
| `ajustándono` | `ajustarse` | 422 | review: merge |
| `auditorium` | `auditorio` | 465 | review: merge |
| `excreto` | `excretar` | 596 | review: merge |
| `investiga` | `investigar` | 476 | review: merge |
| `pavimentador` | `pavimentadora` | 420 | review: merge |
| `pintalabio` | `pintalabios` | 373 | review: merge |
| `plantas` | `planta` | 407 | review: merge |
| `portabicicleta` | `portabicicletas` | 417 | review: merge |
| `pre-producción` | `preproducción` | 322 | review: merge |
| `proxie` | `proxy` | 428 | review: merge |
| `reggaeton` | `reguetón` | 391 | review: merge |
| `sumergirno` | `sumergirse` | 489 | review: merge |
| `verl` | `ver` | 414 | review: merge |
| `actualice` | `actualizar` | 379 | review: merge |
| `anti-polvo` | `antipolvo` | 487 | review: merge |
| `cuentagota` | `cuentagotas` | 370 | review: merge |
| `distribuidores` | `distribuidor` | 253 | review: merge |
| `etica` | `ética` | 348 | review: merge |
| `gramíneo` | `gramínea` | 499 | review: merge |
| `otror` | `otrora` | 349 | review: merge |
| `pendienteo` | `pendiente` | 364 | review: merge |
| `quads` | `quad` | 494 | review: merge |
| `quasar` | `cuásar` | 407 | review: merge |
| `ame` | `amar` | 436 | review: merge |
| `condominium` | `condominio` | 374 | review: merge |
| `dejándol` | `dejar` | 387 | review: merge |
| `dermatiti` | `dermatitis` | 453 | review: merge |
| `después-venta` | `posventa` | 349 | review: merge |
| `in-situ` | `in situ` | 572 | review: merge |
| `multifor` | `multiforme` | 474 | review: merge |
| `plexiglas` | `plexiglás` | 383 | review: merge |
| `spirulina` | `espirulina` | 358 | review: merge |
| `vegana` | `vegano` | 323 | review: merge |
| `yo-yo` | `yoyó` | 363 | review: merge |
| `apocalypse` | `apocalipsis` | 435 | review: merge |
| `bendecida` | `bendecir` | 412 | review: merge |
| `cañado` | `cañada` | 451 | review: merge |
| `comprometiéndono` | `comprometerse` | 256 | review: merge |
| `dra` | `doctor` | 469 | review: merge |
| `epsilon` | `épsilon` | 317 | review: merge |
| `imprime` | `imprimir` | 498 | review: merge |
| `intramuro` | `intramuros` | 349 | review: merge |
| `multi-función` | `multifunción` | 466 | review: merge |
| `mándeno` | `mandar` | 315 | review: merge |
| `raglan` | `raglán` | 313 | review: merge |
| `bóia` | `boya` | 296 | review: merge |
| `correo-e` | `correo electrónico` | 475 | review: merge |
| `estr` | `estrés` | 382 | review: merge |
| `incidentales` | `incidental` | 433 | review: merge |
| `magnesium` | `magnesio` | 352 | review: merge |
| `moka` | `moca` | 361 | review: merge |
| `omnibus` | `ómnibus` | 447 | review: merge |
| `post-it` | `pósit` | 311 | review: merge |
| `preparándono` | `prepararse` | 287 | review: merge |
| `rizada` | `rizado` | 416 | review: merge |
| `anti-inflamatorias` | `antiinflamatorio` | 339 | review: merge |
| `bloq` | `bloqueo` | 286 | review: merge |
| `crayon` | `crayón` | 295 | review: merge |
| `cyan` | `cian` | 362 | review: merge |
| `deposito` | `depósito` | 452 | review: merge |
| `hablándol` | `hablar` | 276 | review: merge |
| `hobbie` | `hobby` | 442 | review: merge |
| `inexactitudes` | `inexactitud` | 487 | review: merge |
| `leds` | `led` | 388 | review: merge |
| `naif` | `naíf` | 342 | review: merge |
| `patche` | `parche` | 280 | review: merge |
| `patr` | `patrón` | 395 | review: merge |
| `senora` | `señora` | 416 | review: merge |
| `tutu` | `tutú` | 333 | review: merge |
| `volleyball` | `voleibol` | 330 | review: merge |
| `barbecue` | `barbacoa` | 377 | review: merge |
| `borrados` | `borrar` | 335 | review: merge |
| `centro-izquierda` | `centroizquierda` | 315 | review: merge |
| `doxycycline` | `doxiciclina` | 323 | review: merge |
| `ejercito` | `ejército` | 339 | review: merge |
| `enséñel` | `enseñar` | 284 | review: merge |
| `filmador` | `filmadora` | 380 | review: merge |
| `gir` | `girar` | 293 | review: merge |
| `mini-juego` | `minijuego` | 454 | review: merge |
| `minibuse` | `minibús` | 221 | review: merge |
| `nickel` | `níquel` | 265 | review: merge |
| `pasamontaña` | `pasamontañas` | 297 | review: merge |
| `perderno` | `perderse` | 294 | review: merge |
| `ratoncito` | `ratón` | 79 | review: merge |
| `re-enfocar` | `reenfocar` | 351 | review: merge |
| `volley` | `vóley` | 413 | review: merge |
| `acuérdate` | `acordarse` | 283 | review: merge |
| `afrikaans` | `afrikáans` | 320 | review: merge |
| `apart-hotel` | `apartahotel` | 305 | review: merge |
| `años-luz` | `año luz` | 466 | review: merge |
| `bazooka` | `bazuca` | 326 | review: merge |
| `brasileiro` | `brasileño` | 308 | review: merge |
| `chassis` | `chasis` | 366 | review: merge |
| `enviándol` | `enviar` | 332 | review: merge |
| `escribirno` | `escribir` | 283 | review: merge |
| `fakir` | `faquir` | 280 | review: merge |
| `garifuna` | `garífuna` | 423 | review: merge |
| `indústria` | `industria` | 281 | review: merge |
| `jajajaja` | `jaja` | 354 | review: merge |
| `minibu` | `minibús` | 234 | review: merge |
| `máquina-herramienta` | `máquina herramienta` | 483 | review: merge |
| `pyrex` | `pírex` | 280 | review: merge |
| `sudadero` | `sudadera` | 350 | review: merge |
| `anti-estrés` | `antiestrés` | 312 | review: merge |
| `codero` | `cordero` | 284 | review: merge |
| `cuidados` | `cuidado` | 284 | review: merge |
| `dob` | `doble` | 427 | review: merge |
| `encuenstra` | `encontrar` | 355 | review: merge |
| `euskara` | `euskera` | 270 | review: merge |
| `gilipolla` | `gilipollas` | 200 | review: merge |
| `golem` | `gólem` | 370 | review: merge |
| `grátis` | `gratis` | 374 | review: merge |
| `llamarno` | `llamar` | 306 | review: merge |
| `magyar` | `magiar` | 290 | review: merge |
| `materno-infantil` | `maternoinfantil` | 318 | review: merge |
| `mostraro` | `mostrar` | 358 | review: merge |
| `multi-funcional` | `multifuncional` | 315 | review: merge |
| `notícias` | `noticia` | 250 | review: merge |
| `olvidarno` | `olvidarse` | 278 | review: merge |
| `planifique` | `planificar` | 332 | review: merge |
| `posavaso` | `posavasos` | 453 | review: merge |
| `rechazan` | `rechazar` | 320 | review: merge |
| `reconociendo` | `reconocer` | 330 | review: merge |
| `spanglish` | `espanglish` | 195 | review: merge |
| `superventa` | `superventas` | 216 | review: merge |
| `unisexo` | `unisex` | 345 | review: merge |
| `abrelata` | `abrelatas` | 280 | review: merge |
| `acercaos` | `acercarse` | 381 | review: merge |
| `adem` | `además` | 237 | review: merge |
| `alejarno` | `alejarse` | 307 | review: merge |
| `barberos` | `barbero` | 333 | review: merge |
| `centro-derecha` | `centroderecha` | 268 | review: merge |
| `corta` | `corto` | 273 | review: merge |
| `e-cigarrillo` | `cigarrillo electrónico` | 324 | review: merge |
| `guardacosta` | `guardacostas` | 485 | review: merge |
| `mea` | `mear` | 423 | review: merge |
| `muell` | `muelle` | 9,001 | review: merge |
| `personalizabl` | `personalizable` | 5,061 | review: merge |
| `ofrecerl` | `ofrecer` | 4,131 | review: merge |
| `dobl` | `doble` | 3,101 | review: merge |
| `encuentr` | `encontrar` | 2,446 | review: merge |
| `brindarl` | `brindar` | 2,138 | review: merge |
| `puzl` | `puzle` | 2,016 | review: merge |
| `descargabl` | `descargable` | 1,918 | review: merge |
| `enseñarl` | `enseñar` | 1,404 | review: merge |
| `proporcionarl` | `proporcionar` | 1,107 | review: merge |
| `multipl` | `múltiple` | 1,242 | review: merge |
| `azafr` | `azafrán` | 1,263 | review: merge |
| `increibl` | `increíble` | 1,058 | review: merge |
| `mostrarl` | `mostrar` | 1,382 | review: merge |
| `coleccionabl` | `coleccionable` | 1,147 | review: merge |
| `psiquiatr` | `psiquiatría` | 809 | review: merge |
| `prevenibl` | `prevenible` | 956 | review: merge |
| `jugabl` | `jugable` | 1,019 | review: merge |
| `servirl` | `servir` | 831 | review: merge |
| `waffl` | `wafle` | 871 | review: merge |
| `masticabl` | `masticable` | 579 | review: merge |
| `invaluabl` | `invaluable` | 571 | review: merge |
| `agradecerl` | `agradecer` | 558 | review: merge |
| `otorgarl` | `otorgar` | 345 | review: merge |
| `permitirl` | `permitir` | 435 | review: merge |
| `descartabl` | `descartable` | 451 | review: merge |
| `transmitirl` | `transmitir` | 319 | review: merge |
| `enviarl` | `enviar` | 381 | review: merge |
| `espectrometr` | `espectrometría` | 364 | review: merge |
| `idolatr` | `idolatría` | 406 | review: merge |
| `liposolubl` | `liposoluble` | 303 | review: merge |
| `causarl` | `causar` | 224 | review: merge |
| `compartirl` | `compartir` | 348 | review: merge |
| `hablarl` | `hablar` | 336 | review: merge |
| `llevarl` | `llevar` | 345 | review: merge |
| `hazl` | `hacer` | 229 | review: merge |
| `portacabl` | `portacables` | 313 | review: merge |
| `psiquiátra` | `psiquiatra` | 222 | review: merge |
| `quitanieve` | `quitanieves` | 331 | review: merge |
| `roast` | `rosbif` | 305 | review: merge |
| `superf` | `superficie` | 248 | review: merge |
| `veintitanto` | `veintitantos` | 219 | review: merge |
| `agrocombustibl` | `agrocombustible` | 385 | review: merge |
| `aparcamento` | `aparcamiento` | 265 | review: merge |
| `arrepentío` | `arrepentirse` | 250 | review: merge |
| `auto-ayuda` | `autoayuda` | 294 | review: merge |
| `concordancias` | `concordancia` | 278 | review: merge |
| `curcumin` | `curcumina` | 396 | review: merge |
| `deleitarno` | `deleitarse` | 251 | review: merge |
| `desbloqueabl` | `desbloqueable` | 257 | review: merge |
| `despedirno` | `despedirse` | 317 | review: merge |
| `diciéndono` | `decir` | 188 | review: merge |
| `e-books` | `e-book` | 379 | review: merge |
| `emulator` | `emulador` | 301 | review: merge |
| `enfocándo` | `enfocar` | 258 | review: merge |
| `enséñal` | `enseñar` | 313 | review: merge |
| `ex-presidente` | `expresidente` | 413 | review: merge |
| `fueron` | `ser` | 334 | review: merge |
| `l-glutamina` | `glutamina` | 368 | review: merge |
| `l-teanina` | `teanina` | 194 | review: merge |
| `legionella` | `legionela` | 395 | review: merge |
| `muéstral` | `mostrar` | 261 | review: merge |
| `neuroendocrinos` | `neuroendocrino` | 292 | review: merge |
| `off-line` | `offline` | 369 | review: merge |
| `pancakes` | `panqueque` | 377 | review: merge |
| `polyimide` | `poliimida` | 284 | review: merge |
| `redon` | `redondo` | 240 | review: merge |
| `teka` | `teca` | 423 | review: merge |
| `vendo` | `vender` | 218 | review: merge |
| `vice-presidente` | `vicepresidente` | 307 | review: merge |
| `zig-zag` | `zigzag` | 351 | review: merge |
| `abrebotella` | `abrebotellas` | 279 | review: merge |
| `alf` | `alfa` | 408 | review: merge |
| `bajero` | `bajera` | 298 | review: merge |
| `boomers` | `boomer` | 341 | review: merge |
| `cazafantasma` | `cazafantasmas` | 258 | review: merge |
| `co-fundadora` | `cofundador` | 252 | review: merge |
| `conserve` | `conservar` | 301 | review: merge |
| `eufrate` | `éufrates` | 285 | review: merge |
| `gangster` | `gánster` | 314 | review: merge |
| `hurtadilla` | `hurtadillas` | 163 | review: merge |
| `informándol` | `informar` | 311 | review: merge |
| `kilate` | `quilate` | 293 | review: merge |
| `mamás` | `mamá` | 343 | review: merge |
| `poniéndono` | `ponerse` | 283 | review: merge |
| `quedarno` | `quedarse` | 220 | review: merge |
| `reumatoideo` | `reumatoide` | 279 | review: merge |
| `taca` | `taza` | 355 | review: merge |
| `talleres` | `taller` | 293 | review: merge |
| `aymara` | `aimara` | 286 | review: merge |
| `bacterial` | `bacteriano` | 331 | review: merge |
| `bautisto` | `bautista` | 258 | review: merge |
| `catamaran` | `catamarán` | 337 | review: merge |
| `centrarno` | `centrarse` | 194 | review: merge |
| `desconocidas` | `desconocido` | 198 | review: merge |
| `doma` | `domar` | 320 | review: merge |
| `enseñándono` | `enseñar` | 231 | review: merge |
| `ex-novia` | `exnovia` | 317 | review: merge |
| `hryvnia` | `grivna` | 304 | review: merge |
| `intimo` | `íntimo` | 264 | review: merge |
| `kilométro` | `kilómetro` | 395 | review: merge |
| `lapis` | `lapislázuli` | 317 | review: merge |
| `lic` | `licenciado` | 279 | review: merge |
| `mesquita` | `mezquita` | 170 | review: merge |
| `mitzvot` | `mitzvá` | 350 | review: merge |
| `otorgándol` | `otorgar` | 288 | review: merge |
| `portadocumento` | `portadocumentos` | 236 | review: merge |
| `portatarjeta` | `portatarjetas` | 338 | review: merge |
| `post-procesamiento` | `posprocesamiento` | 176 | review: merge |
| `prepárese` | `preparar` | 299 | review: merge |
| `quran` | `corán` | 278 | review: merge |
| `quórume` | `quórum` | 185 | review: merge |
| `recopilamos` | `recopilar` | 279 | review: merge |
| `requiem` | `réquiem` | 301 | review: merge |
| `retinoid` | `retinoide` | 260 | review: merge |
| `sheij` | `jeque` | 281 | review: merge |
| `socio-económica` | `socioeconómico` | 358 | review: merge |
| `subtitu` | `subtítulo` | 283 | review: merge |
| `sur-oriental` | `suroriental` | 211 | review: merge |
| `telemetr` | `telemetría` | 298 | review: merge |
| `zircon` | `circón` | 357 | review: merge |
| `acabé` | `acabar` | 169 | review: merge |
| `animo` | `animar` | 223 | review: merge |
| `apocal` | `apocalipsis` | 429 | review: merge |
| `asumí` | `asumir` | 62 | review: merge |
| `audio-visual` | `audiovisual` | 267 | review: merge |
| `berebere` | `bereber` | 65 | review: merge |
| `co-director` | `codirector` | 293 | review: merge |
| `cosmetica` | `cosmética` | 129 | review: merge |
| `explicaro` | `explicar` | 217 | review: merge |
| `filiales` | `filial` | 300 | review: merge |
| `gul` | `gules` | 281 | review: merge |
| `interoperabl` | `interoperable` | 323 | review: merge |
| `invitarl` | `invitar` | 331 | review: merge |
| `limousine` | `limusina` | 354 | review: merge |
| `megapixels` | `megapíxel` | 239 | review: merge |
| `muertos` | `muerto` | 353 | review: merge |
| `multimedio` | `multimedia` | 390 | review: merge |
| `niacin` | `niacina` | 254 | review: merge |
| `optimice` | `optimizar` | 238 | review: merge |
| `perjuicios` | `perjuicio` | 215 | review: merge |
| `polka` | `polca` | 286 | review: merge |
| `ponerl` | `poner` | 276 | review: merge |
| `portapapele` | `portapapeles` | 263 | review: merge |
| `pre-instalación` | `preinstalación` | 286 | review: merge |
| `pregúntel` | `preguntar` | 281 | review: merge |
| `proactiva` | `proactivo` | 145 | review: merge |
| `socio-político` | `sociopolítico` | 314 | review: merge |
| `spin-offs` | `spin-off` | 186 | review: merge |
| `tamoxifen` | `tamoxifeno` | 287 | review: merge |
| `taser` | `táser` | 270 | review: merge |
| `tretinoin` | `tretinoína` | 237 | review: merge |
| `univ` | `universidad` | 352 | review: merge |
| `albume` | `álbum` | 229 | review: merge |
| `ansiso` | `ansioso` | 200 | review: merge |
| `apoyándono` | `apoyarse` | 203 | review: merge |
| `atrave` | `atravesar` | 288 | review: merge |
| `auto-conocimiento` | `autoconocimiento` | 161 | review: merge |
| `ayúdano` | `ayudar` | 223 | review: merge |
| `benchmarks` | `benchmark` | 274 | review: merge |
| `co-crear` | `cocrear` | 323 | review: merge |
| `co-presidente` | `copresidente` | 242 | review: merge |
| `convertío` | `convertir` | 272 | review: merge |
| `freelancers` | `freelance` | 229 | review: merge |
| `gral` | `general` | 262 | review: merge |
| `inclina` | `inclinar` | 176 | review: merge |
| `inmobiliarias` | `inmobiliaria` | 197 | review: merge |
| `inserte` | `insertar` | 291 | review: merge |
| `jiu-jitsu` | `yiu-yitsu` | 224 | review: merge |
| `lame` | `lamer` | 139 | review: merge |
| `lanzallama` | `lanzallamas` | 257 | review: merge |
| `liquitación` | `liquidación` | 246 | review: merge |
| `mantenerl` | `mantener` | 133 | review: merge |
| `menonitas` | `menonita` | 208 | review: merge |
| `minicargadore` | `minicargador` | 306 | review: merge |
| `mostrándol` | `mostrar` | 336 | review: merge |
| `penalty` | `penalti` | 251 | review: merge |
| `portabroca` | `portabrocas` | 243 | review: merge |
| `pre-existentes` | `preexistente` | 258 | review: merge |
| `click` | `clic` | 50,809 | review: merge |
| `reserve` | `reservar` | 41,184 | review: merge |
| `jul` | `julio` | 35,738 | review: merge |
| `busca` | `buscar` | 34,111 | review: merge |
| `descargue` | `descargar` | 34,692 | review: merge |
| `clara` | `claro` | 28,317 | review: merge |
| `poker` | `póker` | 21,741 | review: merge |
| `atrever` | `atreverse` | 16,707 | review: merge |
| `familiarízate` | `familiarizarse` | 18,867 | review: merge |
| `alta` | `alto` | 17,338 | review: merge |
| `visto` | `ver` | 15,433 | review: merge |
| `administrativa` | `administrativo` | 14,899 | review: merge |
| `reyes` | `rey` | 14,034 | review: merge |
| `arar` | `aro` | 15,118 | review: merge |
| `regístrese` | `registrarse` | 14,786 | review: merge |
| `guárdela` | `guardar` | 14,139 | review: merge |
| `campos` | `campo` | 11,239 | review: merge |
| `flores` | `flor` | 11,911 | review: merge |
| `almohadillar` | `almohadilla` | 11,374 | review: merge |
| `ponte` | `ponerse` | 10,162 | review: merge |
| `iglesias` | `iglesia` | 10,204 | review: merge |
| `hechos` | `hecho` | 9,927 | review: merge |
| `consultá` | `consultar` | 10,751 | review: merge |
| `suscríbase` | `suscribirse` | 9,704 | review: merge |
| `explore` | `explorar` | 9,895 | review: merge |
| `derechar` | `derecho` | 9,576 | review: merge |
| `roturar` | `rotura` | 9,297 | review: merge |
| `reales` | `real` | 8,941 | review: merge |
| `fallir` | `fallido` | 8,062 | review: merge |
| `oct` | `octubre` | 8,412 | review: merge |
| `jun` | `junio` | 8,551 | review: merge |
| `ejecutiva` | `ejecutivo` | 7,683 | review: merge |
| `turbinar` | `turbina` | 8,221 | review: merge |
| `incensar` | `incienso` | 8,025 | review: merge |
| `ref` | `referencia` | 8,282 | review: merge |
| `máx` | `máximo` | 7,722 | review: merge |
| `dino` | `decir` | 7,540 | review: merge |
| `forjado` | `forjar` | 7,568 | review: merge |
| `escalonar` | `escalón` | 7,331 | review: merge |
| `tributar` | `tributo` | 7,087 | review: merge |
| `llamadas` | `llamada` | 7,447 | review: merge |
| `nov` | `noviembre` | 7,331 | review: merge |
| `bridar` | `brida` | 7,356 | review: merge |
| `esterar` | `estera` | 6,962 | review: merge |
| `tintar` | `tinte` | 6,898 | review: merge |
| `versar` | `verso` | 6,452 | review: merge |
| `eclipsar` | `eclipse` | 6,394 | review: merge |
| `cargue` | `cargar` | 6,506 | review: merge |
| `magnificar` | `magnífico` | 7,095 | review: merge |
| `mantente` | `mantenerse` | 5,981 | review: merge |
| `azufrar` | `azufre` | 6,598 | review: merge |
| `guión` | `guion` | 6,036 | review: merge |
| `seguida` | `seguir` | 5,653 | review: merge |
| `sobretodo` | `sobre todo` | 6,390 | review: merge |
| `charter` | `chárter` | 6,061 | review: merge |
| `falto` | `falta` | 5,656 | review: merge |
| `dic` | `diciembre` | 6,292 | review: merge |
| `plugins` | `plugin` | 6,522 | review: merge |
| `manuscribir` | `manuscrito` | 5,882 | review: merge |
| `frita` | `frito` | 5,676 | review: merge |
| `cabalá` | `cábala` | 5,434 | review: merge |
| `fuiste` | `ser` | 4,188 | review: merge |
| `introcuzca` | `introducir` | 5,692 | review: merge |
| `arroyar` | `arroyo` | 5,607 | review: merge |
| `ozonar` | `ozono` | 6,047 | review: merge |
| `diafragmar` | `diafragma` | 5,564 | review: merge |
| `trailer` | `tráiler` | 5,881 | review: merge |
| `timbrar` | `timbre` | 5,387 | review: merge |
| `olear` | `oleada` | 5,781 | review: merge |
| `diríjase` | `dirigirse` | 5,321 | review: merge |
| `llagar` | `llaga` | 5,696 | review: merge |
| `cariar` | `caries` | 5,488 | review: merge |
| `status` | `estatus` | 5,469 | review: merge |
| `chefs` | `chef` | 5,504 | review: merge |
| `pigmentar` | `pigmento` | 5,724 | review: merge |
| `posts` | `post` | 5,288 | review: merge |
| `yodar` | `yodo` | 5,201 | review: merge |
| `duplex` | `dúplex` | 5,362 | review: merge |
| `relájese` | `relajarse` | 5,080 | review: merge |
| `gifs` | `gif` | 5,680 | review: merge |
| `providenciar` | `providencia` | 5,234 | review: merge |
| `solarium` | `solárium` | 5,281 | review: merge |
| `cargada` | `cargado` | 5,219 | review: merge |
| `ajuster` | `ajustar` | 5,479 | review: merge |
| `limpia` | `limpio` | 4,676 | review: merge |
| `redirigido` | `redirigir` | 5,045 | review: merge |
| `ene` | `enero` | 4,524 | review: merge |
| `cosmo` | `cosmos` | 4,748 | review: merge |
| `escamar` | `escama` | 4,139 | review: merge |
| `dile` | `decir` | 3,960 | review: merge |
| `ping` | `ping-pong` | 4,827 | review: merge |
| `alójate` | `alojarse` | 4,888 | review: merge |
| `espigar` | `espiga` | 4,469 | review: merge |
| `macizar` | `macizo` | 4,831 | review: merge |
| `escucha` | `escuchar` | 4,198 | review: merge |
| `levar` | `leva` | 4,165 | review: merge |
| `mazar` | `mazo` | 4,267 | review: merge |
| `cocar` | `coca` | 4,838 | review: merge |
| `felpar` | `felpa` | 4,186 | review: merge |
| `ven` | `venir` | 4,293 | review: merge |
| `startups` | `startup` | 4,340 | review: merge |
| `dirigiéndose` | `dirigirse` | 4,115 | review: merge |
| `enviado` | `enviar` | 4,653 | review: merge |
| `manir` | `maní` | 4,048 | review: merge |
| `sic` | `siclo` | 4,722 | review: merge |
| `herniar` | `hernia` | 4,115 | review: merge |
| `broker` | `bróker` | 3,987 | review: merge |
| `relájate` | `relajarse` | 4,149 | review: merge |
| `sorprendase` | `sorprenderse` | 3,934 | review: merge |
| `clorurar` | `cloruro` | 3,843 | review: merge |
| `computarizada` | `computarizado` | 3,881 | review: merge |
| `tragaperra` | `tragaperras` | 3,941 | review: merge |
| `moldurar` | `moldura` | 4,042 | review: merge |
| `ortografiar` | `ortografía` | 3,756 | review: merge |
| `hip` | `hip hop` | 4,029 | review: merge |
| `magento` | `magenta` | 3,551 | review: merge |
| `cartografiar` | `cartografía` | 3,520 | review: merge |
| `cuantiar` | `cuantía` | 3,650 | review: merge |
| `penitenciar` | `penitencia` | 3,595 | review: merge |
| `mirá` | `mirar` | 2,985 | review: merge |
| `condonar` | `condón` | 4,040 | review: merge |
| `cluster` | `clúster` | 3,571 | review: merge |
| `expensar` | `expensas` | 3,387 | review: merge |
| `substanciar` | `sustancia` | 3,352 | review: merge |
| `escobillar` | `escobilla` | 3,376 | review: merge |
| `poster` | `póster` | 3,130 | review: merge |
| `cielos` | `cielo` | 3,476 | review: merge |
| `comic` | `cómic` | 3,241 | review: merge |
| `muchísimo` | `mucho` | 3,271 | review: merge |
| `refiriéndose` | `referirse` | 3,455 | review: merge |
| `cesáreo` | `cesárea` | 3,067 | review: merge |
| `sumérgete` | `sumergirse` | 3,271 | review: merge |
| `carburar` | `carburo` | 3,419 | review: merge |
| `hamburgués` | `hamburguesa` | 3,016 | review: merge |
| `banners` | `banner` | 3,328 | review: merge |
| `estelarizadas` | `estelarizar` | 3,143 | review: merge |
| `escorts` | `escort` | 3,144 | review: merge |
| `dele` | `dar` | 3,388 | review: merge |
| `souvenirs` | `souvenir` | 3,302 | review: merge |
| `curriculum` | `currículum` | 2,981 | review: merge |
| `carbonatar` | `carbonato` | 3,096 | review: merge |
| `cortocircuitar` | `cortocircuito` | 3,046 | review: merge |
| `rallye` | `rally` | 2,886 | review: merge |
| `sulfatar` | `sulfato` | 2,933 | review: merge |
| `avellanar` | `avellana` | 2,699 | review: merge |
| `ecommerce` | `e-commerce` | 2,839 | review: merge |
| `desplácese` | `desplazarse` | 2,646 | review: merge |
| `pilate` | `pilates` | 2,907 | review: merge |
| `fosar` | `fosa` | 2,752 | review: merge |
| `cadmiar` | `cadmio` | 2,799 | review: merge |
| `totál` | `total` | 2,680 | review: merge |
| `bitcoins` | `bitcoin` | 2,956 | review: merge |
| `toldar` | `toldo` | 2,856 | review: merge |
| `buscá` | `buscar` | 2,732 | review: merge |
| `especímenes` | `espécimen` | 2,743 | review: merge |
| `daro` | `dar` | 2,315 | review: merge |
| `lujuriar` | `lujuria` | 2,686 | review: merge |
| `podcasts` | `podcast` | 2,656 | review: merge |
| `subscríbete` | `suscribirse` | 2,692 | review: merge |
| `arpar` | `arpa` | 2,452 | review: merge |
| `explorá` | `explorar` | 2,541 | review: merge |
| `petar` | `peto` | 2,617 | review: merge |
| `reacondicionados` | `reacondicionar` | 2,752 | review: merge |
| `coupé` | `cupé` | 2,529 | review: merge |
| `necesitás` | `necesitar` | 1,972 | review: merge |
| `imagínate` | `imaginarse` | 2,174 | review: merge |
| `únete` | `unirse` | 2,403 | review: merge |
| `espanol` | `español` | 2,335 | review: merge |
| `spas` | `spa` | 2,360 | review: merge |
| `fosfatar` | `fosfato` | 2,539 | review: merge |
| `runo` | `runa` | 2,320 | review: merge |
| `políticas` | `política` | 2,364 | review: merge |
| `elije` | `elegir` | 2,680 | review: merge |
| `buffer` | `búfer` | 2,283 | review: merge |
| `incluído` | `incluir` | 2,446 | review: merge |
| `inox` | `inoxidable` | 2,298 | review: merge |
| `pulg` | `pulgada` | 2,439 | review: merge |
| `empiece` | `empezar` | 2,202 | review: merge |
| `embudar` | `embudo` | 2,531 | review: merge |
| `resor` | `resorte` | 2,253 | review: merge |
| `cocktail` | `cóctel` | 2,305 | review: merge |
| `webcams` | `webcam` | 2,189 | review: merge |
| `cassette` | `casete` | 2,238 | review: merge |
| `conciente` | `consciente` | 1,972 | review: merge |
| `estampillar` | `estampilla` | 1,733 | review: merge |
| `avispar` | `avispa` | 1,748 | review: merge |
| `vistar` | `vista` | 2,261 | review: merge |
| `imagínese` | `imaginarse` | 2,191 | review: merge |
| `tranzar` | `trance` | 2,044 | review: merge |
| `autobu` | `autobús` | 2,341 | review: merge |
| `indumentario` | `indumentaria` | 1,975 | review: merge |
| `laudar` | `laudo` | 2,134 | review: merge |
| `reale` | `real` | 2,058 | review: merge |
| `mocar` | `moco` | 2,147 | review: merge |
| `ojalar` | `ojal` | 2,190 | review: merge |
| `traders` | `trader` | 2,150 | review: merge |
| `caligrafiar` | `caligrafía` | 2,074 | review: merge |
| `candar` | `candado` | 1,821 | review: merge |
| `indulgenciar` | `indulgencia` | 1,951 | review: merge |
| `llegarí` | `llegar` | 2,213 | review: merge |
| `trinchero` | `trinchera` | 1,926 | review: merge |
| `uds` | `ustedes` | 2,067 | review: merge |
| `escoriar` | `escoria` | 1,923 | review: merge |
| `usá` | `usar` | 1,922 | review: merge |
| `demando` | `demanda` | 2,127 | review: merge |
| `ej` | `ejemplo` | 2,014 | review: merge |
| `correar` | `correa` | 2,167 | review: merge |
| `está` | `estar` | 1,790 | review: merge |
| `vol` | `volumen` | 2,156 | review: merge |
| `buscás` | `buscar` | 2,171 | review: merge |
| `resúmen` | `resumen` | 1,898 | review: merge |
| `desigualar` | `desigual` | 1,810 | review: merge |
| `pallet` | `palé` | 1,946 | review: merge |
| `paracaída` | `paracaídas` | 1,870 | review: merge |
| `balar` | `bala` | 1,938 | review: merge |
| `desesperanzar` | `desesperanza` | 1,731 | review: merge |
| `extrañir` | `extraño` | 1,662 | review: merge |
| `millennials` | `millennial` | 2,020 | review: merge |
| `ato` | `atar` | 1,875 | review: merge |
| `enserar` | `enseres` | 1,953 | review: merge |
| `acércate` | `acercarse` | 1,813 | review: merge |
| `bugs` | `bug` | 2,063 | review: merge |
| `gratar` | `grato` | 1,932 | review: merge |
| `recamar` | `recámara` | 1,994 | review: merge |
| `tajar` | `tajada` | 1,480 | review: merge |
| `atópica` | `atópico` | 1,871 | review: merge |
| `bizcochar` | `bizcocho` | 1,711 | review: merge |
| `gofrar` | `gofre` | 1,791 | review: merge |
| `ponter` | `ponerse` | 1,119 | review: merge |
| `sintiéndose` | `sentirse` | 1,808 | review: merge |
| `ampere` | `amperio` | 2,122 | review: merge |
| `maliciar` | `malicia` | 1,803 | review: merge |
| `motora` | `motor` | 1,982 | review: merge |
| `fuer` | `ser` | 1,496 | review: merge |
| `carnicer` | `carnicería` | 1,520 | review: merge |
| `planificá` | `planificar` | 1,734 | review: merge |
| `primas` | `prima` | 1,627 | review: merge |
| `deshabilita` | `deshabilitar` | 1,706 | review: merge |
| `flavonoid` | `flavonoide` | 1,563 | review: merge |
| `softwar` | `software` | 1,901 | review: merge |
| `víver` | `víveres` | 1,350 | review: merge |
| `úsalas` | `usar` | 1,878 | review: merge |
| `resacar` | `resaca` | 1,502 | review: merge |
| `técnicar` | `técnica` | 1,687 | review: merge |
| `intimar` | `íntimo` | 1,541 | review: merge |
| `bloggers` | `blogger` | 1,722 | review: merge |
| `catapultar` | `catapulta` | 1,682 | review: merge |
| `chateo` | `chatear` | 1,535 | review: merge |
| `cripto` | `criptomoneda` | 1,619 | review: merge |
| `faenar` | `faena` | 1,661 | review: merge |
| `fórum` | `foro` | 1,527 | review: merge |
| `hashtags` | `hashtag` | 1,876 | review: merge |
| `mander` | `mando` | 1,849 | review: merge |
| `siembrir` | `siembra` | 1,809 | review: merge |
| `clica` | `clicar` | 1,802 | review: merge |
| `columpiar` | `columpio` | 1,515 | review: merge |
| `odenador` | `ordenador` | 1,626 | review: merge |
| `arenisco` | `arenisca` | 1,664 | review: merge |
| `cupcakes` | `cupcake` | 1,698 | review: merge |
| `electrónicar` | `electrónica` | 1,429 | review: merge |
| `hacé` | `hacer` | 1,439 | review: merge |
| `racks` | `rack` | 2,055 | review: merge |
| `cachar` | `cacho` | 1,336 | review: merge |
| `papar` | `papada` | 1,625 | review: merge |
| `refiérase` | `referirse` | 1,612 | review: merge |
| `listonar` | `listón` | 1,810 | review: merge |
| `visitá` | `visitar` | 1,777 | review: merge |
| `burritos` | `burrito` | 1,789 | review: merge |
| `folklore` | `folclore` | 1,598 | review: merge |
| `newsletters` | `newsletter` | 1,706 | review: merge |
| `desfasar` | `desfase` | 1,506 | review: merge |
| `muerta` | `muerto` | 1,518 | review: merge |
| `endurar` | `enduro` | 1,455 | review: merge |
| `tuits` | `tuit` | 1,768 | review: merge |
| `laptops` | `laptop` | 1,637 | review: merge |
| `mismísimo` | `mismo` | 1,424 | review: merge |
| `muelles` | `muelle` | 1,400 | review: merge |
| `suelta` | `suelto` | 1,222 | review: merge |
| `redireccionado` | `redireccionar` | 1,575 | review: merge |
| `nitratar` | `nitrato` | 1,811 | review: merge |
| `pellets` | `pellet` | 1,628 | review: merge |
| `plug-ins` | `plug-in` | 1,826 | review: merge |
| `bendecido` | `bendecir` | 1,524 | review: merge |
| `colorar` | `colorado` | 1,436 | review: merge |
| `desusar` | `desuso` | 1,723 | review: merge |
| `iner` | `inerte` | 1,666 | review: merge |
| `tuiteó` | `tuitear` | 1,494 | review: merge |
| `cizañar` | `cizaña` | 1,655 | review: merge |
| `emojis` | `emoji` | 1,479 | review: merge |
| `hocicar` | `hocico` | 1,420 | review: merge |
| `pesquisar` | `pesquisa` | 1,488 | review: merge |
| `feeds` | `feed` | 1,410 | review: merge |
| `codec` | `códec` | 1,704 | review: merge |
| `flagelar` | `flagelo` | 1,372 | review: merge |
| `lavada` | `lavar` | 1,313 | review: merge |
| `lazar` | `lazada` | 1,592 | review: merge |
| `torna` | `tornar` | 1,473 | review: merge |
| `parafinar` | `parafina` | 1,369 | review: merge |
| `querellar` | `querella` | 1,580 | review: merge |
| `twittear` | `tuitear` | 1,515 | review: merge |
| `capsular` | `cápsula` | 1,451 | review: merge |
| `likes` | `like` | 1,445 | review: merge |
| `remachar` | `remache` | 1,453 | review: merge |
| `emulsionar` | `emulsión` | 1,410 | review: merge |
| `estufar` | `estufa` | 1,642 | review: merge |
| `expandiéndose` | `expandirse` | 1,253 | review: merge |
| `inmersiva` | `inmersivo` | 1,457 | review: merge |
| `maderar` | `madera` | 1,465 | review: merge |
| `veintiún` | `veintiuno` | 1,488 | review: merge |
| `boyar` | `boya` | 1,479 | review: merge |
| `stress` | `estrés` | 1,539 | review: merge |
| `clicks` | `clic` | 1,590 | review: merge |
| `dermi` | `dermis` | 1,469 | review: merge |
| `nótese` | `notar` | 1,508 | review: merge |
| `cintar` | `cinto` | 1,271 | review: merge |
| `ve` | `ver` | 1,570 | review: merge |
| `adjetivar` | `adjetivo` | 1,396 | review: merge |
| `gadgets` | `gadget` | 1,340 | review: merge |
| `rastrillar` | `rastrillo` | 1,153 | review: merge |
| `asegurese` | `asegurarse` | 1,598 | review: merge |
| `catastrar` | `catastro` | 1,264 | review: merge |
| `riquísimo` | `rico` | 1,112 | review: merge |
| `wikis` | `wiki` | 1,517 | review: merge |
| `anímate` | `animarse` | 1,198 | review: merge |
| `cobaltar` | `cobalto` | 1,655 | review: merge |
| `accesar` | `acceder` | 1,440 | review: merge |
| `abastar` | `abasto` | 1,114 | review: merge |
| `apartmento` | `apartamento` | 1,175 | review: merge |
| `cambiá` | `cambiar` | 1,627 | review: merge |
| `enjambrar` | `enjambre` | 1,292 | review: merge |
| `hisopar` | `hisopo` | 1,458 | review: merge |
| `microfinanza` | `microfinanzas` | 1,164 | review: merge |
| `rendido` | `rendir` | 1,376 | review: merge |
| `últma` | `último` | 1,493 | review: merge |
| `blister` | `blíster` | 1,320 | review: merge |
| `desinstale` | `desinstalar` | 1,299 | review: merge |
| `laparoscópica` | `laparoscópico` | 1,509 | review: merge |
| `llámano` | `llamar` | 1,170 | review: merge |
| `primerísimo` | `primero` | 1,074 | review: merge |
| `páde` | `pádel` | 1,550 | review: merge |
| `snorkeling` | `esnórquel` | 1,404 | review: merge |
| `brumar` | `bruma` | 1,245 | review: merge |
| `chalar` | `chalé` | 1,275 | review: merge |
| `primarias` | `primario` | 1,536 | review: merge |
| `adolecente` | `adolescente` | 1,212 | review: merge |
| `basta` | `bastar` | 1,108 | review: merge |
| `envia` | `enviar` | 1,244 | review: merge |
| `podeis` | `poder` | 1,542 | review: merge |
| `sufijar` | `sufijo` | 1,301 | review: merge |
| `atalayar` | `atalaya` | 1,427 | review: merge |
| `hab` | `habitación` | 1,433 | review: merge |
| `majar` | `majo` | 1,044 | review: merge |
| `bellísimo` | `bello` | 1,176 | review: merge |
| `granar` | `grana` | 1,192 | review: merge |
| `sumérjase` | `sumergirse` | 1,396 | review: merge |
| `cilindrar` | `cilindrada` | 1,302 | review: merge |
| `defendido` | `defender` | 1,402 | review: merge |
| `malabar` | `malabares` | 1,188 | review: merge |
| `oprobiar` | `oprobio` | 1,403 | review: merge |
| `precintar` | `precinto` | 1,344 | review: merge |
| `suscríbete` | `suscribirse` | 1,203 | review: merge |
| `variz` | `várice` | 1,277 | review: merge |
| `atla` | `atlas` | 1,171 | review: merge |
| `dema` | `demás` | 1,172 | review: merge |
| `indultar` | `indulto` | 1,204 | review: merge |
| `preludiar` | `preludio` | 1,217 | review: merge |
| `remolinar` | `remolino` | 1,176 | review: merge |
| `sulfurar` | `sulfuro` | 1,384 | review: merge |
| `alfalfar` | `alfalfa` | 1,127 | review: merge |
| `ceniciento` | `cenicienta` | 1,129 | review: merge |
| `deshelar` | `deshielo` | 1,244 | review: merge |
| `huespede` | `huésped` | 1,220 | review: merge |
| `incluída` | `incluir` | 1,186 | review: merge |
| `reestablecer` | `restablecer` | 1,175 | review: merge |
| `suba` | `subir` | 1,015 | review: merge |
| `trajar` | `traje` | 818 | review: merge |
| `capotar` | `capota` | 1,171 | review: merge |
| `cómpralo` | `comprar` | 1,186 | review: merge |
| `entrepernar` | `entrepierna` | 1,314 | review: merge |
| `envió` | `enviar` | 1,330 | review: merge |
| `lofts` | `loft` | 1,232 | review: merge |
| `muertar` | `muerto` | 1,384 | review: merge |
| `piercings` | `piercing` | 1,247 | review: merge |
| `prediseñadas` | `prediseñado` | 1,282 | review: merge |
| `strass` | `estrás` | 1,340 | review: merge |
| `cavo` | `cava` | 1,323 | review: merge |
| `escaramuzar` | `escaramuza` | 951 | review: merge |
| `murmullar` | `murmullo` | 1,076 | review: merge |
| `remansar` | `remanso` | 1,251 | review: merge |
| `erar` | `ser` | 1,232 | review: merge |
| `garzo` | `garza` | 1,103 | review: merge |
| `lacrar` | `lacre` | 1,078 | review: merge |
| `platinar` | `platina` | 1,281 | review: merge |
| `trocar` | `trueque` | 1,179 | review: merge |
| `cizallar` | `cizalla` | 1,226 | review: merge |
| `guindar` | `guinda` | 1,139 | review: merge |
| `hojaldrar` | `hojaldre` | 1,276 | review: merge |
| `lavamano` | `lavamanos` | 1,221 | review: merge |
| `leída` | `leer` | 1,294 | review: merge |
| `mezclo` | `mezclar` | 1,342 | review: merge |
| `androgénica` | `androgénico` | 1,207 | review: merge |
| `apostillar` | `apostilla` | 882 | review: merge |
| `comprometiéndose` | `comprometerse` | 1,325 | review: merge |
| `dejá` | `dejar` | 497 | review: merge |
| `rededor` | `alrededor` | 1,228 | review: merge |
| `webmasters` | `webmaster` | 1,211 | review: merge |
| `bichar` | `bicho` | 730 | review: merge |
| `construída` | `construir` | 1,242 | review: merge |
| `modus` | `modus operandi` | 1,048 | review: merge |
| `palés` | `palé` | 1,187 | review: merge |
| `sneakers` | `sneaker` | 1,052 | review: merge |
| `stickers` | `sticker` | 1,415 | review: merge |
| `adéntrate` | `adentrarse` | 1,205 | review: merge |
| `gruesa` | `grueso` | 1,408 | review: merge |
| `royo` | `roya` | 1,092 | review: merge |
| `buzar` | `buzo` | 907 | review: merge |
| `folklórico` | `folclórico` | 1,196 | review: merge |
| `alójese` | `alojarse` | 1,025 | review: merge |
| `catamar` | `catamarán` | 1,280 | review: merge |
| `cetogénica` | `cetogénico` | 975 | review: merge |
| `desapegar` | `desapego` | 1,082 | review: merge |
| `mecanografiar` | `mecanografía` | 989 | review: merge |
| `outfits` | `outfit` | 1,083 | review: merge |
| `sabés` | `saber` | 394 | review: merge |
| `tertulio` | `tertulia` | 900 | review: merge |
| `carenar` | `carenado` | 1,172 | review: merge |
| `jacuzzis` | `jacuzzi` | 1,084 | review: merge |
| `peder` | `pedo` | 475 | review: merge |
| `antiinflamatorios` | `antiinflamatorio` | 1,122 | review: merge |
| `cubiertar` | `cubierta` | 1,079 | review: merge |
| `altercar` | `altercado` | 1,135 | review: merge |
| `plomer` | `plomería` | 1,091 | review: merge |
| `tarar` | `tara` | 1,066 | review: merge |
| `cerciórese` | `cerciorarse` | 1,112 | review: merge |
| `fui` | `ir` | 843 | review: merge |
| `llamadar` | `llamada` | 1,298 | review: merge |
| `medidar` | `medida` | 1,098 | review: merge |
| `pósters` | `póster` | 1,159 | review: merge |
| `repe` | `repeler` | 1,141 | review: merge |
| `salve` | `salvar` | 1,084 | review: merge |
| `bellísima` | `bello` | 1,121 | review: merge |
| `dejarlo` | `dejar` | 1,170 | review: merge |
| `firewalls` | `firewall` | 1,279 | review: merge |
| `logs` | `log` | 1,195 | review: merge |
| `prepagada` | `prepagado` | 978 | review: merge |
| `clicando` | `clicar` | 1,015 | review: merge |
| `cosquillar` | `cosquillas` | 798 | review: merge |
| `dismiuye` | `disminuir` | 871 | review: merge |
| `electrica` | `eléctrico` | 1,222 | review: merge |
| `encintar` | `encinta` | 1,103 | review: merge |
| `fúngicas` | `fúngico` | 941 | review: merge |
| `guárdelo` | `guardar` | 1,146 | review: merge |
| `solidar` | `sólido` | 1,121 | review: merge |
| `sáb` | `sábado` | 1,102 | review: merge |
| `bariátrica` | `bariátrico` | 1,008 | review: merge |
| `bor` | `borla` | 1,039 | review: merge |
| `jonrones` | `jonrón` | 1,080 | review: merge |
| `kármica` | `kármico` | 1,015 | review: merge |
| `leé` | `leer` | 1,021 | review: merge |
| `protegiéndolo` | `proteger` | 1,037 | review: merge |
| `volt` | `voltio` | 1,092 | review: merge |
| `carillo` | `carilla` | 1,039 | review: merge |
| `códecs` | `códec` | 1,021 | review: merge |
| `dese` | `dar` | 853 | review: merge |
| `disfrutá` | `disfrutar` | 1,056 | review: merge |
| `valiéndose` | `valerse` | 985 | review: merge |
| `mantenlo` | `mantener` | 936 | review: merge |
| `proporcionándole` | `proporcionar` | 1,055 | review: merge |
| `torrents` | `torrent` | 1,230 | review: merge |
| `trolls` | `troll` | 908 | review: merge |
| `arcoiris` | `arcoíris` | 804 | review: merge |
| `contrapuntar` | `contrapunto` | 1,119 | review: merge |
| `electricas` | `eléctrico` | 800 | review: merge |
| `reservá` | `reservar` | 1,062 | review: merge |
| `toquar` | `tocar` | 1,082 | review: merge |
| `webinars` | `webinar` | 866 | review: merge |
| `avezar` | `avezado` | 843 | review: merge |
| `carpir` | `carpa` | 889 | review: merge |
| `conecciones` | `conexión` | 1,181 | review: merge |
| `cotar` | `cota` | 899 | review: merge |
| `engranar` | `engrane` | 1,121 | review: merge |
| `mampar` | `mampara` | 837 | review: merge |
| `nuesto` | `nuestro` | 891 | review: merge |
| `purpurino` | `purpurina` | 888 | review: merge |
| `chances` | `chance` | 711 | review: merge |
| `metaboliza` | `metabolizar` | 811 | review: merge |
| `tapiar` | `tapia` | 679 | review: merge |
| `workshops` | `workshop` | 1,100 | review: merge |
| `compasar` | `compás` | 1,059 | review: merge |
| `eslingar` | `eslinga` | 714 | review: merge |
| `invasiva` | `invasivo` | 871 | review: merge |
| `cierne` | `cernerse` | 713 | review: merge |
| `discrección` | `discreción` | 751 | review: merge |
| `físicar` | `física` | 957 | review: merge |
| `hacedlo` | `hacer` | 825 | review: merge |
| `lucho` | `lucha` | 1,007 | review: merge |
| `márketing` | `marketing` | 1,094 | review: merge |
| `videocámar` | `videocámara` | 853 | review: merge |
| `antibacteriana` | `antibacteriano` | 1,015 | review: merge |
| `antiinflamatoria` | `antiinflamatorio` | 986 | review: merge |
| `cristaler` | `cristalería` | 952 | review: merge |
| `cucar` | `cuco` | 806 | review: merge |
| `desmesurar` | `desmesurado` | 929 | review: merge |
| `feminizada` | `feminizado` | 1,021 | review: merge |
| `hippy` | `hippie` | 1,089 | review: merge |
| `oid` | `oír` | 933 | review: merge |
| `caminito` | `camino` | 829 | review: merge |
| `estomagar` | `estómago` | 899 | review: merge |
| `família` | `familia` | 1,029 | review: merge |
| `fuir` | `ir` | 596 | review: merge |
| `minibus` | `minibús` | 891 | review: merge |
| `pizzer` | `pizzería` | 957 | review: merge |
| `encontrá` | `encontrar` | 790 | review: merge |
| `ghetto` | `gueto` | 975 | review: merge |
| `hazle` | `hacer` | 846 | review: merge |
| `importantísima` | `importante` | 693 | review: merge |
| `monitoree` | `monitorear` | 882 | review: merge |
| `muera` | `morir` | 555 | review: merge |
| `vente` | `venirse` | 693 | review: merge |
| `aproximamente` | `aproximadamente` | 835 | review: merge |
| `litografiar` | `litografía` | 1,112 | review: merge |
| `posteado` | `postear` | 885 | review: merge |
| `secuestrado` | `secuestrar` | 964 | review: merge |
| `abordo` | `a bordo` | 963 | review: merge |
| `acaudalar` | `acaudalado` | 937 | review: merge |
| `contenian` | `contener` | 901 | review: merge |
| `descripto` | `describir` | 928 | review: merge |
| `grillar` | `grilla` | 940 | review: merge |
| `hacerlo` | `hacer` | 676 | review: merge |
| `illustración` | `ilustración` | 939 | review: merge |
| `obten` | `obtener` | 846 | review: merge |
| `porfavor` | `por favor` | 720 | review: merge |
| `baldar` | `balda` | 969 | review: merge |
| `contraído` | `contraer` | 841 | review: merge |
| `contínua` | `continuo` | 862 | review: merge |
| `ingresá` | `ingresar` | 862 | review: merge |
| `macar` | `maca` | 993 | review: merge |
| `acérquese` | `acercarse` | 639 | review: merge |
| `gavillar` | `gavilla` | 807 | review: merge |
| `hipertrofiar` | `hipertrofia` | 1,003 | review: merge |
| `acidar` | `ácido` | 914 | review: merge |
| `aleatorizados` | `aleatorizar` | 835 | review: merge |
| `carbonar` | `carbón` | 944 | review: merge |
| `compártalo` | `compartir` | 611 | review: merge |
| `corresponderle` | `corresponder` | 761 | review: merge |
| `dejadme` | `dejar` | 496 | review: merge |
| `harmonía` | `armonía` | 543 | review: merge |
| `antibacterianas` | `antibacteriano` | 667 | review: merge |
| `antiinflamatorias` | `antiinflamatorio` | 913 | review: merge |
| `contrapar` | `contraparte` | 851 | review: merge |
| `dadme` | `dar` | 523 | review: merge |
| `danados` | `dañar` | 854 | review: merge |
| `desconéctate` | `desconectarse` | 909 | review: merge |
| `nausear` | `náusea` | 817 | review: merge |
| `percutánea` | `percutáneo` | 732 | review: merge |
| `sociodemográficas` | `sociodemográfico` | 778 | review: merge |
| `sálvame` | `salvar` | 750 | review: merge |
| `tardo` | `tardar` | 578 | review: merge |
| `autocaravanas` | `autocaravana` | 755 | review: merge |
| `créanme` | `creer` | 723 | review: merge |
| `estilismos` | `estilismo` | 764 | review: merge |
| `hosteler` | `hostelería` | 958 | review: merge |
| `hubs` | `hub` | 724 | review: merge |
| `izq` | `izquierda` | 890 | review: merge |
| `manténgalo` | `mantener` | 749 | review: merge |
| `masajea` | `masajear` | 867 | review: merge |
| `restructuración` | `reestructuración` | 631 | review: merge |
| `retenida` | `retener` | 661 | review: merge |
| `seleccioná` | `seleccionar` | 782 | review: merge |
| `déle` | `dar` | 745 | review: merge |
| `diviértase` | `divertirse` | 724 | review: merge |
| `entérese` | `enterarse` | 855 | review: merge |
| `envíelo` | `enviar` | 819 | review: merge |
| `informaciónes` | `información` | 748 | review: merge |
| `tvs` | `tv` | 634 | review: merge |
| `panorámicar` | `panorámica` | 816 | review: merge |
| `routers` | `router` | 607 | review: merge |
| `acogido` | `acoger` | 846 | review: merge |
| `innings` | `inning` | 633 | review: merge |
| `izquierdar` | `izquierda` | 1,015 | review: merge |
| `posmenopáusicas` | `posmenopáusico` | 659 | review: merge |
| `reinterpreta` | `reinterpretar` | 615 | review: merge |
| `vd` | `usted` | 706 | review: merge |
| `almenar` | `almena` | 724 | review: merge |
| `amplísima` | `amplio` | 849 | review: merge |
| `esplender` | `espléndido` | 751 | review: merge |
| `lagrimar` | `lágrima` | 796 | review: merge |
| `perfumer` | `perfumería` | 623 | review: merge |
| `reuniéndose` | `reunirse` | 682 | review: merge |
| `rocio` | `rocío` | 669 | review: merge |
| `ultralenta` | `ultralento` | 583 | review: merge |
| `absortar` | `absorto` | 559 | review: merge |
| `bienvenidar` | `bienvenido` | 654 | review: merge |
| `catálago` | `catálogo` | 725 | review: merge |
| `excrementar` | `excremento` | 762 | review: merge |
| `muffins` | `muffin` | 785 | review: merge |
| `novelar` | `novel` | 675 | review: merge |
| `posters` | `póster` | 712 | review: merge |
| `seleccciones` | `selección` | 617 | review: merge |
| `titulo` | `título` | 820 | review: merge |
| `altísimos` | `alto` | 732 | review: merge |
| `bungalós` | `bungaló` | 678 | review: merge |
| `concéntrese` | `concentrarse` | 718 | review: merge |
| `dpto` | `departamento` | 720 | review: merge |
| `empodera` | `empoderar` | 724 | review: merge |
| `esperándote` | `esperar` | 445 | review: merge |
| `figuro` | `figura` | 702 | review: merge |
| `véanse` | `ver` | 810 | review: merge |
| `whiskey` | `whisky` | 754 | review: merge |
| `yihadistas` | `yihadista` | 704 | review: merge |
| `colaborativa` | `colaborativo` | 655 | review: merge |
| `entendiéndose` | `entender` | 756 | review: merge |
| `gatita` | `gato` | 433 | review: merge |
| `hachar` | `hacha` | 570 | review: merge |
| `hipoalergénica` | `hipoalergénico` | 598 | review: merge |
| `imagínense` | `imaginarse` | 716 | review: merge |
| `recámar` | `recámara` | 715 | review: merge |
| `teni` | `tener` | 630 | review: merge |
| `arencar` | `arenque` | 632 | review: merge |
| `desarollo` | `desarrollo` | 745 | review: merge |
| `estilosa` | `estiloso` | 610 | review: merge |
| `flexográfica` | `flexográfico` | 643 | review: merge |
| `ictu` | `ictus` | 737 | review: merge |
| `kármicas` | `kármico` | 617 | review: merge |
| `monitorea` | `monitorear` | 731 | review: merge |
| `musicar` | `músico` | 734 | review: merge |
| `perfiladora` | `perfilador` | 468 | review: merge |
| `regulatoria` | `regulatorio` | 731 | review: merge |
| `usario` | `usuario` | 801 | review: merge |
| `apártate` | `apartarse` | 680 | review: merge |
| `armadar` | `armada` | 723 | review: merge |
| `bollar` | `bollo` | 533 | review: merge |
| `cnel` | `coronel` | 589 | review: merge |
| `dura` | `duro` | 661 | review: merge |
| `díselo` | `decir` | 361 | review: merge |
| `embárcate` | `embarcarse` | 726 | review: merge |
| `ferrar` | `fierro` | 585 | review: merge |
| `pequeñita` | `pequeñito` | 725 | review: merge |
| `pormás` | `por más` | 567 | review: merge |
| `péguelo` | `pegar` | 626 | review: merge |
| `reinicie` | `reiniciar` | 822 | review: merge |
| `tarífas` | `tarifa` | 712 | review: merge |
| `agradécele` | `agradecer` | 450 | review: merge |
| `alhajar` | `alhaja` | 609 | review: merge |
| `computarizadas` | `computarizado` | 630 | review: merge |
| `dinos` | `decir` | 578 | review: merge |
| `mismísima` | `mismo` | 592 | review: merge |
| `notebooks` | `notebook` | 661 | review: merge |
| `pelis` | `peli` | 578 | review: merge |
| `projecto` | `proyecto` | 644 | review: merge |
| `surfea` | `surfear` | 601 | review: merge |
| `adecue` | `adecuar` | 517 | review: merge |
| `commentario` | `comentario` | 687 | review: merge |
| `deléitese` | `deleitarse` | 645 | review: merge |
| `formadora` | `formador` | 783 | review: merge |
| `playlists` | `playlist` | 501 | review: merge |
| `psicoactivas` | `psicoactivo` | 574 | review: merge |
| `translado` | `traslado` | 521 | review: merge |
| `através` | `a través` | 804 | review: merge |
| `enlistado` | `enlistar` | 551 | review: merge |
| `feminizadas` | `feminizado` | 898 | review: merge |
| `glamurosa` | `glamuroso` | 476 | review: merge |
| `hno` | `hermano` | 523 | review: merge |
| `levántese` | `levantarse` | 543 | review: merge |
| `mostrándote` | `mostrar` | 604 | review: merge |
| `softball` | `sóftbol` | 517 | review: merge |
| `solito` | `solo` | 401 | review: merge |
| `sálvate` | `salvarse` | 563 | review: merge |
| `acuéstate` | `acostarse` | 626 | review: merge |
| `cocino` | `cocina` | 753 | review: merge |
| `dales` | `dar` | 567 | review: merge |
| `deslízate` | `deslizarse` | 658 | review: merge |
| `endechar` | `endecha` | 562 | review: merge |
| `hechor` | `hecho` | 549 | review: merge |
| `hiperenlaces` | `hiperenlace` | 655 | review: merge |
| `multifacética` | `multifacético` | 612 | review: merge |
| `poquísimo` | `poco` | 462 | review: merge |
| `postrer` | `postrero` | 466 | review: merge |
| `redirecciona` | `redireccionar` | 512 | review: merge |
| `semipreciosas` | `semiprecioso` | 636 | review: merge |
| `sintiéndote` | `sentirse` | 443 | review: merge |
| `smatphone` | `smartphone` | 803 | review: merge |
| `tenida` | `tener` | 537 | review: merge |
| `texturizada` | `texturizado` | 621 | review: merge |
| `todxs` | `todo` | 506 | review: merge |
| `arrástrelo` | `arrastrar` | 532 | review: merge |
| `añádelo` | `añadir` | 542 | review: merge |
| `bromar` | `bromo` | 552 | review: merge |
| `caricaturar` | `caricatura` | 691 | review: merge |
| `dadle` | `dar` | 474 | review: merge |
| `disenado` | `diseñar` | 617 | review: merge |
| `finar` | `finado` | 687 | review: merge |
| `funcionabilidad` | `funcionalidad` | 593 | review: merge |
| `fín` | `fin` | 656 | review: merge |
| `muchísimos` | `mucho` | 469 | review: merge |
| `pensás` | `pensar` | 147 | review: merge |
| `pequena` | `pequeño` | 738 | review: merge |
| `purísima` | `purísimo` | 667 | review: merge |
| `abiertas` | `abierto` | 518 | review: merge |
| `comisariada` | `comisariar` | 574 | review: merge |
| `conocés` | `conocer` | 106 | review: merge |
| `despúes` | `después` | 475 | review: merge |
| `enséñame` | `enseñar` | 418 | review: merge |
| `espíritas` | `espírita` | 640 | review: merge |
| `experiéncia` | `experiencia` | 514 | review: merge |
| `incluídas` | `incluir` | 621 | review: merge |
| `pallets` | `palé` | 654 | review: merge |
| `pruébalo` | `probar` | 533 | review: merge |
| `actualizá` | `actualizar` | 395 | review: merge |
| `bagels` | `bagel` | 429 | review: merge |
| `cliquee` | `cliquear` | 683 | review: merge |
| `cúal` | `cuál` | 449 | review: merge |
| `haciéndolo` | `hacer` | 630 | review: merge |
| `prensadora` | `prensador` | 615 | review: merge |
| `sunnah` | `sunna` | 667 | review: merge |
| `bautizándolo` | `bautizar` | 517 | review: merge |
| `botulínica` | `botulínico` | 575 | review: merge |
| `cardigan` | `cárdigan` | 659 | review: merge |
| `deléitate` | `deleitarse` | 526 | review: merge |
| `extesión` | `extensión` | 692 | review: merge |
| `ponis` | `poni` | 752 | review: merge |
| `reinicia` | `reiniciar` | 639 | review: merge |
| `responsar` | `responso` | 605 | review: merge |
| `sarmentar` | `sarmiento` | 410 | review: merge |
| `vidéo` | `vídeo` | 579 | review: merge |
| `accesso` | `acceso` | 497 | review: merge |
| `amenudo` | `a menudo` | 526 | review: merge |
| `analíticar` | `analítica` | 499 | review: merge |
| `andá` | `andar` | 122 | review: merge |
| `asintomática` | `asintomático` | 603 | review: merge |
| `avda` | `avenida` | 501 | review: merge |
| `bellísimas` | `bello` | 456 | review: merge |
| `deshazte` | `deshacerse` | 545 | review: merge |
| `equipamento` | `equipamiento` | 742 | review: merge |
| `glamouroso` | `glamuroso` | 438 | review: merge |
| `guapísima` | `guapo` | 517 | review: merge |
| `maltear` | `malteada` | 659 | review: merge |
| `modulo` | `módulo` | 607 | review: merge |
| `preoperatoria` | `preoperatorio` | 533 | review: merge |
| `promos` | `promo` | 527 | review: merge |
| `regálate` | `regalar` | 488 | review: merge |
| `vencida` | `vencer` | 560 | review: merge |
| `acordás` | `acordar` | 508 | review: merge |
| `decidme` | `decir` | 328 | review: merge |
| `districto` | `distrito` | 352 | review: merge |
| `estrogénica` | `estrogénico` | 470 | review: merge |
| `glamorosa` | `glamuroso` | 533 | review: merge |
| `iro` | `irse` | 355 | review: merge |
| `jihad` | `yihad` | 540 | review: merge |
| `lechar` | `lechada` | 542 | review: merge |
| `porfolio` | `portafolio` | 661 | review: merge |
| `volúmen` | `volumen` | 491 | review: merge |
| `ópticar` | `óptica` | 494 | review: merge |
| `añadiéndole` | `añadir` | 524 | review: merge |
| `basándome` | `basarse` | 424 | review: merge |
| `bulldozer` | `buldócer` | 566 | review: merge |
| `comentatios` | `comentario` | 512 | review: merge |
| `dur` | `durar` | 493 | review: merge |
| `envíenme` | `enviar` | 620 | review: merge |
| `guardarlo` | `guardar` | 553 | review: merge |
| `indisciplinar` | `indisciplinado` | 493 | review: merge |
| `insolentar` | `insolente` | 366 | review: merge |
| `milimétrica` | `milimétrico` | 416 | review: merge |
| `panty` | `panti` | 630 | review: merge |
| `pasados` | `pasado` | 591 | review: merge |
| `plante` | `plantar` | 472 | review: merge |
| `reproductora` | `reproductor` | 527 | review: merge |
| `abróchate` | `abrocharse` | 365 | review: merge |
| `ammonita` | `amonita` | 474 | review: merge |
| `centellar` | `centella` | 488 | review: merge |
| `grandísima` | `grande` | 677 | review: merge |
| `introdúzca` | `introducir` | 558 | review: merge |
| `mancornar` | `mancuerna` | 444 | review: merge |
| `oponiéndose` | `oponerse` | 622 | review: merge |
| `ranciar` | `rancio` | 426 | review: merge |
| `sintiéndome` | `sentirse` | 590 | review: merge |
| `videollamadas` | `videollamada` | 604 | review: merge |
| `virtualizados` | `virtualizar` | 512 | review: merge |
| `acordao` | `acordarse` | 320 | review: merge |
| `afrutados` | `afrutado` | 610 | review: merge |
| `basándote` | `basarse` | 578 | review: merge |
| `bésame` | `besar` | 339 | review: merge |
| `enséñale` | `enseñar` | 352 | review: merge |
| `intersex` | `intersexual` | 454 | review: merge |
| `introducí` | `introducir` | 384 | review: merge |
| `absténgase` | `abstenerse` | 480 | review: merge |
| `agárrate` | `agarrarse` | 242 | review: merge |
| `amplísimo` | `amplio` | 485 | review: merge |
| `avísenme` | `avisar` | 438 | review: merge |
| `añádele` | `añadir` | 405 | review: merge |
| `bájate` | `bajarse` | 385 | review: merge |
| `conocé` | `conocer` | 496 | review: merge |
| `creedme` | `creer` | 352 | review: merge |
| `esfuérzate` | `esforzarse` | 527 | review: merge |
| `gais` | `gay` | 641 | review: merge |
| `paprika` | `páprika` | 457 | review: merge |
| `preinstaladas` | `preinstalado` | 459 | review: merge |
| `prepárense` | `prepararse` | 490 | review: merge |
| `rappel` | `rápel` | 523 | review: merge |
| `sustituta` | `sustituto` | 526 | review: merge |
| `termográfica` | `termográfico` | 426 | review: merge |
| `tiar` | `tiara` | 602 | review: merge |
| `ajustir` | `ajuste` | 418 | review: merge |
| `caballer` | `caballería` | 498 | review: merge |
| `dad` | `dar` | 447 | review: merge |
| `despacito` | `despacio` | 386 | review: merge |
| `fíjense` | `fijarse` | 491 | review: merge |
| `hacés` | `hacer` | 205 | review: merge |
| `infrastructura` | `infraestructura` | 334 | review: merge |
| `precancerosas` | `precanceroso` | 359 | review: merge |
| `quintaesenciar` | `quintaesencia` | 456 | review: merge |
| `sinó` | `sino` | 330 | review: merge |
| `vávula` | `válvula` | 546 | review: merge |
| `amadísimos` | `amado` | 402 | review: merge |
| `cuídense` | `cuidarse` | 329 | review: merge |
| `decidle` | `decir` | 432 | review: merge |
| `facilísimo` | `fácil` | 393 | review: merge |
| `flore` | `flor` | 472 | review: merge |
| `fúngica` | `fúngico` | 545 | review: merge |
| `hiperbárica` | `hiperbárico` | 421 | review: merge |
| `huída` | `huida` | 400 | review: merge |
| `manténganse` | `mantenerse` | 423 | review: merge |
| `mesía` | `mesías` | 419 | review: merge |
| `muellir` | `muelle` | 496 | review: merge |
| `octavar` | `octava` | 447 | review: merge |
| `plomar` | `plomada` | 441 | review: merge |
| `pregrabada` | `pregrabado` | 437 | review: merge |
| `sueñar` | `sueño` | 325 | review: merge |
| `cliquea` | `cliquear` | 461 | review: merge |
| `debés` | `deber` | 227 | review: merge |
| `eligir` | `elegir` | 461 | review: merge |
| `espontanear` | `espontáneo` | 530 | review: merge |
| `familiarícese` | `familiarizarse` | 495 | review: merge |
| `húerfano` | `huérfano` | 511 | review: merge |
| `nosotrxs` | `nosotros` | 465 | review: merge |
| `permitidme` | `permitir` | 331 | review: merge |
| `remítase` | `remitirse` | 354 | review: merge |
| `windsurfing` | `windsurf` | 320 | review: merge |
| `úsala` | `usar` | 552 | review: merge |
| `anonimizada` | `anonimizar` | 368 | review: merge |
| `aprovéchese` | `aprovecharse` | 492 | review: merge |
| `artesonar` | `artesonado` | 473 | review: merge |
| `asintomáticas` | `asintomático` | 338 | review: merge |
| `aymar` | `aymara` | 364 | review: merge |
| `ayurvédica` | `ayurvédico` | 492 | review: merge |
| `cerciórate` | `cerciorarse` | 363 | review: merge |
| `daos` | `darse` | 346 | review: merge |
| `descaregar` | `descargar` | 415 | review: merge |
| `ferrys` | `ferri` | 418 | review: merge |
| `fresquita` | `fresquito` | 304 | review: merge |
| `masajee` | `masajear` | 488 | review: merge |
| `millenials` | `milenial` | 328 | review: merge |
| `miocárdica` | `miocárdico` | 534 | review: merge |
| `netbooks` | `netbook` | 449 | review: merge |
| `prononciación` | `pronunciación` | 364 | review: merge |
| `recuéstate` | `recostarse` | 251 | review: merge |
| `salvífica` | `salvífico` | 456 | review: merge |
| `semiáridas` | `semiárido` | 326 | review: merge |
| `valido` | `valer` | 403 | review: merge |
| `ahorrá` | `ahorrar` | 618 | review: merge |
| `asegúrense` | `asegurarse` | 462 | review: merge |
| `clausular` | `cláusula` | 454 | review: merge |
| `computarizados` | `computarizado` | 372 | review: merge |
| `correción` | `corrección` | 477 | review: merge |
| `cristiana` | `cristiano` | 479 | review: merge |
| `decile` | `decir` | 68 | review: merge |
| `dejándola` | `dejar` | 445 | review: merge |
| `escollar` | `escollo` | 374 | review: merge |
| `mantenla` | `mantener` | 360 | review: merge |
| `metabolizan` | `metabolizar` | 429 | review: merge |
| `niéguese` | `negarse` | 400 | review: merge |
| `numerológicas` | `numerológico` | 609 | review: merge |
| `obro` | `obra` | 411 | review: merge |
| `pirater` | `piratería` | 482 | review: merge |
| `prepagadas` | `prepagado` | 540 | review: merge |
| `prémium` | `premium` | 496 | review: merge |
| `quijar` | `quijada` | 349 | review: merge |
| `remítale` | `remitir` | 478 | review: merge |
| `savoir` | `savoir faire` | 275 | review: merge |
| `sujección` | `sujeción` | 329 | review: merge |
| `sáltese` | `saltarse` | 373 | review: merge |
| `són` | `ser` | 342 | review: merge |
| `alegraos` | `alegrarse` | 393 | review: merge |
| `bruzar` | `bruces` | 308 | review: merge |
| `colocándola` | `colocar` | 413 | review: merge |
| `conectándote` | `conectarse` | 481 | review: merge |
| `crayones` | `crayón` | 445 | review: merge |
| `crio` | `criar` | 352 | review: merge |
| `cómprate` | `comprarse` | 285 | review: merge |
| `decimotercer` | `decimotercero` | 371 | review: merge |
| `depués` | `después` | 324 | review: merge |
| `destruído` | `destruir` | 391 | review: merge |
| `determinadar` | `determinado` | 436 | review: merge |
| `dáselo` | `dar` | 265 | review: merge |
| `energizado` | `energizar` | 404 | review: merge |
| `estereotáctica` | `estereotáctico` | 372 | review: merge |
| `extraña` | `extraño` | 386 | review: merge |
| `llamadme` | `llamar` | 267 | review: merge |
| `miente` | `mentir` | 263 | review: merge |
| `poned` | `poner` | 465 | review: merge |
| `preconfigurados` | `preconfigurado` | 421 | review: merge |
| `traillar` | `traílla` | 429 | review: merge |
| `transformándola` | `transformar` | 246 | review: merge |
| `balinesas` | `balinés` | 334 | review: merge |
| `contracto` | `contrato` | 430 | review: merge |
| `coriónica` | `coriónico` | 461 | review: merge |
| `céntrese` | `centrarse` | 343 | review: merge |
| `diclofenac` | `diclofenaco` | 437 | review: merge |
| `dto` | `descuento` | 369 | review: merge |
| `envíar` | `enviar` | 307 | review: merge |
| `identitaria` | `identitario` | 336 | review: merge |
| `inmersivas` | `inmersivo` | 469 | review: merge |
| `mobilidad` | `movilidad` | 345 | review: merge |
| `museística` | `museístico` | 353 | review: merge |
| `operarador` | `operador` | 328 | review: merge |
| `proveído` | `proveer` | 438 | review: merge |
| `sheik` | `jeque` | 393 | review: merge |
| `siguente` | `siguiente` | 401 | review: merge |
| `snowboarding` | `snowboard` | 304 | review: merge |
| `súmate` | `sumarse` | 388 | review: merge |
| `telclado` | `teclado` | 250 | review: merge |
| `aléjese` | `alejarse` | 397 | review: merge |
| `carísimos` | `caro` | 210 | review: merge |
| `ceno` | `cenar` | 261 | review: merge |
| `chillout` | `chill-out` | 349 | review: merge |
| `cúbrase` | `cubrirse` | 286 | review: merge |
| `encuntre` | `encontrar` | 365 | review: merge |
| `enjuáguese` | `enjuagarse` | 307 | review: merge |
| `enséñele` | `enseñar` | 454 | review: merge |
| `entreabierta` | `entreabierto` | 211 | review: merge |
| `entreguerra` | `entreguerras` | 267 | review: merge |
| `escuchadme` | `escuchar` | 263 | review: merge |
| `habito` | `hábito` | 297 | review: merge |
| `inclínate` | `inclinarse` | 359 | review: merge |
| `indicá` | `indicar` | 260 | review: merge |
| `informándole` | `informar` | 351 | review: merge |
| `inmunohistoquímica` | `inmunohistoquímico` | 343 | review: merge |
| `michoacana` | `michoacano` | 218 | review: merge |
| `musculoesqueléticas` | `musculoesquelético` | 430 | review: merge |
| `notifíquenme` | `notificar` | 431 | review: merge |
| `paulownia` | `paulonia` | 372 | review: merge |
| `pequeñísima` | `pequeño` | 337 | review: merge |
| `podium` | `podio` | 417 | review: merge |
| `psoriásica` | `psoriásico` | 454 | review: merge |
| `rapidísimo` | `rápido` | 329 | review: merge |
| `regocijaos` | `regocijarse` | 379 | review: merge |
| `remasterizada` | `remasterizar` | 287 | review: merge |
| `termográficas` | `termográfico` | 387 | review: merge |
| `tíralo` | `tirar` | 194 | review: merge |
| `abrázame` | `abrazar` | 210 | review: merge |
| `baluar` | `baluarte` | 454 | review: merge |
| `bioregión` | `biorregión` | 379 | review: merge |
| `compañerxs` | `compañero` | 275 | review: merge |
| `dale` | `dar` | 255 | review: merge |
| `diaconar` | `diaconado` | 418 | review: merge |
| `fontaner` | `fontanería` | 459 | review: merge |
| `fíjese` | `fijarse` | 433 | review: merge |
| `grabados` | `grabado` | 312 | review: merge |
| `habitaciónes` | `habitación` | 430 | review: merge |
| `hematoencefálica` | `hematoencefálico` | 352 | review: merge |
| `hydráulica` | `hidráulico` | 271 | review: merge |
| `ibíd` | `ibídem` | 454 | review: merge |
| `instálelo` | `instalar` | 352 | review: merge |
| `levántense` | `levantarse` | 253 | review: merge |
| `muchisimos` | `muchísimo` | 288 | review: merge |
| `mutatis` | `mutatis mutandis` | 347 | review: merge |
| `objectivo` | `objetivo` | 486 | review: merge |
| `prediseñados` | `prediseñado` | 309 | review: merge |
| `protegerla` | `proteger` | 418 | review: merge |
| `remixes` | `remix` | 386 | review: merge |
| `retroiluminada` | `retroiluminado` | 571 | review: merge |
| `superalimentar` | `superalimento` | 286 | review: merge |
| `tediar` | `tedio` | 278 | review: merge |
| `abducido` | `abducir` | 243 | review: merge |
| `acompáñenos` | `acompañar` | 282 | review: merge |
| `acordaos` | `acordarse` | 395 | review: merge |
| `acuícolas` | `acuícola` | 335 | review: merge |
| `anonimizados` | `anonimizar` | 346 | review: merge |
| `ayduar` | `ayudar` | 296 | review: merge |
| `bacar` | `bacará` | 397 | review: merge |
| `cannábica` | `cannábico` | 349 | review: merge |
| `celiaca` | `celíaco` | 353 | review: merge |
| `compruébelo` | `comprobar` | 349 | review: merge |
| `conserjer` | `conserjería` | 422 | review: merge |
| `contínuamente` | `continuamente` | 276 | review: merge |
| `durísimo` | `duro` | 221 | review: merge |
| `enjuágate` | `enjuagarse` | 371 | review: merge |
| `esper` | `esperar` | 191 | review: merge |
| `exelente` | `excelente` | 390 | review: merge |
| `kilometrar` | `kilómetro` | 353 | review: merge |
| `logueado` | `loguearse` | 341 | review: merge |
| `metalmecánica` | `metalmecánico` | 291 | review: merge |
| `nitrurar` | `nitruro` | 340 | review: merge |
| `objecto` | `objeto` | 357 | review: merge |
| `prevee` | `prever` | 282 | review: merge |
| `redar` | `red` | 363 | review: merge |
| `restraso` | `retraso` | 408 | review: merge |
| `semiestructuradas` | `semiestructurado` | 380 | review: merge |
| `suéltalo` | `soltar` | 278 | review: merge |
| `travez` | `través` | 318 | review: merge |
| `trizar` | `triza` | 329 | review: merge |
| `walkie` | `walkie-talkie` | 411 | review: merge |
| `yodurar` | `yoduro` | 323 | review: merge |
| `úsalo` | `usar` | 409 | review: merge |
| `alelar` | `alelo` | 462 | review: merge |
| `antiquísima` | `antiguo` | 334 | review: merge |
| `bellísimos` | `bello` | 227 | review: merge |
| `bioclimática` | `bioclimático` | 338 | review: merge |
| `brindándole` | `brindar` | 417 | review: merge |
| `compuestar` | `compuesto` | 324 | review: merge |
| `construído` | `construido` | 367 | review: merge |
| `cuídese` | `cuidarse` | 222 | review: merge |
| `descripta` | `describir` | 341 | review: merge |
| `destruída` | `destruido` | 217 | review: merge |
| `documentario` | `documental` | 298 | review: merge |
| `déjala` | `dejar` | 352 | review: merge |
| `dése` | `darse` | 296 | review: merge |
| `energizada` | `energizar` | 226 | review: merge |
| `estambrar` | `estambre` | 318 | review: merge |
| `interesantísimo` | `interesante` | 255 | review: merge |
| `invasivas` | `invasivo` | 383 | review: merge |
| `marketplaces` | `marketplace` | 328 | review: merge |
| `misionario` | `misionero` | 315 | review: merge |
| `morenita` | `moreno` | 251 | review: merge |
| `multiplicaos` | `multiplicarse` | 321 | review: merge |
| `nuevos` | `nuevo` | 295 | review: merge |
| `obsérvese` | `observar` | 410 | review: merge |
| `preconfiguradas` | `preconfigurado` | 312 | review: merge |
| `pónte` | `ponerse` | 369 | review: merge |
| `redirija` | `redirigir` | 345 | review: merge |
| `reintroduzca` | `reintroducir` | 292 | review: merge |
| `sobrescribe` | `sobrescribir` | 390 | review: merge |
| `sumergiéndose` | `sumergirse` | 269 | review: merge |
| `alfarer` | `alfarería` | 294 | review: merge |
| `alguién` | `alguien` | 283 | review: merge |
| `almazar` | `almazara` | 306 | review: merge |
| `añádela` | `añadir` | 261 | review: merge |
| `bautícese` | `bautizar` | 341 | review: merge |
| `biofarmacéutica` | `biofarmacéutico` | 386 | review: merge |
| `centrándose` | `centrarse` | 369 | review: merge |
| `comodísima` | `cómodo` | 331 | review: merge |
| `comprá` | `comprar` | 158 | review: merge |
| `constituyéndose` | `constituirse` | 362 | review: merge |
| `deshágase` | `deshacerse` | 376 | review: merge |
| `divertidísimo` | `divertido` | 344 | review: merge |
| `eliminarlo` | `eliminar` | 385 | review: merge |
| `esforzaos` | `esforzarse` | 332 | review: merge |
| `inspírese` | `inspirarse` | 270 | review: merge |
| `keratina` | `queratina` | 395 | review: merge |
| `larguísimo` | `largo` | 251 | review: merge |
| `madurita` | `maduro` | 394 | review: merge |
| `muestreados` | `muestrear` | 264 | review: merge |
| `noviolenta` | `noviolento` | 281 | review: merge |
| `permitirle` | `permitir` | 460 | review: merge |
| `proprietario` | `propietario` | 379 | review: merge |
| `redirigiendo` | `redirigir` | 310 | review: merge |
| `seminueva` | `seminuevo` | 296 | review: merge |
| `showrooms` | `showroom` | 331 | review: merge |
| `sálvano` | `salvar` | 314 | review: merge |
| `sándwiches` | `sándwich` | 345 | review: merge |
| `tambíen` | `también` | 405 | review: merge |
| `trabajadorxs` | `trabajador` | 356 | review: merge |
| `traedme` | `traer` | 216 | review: merge |
| `triage` | `triaje` | 190 | review: merge |
| `ultraperiféricas` | `ultraperiférico` | 301 | review: merge |
| `vestío` | `vestirse` | 260 | review: merge |
| `virtualizadas` | `virtualizar` | 320 | review: merge |
| `accessorio` | `accesorio` | 333 | review: merge |
| `acuérdese` | `acordarse` | 253 | review: merge |
| `acérquense` | `acercarse` | 252 | review: merge |
| `adio` | `adiós` | 351 | review: merge |
| `aerotransportada` | `aerotransportado` | 227 | review: merge |
| `antinflamatorio` | `antiinflamatorio` | 339 | review: merge |
| `aplícalo` | `aplicar` | 263 | review: merge |
| `arrástralo` | `arrastrar` | 435 | review: merge |
| `asegurándote` | `asegurarse` | 249 | review: merge |
| `años` | `año` | 254 | review: merge |
| `balinesa` | `balinés` | 370 | review: merge |
| `bitcóin` | `bitcoin` | 354 | review: merge |
| `colocándolo` | `colocar` | 321 | review: merge |
| `cómprame` | `comprar` | 77 | review: merge |
| `debatar` | `debate` | 348 | review: merge |
| `dinamica` | `dinámica` | 311 | review: merge |
| `felíz` | `feliz` | 282 | review: merge |
| `finísima` | `fino` | 279 | review: merge |
| `hablás` | `hablar` | 53 | review: merge |
| `hemodinámica` | `hemodinámico` | 336 | review: merge |
| `imaginer` | `imaginería` | 273 | review: merge |
| `infanter` | `infantería` | 348 | review: merge |
| `insurreccionar` | `insurrección` | 324 | review: merge |
| `maritimas` | `marítimo` | 366 | review: merge |
| `meningocócica` | `meningocócico` | 324 | review: merge |
| `mielógena` | `mielógeno` | 289 | review: merge |
| `nasogástrica` | `nasogástrico` | 207 | review: merge |
| `naútico` | `náutico` | 268 | review: merge |
| `nuesta` | `nuestro` | 226 | review: merge |
| `oídme` | `oír` | 364 | review: merge |
| `panoramicas` | `panorámico` | 292 | review: merge |
| `particionado` | `particionar` | 353 | review: merge |
| `políticar` | `política` | 278 | review: merge |
| `pontar` | `ponerse` | 275 | review: merge |
| `recatar` | `recato` | 371 | review: merge |
| `repito` | `repetir` | 354 | review: merge |
| `samuráis` | `samurái` | 274 | review: merge |
| `shoppings` | `shopping` | 236 | review: merge |
| `sobrasar` | `sobrasada` | 241 | review: merge |
| `sometiéndose` | `someterse` | 342 | review: merge |
| `tomá` | `tomar` | 131 | review: merge |
| `ámense` | `amar` | 186 | review: merge |
| `éso` | `eso` | 336 | review: merge |
| `adecuen` | `adecuar` | 314 | review: merge |
| `adéntrese` | `adentrarse` | 306 | review: merge |
| `asique` | `así que` | 300 | review: merge |
| `bájese` | `bajarse` | 360 | review: merge |
| `carteler` | `cartelería` | 376 | review: merge |
| `cepíllate` | `cepillarse` | 274 | review: merge |
| `cerchar` | `cercha` | 288 | review: merge |
| `comarcar` | `comarca` | 344 | review: merge |
| `comprarlo` | `comprar` | 292 | review: merge |
| `contribuído` | `contribuido` | 222 | review: merge |
| `conéctor` | `conector` | 270 | review: merge |
| `desarollar` | `desarrollar` | 311 | review: merge |
| `develado` | `develar` | 159 | review: merge |
| `dándote` | `dar` | 229 | review: merge |
| `enlista` | `enlistar` | 282 | review: merge |
| `escúchenme` | `escuchar` | 273 | review: merge |
| `etérica` | `etéreo` | 242 | review: merge |
| `facetados` | `facetado` | 296 | review: merge |
| `famosísima` | `famoso` | 190 | review: merge |
| `finísimo` | `fino` | 327 | review: merge |
| `fuése` | `irse` | 317 | review: merge |
| `gaditas` | `gaditano` | 285 | review: merge |
| `geeks` | `geek` | 301 | review: merge |
| `informaión` | `información` | 323 | review: merge |
| `interaccionan` | `interaccionar` | 372 | review: merge |
| `límpiela` | `limpiar` | 186 | review: merge |
| `milliones` | `millón` | 265 | review: merge |
| `minis` | `mini` | 475 | review: merge |
| `monoinsaturadas` | `monoinsaturado` | 292 | review: merge |
| `muriéndose` | `morirse` | 225 | review: merge |
| `neuropsicológica` | `neuropsicológico` | 358 | review: merge |
| `nostro` | `nosotros` | 361 | review: merge |
| `piénselo` | `pensar` | 259 | review: merge |
| `públicado` | `publicado` | 241 | review: merge |
| `recodar` | `recodo` | 367 | review: merge |
| `reinterpretado` | `reinterpretar` | 275 | review: merge |
| `representaciónes` | `representación` | 428 | review: merge |
| `shéij` | `jeque` | 301 | review: merge |
| `spaghetti` | `espagueti` | 390 | review: merge |
| `sírvanse` | `servirse` | 298 | review: merge |
| `taz` | `taza` | 377 | review: merge |
| `tecnicas` | `técnico` | 446 | review: merge |
| `testeado` | `testear` | 381 | review: merge |
| `triar` | `tríada` | 370 | review: merge |
| `tántrica` | `tántrico` | 201 | review: merge |
| `tírate` | `tirarse` | 237 | review: merge |
| `ultrabaja` | `ultrabajo` | 259 | review: merge |
| `virtualizada` | `virtualizar` | 267 | review: merge |
| `únanse` | `unirse` | 429 | review: merge |
| `abierta` | `abierto` | 333 | review: merge |
| `aburrer` | `aburrido` | 222 | review: merge |
| `albar` | `albarán` | 405 | review: merge |
| `amiotrófica` | `amiotrófico` | 342 | review: merge |
| `auror` | `aurora` | 198 | review: merge |
| `bioenergética` | `bioenergético` | 258 | review: merge |
| `comuniquese` | `comunicarse` | 379 | review: merge |
| `conspirativas` | `conspirativo` | 209 | review: merge |
| `coupage` | `cupaje` | 318 | review: merge |
| `depto` | `departamento` | 386 | review: merge |
| `dialógica` | `dialógico` | 243 | review: merge |
| `dres` | `doctor` | 263 | review: merge |
| `enlistados` | `enlistar` | 289 | review: merge |
| `enséñaselo` | `enseñar` | 236 | review: merge |
| `erotica` | `erótico` | 239 | review: merge |
| `famila` | `familia` | 180 | review: merge |
| `frote` | `frotar` | 298 | review: merge |
| `genómicas` | `genómico` | 340 | review: merge |
| `lasaliana` | `lasaliano` | 252 | review: merge |
| `límpielo` | `limpiar` | 318 | review: merge |
| `medecina` | `medicina` | 264 | review: merge |
| `multiplíquense` | `multiplicarse` | 338 | review: merge |
| `novísimo` | `nuevo` | 289 | review: merge |
| `pedigree` | `pedigrí` | 380 | review: merge |
| `ponchó` | `ponchar` | 263 | review: merge |
| `poniéndote` | `ponerse` | 318 | review: merge |
| `posbilidad` | `posibilidad` | 319 | review: merge |
| `preinstalada` | `preinstalar` | 299 | review: merge |
| `prepaga` | `prepago` | 318 | review: merge |
| `probá` | `probar` | 154 | review: merge |
| `riffs` | `riff` | 219 | review: merge |
| `ráton` | `ratón` | 235 | review: merge |
| `sotaventar` | `sotavento` | 242 | review: merge |
| `trasparentar` | `trasparente` | 282 | review: merge |
| `weblog` | `blog` | 383 | review: merge |
| `acomódate` | `acomodarse` | 355 | review: merge |
| `adolorida` | `adolorido` | 305 | review: merge |
| `brio` | `brío` | 289 | review: merge |
| `clickea` | `clickear` | 280 | review: merge |
| `cofinanciada` | `cofinanciar` | 231 | review: merge |
| `cojiendo` | `coger` | 228 | review: merge |
| `comúnes` | `común` | 225 | review: merge |
| `contáctese` | `contactar` | 198 | review: merge |
| `cria` | `cría` | 270 | review: merge |
| `dejadlo` | `dejar` | 164 | review: merge |
| `encontar` | `encontrar` | 286 | review: merge |
| `enjuáguelo` | `enjuagar` | 219 | review: merge |
| `esfuércense` | `esforzarse` | 192 | review: merge |
| `evolucionaria` | `evolucionario` | 215 | review: merge |
| `exilar` | `exiliado` | 302 | review: merge |
| `facetada` | `facetado` | 180 | review: merge |
| `finanza` | `finanzas` | 267 | review: merge |
| `firmwar` | `firmware` | 235 | review: merge |
| `fotogáfico` | `fotográfico` | 284 | review: merge |
| `frikis` | `friki` | 265 | review: merge |
| `hadices` | `hadiz` | 207 | review: merge |
| `hipoalergénicas` | `hipoalergénico` | 368 | review: merge |
| `huevar` | `hueva` | 364 | review: merge |
| `huído` | `huido` | 258 | review: merge |
| `identificarlas` | `identificar` | 304 | review: merge |
| `interacciona` | `interaccionar` | 313 | review: merge |
| `intranets` | `intranet` | 245 | review: merge |
| `jameos` | `jameo` | 379 | review: merge |
| `maloláctica` | `maloláctico` | 319 | review: merge |
| `malísimo` | `malo` | 127 | review: merge |
| `masterizado` | `masterizar` | 249 | review: merge |
| `metalica` | `metálico` | 209 | review: merge |
| `microfinanciera` | `microfinanciero` | 234 | review: merge |
| `ministrando` | `ministrar` | 335 | review: merge |
| `nuestrxs` | `nuestro` | 203 | review: merge |
| `permeado` | `permear` | 288 | review: merge |
| `precargadas` | `precargado` | 250 | review: merge |
| `preparaos` | `prepararse` | 162 | review: merge |
| `purpurar` | `púrpura` | 382 | review: merge |
| `pza` | `pieza` | 228 | review: merge |
| `quitándole` | `quitar` | 256 | review: merge |
| `redimensiona` | `redimensionar` | 171 | review: merge |
| `subsanarlo` | `subsanar` | 244 | review: merge |
| `technología` | `tecnología` | 242 | review: merge |
| `uff` | `uf` | 233 | review: merge |
| `utilizá` | `utilizar` | 308 | review: merge |
| `vacar` | `vacada` | 292 | review: merge |
| `voodoo` | `vudú` | 340 | review: merge |
| `abilidad` | `habilidad` | 269 | review: merge |
| `adaptándola` | `adaptar` | 283 | review: merge |
| `adhiriéndose` | `adherirse` | 288 | review: merge |
| `antialérgicas` | `antialérgico` | 208 | review: merge |
| `antiquísimo` | `antiguo` | 183 | review: merge |
| `antocianinas` | `antocianina` | 221 | review: merge |
| `aplíquelo` | `aplicar` | 343 | review: merge |
| `besame` | `besar` | 84 | review: merge |
| `buenísimos` | `bueno` | 180 | review: merge |
| `codeine` | `codeína` | 319 | review: merge |
| `cofinanciados` | `cofinanciar` | 174 | review: merge |
| `dalo` | `dar` | 292 | review: merge |
| `descriptas` | `describir` | 253 | review: merge |
| `empoderando` | `empoderar` | 182 | review: merge |
| `enamórate` | `enamorarse` | 340 | review: merge |
| `energizados` | `energizar` | 189 | review: merge |
| `específicado` | `especificado` | 210 | review: merge |
| `explíqueles` | `explicar` | 216 | review: merge |
| `fanzines` | `fanzine` | 266 | review: merge |
| `habérsele` | `haber` | 182 | review: merge |
| `haciéndola` | `hacer` | 369 | review: merge |
| `hermosísima` | `hermoso` | 237 | review: merge |
| `incorpórese` | `incorporarse` | 190 | review: merge |
| `indizado` | `indizar` | 274 | review: merge |
| `larguísima` | `largo` | 269 | review: merge |
| `linck` | `link` | 217 | review: merge |
| `losar` | `losa` | 254 | review: merge |
| `marrónes` | `marrón` | 246 | review: merge |
| `metida` | `meter` | 234 | review: merge |
| `ministran` | `ministrar` | 209 | review: merge |
| `mixturar` | `mixtura` | 295 | review: merge |
| `multiétnica` | `multiétnico` | 276 | review: merge |
| `sikh` | `sij` | 257 | review: merge |
| `socio-ambiental` | `socioambiental` | 289 | review: merge |
| `standar` | `estándar` | 198 | review: merge |
| `triathlon` | `triatlón` | 210 | review: merge |
| `apoyarno` | `apoyarse` | 294 | review: merge |
| `auto-evaluación` | `autoevaluación` | 215 | review: merge |
| `auto-servicio` | `autoservicio` | 255 | review: merge |
| `autobúse` | `autobús` | 230 | review: merge |
| `bisuteria` | `bisutería` | 219 | review: merge |
| `chi-cuadrado` | `chi cuadrado` | 200 | review: merge |
| `contraofensivo` | `contraofensiva` | 283 | review: merge |
| `culinaria` | `culinario` | 226 | review: merge |
| `disconfor` | `disconforme` | 168 | review: merge |
| `dándono` | `dar` | 247 | review: merge |
| `ex-alumno` | `exalumno` | 277 | review: merge |
| `explicarl` | `explicar` | 295 | review: merge |
| `fintechs` | `fintech` | 221 | review: merge |
| `monástica` | `monástico` | 125 | review: merge |
| `muggl` | `muggle` | 345 | review: merge |
| `multi-capa` | `multicapa` | 136 | review: merge |
| `multi-color` | `multicolor` | 270 | review: merge |
| `nupcia` | `nupcias` | 224 | review: merge |
| `optimal` | `óptimo` | 300 | review: merge |
| `penthous` | `penthouse` | 188 | review: merge |
| `permitirno` | `permitir` | 282 | review: merge |
| `post-conflicto` | `posconflicto` | 166 | review: merge |
| `praxi` | `praxis` | 312 | review: merge |
| `pre-instalación#hunt` | `preinstalación` | 135 | review: merge |
| `pre-pago` | `prepago` | 210 | review: merge |
| `pregúntal` | `preguntar` | 229 | review: merge |
| `proporcionándono` | `proporcionar` | 236 | review: merge |
| `psico-social` | `psicosocial` | 122 | review: merge |
| `puños` | `puño` | 197 | review: merge |
| `re-edición` | `reedición` | 199 | review: merge |
| `rias` | `ría` | 235 | review: merge |
| `socio-económicas` | `socioeconómico` | 322 | review: merge |
| `stakeholders` | `stakeholder` | 242 | review: merge |
| `ultra-delgado` | `ultradelgado` | 179 | review: merge |
| `vaping` | `vapeo` | 268 | review: merge |
| `vigila` | `vigilar` | 188 | review: merge |
| `acompáñeno` | `acompañar` | 184 | review: merge |
| `amémono` | `amar` | 210 | review: merge |
| `anti-estrógeno` | `antiestrógeno` | 216 | review: merge |
| `apoyarl` | `apoyar` | 297 | review: merge |
| `arq` | `arquitecto` | 284 | review: merge |
| `auto-control` | `autocontrol` | 206 | review: merge |
| `auto-estima` | `autoestima` | 243 | review: merge |
| `autoalineabl` | `autoalineable` | 197 | review: merge |
| `bebed` | `beber` | 201 | review: merge |
| `berber` | `bereber` | 128 | review: merge |
| `calefactabl` | `calefactable` | 278 | review: merge |
| `carraco` | `carraca` | 226 | review: merge |
| `co-pago` | `copago` | 165 | review: merge |
| `consecuentes` | `consecuente` | 207 | review: merge |
| `cruza` | `cruzar` | 200 | review: merge |
| `cucharadit#Maac` | `cucharadita` | 206 | review: merge |
| `despojarno` | `despojarse` | 163 | review: merge |
| `dirigirno` | `dirigirse` | 200 | review: merge |
| `fisica` | `física` | 194 | review: merge |
| `garantizarl` | `garantizar` | 182 | review: merge |
| `hashe` | `hash` | 226 | review: merge |
| `influencers` | `influencer` | 333 | review: merge |
| `informacióne` | `información` | 176 | review: merge |
| `jesu` | `jesús` | 244 | review: merge |
| `jovene` | `joven` | 266 | review: merge |
| `lanzacohete` | `lanzacohetes` | 275 | review: merge |
| `licenciantes` | `licenciante` | 191 | review: merge |
| `llevándol` | `llevar` | 136 | review: merge |
| `oxímor` | `oxímoron` | 130 | review: merge |
| `parótido` | `parótida` | 236 | review: merge |
| `pic-nic` | `picnic` | 134 | review: merge |
| `ponero` | `poner` | 219 | review: merge |
| `sintiéndono` | `sentirse` | 226 | review: merge |
| `socio-política` | `sociopolítico` | 162 | review: merge |
| `testers` | `tester` | 293 | review: merge |
| `tupper` | `táper` | 233 | review: merge |
| `utilizadore` | `utilizador` | 181 | review: merge |
| `acerquémono` | `acercarse` | 235 | review: merge |
| `anti-corrupción` | `anticorrupción` | 200 | review: merge |
| `anti-robo` | `antirrobo` | 201 | review: merge |
| `arrepiéntanse` | `arrepentirse` | 242 | review: merge |
| `auto-expresión` | `autoexpresión` | 148 | review: merge |
| `dadito` | `dado` | 176 | review: merge |
| `depilada` | `depilado` | 136 | review: merge |
| `dígal` | `decir` | 225 | review: merge |
| `educa` | `educar` | 268 | review: merge |
| `encontr` | `encontrar` | 209 | review: merge |
| `esforzándo` | `esforzarse` | 183 | review: merge |
| `esperad` | `esperar` | 144 | review: merge |
| `galeon` | `galeón` | 160 | review: merge |
| `guiándo` | `guiar` | 181 | review: merge |
| `implantabl` | `implantable` | 263 | review: merge |
| `lanzamisil` | `lanzamisiles` | 163 | review: merge |
| `lapsu` | `lapsus` | 122 | review: merge |
| `londr` | `londres` | 194 | review: merge |
| `macrame` | `macramé` | 202 | review: merge |
| `mandarl` | `mandar` | 140 | review: merge |
| `manteneo` | `mantenerse` | 170 | review: merge |
| `nosostro` | `nosotros` | 264 | review: merge |
| `notifíqueno` | `notificar` | 149 | review: merge |
| `okay` | `okey` | 316 | review: merge |
| `pagarl` | `pagar` | 196 | review: merge |
| `post-traumático` | `postraumático` | 200 | review: merge |
| `provea` | `proveer` | 114 | review: merge |
| `puedr` | `poder` | 194 | review: merge |
| `rompeola` | `rompeolas` | 117 | review: merge |
| `semi-nuevo` | `seminuevo` | 136 | review: merge |
| `suministrarl` | `suministrar` | 196 | review: merge |
| `vibrio` | `vibrión` | 224 | review: merge |
| `anti-arruga` | `antiarrugas` | 173 | review: merge |
| `aros` | `aro` | 253 | review: merge |
| `arrepentirno` | `arrepentirse` | 129 | review: merge |
| `auto-determinación` | `autodeterminación` | 205 | review: merge |
| `añadiéndol` | `añadir` | 143 | review: merge |
| `confetti` | `confeti` | 189 | review: merge |
| `confíen` | `confiar` | 160 | review: merge |
| `contactado` | `contactar` | 284 | review: merge |
| `contáctanos` | `contactar` | 263 | review: merge |
| `crean` | `crear` | 172 | review: merge |
| `dejándono` | `dejar` | 224 | review: merge |
| `despertarno` | `despertarse` | 178 | review: merge |
| `hotelera` | `hotelero` | 1,348 | review: merge |
| `espana` | `españa` | 1,177 | review: merge |
| `logistica` | `logística` | 611 | review: merge |
| `biociencias` | `biociencia` | 376 | review: merge |
| `inglésd` | `inglés` | 309 | review: merge |
| `facilitarl` | `facilitar` | 265 | review: merge |
| `maritima` | `marítimo` | 237 | review: merge |
| `chlamydia` | `clamidia` | 235 | review: merge |
| `aplicada` | `aplicado` | 233 | review: merge |
| `echinacea` | `equinácea` | 233 | review: merge |
| `muéstrano` | `mostrar` | 227 | review: merge |
| `sufi` | `sufí` | 227 | review: merge |
| `multidepor` | `multideporte` | 219 | review: merge |
| `pre-tratamiento` | `pretratamiento` | 211 | review: merge |
| `dirigiéndono` | `dirigirse` | 208 | review: merge |
| `amarte` | `amar` | 201 | review: merge |
| `cerciorarno` | `cerciorarse` | 192 | review: merge |
| `hiphop` | `hip hop` | 192 | review: merge |
| `punjabi` | `panyabí` | 190 | review: merge |
| `piretroid` | `piretroide` | 186 | review: merge |
| `diám` | `diámetro` | 183 | review: merge |
| `ingl` | `inglés` | 183 | review: merge |
| `fluoxetine` | `fluoxetina` | 181 | review: merge |
| `explicándol` | `explicar` | 180 | review: merge |
| `resuelve` | `resolver` | 178 | review: merge |
| `padrespadr` | `padre` | 173 | review: merge |
| `by-pass` | `bypass` | 172 | review: merge |
| `nanoparticl` | `nanopartícula` | 166 | review: merge |
| `mantras` | `mantra` | 162 | review: merge |
| `mecca` | `meca` | 161 | review: merge |
| `meterno` | `meterse` | 160 | review: merge |
| `mycoplasma` | `micoplasma` | 159 | review: merge |
| `dejémono` | `dejarse` | 157 | review: merge |
| `go-go` | `gogó` | 152 | review: merge |
| `igloo` | `iglú` | 152 | review: merge |
| `metrobus` | `metrobús` | 152 | review: merge |
| `gingko` | `ginkgo` | 149 | review: merge |
| `convencerl` | `convencer` | 147 | review: merge |
| `crimene` | `crimen` | 147 | review: merge |
| `canguros` | `canguro` | 145 | review: merge |
| `equivocarno` | `equivocarse` | 143 | review: merge |
| `reusabl` | `reusable` | 143 | review: merge |
| `kleenex` | `clínex` | 142 | review: merge |
| `mareos` | `mareo` | 142 | review: merge |
| `formalidades` | `formalidad` | 140 | review: merge |
| `litchi` | `lichi` | 138 | review: merge |
| `nacidos` | `nacido` | 138 | review: merge |
| `pre-autorización` | `preautorización` | 138 | review: merge |
| `adhoc` | `ad hoc` | 137 | review: merge |
| `marathi` | `maratí` | 136 | review: merge |
| `anti-gravedad` | `antigravedad` | 135 | review: merge |
| `renuncian` | `renunciar` | 135 | review: merge |
| `dedicándono` | `dedicarse` | 134 | review: merge |
| `co-producción` | `coproducción` | 133 | review: merge |
| `cazacarro` | `cazacarros` | 132 | review: merge |
| `penis` | `pene` | 132 | review: merge |
| `concederl` | `conceder` | 130 | review: merge |
| `pagada` | `pagar` | 130 | review: merge |
| `curiosidades` | `curiosidad` | 129 | review: merge |
| `aparthotels` | `apartahotel` | 128 | review: merge |
| `infanto-juvenil` | `infantojuvenil` | 127 | review: merge |
| `oximetr` | `oximetría` | 127 | review: merge |
| `asegurémono` | `asegurarse` | 124 | review: merge |
| `oxicor` | `oxicorte` | 124 | review: merge |
| `jovenes` | `joven` | 2,177 | review: merge |
| `pasamano` | `pasamanos` | 1,320 | review: merge |
| `start-up` | `startup` | 1,010 | review: merge |
| `calentito` | `caliente` | 923 | review: merge |
| `amarar` | `amar` | 773 | review: merge |
| `cerdito` | `cerdo` | 751 | review: merge |
| `patito` | `pato` | 747 | review: merge |
| `cerquita` | `cerca` | 657 | review: merge |
| `sobreescribir` | `sobrescribir` | 636 | review: merge |
| `brear` | `brea` | 627 | review: merge |
| `hibridar` | `híbrido` | 605 | review: merge |
| `mejoro` | `mejorar` | 592 | review: merge |
| `valorarse` | `valorar` | 571 | review: merge |
| `fregón` | `fregona` | 502 | review: merge |
| `cuadrito` | `cuadro` | 499 | review: merge |
| `congojar` | `congoja` | 464 | review: merge |
| `quilatar` | `quilate` | 451 | review: merge |
| `catolica` | `católico` | 433 | review: merge |
| `trozar` | `troza` | 426 | review: merge |
| `playita` | `playa` | 411 | review: merge |
| `adujar` | `aducir` | 347 | review: merge |
| `succiona` | `succionar` | 335 | review: merge |
| `propuestar` | `propuesta` | 313 | review: merge |
| `coñito` | `coño` | 312 | review: merge |
| `dildos` | `dildo` | 299 | review: merge |
| `agusto` | `a gusto` | 294 | review: merge |
| `ripiar` | `ripio` | 282 | review: merge |
| `desalmar` | `desalmado` | 280 | review: merge |
| `pasad` | `pasar` | 280 | review: merge |
| `posmoderna` | `posmoderno` | 278 | review: merge |
| `telefonica` | `telefónico` | 278 | review: merge |
| `agroecológica` | `agroecológico` | 270 | review: merge |
| `alijar` | `alijo` | 265 | review: merge |
| `precargada` | `precargado` | 265 | review: merge |
| `actualícelo` | `actualizar` | 264 | review: merge |
| `espectroscopio` | `espectroscopia` | 262 | review: merge |
| `transcendencia` | `trascendencia` | 260 | review: merge |
| `esclerótico` | `esclerótica` | 259 | review: merge |
| `papeleria` | `papelería` | 249 | review: merge |
| `enaguar` | `enagua` | 246 | review: merge |
| `volvio` | `volver` | 246 | review: merge |
| `ticks` | `tic` | 242 | review: merge |
| `jurisdiciones` | `jurisdicción` | 241 | review: merge |
| `regulamiento` | `reglamento` | 241 | review: merge |
| `sopar` | `sopa` | 239 | review: merge |
| `maravíllese` | `maravillarse` | 236 | review: merge |
| `calefactados` | `calefactado` | 233 | review: merge |
| `contendor` | `contenedor` | 232 | review: merge |
| `minivans` | `minivan` | 231 | review: merge |
| `completísima` | `completo` | 230 | review: merge |
| `inconciente` | `inconsciente` | 230 | review: merge |
| `cantonero` | `cantonera` | 229 | review: merge |
| `coporativo` | `corporativo` | 229 | review: merge |
| `ejecútelo` | `ejecutar` | 226 | review: merge |
| `omelettes` | `omelette` | 224 | review: merge |
| `lacito` | `lazo` | 223 | review: merge |
| `úselo` | `usar` | 223 | review: merge |
| `huesecillo` | `hueso` | 220 | review: merge |
| `refrésquese` | `refrescarse` | 220 | review: merge |
| `sijs` | `sij` | 220 | review: merge |
| `advirtiéndole` | `advertir` | 218 | review: merge |
| `posteriora` | `posterior` | 217 | review: merge |
| `compártala` | `compartir` | 216 | review: merge |
| `culturistas` | `culturista` | 213 | review: merge |
| `acordeonar` | `acordeón` | 212 | review: merge |
| `acomódese` | `acomodarse` | 208 | review: merge |
| `raviolis` | `ravioli` | 208 | review: merge |
| `jabonar` | `jabón` | 207 | review: merge |
| `precisa` | `preciso` | 207 | review: merge |
| `intalaciones` | `instalación` | 203 | review: merge |
| `fentanyl` | `fentanilo` | 202 | review: merge |
| `sinergizado` | `sinergizar` | 202 | review: merge |
| `visítame` | `visitar` | 151 | review: merge |
| `buenísimas` | `bueno` | 200 | review: merge |
| `desconéctelo` | `desconectar` | 200 | review: merge |
| `sentia` | `sentir` | 200 | review: merge |
| `suporta` | `soportar` | 199 | review: merge |
| `atravez` | `a través` | 198 | review: merge |
| `pidámosle` | `pedir` | 197 | review: merge |
| `agradeciéndole` | `agradecer` | 193 | review: merge |
| `pidiéndole` | `pedir` | 192 | review: merge |
| `proporcionándo` | `proporcionar` | 191 | review: merge |
| `contenidor` | `contenido` | 189 | review: merge |
| `transdermal` | `transdérmico` | 189 | review: merge |
| `glamorosas` | `glamoroso` | 187 | review: merge |
| `rutilar` | `rutilo` | 186 | review: merge |
| `exponiéndolo` | `exponer` | 185 | review: merge |
| `llamarle` | `llamar` | 182 | review: merge |
| `ortostática` | `ortostático` | 181 | review: merge |
| `subcategoria` | `subcategoría` | 180 | review: merge |
| `triatletas` | `triatleta` | 180 | review: merge |
| `florecita` | `flor` | 178 | review: merge |
| `diria` | `decir` | 177 | review: merge |
| `floreria` | `florería` | 177 | review: merge |
| `hacero` | `hacer` | 176 | review: merge |
| `visitano` | `visitar` | 176 | review: merge |
| `estratégia` | `estrategia` | 175 | review: merge |
| `manteniéndola` | `mantener` | 175 | review: merge |
| `transsexual` | `transexual` | 175 | review: merge |
| `customizados` | `customizar` | 174 | review: merge |
| `enlistan` | `enlistar` | 174 | review: merge |
| `corderito` | `cordero` | 173 | review: merge |
| `dividiéndolo` | `dividir` | 173 | review: merge |
| `pobrecito` | `pobre` | 173 | review: merge |
| `viejecito` | `viejo` | 173 | review: merge |
| `contenio` | `contenido` | 172 | review: merge |
| `espejito` | `espejo` | 172 | review: merge |
| `retorciéndose` | `retorcerse` | 172 | review: merge |
| `valiosísimo` | `valioso` | 172 | review: merge |
| `amadísimo` | `amado` | 171 | review: merge |
| `clústers` | `clúster` | 170 | review: merge |
| `veracruzana` | `veracruzano` | 170 | review: merge |
| `ofrec` | `ofrecer` | 169 | review: merge |
| `ramito` | `ramo` | 169 | review: merge |
| `antiimperialistas` | `antiimperialista` | 168 | review: merge |
| `elimínelo` | `eliminar` | 168 | review: merge |
| `haciéndonoslo` | `hacer` | 168 | review: merge |
| `olográfica` | `holográfico` | 168 | review: merge |
| `tempertura` | `temperatura` | 168 | review: merge |
| `ventanita` | `ventana` | 168 | review: merge |
| `acompañandolo` | `acompañar` | 167 | review: merge |
| `coffeeshops` | `coffeeshop` | 167 | review: merge |
| `transcutánea` | `transcutáneo` | 167 | review: merge |
| `sidrerías` | `sidrería` | 166 | review: merge |
| `excluído` | `excluido` | 131 | review: merge |
| `monitoreen` | `monitorear` | 165 | review: merge |
| `ocaciones` | `ocasión` | 165 | review: merge |
| `dejarla` | `dejar` | 163 | review: merge |
| `autocontener` | `autocontenido` | 162 | review: merge |
| `circulo` | `círculo` | 162 | review: merge |
| `portamaleta` | `portamaletas` | 162 | review: merge |
| `sorpréndase` | `sorprenderse` | 162 | review: merge |
| `impidiéndole` | `impedir` | 161 | review: merge |
| `dashboards` | `dashboard` | 160 | review: merge |
| `destajar` | `destajo` | 160 | review: merge |
| `queridísimos` | `querido` | 160 | review: merge |
| `utizada` | `utilizar` | 160 | review: merge |
| `cremados` | `cremar` | 159 | review: merge |
| `populación` | `población` | 159 | review: merge |
| `acercándote` | `acercarse` | 158 | review: merge |
| `omnichannel` | `omnicanal` | 158 | review: merge |
| `remasterizados` | `remasterizar` | 158 | review: merge |
| `durísima` | `duro` | 157 | review: merge |
| `imponiéndose` | `imponerse` | 157 | review: merge |
| `otrxs` | `otro` | 157 | review: merge |
| `balotar` | `balota` | 156 | review: merge |
| `enlistadas` | `enlistar` | 156 | review: merge |
| `fundiéndose` | `fundirse` | 156 | review: merge |
| `queridísima` | `querido` | 156 | review: merge |
| `pruebo` | `prueba` | 155 | review: merge |
| `tesorer` | `tesorería` | 155 | review: merge |
| `collección` | `colección` | 154 | review: merge |
| `digita` | `digitar` | 154 | review: merge |
| `reinterpretada` | `reinterpretar` | 154 | review: merge |
| `comuniciación` | `comunicación` | 153 | review: merge |
| `sáquelo` | `sacar` | 153 | review: merge |
| `capuccino` | `capuchino` | 152 | review: merge |
| `fotocromática` | `fotocromático` | 151 | review: merge |
| `párking` | `parking` | 150 | review: merge |
| `tornasolar` | `tornasolado` | 150 | review: merge |
| `adáptese` | `adaptarse` | 147 | review: merge |
| `nanométrica` | `nanométrico` | 147 | review: merge |
| `dobladoras` | `dobladora` | 146 | review: merge |
| `electronicos` | `electrónico` | 146 | review: merge |
| `pequeñitas` | `pequeñito` | 146 | review: merge |
| `selecionado` | `seleccionado` | 146 | review: merge |
| `consultarlas` | `consultar` | 145 | review: merge |
| `enjuágala` | `enjuagar` | 145 | review: merge |
| `doradito` | `dorado` | 144 | review: merge |
| `interes` | `interés` | 144 | review: merge |
| `toppings` | `topping` | 144 | review: merge |
| `glorifícame` | `glorificar` | 143 | review: merge |
| `qeu` | `que` | 143 | review: merge |
| `antroposófica` | `antroposófico` | 142 | review: merge |
| `centrarte` | `centrarse` | 142 | review: merge |
| `consérvelo` | `conservar` | 142 | review: merge |
| `edificándoos` | `edificar` | 141 | review: merge |
| `vivifícame` | `vivificar` | 141 | review: merge |
| `differente` | `diferente` | 140 | review: merge |
| `evangelística` | `evangelístico` | 140 | review: merge |
| `muestreadas` | `muestrear` | 140 | review: merge |
| `socioeducativa` | `socioeducativo` | 140 | review: merge |
| `pregúntense` | `preguntarse` | 139 | review: merge |
| `conservarla` | `conservar` | 138 | review: merge |
| `datasets` | `dataset` | 138 | review: merge |
| `sosteniéndola` | `sostener` | 138 | review: merge |
| `esfuércese` | `esforzarse` | 137 | review: merge |
| `ismos` | `ismo` | 137 | review: merge |
| `actívela` | `activar` | 136 | review: merge |
| `artesanias` | `artesanía` | 136 | review: merge |
| `capsaicin` | `capsaicina` | 135 | review: merge |
| `shinto` | `sintoísmo` | 135 | review: merge |
| `agende` | `agendar` | 134 | review: merge |
| `completá` | `completar` | 133 | review: merge |
| `loque` | `lo que` | 133 | review: merge |
| `pixelados` | `pixelado` | 133 | review: merge |
| `envien` | `enviar` | 132 | review: merge |
| `numerosísimo` | `numeroso` | 132 | review: merge |
| `zooms` | `zoom` | 132 | review: merge |
| `apropriada` | `apropiado` | 131 | review: merge |
| `ole` | `olé` | 1,392 | review: merge |
| `articulos` | `artículo` | 1,085 | review: merge |
| `quite` | `quitar` | 514 | review: merge |
| `symposium` | `simposio` | 241 | review: merge |
| `artemisia` | `artemisa` | 235 | review: merge |
| `formica` | `fórmica` | 235 | review: merge |
| `post-operatorio` | `postoperatorio` | 235 | review: merge |
| `anti-oxidante` | `antioxidante` | 225 | review: merge |
| `comunicándono` | `comunicarse` | 192 | review: merge |
| `ojosojo` | `ojo` | 189 | review: merge |
| `produsctos` | `producto` | 189 | review: merge |
| `ntra` | `nuestro` | 187 | review: merge |
| `post-entrenamiento` | `postentrenamiento` | 185 | review: merge |
| `sinópsis` | `sinopsis` | 182 | review: merge |
| `fotografica` | `fotográfico` | 181 | review: merge |
| `ayúdal` | `ayudar` | 180 | review: merge |
| `post-tratamiento` | `postratamiento` | 178 | review: merge |
| `entérate` | `enterarse` | 177 | review: merge |
| `entregarl` | `entregar` | 174 | review: merge |
| `multi-plataforma` | `multiplataforma` | 174 | review: merge |
| `sub-páginas` | `subpágina` | 173 | review: merge |
| `guiarno` | `guiar` | 172 | review: merge |
| `cubrebota` | `cubrebotas` | 170 | review: merge |
| `avisarno` | `avisar` | 169 | review: merge |
| `siervosiervo` | `siervo` | 165 | review: merge |
| `post-grado` | `posgrado` | 162 | review: merge |
| `dispararl` | `disparar` | 161 | review: merge |
| `rooibo` | `rooibos` | 157 | review: merge |
| `biblica` | `bíblico` | 156 | review: merge |
| `cordobé` | `cordobés` | 156 | review: merge |
| `instagramers` | `instagramer` | 156 | review: merge |
| `post-sinodal` | `postsinodal` | 156 | review: merge |
| `cortaseto` | `cortasetos` | 155 | review: merge |
| `insomnia` | `insomnio` | 153 | review: merge |
| `siervossiervo` | `siervo` | 153 | review: merge |
| `tíos` | `tío` | 153 | review: merge |
| `auto-regulación` | `autorregulación` | 150 | review: merge |
| `dongl` | `dongle` | 149 | review: merge |
| `explicándono` | `explicar` | 148 | review: merge |
| `eucaliptu` | `eucalipto` | 147 | review: merge |
| `taqueria` | `taquería` | 146 | review: merge |
| `acercarno` | `acercarse` | 144 | review: merge |
| `regocijarno` | `regocijarse` | 144 | review: merge |
| `qibla` | `quibla` | 143 | review: merge |
| `tejidas` | `tejer` | 143 | review: merge |
| `neanderthal` | `neandertal` | 141 | review: merge |
| `concibió` | `concebir` | 140 | review: merge |
| `animándol` | `animar` | 139 | review: merge |
| `ofrecerno` | `ofrecer` | 139 | review: merge |
| `tomarl` | `tomar` | 139 | review: merge |
| `rosacruces` | `rosacruz` | 135 | review: merge |
| `tierna` | `tierno` | 134 | review: merge |
| `co-propietario` | `copropietario` | 133 | review: merge |
| `concentrándono` | `concentrarse` | 133 | review: merge |
| `escucharl` | `escuchar` | 133 | review: merge |
| `anti-guerra` | `antiguerra` | 132 | review: merge |
| `centrémono` | `centrarse` | 132 | review: merge |
| `refiriéndono` | `referirse` | 132 | review: merge |
| `semi-profesional` | `semiprofesional` | 131 | review: merge |
| `neoprene` | `neopreno` | 129 | review: merge |
| `pre-final` | `prefinal` | 129 | review: merge |
| `proporcionada` | `proporcionar` | 128 | review: merge |
| `aportarl` | `aportar` | 127 | review: merge |
| `internaciol` | `internacional` | 127 | review: merge |
| `licence` | `licencia` | 127 | review: merge |
| `bulevard` | `bulevar` | 124 | review: merge |
| `afroestadounidens` | `afroestadounidense` | 123 | review: merge |
| `co-escribió` | `coescribir` | 123 | review: merge |
| `nervios` | `nervio` | 29,958 | review: merge |
| `medioambiente` | `medio ambiente` | 14,844 | review: merge |
| `rascacielo` | `rascacielos` | 5,127 | review: merge |
| `eslabonar` | `eslabón` | 3,391 | review: merge |
| `memorar` | `memorando` | 2,725 | review: merge |
| `comisar` | `comisaría` | 2,529 | review: merge |
| `fajar` | `faja` | 2,504 | review: merge |
| `papelear` | `papeleo` | 2,252 | review: merge |
| `piar` | `pie` | 2,170 | review: merge |
| `alicatar` | `alicate` | 1,920 | review: merge |
| `indexado` | `indexar` | 1,590 | review: merge |
| `vacación` | `vacaciones` | 981 | review: merge |
| `trasporte` | `transporte` | 828 | review: merge |
| `inscripto` | `inscrito` | 751 | review: merge |
| `sicológico` | `psicológico` | 749 | review: merge |
| `culotte` | `culote` | 720 | review: merge |
| `pajarito` | `pájaro` | 720 | review: merge |
| `tocadisco` | `tocadiscos` | 490 | review: merge |
| `desvergonzar` | `desvergonzado` | 469 | review: merge |
| `sendo` | `sendos` | 461 | review: merge |
| `terraplenar` | `terraplén` | 437 | review: merge |
| `alambicar` | `alambique` | 434 | review: merge |
| `taladrador` | `taladradora` | 403 | review: merge |
| `trasferencia` | `transferencia` | 400 | review: merge |
| `conectador` | `conector` | 396 | review: merge |
| `transcendental` | `trascendental` | 387 | review: merge |
| `barbechar` | `barbecho` | 378 | review: merge |
| `solario` | `solárium` | 374 | review: merge |
| `nectarino` | `nectarina` | 371 | review: merge |
| `farolito` | `farol` | 365 | review: merge |
| `logar` | `lograr` | 354 | review: merge |
| `preste` | `prestar` | 329 | review: merge |
| `formo` | `forma` | 328 | review: merge |
| `estilosas` | `estiloso` | 324 | review: merge |
| `convesaciones` | `conversación` | 323 | review: merge |
| `fregador` | `fregadora` | 323 | review: merge |
| `postmenopáusicas` | `postmenopáusico` | 316 | review: merge |
| `pocito` | `pozo` | 302 | review: merge |
| `interlinear` | `interlineado` | 300 | review: merge |
| `echadle` | `echar` | 295 | review: merge |
| `departmento` | `departamento` | 294 | review: merge |
| `colonoscopía` | `colonoscopia` | 282 | review: merge |
| `angelus` | `ángelus` | 279 | review: merge |
| `notifiqueme` | `notificar` | 271 | review: merge |
| `cofundó` | `cofundar` | 266 | review: merge |
| `aplíquese` | `aplicarse` | 256 | review: merge |
| `hydráulico` | `hidráulico` | 253 | review: merge |
| `paqueter` | `paquetería` | 250 | review: merge |
| `kebabs` | `kebab` | 249 | review: merge |
| `pequenas` | `pequeño` | 248 | review: merge |
| `cafetalera` | `cafetalero` | 247 | review: merge |
| `energiza` | `energizar` | 247 | review: merge |
| `ensenanza` | `enseñanza` | 246 | review: merge |
| `permea` | `permear` | 244 | review: merge |
| `desganar` | `desgana` | 243 | review: merge |
| `ramitas` | `ramita` | 235 | review: merge |
| `cacito` | `cazo` | 231 | review: merge |
| `gruas` | `grúa` | 230 | review: merge |
| `proteje` | `proteger` | 229 | review: merge |
| `circonitas` | `circonita` | 227 | review: merge |
| `alégrense` | `alegrarse` | 226 | review: merge |
| `compadrar` | `compadre` | 225 | review: merge |
| `patita` | `pata` | 225 | review: merge |
| `reflectiva` | `reflectivo` | 225 | review: merge |
| `optimas` | `óptimo` | 224 | review: merge |
| `redirigiremos` | `redirigir` | 223 | review: merge |
| `porcar` | `porqué` | 221 | review: merge |
| `touchdowns` | `touchdown` | 220 | review: merge |
| `significantemente` | `significativamente` | 218 | review: merge |
| `tenar` | `tener` | 218 | review: merge |
| `decider` | `decidir` | 216 | review: merge |
| `solita` | `solito` | 214 | review: merge |
| `hahaha` | `jaja` | 213 | review: merge |
| `vallecito` | `valle` | 213 | review: merge |
| `simposium` | `simposio` | 212 | review: merge |
| `conéctelo` | `conectar` | 210 | review: merge |
| `violaciónes` | `violación` | 209 | review: merge |
| `acuérdense` | `acordarse` | 208 | review: merge |
| `invítelo` | `invitar` | 208 | review: merge |
| `separándolo` | `separar` | 206 | review: merge |
| `propriedad` | `propiedad` | 205 | review: merge |
| `rooteado` | `rootear` | 205 | review: merge |
| `habiéndose` | `haber` | 203 | review: merge |
| `entretelar` | `entretela` | 201 | review: merge |
| `mantita` | `manta` | 201 | review: merge |
| `pelet` | `pélet` | 201 | review: merge |
| `sepultáronlo` | `sepultar` | 200 | review: merge |
| `cusqueña` | `cusqueño` | 197 | review: merge |
| `dotándola` | `dotar` | 197 | review: merge |
| `cocteler` | `coctelería` | 194 | review: merge |
| `empápate` | `empaparse` | 194 | review: merge |
| `prepar` | `preparar` | 194 | review: merge |
| `alojándose` | `alojarse` | 193 | review: merge |
| `arrástrala` | `arrastrar` | 193 | review: merge |
| `estandardizar` | `estandarizar` | 193 | review: merge |
| `horcajada` | `horcajadas` | 192 | review: merge |
| `perdonándoos` | `perdonar` | 191 | review: merge |
| `companero` | `compañero` | 190 | review: merge |
| `antineumocócica` | `antineumocócico` | 185 | review: merge |
| `deseás` | `desear` | 185 | review: merge |
| `íconos` | `ícono` | 185 | review: merge |
| `gistograma` | `histograma` | 184 | review: merge |
| `amaderada` | `amaderado` | 182 | review: merge |
| `recuéstese` | `recostarse` | 182 | review: merge |
| `famlia` | `familia` | 180 | review: merge |
| `veia` | `ver` | 180 | review: merge |
| `brahmana` | `brahmán` | 178 | review: merge |
| `dovelar` | `dovela` | 176 | review: merge |
| `levantáronse` | `levantarse` | 176 | review: merge |
| `transcendente` | `trascendente` | 176 | review: merge |
| `digite` | `digitar` | 174 | review: merge |
| `reúnanse` | `reunirse` | 173 | review: merge |
| `scones` | `scone` | 173 | review: merge |
| `electromágnetico` | `electromagnético` | 172 | review: merge |
| `mézclelo` | `mezclar` | 172 | review: merge |
| `titulizaciones` | `titulización` | 172 | review: merge |
| `danar` | `dañar` | 171 | review: merge |
| `suprimirlo` | `suprimir` | 171 | review: merge |
| `quadrados` | `cuadrado` | 170 | review: merge |
| `arrastrándolo` | `arrastrar` | 169 | review: merge |
| `destruídos` | `destruir` | 169 | review: merge |
| `rigoroso` | `riguroso` | 168 | review: merge |
| `coproducido` | `coproducir` | 167 | review: merge |
| `descargá` | `descargar` | 167 | review: merge |
| `utilizándola` | `utilizar` | 167 | review: merge |
| `anio` | `año` | 166 | review: merge |
| `girándola` | `girar` | 166 | review: merge |
| `hermosísimo` | `hermoso` | 166 | review: merge |
| `pantys` | `panti` | 166 | review: merge |
| `vouchers` | `voucher` | 166 | review: merge |
| `desinstala` | `desinstalar` | 164 | review: merge |
| `etiqueado` | `etiquetar` | 164 | review: merge |
| `martinis` | `martini` | 164 | review: merge |
| `asignandole` | `asignar` | 163 | review: merge |
| `archeologico` | `arqueológico` | 162 | review: merge |
| `consígalo` | `conseguir` | 161 | review: merge |
| `unámonos` | `unirse` | 161 | review: merge |
| `enséñanos` | `enseñar` | 159 | review: merge |
| `mandarno` | `mandar` | 159 | review: merge |
| `mensa` | `menso` | 159 | review: merge |
| `pixelada` | `pixelado` | 158 | review: merge |
| `serigrafiada` | `serigrafiado` | 158 | review: merge |
| `contruir` | `construir` | 157 | review: merge |
| `cubico` | `cúbico` | 157 | review: merge |
| `desatadlo` | `desatar` | 157 | review: merge |
| `randomizados` | `randomizado` | 157 | review: merge |
| `ferratas` | `ferrata` | 155 | review: merge |
| `matémosle` | `matar` | 155 | review: merge |
| `traduciéndose` | `traducirse` | 155 | review: merge |
| `proyectación` | `proyección` | 154 | review: merge |
| `apáguelo` | `apagar` | 153 | review: merge |
| `conociéndose` | `conocer` | 153 | review: merge |
| `florister` | `floristería` | 153 | review: merge |
| `niñxs` | `niño` | 153 | review: merge |
| `preveer` | `prever` | 153 | review: merge |
| `superfície` | `superficie` | 152 | review: merge |
| `cientifica` | `científico` | 151 | review: merge |
| `ohhh` | `oh` | 150 | review: merge |
| `súmese` | `sumarse` | 150 | review: merge |
| `autolesiones` | `autolesión` | 149 | review: merge |
| `gloríese` | `gloriarse` | 149 | review: merge |
| `vlogs` | `vlog` | 149 | review: merge |
| `aplastarlo` | `aplastar` | 148 | review: merge |
| `droguer` | `droguería` | 148 | review: merge |
| `desarollado` | `desarrollado` | 146 | review: merge |
| `peraltar` | `peralte` | 146 | review: merge |
| `sidrer` | `sidrería` | 146 | review: merge |
| `poliquística` | `poliquístico` | 145 | review: merge |
| `teatralizadas` | `teatralizado` | 145 | review: merge |
| `comunicándote` | `comunicarse` | 144 | review: merge |
| `hepatotóxica` | `hepatotóxico` | 144 | review: merge |
| `prolífero` | `prolífico` | 143 | review: merge |
| `aerotransportadas` | `aerotransportado` | 141 | review: merge |
| `orfebrer` | `orfebrería` | 141 | review: merge |
| `prescolar` | `preescolar` | 141 | review: merge |
| `sencillísimo` | `sencillo` | 141 | review: merge |
| `yóguica` | `yóguico` | 141 | review: merge |
| `artísta` | `artista` | 138 | review: merge |
| `contrareembolso` | `contrarreembolso` | 138 | review: merge |
| `instálela` | `instalar` | 138 | review: merge |
| `utlizar` | `utilizar` | 138 | review: merge |
| `diputar` | `diputada` | 137 | review: merge |
| `estámos` | `estar` | 136 | review: merge |
| `rápidaente` | `rápidamente` | 136 | review: merge |
| `ámplia` | `amplio` | 136 | review: merge |
| `creosotar` | `creosota` | 135 | review: merge |
| `nerds` | `nerd` | 135 | review: merge |
| `santer` | `santería` | 135 | review: merge |
| `analizarla` | `analizar` | 134 | review: merge |
| `arpegiar` | `arpegio` | 134 | review: merge |
| `lapices` | `lápiz` | 134 | review: merge |
| `qubits` | `qubit` | 134 | review: merge |
| `atópicas` | `atópico` | 133 | review: merge |
| `plomeria` | `plomería` | 133 | review: merge |
| `torniller` | `tornillería` | 132 | review: merge |
| `senor` | `señor` | 3,499 | review: merge |
| `bazaar` | `bazar` | 812 | review: merge |
| `oops` | `ups` | 665 | review: merge |
| `gestiona` | `gestionar` | 593 | review: merge |
| `sonríe` | `sonreír` | 506 | review: merge |
| `medica` | `médica` | 391 | review: merge |
| `entienda` | `entender` | 316 | review: merge |
| `pentecostale` | `pentecostal` | 275 | review: merge |
| `hábea` | `hábeas corpus` | 270 | review: merge |
| `pre-existente` | `preexistente` | 252 | review: merge |
| `maasai` | `masái` | 240 | review: merge |
| `post-apocalíptico` | `postapocalíptico` | 227 | review: merge |
| `auto-cuidado` | `autocuidado` | 226 | review: merge |
| `incorpora` | `incorporar` | 226 | review: merge |
| `tecnologias` | `tecnología` | 224 | review: merge |
| `pagina` | `página` | 218 | review: merge |
| `queloid` | `queloide` | 217 | review: merge |
| `chilli` | `chile` | 215 | review: merge |
| `facilitándol` | `facilitar` | 214 | review: merge |
| `descagar` | `descargar` | 213 | review: merge |
| `musica` | `música` | 207 | review: merge |
| `callejas` | `calleja` | 204 | review: merge |
| `lumens` | `lumen` | 203 | review: merge |
| `bioflavonoid` | `bioflavonoide` | 201 | review: merge |
| `marcapunto` | `marcapuntos` | 199 | review: merge |
| `afloje` | `aflojar` | 196 | review: merge |
| `asignarl` | `asignar` | 193 | review: merge |
| `olvídate` | `olvidarse` | 189 | review: merge |
| `biotec` | `biotecnología` | 187 | review: merge |
| `post-parto` | `posparto` | 185 | review: merge |
| `apúntate` | `apuntarse` | 183 | review: merge |
| `desprendibl` | `desprendible` | 183 | review: merge |
| `e-bikes` | `e-bike` | 183 | review: merge |
| `interiores` | `interior` | 183 | review: merge |
| `papito` | `papá` | 182 | review: merge |
| `pre-escucha` | `preescucha` | 182 | review: merge |
| `considerarno` | `considerarse` | 180 | review: merge |
| `auto-conciencia` | `autoconciencia` | 175 | review: merge |
| `escríbano` | `escribir` | 174 | review: merge |
| `punky` | `punki` | 174 | review: merge |
| `haciéndono` | `hacer` | 172 | review: merge |
| `semi-automática` | `semiautomático` | 171 | review: merge |
| `alegrémono` | `alegrarse` | 168 | review: merge |
| `exequia` | `exequias` | 164 | review: merge |
| `semi-intensivo` | `semiintensivo` | 162 | review: merge |
| `limpiacristal` | `limpiacristales` | 160 | review: merge |
| `moje` | `mojar` | 158 | review: merge |
| `spoilers` | `spoiler` | 158 | review: merge |
| `meleno` | `melena` | 157 | review: merge |
| `comentatio` | `comentario` | 156 | review: merge |
| `coroid` | `coroides` | 156 | review: merge |
| `chaise-longue` | `chaise longue` | 155 | review: merge |
| `dadno` | `dar` | 151 | review: merge |
| `estandare` | `estándar` | 151 | review: merge |
| `opensource` | `open source` | 151 | review: merge |
| `autoga` | `autogás` | 150 | review: merge |
| `cuentakilómetro` | `cuentakilómetros` | 150 | review: merge |
| `boletu` | `boletus` | 149 | review: merge |
| `alejándono` | `alejarse` | 147 | review: merge |
| `tiendetubo` | `tiendetubos` | 147 | review: merge |
| `standart` | `estándar` | 145 | review: merge |
| `contra-notificación` | `contranotificación` | 144 | review: merge |
| `pre-evento` | `preevento` | 144 | review: merge |
| `sisben` | `sisbén` | 144 | review: merge |
| `fué` | `ser` | 142 | review: merge |
| `henificadore` | `henificador` | 142 | review: merge |
| `arnica` | `árnica` | 140 | review: merge |
| `nodosa` | `nodoso` | 140 | review: merge |
| `reconciliarno` | `reconciliarse` | 140 | review: merge |
| `nnuu` | `onu` | 138 | review: merge |
| `interferometr` | `interferometría` | 137 | review: merge |
| `respondí` | `responder` | 137 | review: merge |
| `juntarno` | `juntarse` | 135 | review: merge |
| `diaspora` | `diáspora` | 134 | review: merge |
| `bíblia` | `biblia` | 133 | review: merge |
| `contraindicaciones` | `contraindicación` | 133 | review: merge |
| `auto-defensa` | `autodefensa` | 128 | review: merge |
| `hadith` | `hadiz` | 128 | review: merge |
| `multi-jugador` | `multijugador` | 127 | review: merge |
| `decidl#Fem` | `decir` | 126 | review: merge |
| `passiflora` | `pasiflora` | 126 | review: merge |
| `remoje` | `remojar` | 126 | review: merge |
| `viburnum` | `viburno` | 126 | review: merge |
| `beta-bloqueador` | `betabloqueador` | 125 | review: merge |
| `distraerno` | `distraerse` | 124 | review: merge |
| `siller` | `sillería` | 124 | review: merge |
| `pendientes` | `pendiente` | 13,322 | review: merge |
| `ayudarse` | `ayudar` | 9,014 | review: merge |
| `abstener` | `abstenerse` | 6,930 | review: merge |
| `silicón` | `silicona` | 4,554 | review: merge |
| `rielar` | `riel` | 3,132 | review: merge |
| `substituir` | `sustituir` | 1,960 | review: merge |
| `valles` | `valle` | 1,672 | review: merge |
| `podrir` | `pudrir` | 1,571 | review: merge |
| `aspar` | `aspa` | 1,500 | review: merge |
| `aposentar` | `aposento` | 1,377 | review: merge |
| `trasmisión` | `transmisión` | 1,154 | review: merge |
| `alambrar` | `alambrada` | 1,147 | review: merge |
| `gotita` | `gota` | 1,147 | review: merge |
| `cofinanciado` | `cofinanciar` | 932 | review: merge |
| `descabellar` | `descabellado` | 856 | review: merge |
| `cosido` | `coser` | 855 | review: merge |
| `cinchar` | `cincha` | 820 | review: merge |
| `confederar` | `confederado` | 817 | review: merge |
| `charolar` | `charola` | 746 | review: merge |
| `barrenar` | `barrena` | 727 | review: merge |
| `caracteristicas` | `característica` | 707 | review: merge |
| `fluidizado` | `fluidizar` | 686 | review: merge |
| `desdecir` | `desdicha` | 673 | review: merge |
| `recuestar` | `recostar` | 577 | review: merge |
| `aureolar` | `aureola` | 573 | review: merge |
| `anejar` | `anejo` | 509 | review: merge |
| `frisar` | `friso` | 509 | review: merge |
| `ahincar` | `ahínco` | 496 | review: merge |
| `best-seller` | `bestséller` | 488 | review: merge |
| `hacendar` | `hacendado` | 487 | review: merge |
| `rwandés` | `ruandés` | 477 | review: merge |
| `gangrenar` | `gangrena` | 444 | review: merge |
| `ulcerar` | `úlcera` | 433 | review: merge |
| `orillar` | `orillo` | 419 | review: merge |
| `intensión` | `intención` | 412 | review: merge |
| `sugestionar` | `sugestión` | 407 | review: merge |
| `medido` | `medida` | 403 | review: merge |
| `ovillar` | `ovillo` | 371 | review: merge |
| `eslálom` | `slalom` | 368 | review: merge |
| `artroscópica` | `artroscópico` | 361 | review: merge |
| `cohechar` | `cohecho` | 355 | review: merge |
| `blockchains` | `blockchain` | 336 | review: merge |
| `estipendiar` | `estipendio` | 336 | review: merge |
| `elijen` | `elegir` | 327 | review: merge |
| `construción` | `construcción` | 277 | review: merge |
| `afrutada` | `afrutado` | 311 | review: merge |
| `escondiéndose` | `esconderse` | 299 | review: merge |
| `oaxaqueña` | `oaxaqueño` | 297 | review: merge |
| `suéltelo` | `soltar` | 295 | review: merge |
| `blanqueadora` | `blanqueador` | 293 | review: merge |
| `chamánica` | `chamánico` | 287 | review: merge |
| `reinterpretando` | `reinterpretar` | 279 | review: merge |
| `madreper` | `madreperla` | 278 | review: merge |
| `entarimar` | `entarimado` | 275 | review: merge |
| `kaki` | `caqui` | 275 | review: merge |
| `crucifícalo` | `crucificar` | 274 | review: merge |
| `enmedio` | `en medio` | 268 | review: merge |
| `estrellita` | `estrella` | 262 | review: merge |
| `devela` | `develar` | 261 | review: merge |
| `abullonar` | `abullonado` | 260 | review: merge |
| `hoteler` | `hotelería` | 260 | review: merge |
| `prácticar` | `practicar` | 257 | review: merge |
| `prepagados` | `prepagado` | 255 | review: merge |
| `cambiarlo` | `cambiar` | 254 | review: merge |
| `hágalo` | `hacer` | 253 | review: merge |
| `seleciona` | `seleccionar` | 253 | review: merge |
| `hospédate` | `hospedarse` | 252 | review: merge |
| `acolchonar` | `acolchonado` | 249 | review: merge |
| `pequeñísimo` | `pequeño` | 249 | review: merge |
| `halogenar` | `halogenado` | 248 | review: merge |
| `equípate` | `equiparse` | 246 | review: merge |
| `oceáno` | `océano` | 245 | review: merge |
| `preciosísima` | `precioso` | 245 | review: merge |
| `espectativa` | `expectativa` | 244 | review: merge |
| `premenopáusicas` | `premenopáusico` | 241 | review: merge |
| `adaptándolo` | `adaptar` | 237 | review: merge |
| `bajísimo` | `bajo` | 236 | review: merge |
| `sueno` | `sueño` | 235 | review: merge |
| `bodie` | `body` | 233 | review: merge |
| `enlances` | `enlace` | 233 | review: merge |
| `dividiéndose` | `dividirse` | 230 | review: merge |
| `hámsteres` | `hámster` | 228 | review: merge |
| `metabolizado` | `metabolizar` | 228 | review: merge |
| `comedir` | `comedido` | 227 | review: merge |
| `ponla` | `poner` | 226 | review: merge |
| `despreocúpate` | `despreocuparse` | 225 | review: merge |
| `suscribiéndote` | `suscribirse` | 182 | review: merge |
| `masoner` | `masonería` | 223 | review: merge |
| `rohingyas` | `rohingya` | 220 | review: merge |
| `desvio` | `desvío` | 219 | review: merge |
| `relajándote` | `relajarse` | 212 | review: merge |
| `balinese` | `balinés` | 211 | review: merge |
| `metereológico` | `meteorológico` | 211 | review: merge |
| `albañiler` | `albañilería` | 210 | review: merge |
| `microempresas` | `microempresa` | 210 | review: merge |
| `translucir` | `translúcido` | 208 | review: merge |
| `propria` | `propio` | 206 | review: merge |
| `disrupciones` | `disrupción` | 205 | review: merge |
| `inovación` | `innovación` | 205 | review: merge |
| `enseñándole` | `enseñar` | 203 | review: merge |
| `violoncello` | `violonchelo` | 201 | review: merge |
| `kioskos` | `quiosco` | 200 | review: merge |
| `agréguenme` | `agregar` | 198 | review: merge |
| `cols` | `colaborador` | 197 | review: merge |
| `uniéndote` | `unirse` | 195 | review: merge |
| `androgenética` | `androgenético` | 193 | review: merge |
| `cilndro` | `cilindro` | 193 | review: merge |
| `dalits` | `dalit` | 193 | review: merge |
| `relojer` | `relojería` | 193 | review: merge |
| `stalinismo` | `estalinismo` | 193 | review: merge |
| `estadío` | `estadio` | 192 | review: merge |
| `minicargadoras` | `minicargadora` | 190 | review: merge |
| `arrástrela` | `arrastrar` | 188 | review: merge |
| `comprehensiva` | `comprehensivo` | 188 | review: merge |
| `portapieza` | `portapiezas` | 187 | review: merge |
| `infomación` | `información` | 186 | review: merge |
| `sinergía` | `sinergia` | 185 | review: merge |
| `porticada` | `porticado` | 184 | review: merge |
| `responsibilidad` | `responsabilidad` | 184 | review: merge |
| `habitacionales` | `habitacional` | 182 | review: merge |
| `hidraulica` | `hidráulica` | 180 | review: merge |
| `sitema` | `sistema` | 179 | review: merge |
| `exterminarlo` | `exterminar` | 178 | review: merge |
| `postea` | `postear` | 178 | review: merge |
| `quitadle` | `quitar` | 178 | review: merge |
| `afrocolombianas` | `afrocolombiano` | 177 | review: merge |
| `aplíquela` | `aplicar` | 177 | review: merge |
| `instalaciónes` | `instalación` | 176 | review: merge |
| `reacondicionada` | `reacondicionar` | 176 | review: merge |
| `androgénicas` | `androgénico` | 175 | review: merge |
| `teletransporta` | `teletransportar` | 174 | review: merge |
| `mamita` | `mamá` | 173 | review: merge |
| `desmedrar` | `desmedro` | 172 | review: merge |
| `eliminarla` | `eliminar` | 172 | review: merge |
| `tagalog` | `tagalo` | 171 | review: merge |
| `cogida` | `coger` | 170 | review: merge |
| `digámoslo` | `decir` | 170 | review: merge |
| `basandose` | `basarse` | 169 | review: merge |
| `exculparse` | `exculpar` | 169 | review: merge |
| `desbarajustar` | `desbarajuste` | 168 | review: merge |
| `kasbahs` | `casba` | 168 | review: merge |
| `podeís` | `poder` | 167 | review: merge |
| `externalizados` | `externalizar` | 166 | review: merge |
| `paramentar` | `paramento` | 166 | review: merge |
| `redecorado` | `redecorar` | 166 | review: merge |
| `fluído` | `fluido` | 165 | review: merge |
| `deslícese` | `deslizarse` | 164 | review: merge |
| `freaks` | `friki` | 164 | review: merge |
| `rapidito` | `rápido` | 164 | review: merge |
| `ché` | `che` | 163 | review: merge |
| `deltoid` | `deltoides` | 163 | review: merge |
| `giradisco` | `giradiscos` | 163 | review: merge |
| `refino` | `refinar` | 163 | review: merge |
| `siembrar` | `sembrar` | 163 | review: merge |
| `arponar` | `arpón` | 162 | review: merge |
| `brevísimo` | `breve` | 162 | review: merge |
| `revisita` | `revisitar` | 162 | review: merge |
| `sumérgela` | `sumergir` | 162 | review: merge |
| `cúbrala` | `cubrir` | 161 | review: merge |
| `guiarlo` | `guiar` | 161 | review: merge |
| `critico` | `crítico` | 159 | review: merge |
| `entregándole` | `entregar` | 159 | review: merge |
| `propriedade` | `propiedad` | 159 | review: merge |
| `texturada` | `texturado` | 159 | review: merge |
| `videir` | `video` | 159 | review: merge |
| `apártese` | `apartarse` | 158 | review: merge |
| `seguidle` | `seguir` | 157 | review: merge |
| `provedor` | `proveedor` | 156 | review: merge |
| `lobbista` | `lobista` | 155 | review: merge |
| `regálese` | `regalarse` | 155 | review: merge |
| `transformándo` | `transformar` | 155 | review: merge |
| `gob` | `gobierno` | 154 | review: merge |
| `príncipal` | `principal` | 154 | review: merge |
| `transplantar` | `trasplantar` | 154 | review: merge |
| `eléctronico` | `electrónico` | 152 | review: merge |
| `reconecta` | `reconectar` | 152 | review: merge |
| `comuníquenoslo` | `comunicar` | 151 | review: merge |
| `destruídas` | `destruir` | 151 | review: merge |
| `ganacia` | `ganancia` | 151 | review: merge |
| `acompañándola` | `acompañar` | 148 | review: merge |
| `keyloggers` | `keylogger` | 148 | review: merge |
| `rusticas` | `rústico` | 147 | review: merge |
| `persuadirlo` | `persuadir` | 146 | review: merge |
| `palado` | `palada` | 145 | review: merge |
| `apártense` | `apartarse` | 144 | review: merge |
| `ilegitimar` | `ilegítimo` | 144 | review: merge |
| `organofosforados` | `organofosforado` | 144 | review: merge |
| `palmita` | `palma` | 143 | review: merge |
| `quítelo` | `quitar` | 143 | review: merge |
| `acompáñalo` | `acompañar` | 142 | review: merge |
| `cualquie` | `cualquier` | 142 | review: merge |
| `desparecido` | `desaparecer` | 142 | review: merge |
| `mediúmnica` | `mediúmnico` | 142 | review: merge |
| `rohinyás` | `rohinyá` | 141 | review: merge |
| `telefonico` | `telefónico` | 141 | review: merge |
| `párrs` | `párrafo` | 140 | review: merge |
| `marrar` | `marras` | 139 | review: merge |
| `mochar` | `mocho` | 139 | review: merge |
| `uníos` | `unirse` | 139 | review: merge |
| `conyugue` | `cónyuge` | 138 | review: merge |
| `síquico` | `psíquico` | 138 | review: merge |
| `veintiuna` | `veintiuno` | 138 | review: merge |
| `bitcoines` | `bitcoin` | 137 | review: merge |
| `lasagna` | `lasaña` | 137 | review: merge |
| `targeta` | `tarjeta` | 137 | review: merge |
| `comuníquelo` | `comunicar` | 136 | review: merge |
| `estár` | `estar` | 136 | review: merge |
| `hospedándote` | `hospedarse` | 136 | review: merge |
| `integrarlas` | `integrar` | 136 | review: merge |
| `ministró` | `ministrar` | 136 | review: merge |
| `visítalo` | `visitar` | 104 | review: merge |
| `ellxs` | `ellos` | 134 | review: merge |
| `envolviéndolo` | `envolver` | 134 | review: merge |
| `melamine` | `melamina` | 134 | review: merge |
| `chaflanar` | `chaflán` | 133 | review: merge |
| `inmunodeprimidos` | `inmunodeprimido` | 133 | review: merge |
| `elimínela` | `eliminar` | 132 | review: merge |
| `estragar` | `estrago` | 131 | review: merge |
| `nandrolone` | `nandrolona` | 494 | review: merge |
| `indonesa` | `indonesio` | 335 | review: merge |
| `auto-organización` | `autoorganización` | 265 | review: merge |
| `harem` | `harén` | 261 | review: merge |
| `mini-nevera` | `mininevera` | 233 | review: merge |
| `noodl` | `noodles` | 230 | review: merge |
| `policias` | `policía` | 228 | review: merge |
| `echarl` | `echar` | 221 | review: merge |
| `músculo-esquelético` | `musculoesquelético` | 207 | review: merge |
| `incluímo` | `incluir` | 206 | review: merge |
| `seguidme` | `seguir` | 204 | review: merge |
| `encontrarl` | `encontrar` | 197 | review: merge |
| `checkin` | `check-in` | 189 | review: merge |
| `restaura` | `restaurar` | 188 | review: merge |
| `rezad` | `rezar` | 186 | review: merge |
| `ferreteria` | `ferretería` | 185 | review: merge |
| `socio-emocional` | `socioemocional` | 181 | review: merge |
| `alqueria` | `alquería` | 179 | review: merge |
| `introducirno` | `introducirse` | 173 | review: merge |
| `afiliadas` | `afiliado` | 171 | review: merge |
| `pídano` | `pedir` | 169 | review: merge |
| `semi-automático` | `semiautomático` | 169 | review: merge |
| `belladonna` | `belladona` | 167 | review: merge |
| `rimmel` | `rímel` | 165 | review: merge |
| `llámenos` | `llamar` | 164 | review: merge |
| `échal` | `echar` | 164 | review: merge |
| `geriatr` | `geriatría` | 153 | review: merge |
| `simetr` | `simetría` | 149 | review: merge |
| `cabochon` | `cabujón` | 145 | review: merge |
| `bi-direccional` | `bidireccional` | 144 | review: merge |
| `judeo-cristiana` | `judeocristiano` | 144 | review: merge |
| `preparao` | `prepararse` | 144 | review: merge |
| `cous` | `cuscús` | 72 | review: merge |
| `supón` | `suponer` | 143 | review: merge |
| `floristeria` | `floristería` | 141 | review: merge |
| `guiarl` | `guiar` | 140 | review: merge |
| `pasacabl` | `pasacables` | 140 | review: merge |
| `atacarno` | `atacar` | 138 | review: merge |
| `greco-romana` | `grecorromano` | 138 | review: merge |
| `recuerde` | `recordar` | 138 | review: merge |
| `prospera` | `prosperar` | 137 | review: merge |
| `semi-transparente` | `semitransparente` | 135 | review: merge |
| `cerebro-vascular` | `cerebrovascular` | 134 | review: merge |
| `responderl` | `responder` | 134 | review: merge |
| `taino` | `taíno` | 134 | review: merge |
| `afro-americana` | `afroamericano` | 132 | review: merge |
| `surjan` | `surgir` | 132 | review: merge |
| `esquie` | `esquí` | 129 | review: merge |
| `visitándono` | `visitar` | 129 | review: merge |
| `micro-sd` | `microsd` | 128 | review: merge |
| `brindándono` | `brindar` | 127 | review: merge |
| `peritado` | `peritar` | 126 | review: merge |
| `ultra-ligero` | `ultraligero` | 126 | review: merge |
| `auto-estudio` | `autoestudio` | 125 | review: merge |
| `replicabl` | `replicable` | 125 | review: merge |
| `alojarno` | `alojarse` | 124 | review: merge |
| `pre-construcción` | `preconstrucción` | 124 | review: merge |
| `bobinar` | `bobina` | 4,292 | review: merge |
| `desproporcionar` | `desproporcionado` | 3,969 | review: merge |
| `alcantarillar` | `alcantarillado` | 3,731 | review: merge |
| `dobladillar` | `dobladillo` | 3,652 | review: merge |
| `cascar` | `cascada` | 3,606 | review: merge |
| `dentar` | `dentado` | 3,435 | review: merge |
| `diluviar` | `diluvio` | 3,328 | review: merge |
| `escarpar` | `escarpado` | 3,272 | review: merge |
| `elevadora` | `elevador` | 3,169 | review: merge |
| `recordarse` | `recordar` | 3,080 | review: merge |
| `bolsita` | `bolsa` | 2,409 | review: merge |
| `jalear` | `jalea` | 2,217 | review: merge |
| `murar` | `morir` | 1,598 | review: merge |
| `tétano` | `tétanos` | 1,506 | review: merge |
| `descalzar` | `descalzo` | 1,377 | review: merge |
| `llamado` | `llamada` | 1,161 | review: merge |
| `rosáceo` | `rosácea` | 1,126 | review: merge |
| `portaherramienta` | `portaherramientas` | 1,011 | review: merge |
| `leguminoso` | `leguminosa` | 994 | review: merge |
| `substituto` | `sustituto` | 941 | review: merge |
| `archidiócesis` | `arquidiócesis` | 939 | review: merge |
| `teneis` | `tener` | 757 | review: merge |
| `esputar` | `esputo` | 746 | review: merge |
| `microcosmo` | `microcosmos` | 714 | review: merge |
| `atarear` | `atareado` | 656 | review: merge |
| `habeis` | `haber` | 568 | review: merge |
| `creatura` | `criatura` | 550 | review: merge |
| `niñito` | `niño` | 512 | review: merge |
| `pulimentar` | `pulimento` | 510 | review: merge |
| `ahijar` | `ahijado` | 462 | review: merge |
| `lidio` | `lidia` | 449 | review: merge |
| `lavarropa` | `lavarropas` | 387 | review: merge |
| `eclíptico` | `eclíptica` | 380 | review: merge |
| `piedrecita` | `piedra` | 374 | review: merge |
| `proporcionándote` | `proporcionar` | 352 | review: merge |
| `kiosko` | `quiosco` | 351 | review: merge |
| `consejer` | `consejería` | 344 | review: merge |
| `sunitas` | `sunita` | 343 | review: merge |
| `ojito` | `ojo` | 341 | review: merge |
| `pedicure` | `pedicura` | 339 | review: merge |
| `chenille` | `chenilla` | 327 | review: merge |
| `eléctrica` | `eléctrico` | 327 | review: merge |
| `podreis` | `poder` | 324 | review: merge |
| `gravísimo` | `grave` | 323 | review: merge |
| `enramar` | `enramada` | 319 | review: merge |
| `mímico` | `mímica` | 274 | review: merge |
| `hospédese` | `hospedarse` | 302 | review: merge |
| `liquido` | `líquido` | 298 | review: merge |
| `recicladores` | `reciclador` | 296 | review: merge |
| `protegiéndola` | `proteger` | 294 | review: merge |
| `rimel` | `rímel` | 291 | review: merge |
| `chequee` | `chequear` | 289 | review: merge |
| `hidraulico` | `hidráulico` | 286 | review: merge |
| `twitteado` | `tuitear` | 276 | review: merge |
| `extruidos` | `extruido` | 273 | review: merge |
| `neumocócica` | `neumocócico` | 273 | review: merge |
| `santificaos` | `santificar` | 257 | review: merge |
| `sofas` | `sofá` | 255 | review: merge |
| `ultramoderna` | `ultramoderno` | 254 | review: merge |
| `agroecológicas` | `agroecológico` | 249 | review: merge |
| `dexamethasone` | `dexametasona` | 249 | review: merge |
| `corset` | `corsé` | 248 | review: merge |
| `milimétricas` | `milimétrico` | 248 | review: merge |
| `famíla` | `familia` | 247 | review: merge |
| `altivar` | `altivo` | 245 | review: merge |
| `prepintada` | `prepintado` | 245 | review: merge |
| `concluído` | `concluido` | 242 | review: merge |
| `pregrabados` | `pregrabado` | 242 | review: merge |
| `tersar` | `terso` | 241 | review: merge |
| `reproduciéndose` | `reproducirse` | 240 | review: merge |
| `cúbralo` | `cubrir` | 239 | review: merge |
| `periurbana` | `periurbano` | 239 | review: merge |
| `brindándote` | `brindar` | 233 | review: merge |
| `reciprocar` | `recíproco` | 233 | review: merge |
| `rectar` | `recta` | 232 | review: merge |
| `mostrarlo` | `mostrar` | 229 | review: merge |
| `salita` | `sala` | 229 | review: merge |
| `móbil` | `móvil` | 228 | review: merge |
| `telf` | `teléfono` | 224 | review: merge |
| `gratuíto` | `gratuito` | 221 | review: merge |
| `puntación` | `puntuación` | 221 | review: merge |
| `devolviéndole` | `devolver` | 219 | review: merge |
| `paquetito` | `paquete` | 219 | review: merge |
| `soldadito` | `soldado` | 219 | review: merge |
| `estadistica` | `estadística` | 218 | review: merge |
| `matadlo` | `matar` | 218 | review: merge |
| `descubir` | `descubrir` | 216 | review: merge |
| `série` | `serie` | 213 | review: merge |
| `renders` | `render` | 212 | review: merge |
| `barrar` | `barrado` | 211 | review: merge |
| `animatronic` | `animatrónico` | 210 | review: merge |
| `gruesar` | `grueso` | 210 | review: merge |
| `inscribiéndose` | `inscribirse` | 210 | review: merge |
| `suscribiéndose` | `suscribirse` | 210 | review: merge |
| `deseleccione` | `deseleccionar` | 209 | review: merge |
| `equipaciones` | `equipación` | 208 | review: merge |
| `rapidísima` | `rápido` | 205 | review: merge |
| `ampli` | `amplificador` | 203 | review: merge |
| `acoplándolo` | `acoplar` | 201 | review: merge |
| `methotrexate` | `metotrexato` | 201 | review: merge |
| `díficil` | `difícil` | 200 | review: merge |
| `cebollita` | `cebolla` | 198 | review: merge |
| `descatalogados` | `descatalogado` | 198 | review: merge |
| `experencia` | `experiencia` | 198 | review: merge |
| `nanotube` | `nanotubo` | 198 | review: merge |
| `preinstalados` | `preinstalado` | 197 | review: merge |
| `anabólica` | `anabólico` | 192 | review: merge |
| `shampoos` | `champú` | 192 | review: merge |
| `encripción` | `encriptación` | 191 | review: merge |
| `bioclimáticas` | `bioclimático` | 190 | review: merge |
| `viéndola` | `ver` | 190 | review: merge |
| `tattoos` | `tatuaje` | 188 | review: merge |
| `atrévase` | `atreverse` | 186 | review: merge |
| `elastane` | `elastano` | 186 | review: merge |
| `separadora` | `separador` | 186 | review: merge |
| `zapar` | `zapatilla` | 186 | review: merge |
| `papita` | `papa` | 183 | review: merge |
| `regocíjense` | `regocijarse` | 183 | review: merge |
| `acompañándolo` | `acompañar` | 182 | review: merge |
| `malls` | `mall` | 182 | review: merge |
| `periódo` | `período` | 182 | review: merge |
| `interesantísima` | `interesante` | 181 | review: merge |
| `tazo` | `taza` | 181 | review: merge |
| `vinotecas` | `vinoteca` | 180 | review: merge |
| `añádalo` | `añadir` | 179 | review: merge |
| `ríete` | `reírse` | 178 | review: merge |
| `guardadlo` | `guardar` | 177 | review: merge |
| `añadió` | `añadir` | 175 | review: merge |
| `puden` | `poder` | 175 | review: merge |
| `distópica` | `distópico` | 174 | review: merge |
| `identitarias` | `identitario` | 174 | review: merge |
| `deshabilite` | `deshabilitar` | 171 | review: merge |
| `malhumorar` | `malhumorado` | 171 | review: merge |
| `aimar` | `aimara` | 170 | review: merge |
| `semanita` | `semana` | 170 | review: merge |
| `realize` | `realizar` | 169 | review: merge |
| `zoonóticas` | `zoonótico` | 169 | review: merge |
| `especiadas` | `especiado` | 168 | review: merge |
| `córtelo` | `cortar` | 167 | review: merge |
| `neuropsicológicas` | `neuropsicológico` | 167 | review: merge |
| `ahórrese` | `ahorrar` | 130 | review: merge |
| `pastorcito` | `pastor` | 166 | review: merge |
| `nitroglycerin` | `nitroglicerina` | 165 | review: merge |
| `pelito` | `pelo` | 165 | review: merge |
| `smileys` | `smiley` | 165 | review: merge |
| `démosle` | `dar` | 164 | review: merge |
| `explíquele` | `explicar` | 164 | review: merge |
| `servidle` | `servir` | 164 | review: merge |
| `voilá` | `voilà` | 164 | review: merge |
| `kernels` | `kernel` | 162 | review: merge |
| `mendocina` | `mendocino` | 162 | review: merge |
| `prebendar` | `prebenda` | 162 | review: merge |
| `coproducida` | `coproducir` | 161 | review: merge |
| `torito` | `toro` | 161 | review: merge |
| `computerizada` | `computerizado` | 160 | review: merge |
| `habitac` | `habitación` | 160 | review: merge |
| `huskie` | `husky` | 160 | review: merge |
| `pasaro` | `pasar` | 160 | review: merge |
| `molesta` | `molesto` | 158 | review: merge |
| `obtenlo` | `obtener` | 158 | review: merge |
| `karaokes` | `karaoke` | 157 | review: merge |
| `priesa` | `prisa` | 157 | review: merge |
| `reinterpretan` | `reinterpretar` | 157 | review: merge |
| `companía` | `compañía` | 156 | review: merge |
| `estaran` | `estar` | 156 | review: merge |
| `semiárida` | `semiárido` | 156 | review: merge |
| `habitacio` | `habitación` | 155 | review: merge |
| `vírgen` | `virgen` | 155 | review: merge |
| `camiónes` | `camión` | 154 | review: merge |
| `identifíquese` | `identificarse` | 154 | review: merge |
| `mirándola` | `mirar` | 154 | review: merge |
| `lowcost` | `low cost` | 153 | review: merge |
| `benzocaine` | `benzocaína` | 152 | review: merge |
| `diríjanse` | `dirigirse` | 152 | review: merge |
| `redirige` | `redirigir` | 152 | review: merge |
| `naproxen` | `naproxeno` | 151 | review: merge |
| `reconfigurado` | `reconfigurar` | 151 | review: merge |
| `empoderada` | `empoderado` | 149 | review: merge |
| `adenomatosa` | `adenomatoso` | 148 | review: merge |
| `sostenlo` | `sostener` | 148 | review: merge |
| `asiatica` | `asiático` | 147 | review: merge |
| `kayac` | `kayak` | 147 | review: merge |
| `sustituyéndolo` | `sustituir` | 147 | review: merge |
| `veranito` | `verano` | 147 | review: merge |
| `bolsito` | `bolso` | 146 | review: merge |
| `cómprala` | `comprar` | 146 | review: merge |
| `desestacionalizada` | `desestacionalizado` | 146 | review: merge |
| `hidración` | `hidratación` | 146 | review: merge |
| `deciembre` | `diciembre` | 145 | review: merge |
| `facetadas` | `facetado` | 145 | review: merge |
| `mashups` | `mashup` | 145 | review: merge |
| `báñate` | `bañarse` | 144 | review: merge |
| `cheesecakes` | `cheesecake` | 144 | review: merge |
| `conversoras` | `conversor` | 144 | review: merge |
| `rembolso` | `reembolso` | 144 | review: merge |
| `licua` | `licuar` | 143 | review: merge |
| `sabiéndolo` | `saber` | 143 | review: merge |
| `desenrolladoras` | `desenrolladora` | 141 | review: merge |
| `sastrer` | `sastrería` | 141 | review: merge |
| `desdentar` | `desdentado` | 140 | review: merge |
| `exponiéndose` | `exponerse` | 140 | review: merge |
| `explicarle` | `explicar` | 139 | review: merge |
| `mujeres` | `mujer` | 139 | review: merge |
| `dóblala` | `doblar` | 137 | review: merge |
| `enseñárselo` | `enseñar` | 137 | review: merge |
| `gamification` | `gamificación` | 137 | review: merge |
| `geoestratégica` | `geoestratégico` | 136 | review: merge |
| `típo` | `tipo` | 136 | review: merge |
| `bolshevique` | `bolchevique` | 135 | review: merge |
| `hase` | `haber` | 135 | review: merge |
| `fontaneria` | `fontanería` | 134 | review: merge |
| `libérese` | `liberarse` | 134 | review: merge |
| `applicación` | `aplicación` | 133 | review: merge |
| `autodenomina` | `autodenominarse` | 133 | review: merge |
| `inténtalo` | `intentar` | 133 | review: merge |
| `mapeados` | `mapear` | 133 | review: merge |
| `pasamanar` | `pasamano` | 132 | review: merge |
| `ñoquis` | `ñoqui` | 132 | review: merge |
| `abuelita` | `abuelo` | 846 | review: merge |
| `sacapunta` | `sacapuntas` | 495 | review: merge |
| `navegue` | `navegar` | 461 | review: merge |
| `pua` | `púa` | 282 | review: merge |
| `construya` | `construir` | 251 | review: merge |
| `manzanita` | `manzana` | 249 | review: merge |
| `austro-húngaro` | `austrohúngaro` | 243 | review: merge |
| `pruébelo` | `probar` | 242 | review: merge |
| `seca-toallas` | `secatoallas` | 224 | review: merge |
| `practico` | `práctico` | 223 | review: merge |
| `auto-adhesivo` | `autoadhesivo` | 219 | review: merge |
| `anti-corrosión` | `anticorrosión` | 213 | review: merge |
| `anti-estática` | `antiestático` | 212 | review: merge |
| `performers` | `performer` | 211 | review: merge |
| `peridot` | `peridoto` | 209 | review: merge |
| `salvaescalera` | `salvaescaleras` | 200 | review: merge |
| `rectángular` | `rectangular` | 197 | review: merge |
| `pre-reserva` | `prerreserva` | 193 | review: merge |
| `megaciudade` | `megaciudad` | 190 | review: merge |
| `recordándol` | `recordar` | 190 | review: merge |
| `ayudándol` | `ayudar` | 185 | review: merge |
| `metr` | `metro` | 185 | review: merge |
| `yoes` | `yo` | 180 | review: merge |
| `rajador` | `rajadora` | 173 | review: merge |
| `habilite` | `habilitar` | 170 | review: merge |
| `nicks` | `nick` | 168 | review: merge |
| `off-shore` | `offshore` | 167 | review: merge |
| `píceo` | `pícea` | 166 | review: merge |
| `auto-confianza` | `autoconfianza` | 165 | review: merge |
| `cápit#Maac` | `cápita` | 165 | review: merge |
| `informándono` | `informar` | 165 | review: merge |
| `insertabl` | `insertable` | 164 | review: merge |
| `multi-canal` | `multicanal` | 163 | review: merge |
| `pirifor` | `piriforme` | 163 | review: merge |
| `asociarno` | `asociarse` | 162 | review: merge |
| `indemnizarno` | `indemnizar` | 161 | review: merge |
| `d-os` | `dios` | 159 | review: merge |
| `post-guerra` | `posguerra` | 158 | review: merge |
| `anti-imperialista` | `antiimperialista` | 156 | review: merge |
| `chiffon` | `chifón` | 156 | review: merge |
| `multi-nivel` | `multinivel` | 155 | review: merge |
| `co-working` | `coworking` | 154 | review: merge |
| `créeme` | `creer` | 154 | review: merge |
| `pásate` | `pasarse` | 154 | review: merge |
| `advirtiéndol` | `advertir` | 153 | review: merge |
| `anti-inflamatoria` | `antiinflamatorio` | 153 | review: merge |
| `pre-aprobación` | `preaprobación` | 152 | review: merge |
| `amoladoras` | `amoladora` | 151 | review: merge |
| `punitivos` | `punitivo` | 150 | review: merge |
| `resulten` | `resultar` | 150 | review: merge |
| `calabacero` | `calabacera` | 149 | review: merge |
| `atenderl` | `atender` | 146 | review: merge |
| `commentarios` | `comentario` | 145 | review: merge |
| `anis` | `anís` | 144 | review: merge |
| `llamándono` | `llamar` | 143 | review: merge |
| `ciudadciudad` | `ciudad` | 141 | review: merge |
| `factoria` | `factoría` | 141 | review: merge |
| `semi-estructurada` | `semiestructurado` | 140 | review: merge |
| `identificativos` | `identificativo` | 139 | review: merge |
| `auto-descubrimiento` | `autodescubrimiento` | 138 | review: merge |
| `muar` | `muaré` | 138 | review: merge |
| `alter-ego` | `alter ego` | 136 | review: merge |
| `respóndeme` | `responder` | 136 | review: merge |
| `camióne` | `camión` | 133 | review: merge |
| `sub-licenciar` | `sublicenciar` | 133 | review: merge |
| `arriendos` | `arriendo` | 132 | review: merge |
| `open-source` | `open source` | 132 | review: merge |
| `reunámono` | `reunirse` | 132 | review: merge |
| `volvámono` | `volverse` | 132 | review: merge |
| `mullah` | `mulá` | 131 | review: merge |
| `durian` | `durián` | 130 | review: merge |
| `post-mortem` | `post mortem` | 130 | review: merge |
| `pornostars` | `pornostar` | 129 | review: merge |
| `bafl` | `bafle` | 128 | review: merge |
| `grupales` | `grupal` | 127 | review: merge |
| `auto-guiado` | `autoguiado` | 126 | review: merge |
| `teletranspor` | `teletransporte` | 126 | review: merge |
| `impidiéndol` | `impedir` | 124 | review: merge |
| `asegurarl` | `asegurar` | 123 | review: merge |
| `salivar` | `saliva` | 4,632 | review: merge |
| `balizar` | `baliza` | 3,735 | review: merge |
| `sillita` | `silla` | 3,435 | review: merge |
| `perrito` | `perro` | 3,121 | review: merge |
| `parachoque` | `parachoques` | 3,071 | review: merge |
| `ornamentar` | `ornamento` | 3,038 | review: merge |
| `entramar` | `entramado` | 2,905 | review: merge |
| `perchar` | `percha` | 2,791 | review: merge |
| `combar` | `combo` | 2,767 | review: merge |
| `revistar` | `revestir` | 2,691 | review: merge |
| `poseído` | `poseer` | 2,339 | review: merge |
| `mechar` | `mecha` | 2,299 | review: merge |
| `descarar` | `descarado` | 2,148 | review: merge |
| `abovedar` | `abovedado` | 2,048 | review: merge |
| `ensilar` | `ensilado` | 2,025 | review: merge |
| `federar` | `federado` | 1,940 | review: merge |
| `punzonar` | `punzonado` | 1,764 | review: merge |
| `recidivar` | `recidiva` | 1,689 | review: merge |
| `recocer` | `recocido` | 1,674 | review: merge |
| `perturbado` | `perturbar` | 1,188 | review: merge |
| `autodidacto` | `autodidacta` | 1,106 | review: merge |
| `mellar` | `mella` | 827 | review: merge |
| `orejero` | `orejera` | 781 | review: merge |
| `rapiñar` | `rapiña` | 756 | review: merge |
| `herrumbrar` | `herrumbre` | 716 | review: merge |
| `ciar` | `cian` | 643 | review: merge |
| `serigrafiado` | `serigrafiar` | 571 | review: merge |
| `trasformar` | `transformar` | 555 | review: merge |
| `mestizar` | `mestizo` | 554 | review: merge |
| `pirar` | `pira` | 511 | review: merge |
| `substitución` | `sustitución` | 502 | review: merge |
| `servico` | `servicio` | 397 | review: merge |
| `neoyorkino` | `neoyorquino` | 389 | review: merge |
| `eléct` | `eléctrico` | 376 | review: merge |
| `gravísima` | `grave` | 371 | review: merge |
| `diviértete` | `divertirse` | 351 | review: merge |
| `macarons` | `macaron` | 351 | review: merge |
| `aparecido` | `aparecer` | 350 | review: merge |
| `escuadrar` | `escuadra` | 339 | review: merge |
| `insulin` | `insulina` | 334 | review: merge |
| `autosómica` | `autosómico` | 332 | review: merge |
| `mandrilar` | `mandril` | 329 | review: merge |
| `precargados` | `precargado` | 326 | review: merge |
| `ibuprofen` | `ibuprofeno` | 321 | review: merge |
| `cervecer` | `cervecería` | 293 | review: merge |
| `emoticon` | `emoticono` | 292 | review: merge |
| `solido` | `sólido` | 284 | review: merge |
| `endocannabinoid` | `endocannabinoide` | 283 | review: merge |
| `arbequino` | `arbequina` | 280 | review: merge |
| `consultación` | `consulta` | 279 | review: merge |
| `apropriado` | `apropiado` | 277 | review: merge |
| `posiblidad` | `posibilidad` | 275 | review: merge |
| `tramontano` | `tramontana` | 268 | review: merge |
| `vidio` | `vídeo` | 266 | review: merge |
| `añádelas` | `añadir` | 265 | review: merge |
| `cintur` | `cinturón` | 263 | review: merge |
| `subscríbase` | `suscribir` | 186 | review: merge |
| `obstetras` | `obstetra` | 250 | review: merge |
| `píxels` | `píxel` | 250 | review: merge |
| `tascar` | `tasca` | 247 | review: merge |
| `enviá` | `enviar` | 243 | review: merge |
| `rastrojar` | `rastrojo` | 243 | review: merge |
| `embárquese` | `embarcarse` | 240 | review: merge |
| `absteniéndose` | `abstenerse` | 239 | review: merge |
| `pararrayo` | `pararrayos` | 238 | review: merge |
| `trols` | `trol` | 234 | review: merge |
| `mipymes` | `mipyme` | 233 | review: merge |
| `pasteler` | `pastelería` | 233 | review: merge |
| `recuérdele` | `recordar` | 233 | review: merge |
| `digitizadores` | `digitalizador` | 232 | review: merge |
| `recuérdese` | `recordar` | 232 | review: merge |
| `argamasar` | `argamasa` | 228 | review: merge |
| `rechazarla` | `rechazar` | 228 | review: merge |
| `preconfigurada` | `preconfigurar` | 227 | review: merge |
| `desclasificados` | `desclasificado` | 223 | review: merge |
| `bochar` | `bocha` | 221 | review: merge |
| `história` | `historia` | 220 | review: merge |
| `microfilm` | `microfilme` | 220 | review: merge |
| `applets` | `applet` | 218 | review: merge |
| `pandear` | `pandeo` | 216 | review: merge |
| `traédmelo` | `traer` | 216 | review: merge |
| `demonstrar` | `demostrar` | 214 | review: merge |
| `ascención` | `ascensión` | 211 | review: merge |
| `clama` | `clamar` | 209 | review: merge |
| `develó` | `develar` | 209 | review: merge |
| `mostro` | `mostrar` | 209 | review: merge |
| `siquiente` | `siguiente` | 207 | review: merge |
| `calcetar` | `calceta` | 205 | review: merge |
| `informacin` | `información` | 204 | review: merge |
| `raspones` | `raspón` | 202 | review: merge |
| `dirigiéndote` | `dirigirse` | 201 | review: merge |
| `ahhh` | `ah` | 200 | review: merge |
| `dipositivo` | `dispositivo` | 199 | review: merge |
| `enjuágalo` | `enjuagar` | 199 | review: merge |
| `hematite` | `hematita` | 199 | review: merge |
| `cierrapuerta` | `cierrapuertas` | 196 | review: merge |
| `coriónicas` | `coriónico` | 194 | review: merge |
| `introduciéndose` | `introducirse` | 194 | review: merge |
| `abrazader` | `abrazadera` | 193 | review: merge |
| `debiéndose` | `deberse` | 192 | review: merge |
| `conviértanse` | `convertirse` | 190 | review: merge |
| `vuélvete` | `volverse` | 189 | review: merge |
| `posteando` | `postear` | 188 | review: merge |
| `unío` | `unirse` | 188 | review: merge |
| `apor` | `aporte` | 187 | review: merge |
| `ayurvédicas` | `ayurvédico` | 186 | review: merge |
| `buro` | `buró` | 185 | review: merge |
| `psicoactiva` | `psicoactivo` | 185 | review: merge |
| `melar` | `melé` | 184 | review: merge |
| `semipreciosa` | `semiprecioso` | 184 | review: merge |
| `atadla` | `atar` | 183 | review: merge |
| `frótalo` | `frotar` | 183 | review: merge |
| `globulin` | `globulina` | 182 | review: merge |
| `intrahospitalaria` | `intrahospitalario` | 181 | review: merge |
| `subaguda` | `subagudo` | 181 | review: merge |
| `desactualizadas` | `desactualizado` | 177 | review: merge |
| `oxycodone` | `oxicodona` | 177 | review: merge |
| `escarolar` | `escarola` | 176 | review: merge |
| `irisar` | `irisado` | 176 | review: merge |
| `lascar` | `lasca` | 176 | review: merge |
| `regimenes` | `régimen` | 176 | review: merge |
| `separándola` | `separar` | 176 | review: merge |
| `tenerlo` | `tener` | 176 | review: merge |
| `catequética` | `catequético` | 175 | review: merge |
| `notícia` | `noticia` | 174 | review: merge |
| `pistar` | `pisto` | 174 | review: merge |
| `comodísimos` | `cómodo` | 173 | review: merge |
| `espitar` | `espita` | 173 | review: merge |
| `ultraelevada` | `ultraelevado` | 173 | review: merge |
| `córtela` | `cortar` | 172 | review: merge |
| `agregá` | `agregar` | 171 | review: merge |
| `fibroid` | `fibroide` | 171 | review: merge |
| `sonrosar` | `sonrosado` | 171 | review: merge |
| `técnología` | `tecnología` | 171 | review: merge |
| `reemplácelo` | `reemplazar` | 170 | review: merge |
| `lavarlo` | `lavar` | 168 | review: merge |
| `tuitea` | `tuitear` | 168 | review: merge |
| `bolsitas` | `bolsita` | 167 | review: merge |
| `sevicio` | `servicio` | 167 | review: merge |
| `debia` | `deber` | 166 | review: merge |
| `cliqueando` | `cliquear` | 165 | review: merge |
| `enseriar` | `serio` | 164 | review: merge |
| `promociónes` | `promoción` | 164 | review: merge |
| `remanufacturados` | `remanufacturar` | 164 | review: merge |
| `apróximadamente` | `aproximadamente` | 163 | review: merge |
| `bajísima` | `bajo` | 163 | review: merge |
| `divertidísima` | `divertido` | 163 | review: merge |
| `kirguisa` | `kirguís` | 163 | review: merge |
| `fotorrealistas` | `fotorrealista` | 162 | review: merge |
| `garantir` | `garantizar` | 161 | review: merge |
| `conectándolo` | `conectar` | 160 | review: merge |
| `escuelita` | `escuela` | 160 | review: merge |
| `júrame` | `jurar` | 160 | review: merge |
| `monobloc` | `monobloque` | 159 | review: merge |
| `timpo` | `tiempo` | 159 | review: merge |
| `escencia` | `esencia` | 158 | review: merge |
| `storyboards` | `storyboard` | 158 | review: merge |
| `buenísimo` | `bueno` | 157 | review: merge |
| `confiriéndole` | `conferir` | 157 | review: merge |
| `comprueba` | `comprobar` | 156 | review: merge |
| `separada` | `separado` | 156 | review: merge |
| `subtitulo` | `subtítulo` | 156 | review: merge |
| `empalizar` | `empalizada` | 155 | review: merge |
| `esforzándome` | `esforzarse` | 155 | review: merge |
| `mojonar` | `mojón` | 154 | review: merge |
| `tántricas` | `tántrico` | 154 | review: merge |
| `elijes` | `elegir` | 153 | review: merge |
| `piés` | `pie` | 153 | review: merge |
| `palosanto` | `palo santo` | 151 | review: merge |
| `escudillar` | `escudilla` | 150 | review: merge |
| `entrenimiento` | `entretenimiento` | 149 | review: merge |
| `texana` | `texano` | 149 | review: merge |
| `estírate` | `estirarse` | 148 | review: merge |
| `restaurarlo` | `restaurar` | 148 | review: merge |
| `abonador` | `abonadora` | 147 | review: merge |
| `demonstración` | `demostración` | 147 | review: merge |
| `kazaja` | `kazajo` | 147 | review: merge |
| `desición` | `decisión` | 115 | review: merge |
| `gestionarlas` | `gestionar` | 146 | review: merge |
| `farmaceutico` | `farmacéutico` | 145 | review: merge |
| `santificadora` | `santificador` | 145 | review: merge |
| `baneado` | `banear` | 144 | review: merge |
| `cajilla` | `caja` | 144 | review: merge |
| `copatrocinado` | `copatrocinar` | 144 | review: merge |
| `brujer` | `brujería` | 143 | review: merge |
| `redireccionando` | `redireccionar` | 143 | review: merge |
| `sobrecito` | `sobre` | 143 | review: merge |
| `recordá` | `recordar` | 142 | review: merge |
| `amiguita` | `amigo` | 141 | review: merge |
| `buscadme` | `buscar` | 141 | review: merge |
| `deslícelo` | `deslizar` | 141 | review: merge |
| `snob` | `esnob` | 141 | review: merge |
| `ámplio` | `amplio` | 141 | review: merge |
| `alabadle` | `alabar` | 140 | review: merge |
| `fucus` | `fuco` | 140 | review: merge |
| `quipo` | `quipu` | 140 | review: merge |
| `tuiteando` | `tuitear` | 140 | review: merge |
| `centrándome` | `centrarse` | 139 | review: merge |
| `dóblalo` | `doblar` | 139 | review: merge |
| `combínelo` | `combinar` | 138 | review: merge |
| `warrants` | `warrant` | 137 | review: merge |
| `deejay` | `dj` | 136 | review: merge |
| `destiler` | `destilería` | 135 | review: merge |
| `eléctricas` | `eléctrico` | 135 | review: merge |
| `notifíque` | `notificar` | 135 | review: merge |
| `posteó` | `postear` | 135 | review: merge |
| `embolismar` | `embolismo` | 134 | review: merge |
| `frótala` | `frotar` | 134 | review: merge |
| `rinoplastía` | `rinoplastia` | 134 | review: merge |
| `estaciónes` | `estación` | 133 | review: merge |
| `iodo` | `yodo` | 133 | review: merge |
| `pasamaner` | `pasamanería` | 132 | review: merge |
| `podais` | `poder` | 132 | review: merge |
| `randomizado` | `aleatorizado` | 132 | review: merge |
| `customizadas` | `customizado` | 131 | review: merge |
| `epóxica` | `epóxico` | 131 | review: merge |
| `pio` | `pío` | 1,380 | review: merge |
| `cerrito` | `cerro` | 1,324 | review: merge |
| `fenix` | `fénix` | 1,269 | review: merge |
| `basándonos` | `basarse` | 1,165 | review: merge |
| `hibiscus` | `hibisco` | 456 | review: merge |
| `kilogram` | `kilogramo` | 354 | review: merge |
| `pedid` | `pedir` | 322 | review: merge |
| `mini-golf` | `minigolf` | 293 | review: merge |
| `sangr` | `sangría` | 279 | review: merge |
| `multi-idioma` | `multiidioma` | 274 | review: merge |
| `borosilicate` | `borosilicato` | 265 | review: merge |
| `suministrados` | `suministrar` | 246 | review: merge |
| `inflatabl` | `inflable` | 242 | review: merge |
| `recuerden` | `recordar` | 241 | review: merge |
| `rgdp` | `rgpd` | 232 | review: merge |
| `rellena` | `rellenar` | 221 | review: merge |
| `avecilla` | `ave` | 217 | review: merge |
| `comprometerno` | `comprometerse` | 211 | review: merge |
| `vermouth` | `vermut` | 211 | review: merge |
| `hadice` | `hadiz` | 210 | review: merge |
| `enseñaro` | `enseñar` | 206 | review: merge |
| `cazatalento` | `cazatalentos` | 205 | review: merge |
| `acompañarl` | `acompañar` | 199 | review: merge |
| `desearl` | `desear` | 196 | review: merge |
| `planetarium` | `planetario` | 196 | review: merge |
| `hamman` | `hammam` | 192 | review: merge |
| `multiplicao` | `multiplicarse` | 192 | review: merge |
| `pre-instalado` | `preinstalado` | 191 | review: merge |
| `amoxicillin` | `amoxicilina` | 190 | review: merge |
| `panaderías` | `panadería` | 187 | review: merge |
| `mistica` | `mística` | 181 | review: merge |
| `arra` | `arras` | 178 | review: merge |
| `sacad` | `sacar` | 178 | review: merge |
| `panna` | `panna cotta` | 175 | review: merge |
| `vehicu` | `vehículo` | 173 | review: merge |
| `anticiparno` | `anticiparse` | 172 | review: merge |
| `deseándol` | `desear` | 170 | review: merge |
| `pre-registro` | `preregistro` | 168 | review: merge |
| `aupair` | `au pair` | 167 | review: merge |
| `gehenna` | `gehena` | 167 | review: merge |
| `bbdd` | `base de datos` | 166 | review: merge |
| `cód` | `código` | 166 | review: merge |
| `ibérica` | `ibérico` | 166 | review: merge |
| `semi-remolque` | `semirremolque` | 163 | review: merge |
| `omisiones` | `omisión` | 162 | review: merge |
| `pre-lanzamiento` | `prelanzamiento` | 158 | review: merge |
| `adentrándono` | `adentrarse` | 157 | review: merge |
| `bodies` | `body` | 155 | review: merge |
| `muéstrame` | `mostrar` | 153 | review: merge |
| `re-creación` | `recreación` | 153 | review: merge |
| `fluo` | `fluorescente` | 151 | review: merge |
| `hermanoshermano` | `hermano` | 149 | review: merge |
| `aventurino` | `aventurina` | 148 | review: merge |
| `garantizándol` | `garantizar` | 147 | review: merge |
| `infórmele` | `informar` | 147 | review: merge |
| `multi-usuario` | `multiusuario` | 147 | review: merge |
| `post-industrial` | `postindustrial` | 147 | review: merge |
| `seguirno` | `seguir` | 146 | review: merge |
| `enfocándono` | `enfocarse` | 145 | review: merge |
| `unirno` | `unirse` | 145 | review: merge |
| `anti-capitalista` | `anticapitalista` | 144 | review: merge |
| `iaea` | `aiea` | 144 | review: merge |
| `glbt` | `lgbt` | 142 | review: merge |
| `subespecialidade` | `subespecialidad` | 142 | review: merge |
| `tetracycline` | `tetraciclina` | 141 | review: merge |
| `post-cosecha` | `poscosecha` | 139 | review: merge |
| `auto-disciplina` | `autodisciplina` | 138 | review: merge |
| `ultra-rápido` | `ultrarrápido` | 138 | review: merge |
| `diagnostico` | `diagnóstico` | 137 | review: merge |
| `tragus` | `trago` | 137 | review: merge |
| `amiloid` | `amiloide` | 136 | review: merge |
| `mahjongg` | `mahjong` | 136 | review: merge |
| `post-secundaria` | `postsecundaria` | 136 | review: merge |
| `fuchsia` | `fucsia` | 132 | review: merge |
| `multi-uso` | `multiuso` | 131 | review: merge |
| `guardamuebl` | `guardamuebles` | 130 | review: merge |
| `practicum` | `prácticum` | 130 | review: merge |
| `cuasi-experimental` | `cuasiexperimental` | 129 | review: merge |
| `post-consumo` | `posconsumo` | 129 | review: merge |
| `decima` | `décima` | 128 | review: merge |
| `in-vitro` | `in vitro` | 128 | review: merge |
| `auto-renovación` | `autorrenovación` | 126 | review: merge |
| `pre-kinder` | `prekínder` | 126 | review: merge |
| `devociona` | `devocional` | 125 | review: merge |
| `imprimirlo` | `imprimir` | 124 | review: merge |
| `audiometr` | `audiometría` | 123 | review: merge |
| `seleccionado` | `seleccionar` | 46,392 | review: merge |
| `agregado` | `agregar` | 17,528 | review: merge |
| `solear` | `soleado` | 7,222 | review: merge |
| `contrachapar` | `contrachapado` | 4,326 | review: merge |
| `malentender` | `malentendido` | 2,310 | review: merge |
| `subscribir` | `suscribir` | 1,899 | review: merge |
| `subscripción` | `suscripción` | 1,890 | review: merge |
| `pontificar` | `pontificado` | 1,579 | review: merge |
| `almidonar` | `almidón` | 1,156 | review: merge |
| `dinamitar` | `dinamita` | 1,000 | review: merge |
| `alar` | `alado` | 979 | review: merge |
| `envie` | `enviar` | 957 | review: merge |
| `tuno` | `tuna` | 918 | review: merge |
| `deberia` | `deber` | 789 | review: merge |
| `reunen` | `reunir` | 510 | review: merge |
| `cámping` | `camping` | 492 | review: merge |
| `descampar` | `descampado` | 491 | review: merge |
| `obscurecer` | `oscurecer` | 445 | review: merge |
| `stalinista` | `estalinista` | 418 | review: merge |
| `menudear` | `menudeo` | 398 | review: merge |
| `quilómetro` | `kilómetro` | 376 | review: merge |
| `arcillar` | `arcilla` | 368 | review: merge |
| `inspirándose` | `inspirarse` | 356 | review: merge |
| `resinar` | `resina` | 338 | review: merge |
| `quereis` | `querer` | 326 | review: merge |
| `maleficiar` | `maleficio` | 324 | review: merge |
| `cocinita` | `cocina` | 321 | review: merge |
| `completísimo` | `completo` | 320 | review: merge |
| `trovar` | `trova` | 318 | review: merge |
| `maño` | `maña` | 311 | review: merge |
| `jabonero` | `jabonera` | 306 | review: merge |
| `chatee` | `chatear` | 303 | review: merge |
| `dumper` | `dúmper` | 302 | review: merge |
| `contrucción` | `construcción` | 234 | review: merge |
| `terracita` | `terraza` | 301 | review: merge |
| `acessorio` | `accesorio` | 294 | review: merge |
| `zoster` | `zóster` | 293 | review: merge |
| `llevándote` | `llevar` | 291 | review: merge |
| `crística` | `crístico` | 281 | review: merge |
| `probióticas` | `probiótico` | 280 | review: merge |
| `afrutadas` | `afrutado` | 276 | review: merge |
| `quejas` | `queja` | 276 | review: merge |
| `personalízalo` | `personalizar` | 220 | review: merge |
| `tonar` | `tonada` | 270 | review: merge |
| `escencial` | `esencial` | 264 | review: merge |
| `reprogramado` | `reprogramar` | 264 | review: merge |
| `escápese` | `escaparse` | 263 | review: merge |
| `indigena` | `indígena` | 260 | review: merge |
| `preclínica` | `preclínico` | 260 | review: merge |
| `regocíjate` | `regocijarse` | 257 | review: merge |
| `tercerizado` | `tercerizar` | 257 | review: merge |
| `intraoperatoria` | `intraoperatorio` | 256 | review: merge |
| `plater` | `platería` | 256 | review: merge |
| `multicámar` | `multicámara` | 254 | review: merge |
| `qualquier` | `cualquier` | 254 | review: merge |
| `crucifícale` | `crucificar` | 247 | review: merge |
| `electromágnetica` | `electromagnético` | 246 | review: merge |
| `metil` | `metilo` | 246 | review: merge |
| `pasteleria` | `pastelería` | 244 | review: merge |
| `acercándose` | `acercarse` | 239 | review: merge |
| `margar` | `marga` | 239 | review: merge |
| `evacua` | `evacuar` | 235 | review: merge |
| `sisar` | `sisa` | 235 | review: merge |
| `cabestrar` | `cabestro` | 233 | review: merge |
| `avisadme` | `avisar` | 232 | review: merge |
| `mallar` | `mallado` | 232 | review: merge |
| `enrutado` | `enrutar` | 230 | review: merge |
| `glamurosas` | `glamuroso` | 230 | review: merge |
| `entiéndase` | `entender` | 227 | review: merge |
| `tupi` | `tupí` | 227 | review: merge |
| `sigua` | `seguir` | 222 | review: merge |
| `desacertar` | `desacertado` | 219 | review: merge |
| `mantram` | `mantra` | 217 | review: merge |
| `facilitarle` | `facilitar` | 216 | review: merge |
| `júntense` | `juntar` | 216 | review: merge |
| `desionizada` | `desionizado` | 214 | review: merge |
| `flexográficas` | `flexográfico` | 214 | review: merge |
| `maldecido` | `maldecir` | 213 | review: merge |
| `difrutar` | `disfrutar` | 212 | review: merge |
| `crupiers` | `crupier` | 210 | review: merge |
| `importantísimos` | `importante` | 209 | review: merge |
| `nuve` | `nube` | 208 | review: merge |
| `enruta` | `enrutar` | 207 | review: merge |
| `hazlo` | `hacer` | 206 | review: merge |
| `weblogs` | `weblog` | 206 | review: merge |
| `gurdo` | `gurda` | 205 | review: merge |
| `bendíceme` | `bendecir` | 204 | review: merge |
| `famosísimo` | `famoso` | 202 | review: merge |
| `boolean` | `booleano` | 200 | review: merge |
| `oleo` | `óleo` | 200 | review: merge |
| `doctrinar` | `doctrina` | 199 | review: merge |
| `hidrolipídica` | `hidrolipídico` | 199 | review: merge |
| `postmoderna` | `postmoderno` | 199 | review: merge |
| `pomeranio` | `pomerania` | 198 | review: merge |
| `smartwatche` | `smartwatch` | 196 | review: merge |
| `transtorno` | `trastorno` | 195 | review: merge |
| `clinicas` | `clínica` | 194 | review: merge |
| `informándote` | `informar` | 192 | review: merge |
| `reacondicionadas` | `reacondicionado` | 192 | review: merge |
| `cunar` | `cuna` | 191 | review: merge |
| `copita` | `copa` | 190 | review: merge |
| `disponde` | `disponer` | 189 | review: merge |
| `laborear` | `laboreo` | 189 | review: merge |
| `menúes` | `menú` | 189 | review: merge |
| `personalízala` | `personalizar` | 189 | review: merge |
| `cepíllese` | `cepillarse` | 188 | review: merge |
| `interiorizado` | `interiorizar` | 188 | review: merge |
| `despídete` | `despedirse` | 186 | review: merge |
| `escojer` | `escoger` | 186 | review: merge |
| `jamaiquina` | `jamaiquino` | 186 | review: merge |
| `sofware` | `software` | 186 | review: merge |
| `cancerar` | `cáncer` | 185 | review: merge |
| `diviertete` | `divertirse` | 185 | review: merge |
| `viejita` | `viejo` | 185 | review: merge |
| `preprogramados` | `preprogramado` | 182 | review: merge |
| `insercciones` | `inserción` | 180 | review: merge |
| `cronica` | `crónica` | 179 | review: merge |
| `sacándo` | `sacar` | 179 | review: merge |
| `yihada` | `yihad` | 179 | review: merge |
| `sojuzgadla` | `sojuzgar` | 178 | review: merge |
| `empieze` | `empezar` | 177 | review: merge |
| `traedlo` | `traer` | 177 | review: merge |
| `incluydo` | `incluir` | 176 | review: merge |
| `teasers` | `teaser` | 175 | review: merge |
| `shells` | `shell` | 174 | review: merge |
| `estadisticas` | `estadística` | 173 | review: merge |
| `redirigen` | `redirigir` | 173 | review: merge |
| `coloraciónes` | `coloración` | 172 | review: merge |
| `fintar` | `finta` | 172 | review: merge |
| `asóciese` | `asociarse` | 169 | review: merge |
| `imaginaos` | `imaginarse` | 169 | review: merge |
| `quédense` | `quedarse` | 169 | review: merge |
| `renderiza` | `renderizar` | 169 | review: merge |
| `acojedor` | `acogedor` | 168 | review: merge |
| `bioactivas` | `bioactivo` | 168 | review: merge |
| `habitaci` | `habitación` | 168 | review: merge |
| `chiquitito` | `chiquito` | 167 | review: merge |
| `hijita` | `hijo` | 167 | review: merge |
| `fantacia` | `fantasía` | 166 | review: merge |
| `mískito` | `miskito` | 166 | review: merge |
| `pregúntenle` | `preguntar` | 166 | review: merge |
| `quantidad` | `cantidad` | 166 | review: merge |
| `hosteleria` | `hostelería` | 165 | review: merge |
| `testosterone` | `testosterona` | 165 | review: merge |
| `entendiéndolo` | `entender` | 164 | review: merge |
| `lucecita` | `luz` | 164 | review: merge |
| `sobrescriben` | `sobrescribir` | 164 | review: merge |
| `danado` | `dañado` | 163 | review: merge |
| `ummah` | `umma` | 163 | review: merge |
| `infrarojo` | `infrarrojo` | 162 | review: merge |
| `placita` | `plaza` | 162 | review: merge |
| `cuartito` | `cuarto` | 161 | review: merge |
| `anodinar` | `anodino` | 160 | review: merge |
| `consejeria` | `consejería` | 160 | review: merge |
| `aceso` | `acceso` | 159 | review: merge |
| `masturbandose` | `masturbarse` | 159 | review: merge |
| `papeler` | `papelería` | 159 | review: merge |
| `omeprazole` | `omeprazol` | 158 | review: merge |
| `historiar` | `historia` | 157 | review: merge |
| `probiótica` | `probiótico` | 157 | review: merge |
| `telefóno` | `teléfono` | 157 | review: merge |
| `automóbil` | `automóvil` | 156 | review: merge |
| `gratuíta` | `gratuito` | 156 | review: merge |
| `mixes` | `mix` | 156 | review: merge |
| `anonimiza` | `anonimizar` | 155 | review: merge |
| `escusa` | `excusa` | 154 | review: merge |
| `muestreado` | `muestrear` | 154 | review: merge |
| `vistiéndose` | `vestirse` | 154 | review: merge |
| `distinguiéndose` | `distinguirse` | 153 | review: merge |
| `pedrer` | `pedrería` | 152 | review: merge |
| `matrizar` | `matriz` | 151 | review: merge |
| `ateniéndose` | `atenerse` | 150 | review: merge |
| `abiertar` | `abierto` | 149 | review: merge |
| `cualquiero` | `cualquiera` | 149 | review: merge |
| `deslícela` | `deslizar` | 149 | review: merge |
| `premiaciones` | `premiación` | 149 | review: merge |
| `quántica` | `cuántica` | 149 | review: merge |
| `vertir` | `verter` | 149 | review: merge |
| `eternalmente` | `eternamente` | 148 | review: merge |
| `propuesto` | `propuesta` | 148 | review: merge |
| `soufflé` | `suflé` | 148 | review: merge |
| `desplazándote` | `desplazarse` | 147 | review: merge |
| `mapeando` | `mapear` | 147 | review: merge |
| `abónese` | `abonarse` | 146 | review: merge |
| `borrarlas` | `borrar` | 146 | review: merge |
| `coladuria` | `coladuría` | 146 | review: merge |
| `dcha` | `derecha` | 146 | review: merge |
| `enfrie` | `enfriar` | 146 | review: merge |
| `vencerlo` | `vencer` | 146 | review: merge |
| `abuhardillada` | `abuhardillado` | 145 | review: merge |
| `cebollines` | `cebollín` | 145 | review: merge |
| `suscribite` | `suscribir` | 145 | review: merge |
| `distribuídos` | `distribuir` | 144 | review: merge |
| `inscripta` | `inscribir` | 144 | review: merge |
| `museísticas` | `museístico` | 144 | review: merge |
| `tambi` | `también` | 144 | review: merge |
| `biopelículas` | `biopelícula` | 143 | review: merge |
| `reemplácela` | `reemplazar` | 143 | review: merge |
| `tapita` | `tapa` | 143 | review: merge |
| `vivenda` | `vivienda` | 143 | review: merge |
| `construídas` | `construir` | 142 | review: merge |
| `enfocándote` | `enfocarse` | 142 | review: merge |
| `rejuvenecedoras` | `rejuvenecedor` | 142 | review: merge |
| `dirigiéndolo` | `dirigir` | 141 | review: merge |
| `ecográfica` | `ecográfico` | 141 | review: merge |
| `monoinsaturados` | `monoinsaturado` | 141 | review: merge |
| `quiéres` | `querer` | 141 | review: merge |
| `acompáñame` | `acompañar` | 140 | review: merge |
| `avatars` | `avatar` | 139 | review: merge |
| `comenzá` | `comenzar` | 107 | review: merge |
| `develando` | `develar` | 138 | review: merge |
| `visibiliza` | `visibilizar` | 138 | review: merge |
| `chamánicas` | `chamánico` | 137 | review: merge |
| `prendedle` | `prender` | 137 | review: merge |
| `brókers` | `bróker` | 136 | review: merge |
| `conspirativa` | `conspirativo` | 136 | review: merge |
| `laparoscópicas` | `laparoscópico` | 136 | review: merge |
| `mezclándola` | `mezclar` | 136 | review: merge |
| `multipar` | `multiparte` | 136 | review: merge |
| `deséchelo` | `desechar` | 135 | review: merge |
| `laxar` | `laxo` | 135 | review: merge |
| `enamorarme` | `enamorarse` | 134 | review: merge |
| `etáreo` | `etario` | 133 | review: merge |
| `trombocitopénica` | `trombocitopénico` | 133 | review: merge |
| `adelántate` | `adelantarse` | 132 | review: merge |
| `clomiphene` | `clomifeno` | 132 | review: merge |
| `comuníquense` | `comunicarse` | 132 | review: merge |
| `amantísima` | `amante` | 481 | review: merge |
| `bajísimos` | `bajo` | 107 | review: merge |
| `buenísima` | `bueno` | 119 | review: merge |
| `comodísimo` | `cómodo` | 200 | review: merge |
| `conocidísimo` | `conocido` | 105 | review: merge |
| `divertidísimos` | `divertido` | 107 | review: merge |
| `durísimas` | `duro` | 96 | review: merge |
| `elegantísima` | `elegante` | 97 | review: merge |
| `elevadísima` | `elevado` | 130 | review: merge |
| `elevadísimo` | `elevado` | 97 | review: merge |
| `esperadísima` | `esperado` | 102 | review: merge |
| `esperadísimo` | `esperado` | 110 | review: merge |
| `facilísima` | `fácil` | 94 | review: merge |
| `fortísimo` | `fuerte` | 166 | review: merge |
| `guapísimo` | `guapo` | 127 | review: merge |
| `jovencísimo` | `joven` | 128 | review: merge |
| `larguísimas` | `largo` | 122 | review: merge |
| `lindísimo` | `lindo` | 103 | review: merge |
| `monísima` | `mono` | 94 | review: merge |
| `personalísimo` | `personal` | 102 | review: merge |
| `potentísimo` | `potente` | 107 | review: merge |
| `preciosísimo` | `precioso` | 102 | review: merge |
| `queridísimo` | `querido` | 137 | review: merge |
| `rarísima` | `raro` | 94 | review: merge |
| `rarísimo` | `raro` | 94 | review: merge |
| `tantísimas` | `tanto` | 101 | review: merge |
| `tantísimo` | `tanto` | 213 | review: merge |
| `valiosísima` | `valioso` | 198 | review: merge |
| `multi-propósito` | `multipropósito` | 123 | review: merge |
| `ashkenazi` | `asquenazí` | 122 | review: merge |
| `entregándol` | `entregar` | 122 | review: merge |
| `check-ins` | `check-in` | 121 | review: merge |
| `insitu` | `in situ` | 121 | review: merge |
| `geo-localización` | `geolocalización` | 120 | review: merge |
| `especifique` | `especificar` | 119 | review: merge |
| `pelacabl` | `pelacables` | 119 | review: merge |
| `congregarno` | `congregarse` | 118 | review: merge |
| `gorrita` | `gorra` | 118 | review: merge |
| `hobbits` | `hobbit` | 118 | review: merge |
| `monorail` | `monorraíl` | 118 | review: merge |
| `all-inclusive` | `all inclusive` | 117 | review: merge |
| `hypervisor` | `hipervisor` | 117 | review: merge |
| `sirviéndol` | `servir` | 117 | review: merge |
| `dañinos` | `dañino` | 116 | review: merge |
| `l-tirosina` | `tirosina` | 116 | review: merge |
| `reinventarno` | `reinventarse` | 116 | review: merge |
| `solicitarl` | `solicitar` | 116 | review: merge |
| `esperándono` | `esperar` | 115 | review: merge |
| `manténgala` | `mantener` | 115 | review: merge |
| `oxfords` | `oxford` | 115 | review: merge |
| `prednisone` | `prednisona` | 115 | review: merge |
| `transpaletas` | `transpaleta` | 115 | review: merge |
| `co-productor` | `coproductor` | 114 | review: merge |
| `pre-inscripción` | `preinscripción` | 114 | review: merge |
| `costo-efectivo` | `costoefectivo` | 113 | review: merge |
| `kungfu` | `kung-fu` | 113 | review: merge |
| `anti-desgaste` | `antidesgaste` | 112 | review: merge |
| `pidan` | `pedir` | 112 | review: merge |
| `anti-reflectante` | `antirreflectante` | 111 | review: merge |
| `l-triptófano` | `triptófano` | 111 | review: merge |
| `lychee` | `lichi` | 111 | review: merge |
| `cuneifor` | `cuneiforme` | 110 | review: merge |
| `sanarno` | `sanar` | 110 | review: merge |
| `arawak` | `arahuaco` | 108 | review: merge |
| `auto-sacrificio` | `autosacrificio` | 108 | review: merge |
| `ilocalizab` | `ilocalizable` | 108 | review: merge |
| `sub-grupo` | `subgrupo` | 108 | review: merge |
| `greco-romano` | `grecorromano` | 107 | review: merge |
| `invócalo` | `invocar` | 107 | review: merge |
| `luces` | `luz` | 107 | review: merge |
| `materail` | `material` | 107 | review: merge |
| `re-evaluación` | `reevaluación` | 107 | review: merge |
| `semi-abierta` | `semiabierto` | 107 | review: merge |
| `mudanzas` | `mudanza` | 106 | review: merge |
| `rapper` | `rapero` | 106 | review: merge |
| `comuníqueno` | `comunicar` | 105 | review: merge |
| `contadno` | `contar` | 105 | review: merge |
| `micro-momento` | `micromomento` | 105 | review: merge |
| `otorrinos` | `otorrino` | 105 | review: merge |
| `cilíndricos` | `cilíndrico` | 104 | review: merge |
| `negarl` | `negar` | 104 | review: merge |
| `riads` | `riad` | 104 | review: merge |
| `carrousel` | `carrusel` | 103 | review: merge |
| `guadalupana` | `guadalupano` | 103 | review: merge |
| `illegal` | `ilegal` | 103 | review: merge |
| `aah` | `ah` | 102 | review: merge |
| `auto-organizado` | `autoorganizado` | 102 | review: merge |
| `beta-glucano` | `betaglucano` | 102 | review: merge |
| `semi-acabado` | `semiacabado` | 102 | review: merge |
| `socio-sanitario` | `sociosanitario` | 102 | review: merge |
| `barbeque` | `barbacoa` | 101 | review: merge |
| `exhortándo` | `exhortar` | 101 | review: merge |
| `revelarl` | `revelar` | 101 | review: merge |
| `sacerdotessacerdote` | `sacerdote` | 101 | review: merge |
| `ciclocros` | `ciclocrós` | 100 | review: merge |
| `conéctese` | `conectarse` | 100 | review: merge |
| `diós` | `dios` | 100 | review: merge |
| `sorprenderno` | `sorprenderse` | 100 | review: merge |
| `ultra-rápida` | `ultrarrápido` | 100 | review: merge |
| `avambrazos` | `avambrazo` | 99 | review: merge |
| `pre-ordenar` | `preordenar` | 98 | review: merge |
| `tocarno` | `tocar` | 98 | review: merge |
| `licenciatarios` | `licenciatario` | 97 | review: merge |
| `semi-preciosas` | `semiprecioso` | 97 | review: merge |
| `chil` | `chile` | 96 | review: merge |
| `judeo-cristiano` | `judeocristiano` | 96 | review: merge |
| `leerl` | `leer` | 96 | review: merge |
| `ahorit` | `ahorita` | 95 | review: merge |
| `auto-observación` | `autoobservación` | 95 | review: merge |
| `poniéndol` | `poner` | 95 | review: merge |
| `pre-orden` | `preorden` | 95 | review: merge |
| `amándono` | `amar` | 94 | review: merge |
| `caloria` | `caloría` | 94 | review: merge |
| `champagn#Fem` | `champán` | 94 | review: merge |
| `narró` | `narrar` | 94 | review: merge |
| `no-violento` | `no violento` | 94 | review: merge |
| `tiempo-real` | `tiempo real` | 94 | review: merge |
| `búsquelo` | `buscar` | 130 | review: merge |
| `emtricitabine` | `emtricitabina` | 130 | review: merge |
| `sobrescribió` | `sobrescribir` | 130 | review: merge |
| `échalo` | `echar` | 130 | review: merge |
| `desapasionar` | `desapasionado` | 129 | review: merge |
| `meperidine` | `meperidina` | 129 | review: merge |
| `tambié` | `también` | 129 | review: merge |
| `cerrajeria` | `cerrajería` | 128 | review: merge |
| `estands` | `estand` | 128 | review: merge |
| `preprogramadas` | `preprogramado` | 128 | review: merge |
| `enfrentarlas` | `enfrentar` | 127 | review: merge |
| `salvarla` | `salvar` | 127 | review: merge |
| `botitas` | `botita` | 126 | review: merge |
| `diciéndote` | `decir` | 126 | review: merge |
| `harmonioso` | `armonioso` | 126 | review: merge |
| `reprogramada` | `reprogramar` | 126 | review: merge |
| `rocíalo` | `rociar` | 126 | review: merge |
| `hallándole` | `hallar` | 125 | review: merge |
| `payé` | `payés` | 125 | review: merge |
| `anágena` | `anágeno` | 124 | review: merge |
| `viajá` | `viajar` | 124 | review: merge |
| `animistas` | `animista` | 123 | review: merge |
| `bollito` | `bollo` | 123 | review: merge |
| `encantarar` | `encantar` | 123 | review: merge |
| `fresquitas` | `fresquito` | 123 | review: merge |
| `subnutridas` | `subnutrido` | 123 | review: merge |
| `comienze` | `comenzar` | 122 | review: merge |
| `encamar` | `encamado` | 122 | review: merge |
| `introduciéndolo` | `introducir` | 122 | review: merge |
| `warfarin` | `warfarina` | 122 | review: merge |
| `boligrafos` | `bolígrafo` | 121 | review: merge |
| `conectándola` | `conectar` | 121 | review: merge |
| `pregrabadas` | `pregrabado` | 121 | review: merge |
| `reconecte` | `reconectar` | 121 | review: merge |
| `adecua` | `adecuar` | 120 | review: merge |
| `cofinanciadas` | `cofinanciar` | 120 | review: merge |
| `enlistó` | `enlistar` | 120 | review: merge |
| `europalets` | `europalet` | 120 | review: merge |
| `flaccidez` | `flacidez` | 120 | review: merge |
| `polcar` | `polca` | 120 | review: merge |
| `produción` | `producción` | 120 | review: merge |
| `retroiluminadas` | `retroiluminado` | 120 | review: merge |
| `sáquele` | `sacar` | 120 | review: merge |
| `aprovechá` | `aprovechar` | 119 | review: merge |
| `estádio` | `estadio` | 119 | review: merge |
| `furgónes` | `furgón` | 119 | review: merge |
| `hiriéndolo` | `herir` | 119 | review: merge |
| `integrándolo` | `integrar` | 119 | review: merge |
| `sandio` | `sandía` | 119 | review: merge |
| `aquellxs` | `aquel` | 118 | review: merge |
| `bioga` | `biogás` | 118 | review: merge |
| `implicita` | `implícito` | 118 | review: merge |
| `multifacéticas` | `multifacético` | 118 | review: merge |
| `pañito` | `paño` | 118 | review: merge |
| `selecionar` | `seleccionar` | 118 | review: merge |
| `tiramisu` | `tiramisú` | 118 | review: merge |
| `ususario` | `usuario` | 118 | review: merge |
| `rápidez` | `rapidez` | 117 | review: merge |
| `desparecer` | `desaparecer` | 116 | review: merge |
| `osteopática` | `osteopático` | 116 | review: merge |
| `piénsese` | `pensar` | 116 | review: merge |
| `retroalimentan` | `retroalimentar` | 116 | review: merge |
| `ruína` | `ruina` | 116 | review: merge |
| `semicubierta` | `semicubierto` | 116 | review: merge |
| `industría` | `industria` | 115 | review: merge |
| `substraer` | `sustraer` | 115 | review: merge |
| `bautizándola` | `bautizar` | 114 | review: merge |
| `cormor` | `cormorán` | 114 | review: merge |
| `disfrútelo` | `disfrutar` | 114 | review: merge |
| `mímate` | `mimar` | 114 | review: merge |
| `nuetra` | `nuestro` | 114 | review: merge |
| `rumorar` | `rumorear` | 114 | review: merge |
| `vitrocerámicas` | `vitrocerámica` | 114 | review: merge |
| `cabuchones` | `cabuchón` | 113 | review: merge |
| `escúchenlo` | `escuchar` | 113 | review: merge |
| `soltándolo` | `soltar` | 113 | review: merge |
| `taimar` | `taimado` | 113 | review: merge |
| `toples` | `topless` | 113 | review: merge |
| `describiéndolo` | `describir` | 112 | review: merge |
| `gánate` | `ganarse` | 112 | review: merge |
| `opci` | `opción` | 112 | review: merge |
| `translación` | `traslación` | 112 | review: merge |
| `álter` | `alter ego` | 112 | review: merge |
| `frequencia` | `frecuencia` | 111 | review: merge |
| `gobernancia` | `gobernanza` | 111 | review: merge |
| `acyclovir` | `aciclovir` | 110 | review: merge |
| `besitos` | `besito` | 110 | review: merge |
| `extrafuer` | `extrafuerte` | 110 | review: merge |
| `homofóbica` | `homofóbico` | 110 | review: merge |
| `mezclándolo` | `mezclar` | 110 | review: merge |
| `mostrarno` | `mostrar` | 110 | review: merge |
| `porteria` | `portería` | 110 | review: merge |
| `artculo` | `artículo` | 109 | review: merge |
| `avisor` | `aviso` | 109 | review: merge |
| `buggys` | `buggy` | 109 | review: merge |
| `contruido` | `construir` | 109 | review: merge |
| `esforzándote` | `esforzarse` | 109 | review: merge |
| `princípio` | `principio` | 109 | review: merge |
| `retroalimenta` | `retroalimentar` | 109 | review: merge |
| `bivouac` | `vivac` | 108 | review: merge |
| `ecoturísticas` | `ecoturístico` | 108 | review: merge |
| `fideliza` | `fidelizar` | 108 | review: merge |
| `microfinancieras` | `microfinanciero` | 108 | review: merge |
| `márgen` | `margen` | 108 | review: merge |
| `conociéndolo` | `conocer` | 107 | review: merge |
| `permean` | `permear` | 107 | review: merge |
| `reinvertido` | `reinvertir` | 107 | review: merge |
| `smarttv` | `smart tv` | 107 | review: merge |
| `sosténgalo` | `sostener` | 107 | review: merge |
| `dulcer` | `dulcería` | 106 | review: merge |
| `lasreseñas` | `reseña` | 106 | review: merge |
| `previsualiza` | `previsualizar` | 106 | review: merge |
| `romanticas` | `romántico` | 106 | review: merge |
| `stilettos` | `stiletto` | 106 | review: merge |
| `succione` | `succionar` | 106 | review: merge |
| `suspención` | `suspensión` | 106 | review: merge |
| `averígualo` | `averiguar` | 105 | review: merge |
| `calientita` | `caliente` | 105 | review: merge |
| `examinarlas` | `examinar` | 105 | review: merge |
| `patchouli` | `pachulí` | 105 | review: merge |
| `suéltala` | `soltar` | 105 | review: merge |
| `anyo` | `año` | 104 | review: merge |
| `difundiéndose` | `difundirse` | 104 | review: merge |
| `disenada` | `diseñar` | 104 | review: merge |
| `mesias` | `mesías` | 104 | review: merge |
| `rescribir` | `reescribir` | 104 | review: merge |
| `flúida` | `fluido` | 103 | review: merge |
| `parejita` | `pareja` | 103 | review: merge |
| `poltrón` | `poltrona` | 103 | review: merge |
| `sitioweb` | `sitio web` | 103 | review: merge |
| `estaci` | `estación` | 102 | review: merge |
| `inspirándome` | `inspirarse` | 102 | review: merge |
| `pasandolo` | `pasar` | 102 | review: merge |
| `sacudiéndose` | `sacudirse` | 102 | review: merge |
| `trasportado` | `transportar` | 102 | review: merge |
| `vinculo` | `vínculo` | 102 | review: merge |
| `anímale` | `animar` | 101 | review: merge |
| `entrénate` | `entrenarse` | 101 | review: merge |
| `indicándole` | `indicar` | 101 | review: merge |
| `tomarlo` | `tomar` | 101 | review: merge |
| `bancarizados` | `bancarizado` | 100 | review: merge |
| `mezlador` | `mezclador` | 100 | review: merge |
| `aparencia` | `apariencia` | 99 | review: merge |
| `pequeo` | `pequeño` | 99 | review: merge |
| `resturante` | `restaurante` | 99 | review: merge |
| `romperla` | `romper` | 99 | review: merge |
| `automedicar` | `automedicarse` | 98 | review: merge |
| `ministr` | `ministrar` | 123 | review: merge |
| `terracotta` | `terracota` | 123 | review: merge |
| `concediéndol` | `conceder` | 122 | review: merge |
| `detengámono` | `detenerse` | 122 | review: merge |
| `geckos` | `gecko` | 122 | review: merge |
| `greco-católica` | `grecocatólico` | 122 | review: merge |
| `mini-crucero` | `minicrucero` | 122 | review: merge |
| `glucosamine` | `glucosamina` | 121 | review: merge |
| `geyser` | `géiser` | 120 | review: merge |
| `kaftan` | `caftán` | 120 | review: merge |
| `multi-cultural` | `multicultural` | 120 | review: merge |
| `regocijémono` | `regocijarse` | 120 | review: merge |
| `gujarati` | `guyaratí` | 119 | review: merge |
| `preguntándol` | `preguntar` | 118 | review: merge |
| `vestibl` | `vestible` | 118 | review: merge |
| `anti-vibración` | `antivibración` | 117 | review: merge |
| `establecida` | `establecido` | 117 | review: merge |
| `proveerl` | `proveer` | 116 | review: merge |
| `socio-laboral` | `sociolaboral` | 116 | review: merge |
| `bifida` | `bífido` | 115 | review: merge |
| `comparta` | `compartir` | 115 | review: merge |
| `d-manosa` | `manosa` | 114 | review: merge |
| `nylón` | `nailon` | 114 | review: merge |
| `chaga` | `chagas` | 113 | review: merge |
| `cromatograf` | `cromatografía` | 113 | review: merge |
| `restaure` | `restaurar` | 113 | review: merge |
| `art-deco` | `art déco` | 112 | review: merge |
| `avatara` | `avatar` | 112 | review: merge |
| `deshacerno` | `deshacerse` | 112 | review: merge |
| `moissanite` | `moissanita` | 112 | review: merge |
| `todo-incluido` | `todo incluido` | 112 | review: merge |
| `auto-aprendizaje` | `autoaprendizaje` | 111 | review: merge |
| `eco-diseño` | `ecodiseño` | 111 | review: merge |
| `hotspots` | `hotspot` | 111 | review: merge |
| `capitalo` | `capital` | 110 | review: merge |
| `terrino` | `terrina` | 110 | review: merge |
| `bungy` | `bungee` | 109 | review: merge |
| `l-leucina` | `leucina` | 109 | review: merge |
| `strip-tease` | `striptease` | 109 | review: merge |
| `anti-inmigración` | `antiinmigración` | 108 | review: merge |
| `arthritis` | `artritis` | 108 | review: merge |
| `despuésdespués` | `después` | 108 | review: merge |
| `eximirno` | `eximir` | 106 | review: merge |
| `hermanohermano` | `hermano` | 106 | review: merge |
| `proveyéndol` | `proveer` | 106 | review: merge |
| `pre-diabete` | `prediabetes` | 105 | review: merge |
| `viruse` | `virus` | 105 | review: merge |
| `compuestos` | `compuesto` | 104 | review: merge |
| `conectándono` | `conectarse` | 104 | review: merge |
| `pinup` | `pin-up` | 104 | review: merge |
| `co-directora` | `codirectora` | 103 | review: merge |
| `robarl` | `robar` | 103 | review: merge |
| `ofrecero` | `ofrecer` | 102 | review: merge |
| `aclare` | `aclarar` | 100 | review: merge |
| `ayatollah` | `ayatolá` | 100 | review: merge |
| `minipimer` | `minipímer` | 100 | review: merge |
| `negamos` | `negar` | 100 | review: merge |
| `horrocruxes` | `horrocrux` | 99 | review: merge |
| `karate-do` | `karate` | 99 | review: merge |
| `masterclasse` | `masterclass` | 99 | review: merge |
| `rishis` | `rishi` | 99 | review: merge |
| `subsidiarias` | `subsidiario` | 99 | review: merge |
| `anti-vaho` | `antivaho` | 97 | review: merge |
| `aportándol` | `aportar` | 96 | review: merge |
| `juntaos` | `juntarse` | 96 | review: merge |
| `bootcamps` | `bootcamp` | 95 | review: merge |
| `saciarno` | `saciarse` | 95 | review: merge |
| `srta` | `señorita` | 95 | review: merge |
| `analizamos` | `analizar` | 94 | review: merge |
| `azithromycin` | `azitromicina` | 94 | review: merge |
| `dirigirl` | `dirigir` | 94 | review: merge |
| `semi-esencial` | `semiesencial` | 94 | review: merge |
| `socio-ecológico` | `socioecológico` | 94 | review: merge |
| `sultano` | `sultana` | 131 | review: merge |
| `aromatase` | `aromatasa` | 130 | review: merge |
| `ministraba` | `ministrar` | 130 | review: merge |
| `seguid` | `seguir` | 130 | review: merge |
| `coorganizado` | `coorganizar` | 129 | review: merge |
| `echémosle` | `echar` | 129 | review: merge |
| `lamprear` | `lamprea` | 129 | review: merge |
| `pings` | `ping` | 129 | review: merge |
| `problemilla` | `problema` | 129 | review: merge |
| `enfrentándote` | `enfrentarse` | 128 | review: merge |
| `raps` | `rap` | 127 | review: merge |
| `diskette` | `disquete` | 126 | review: merge |
| `ofreciéndole` | `ofrecer` | 126 | review: merge |
| `tentándole` | `tentar` | 126 | review: merge |
| `hidraúlico` | `hidráulico` | 125 | review: merge |
| `atraccion` | `atracción` | 124 | review: merge |
| `envuelta` | `envolver` | 124 | review: merge |
| `farmaceútico` | `farmacéutico` | 124 | review: merge |
| `muévelo` | `mover` | 124 | review: merge |
| `premontados` | `premontado` | 124 | review: merge |
| `excluídos` | `excluir` | 123 | review: merge |
| `ferreter` | `ferretería` | 123 | review: merge |
| `portugue` | `portugués` | 123 | review: merge |
| `pudriéndose` | `pudrirse` | 123 | review: merge |
| `nubuc` | `nubuck` | 122 | review: merge |
| `tipis` | `tipi` | 122 | review: merge |
| `bebita` | `bebé` | 121 | review: merge |
| `distribuída` | `distribuir` | 121 | review: merge |
| `estós` | `este` | 121 | review: merge |
| `intersectan` | `intersectar` | 121 | review: merge |
| `numerico` | `numérico` | 121 | review: merge |
| `parasitado` | `parasitar` | 121 | review: merge |
| `prendido` | `prender` | 121 | review: merge |
| `capilariza` | `capilarizar` | 120 | review: merge |
| `externalizado` | `externalizar` | 120 | review: merge |
| `llevadlo` | `llevar` | 120 | review: merge |
| `ponedlo` | `poner` | 120 | review: merge |
| `proxys` | `proxy` | 120 | review: merge |
| `interfer` | `interferón` | 119 | review: merge |
| `parket` | `parqué` | 119 | review: merge |
| `averia` | `avería` | 118 | review: merge |
| `dejadle` | `dejar` | 118 | review: merge |
| `entradas` | `entrada` | 118 | review: merge |
| `transmitencia` | `transmitancia` | 118 | review: merge |
| `arterítica` | `arterítico` | 117 | review: merge |
| `campanita` | `campana` | 117 | review: merge |
| `divisiva` | `divisivo` | 117 | review: merge |
| `portorriqueño` | `puertorriqueño` | 117 | review: merge |
| `econtrar` | `encontrar` | 116 | review: merge |
| `lógicar` | `lógica` | 116 | review: merge |
| `reinvierten` | `reinvertir` | 116 | review: merge |
| `amonitas` | `amonita` | 115 | review: merge |
| `gramnegativas` | `gramnegativo` | 115 | review: merge |
| `ingerencia` | `injerencia` | 115 | review: merge |
| `neuquina` | `neuquino` | 115 | review: merge |
| `ordenándole` | `ordenar` | 115 | review: merge |
| `tankinis` | `tankini` | 115 | review: merge |
| `truquito` | `truco` | 115 | review: merge |
| `alcántar` | `alcántara` | 114 | review: merge |
| `codiciones` | `condición` | 114 | review: merge |
| `cortita` | `corto` | 114 | review: merge |
| `hizó` | `hacer` | 114 | review: merge |
| `panelistas` | `panelista` | 114 | review: merge |
| `sacándolo` | `sacar` | 114 | review: merge |
| `digitado` | `digitar` | 113 | review: merge |
| `fuéronse` | `irse` | 113 | review: merge |
| `muuuy` | `muy` | 113 | review: merge |
| `cánnabis` | `cannabis` | 112 | review: merge |
| `innovativa` | `innovador` | 112 | review: merge |
| `simpre` | `siempre` | 112 | review: merge |
| `uniéndo` | `unir` | 112 | review: merge |
| `abdominoplastía` | `abdominoplastia` | 111 | review: merge |
| `cristológica` | `cristológico` | 111 | review: merge |
| `guárdese` | `guardarse` | 111 | review: merge |
| `jugones` | `jugón` | 111 | review: merge |
| `musculoesquelética` | `musculoesquelético` | 111 | review: merge |
| `nebulizada` | `nebulizar` | 111 | review: merge |
| `purito` | `puro` | 111 | review: merge |
| `heramienta` | `herramienta` | 110 | review: merge |
| `reintroduce` | `reintroducir` | 110 | review: merge |
| `rivaroxaban` | `rivaroxabán` | 110 | review: merge |
| `yoe` | `yo` | 110 | review: merge |
| `electroquirúrgica` | `electroquirúrgico` | 109 | review: merge |
| `harmónica` | `armónico` | 109 | review: merge |
| `interpretarlas` | `interpretar` | 109 | review: merge |
| `isoniazid` | `isoniazida` | 109 | review: merge |
| `microtransacciones` | `microtransacción` | 109 | review: merge |
| `muchxs` | `mucho` | 109 | review: merge |
| `reestablecimiento` | `restablecimiento` | 109 | review: merge |
| `culés` | `culé` | 108 | review: merge |
| `encuentrar` | `encontrar` | 108 | review: merge |
| `jarciar` | `jarcia` | 108 | review: merge |
| `peguntar` | `preguntar` | 108 | review: merge |
| `pued` | `poder` | 108 | review: merge |
| `apropriadas` | `apropiado` | 107 | review: merge |
| `orginal` | `original` | 107 | review: merge |
| `persecusión` | `persecución` | 107 | review: merge |
| `preocupándote` | `preocuparse` | 107 | review: merge |
| `reprogramadas` | `reprogramar` | 107 | review: merge |
| `vampírica` | `vampírico` | 107 | review: merge |
| `anticipándose` | `anticiparse` | 106 | review: merge |
| `desenchúfelo` | `desenchufar` | 106 | review: merge |
| `redireccionados` | `redireccionar` | 106 | review: merge |
| `contácte` | `contactar` | 105 | review: merge |
| `diferencio` | `diferencia` | 105 | review: merge |
| `encendiéndose` | `encenderse` | 105 | review: merge |
| `excluyéndose` | `excluir` | 105 | review: merge |
| `llevándola` | `llevar` | 105 | review: merge |
| `solter` | `soltería` | 105 | review: merge |
| `agítelo` | `agitar` | 104 | review: merge |
| `clorina` | `cloro` | 104 | review: merge |
| `creyéndose` | `creerse` | 104 | review: merge |
| `familial` | `familiar` | 104 | review: merge |
| `gasífera` | `gasífero` | 104 | review: merge |
| `llénala` | `llenar` | 104 | review: merge |
| `líbido` | `libido` | 104 | review: merge |
| `matémoslo` | `matar` | 104 | review: merge |
| `retirarno` | `retirarse` | 104 | review: merge |
| `risita` | `risa` | 104 | review: merge |
| `asegúrelo` | `asegurar` | 103 | review: merge |
| `chasís` | `chasis` | 103 | review: merge |
| `desestructurada` | `desestructurado` | 103 | review: merge |
| `tratativas` | `tratativa` | 103 | review: merge |
| `vincu` | `vínculo` | 103 | review: merge |
| `casette` | `casete` | 102 | review: merge |
| `clickeando` | `cliquear` | 102 | review: merge |
| `expectacular` | `espectacular` | 102 | review: merge |
| `virológica` | `virológico` | 102 | review: merge |
| `dósis` | `dosis` | 101 | review: merge |
| `senorita` | `señorita` | 101 | review: merge |
| `tomándole` | `tomar` | 101 | review: merge |
| `asanas` | `asana` | 100 | review: merge |
| `compatir` | `compartir` | 100 | review: merge |
| `desactivarlo` | `desactivar` | 100 | review: merge |
| `mescla` | `mezcla` | 100 | review: merge |
| `refiriéndome` | `referirse` | 100 | review: merge |
| `subterranea` | `subterráneo` | 100 | review: merge |
| `cetogénicas` | `cetogénico` | 99 | review: merge |
| `distribuídas` | `distribuir` | 99 | review: merge |
| `drizar` | `driza` | 99 | review: merge |
| `geolocalizados` | `geolocalizar` | 99 | review: merge |
| `protegiéndote` | `protegerse` | 99 | review: merge |
| `terroirs` | `terroir` | 99 | review: merge |
| `semi-independiente` | `semiindependiente` | 122 | review: merge |
| `lecto-escritura` | `lectoescritura` | 121 | review: merge |
| `traves` | `través` | 121 | review: merge |
| `bolívares` | `bolívar` | 119 | review: merge |
| `back-up` | `backup` | 118 | review: merge |
| `depa` | `departamento` | 118 | review: merge |
| `esforcémo` | `esforzarse` | 118 | review: merge |
| `negativos` | `negativo` | 118 | review: merge |
| `pre-pagada` | `prepagada` | 117 | review: merge |
| `tai-chi` | `tai chi` | 117 | review: merge |
| `tobilleras` | `tobillera` | 117 | review: merge |
| `jacarando` | `jacaranda` | 116 | review: merge |
| `lanzagranada` | `lanzagranadas` | 116 | review: merge |
| `auto-suficiente` | `autosuficiente` | 115 | review: merge |
| `carbamazepine` | `carbamazepina` | 115 | review: merge |
| `co-organizado` | `coorganizar` | 115 | review: merge |
| `mugs` | `mug` | 115 | review: merge |
| `saciaro` | `saciar` | 115 | review: merge |
| `asignándol` | `asignar` | 113 | review: merge |
| `diáspor` | `diáspora` | 113 | review: merge |
| `morbi-mortalidad` | `morbimortalidad` | 112 | review: merge |
| `atrapasueño` | `atrapasueños` | 111 | review: merge |
| `manipule` | `manipular` | 111 | review: merge |
| `pre-selección` | `preselección` | 111 | review: merge |
| `binador` | `binadora` | 110 | review: merge |
| `auto-descarga` | `autodescarga` | 109 | review: merge |
| `corruptibl` | `corruptible` | 109 | review: merge |
| `intérpretes` | `intérprete` | 109 | review: merge |
| `practique` | `practicar` | 109 | review: merge |
| `tenerl` | `tener` | 108 | review: merge |
| `dosimetr` | `dosimetría` | 107 | review: merge |
| `fitoesterole` | `fitoesterol` | 107 | review: merge |
| `ofreciéndono` | `ofrecer` | 107 | review: merge |
| `aquiler` | `alquiler` | 106 | review: merge |
| `bonsáis` | `bonsái` | 105 | review: merge |
| `recordarl` | `recordar` | 105 | review: merge |
| `slim-fit` | `slim fit` | 105 | review: merge |
| `auto-imagen` | `autoimagen` | 104 | review: merge |
| `confirmaro` | `confirmar` | 104 | review: merge |
| `horas-hombre` | `hora hombre` | 104 | review: merge |
| `pre-requisito` | `prerrequisito` | 104 | review: merge |
| `seguís` | `seguir` | 104 | review: merge |
| `ex-novio` | `exnovio` | 103 | review: merge |
| `jejejeje` | `jeje` | 103 | review: merge |
| `reconfigur` | `reconfigurar` | 103 | review: merge |
| `sangria` | `sangría` | 103 | review: merge |
| `visítano` | `visitar` | 103 | review: merge |
| `corregidos` | `corregir` | 102 | review: merge |
| `ex-compañero` | `excompañero` | 102 | review: merge |
| `fijémono` | `fijarse` | 102 | review: merge |
| `quebequens` | `quebequense` | 102 | review: merge |
| `sub-sahariana` | `subsahariano` | 102 | review: merge |
| `olanzapine` | `olanzapina` | 101 | review: merge |
| `explíquel` | `explicar` | 100 | review: merge |
| `metrica` | `métrica` | 100 | review: merge |
| `nicotine` | `nicotina` | 100 | review: merge |
| `consecuenciales` | `consecuencial` | 99 | review: merge |
| `proveerno` | `proveer` | 99 | review: merge |
| `accesibles` | `accesible` | 98 | review: merge |
| `distritale` | `distrital` | 98 | review: merge |
| `aproximarno` | `aproximarse` | 97 | review: merge |
| `broccoli` | `brócoli` | 97 | review: merge |
| `aprenda` | `aprender` | 96 | review: merge |
| `pizarras` | `pizarra` | 96 | review: merge |
| `pre-filtro` | `prefiltro` | 96 | review: merge |
| `serviro` | `servir` | 96 | review: merge |
| `elevabl` | `elevable` | 95 | review: merge |
| `ex-director` | `exdirector` | 95 | review: merge |
| `post-doctoral` | `posdoctoral` | 95 | review: merge |
| `admiro` | `admirar` | 94 | review: merge |
| `anti-cristo` | `anticristo` | 94 | review: merge |
| `co-autora` | `coautora` | 94 | review: merge |
| `ex-jugador` | `exjugador` | 94 | review: merge |
| `agítalo` | `agitar` | 130 | review: merge |
| `asechar` | `acechar` | 130 | review: merge |
| `intrucciones` | `instrucción` | 130 | review: merge |
| `neomycin` | `neomicina` | 130 | review: merge |
| `rugbi` | `rugby` | 130 | review: merge |
| `anímense` | `animarse` | 129 | review: merge |
| `copresidido` | `copresidir` | 129 | review: merge |
| `jihadista` | `yihadista` | 129 | review: merge |
| `lanchar` | `lancha` | 129 | review: merge |
| `notifícame` | `notificar` | 129 | review: merge |
| `tomadle` | `tomar` | 129 | review: merge |
| `videoconsolas` | `videoconsola` | 129 | review: merge |
| `crímen` | `crimen` | 128 | review: merge |
| `doberman` | `dóberman` | 128 | review: merge |
| `jesuíticas` | `jesuítico` | 128 | review: merge |
| `perioperatoria` | `perioperatorio` | 128 | review: merge |
| `sacándola` | `sacar` | 128 | review: merge |
| `críticar` | `criticar` | 127 | review: merge |
| `liberándolo` | `liberar` | 127 | review: merge |
| `notifíquelo` | `notificar` | 127 | review: merge |
| `bistrós` | `bistró` | 126 | review: merge |
| `camita` | `cama` | 126 | review: merge |
| `empodere` | `empoderar` | 126 | review: merge |
| `tricuspídea` | `tricuspídeo` | 126 | review: merge |
| `creá` | `crear` | 125 | review: merge |
| `macero` | `macerar` | 125 | review: merge |
| `bloggera` | `bloguera` | 123 | review: merge |
| `búqueda` | `búsqueda` | 123 | review: merge |
| `chapuzar` | `chapuza` | 123 | review: merge |
| `desecharlo` | `desechar` | 123 | review: merge |
| `extramuro` | `extramuros` | 123 | review: merge |
| `imprímalo` | `imprimir` | 123 | review: merge |
| `reconociéndolo` | `reconocer` | 123 | review: merge |
| `wellnes` | `wellness` | 123 | review: merge |
| `hazla` | `hacer` | 122 | review: merge |
| `preguntá` | `preguntar` | 122 | review: merge |
| `succionando` | `succionar` | 122 | review: merge |
| `centrándote` | `centrarse` | 121 | review: merge |
| `cocínelo` | `cocinar` | 121 | review: merge |
| `kerosene` | `queroseno` | 121 | review: merge |
| `pídanle` | `pedir` | 121 | review: merge |
| `salafistas` | `salafista` | 121 | review: merge |
| `visitarla` | `visitar` | 121 | review: merge |
| `antidiurética` | `antidiurético` | 120 | review: merge |
| `dejadla` | `dejar` | 120 | review: merge |
| `despiértese` | `despertarse` | 120 | review: merge |
| `estrategía` | `estrategia` | 120 | review: merge |
| `hiperlink` | `hipervínculo` | 120 | review: merge |
| `indentificar` | `identificar` | 120 | review: merge |
| `intesificado` | `intensificar` | 120 | review: merge |
| `reintroducido` | `reintroducir` | 120 | review: merge |
| `tambin` | `también` | 120 | review: merge |
| `animándolo` | `animar` | 119 | review: merge |
| `mayora` | `mayoría` | 119 | review: merge |
| `anímalo` | `animar` | 118 | review: merge |
| `circumstancia` | `circunstancia` | 118 | review: merge |
| `volvi` | `volver` | 118 | review: merge |
| `aceptás` | `aceptar` | 117 | review: merge |
| `contadme` | `contar` | 117 | review: merge |
| `trofoblástica` | `trofoblástico` | 117 | review: merge |
| `aniquilarlo` | `aniquilar` | 116 | review: merge |
| `apliqúese` | `aplicar` | 116 | review: merge |
| `reclasificado` | `reclasificar` | 116 | review: merge |
| `sociodemográfica` | `sociodemográfico` | 116 | review: merge |
| `innovativas` | `innovativo` | 115 | review: merge |
| `buenisima` | `bueno` | 114 | review: merge |
| `domotica` | `domótica` | 114 | review: merge |
| `imprímelo` | `imprimir` | 114 | review: merge |
| `perfomance` | `performance` | 114 | review: merge |
| `vuélvanse` | `volverse` | 114 | review: merge |
| `charcuter` | `charcutería` | 113 | review: merge |
| `selecione` | `seleccionar` | 113 | review: merge |
| `taquigrafiar` | `taquigrafía` | 113 | review: merge |
| `configúralo` | `configurar` | 112 | review: merge |
| `línia` | `línea` | 112 | review: merge |
| `niñ` | `niño` | 112 | review: merge |
| `perdonadme` | `perdonar` | 112 | review: merge |
| `abuhardillados` | `abuhardillado` | 111 | review: merge |
| `amándote` | `amar` | 111 | review: merge |
| `enlistada` | `enlistar` | 111 | review: merge |
| `hoverboards` | `hoverboard` | 111 | review: merge |
| `omelet` | `omelette` | 111 | review: merge |
| `serums` | `sérum` | 111 | review: merge |
| `terafines` | `terafín` | 111 | review: merge |
| `trás` | `tras` | 111 | review: merge |
| `apartir` | `a partir` | 110 | review: merge |
| `pingpong` | `ping-pong` | 110 | review: merge |
| `reinvier` | `reinvertir` | 110 | review: merge |
| `amigxs` | `amigo` | 109 | review: merge |
| `añádase` | `añadir` | 109 | review: merge |
| `concentrándote` | `concentrarse` | 109 | review: merge |
| `enrutan` | `enrutar` | 109 | review: merge |
| `guiándome` | `guiar` | 109 | review: merge |
| `harpa` | `arpa` | 109 | review: merge |
| `naloxone` | `naloxona` | 109 | review: merge |
| `rehidrata` | `rehidratar` | 109 | review: merge |
| `sumergiéndote` | `sumergirse` | 109 | review: merge |
| `cúanto` | `cuánto` | 108 | review: merge |
| `generalicia` | `generalicio` | 108 | review: merge |
| `rigida` | `rígido` | 108 | review: merge |
| `bajen` | `bajar` | 107 | review: merge |
| `excursiónes` | `excursión` | 107 | review: merge |
| `gnocchi` | `ñoqui` | 107 | review: merge |
| `laissez` | `laissez faire` | 107 | review: merge |
| `prinicipal` | `principal` | 107 | review: merge |
| `reconociéndose` | `reconocerse` | 107 | review: merge |
| `spammers` | `spammer` | 107 | review: merge |
| `antigüa` | `antiguo` | 106 | review: merge |
| `diviértanse` | `divertirse` | 106 | review: merge |
| `habitu` | `habitus` | 106 | review: merge |
| `ponys` | `poni` | 106 | review: merge |
| `reemplazándola` | `reemplazar` | 106 | review: merge |
| `surfeando` | `surfear` | 106 | review: merge |
| `adivasis` | `adivasi` | 105 | review: merge |
| `deslízalo` | `deslizar` | 105 | review: merge |
| `jajajajaja` | `jaja` | 105 | review: merge |
| `nimbar` | `nimbo` | 105 | review: merge |
| `travéz` | `través` | 105 | review: merge |
| `achaparrar` | `achaparrado` | 104 | review: merge |
| `amitriptyline` | `amitriptilina` | 104 | review: merge |
| `ayúdalo` | `ayudar` | 104 | review: merge |
| `flashearla` | `flashear` | 104 | review: merge |
| `mufti` | `muftí` | 104 | review: merge |
| `ninjas` | `ninja` | 104 | review: merge |
| `protegiéndose` | `protegerse` | 104 | review: merge |
| `téxtil` | `textil` | 104 | review: merge |
| `customizada` | `customizar` | 103 | review: merge |
| `inmunocomprometidos` | `inmunocomprometido` | 103 | review: merge |
| `levitando` | `levitar` | 103 | review: merge |
| `sobreexplotado` | `sobreexplotar` | 103 | review: merge |
| `asícomo` | `así como` | 102 | review: merge |
| `blogueando` | `bloguear` | 102 | review: merge |
| `extrano` | `extraño` | 102 | review: merge |
| `infórmacion` | `información` | 102 | review: merge |
| `noticas` | `noticia` | 102 | review: merge |
| `victimizados` | `victimizar` | 102 | review: merge |
| `conocimento` | `conocimiento` | 101 | review: merge |
| `postprocesamiento` | `posprocesamiento` | 101 | review: merge |
| `sicotrópicas` | `sicotrópico` | 101 | review: merge |
| `tuiteado` | `tuitear` | 101 | review: merge |
| `dijó` | `decir` | 100 | review: merge |
| `ecorregiones` | `ecorregión` | 100 | review: merge |
| `encontrarlo` | `encontrar` | 100 | review: merge |
| `hize` | `hacer` | 100 | review: merge |
| `roadtrip` | `road trip` | 100 | review: merge |
| `fútsal` | `futsal` | 99 | review: merge |
| `presxs` | `preso` | 99 | review: merge |
| `sudcoreano` | `surcoreano` | 99 | review: merge |
| `élla` | `ella` | 99 | review: merge |
| `antiinmigrantes` | `antiinmigrante` | 98 | review: merge |
| `boulevar` | `bulevar` | 98 | review: merge |
| `prohibidas` | `prohibido` | 123 | review: merge |
| `co-fundó` | `cofundar` | 122 | review: merge |
| `amonestaro` | `amonestar` | 121 | review: merge |
| `pre-test` | `pretest` | 121 | review: merge |
| `quitándol` | `quitar` | 121 | review: merge |
| `capris` | `capri` | 120 | review: merge |
| `sumak` | `sumak kawsay` | 120 | review: merge |
| `aplicarl` | `aplicar` | 119 | review: merge |
| `audio-guía` | `audioguía` | 119 | review: merge |
| `eco-turismo` | `ecoturismo` | 119 | review: merge |
| `haver` | `hacer` | 117 | review: merge |
| `oxido` | `óxido` | 116 | review: merge |
| `semi-permanente` | `semipermanente` | 116 | review: merge |
| `sikhs` | `sikh` | 116 | review: merge |
| `anti-falsificación` | `antifalsificación` | 115 | review: merge |
| `betamethasone` | `betametasona` | 114 | review: merge |
| `guiándono` | `guiar` | 114 | review: merge |
| `subwoofers` | `subwoofer` | 114 | review: merge |
| `autoelevadore` | `autoelevador` | 113 | review: merge |
| `reunío` | `reunirse` | 113 | review: merge |
| `sobreponerno` | `sobreponerse` | 113 | review: merge |
| `físico-química` | `fisicoquímico` | 112 | review: merge |
| `lasers` | `láser` | 112 | review: merge |
| `onu-mujer` | `onu mujeres` | 112 | review: merge |
| `transabl` | `transable` | 112 | review: merge |
| `paranoid` | `paranoide` | 111 | review: merge |
| `anti-reflejo` | `antirreflejo` | 110 | review: merge |
| `outsiders` | `outsider` | 110 | review: merge |
| `wafl` | `wafle` | 110 | review: merge |
| `caracter` | `carácter` | 109 | review: merge |
| `escritos` | `escrito` | 109 | review: merge |
| `cryolipolysis` | `criolipólisis` | 108 | review: merge |
| `urbanizaciones` | `urbanización` | 108 | review: merge |
| `agar-agar` | `agar` | 107 | review: merge |
| `arregle` | `arreglar` | 107 | review: merge |
| `furosemide` | `furosemida` | 107 | review: merge |
| `nacional-socialista` | `nacionalsocialista` | 107 | review: merge |
| `auto-reflexión` | `autorreflexión` | 106 | review: merge |
| `common-rail` | `common rail` | 106 | review: merge |
| `triple-doble` | `triple doble` | 106 | review: merge |
| `co-líder` | `colíder` | 105 | review: merge |
| `gobernancía` | `gobernanza` | 105 | review: merge |
| `ordenándol` | `ordenar` | 105 | review: merge |
| `inconfor` | `inconforme` | 104 | review: merge |
| `vá` | `ir` | 104 | review: merge |
| `felicitarl` | `felicitar` | 103 | review: merge |
| `humillaos` | `humillarse` | 103 | review: merge |
| `avíseno` | `avisar` | 102 | review: merge |
| `ex-esposa` | `exesposa` | 102 | review: merge |
| `multi-dimensional` | `multidimensional` | 102 | review: merge |
| `snorkling` | `esnórquel` | 101 | review: merge |
| `todo-terreno` | `todoterreno` | 101 | review: merge |
| `asegurándol` | `asegurar` | 100 | review: merge |
| `seronr` | `ser` | 100 | review: merge |
| `tenedur` | `teneduría` | 100 | review: merge |
| `atraídos` | `atraer` | 99 | review: merge |
| `planimetr` | `planimetría` | 99 | review: merge |
| `riendo` | `reír` | 99 | review: merge |
| `solicitándol` | `solicitar` | 98 | review: merge |
| `cerveceria` | `cervecería` | 97 | review: merge |
| `fuel-oil` | `fueloil` | 97 | review: merge |
| `semi-automáticas` | `semiautomático` | 97 | review: merge |
| `acolchada` | `acolchado` | 96 | review: merge |
| `econometr` | `econometría` | 96 | review: merge |
| `grababl` | `grabable` | 96 | review: merge |
| `luthiers` | `luthier` | 96 | review: merge |
| `notificarl` | `notificar` | 96 | review: merge |
| `queen-size` | `queen size` | 96 | review: merge |
| `detenerno` | `detenerse` | 95 | review: merge |
| `pre-adolescentes` | `preadolescente` | 95 | review: merge |
| `semi-sótano` | `semisótano` | 95 | review: merge |
| `sugerirl` | `sugerir` | 95 | review: merge |
| `acompañándono` | `acompañar` | 94 | review: merge |
| `habiéndol` | `haber` | 94 | review: merge |
| `n-hexano` | `hexano` | 94 | review: merge |
| `talones` | `talón` | 94 | review: merge |
| `sosteniéndolo` | `sostener` | 131 | review: merge |
| `antillana` | `antillano` | 130 | review: merge |
| `glicosilada` | `glicosilado` | 130 | review: merge |
| `infographic` | `infografía` | 130 | review: merge |
| `añádale` | `añadir` | 129 | review: merge |
| `castellers` | `casteller` | 129 | review: merge |
| `dejad` | `dejar` | 129 | review: merge |
| `extrañas` | `extraño` | 129 | review: merge |
| `justica` | `justicia` | 129 | review: merge |
| `sútil` | `sutil` | 129 | review: merge |
| `violacion` | `violación` | 129 | review: merge |
| `insértelo` | `insertar` | 128 | review: merge |
| `médicar` | `médico` | 128 | review: merge |
| `soriasis` | `psoriasis` | 128 | review: merge |
| `bahiana` | `bahiano` | 127 | review: merge |
| `fanes` | `fan` | 127 | review: merge |
| `reconfigura` | `reconfigurar` | 127 | review: merge |
| `revuélvelo` | `revolver` | 127 | review: merge |
| `súmale` | `sumar` | 127 | review: merge |
| `autodenominan` | `autodenominarse` | 126 | review: merge |
| `devolverse` | `devolver` | 126 | review: merge |
| `guiándote` | `guiar` | 126 | review: merge |
| `postraumática` | `postraumático` | 126 | review: merge |
| `rastas` | `rasta` | 126 | review: merge |
| `veran` | `ver` | 126 | review: merge |
| `econtraremos` | `encontrar` | 125 | review: merge |
| `exáctamente` | `exactamente` | 125 | review: merge |
| `inespecífica` | `inespecífico` | 125 | review: merge |
| `metronidazole` | `metronidazol` | 125 | review: merge |
| `reglón` | `renglón` | 125 | review: merge |
| `uniéndolo` | `unir` | 125 | review: merge |
| `cester` | `cestería` | 124 | review: merge |
| `decembrinas` | `decembrino` | 124 | review: merge |
| `poblana` | `poblano` | 124 | review: merge |
| `proyeccion` | `proyección` | 124 | review: merge |
| `inovador` | `innovador` | 123 | review: merge |
| `polígloto` | `poliglota` | 123 | review: merge |
| `posteados` | `postear` | 123 | review: merge |
| `transdisciplinaria` | `transdisciplinario` | 123 | review: merge |
| `bipartidistas` | `bipartidista` | 122 | review: merge |
| `cabriolar` | `cabriola` | 122 | review: merge |
| `construídos` | `construido` | 122 | review: merge |
| `empezé` | `empezar` | 122 | review: merge |
| `huzí` | `hutí` | 122 | review: merge |
| `redireccionan` | `redireccionar` | 122 | review: merge |
| `bisuter` | `bisutería` | 121 | review: merge |
| `desbalances` | `desbalance` | 121 | review: merge |
| `garífunas` | `garífuna` | 121 | review: merge |
| `inalambrica` | `inalámbrico` | 121 | review: merge |
| `permítanos` | `permitir` | 121 | review: merge |
| `resistiéndose` | `resistirse` | 121 | review: merge |
| `acrítica` | `acrítico` | 120 | review: merge |
| `añadiéndose` | `añadirse` | 120 | review: merge |
| `etaria` | `etario` | 120 | review: merge |
| `previsualice` | `previsualizar` | 120 | review: merge |
| `salté` | `saltar` | 120 | review: merge |
| `demonizado` | `demonizar` | 119 | review: merge |
| `insértela` | `insertar` | 119 | review: merge |
| `invitándole` | `invitar` | 119 | review: merge |
| `partiéndose` | `partirse` | 119 | review: merge |
| `propositiva` | `propositivo` | 119 | review: merge |
| `vistir` | `vista` | 119 | review: merge |
| `configúrelo` | `configurar` | 118 | review: merge |
| `marginalizadas` | `marginalizado` | 118 | review: merge |
| `muel` | `muelle` | 118 | review: merge |
| `testeada` | `testear` | 118 | review: merge |
| `vídeojuego` | `videojuego` | 118 | review: merge |
| `yogis` | `yogui` | 118 | review: merge |
| `aventúrese` | `aventurarse` | 117 | review: merge |
| `contínuo` | `continuo` | 117 | review: merge |
| `esperiencia` | `experiencia` | 117 | review: merge |
| `pantie` | `panti` | 117 | review: merge |
| `catabólicas` | `catabólico` | 116 | review: merge |
| `dirigiéndome` | `dirigirse` | 116 | review: merge |
| `edif` | `edificio` | 116 | review: merge |
| `miconazole` | `miconazol` | 116 | review: merge |
| `modu` | `módulo` | 116 | review: merge |
| `preprints` | `preprint` | 116 | review: merge |
| `resilencia` | `resiliencia` | 116 | review: merge |
| `snorkelling` | `snorkel` | 116 | review: merge |
| `succionado` | `succionar` | 116 | review: merge |
| `tráder` | `trader` | 116 | review: merge |
| `ketoconazole` | `ketoconazol` | 115 | review: merge |
| `ultradelgada` | `ultradelgado` | 115 | review: merge |
| `clorpirifo` | `clorpirifós` | 114 | review: merge |
| `desague` | `desagüe` | 114 | review: merge |
| `notifíqueme` | `notificar` | 114 | review: merge |
| `potenciadora` | `potenciador` | 114 | review: merge |
| `protagónica` | `protagónico` | 114 | review: merge |
| `váyanse` | `irse` | 114 | review: merge |
| `aplicaciónes` | `aplicación` | 113 | review: merge |
| `desestabilizadoras` | `desestabilizador` | 113 | review: merge |
| `naufrago` | `náufrago` | 113 | review: merge |
| `azúl` | `azul` | 112 | review: merge |
| `briza` | `brisa` | 112 | review: merge |
| `enrutaremos` | `enrutar` | 112 | review: merge |
| `incio` | `inicio` | 111 | review: merge |
| `terapeutico` | `terapéutico` | 111 | review: merge |
| `cannábicas` | `cannábico` | 110 | review: merge |
| `chondroitin` | `condroitina` | 110 | review: merge |
| `coran` | `corán` | 110 | review: merge |
| `cualquer` | `cualquier` | 110 | review: merge |
| `díganle` | `decir` | 110 | review: merge |
| `metalera` | `metalero` | 110 | review: merge |
| `quítele` | `quitar` | 110 | review: merge |
| `renderizada` | `renderizar` | 110 | review: merge |
| `rocíe` | `rociar` | 110 | review: merge |
| `desinstalando` | `desinstalar` | 109 | review: merge |
| `nanomaterials` | `nanomaterial` | 109 | review: merge |
| `resi` | `residencia` | 109 | review: merge |
| `seleccíon` | `selección` | 109 | review: merge |
| `succionan` | `succionar` | 109 | review: merge |
| `deslizándola` | `deslizar` | 108 | review: merge |
| `develan` | `develar` | 108 | review: merge |
| `dotándolo` | `dotar` | 108 | review: merge |
| `evacuan` | `evacuar` | 108 | review: merge |
| `loratadine` | `loratadina` | 108 | review: merge |
| `antiespasmódicas` | `antiespasmódico` | 107 | review: merge |
| `calentaos` | `calentarse` | 107 | review: merge |
| `decóralo` | `decorar` | 107 | review: merge |
| `eliga` | `elegir` | 107 | review: merge |
| `expidir` | `expedir` | 107 | review: merge |
| `intrahospitalarias` | `intrahospitalario` | 107 | review: merge |
| `pobrecita` | `pobrecito` | 107 | review: merge |
| `yedra` | `hiedra` | 107 | review: merge |
| `antioqueña` | `antioqueño` | 106 | review: merge |
| `entrá` | `entrar` | 106 | review: merge |
| `estrogen` | `estrógeno` | 106 | review: merge |
| `haciéndo` | `hacer` | 106 | review: merge |
| `malwar` | `malware` | 106 | review: merge |
| `mesothelioma` | `mesotelioma` | 106 | review: merge |
| `serializado` | `serializar` | 106 | review: merge |
| `sosteniéndose` | `sostenerse` | 106 | review: merge |
| `chauvinismo` | `chovinismo` | 105 | review: merge |
| `eduardiana` | `eduardiano` | 105 | review: merge |
| `judeocristiana` | `judeocristiano` | 105 | review: merge |
| `adoloridas` | `adolorido` | 104 | review: merge |
| `antimicrobial` | `antimicrobiano` | 104 | review: merge |
| `cambiarlas` | `cambiar` | 104 | review: merge |
| `cuelga` | `colgar` | 104 | review: merge |
| `déjense` | `dejarse` | 104 | review: merge |
| `forzándolo` | `forzar` | 104 | review: merge |
| `hipospadia` | `hipospadias` | 104 | review: merge |
| `llenándola` | `llenar` | 104 | review: merge |
| `mapeadas` | `mapear` | 104 | review: merge |
| `revuélvela` | `revolver` | 104 | review: merge |
| `submilimétricas` | `submilimétrico` | 104 | review: merge |
| `ínglés` | `inglés` | 104 | review: merge |
| `báñese` | `bañarse` | 103 | review: merge |
| `carnita` | `carnitas` | 103 | review: merge |
| `dejémoslo` | `dejar` | 103 | review: merge |
| `licue` | `licuar` | 103 | review: merge |
| `reconfigurando` | `reconfigurar` | 103 | review: merge |
| `santar` | `santa` | 103 | review: merge |
| `bármanes` | `bárman` | 102 | review: merge |
| `hacedla` | `hacer` | 102 | review: merge |
| `incorpórate` | `incorporarse` | 102 | review: merge |
| `mientra` | `mientras` | 102 | review: merge |
| `oscarizada` | `oscarizado` | 102 | review: merge |
| `sujételo` | `sujetar` | 102 | review: merge |
| `tayikos` | `tayiko` | 102 | review: merge |
| `traquear` | `tráquea` | 102 | review: merge |
| `videoar` | `videoarte` | 102 | review: merge |
| `albañileria` | `albañilería` | 101 | review: merge |
| `amplis` | `amplificador` | 101 | review: merge |
| `deacuerdo` | `de acuerdo` | 101 | review: merge |
| `fluoroscopía` | `fluoroscopia` | 101 | review: merge |
| `gángsters` | `gánster` | 101 | review: merge |
| `penicillin` | `penicilina` | 101 | review: merge |
| `suitte` | `suite` | 101 | review: merge |
| `apriscar` | `aprisco` | 100 | review: merge |
| `contínuas` | `continuo` | 100 | review: merge |
| `definiéndose` | `definir` | 100 | review: merge |
| `diseñ` | `diseño` | 100 | review: merge |
| `glucosilada` | `glucosilado` | 100 | review: merge |
| `incluímos` | `incluir` | 100 | review: merge |
| `involúcrese` | `involucrarse` | 100 | review: merge |
| `mountainbike` | `mountain bike` | 100 | review: merge |
| `protable` | `portátil` | 100 | review: merge |
| `maldíceme` | `maldecir` | 99 | review: merge |
| `melatonin` | `melatonina` | 99 | review: merge |
| `nanogramos` | `nanogramo` | 99 | review: merge |
| `ruedecita` | `rueda` | 99 | review: merge |
| `teletransportado` | `teletransportar` | 99 | review: merge |
| `arrójalo` | `arrojar` | 98 | review: merge |
| `anticipándono` | `anticiparse` | 93 | review: merge |
| `co-financiado` | `cofinanciar` | 93 | review: merge |
| `reuniéndono` | `reunirse` | 93 | review: merge |
| `automovi` | `automóvil` | 92 | review: merge |
| `borax` | `bórax` | 92 | review: merge |
| `ex-empleado` | `exempleado` | 92 | review: merge |
| `lookbooks` | `lookbook` | 92 | review: merge |
| `nutrirno` | `nutrirse` | 92 | review: merge |
| `sincronicidade` | `sincronicidad` | 92 | review: merge |
| `bigdata` | `big data` | 91 | review: merge |
| `in-company` | `in company` | 91 | review: merge |
| `uniéndono` | `unirse` | 91 | review: merge |
| `auto-proclamado` | `autoproclamado` | 90 | review: merge |
| `filisteosfilisteo` | `filisteo` | 90 | review: merge |
| `go-kart` | `kart` | 90 | review: merge |
| `martingale` | `martingala` | 90 | review: merge |
| `pre-incas` | `preinca` | 90 | review: merge |
| `emplee` | `emplear` | 89 | review: merge |
| `explícal` | `explicar` | 89 | review: merge |
| `mudarno` | `mudarse` | 89 | review: merge |
| `re-elección` | `reelección` | 89 | review: merge |
| `thermos` | `termo` | 89 | review: merge |
| `exigiéndol` | `exigir` | 88 | review: merge |
| `anti-deslizante` | `antideslizante` | 87 | review: merge |
| `co-estrella` | `coestrella` | 87 | review: merge |
| `ex-post` | `ex post` | 87 | review: merge |
| `brochur` | `brochure` | 86 | review: merge |
| `contra-ángulo` | `contraángulo` | 86 | review: merge |
| `levantóse` | `levantarse` | 86 | review: merge |
| `meditad` | `meditar` | 86 | review: merge |
| `posicionándono` | `posicionarse` | 86 | review: merge |
| `anti-gay` | `antigay` | 85 | review: merge |
| `controversias` | `controversia` | 85 | review: merge |
| `pro-activa` | `proactivo` | 85 | review: merge |
| `servío` | `servirse` | 85 | review: merge |
| `díganl` | `decir` | 84 | review: merge |
| `aplicá` | `aplicar` | 83 | review: merge |
| `cobertero` | `cobertera` | 83 | review: merge |
| `extraibl` | `extraíble` | 83 | review: merge |
| `leukemia` | `leucemia` | 83 | review: merge |
| `audior` | `audio` | 82 | review: merge |
| `abandonados` | `abandonado` | 81 | review: merge |
| `adherirno` | `adherirse` | 81 | review: merge |
| `controlarno` | `controlarse` | 81 | review: merge |
| `descárgalo` | `descargar` | 81 | review: merge |
| `excederá` | `exceder` | 81 | review: merge |
| `largometrajes` | `largometraje` | 81 | review: merge |
| `reconocimientos` | `reconocimiento` | 81 | review: merge |
| `reyesrey` | `rey` | 81 | review: merge |
| `room-service` | `room service` | 81 | review: merge |
| `súper-tierra` | `supertierra` | 81 | review: merge |
| `acuariana` | `acuariano` | 80 | review: merge |
| `druid` | `druida` | 98 | review: merge |
| `fashionistas` | `fashionista` | 98 | review: merge |
| `reyno` | `reino` | 98 | review: merge |
| `streamers` | `streamer` | 98 | review: merge |
| `viértela` | `verter` | 98 | review: merge |
| `ajuarar` | `ajuar` | 97 | review: merge |
| `animarle` | `animar` | 97 | review: merge |
| `apícolas` | `apícola` | 97 | review: merge |
| `biblicas` | `bíblico` | 97 | review: merge |
| `concretiza` | `concretizar` | 97 | review: merge |
| `correciones` | `corrección` | 97 | review: merge |
| `cumunidad` | `comunidad` | 97 | review: merge |
| `huequito` | `hueco` | 97 | review: merge |
| `lense` | `lente` | 97 | review: merge |
| `ofrecio` | `ofrecer` | 97 | review: merge |
| `yazidis` | `yazidí` | 97 | review: merge |
| `seguiriya` | `siguiriya` | 96 | review: merge |
| `archiconocida` | `archiconocido` | 95 | review: merge |
| `habiéndolo` | `haber` | 95 | review: merge |
| `listando` | `listar` | 95 | review: merge |
| `milenials` | `milenial` | 95 | review: merge |
| `twitteó` | `tuitear` | 95 | review: merge |
| `bebito` | `bebé` | 94 | review: merge |
| `dirigío` | `dirigirse` | 94 | review: merge |
| `erigiéndose` | `erigirse` | 94 | review: merge |
| `estatica` | `estático` | 94 | review: merge |
| `habilítelo` | `habilitar` | 94 | review: merge |
| `precortadas` | `precortado` | 94 | review: merge |
| `sáquela` | `sacar` | 94 | review: merge |
| `testea` | `testear` | 94 | review: merge |
| `cigarillo` | `cigarrillo` | 93 | review: merge |
| `dadlo` | `dar` | 93 | review: merge |
| `desagradecer` | `desagradecido` | 93 | review: merge |
| `flúido` | `fluido` | 93 | review: merge |
| `imporante` | `importante` | 93 | review: merge |
| `millenial` | `milenial` | 93 | review: merge |
| `notificándole` | `notificar` | 93 | review: merge |
| `pensá` | `pensar` | 93 | review: merge |
| `párkings` | `párking` | 93 | review: merge |
| `sobrescriba` | `sobrescribir` | 93 | review: merge |
| `sérums` | `sérum` | 93 | review: merge |
| `testeados` | `testear` | 93 | review: merge |
| `urbanitas` | `urbanita` | 93 | review: merge |
| `candelita` | `candela` | 92 | review: merge |
| `carácteristica` | `característica` | 92 | review: merge |
| `hacédmelo` | `hacer` | 92 | review: merge |
| `perdónenme` | `perdonar` | 92 | review: merge |
| `precortada` | `precortado` | 92 | review: merge |
| `rosacea` | `rosácea` | 92 | review: merge |
| `transplantado` | `trasplantado` | 92 | review: merge |
| `aleatorizada` | `aleatorizado` | 91 | review: merge |
| `disenter` | `disentería` | 91 | review: merge |
| `genetica` | `genética` | 91 | review: merge |
| `oaxaqueñas` | `oaxaqueño` | 91 | review: merge |
| `satisfación` | `satisfacción` | 91 | review: merge |
| `utilícela` | `utilizar` | 91 | review: merge |
| `aproximádamente` | `aproximadamente` | 90 | review: merge |
| `cianobacterias` | `cianobacteria` | 90 | review: merge |
| `cocerlo` | `cocer` | 90 | review: merge |
| `dejaro` | `dejarse` | 90 | review: merge |
| `edifício` | `edificio` | 90 | review: merge |
| `frótela` | `frotar` | 90 | review: merge |
| `homofóbicas` | `homofóbico` | 90 | review: merge |
| `ministre` | `ministrar` | 90 | review: merge |
| `acuñó` | `acuñar` | 89 | review: merge |
| `intrínsicamente` | `intrínsecamente` | 89 | review: merge |
| `llenándolo` | `llenar` | 89 | review: merge |
| `performática` | `performático` | 89 | review: merge |
| `reinaugurado` | `reinaugurar` | 89 | review: merge |
| `trolleys` | `trolley` | 89 | review: merge |
| `afgani` | `afgano` | 88 | review: merge |
| `antijudía` | `antijudío` | 88 | review: merge |
| `autoproclamada` | `autoproclamado` | 88 | review: merge |
| `bumer` | `bumerán` | 88 | review: merge |
| `cilíndro` | `cilindro` | 88 | review: merge |
| `extención` | `extensión` | 88 | review: merge |
| `interétnicas` | `interétnico` | 88 | review: merge |
| `ministrado` | `ministrar` | 88 | review: merge |
| `mueso` | `museo` | 88 | review: merge |
| `postean` | `postear` | 88 | review: merge |
| `xylitol` | `xilitol` | 88 | review: merge |
| `abstente` | `abstenerse` | 87 | review: merge |
| `consúmate` | `consumirse` | 87 | review: merge |
| `escofinar` | `escofina` | 87 | review: merge |
| `explicándole` | `explicar` | 87 | review: merge |
| `frótate` | `frotarse` | 87 | review: merge |
| `informaci` | `información` | 87 | review: merge |
| `santifícalo` | `santificar` | 87 | review: merge |
| `suavecito` | `suave` | 87 | review: merge |
| `tené` | `tener` | 87 | review: merge |
| `trimar` | `trimarán` | 87 | review: merge |
| `yanki` | `yanqui` | 87 | review: merge |
| `geolocalizada` | `geolocalizado` | 86 | review: merge |
| `identificarlo` | `identificar` | 86 | review: merge |
| `influente` | `influyente` | 86 | review: merge |
| `noviolentas` | `noviolento` | 86 | review: merge |
| `proponiéndole` | `proponer` | 86 | review: merge |
| `reintrodujo` | `reintroducir` | 86 | review: merge |
| `tene` | `tener` | 86 | review: merge |
| `traslocación` | `translocación` | 86 | review: merge |
| `télefono` | `teléfono` | 86 | review: merge |
| `vols` | `volumen` | 86 | review: merge |
| `crearla` | `crear` | 85 | review: merge |
| `garam` | `garam masala` | 85 | review: merge |
| `lasalianas` | `lasaliano` | 85 | review: merge |
| `reprograma` | `reprogramar` | 85 | review: merge |
| `anticipatoria` | `anticipatorio` | 84 | review: merge |
| `arquita` | `arca` | 84 | review: merge |
| `cientificas` | `científico` | 84 | review: merge |
| `acoplabl` | `acoplable` | 92 | review: merge |
| `afro-descendiente` | `afrodescendiente` | 92 | review: merge |
| `ex-ministro` | `exministro` | 92 | review: merge |
| `costes` | `coste` | 91 | review: merge |
| `falcifor` | `falciforme` | 91 | review: merge |
| `incorporada` | `incorporado` | 91 | review: merge |
| `anti-niebla` | `antiniebla` | 90 | review: merge |
| `bussiness` | `business` | 90 | review: merge |
| `ecowas` | `cedeao` | 90 | review: merge |
| `semi-industrial` | `semiindustrial` | 90 | review: merge |
| `ultra-lujo` | `ultralujo` | 90 | review: merge |
| `enemigosenemigo` | `enemigo` | 89 | review: merge |
| `puffs` | `puf` | 89 | review: merge |
| `social-demócrata` | `socialdemócrata` | 89 | review: merge |
| `log-in` | `login` | 88 | review: merge |
| `medio-ambiental` | `medioambiental` | 88 | review: merge |
| `notificándono` | `notificar` | 88 | review: merge |
| `purificaos` | `purificar` | 88 | review: merge |
| `ex-testigo` | `extestigo` | 87 | review: merge |
| `inhala` | `inhalar` | 87 | review: merge |
| `re-crear` | `recrear` | 87 | review: merge |
| `brujita` | `bruja` | 86 | review: merge |
| `gloriarno` | `gloriarse` | 86 | review: merge |
| `agrícolo` | `agrícola` | 85 | review: merge |
| `creperie` | `crepería` | 85 | review: merge |
| `fuegofuego` | `fuego` | 85 | review: merge |
| `multi-tarea` | `multitarea` | 85 | review: merge |
| `reconectarno` | `reconectarse` | 85 | review: merge |
| `semi-privado` | `semiprivado` | 85 | review: merge |
| `devolviéndol` | `devolver` | 84 | review: merge |
| `hipodermi` | `hipodermis` | 84 | review: merge |
| `háblal` | `hablar` | 84 | review: merge |
| `pre-aprobado` | `preaprobado` | 84 | review: merge |
| `desiertodesierto` | `desierto` | 83 | review: merge |
| `llenadore` | `llenador` | 83 | review: merge |
| `montabl` | `montable` | 83 | review: merge |
| `norte-oeste` | `noroeste` | 83 | review: merge |
| `palabrapalabra` | `palabra` | 83 | review: merge |
| `recuérdel` | `recordar` | 83 | review: merge |
| `tfno` | `teléfono` | 83 | review: merge |
| `táctiles` | `táctil` | 83 | review: merge |
| `ayto` | `ayuntamiento` | 82 | review: merge |
| `extra-curricular` | `extracurricular` | 82 | review: merge |
| `portamoneda` | `portamonedas` | 82 | review: merge |
| `reconfigurabl` | `reconfigurable` | 82 | review: merge |
| `shilling` | `chelín` | 82 | review: merge |
| `socio-demográfico` | `sociodemográfico` | 82 | review: merge |
| `ómnibu` | `ómnibus` | 81 | review: merge |
| `déjalo` | `dejar` | 98 | review: merge |
| `golems` | `golem` | 98 | review: merge |
| `palabrer` | `palabrería` | 98 | review: merge |
| `ponedla` | `poner` | 98 | review: merge |
| `potencializa` | `potencializar` | 98 | review: merge |
| `sirgar` | `sirga` | 98 | review: merge |
| `asómate` | `asomarse` | 97 | review: merge |
| `dijo` | `decir` | 97 | review: merge |
| `ebanister` | `ebanistería` | 97 | review: merge |
| `epinephrine` | `epinefrina` | 97 | review: merge |
| `levántelo` | `levantar` | 97 | review: merge |
| `moais` | `moai` | 97 | review: merge |
| `mágia` | `magia` | 97 | review: merge |
| `preconcepciones` | `preconcepción` | 97 | review: merge |
| `biofarmacéuticas` | `biofarmacéutico` | 96 | review: merge |
| `geolocalizadas` | `geolocalizar` | 96 | review: merge |
| `hipoactiva` | `hipoactivo` | 96 | review: merge |
| `retuits` | `retuit` | 96 | review: merge |
| `absorve` | `absorber` | 95 | review: merge |
| `feminina` | `femenino` | 95 | review: merge |
| `mantenme` | `mantener` | 95 | review: merge |
| `permítaseme` | `permitir` | 95 | review: merge |
| `reclasificados` | `reclasificar` | 95 | review: merge |
| `respondedme` | `responder` | 95 | review: merge |
| `altaner` | `altanería` | 94 | review: merge |
| `antirresbaladiza` | `antirresbaladizo` | 94 | review: merge |
| `enculada` | `encular` | 94 | review: merge |
| `habitacione` | `habitación` | 94 | review: merge |
| `hipocarbónica` | `hipocarbónico` | 94 | review: merge |
| `múdate` | `mudarse` | 94 | review: merge |
| `testeadas` | `testear` | 94 | review: merge |
| `asígnele` | `asignar` | 93 | review: merge |
| `enfríar` | `enfriar` | 93 | review: merge |
| `gírala` | `girar` | 93 | review: merge |
| `herid` | `herir` | 93 | review: merge |
| `hiperrealistas` | `hiperrealista` | 93 | review: merge |
| `ruter` | `router` | 93 | review: merge |
| `sumergiéndolo` | `sumergir` | 93 | review: merge |
| `banera` | `bañera` | 92 | review: merge |
| `osteoporóticas` | `osteoporótico` | 92 | review: merge |
| `tangara` | `tángara` | 92 | review: merge |
| `acesorio` | `accesorio` | 91 | review: merge |
| `bendiciéndolo` | `bendecir` | 91 | review: merge |
| `buenisimo` | `bueno` | 91 | review: merge |
| `edítalo` | `editar` | 91 | review: merge |
| `gengibre` | `jengibre` | 91 | review: merge |
| `hemodinámicas` | `hemodinámico` | 91 | review: merge |
| `leit` | `leitmotiv` | 91 | review: merge |
| `alrrededor` | `alrededor` | 90 | review: merge |
| `fotocatalítica` | `fotocatalítico` | 90 | review: merge |
| `harálo` | `hacer` | 90 | review: merge |
| `insisto` | `insistir` | 90 | review: merge |
| `ropita` | `ropa` | 90 | review: merge |
| `substracción` | `sustracción` | 90 | review: merge |
| `bioidénticas` | `bioidéntico` | 89 | review: merge |
| `disponte` | `disponerse` | 89 | review: merge |
| `entonce` | `entonces` | 89 | review: merge |
| `immediatamente` | `inmediatamente` | 89 | review: merge |
| `interpretarlo` | `interpretar` | 89 | review: merge |
| `jajaj` | `jaja` | 89 | review: merge |
| `malísima` | `malo` | 89 | review: merge |
| `muestrea` | `muestrear` | 89 | review: merge |
| `robusteza` | `robustez` | 89 | review: merge |
| `tomadlo` | `tomar` | 89 | review: merge |
| `decidlo` | `decir` | 88 | review: merge |
| `empezá` | `empezar` | 88 | review: merge |
| `hidrofílica` | `hidrofílico` | 88 | review: merge |
| `idish` | `yidis` | 88 | review: merge |
| `microblogs` | `microblog` | 88 | review: merge |
| `mirándote` | `mirar` | 88 | review: merge |
| `mútua` | `mutua` | 88 | review: merge |
| `nigún` | `ningún` | 88 | review: merge |
| `província` | `provincia` | 88 | review: merge |
| `adquiéralo` | `adquirir` | 87 | review: merge |
| `atribuyéndole` | `atribuir` | 87 | review: merge |
| `coneccion` | `conexión` | 87 | review: merge |
| `externalizada` | `externalizar` | 87 | review: merge |
| `hiriólo` | `herir` | 87 | review: merge |
| `ranitidine` | `ranitidina` | 87 | review: merge |
| `antitetánica` | `antitetánico` | 86 | review: merge |
| `enfocándose` | `enfocarse` | 86 | review: merge |
| `incomodo` | `incómodo` | 86 | review: merge |
| `serializada` | `serializar` | 86 | review: merge |
| `superfice` | `superficie` | 86 | review: merge |
| `tensiona` | `tensionar` | 86 | review: merge |
| `arrepentiras` | `arrepentirse` | 85 | review: merge |
| `communidad` | `comunidad` | 85 | review: merge |
| `desestructurados` | `desestructurado` | 85 | review: merge |
| `escuchándola` | `escuchar` | 85 | review: merge |
| `mensajito` | `mensaje` | 85 | review: merge |
| `nootropic` | `nootrópico` | 85 | review: merge |
| `stablecoins` | `stablecoin` | 85 | review: merge |
| `tantísima` | `tanto` | 85 | review: merge |
| `valdiviana` | `valdiviano` | 85 | review: merge |
| `alojativa` | `alojativo` | 84 | review: merge |
| `atrápame` | `atrapar` | 84 | review: merge |
| `avisándole` | `avisar` | 84 | review: merge |
| `dedicarl` | `dedicar` | 93 | review: merge |
| `eco-eficiencia` | `ecoeficiencia` | 92 | review: merge |
| `laminada` | `laminado` | 92 | review: merge |
| `quimioprofilaxi` | `quimioprofilaxis` | 92 | review: merge |
| `anti-colisión` | `anticolisión` | 91 | review: merge |
| `comprometámono` | `comprometerse` | 91 | review: merge |
| `covariabl` | `covariable` | 91 | review: merge |
| `euro-mediterránea` | `euromediterráneo` | 91 | review: merge |
| `terrazzo` | `terrazo` | 91 | review: merge |
| `unámono` | `unirse` | 91 | review: merge |
| `adaptándol` | `adaptar` | 90 | review: merge |
| `animao` | `animarse` | 90 | review: merge |
| `enfrentándono` | `enfrentarse` | 90 | review: merge |
| `pcia` | `provincia` | 90 | review: merge |
| `racquetball` | `raquetbol` | 90 | review: merge |
| `rhesu` | `rhesus` | 90 | review: merge |
| `advertido` | `advertir` | 89 | review: merge |
| `juré` | `jurar` | 89 | review: merge |
| `polihidramnio` | `polihidramnios` | 89 | review: merge |
| `vaisnavas` | `vaisnava` | 89 | review: merge |
| `aplicacisn` | `aplicación` | 88 | review: merge |
| `insulino-dependiente` | `insulinodependiente` | 88 | review: merge |
| `portacoche` | `portacoches` | 88 | review: merge |
| `censurado` | `censurar` | 87 | review: merge |
| `determina` | `determinar` | 87 | review: merge |
| `interamericana` | `interamericano` | 87 | review: merge |
| `multi-efecto` | `multiefecto` | 87 | review: merge |
| `adaptor` | `adaptador` | 86 | review: merge |
| `pólvor` | `pólvora` | 86 | review: merge |
| `co-organizador` | `coorganizador` | 85 | review: merge |
| `re-diseño` | `rediseño` | 85 | review: merge |
| `vitro-cerámica` | `vitrocerámica` | 85 | review: merge |
| `cefixime` | `cefixima` | 84 | review: merge |
| `ganarl` | `ganar` | 84 | review: merge |
| `ginko` | `ginkgo` | 84 | review: merge |
| `protegiéndono` | `proteger` | 84 | review: merge |
| `acogero` | `acoger` | 83 | review: merge |
| `auto-suficiencia` | `autosuficiencia` | 83 | review: merge |
| `beta-bloqueante` | `betabloqueante` | 83 | review: merge |
| `chipotl` | `chipotle` | 83 | review: merge |
| `indicándono` | `indicar` | 83 | review: merge |
| `plexi` | `plexiglás` | 83 | review: merge |
| `agradecimientos` | `agradecimiento` | 82 | review: merge |
| `arribos` | `arribo` | 82 | review: merge |
| `disfruté` | `disfrutar` | 82 | review: merge |
| `fabulosas` | `fabuloso` | 82 | review: merge |
| `galimatía` | `galimatías` | 82 | review: merge |
| `llenad` | `llenar` | 82 | review: merge |
| `metoclopramide` | `metoclopramida` | 82 | review: merge |
| `querei` | `querer` | 82 | review: merge |
| `transceiver` | `transceptor` | 82 | review: merge |
| `acercao` | `acercarse` | 81 | review: merge |
| `agnus` | `agnus dei` | 81 | review: merge |
| `concédeno` | `conceder` | 81 | review: merge |
| `eco-eficiente` | `ecoeficiente` | 81 | review: merge |
| `formaciónformación` | `formación` | 81 | review: merge |
| `fusionarno` | `fusionarse` | 81 | review: merge |
| `jute` | `yute` | 81 | review: merge |
| `mini-álbum` | `miniálbum` | 81 | review: merge |
| `vice-versa` | `viceversa` | 81 | review: merge |
| `casos` | `caso` | 98 | review: merge |
| `claúsula` | `cláusula` | 98 | review: merge |
| `enviadme` | `enviar` | 98 | review: merge |
| `gorditas` | `gordito` | 98 | review: merge |
| `voluntarixs` | `voluntario` | 98 | review: merge |
| `creisteis` | `creer` | 97 | review: merge |
| `hipocalórica` | `hipocalórico` | 97 | review: merge |
| `háganse` | `hacerse` | 97 | review: merge |
| `ninis` | `nini` | 97 | review: merge |
| `añadiéndolo` | `añadir` | 96 | review: merge |
| `escán` | `escáner` | 96 | review: merge |
| `fluída` | `fluido` | 96 | review: merge |
| `hechicer` | `hechicería` | 96 | review: merge |
| `parapanamericanos` | `parapanamericano` | 96 | review: merge |
| `péguela` | `pegar` | 96 | review: merge |
| `telefonos` | `teléfono` | 96 | review: merge |
| `acompañándo` | `acompañar` | 95 | review: merge |
| `albúm` | `álbum` | 95 | review: merge |
| `intentándolo` | `intentar` | 95 | review: merge |
| `levothyroxine` | `levotiroxina` | 95 | review: merge |
| `muuuuy` | `muy` | 95 | review: merge |
| `organizarla` | `organizar` | 95 | review: merge |
| `persiguiéndolo` | `perseguir` | 95 | review: merge |
| `recojer` | `recoger` | 95 | review: merge |
| `antropomorfa` | `antropomorfo` | 94 | review: merge |
| `despídase` | `despedirse` | 94 | review: merge |
| `disminuído` | `disminuido` | 94 | review: merge |
| `especialemente` | `especialmente` | 94 | review: merge |
| `meciéndose` | `mecerse` | 94 | review: merge |
| `reemplazándolo` | `reemplazar` | 94 | review: merge |
| `sobrescriban` | `sobrescribir` | 94 | review: merge |
| `testeando` | `testear` | 94 | review: merge |
| `deslizándote` | `deslizarse` | 93 | review: merge |
| `juntxs` | `junto` | 93 | review: merge |
| `recuérde` | `recordar` | 93 | review: merge |
| `rodiada` | `rodiado` | 93 | review: merge |
| `sorbito` | `sorbo` | 93 | review: merge |
| `trabajito` | `trabajo` | 93 | review: merge |
| `arequipeña` | `arequipeño` | 92 | review: merge |
| `cannabinoid` | `cannabinoide` | 92 | review: merge |
| `envuélvalo` | `envolver` | 92 | review: merge |
| `fluídica` | `fluídico` | 92 | review: merge |
| `proporcionás` | `proporcionar` | 92 | review: merge |
| `seleccionalo` | `seleccionar` | 92 | review: merge |
| `bástate` | `bastar` | 91 | review: merge |
| `desinformados` | `desinformado` | 91 | review: merge |
| `estatinas` | `estatina` | 91 | review: merge |
| `hileradores` | `hilerador` | 91 | review: merge |
| `independente` | `independiente` | 91 | review: merge |
| `neurogénica` | `neurogénico` | 91 | review: merge |
| `preguntémonos` | `preguntarse` | 91 | review: merge |
| `recoje` | `recoger` | 91 | review: merge |
| `autoritativa` | `autoritativo` | 90 | review: merge |
| `deselecciona` | `deseleccionar` | 90 | review: merge |
| `estol` | `estola` | 90 | review: merge |
| `examínese` | `examinarse` | 90 | review: merge |
| `interioriza` | `interiorizar` | 90 | review: merge |
| `legrar` | `legrado` | 90 | review: merge |
| `lúpica` | `lúpico` | 90 | review: merge |
| `premezclados` | `premezclado` | 90 | review: merge |
| `redilar` | `redil` | 90 | review: merge |
| `sujetándola` | `sujetar` | 90 | review: merge |
| `consiéntase` | `consentirse` | 89 | review: merge |
| `familar` | `familiar` | 89 | review: merge |
| `fuéle` | `ser` | 89 | review: merge |
| `guardándola` | `guardar` | 89 | review: merge |
| `odontologicas` | `odontológico` | 89 | review: merge |
| `quarterbacks` | `quarterback` | 89 | review: merge |
| `redireccione` | `redireccionar` | 89 | review: merge |
| `teatralizada` | `teatralizado` | 89 | review: merge |
| `élfica` | `élfico` | 89 | review: merge |
| `arrastrándola` | `arrastrar` | 88 | review: merge |
| `brevísima` | `breve` | 88 | review: merge |
| `clarithromycin` | `claritromicina` | 88 | review: merge |
| `hornéalo` | `hornear` | 88 | review: merge |
| `lindísima` | `lindo` | 88 | review: merge |
| `mismísimas` | `mismo` | 88 | review: merge |
| `pecanas` | `pecana` | 88 | review: merge |
| `socórreme` | `socorrer` | 88 | review: merge |
| `tranferencia` | `transferencia` | 88 | review: merge |
| `zurriagar` | `zurriago` | 88 | review: merge |
| `acogiéndose` | `acogerse` | 87 | review: merge |
| `competividad` | `competitividad` | 87 | review: merge |
| `disenados` | `diseñar` | 87 | review: merge |
| `eletrónico` | `electrónico` | 87 | review: merge |
| `pizarrones` | `pizarrón` | 87 | review: merge |
| `preguntadle` | `preguntar` | 87 | review: merge |
| `renderizados` | `renderizado` | 87 | review: merge |
| `semillita` | `semilla` | 87 | review: merge |
| `viajecito` | `viaje` | 87 | review: merge |
| `alcanze` | `alcance` | 86 | review: merge |
| `canillero` | `canillera` | 86 | review: merge |
| `desecharla` | `desechar` | 86 | review: merge |
| `enjuáguela` | `enjuagar` | 86 | review: merge |
| `fakes` | `fake` | 86 | review: merge |
| `foodies` | `foodie` | 86 | review: merge |
| `relájense` | `relajarse` | 86 | review: merge |
| `sonografico` | `sonográfico` | 86 | review: merge |
| `tematizadas` | `tematizado` | 86 | review: merge |
| `antiquísimos` | `antiguo` | 85 | review: merge |
| `buldóceres` | `buldócer` | 85 | review: merge |
| `calefación` | `calefacción` | 85 | review: merge |
| `computadorizada` | `computadorizado` | 85 | review: merge |
| `desafíate` | `desafiar` | 85 | review: merge |
| `elíxir` | `elixir` | 85 | review: merge |
| `excusión` | `excursión` | 85 | review: merge |
| `hipsters` | `hipster` | 85 | review: merge |
| `mquina` | `máquina` | 85 | review: merge |
| `quántum` | `quantum` | 85 | review: merge |
| `sectorizada` | `sectorizado` | 85 | review: merge |
| `semiprivadas` | `semiprivado` | 85 | review: merge |
| `sustituído` | `sustituir` | 85 | review: merge |
| `alquien` | `alguien` | 84 | review: merge |
| `autodenominada` | `autodenominado` | 84 | review: merge |
| `bikiní` | `bikini` | 84 | review: merge |
| `comentário` | `comentario` | 84 | review: merge |
| `confie` | `confiar` | 84 | review: merge |
| `aplicándol` | `aplicar` | 93 | review: merge |
| `chollos` | `chollo` | 93 | review: merge |
| `negro-jack` | `blackjack` | 93 | review: merge |
| `yin-yang` | `yin yang` | 93 | review: merge |
| `auto-destrucción` | `autodestrucción` | 92 | review: merge |
| `co-creativo` | `cocreativo` | 92 | review: merge |
| `pre-inca` | `preinca` | 92 | review: merge |
| `au-pair` | `au pair` | 91 | review: merge |
| `dracaena` | `drácena` | 91 | review: merge |
| `opec` | `opep` | 91 | review: merge |
| `triangulo` | `triángulo` | 91 | review: merge |
| `acordándono` | `acordarse` | 90 | review: merge |
| `preparémono` | `prepararse` | 90 | review: merge |
| `valkiria` | `valquiria` | 90 | review: merge |
| `huid` | `huir` | 89 | review: merge |
| `orooro` | `oro` | 89 | review: merge |
| `mini-mercado` | `minimercado` | 88 | review: merge |
| `pickl` | `pickles` | 88 | review: merge |
| `asociándono` | `asociarse` | 87 | review: merge |
| `fotogrametr` | `fotogrametría` | 87 | review: merge |
| `micro-organismo` | `microorganismo` | 87 | review: merge |
| `poderl` | `poder` | 87 | review: merge |
| `pro-vitamina` | `provitamina` | 87 | review: merge |
| `proponerl` | `proponer` | 87 | review: merge |
| `medio-ambiente` | `medio ambiente` | 86 | review: merge |
| `presentarno` | `presentarse` | 86 | review: merge |
| `socio-demográficas` | `sociodemográfico` | 86 | review: merge |
| `sub-nacional` | `subnacional` | 86 | review: merge |
| `advertirl` | `advertir` | 85 | review: merge |
| `anti-choque` | `antichoque` | 85 | review: merge |
| `casbah` | `casba` | 85 | review: merge |
| `cubano-americana` | `cubanoamericano` | 85 | review: merge |
| `inumerabl` | `inumerable` | 85 | review: merge |
| `respondióle` | `responder` | 85 | review: merge |
| `saludarl` | `saludar` | 85 | review: merge |
| `siguiéndono` | `seguir` | 85 | review: merge |
| `chitosan` | `quitosano` | 84 | review: merge |
| `go-karts` | `kart` | 84 | review: merge |
| `infaltabl` | `infaltable` | 84 | review: merge |
| `jet-set` | `jet set` | 84 | review: merge |
| `arrebatándo` | `arrebatar` | 83 | review: merge |
| `defenderno` | `defenderse` | 83 | review: merge |
| `goggl` | `goggles` | 83 | review: merge |
| `loperamide` | `loperamida` | 83 | review: merge |
| `síganos` | `seguir` | 83 | review: merge |
| `aguaagua` | `agua` | 82 | review: merge |
| `bohio` | `bohío` | 82 | review: merge |
| `co-escrito` | `coescribir` | 82 | review: merge |
| `escríbeno` | `escribir` | 82 | review: merge |
| `adelantándono` | `adelantarse` | 81 | review: merge |
| `archaea` | `arquea` | 81 | review: merge |
| `dividiéndol` | `dividir` | 81 | review: merge |
| `semi-rígido` | `semirrígido` | 81 | review: merge |
| `cocerla` | `cocer` | 98 | review: merge |
| `edítala` | `editar` | 98 | review: merge |
| `emitado` | `emitir` | 98 | review: merge |
| `funcionamento` | `funcionamiento` | 98 | review: merge |
| `márqueting` | `marketing` | 98 | review: merge |
| `portacarga` | `portacargas` | 98 | review: merge |
| `prequirúrgica` | `prequirúrgico` | 98 | review: merge |
| `rubiecita` | `rubio` | 98 | review: merge |
| `tómalo` | `tomar` | 98 | review: merge |
| `ayudadme` | `ayudar` | 97 | review: merge |
| `coje` | `coger` | 97 | review: merge |
| `enriqueciéndose` | `enriquecerse` | 97 | review: merge |
| `escuchá` | `escuchar` | 97 | review: merge |
| `infórmense` | `informarse` | 97 | review: merge |
| `monstruito` | `monstruo` | 97 | review: merge |
| `amaderadas` | `amaderado` | 96 | review: merge |
| `baristas` | `barista` | 96 | review: merge |
| `gorgojar` | `gorgojo` | 96 | review: merge |
| `muestreada` | `muestrear` | 96 | review: merge |
| `observándola` | `observar` | 96 | review: merge |
| `precancerosa` | `precanceroso` | 96 | review: merge |
| `rodeándola` | `rodear` | 96 | review: merge |
| `santisima` | `santo` | 96 | review: merge |
| `calefactada` | `calefactar` | 95 | review: merge |
| `cuécelo` | `cocer` | 95 | review: merge |
| `desiciones` | `decisión` | 95 | review: merge |
| `echadlo` | `echar` | 95 | review: merge |
| `fragrancia` | `fragancia` | 95 | review: merge |
| `gintonic` | `gin-tonic` | 95 | review: merge |
| `juzgad` | `juzgar` | 95 | review: merge |
| `terasse` | `terraza` | 95 | review: merge |
| `transmitiéndose` | `transmitir` | 95 | review: merge |
| `basándo` | `basarse` | 94 | review: merge |
| `botellones` | `botellón` | 94 | review: merge |
| `chics` | `chic` | 94 | review: merge |
| `diminuir` | `disminuir` | 94 | review: merge |
| `haberlo` | `haber` | 94 | review: merge |
| `mediúmnicas` | `mediúmnico` | 94 | review: merge |
| `hackea` | `hackear` | 93 | review: merge |
| `leguaje` | `lenguaje` | 93 | review: merge |
| `oyéndolo` | `oír` | 93 | review: merge |
| `pensad` | `pensar` | 93 | review: merge |
| `retazar` | `retazo` | 93 | review: merge |
| `averigue` | `averiguar` | 92 | review: merge |
| `cabar` | `cabaré` | 92 | review: merge |
| `caulquier` | `cualquier` | 92 | review: merge |
| `ergométrica` | `ergométrico` | 92 | review: merge |
| `excellente` | `excelente` | 92 | review: merge |
| `georreferenciados` | `georreferenciado` | 92 | review: merge |
| `internalizado` | `internalizar` | 92 | review: merge |
| `museográfica` | `museográfico` | 92 | review: merge |
| `reprogramados` | `reprogramar` | 92 | review: merge |
| `senal` | `señal` | 92 | review: merge |
| `antimicótica` | `antimicótico` | 91 | review: merge |
| `créanlo` | `creer` | 91 | review: merge |
| `etil` | `etilo` | 91 | review: merge |
| `evangelísticas` | `evangelístico` | 91 | review: merge |
| `ketoprofen` | `ketoprofeno` | 91 | review: merge |
| `mesurable` | `mensurable` | 91 | review: merge |
| `preocues` | `preocuparse` | 91 | review: merge |
| `protegerlo` | `proteger` | 91 | review: merge |
| `ultramodernas` | `ultramoderno` | 91 | review: merge |
| `vmdeo` | `vídeo` | 91 | review: merge |
| `conexi` | `conexión` | 90 | review: merge |
| `crucer` | `crucería` | 90 | review: merge |
| `deconstruye` | `deconstruir` | 90 | review: merge |
| `enfrentándose` | `enfrentarse` | 90 | review: merge |
| `estrendo` | `estreno` | 90 | review: merge |
| `incluídos` | `incluido` | 90 | review: merge |
| `intricado` | `intrincado` | 90 | review: merge |
| `mapean` | `mapear` | 90 | review: merge |
| `muuuucho` | `mucho` | 90 | review: merge |
| `reenvasado` | `reenvasar` | 90 | review: merge |
| `requintar` | `requinto` | 90 | review: merge |
| `rigiéndose` | `regirse` | 90 | review: merge |
| `soportándoos` | `soportar` | 90 | review: merge |
| `aereopuerto` | `aeropuerto` | 89 | review: merge |
| `angioplastía` | `angioplastia` | 89 | review: merge |
| `bioeléctrica` | `bioeléctrico` | 89 | review: merge |
| `contrayéndose` | `contraerse` | 89 | review: merge |
| `deslízala` | `deslizar` | 89 | review: merge |
| `moverla` | `mover` | 89 | review: merge |
| `muuucho` | `mucho` | 89 | review: merge |
| `posquirúrgica` | `posquirúrgico` | 89 | review: merge |
| `promielocítica` | `promielocítico` | 89 | review: merge |
| `segundario` | `secundario` | 89 | review: merge |
| `viértelo` | `verter` | 89 | review: merge |
| `aera` | `área` | 88 | review: merge |
| `contentísimo` | `contento` | 88 | review: merge |
| `llevarla` | `llevar` | 88 | review: merge |
| `metabolizada` | `metabolizar` | 88 | review: merge |
| `proponiéndose` | `proponerse` | 88 | review: merge |
| `tráigalo` | `traer` | 88 | review: merge |
| `zambúllete` | `zambullirse` | 88 | review: merge |
| `conoceis` | `conocer` | 87 | review: merge |
| `cómprale` | `comprar` | 87 | review: merge |
| `dificilísimo` | `difícil` | 87 | review: merge |
| `entendiéndola` | `entender` | 87 | review: merge |
| `geminar` | `geminado` | 87 | review: merge |
| `integrándola` | `integrar` | 87 | review: merge |
| `llámenme` | `llamar` | 87 | review: merge |
| `límpiese` | `limpiar` | 87 | review: merge |
| `mátenlo` | `matar` | 87 | review: merge |
| `paddel` | `pádel` | 87 | review: merge |
| `satisfecen` | `satisfacer` | 87 | review: merge |
| `sicoterapia` | `psicoterapia` | 87 | review: merge |
| `sobreponiéndose` | `sobreponerse` | 87 | review: merge |
| `teconología` | `tecnología` | 87 | review: merge |
| `viritual` | `virtual` | 87 | review: merge |
| `carino` | `cariño` | 86 | review: merge |
| `marginalizados` | `marginalizado` | 86 | review: merge |
| `mímese` | `mimar` | 86 | review: merge |
| `oculoplástica` | `oculoplástico` | 86 | review: merge |
| `portatraje` | `portatrajes` | 86 | review: merge |
| `autentico` | `auténtico` | 85 | review: merge |
| `construímos` | `construir` | 85 | review: merge |
| `dialógicas` | `dialógico` | 85 | review: merge |
| `engañándoos` | `engañarse` | 85 | review: merge |
| `exitante` | `excitante` | 85 | review: merge |
| `makis` | `maki` | 85 | review: merge |
| `preordenado` | `preordenar` | 85 | review: merge |
| `sentira` | `sentir` | 85 | review: merge |
| `sumergirlo` | `sumergir` | 85 | review: merge |
| `taaan` | `tan` | 85 | review: merge |
| `trazodone` | `trazodona` | 85 | review: merge |
| `aplicadar` | `aplicar` | 84 | review: merge |
| `copito` | `copo` | 84 | review: merge |
| `anti-aborto` | `antiaborto` | 80 | review: merge |
| `auto-gestión` | `autogestión` | 80 | review: merge |
| `crucifor` | `cruciforme` | 80 | review: merge |
| `discreta` | `discreto` | 80 | review: merge |
| `especímene` | `espécimen` | 80 | review: merge |
| `houthi` | `hutí` | 80 | review: merge |
| `proponiéndol` | `proponer` | 80 | review: merge |
| `sabores` | `sabor` | 80 | review: merge |
| `sub-licenciable` | `sublicenciable` | 80 | review: merge |
| `anti-rayado` | `antirrayado` | 79 | review: merge |
| `co-diseño` | `codiseño` | 79 | review: merge |
| `congregarlo` | `congregar` | 79 | review: merge |
| `eco-amigable` | `ecoamigable` | 79 | review: merge |
| `envieno` | `enviar` | 79 | review: merge |
| `lavaparabrisa` | `lavaparabrisas` | 79 | review: merge |
| `ultra-delgada` | `ultradelgado` | 79 | review: merge |
| `video-clip` | `videoclip` | 79 | review: merge |
| `cazarrecompensa` | `cazarrecompensas` | 78 | review: merge |
| `configuracisn` | `configuración` | 78 | review: merge |
| `enviano` | `enviar` | 78 | review: merge |
| `linfocitos` | `linfocito` | 78 | review: merge |
| `ofrécel` | `ofrecer` | 78 | review: merge |
| `ultra-moderno` | `ultramoderno` | 78 | review: merge |
| `auto-eficacia` | `autoeficacia` | 77 | review: merge |
| `ex-presidente#Masc` | `expresidente` | 77 | review: merge |
| `lloré` | `llorar` | 77 | review: merge |
| `necesitarán` | `necesitar` | 77 | review: merge |
| `post-crisis` | `poscrisis` | 77 | review: merge |
| `sexie` | `sexi` | 77 | review: merge |
| `sub-sección` | `subsección` | 77 | review: merge |
| `traicionado` | `traicionar` | 77 | review: merge |
| `semi-amueblado` | `semiamueblado` | 76 | review: merge |
| `socio-espacial` | `socioespacial` | 76 | review: merge |
| `declina` | `declinar` | 75 | review: merge |
| `enlazado` | `enlazar` | 75 | review: merge |
| `latinxs` | `latinx` | 75 | review: merge |
| `purifíquense` | `purificarse` | 75 | review: merge |
| `riéndono` | `reírse` | 75 | review: merge |
| `taina` | `taíno` | 75 | review: merge |
| `anti-viral` | `antiviral` | 74 | review: merge |
| `auto-compasión` | `autocompasión` | 74 | review: merge |
| `escobo` | `escoba` | 74 | review: merge |
| `geo-cerca` | `geocerca` | 74 | review: merge |
| `post-electoral` | `postelectoral` | 74 | review: merge |
| `semi-estructuradas` | `semiestructurado` | 74 | review: merge |
| `afro-americanas` | `afroamericano` | 73 | review: merge |
| `ampicillin` | `ampicilina` | 73 | review: merge |
| `desarrolado` | `desarrollado` | 84 | review: merge |
| `estrogenic` | `estrogénico` | 84 | review: merge |
| `ofrecerlo` | `ofrecer` | 84 | review: merge |
| `transpondor` | `transpondedor` | 84 | review: merge |
| `dueno` | `dueño` | 83 | review: merge |
| `encontraro` | `encontrar` | 83 | review: merge |
| `exhibidores` | `exhibidor` | 83 | review: merge |
| `gluones` | `gluón` | 83 | review: merge |
| `hagámoslo` | `hacer` | 83 | review: merge |
| `pasajess` | `pasaje` | 83 | review: merge |
| `recriar` | `recría` | 83 | review: merge |
| `apredizaje` | `aprendizaje` | 82 | review: merge |
| `beneficiándose` | `beneficiarse` | 82 | review: merge |
| `extráigalo` | `extraer` | 82 | review: merge |
| `hidraúlica` | `hidráulico` | 82 | review: merge |
| `insértalo` | `insertar` | 82 | review: merge |
| `limítese` | `limitarse` | 82 | review: merge |
| `personalícelo` | `personalizar` | 82 | review: merge |
| `reposiciona` | `reposicionar` | 82 | review: merge |
| `santificarlo` | `santificar` | 82 | review: merge |
| `venlafaxine` | `venlafaxina` | 82 | review: merge |
| `búsque` | `buscar` | 81 | review: merge |
| `colónica` | `colónico` | 81 | review: merge |
| `evocativa` | `evocativo` | 81 | review: merge |
| `machnovistas` | `machnovista` | 81 | review: merge |
| `mírala` | `mirar` | 81 | review: merge |
| `orecemos` | `ofrecer` | 81 | review: merge |
| `protégete` | `protegerse` | 81 | review: merge |
| `recalcula` | `recalcular` | 81 | review: merge |
| `regocíjese` | `regocijarse` | 81 | review: merge |
| `videoclips` | `videoclip` | 81 | review: merge |
| `apedrearlo` | `apedrear` | 80 | review: merge |
| `empújelo` | `empujar` | 80 | review: merge |
| `interiorizada` | `interiorizado` | 80 | review: merge |
| `mercaderia` | `mercadería` | 80 | review: merge |
| `registar` | `registrar` | 80 | review: merge |
| `remezclada` | `remezclar` | 80 | review: merge |
| `teneís` | `tener` | 80 | review: merge |
| `aguafuer` | `aguafuerte` | 79 | review: merge |
| `alejándome` | `alejarse` | 79 | review: merge |
| `autolimitada` | `autolimitado` | 79 | review: merge |
| `colesistectomía` | `colecistectomía` | 79 | review: merge |
| `copisteria` | `copistería` | 79 | review: merge |
| `demonstraciones` | `demostración` | 79 | review: merge |
| `fríelo` | `freír` | 79 | review: merge |
| `habérselo` | `haber` | 79 | review: merge |
| `jovencísima` | `joven` | 79 | review: merge |
| `malwares` | `malware` | 79 | review: merge |
| `mujere` | `mujer` | 79 | review: merge |
| `proinflamatorias` | `proinflamatorio` | 79 | review: merge |
| `prática` | `práctica` | 79 | review: merge |
| `restaurantera` | `restaurantero` | 79 | review: merge |
| `revenir` | `revenirse` | 79 | review: merge |
| `anticípese` | `anticiparse` | 78 | review: merge |
| `deseándole` | `desear` | 78 | review: merge |
| `esparciéndose` | `esparcirse` | 78 | review: merge |
| `golosinar` | `golosina` | 78 | review: merge |
| `personalísima` | `personal` | 78 | review: merge |
| `porporcionando` | `proporcionar` | 78 | review: merge |
| `rasuradoras` | `rasuradora` | 78 | review: merge |
| `abuhardilladas` | `abuhardillado` | 77 | review: merge |
| `cómos` | `cómo` | 77 | review: merge |
| `dedicándome` | `dedicarse` | 77 | review: merge |
| `descubriéndose` | `descubrir` | 77 | review: merge |
| `infusionado` | `infusionar` | 77 | review: merge |
| `liberándola` | `liberar` | 77 | review: merge |
| `lubrificación` | `lubricación` | 77 | review: merge |
| `déjal` | `dejar` | 80 | review: merge |
| `espritu` | `espíritu` | 80 | review: merge |
| `exhortaro` | `exhortar` | 80 | review: merge |
| `limpiapipa` | `limpiapipas` | 80 | review: merge |
| `longboards` | `longboard` | 80 | review: merge |
| `mercadito` | `mercado` | 80 | review: merge |
| `multi-núcleo` | `multinúcleo` | 80 | review: merge |
| `nereido` | `nereida` | 80 | review: merge |
| `permítal` | `permitir` | 80 | review: merge |
| `re-entrada` | `reentrada` | 80 | review: merge |
| `rendirl` | `rendir` | 80 | review: merge |
| `satana` | `satanás` | 80 | review: merge |
| `abiertasr` | `abierto` | 79 | review: merge |
| `aplausos` | `aplauso` | 79 | review: merge |
| `consultabl` | `consultable` | 79 | review: merge |
| `emoticons` | `emoticono` | 79 | review: merge |
| `epistaxi` | `epistaxis` | 79 | review: merge |
| `ex-jefe` | `exjefe` | 79 | review: merge |
| `restaurativa` | `restaurativo` | 79 | review: merge |
| `semi-privada` | `semiprivado` | 79 | review: merge |
| `feed-back` | `feedback` | 78 | review: merge |
| `pro-capitalista` | `procapitalista` | 78 | review: merge |
| `anti-arañazo` | `antiarañazos` | 77 | review: merge |
| `atenerno` | `atenerse` | 77 | review: merge |
| `feng-shui` | `feng shui` | 77 | review: merge |
| `inspirándono` | `inspirarse` | 77 | review: merge |
| `mandeno` | `mandar` | 77 | review: merge |
| `multi-pantalla` | `multipantalla` | 77 | review: merge |
| `post-soviético` | `postsoviético` | 77 | review: merge |
| `pre-industrial` | `preindustrial` | 77 | review: merge |
| `allopurinol` | `alopurinol` | 76 | review: merge |
| `pre-seleccionados` | `preseleccionar` | 76 | review: merge |
| `web-site` | `website` | 76 | review: merge |
| `interreligiosa` | `interreligioso` | 75 | review: merge |
| `molecule` | `molécula` | 75 | review: merge |
| `sorbida` | `sorber` | 75 | review: merge |
| `sub-región` | `subregión` | 75 | review: merge |
| `anti-héroe` | `antihéroe` | 74 | review: merge |
| `explícita` | `explícito` | 74 | review: merge |
| `mini-torneo` | `minitorneo` | 74 | review: merge |
| `regrababl` | `regrabable` | 74 | review: merge |
| `sub-regional` | `subregional` | 74 | review: merge |
| `animándono` | `animar` | 73 | review: merge |
| `auditabl` | `auditable` | 73 | review: merge |
| `deconstruido` | `deconstruir` | 84 | review: merge |
| `desestacionalizados` | `desestacionalizado` | 84 | review: merge |
| `dijéronle` | `decir` | 84 | review: merge |
| `escuchadle` | `escuchar` | 84 | review: merge |
| `esque` | `es que` | 84 | review: merge |
| `moviéndote` | `moverse` | 84 | review: merge |
| `muyahidin` | `muyahidín` | 84 | review: merge |
| `adaptivo` | `adaptativo` | 83 | review: merge |
| `atreviéndose` | `atreverse` | 83 | review: merge |
| `caraterística` | `característica` | 83 | review: merge |
| `compará` | `comparar` | 83 | review: merge |
| `mapeada` | `mapear` | 83 | review: merge |
| `midiéndose` | `medir` | 83 | review: merge |
| `níque` | `níquel` | 83 | review: merge |
| `quinceanera` | `quinceañera` | 83 | review: merge |
| `sertraline` | `sertralina` | 83 | review: merge |
| `tematizada` | `tematizar` | 83 | review: merge |
| `tornáronse` | `tornarse` | 83 | review: merge |
| `admitámoslo` | `admitir` | 82 | review: merge |
| `aúnque` | `aunque` | 82 | review: merge |
| `bumerang` | `bumerán` | 82 | review: merge |
| `clickar` | `clicar` | 82 | review: merge |
| `cremado` | `cremar` | 82 | review: merge |
| `cítar` | `cítara` | 82 | review: merge |
| `grandísimos` | `grande` | 82 | review: merge |
| `pochado` | `pochar` | 82 | review: merge |
| `acercándome` | `acercarse` | 81 | review: merge |
| `añádala` | `añadir` | 81 | review: merge |
| `desarolla` | `desarrollar` | 81 | review: merge |
| `escúrrelo` | `escurrir` | 81 | review: merge |
| `hiriéndole` | `herir` | 81 | review: merge |
| `pantis` | `panti` | 81 | review: merge |
| `pregúntate` | `preguntarse` | 81 | review: merge |
| `proveyéndole` | `proveer` | 81 | review: merge |
| `salidad` | `salida` | 81 | review: merge |
| `tarjetita` | `tarjeta` | 81 | review: merge |
| `transformándolo` | `transformar` | 81 | review: merge |
| `asíque` | `así que` | 80 | review: merge |
| `capacitándolo` | `capacitar` | 80 | review: merge |
| `focu` | `focus group` | 80 | review: merge |
| `gerenciados` | `gerenciar` | 80 | review: merge |
| `hacerla` | `hacer` | 80 | review: merge |
| `numerosísima` | `numeroso` | 80 | review: merge |
| `palabrita` | `palabra` | 80 | review: merge |
| `profecional` | `profesional` | 80 | review: merge |
| `saciaos` | `saciarse` | 80 | review: merge |
| `superelásticas` | `superelástico` | 80 | review: merge |
| `terapeútico` | `terapéutico` | 80 | review: merge |
| `brandie` | `brandy` | 79 | review: merge |
| `cochinita` | `cochinita pibil` | 79 | review: merge |
| `collages` | `collage` | 79 | review: merge |
| `enfurruñar` | `enfurruñarse` | 79 | review: merge |
| `especiada` | `especiado` | 79 | review: merge |
| `indivíduo` | `individuo` | 79 | review: merge |
| `izda` | `izquierdo` | 79 | review: merge |
| `lazuli` | `lapislázuli` | 79 | review: merge |
| `llamémosle` | `llamar` | 79 | review: merge |
| `naive` | `naíf` | 79 | review: merge |
| `repartidlo` | `repartir` | 79 | review: merge |
| `revísalo` | `revisar` | 79 | review: merge |
| `substantivar` | `sustantivo` | 79 | review: merge |
| `taaaan` | `tan` | 79 | review: merge |
| `telekinesis` | `telequinesis` | 79 | review: merge |
| `verdurita` | `verdura` | 79 | review: merge |
| `véa` | `ver` | 79 | review: merge |
| `woks` | `wok` | 79 | review: merge |
| `comedla` | `comer` | 78 | review: merge |
| `enseñándoos` | `enseñar` | 78 | review: merge |
| `especio` | `espacio` | 78 | review: merge |
| `fluconazole` | `fluconazol` | 78 | review: merge |
| `gestionarla` | `gestionar` | 78 | review: merge |
| `hombros` | `hombro` | 78 | review: merge |
| `martiana` | `martiano` | 78 | review: merge |
| `mútuo` | `mutuo` | 78 | review: merge |
| `urgiéndola` | `urgir` | 78 | review: merge |
| `antropógenas` | `antropógeno` | 77 | review: merge |
| `correspondente` | `correspondiente` | 77 | review: merge |
| `cubreboca` | `cubrebocas` | 77 | review: merge |
| `dejándote` | `dejar` | 77 | review: merge |
| `eduación` | `educación` | 77 | review: merge |
| `examinarla` | `examinar` | 77 | review: merge |
| `metrológicas` | `metrológico` | 77 | review: merge |
| `amaras` | `amar` | 80 | review: merge |
| `cephalexin` | `cefalexina` | 80 | review: merge |
| `estandard` | `estándar` | 80 | review: merge |
| `mega-proyecto` | `megaproyecto` | 80 | review: merge |
| `passepartout` | `paspartú` | 80 | review: merge |
| `pre-establecidos` | `preestablecido` | 80 | review: merge |
| `prohibiciones` | `prohibición` | 80 | review: merge |
| `reabsorbibl` | `reabsorbible` | 80 | review: merge |
| `relaja` | `relajar` | 80 | review: merge |
| `sufis` | `sufí` | 80 | review: merge |
| `buscapersona` | `buscapersonas` | 79 | review: merge |
| `derivabrisa` | `derivabrisas` | 79 | review: merge |
| `garrapatas` | `garrapata` | 79 | review: merge |
| `importarl` | `importar` | 79 | review: merge |
| `sonreí` | `sonreír` | 79 | review: merge |
| `compagina` | `compaginar` | 78 | review: merge |
| `dotándol` | `dotar` | 78 | review: merge |
| `hablól` | `hablar` | 78 | review: merge |
| `enfrentarno` | `enfrentarse` | 77 | review: merge |
| `ibidem` | `ibídem` | 77 | review: merge |
| `piperine` | `piperina` | 77 | review: merge |
| `pre-temporada` | `pretemporada` | 77 | review: merge |
| `véase` | `ver` | 77 | review: merge |
| `comfortabl` | `confortable` | 76 | review: merge |
| `mostrad` | `mostrar` | 76 | review: merge |
| `pre-electoral` | `preelectoral` | 76 | review: merge |
| `agro-industrial` | `agroindustrial` | 75 | review: merge |
| `co-creando` | `cocrear` | 75 | review: merge |
| `expandirno` | `expandirse` | 75 | review: merge |
| `fijaos` | `fijarse` | 75 | review: merge |
| `invitándol` | `invitar` | 75 | review: merge |
| `profetiza` | `profetizar` | 75 | review: merge |
| `subliminales` | `subliminal` | 75 | review: merge |
| `anti-mancha` | `antimanchas` | 74 | review: merge |
| `colchicine` | `colchicina` | 74 | review: merge |
| `educativa` | `educativo` | 74 | review: merge |
| `neo-liberal` | `neoliberal` | 74 | review: merge |
| `parasitoid` | `parasitoide` | 74 | review: merge |
| `auto-registro` | `autorregistro` | 73 | review: merge |
| `logins` | `login` | 84 | review: merge |
| `paninis` | `panini` | 84 | review: merge |
| `usuário` | `usuario` | 84 | review: merge |
| `asegúrela` | `asegurar` | 83 | review: merge |
| `directar` | `directo` | 83 | review: merge |
| `fortalecerlas` | `fortalecer` | 83 | review: merge |
| `losartan` | `losartán` | 83 | review: merge |
| `previéndose` | `prever` | 83 | review: merge |
| `pupusas` | `pupusa` | 83 | review: merge |
| `remasterizadas` | `remasterizado` | 83 | review: merge |
| `resetea` | `resetear` | 83 | review: merge |
| `antirracistas` | `antirracista` | 82 | review: merge |
| `arrepintiéndose` | `arrepentirse` | 82 | review: merge |
| `bioactiva` | `bioactivo` | 82 | review: merge |
| `colleción` | `colección` | 82 | review: merge |
| `despu` | `después` | 82 | review: merge |
| `levántela` | `levantar` | 82 | review: merge |
| `proprietad` | `propiedad` | 82 | review: merge |
| `rasterizada` | `rasterizar` | 82 | review: merge |
| `reconciliaos` | `reconciliarse` | 82 | review: merge |
| `capot` | `capó` | 81 | review: merge |
| `combis` | `combi` | 81 | review: merge |
| `empoderen` | `empoderar` | 81 | review: merge |
| `estaras` | `estar` | 81 | review: merge |
| `grancanaria` | `grancanario` | 81 | review: merge |
| `incial` | `inicial` | 81 | review: merge |
| `metacognitivas` | `metacognitivo` | 81 | review: merge |
| `perfiladoras` | `perfiladora` | 81 | review: merge |
| `aféitate` | `afeitarse` | 80 | review: merge |
| `dejano` | `dejar` | 80 | review: merge |
| `desmopressin` | `desmopresina` | 80 | review: merge |
| `mezclarlo` | `mezclar` | 80 | review: merge |
| `sombrerito` | `sombrero` | 80 | review: merge |
| `academía` | `academia` | 79 | review: merge |
| `bolsillito` | `bolsillo` | 79 | review: merge |
| `chequen` | `chequear` | 79 | review: merge |
| `cocínela` | `cocinar` | 79 | review: merge |
| `coreografiada` | `coreografiar` | 79 | review: merge |
| `desplazándolo` | `desplazar` | 79 | review: merge |
| `ejércitos` | `ejército` | 79 | review: merge |
| `enlentece` | `enlentecer` | 79 | review: merge |
| `nuestas` | `nuestro` | 79 | review: merge |
| `proteción` | `protección` | 79 | review: merge |
| `putita` | `puta` | 79 | review: merge |
| `resíduo` | `residuo` | 79 | review: merge |
| `rindiéndose` | `rendirse` | 79 | review: merge |
| `saborizados` | `saborizar` | 79 | review: merge |
| `sensora` | `sensor` | 79 | review: merge |
| `tirolinas` | `tirolina` | 79 | review: merge |
| `algúna` | `alguno` | 78 | review: merge |
| `antimeningocócica` | `antimeningocócico` | 78 | review: merge |
| `aréola` | `areola` | 78 | review: merge |
| `atropine` | `atropina` | 78 | review: merge |
| `decimosegunda` | `decimosegundo` | 78 | review: merge |
| `desmotivados` | `desmotivado` | 78 | review: merge |
| `enseñándote` | `enseñar` | 78 | review: merge |
| `específi` | `específico` | 78 | review: merge |
| `instruciones` | `instrucción` | 78 | review: merge |
| `ojillo` | `ojo` | 78 | review: merge |
| `revisá` | `revisar` | 78 | review: merge |
| `selyúcidas` | `selyúcida` | 78 | review: merge |
| `supóngase` | `suponer` | 78 | review: merge |
| `termoselladas` | `termosellado` | 78 | review: merge |
| `totems` | `tótem` | 78 | review: merge |
| `amplísimos` | `amplio` | 77 | review: merge |
| `aplástica` | `aplástico` | 77 | review: merge |
| `arquitectonica` | `arquitectónico` | 77 | review: merge |
| `botoncito` | `botón` | 77 | review: merge |
| `currys` | `curry` | 77 | review: merge |
| `desarrolo` | `desarrollo` | 77 | review: merge |
| `gastronomica` | `gastronómico` | 77 | review: merge |
| `happenings` | `happening` | 77 | review: merge |
| `mantenerlo` | `mantener` | 77 | review: merge |
| `poney` | `poni` | 77 | review: merge |
| `efemérid` | `efeméride` | 80 | review: merge |
| `engaña` | `engañar` | 80 | review: merge |
| `flip-flops` | `flip-flop` | 80 | review: merge |
| `mézclate` | `mezclarse` | 80 | review: merge |
| `palmas` | `palma` | 80 | review: merge |
| `reembolsos` | `reembolso` | 80 | review: merge |
| `respondiéndol` | `responder` | 79 | review: merge |
| `whigs` | `whig` | 79 | review: merge |
| `compr` | `comprar` | 78 | review: merge |
| `levantémono` | `levantarse` | 78 | review: merge |
| `boletas` | `boleta` | 77 | review: merge |
| `dirigiro` | `dirigirse` | 77 | review: merge |
| `leoncito` | `león` | 77 | review: merge |
| `teclist` | `teclista` | 77 | review: merge |
| `multi-media` | `multimedia` | 76 | review: merge |
| `ongs` | `ong` | 76 | review: merge |
| `post-its` | `post-it` | 76 | review: merge |
| `pre-exposición` | `preexposición` | 76 | review: merge |
| `sorprendiéndono` | `sorprender` | 76 | review: merge |
| `confesarl` | `confesar` | 75 | review: merge |
| `limpiémono` | `limpiarse` | 75 | review: merge |
| `mini-serie` | `miniserie` | 75 | review: merge |
| `pre-kínder` | `prekínder` | 75 | review: merge |
| `semi-auto` | `semiautomático` | 75 | review: merge |
| `dedicarno` | `dedicarse` | 74 | review: merge |
| `freesia` | `fresia` | 74 | review: merge |
| `l-dopa` | `levodopa` | 74 | review: merge |
| `olvidándono` | `olvidarse` | 74 | review: merge |
| `partenariados` | `partenariado` | 74 | review: merge |
| `recomendarl` | `recomendar` | 74 | review: merge |
| `bahai` | `bahaí` | 73 | review: merge |
| `cumpleano` | `cumpleaños` | 84 | review: merge |
| `dentellar` | `dentellada` | 84 | review: merge |
| `enseñándome` | `enseñar` | 84 | review: merge |
| `gentamicin` | `gentamicina` | 84 | review: merge |
| `sencillito` | `sencillo` | 84 | review: merge |
| `suéltela` | `soltar` | 84 | review: merge |
| `tizo` | `tiza` | 84 | review: merge |
| `acojedora` | `acogedor` | 83 | review: merge |
| `extruye` | `extruir` | 83 | review: merge |
| `máquinaria` | `maquinaria` | 83 | review: merge |
| `propolis` | `própolis` | 83 | review: merge |
| `remitiéndose` | `remitirse` | 83 | review: merge |
| `snowboarders` | `snowboarder` | 83 | review: merge |
| `alheñar` | `alheña` | 82 | review: merge |
| `anótelo` | `anotar` | 82 | review: merge |
| `disfrutarla` | `disfrutar` | 82 | review: merge |
| `docusate` | `docusato` | 82 | review: merge |
| `hipóxica` | `hipóxico` | 82 | review: merge |
| `importantísimas` | `importante` | 82 | review: merge |
| `inovadora` | `innovador` | 82 | review: merge |
| `presición` | `precisión` | 82 | review: merge |
| `pránica` | `pránico` | 82 | review: merge |
| `sanarlo` | `sanar` | 82 | review: merge |
| `vedio` | `vídeo` | 82 | review: merge |
| `adríatica` | `adriático` | 81 | review: merge |
| `conocidísima` | `conocido` | 81 | review: merge |
| `cópielo` | `copiar` | 81 | review: merge |
| `estralla` | `estrella` | 81 | review: merge |
| `exámen` | `examen` | 81 | review: merge |
| `hidrofílicas` | `hidrofílico` | 81 | review: merge |
| `indomethacin` | `indometacina` | 81 | review: merge |
| `intraoperatorias` | `intraoperatorio` | 81 | review: merge |
| `multivitamin` | `multivitamínico` | 81 | review: merge |
| `sométase` | `someterse` | 81 | review: merge |
| `topiramate` | `topiramato` | 81 | review: merge |
| `tremolar` | `trémolo` | 81 | review: merge |
| `ultrabajas` | `ultrabajo` | 81 | review: merge |
| `ajustándola` | `ajustar` | 80 | review: merge |
| `cerrándola` | `cerrar` | 80 | review: merge |
| `escúchala` | `escuchar` | 80 | review: merge |
| `estresa` | `estresar` | 80 | review: merge |
| `externaliza` | `externalizar` | 80 | review: merge |
| `guiándolo` | `guiar` | 80 | review: merge |
| `llamémoslo` | `llamar` | 80 | review: merge |
| `mobilización` | `movilización` | 80 | review: merge |
| `prellenada` | `prellenado` | 80 | review: merge |
| `rellénalo` | `rellenar` | 80 | review: merge |
| `sométete` | `someterse` | 80 | review: merge |
| `stricto` | `stricto sensu` | 80 | review: merge |
| `tírala` | `tirar` | 80 | review: merge |
| `angu` | `ángulo` | 79 | review: merge |
| `deténganse` | `detenerse` | 79 | review: merge |
| `frustado` | `frustrado` | 79 | review: merge |
| `inciativa` | `iniciativa` | 79 | review: merge |
| `lansoprazole` | `lansoprazol` | 79 | review: merge |
| `millones` | `millón` | 79 | review: merge |
| `pescaito` | `pescado` | 79 | review: merge |
| `remezclado` | `remezclar` | 79 | review: merge |
| `retwittear` | `retuitear` | 79 | review: merge |
| `sitúese` | `situarse` | 79 | review: merge |
| `visibilizando` | `visibilizar` | 79 | review: merge |
| `ashaninka` | `asháninka` | 78 | review: merge |
| `briefings` | `briefing` | 78 | review: merge |
| `dejadlos` | `dejar` | 78 | review: merge |
| `grampones` | `crampón` | 78 | review: merge |
| `paséate` | `pasearse` | 78 | review: merge |
| `revísala` | `revisar` | 78 | review: merge |
| `sonrie` | `sonreír` | 78 | review: merge |
| `transfiéralo` | `transferir` | 78 | review: merge |
| `ungiéndole` | `ungir` | 78 | review: merge |
| `victimizado` | `victimizar` | 78 | review: merge |
| `virtualiza` | `virtualizar` | 78 | review: merge |
| `atraidos` | `atraer` | 77 | review: merge |
| `cañoner` | `cañonera` | 77 | review: merge |
| `compasivísimo` | `compasivo` | 77 | review: merge |
| `cubertura` | `cobertura` | 77 | review: merge |
| `flipa` | `flipar` | 77 | review: merge |
| `guardavida` | `guardavidas` | 77 | review: merge |
| `intestar` | `intestado` | 77 | review: merge |
| `multipremiada` | `multipremiado` | 77 | review: merge |
| `nutriéndose` | `nutrirse` | 77 | review: merge |
| `pistónes` | `pistón` | 77 | review: merge |
| `preclínicas` | `preclínico` | 77 | review: merge |
| `primula` | `prímula` | 77 | review: merge |
| `gatito` | `gato` | 5,552 | review: merge |
| `casita` | `casa` | 5,307 | review: merge |
| `bolita` | `bola` | 3,052 | review: merge |
| `pequeñito` | `pequeño` | 1,597 | review: merge |
| `conejito` | `conejo` | 2,254 | review: merge |
| `pedacito` | `pedazo` | 2,253 | review: merge |
| `trocito` | `trozo` | 1,988 | review: merge |
| `pueblecito` | `pueblo` | 1,970 | review: merge |
| `hijito` | `hijo` | 1,948 | review: merge |
| `jovencito` | `joven` | 1,945 | review: merge |
| `palito` | `palo` | 1,764 | review: merge |
| `fresquito` | `fresco` | 1,131 | review: merge |
| `cosita` | `cosa` | 1,481 | review: merge |
| `golpecito` | `golpe` | 1,133 | review: merge |
| `ramita` | `rama` | 843 | review: merge |
| `chorrito` | `chorro` | 934 | review: merge |
| `cajita` | `caja` | 917 | review: merge |
| `manita` | `mano` | 888 | review: merge |
| `pueblito` | `pueblo` | 876 | review: merge |
| `braguita` | `braga` | 859 | review: merge |
| `pastelito` | `pastel` | 833 | review: merge |
| `bajito` | `bajo` | 717 | review: merge |
| `regalito` | `regalo` | 702 | review: merge |
| `angelito` | `ángel` | 664 | review: merge |
| `palmadita` | `palmada` | 612 | review: merge |
| `puntito` | `punto` | 602 | review: merge |
| `besito` | `beso` | 461 | review: merge |
| `arbolito` | `árbol` | 562 | review: merge |
| `galletita` | `galleta` | 559 | review: merge |
| `plaquita` | `placa` | 553 | review: merge |
| `bocadito` | `bocado` | 547 | review: merge |
| `amiguito` | `amigo` | 537 | review: merge |
| `perlita` | `perla` | 519 | review: merge |
| `añito` | `año` | 499 | review: merge |
| `pasito` | `paso` | 479 | review: merge |
| `saquito` | `saco` | 467 | review: merge |
| `cosilla` | `cosa` | 458 | review: merge |
| `gordito` | `gordo` | 357 | review: merge |
| `vasito` | `vaso` | 448 | review: merge |
| `pajarillo` | `pájaro` | 446 | review: merge |
| `rinconcito` | `rincón` | 440 | review: merge |
| `hermanita` | `hermano` | 439 | review: merge |
| `pollito` | `pollo` | 435 | review: merge |
| `hombrecito` | `hombre` | 384 | review: merge |
| `toquecito` | `toque` | 361 | review: merge |
| `gorrito` | `gorro` | 360 | review: merge |
| `cachorrito` | `cachorro` | 348 | review: merge |
| `barquito` | `barco` | 347 | review: merge |
| `culito` | `culo` | 347 | review: merge |
| `cabecita` | `cabeza` | 329 | review: merge |
| `vestidito` | `vestido` | 329 | review: merge |
| `hotelito` | `hotel` | 318 | review: merge |
| `agujerito` | `agujero` | 301 | review: merge |
| `papelito` | `papel` | 301 | review: merge |
| `clarito` | `claro` | 289 | review: merge |
| `cuadradito` | `cuadrado` | 287 | review: merge |
| `leoncillo` | `león` | 286 | review: merge |
| `cafecito` | `café` | 284 | review: merge |
| `modelito` | `modelo` | 283 | review: merge |
| `animalito` | `animal` | 282 | review: merge |
| `fotito` | `foto` | 281 | review: merge |
| `bodeguita` | `bodega` | 279 | review: merge |
| `callecita` | `calle` | 279 | review: merge |
| `putilla` | `puta` | 273 | review: merge |
| `muchachito` | `muchacho` | 271 | review: merge |
| `grupito` | `grupo` | 267 | review: merge |
| `bosquecillo` | `bosque` | 264 | review: merge |
| `calorcito` | `calor` | 259 | review: merge |
| `pececillo` | `pez` | 257 | review: merge |
| `empujoncito` | `empujón` | 253 | review: merge |
| `piedrita` | `piedra` | 251 | review: merge |
| `pastelillo` | `pastel` | 250 | review: merge |
| `cadenilla` | `cadena` | 249 | review: merge |
| `ruedecilla` | `rueda` | 249 | review: merge |
| `hojita` | `hoja` | 246 | review: merge |
| `botellita` | `botella` | 245 | review: merge |
| `cortito` | `corto` | 241 | review: merge |
| `islita` | `isla` | 233 | review: merge |
| `botita` | `bota` | 99 | review: merge |
| `perrillo` | `perro` | 225 | review: merge |
| `colita` | `cola` | 219 | review: merge |
| `diablillo` | `diablo` | 219 | review: merge |
| `taquito` | `taco` | 215 | review: merge |
| `hermanito` | `hermano` | 212 | review: merge |
| `conejita` | `conejo` | 211 | review: merge |
| `corazoncito` | `corazón` | 209 | review: merge |
| `tubito` | `tubo` | 206 | review: merge |
| `cañita` | `caña` | 205 | review: merge |
| `personita` | `persona` | 205 | review: merge |
| `viejito` | `viejo` | 199 | review: merge |
| `barriguita` | `barriga` | 196 | review: merge |
| `detallito` | `detalle` | 190 | review: merge |
| `zapatito` | `zapato` | 187 | review: merge |
| `calientito` | `caliente` | 181 | review: merge |
| `velita` | `vela` | 181 | review: merge |
| `muñequita` | `muñeca` | 177 | review: merge |
| `cervecita` | `cerveza` | 171 | review: merge |
| `ruedita` | `rueda` | 171 | review: merge |
| `banderita` | `bandera` | 166 | review: merge |
| `polvillo` | `polvo` | 166 | review: merge |
| `librito` | `libro` | 160 | review: merge |
| `dedito` | `dedo` | 159 | review: merge |
| `boquita` | `boca` | 157 | review: merge |
| `trenecito` | `tren` | 156 | review: merge |
| `duendecillo` | `duende` | 154 | review: merge |
| `maquinita` | `máquina` | 152 | review: merge |
| `pececito` | `pez` | 149 | review: merge |
| `princesita` | `princesa` | 149 | review: merge |
| `probadita` | `probada` | 148 | review: merge |
| `florecilla` | `flor` | 146 | review: merge |
| `cerrillo` | `cerro` | 145 | review: merge |
| `blandito` | `blando` | 143 | review: merge |
| `rayito` | `rayo` | 141 | review: merge |
| `ranita` | `rana` | 140 | review: merge |
| `pescadito` | `pescado` | 136 | review: merge |
| `mejorcito` | `mejor` | 134 | review: merge |
| `mujercita` | `mujer` | 133 | review: merge |
| `tiendecita` | `tienda` | 133 | review: merge |
| `cachito` | `cacho` | 132 | review: merge |
| `juguetito` | `juguete` | 130 | review: merge |
| `cestillo` | `cesto` | 129 | review: merge |
| `plantita` | `planta` | 129 | review: merge |
| `abuelito` | `abuelo` | 128 | review: merge |
| `lamparita` | `lámpara` | 126 | review: merge |
| `solecito` | `sol` | 125 | review: merge |
| `tiendita` | `tienda` | 125 | review: merge |
| `muñequito` | `muñeco` | 124 | review: merge |
| `ricito` | `rizo` | 120 | review: merge |
| `saltito` | `salto` | 120 | review: merge |
| `joyita` | `joya` | 119 | review: merge |
| `tortuguita` | `tortuga` | 118 | review: merge |
| `platito` | `plato` | 116 | review: merge |
| `cuerpecito` | `cuerpo` | 115 | review: merge |
| `vocecita` | `voz` | 115 | review: merge |
| `escapadita` | `escapada` | 114 | review: merge |
| `frasquito` | `frasco` | 112 | review: merge |
| `niñita` | `niño` | 112 | review: merge |
| `botecito` | `bote` | 109 | review: merge |
| `saloncito` | `salón` | 109 | review: merge |
| `huevito` | `huevo` | 108 | review: merge |
| `tiempito` | `tiempo` | 107 | review: merge |
| `zorrita` | `zorra` | 106 | review: merge |
| `gusanito` | `gusano` | 105 | review: merge |
| `orejita` | `oreja` | 104 | review: merge |
| `ovejita` | `oveja` | 104 | review: merge |
| `huevecillo` | `huevo` | 102 | review: merge |
| `banquito` | `banco` | 101 | review: merge |
| `normalito` | `normal` | 100 | review: merge |
| `bichito` | `bicho` | 98 | review: merge |
| `manchita` | `mancha` | 96 | review: merge |
| `montoncito` | `montón` | 96 | review: merge |
| `manito` | `mano` | 93 | review: merge |
| `piedrecilla` | `piedra` | 93 | review: merge |
| `barquita` | `barca` | 92 | review: merge |
| `amorcito` | `amor` | 91 | review: merge |
| `cochecillo` | `coche` | 90 | review: merge |
| `cadenita` | `cadena` | 89 | review: merge |
| `raicilla` | `raíz` | 89 | review: merge |
| `cartelito` | `cartel` | 88 | review: merge |
| `esponjita` | `esponja` | 88 | review: merge |
| `madrecita` | `madre` | 88 | review: merge |
| `bolilla` | `bola` | 87 | review: merge |
| `diablito` | `diablo` | 84 | review: merge |
| `monedita` | `moneda` | 84 | review: merge |
| `planchita` | `plancha` | 78 | review: merge |
| `bizcochito` | `bizcocho` | 77 | review: merge |
| `lugarcito` | `lugar` | 77 | review: merge |
| `chochito` | `chocho` | 75 | review: merge |
| `pelotita` | `pelota` | 75 | review: merge |
| `arito` | `aro` | 74 | review: merge |
| `hombrecillo` | `hombre` | 74 | review: merge |
| `abrigadito` | `abrigado` | 73 | review: merge |
| `carbonio` | `carbono` | 73 | review: merge |
| `co-creativa` | `cocreativo` | 73 | review: merge |
| `llenándono` | `llenar` | 73 | review: merge |
| `utilízalos` | `utilizar` | 73 | review: merge |
| `electro-hidráulico` | `electrohidráulico` | 72 | review: merge |
| `entregaro` | `entregarse` | 72 | review: merge |
| `greco-católico` | `grecocatólico` | 72 | review: merge |
| `maravillarno` | `maravillarse` | 72 | review: merge |
| `saldré` | `salir` | 72 | review: merge |
| `bi-xenón` | `bixenón` | 71 | review: merge |
| `fitocannabinoid` | `fitocannabinoide` | 71 | review: merge |
| `pre-embarque` | `preembarque` | 71 | review: merge |
| `transgender` | `transgénero` | 71 | review: merge |
| `clutche` | `clutch` | 70 | review: merge |
| `couscous` | `cuscús` | 70 | review: merge |
| `ingenería` | `ingeniería` | 70 | review: merge |
| `serl` | `ser` | 70 | review: merge |
| `suministrándol` | `suministrar` | 70 | review: merge |
| `doble-clic` | `doble clic` | 69 | review: merge |
| `ex-marido` | `exmarido` | 69 | review: merge |
| `multicin#Fem` | `multicine` | 69 | review: merge |
| `sabrán` | `saber` | 69 | review: merge |
| `valenciana` | `valenciano` | 69 | review: merge |
| `vendr` | `venir` | 69 | review: merge |
| `reimaginado` | `reimaginar` | 77 | review: merge |
| `vacaciónes` | `vacaciones` | 77 | review: merge |
| `blisters` | `blíster` | 76 | review: merge |
| `comedlo` | `comer` | 76 | review: merge |
| `decembrina` | `decembrino` | 76 | review: merge |
| `develada` | `develar` | 76 | review: merge |
| `déme` | `dar` | 76 | review: merge |
| `envienos` | `enviar` | 76 | review: merge |
| `ministraban` | `ministrar` | 76 | review: merge |
| `nucléico` | `nucleico` | 76 | review: merge |
| `oisteis` | `oír` | 76 | review: merge |
| `panderia` | `panadería` | 76 | review: merge |
| `rehuso` | `rehusar` | 76 | review: merge |
| `treking` | `trekking` | 76 | review: merge |
| `twitear` | `tuitear` | 76 | review: merge |
| `belarusa` | `bielorruso` | 75 | review: merge |
| `cansadísimo` | `cansado` | 75 | review: merge |
| `cliparts` | `clipart` | 75 | review: merge |
| `depue` | `después` | 75 | review: merge |
| `distribuyéndose` | `distribuirse` | 75 | review: merge |
| `ejercitándote` | `ejercitarse` | 75 | review: merge |
| `enrrollable` | `enrollable` | 75 | review: merge |
| `famotidine` | `famotidina` | 75 | review: merge |
| `inconcientemente` | `inconscientemente` | 75 | review: merge |
| `mísil` | `misil` | 75 | review: merge |
| `perdicera` | `perdicero` | 75 | review: merge |
| `polícia` | `policía` | 75 | review: merge |
| `reunio` | `reunir` | 75 | review: merge |
| `texturados` | `texturado` | 75 | review: merge |
| `tratá` | `tratar` | 75 | review: merge |
| `aymaras` | `aymara` | 74 | review: merge |
| `beig` | `beige` | 74 | review: merge |
| `cirujía` | `cirugía` | 74 | review: merge |
| `cristaleria` | `cristalería` | 74 | review: merge |
| `desconéctese` | `desconectarse` | 74 | review: merge |
| `diólo` | `dar` | 74 | review: merge |
| `déjela` | `dejar` | 74 | review: merge |
| `frotándola` | `frotar` | 74 | review: merge |
| `incentivarlo` | `incentivar` | 74 | review: merge |
| `postquirúrgica` | `postquirúrgico` | 74 | review: merge |
| `rellénala` | `rellenar` | 74 | review: merge |
| `sampleado` | `samplear` | 74 | review: merge |
| `acompañándote` | `acompañar` | 73 | review: merge |
| `agrandarla` | `agrandar` | 73 | review: merge |
| `alquilarla` | `alquilar` | 73 | review: merge |
| `cestita` | `cesta` | 73 | review: merge |
| `cremita` | `crema` | 73 | review: merge |
| `ejercítese` | `ejercitarse` | 73 | review: merge |
| `enseñároslo` | `enseñar` | 73 | review: merge |
| `háznoslo` | `hacer` | 73 | review: merge |
| `impérial` | `imperial` | 73 | review: merge |
| `mantenimento` | `mantenimiento` | 73 | review: merge |
| `multiplícate` | `multiplicarse` | 73 | review: merge |
| `pareciéndose` | `parecerse` | 73 | review: merge |
| `ponie` | `poni` | 73 | review: merge |
| `recircula` | `recircular` | 73 | review: merge |
| `reevaluando` | `reevaluar` | 73 | review: merge |
| `antibacterias` | `antibacteriano` | 72 | review: merge |
| `avaluo` | `avalúo` | 72 | review: merge |
| `cholecalciferol` | `colecalciferol` | 72 | review: merge |
| `convéncete` | `convencerse` | 72 | review: merge |
| `creps` | `crepe` | 72 | review: merge |
| `holgóse` | `holgarse` | 72 | review: merge |
| `llámenlo` | `llamar` | 72 | review: merge |
| `ocúpese` | `ocuparse` | 72 | review: merge |
| `querrá` | `querer` | 72 | review: merge |
| `selecciónalo` | `seleccionar` | 72 | review: merge |
| `echándol` | `echar` | 73 | review: merge |
| `establecerno` | `establecerse` | 73 | review: merge |
| `graba` | `grabar` | 73 | review: merge |
| `hijahija` | `hija` | 73 | review: merge |
| `post-tensión` | `postensión` | 73 | review: merge |
| `tapatía` | `tapatío` | 73 | review: merge |
| `usabl` | `usable` | 73 | review: merge |
| `comprimidos` | `comprimido` | 72 | review: merge |
| `detritu` | `detritus` | 72 | review: merge |
| `engaños` | `engaño` | 72 | review: merge |
| `limitará` | `limitar` | 72 | review: merge |
| `post-ciclo` | `posciclo` | 72 | review: merge |
| `pre-impresión` | `preimpresión` | 72 | review: merge |
| `rpms` | `rpm` | 72 | review: merge |
| `anti-terrorista` | `antiterrorista` | 71 | review: merge |
| `audiobooks` | `audiolibro` | 71 | review: merge |
| `decidno` | `decir` | 71 | review: merge |
| `dormid` | `dormir` | 71 | review: merge |
| `exhortándol` | `exhortar` | 71 | review: merge |
| `misericordiosísimo` | `misericordioso` | 71 | review: merge |
| `pre-factibilidad` | `prefactibilidad` | 71 | review: merge |
| `separarno` | `separarse` | 71 | review: merge |
| `transmitiro` | `transmitir` | 71 | review: merge |
| `auto-desarrollo` | `autodesarrollo` | 70 | review: merge |
| `fijarno` | `fijarse` | 70 | review: merge |
| `l-isoleucina` | `isoleucina` | 70 | review: merge |
| `ofrézcal` | `ofrecer` | 70 | review: merge |
| `permítel` | `permitir` | 70 | review: merge |
| `pompom` | `pompón` | 70 | review: merge |
| `visité` | `visitar` | 70 | review: merge |
| `amorita` | `amorreo` | 69 | review: merge |
| `co-investigador` | `coinvestigador` | 69 | review: merge |
| `post-colonial` | `poscolonial` | 69 | review: merge |
| `prometiéndol` | `prometer` | 69 | review: merge |
| `rosetas` | `roseta` | 69 | review: merge |
| `súper-héroe` | `superhéroe` | 69 | review: merge |
| `amaderados` | `amaderado` | 76 | review: merge |
| `ampollosa` | `ampolloso` | 76 | review: merge |
| `audicionó` | `audicionar` | 76 | review: merge |
| `comfortablemente` | `confortablemente` | 76 | review: merge |
| `ecosistémica` | `ecosistémico` | 76 | review: merge |
| `empápese` | `empaparse` | 76 | review: merge |
| `extractivistas` | `extractivista` | 76 | review: merge |
| `inciar` | `iniciar` | 76 | review: merge |
| `nooo` | `no` | 76 | review: merge |
| `proinflamatoria` | `proinflamatorio` | 76 | review: merge |
| `sugiérale` | `sugerir` | 76 | review: merge |
| `trimethoprim` | `trimetoprima` | 76 | review: merge |
| `abrahámicas` | `abrahámico` | 75 | review: merge |
| `actualemente` | `actualmente` | 75 | review: merge |
| `algunxs` | `alguno` | 75 | review: merge |
| `biga` | `viga` | 75 | review: merge |
| `chupacabra` | `chupacabras` | 75 | review: merge |
| `cogido` | `coger` | 75 | review: merge |
| `contenter` | `contener` | 75 | review: merge |
| `desestimiento` | `desistimiento` | 75 | review: merge |
| `domitorio` | `dormitorio` | 75 | review: merge |
| `evitarlo` | `evitar` | 75 | review: merge |
| `interdisciplinaridad` | `interdisciplinariedad` | 75 | review: merge |
| `quitarla` | `quitar` | 75 | review: merge |
| `ufff` | `uf` | 75 | review: merge |
| `adámica` | `adámico` | 74 | review: merge |
| `facsímile` | `facsímil` | 74 | review: merge |
| `huerfano` | `huérfano` | 74 | review: merge |
| `inmediatemente` | `inmediatamente` | 74 | review: merge |
| `metalurgía` | `metalurgia` | 74 | review: merge |
| `actualizarlo` | `actualizar` | 73 | review: merge |
| `agustiniana` | `agustiniano` | 73 | review: merge |
| `alábenlo` | `alabar` | 73 | review: merge |
| `arquivolta` | `archivolta` | 73 | review: merge |
| `contralaminada` | `contralaminado` | 73 | review: merge |
| `disponiblidad` | `disponibilidad` | 73 | review: merge |
| `encoje` | `encoger` | 73 | review: merge |
| `evacue` | `evacuar` | 73 | review: merge |
| `extensísima` | `extenso` | 73 | review: merge |
| `metilado` | `metilar` | 73 | review: merge |
| `nustro` | `nuestro` | 73 | review: merge |
| `precompilado` | `precompilar` | 73 | review: merge |
| `recomer` | `recomendar` | 73 | review: merge |
| `registrándote` | `registrarse` | 73 | review: merge |
| `selecc` | `selección` | 73 | review: merge |
| `voltéalo` | `voltear` | 73 | review: merge |
| `antifosfolípidos` | `antifosfolípido` | 72 | review: merge |
| `asegúrele` | `asegurar` | 72 | review: merge |
| `butiescopolamina` | `butilescopolamina` | 72 | review: merge |
| `consequencia` | `consecuencia` | 72 | review: merge |
| `decórala` | `decorar` | 72 | review: merge |
| `guíese` | `guiarse` | 72 | review: merge |
| `premezclada` | `premezclado` | 72 | review: merge |
| `proviniente` | `proveniente` | 72 | review: merge |
| `pusiéronse` | `ponerse` | 72 | review: merge |
| `remuévelo` | `remover` | 72 | review: merge |
| `situándola` | `situar` | 72 | review: merge |
| `dermabrasion` | `dermabrasión` | 73 | review: merge |
| `esterilizabl` | `esterilizable` | 73 | review: merge |
| `semi-adosado` | `semiadosado` | 73 | review: merge |
| `trabajad` | `trabajar` | 73 | review: merge |
| `evaluaciones` | `evaluación` | 72 | review: merge |
| `situándono` | `situarse` | 72 | review: merge |
| `surah` | `sura` | 72 | review: merge |
| `francésd` | `francés` | 71 | review: merge |
| `liliums` | `lilium` | 71 | review: merge |
| `pre-programados` | `preprogramar` | 71 | review: merge |
| `sobre-descarga` | `sobredescarga` | 71 | review: merge |
| `terminados` | `terminado` | 71 | review: merge |
| `ex-militar` | `exmilitar` | 70 | review: merge |
| `indexabl` | `indexable` | 70 | review: merge |
| `neo-nazis` | `neonazi` | 70 | review: merge |
| `sub-licencia` | `sublicencia` | 70 | review: merge |
| `acompañándol` | `acompañar` | 69 | review: merge |
| `auto-sanación` | `autosanación` | 69 | review: merge |
| `electro-óptico` | `electroóptico` | 69 | review: merge |
| `liposuction` | `liposucción` | 69 | review: merge |
| `pre-grabadas` | `pregrabado` | 69 | review: merge |
| `re-establecer` | `restablecer` | 69 | review: merge |
| `reflectantes` | `reflectante` | 69 | review: merge |
| `recupérate` | `recuperarse` | 77 | review: merge |
| `reintroducida` | `reintroducir` | 77 | review: merge |
| `salmonera` | `salmonero` | 77 | review: merge |
| `submilimétrica` | `submilimétrico` | 77 | review: merge |
| `comparándola` | `comparar` | 76 | review: merge |
| `cúando` | `cuándo` | 76 | review: merge |
| `dirígete` | `dirigirse` | 76 | review: merge |
| `levantándolo` | `levantar` | 76 | review: merge |
| `paraque` | `para que` | 76 | review: merge |
| `ponchado` | `ponchar` | 76 | review: merge |
| `simulacion` | `simulación` | 76 | review: merge |
| `socioeducativas` | `socioeducativo` | 76 | review: merge |
| `sumergirme` | `sumergirse` | 76 | review: merge |
| `volvé` | `volver` | 76 | review: merge |
| `adems` | `además` | 75 | review: merge |
| `adviértase` | `advertir` | 75 | review: merge |
| `direcciónes` | `dirección` | 75 | review: merge |
| `empeze` | `empezar` | 75 | review: merge |
| `escúrrela` | `escurrir` | 75 | review: merge |
| `esteroideas` | `esteroideo` | 75 | review: merge |
| `fidelizados` | `fidelizado` | 75 | review: merge |
| `fortalecerlo` | `fortalecer` | 75 | review: merge |
| `gíralo` | `girar` | 75 | review: merge |
| `internalizada` | `internalizar` | 75 | review: merge |
| `llevártelo` | `llevarse` | 75 | review: merge |
| `modernísima` | `moderno` | 75 | review: merge |
| `reevaluado` | `reevaluar` | 75 | review: merge |
| `suéltate` | `soltarse` | 75 | review: merge |
| `vestidle` | `vestir` | 75 | review: merge |
| `alagar` | `halagar` | 74 | review: merge |
| `balancéate` | `balancearse` | 74 | review: merge |
| `evolucionarias` | `evolucionario` | 74 | review: merge |
| `fijaciónes` | `fijación` | 74 | review: merge |
| `instálalo` | `instalar` | 74 | review: merge |
| `magneta` | `magnetita` | 74 | review: merge |
| `naturópatas` | `naturópata` | 74 | review: merge |
| `pedrizo` | `pedriza` | 74 | review: merge |
| `pintacarita` | `pintacaritas` | 74 | review: merge |
| `quinolonas` | `quinolona` | 74 | review: merge |
| `semiurbana` | `semiurbano` | 74 | review: merge |
| `transesofágica` | `transesofágico` | 74 | review: merge |
| `acuaticas` | `acuático` | 73 | review: merge |
| `apeguen` | `apegarse` | 73 | review: merge |
| `externalizando` | `externalizar` | 73 | review: merge |
| `hibrido` | `híbrido` | 73 | review: merge |
| `hiperbáricas` | `hiperbárico` | 73 | review: merge |
| `imigrante` | `inmigrante` | 73 | review: merge |
| `multiétnicas` | `multiétnico` | 73 | review: merge |
| `pesadas` | `pesado` | 73 | review: merge |
| `postee` | `postear` | 73 | review: merge |
| `redímeme` | `redimir` | 73 | review: merge |
| `trasportó` | `transportar` | 73 | review: merge |
| `actualícese` | `actualizarse` | 72 | review: merge |
| `algúno` | `alguno` | 72 | review: merge |
| `dalái` | `dalái lama` | 72 | review: merge |
| `hidrátate` | `hidratarse` | 72 | review: merge |
| `manos` | `mano` | 72 | review: merge |
| `meditándola` | `meditar` | 72 | review: merge |
| `pánel` | `panel` | 72 | review: merge |
| `co-autoría` | `coautoría` | 73 | review: merge |
| `espaciadora` | `espaciador` | 73 | review: merge |
| `gigolo` | `gigoló` | 73 | review: merge |
| `faciles` | `fácil` | 72 | review: merge |
| `mastique` | `masticar` | 72 | review: merge |
| `anti-cáncer` | `anticáncer` | 71 | review: merge |
| `autosostenibl` | `autosostenible` | 71 | review: merge |
| `confortables` | `confortable` | 71 | review: merge |
| `gram-positivas` | `grampositivo` | 71 | review: merge |
| `hebreos` | `hebreo` | 71 | review: merge |
| `layouts` | `layout` | 71 | review: merge |
| `preguntémono` | `preguntarse` | 71 | review: merge |
| `replantearno` | `replantearse` | 71 | review: merge |
| `sub-categorías` | `subcategoría` | 71 | review: merge |
| `transformándono` | `transformarse` | 71 | review: merge |
| `anti-bacteriano` | `antibacteriano` | 70 | review: merge |
| `campuse` | `campus` | 70 | review: merge |
| `formé` | `formar` | 70 | review: merge |
| `post-procesado` | `postprocesado` | 70 | review: merge |
| `pre-programadas` | `preprogramado` | 70 | review: merge |
| `re-escribir` | `reescribir` | 70 | review: merge |
| `acompáñe` | `acompañar` | 69 | review: merge |
| `carnecarne` | `carne` | 69 | review: merge |
| `comprarl` | `comprar` | 69 | review: merge |
| `moviéndono` | `moverse` | 69 | review: merge |
| `nacional-socialismo` | `nacionalsocialismo` | 69 | review: merge |
| `re-lanzamiento` | `relanzamiento` | 69 | review: merge |
| `remitirl` | `remitir` | 69 | review: merge |
| `sintiéndolo` | `sentir` | 77 | review: merge |
| `volteándolo` | `voltear` | 77 | review: merge |
| `condenándolo` | `condenar` | 76 | review: merge |
| `elejir` | `elegir` | 76 | review: merge |
| `ingréselo` | `ingresar` | 76 | review: merge |
| `solidariedad` | `solidaridad` | 76 | review: merge |
| `étnia` | `etnia` | 76 | review: merge |
| `crep` | `crepe` | 75 | review: merge |
| `descontinúe` | `descontinuar` | 75 | review: merge |
| `enoxaparin` | `enoxaparina` | 75 | review: merge |
| `esphritu` | `espíritu` | 75 | review: merge |
| `garantizándote` | `garantizar` | 75 | review: merge |
| `hablá` | `hablar` | 75 | review: merge |
| `jázar` | `jázaro` | 75 | review: merge |
| `revolviéndolo` | `revolver` | 75 | review: merge |
| `sométanse` | `someterse` | 75 | review: merge |
| `utilizen` | `utilizar` | 75 | review: merge |
| `acercándo` | `acercar` | 74 | review: merge |
| `alimonar` | `alimonado` | 74 | review: merge |
| `carniceria` | `carnicería` | 74 | review: merge |
| `desarollador` | `desarrollador` | 74 | review: merge |
| `diran` | `decir` | 74 | review: merge |
| `décimocuarto` | `decimocuarto` | 74 | review: merge |
| `encuetra` | `encontrar` | 74 | review: merge |
| `envíamos` | `enviar` | 74 | review: merge |
| `financiamento` | `financiamiento` | 74 | review: merge |
| `possibilidad` | `posibilidad` | 74 | review: merge |
| `reconcíliate` | `reconciliarse` | 74 | review: merge |
| `tantísimos` | `tanto` | 74 | review: merge |
| `acídico` | `ácido` | 73 | review: merge |
| `aplicaci` | `aplicación` | 73 | review: merge |
| `capacítese` | `capacitarse` | 73 | review: merge |
| `despojarlo` | `despojar` | 73 | review: merge |
| `emparejarlo` | `emparejar` | 73 | review: merge |
| `enróllalo` | `enrollar` | 73 | review: merge |
| `imponiéndole` | `imponer` | 73 | review: merge |
| `interaccionando` | `interaccionar` | 73 | review: merge |
| `molona` | `molón` | 73 | review: merge |
| `paparazzis` | `paparazzi` | 73 | review: merge |
| `propietário` | `propietario` | 73 | review: merge |
| `revenderlo` | `revender` | 73 | review: merge |
| `simpatiquísimo` | `simpático` | 73 | review: merge |
| `calef` | `calefacción` | 72 | review: merge |
| `dirije` | `dirigir` | 72 | review: merge |
| `economicos` | `económico` | 72 | review: merge |
| `histopatológicas` | `histopatológico` | 72 | review: merge |
| `mapea` | `mapear` | 72 | review: merge |
| `ocación` | `ocasión` | 72 | review: merge |
| `póngalas` | `poner` | 72 | review: merge |
| `querosén` | `queroseno` | 72 | review: merge |
| `semiolímpica` | `semiolímpico` | 72 | review: merge |
| `sesiona` | `sesionar` | 72 | review: merge |
| `cetera` | `etcétera` | 68 | review: merge |
| `disfrutabl` | `disfrutable` | 68 | review: merge |
| `inculcarl` | `inculcar` | 68 | review: merge |
| `nochenoche` | `noche` | 68 | review: merge |
| `olvidémono` | `olvidarse` | 68 | review: merge |
| `solidos` | `sólido` | 68 | review: merge |
| `trabalengua` | `trabalenguas` | 68 | review: merge |
| `amargur` | `amargura` | 67 | review: merge |
| `anti-social` | `antisocial` | 67 | review: merge |
| `auto-percepción` | `autopercepción` | 67 | review: merge |
| `co-construcción` | `coconstrucción` | 67 | review: merge |
| `escafoid` | `escafoides` | 67 | review: merge |
| `ex-agente` | `exagente` | 67 | review: merge |
| `hooligans` | `hooligan` | 67 | review: merge |
| `háblales` | `hablar` | 67 | review: merge |
| `multi-táctil` | `multitáctil` | 67 | review: merge |
| `re-evaluar` | `reevaluar` | 67 | review: merge |
| `semi-cubierto` | `semicubierto` | 67 | review: merge |
| `contra-reembolso` | `contrarreembolso` | 66 | review: merge |
| `diakonia` | `diaconía` | 66 | review: merge |
| `lloró` | `llorar` | 66 | review: merge |
| `pagándol` | `pagar` | 66 | review: merge |
| `sumérgelo` | `sumergir` | 72 | review: merge |
| `alergía` | `alergia` | 71 | review: merge |
| `bonuse` | `bonus` | 71 | review: merge |
| `ecosistémicos` | `ecosistémico` | 71 | review: merge |
| `insesgados` | `insesgado` | 71 | review: merge |
| `megawatts` | `megavatio` | 71 | review: merge |
| `proponte` | `proponerse` | 71 | review: merge |
| `puntajes` | `puntaje` | 71 | review: merge |
| `quántico` | `cuántico` | 71 | review: merge |
| `reimagina` | `reimaginar` | 71 | review: merge |
| `resurección` | `resurrección` | 71 | review: merge |
| `texturizadas` | `texturizado` | 71 | review: merge |
| `videogame` | `videojuego` | 71 | review: merge |
| `asisitir` | `asistir` | 70 | review: merge |
| `autoexcluir` | `autoexcluirse` | 70 | review: merge |
| `besándola` | `besar` | 70 | review: merge |
| `desprendiéndose` | `desprenderse` | 70 | review: merge |
| `envíen` | `enviar` | 70 | review: merge |
| `fexiblemente` | `flexiblemente` | 70 | review: merge |
| `insume` | `insumir` | 70 | review: merge |
| `methylphenidate` | `metilfenidato` | 70 | review: merge |
| `morira` | `morir` | 70 | review: merge |
| `progesterone` | `progesterona` | 70 | review: merge |
| `tabajo` | `trabajo` | 70 | review: merge |
| `aerospacial` | `aeroespacial` | 69 | review: merge |
| `arrójate` | `arrojarse` | 69 | review: merge |
| `bús` | `bus` | 69 | review: merge |
| `enseñaza` | `enseñanza` | 69 | review: merge |
| `estrese` | `estresarse` | 69 | review: merge |
| `fuxia` | `fucsia` | 69 | review: merge |
| `jijiji` | `jiji` | 69 | review: merge |
| `llamadle` | `llamar` | 69 | review: merge |
| `methadone` | `metadona` | 69 | review: merge |
| `remise` | `remís` | 69 | review: merge |
| `rodhio` | `rodio` | 69 | review: merge |
| `acercándola` | `acercar` | 68 | review: merge |
| `apartemento` | `apartamento` | 68 | review: merge |
| `apdo` | `apartado` | 68 | review: merge |
| `bien-estar` | `bienestar` | 68 | review: merge |
| `co-protagonista` | `coprotagonista` | 68 | review: merge |
| `contándono` | `contar` | 68 | review: merge |
| `despojémono` | `despojarse` | 68 | review: merge |
| `nuestr` | `nuestro` | 68 | review: merge |
| `sangresangre` | `sangre` | 68 | review: merge |
| `arcoiri` | `arcoíris` | 67 | review: merge |
| `buganvilia` | `buganvilla` | 67 | review: merge |
| `concentrémono` | `concentrarse` | 67 | review: merge |
| `embalajes` | `embalaje` | 67 | review: merge |
| `norte-este` | `noreste` | 67 | review: merge |
| `valiéndono` | `valerse` | 67 | review: merge |
| `acuarelabl` | `acuarelable` | 66 | review: merge |
| `anti-austeridad` | `antiausteridad` | 66 | review: merge |
| `esperándol` | `esperar` | 66 | review: merge |
| `involucrándo` | `involucrarse` | 66 | review: merge |
| `mantra-s` | `mantra` | 66 | review: merge |
| `usás` | `usar` | 72 | review: merge |
| `attometro` | `attómetro` | 71 | review: merge |
| `coescribió` | `coescribir` | 71 | review: merge |
| `desmemoriar` | `desmemoriado` | 71 | review: merge |
| `empavesar` | `empavesado` | 71 | review: merge |
| `entregándo` | `entregar` | 71 | review: merge |
| `fibroquística` | `fibroquístico` | 71 | review: merge |
| `frite` | `fritar` | 71 | review: merge |
| `gameplays` | `gameplay` | 71 | review: merge |
| `guantero` | `guantera` | 71 | review: merge |
| `incredula` | `incrédulo` | 71 | review: merge |
| `intersecta` | `intersectar` | 71 | review: merge |
| `melamin` | `melamina` | 71 | review: merge |
| `muestrean` | `muestrear` | 71 | review: merge |
| `neumocócicas` | `neumocócico` | 71 | review: merge |
| `práxis` | `praxis` | 71 | review: merge |
| `seise` | `seis` | 71 | review: merge |
| `telefilm` | `telefilme` | 71 | review: merge |
| `tranquilla` | `tranquilo` | 71 | review: merge |
| `triquis` | `triqui` | 71 | review: merge |
| `yankis` | `yanqui` | 71 | review: merge |
| `acostúmbrese` | `acostumbrarse` | 70 | review: merge |
| `affidávit` | `afidávit` | 70 | review: merge |
| `amenza` | `amenaza` | 70 | review: merge |
| `anonimizan` | `anonimizar` | 70 | review: merge |
| `aprovado` | `aprobar` | 70 | review: merge |
| `ateroscleróticas` | `aterosclerótico` | 70 | review: merge |
| `autoimpuesta` | `autoimpuesto` | 70 | review: merge |
| `chlorhexidine` | `clorhexidina` | 70 | review: merge |
| `ciñéndose` | `ceñirse` | 70 | review: merge |
| `cuotidiano` | `cotidiano` | 70 | review: merge |
| `dadles` | `dar` | 70 | review: merge |
| `estress` | `estrés` | 70 | review: merge |
| `extendiéndola` | `extender` | 70 | review: merge |
| `flasheando` | `flashear` | 70 | review: merge |
| `forzándola` | `forzar` | 70 | review: merge |
| `hornéala` | `hornear` | 70 | review: merge |
| `promocionarlo` | `promocionar` | 70 | review: merge |
| `reabastecido` | `reabastecer` | 70 | review: merge |
| `sobreexplotadas` | `sobreexplotado` | 70 | review: merge |
| `agítala` | `agitar` | 69 | review: merge |
| `apágalo` | `apagar` | 69 | review: merge |
| `cdta` | `cucharadita` | 69 | review: merge |
| `concédale` | `conceder` | 69 | review: merge |
| `dirigiéndola` | `dirigir` | 69 | review: merge |
| `entregándola` | `entregar` | 69 | review: merge |
| `huéspued` | `huésped` | 69 | review: merge |
| `larguísimos` | `largo` | 69 | review: merge |
| `mójate` | `mojarse` | 69 | review: merge |
| `plantéese` | `plantearse` | 69 | review: merge |
| `posherpética` | `posherpético` | 69 | review: merge |
| `pricipal` | `principal` | 69 | review: merge |
| `átate` | `atarse` | 69 | review: merge |
| `aver` | `a ver` | 68 | review: merge |
| `apliquen` | `aplicar` | 68 | review: merge |
| `auto-consciente` | `autoconsciente` | 68 | review: merge |
| `corta-césped` | `cortacésped` | 68 | review: merge |
| `infundirl` | `infundir` | 68 | review: merge |
| `ministrarl` | `ministrar` | 68 | review: merge |
| `practica` | `práctica` | 68 | review: merge |
| `sub-tropical` | `subtropical` | 68 | review: merge |
| `vulnerabilidades` | `vulnerabilidad` | 68 | review: merge |
| `ammonite` | `amonita` | 67 | review: merge |
| `bar-b-que` | `barbacoa` | 67 | review: merge |
| `diece` | `diez` | 67 | review: merge |
| `dícel` | `decir` | 67 | review: merge |
| `ergonómica` | `ergonómico` | 67 | review: merge |
| `estilistas` | `estilista` | 67 | review: merge |
| `jóven` | `joven` | 67 | review: merge |
| `remontándono` | `remontarse` | 67 | review: merge |
| `ultimo` | `último` | 67 | review: merge |
| `venderno` | `vender` | 67 | review: merge |
| `vozvoz` | `voz` | 67 | review: merge |
| `deleitándono` | `deleitarse` | 66 | review: merge |
| `estándard` | `estándar` | 66 | review: merge |
| `hotdog` | `hot dog` | 66 | review: merge |
| `neo-colonial` | `neocolonial` | 66 | review: merge |
| `prestándol` | `prestar` | 66 | review: merge |
| `tomaro` | `tomarse` | 66 | review: merge |
| `sustitúyase` | `sustituir` | 72 | review: merge |
| `compuester` | `componer` | 71 | review: merge |
| `dialogo` | `diálogo` | 71 | review: merge |
| `itinere` | `in itinere` | 71 | review: merge |
| `kilims` | `kilim` | 71 | review: merge |
| `oxymetazoline` | `oximetazolina` | 71 | review: merge |
| `profesionistas` | `profesionista` | 71 | review: merge |
| `redirijan` | `redirigir` | 71 | review: merge |
| `sexualizada` | `sexualizado` | 71 | review: merge |
| `transformándolas` | `transformar` | 71 | review: merge |
| `trombótica` | `trombótico` | 71 | review: merge |
| `adjúntelo` | `adjuntar` | 70 | review: merge |
| `chaqueña` | `chaqueño` | 70 | review: merge |
| `dedíquese` | `dedicarse` | 70 | review: merge |
| `enrrollado` | `enrollado` | 70 | review: merge |
| `nuetro` | `nuestro` | 70 | review: merge |
| `usuarixs` | `usuario` | 70 | review: merge |
| `convenciéndolo` | `convencer` | 69 | review: merge |
| `curricula` | `currículum` | 69 | review: merge |
| `disfrázate` | `disfrazarse` | 69 | review: merge |
| `fribra` | `fibra` | 69 | review: merge |
| `harmónico` | `armónico` | 69 | review: merge |
| `incorporándola` | `incorporar` | 69 | review: merge |
| `movidito` | `movido` | 69 | review: merge |
| `phising` | `phishing` | 69 | review: merge |
| `pozones` | `pozón` | 69 | review: merge |
| `vampíricas` | `vampírico` | 69 | review: merge |
| `arrepiéntase` | `arrepentirse` | 68 | review: merge |
| `balnerario` | `balneario` | 68 | review: merge |
| `anafilaxi` | `anafilaxis` | 68 | review: merge |
| `anti-fraude` | `antifraude` | 68 | review: merge |
| `contactarno` | `contactar` | 68 | review: merge |
| `cortaúña` | `cortaúñas` | 68 | review: merge |
| `diosesdiose` | `dios` | 68 | review: merge |
| `mañanamañana` | `mañana` | 68 | review: merge |
| `membresías` | `membresía` | 68 | review: merge |
| `pro-bono` | `pro bono` | 68 | review: merge |
| `alejándol` | `alejar` | 67 | review: merge |
| `anti-incendio` | `antiincendios` | 67 | review: merge |
| `bendecidos` | `bendecido` | 67 | review: merge |
| `bodysuit` | `body` | 67 | review: merge |
| `co-conspirador` | `coconspirador` | 67 | review: merge |
| `mandándono` | `mandar` | 67 | review: merge |
| `platanito` | `plátano` | 67 | review: merge |
| `resuélvase` | `resolver` | 67 | review: merge |
| `yurt` | `yurta` | 67 | review: merge |
| `conociéndono` | `conocerse` | 66 | review: merge |
| `dabigatr` | `dabigatrán` | 66 | review: merge |
| `divulgada` | `divulgar` | 66 | review: merge |
| `eco-sostenible` | `ecosostenible` | 66 | review: merge |
| `expandiéndono` | `expandirse` | 66 | review: merge |
| `gels` | `gel` | 66 | review: merge |
| `oh-oh` | `oh` | 66 | review: merge |
| `torreña` | `torreño` | 72 | review: merge |
| `autodirigida` | `autodirigido` | 71 | review: merge |
| `campesinxs` | `campesino` | 71 | review: merge |
| `comuníquele` | `comunicar` | 71 | review: merge |
| `dulcísimo` | `dulce` | 71 | review: merge |
| `ejecútela` | `ejecutar` | 71 | review: merge |
| `gulags` | `gulag` | 71 | review: merge |
| `inaguración` | `inauguración` | 71 | review: merge |
| `mátalo` | `matar` | 71 | review: merge |
| `pgina` | `página` | 71 | review: merge |
| `potentísima` | `potente` | 71 | review: merge |
| `psycodelico` | `psicodélico` | 71 | review: merge |
| `rebufar` | `rebufo` | 71 | review: merge |
| `requisite` | `requisito` | 71 | review: merge |
| `vivito` | `vivo` | 71 | review: merge |
| `alejándote` | `alejarse` | 70 | review: merge |
| `autodirigidos` | `autodirigido` | 70 | review: merge |
| `crucificadle` | `crucificar` | 70 | review: merge |
| `desmontarlo` | `desmontar` | 70 | review: merge |
| `dominatrices` | `dominatriz` | 70 | review: merge |
| `eligido` | `elegir` | 70 | review: merge |
| `enjutar` | `enjuto` | 70 | review: merge |
| `folklor` | `folclore` | 70 | review: merge |
| `hazar` | `hazara` | 70 | review: merge |
| `impase` | `impasse` | 70 | review: merge |
| `koreano` | `coreano` | 70 | review: merge |
| `naútica` | `náutica` | 70 | review: merge |
| `platforma` | `plataforma` | 70 | review: merge |
| `psicoterapéuticas` | `psicoterapéutico` | 70 | review: merge |
| `reintroducidos` | `reintroducir` | 70 | review: merge |
| `vistante` | `visitante` | 70 | review: merge |
| `zakaah` | `zakat` | 70 | review: merge |
| `bloggero` | `bloguero` | 69 | review: merge |
| `caloroso` | `caluroso` | 69 | review: merge |
| `crowfunding` | `crowdfunding` | 69 | review: merge |
| `enfrentémoslo` | `enfrentar` | 69 | review: merge |
| `gólems` | `gólem` | 69 | review: merge |
| `limpiao` | `limpiarse` | 69 | review: merge |
| `mantené` | `mantener` | 69 | review: merge |
| `microbial` | `microbiano` | 69 | review: merge |
| `refrigérala` | `refrigerar` | 69 | review: merge |
| `semidesnuda` | `semidesnudo` | 69 | review: merge |
| `alentejana` | `alentejano` | 68 | review: merge |
| `atacameña` | `atacameño` | 68 | review: merge |
| `borreguito` | `borrego` | 68 | review: merge |
| `bátelo` | `batir` | 68 | review: merge |
| `búscar` | `buscar` | 68 | review: merge |
| `calefactadas` | `calefactado` | 68 | review: merge |
| `comenzé` | `comenzar` | 68 | review: merge |
| `cuboid` | `cuboide` | 68 | review: merge |
| `dejándolo` | `dejar` | 68 | review: merge |
| `desamorar` | `desamor` | 68 | review: merge |
| `dimenhydrinate` | `dimenhidrinato` | 68 | review: merge |
| `disfutar` | `disfrutar` | 68 | review: merge |
| `disponiéndose` | `disponerse` | 68 | review: merge |
| `dándo` | `dar` | 68 | review: merge |
| `dánoslo` | `dar` | 68 | review: merge |
| `encintadoras` | `encintadora` | 68 | review: merge |
| `entenderlos` | `entender` | 68 | review: merge |
| `eurocéntrica` | `eurocéntrico` | 68 | review: merge |
| `fresquísimo` | `fresco` | 68 | review: merge |
| `guarnicioner` | `guarnicionería` | 68 | review: merge |
| `heparin` | `heparina` | 68 | review: merge |
| `hoteleria` | `hotelería` | 68 | review: merge |
| `inmunoquímica` | `inmunoquímico` | 68 | review: merge |
| `linguística` | `lingüística` | 68 | review: merge |
| `linguístico` | `lingüístico` | 68 | review: merge |
| `mandarlas` | `mandar` | 68 | review: merge |
| `morenito` | `moreno` | 68 | review: merge |
| `mostradme` | `mostrar` | 68 | review: merge |
| `netural` | `neutral` | 68 | review: merge |
| `nisiquiera` | `ni siquiera` | 68 | review: merge |
| `nmero` | `número` | 68 | review: merge |
| `permítase` | `permitir` | 68 | review: merge |
| `personalícela` | `personalizar` | 68 | review: merge |
| `procedimento` | `procedimiento` | 68 | review: merge |
| `pulgs` | `pulgada` | 68 | review: merge |
| `quier` | `querer` | 68 | review: merge |
| `relacionándolo` | `relacionar` | 68 | review: merge |
| `representate` | `representante` | 68 | review: merge |
| `sometiéndolo` | `someter` | 68 | review: merge |
| `sostenla` | `sostener` | 68 | review: merge |
| `símplemente` | `simplemente` | 68 | review: merge |
| `transfiérelo` | `transferir` | 68 | review: merge |
| `afrontémoslo` | `afrontar` | 67 | review: merge |
| `apreciados` | `apreciado` | 67 | review: merge |
| `arrastrándome` | `arrastrar` | 67 | review: merge |
| `arrástre` | `arrastrar` | 67 | review: merge |
| `audioguías` | `audioguía` | 67 | review: merge |
| `bromea` | `bromear` | 67 | review: merge |
| `canalera` | `canalero` | 67 | review: merge |
| `carenciadas` | `carenciado` | 67 | review: merge |
| `cerdita` | `cerdo` | 67 | review: merge |
| `cibernautas` | `cibernauta` | 67 | review: merge |
| `contrasena` | `contraseña` | 67 | review: merge |
| `copatrocinada` | `copatrocinar` | 67 | review: merge |
| `cuchiller` | `cuchillería` | 67 | review: merge |
| `desátenlo` | `desatar` | 67 | review: merge |
| `dólares` | `dólar` | 67 | review: merge |
| `enfocándome` | `enfocarse` | 67 | review: merge |
| `enjuagarla` | `enjuagar` | 67 | review: merge |
| `enróllala` | `enrollar` | 67 | review: merge |
| `enstala` | `instalar` | 67 | review: merge |
| `estuprar` | `estupro` | 67 | review: merge |
| `exhortándoos` | `exhortar` | 67 | review: merge |
| `extruidas` | `extruir` | 67 | review: merge |
| `fandoms` | `fandom` | 67 | review: merge |
| `fríela` | `freír` | 67 | review: merge |
| `frótelo` | `frotar` | 67 | review: merge |
| `gravísimas` | `grave` | 67 | review: merge |
| `hipertónica` | `hipertónico` | 67 | review: merge |
| `insértese` | `insertar` | 67 | review: merge |
| `interesantísimas` | `interesante` | 67 | review: merge |
| `inuits` | `inuit` | 67 | review: merge |
| `lubrificar` | `lubricar` | 67 | review: merge |
| `límpio` | `limpio` | 67 | review: merge |
| `manano` | `mañana` | 67 | review: merge |
| `matérica` | `matérico` | 67 | review: merge |
| `meterte` | `meterse` | 67 | review: merge |
| `micológica` | `micológico` | 67 | review: merge |
| `microesferas` | `microesfera` | 67 | review: merge |
| `monísimo` | `mono` | 67 | review: merge |
| `mézclela` | `mezclar` | 67 | review: merge |
| `parabenes` | `parabeno` | 67 | review: merge |
| `permeando` | `permear` | 67 | review: merge |
| `persiguiéndo` | `perseguir` | 67 | review: merge |
| `pronostico` | `pronóstico` | 67 | review: merge |
| `péinate` | `peinarse` | 67 | review: merge |
| `redireccionada` | `redireccionar` | 67 | review: merge |
| `relizar` | `realizar` | 67 | review: merge |
| `sazónalo` | `sazonar` | 67 | review: merge |
| `solicitándola` | `solicitar` | 67 | review: merge |
| `sometedla` | `someter` | 67 | review: merge |
| `subatendidas` | `subatendido` | 67 | review: merge |
| `submuniciones` | `submunición` | 67 | review: merge |
| `suspensiónes` | `suspensión` | 67 | review: merge |
| `sustitúyalo` | `sustituir` | 67 | review: merge |
| `sílica` | `sílice` | 67 | review: merge |
| `sóis` | `ser` | 67 | review: merge |
| `tempranito` | `temprano` | 67 | review: merge |
| `trasládese` | `trasladarse` | 67 | review: merge |
| `trinidade` | `trinidad` | 67 | review: merge |
| `vacúnese` | `vacunarse` | 67 | review: merge |
| `rencontrar` | `reencontrarse` | 67 | review: merge |
| `vestidores` | `vestidor` | 66 | review: merge |
| `beatísima` | `beato` | 65 | review: merge |
| `cantaloupe` | `cantalupo` | 65 | review: merge |
| `corazóncorazón` | `corazón` | 65 | review: merge |
| `deslizarno` | `deslizarse` | 65 | review: merge |
| `destacadas` | `destacado` | 65 | review: merge |
| `digoxin` | `digoxina` | 65 | review: merge |
| `dormirno` | `dormirse` | 65 | review: merge |
| `e-bicis` | `e-bici` | 65 | review: merge |
| `eco-sistema` | `ecosistema` | 65 | review: merge |
| `consérvela` | `conservar` | 66 | review: merge |
| `contario` | `contrario` | 66 | review: merge |
| `covertura` | `cobertura` | 66 | review: merge |
| `cámera` | `cámara` | 66 | review: merge |
| `debio` | `deber` | 66 | review: merge |
| `desabrir` | `desabrido` | 66 | review: merge |
| `descarge` | `descargar` | 66 | review: merge |
| `desinformada` | `desinformado` | 66 | review: merge |
| `desosar` | `deshuesar` | 66 | review: merge |
| `detentor` | `detentador` | 66 | review: merge |
| `discrminación` | `discriminación` | 66 | review: merge |
| `dopaminérgicas` | `dopaminérgico` | 66 | review: merge |
| `echá` | `echar` | 66 | review: merge |
| `engalletadoras` | `engalletadora` | 66 | review: merge |
| `envíanoslo` | `enviar` | 66 | review: merge |
| `esforcémonos` | `esforzarse` | 66 | review: merge |
| `estírese` | `estirarse` | 66 | review: merge |
| `exhibiéndose` | `exhibirse` | 66 | review: merge |
| `extirparlo` | `extirpar` | 66 | review: merge |
| `fluídez` | `fluidez` | 66 | review: merge |
| `guardándolo` | `guardar` | 66 | review: merge |
| `habiéndoles` | `haber` | 66 | review: merge |
| `incorporándolo` | `incorporar` | 66 | review: merge |
| `insituto` | `instituto` | 66 | review: merge |
| `insértala` | `insertar` | 66 | review: merge |
| `intrahepática` | `intrahepático` | 66 | review: merge |
| `intégrelo` | `integrar` | 66 | review: merge |
| `jajajaj` | `jajaja` | 66 | review: merge |
| `juguetera` | `juguetero` | 66 | review: merge |
| `juntarlo` | `juntar` | 66 | review: merge |
| `kilito` | `kilo` | 66 | review: merge |
| `logeado` | `loguear` | 66 | review: merge |
| `lorquina` | `lorquino` | 66 | review: merge |
| `lujazo` | `lujo` | 66 | review: merge |
| `matifica` | `matificar` | 66 | review: merge |
| `mayorcito` | `mayor` | 66 | review: merge |
| `modifíquelo` | `modificar` | 66 | review: merge |
| `motivándolo` | `motivar` | 66 | review: merge |
| `mtro` | `maestro` | 66 | review: merge |
| `mudas` | `mudar` | 66 | review: merge |
| `neutrónica` | `neutrónico` | 66 | review: merge |
| `paracaidas` | `paracaídas` | 66 | review: merge |
| `peruviano` | `peruano` | 66 | review: merge |
| `playazo` | `playa` | 66 | review: merge |
| `potenciométrica` | `potenciométrico` | 66 | review: merge |
| `protectiva` | `protector` | 66 | review: merge |
| `purifícate` | `purificarse` | 66 | review: merge |
| `regálale` | `regalar` | 66 | review: merge |
| `reinterpretados` | `reinterpretar` | 66 | review: merge |
| `reponsable` | `responsable` | 66 | review: merge |
| `ruidito` | `ruido` | 66 | review: merge |
| `sacadla` | `sacar` | 66 | review: merge |
| `silenciarlo` | `silenciar` | 66 | review: merge |
| `similiar` | `similar` | 66 | review: merge |
| `sueters` | `suéter` | 66 | review: merge |
| `suminístrele` | `suministrar` | 66 | review: merge |
| `tecnificada` | `tecnificado` | 66 | review: merge |
| `testerone` | `testosterona` | 66 | review: merge |
| `tintorerias` | `tintorería` | 66 | review: merge |
| `transfondo` | `trasfondo` | 66 | review: merge |
| `trasportados` | `transportar` | 66 | review: merge |
| `tóquelo` | `tocar` | 66 | review: merge |
| `valroaciones` | `valoración` | 66 | review: merge |
| `vedlo` | `ver` | 66 | review: merge |
| `voltéala` | `voltear` | 66 | review: merge |
| `átalo` | `atar` | 66 | review: merge |
| `aceptándola` | `aceptar` | 65 | review: merge |
| `acoje` | `acoger` | 65 | review: merge |
| `adaptándo` | `adaptarse` | 65 | review: merge |
| `aferrándome` | `aferrarse` | 65 | review: merge |
| `alumino` | `aluminio` | 65 | review: merge |
| `analizarlo` | `analizar` | 65 | review: merge |
| `anonimizaremos` | `anonimizar` | 65 | review: merge |
| `anterógrada` | `anterógrado` | 65 | review: merge |
| `apartadme` | `apartar` | 65 | review: merge |
| `arbitro` | `árbitro` | 65 | review: merge |
| `arréglate` | `arreglarse` | 65 | review: merge |
| `beisbolera` | `beisbolero` | 65 | review: merge |
| `blanquito` | `blanco` | 65 | review: merge |
| `brunchs` | `brunch` | 65 | review: merge |
| `caponar` | `capón` | 65 | review: merge |
| `chavistas` | `chavista` | 65 | review: merge |
| `clicka` | `clicar` | 65 | review: merge |
| `convirtiéndolo` | `convertir` | 65 | review: merge |
| `cosplayers` | `cosplayer` | 65 | review: merge |
| `desenchúfela` | `desenchufar` | 65 | review: merge |
| `deslizándose` | `deslizarse` | 65 | review: merge |
| `dulcísima` | `dulce` | 65 | review: merge |
| `dásela` | `dar` | 65 | review: merge |
| `dúchese` | `ducharse` | 65 | review: merge |
| `edificaos` | `edificar` | 65 | review: merge |
| `eritematosa` | `eritematoso` | 65 | review: merge |
| `exhuberante` | `exuberante` | 65 | review: merge |
| `experienca` | `experiencia` | 65 | review: merge |
| `floto` | `flota` | 65 | review: merge |
| `fruter` | `frutería` | 65 | review: merge |
| `ghrelin` | `grelina` | 65 | review: merge |
| `gruir` | `gruyer` | 65 | review: merge |
| `gástalo` | `gastar` | 65 | review: merge |
| `l-cisteína` | `cisteína` | 65 | review: merge |
| `l-lisina` | `lisina` | 65 | review: merge |
| `l-valina` | `valina` | 65 | review: merge |
| `multi-hilo` | `multihilo` | 65 | review: merge |
| `obligarno` | `obligar` | 65 | review: merge |
| `revestío` | `revestirse` | 65 | review: merge |
| `rogad` | `rogar` | 65 | review: merge |
| `rosuvastatin` | `rosuvastatina` | 65 | review: merge |
| `secuelas` | `secuela` | 65 | review: merge |
| `semi-abierto` | `semiabierto` | 65 | review: merge |
| `sheol` | `seol` | 65 | review: merge |
| `videográfica` | `videográfico` | 67 | review: merge |
| `yoghurt` | `yogur` | 67 | review: merge |
| `zakah` | `zakat` | 67 | review: merge |
| `abrumante` | `abrumador` | 66 | review: merge |
| `aceptémoslo` | `aceptar` | 66 | review: merge |
| `agrupándolo` | `agrupar` | 66 | review: merge |
| `ahorrándote` | `ahorrar` | 66 | review: merge |
| `amabilísimo` | `amable` | 66 | review: merge |
| `amnéstico` | `amnésico` | 66 | review: merge |
| `aprovecharlas` | `aprovechar` | 66 | review: merge |
| `atribuído` | `atribuir` | 66 | review: merge |
| `cafetaleras` | `cafetalero` | 66 | review: merge |
| `calificándola` | `calificar` | 66 | review: merge |
| `canjearlo` | `canjear` | 66 | review: merge |
| `informándome` | `informar` | 65 | review: merge |
| `instruído` | `instruir` | 65 | review: merge |
| `jaur` | `jauría` | 65 | review: merge |
| `jueguito` | `juego` | 65 | review: merge |
| `juzgadle` | `juzgar` | 65 | review: merge |
| `lobbys` | `lobby` | 65 | review: merge |
| `maculosa` | `maculoso` | 65 | review: merge |
| `menthol` | `mentol` | 65 | review: merge |
| `metastatizado` | `metastatizar` | 65 | review: merge |
| `miniaturizada` | `miniaturizado` | 65 | review: merge |
| `misma` | `mismo` | 65 | review: merge |
| `mismxs` | `mismo` | 65 | review: merge |
| `monísimos` | `mono` | 65 | review: merge |
| `movilizadora` | `movilizador` | 65 | review: merge |
| `muéstrenme` | `mostrar` | 65 | review: merge |
| `orwelliana` | `orwelliano` | 65 | review: merge |
| `osteoporótica` | `osteoporótico` | 65 | review: merge |
| `pagadle` | `pagar` | 65 | review: merge |
| `pendenciar` | `pendencia` | 65 | review: merge |
| `pisicina` | `piscina` | 65 | review: merge |
| `pitbulls` | `pitbull` | 65 | review: merge |
| `postherpética` | `postherpético` | 65 | review: merge |
| `protejer` | `proteger` | 65 | review: merge |
| `quejándote` | `quejarse` | 65 | review: merge |
| `quemólo` | `quemar` | 65 | review: merge |
| `rayita` | `raya` | 65 | review: merge |
| `recibidle` | `recibir` | 65 | review: merge |
| `renderice` | `renderizar` | 65 | review: merge |
| `rindiéndole` | `rendir` | 65 | review: merge |
| `rockeando` | `rockear` | 65 | review: merge |
| `rostizados` | `rostizado` | 65 | review: merge |
| `rosto` | `rostro` | 65 | review: merge |
| `saborizadas` | `saborizado` | 65 | review: merge |
| `sencillísima` | `sencillo` | 65 | review: merge |
| `sidrera` | `sidrero` | 65 | review: merge |
| `someteos` | `someterse` | 65 | review: merge |
| `sopresa` | `sorpresa` | 65 | review: merge |
| `spaming` | `spam` | 65 | review: merge |
| `succionada` | `succionar` | 65 | review: merge |
| `sujétela` | `sujetar` | 65 | review: merge |
| `superviviencia` | `supervivencia` | 65 | review: merge |
| `halar` | `halo` | 4,306 | review: merge |
| `hombr` | `hombría` | 45 | review: merge |
| `ufanar` | `ufanarse` | 90 | review: merge |
| `bazucar` | `bazuca` | 69 | review: merge |
| `extension` | `extensión` | 20,319 | accented spelling 310,132 vs 20,319 |
| `america` | `américa` | 19,753 | accented spelling 166,255 vs 19,753 |
| `codigo` | `código` | 14,859 | accented spelling 436,357 vs 14,859 |
| `via` | `vía` | 12,278 | accented spelling 295,818 vs 12,278 |
| `berlin` | `berlín` | 12,241 | accented spelling 111,482 vs 12,241 |
| `menu` | `menú` | 11,506 | accented spelling 251,105 vs 11,506 |
| `jose` | `josé` | 11,285 | accented spelling 152,710 vs 11,285 |
| `union` | `unión` | 11,155 | accented spelling 157,146 vs 11,155 |
| `panama` | `panamá` | 9,807 | accented spelling 95,703 vs 9,807 |
| `canada` | `canadá` | 9,473 | accented spelling 172,055 vs 9,473 |
| `salon` | `salón` | 8,257 | accented spelling 298,357 vs 8,257 |
| `angel` | `ángel` | 8,076 | accented spelling 115,834 vs 8,076 |
| `dragon` | `dragón` | 7,433 | accented spelling 38,560 vs 7,433 |
| `record` | `récord` | 6,732 | accented spelling 44,291 vs 6,732 |
| `personalizacion` | `personalización` | 6,368 | accented spelling 42,261 vs 6,368 |
| `futbol` | `fútbol` | 6,266 | accented spelling 155,424 vs 6,266 |
| `compañia` | `compañía` | 6,190 | accented spelling 704,296 vs 6,190 |
| `pension` | `pensión` | 6,123 | accented spelling 54,244 vs 6,123 |
| `fusion` | `fusión` | 6,081 | accented spelling 58,914 vs 6,081 |
| `milan` | `milán` | 6,040 | accented spelling 98,098 vs 6,040 |
| `peru` | `perú` | 5,886 | accented spelling 138,416 vs 5,886 |
| `tenia` | `tener` | 5,543 | accented spelling 192,839 vs 5,543 |
| `cordoba` | `córdoba` | 5,255 | accented spelling 49,035 vs 5,255 |
| `television` | `televisión` | 5,199 | accented spelling 302,201 vs 5,199 |
| `version` | `versión` | 4,884 | accented spelling 561,239 vs 4,884 |
| `dia` | `día` | 4,699 | accented spelling 3,135,517 vs 4,699 |
| `cancer` | `cáncer` | 4,541 | accented spelling 368,281 vs 4,541 |
| `aaron` | `aarón` | 4,476 | accented spelling 36,088 vs 4,476 |
| `dublin` | `dublín` | 4,417 | accented spelling 65,242 vs 4,417 |
| `busqueda` | `búsqueda` | 4,416 | accented spelling 1,076,144 vs 4,416 |
| `bahia` | `bahía` | 4,254 | accented spelling 90,851 vs 4,254 |
| `raices` | `raíz` | 4,057 | accented spelling 51,927 vs 4,057 |
| `galeria` | `galería` | 3,896 | accented spelling 127,865 vs 3,896 |
| `comodo` | `cómodo` | 3,828 | accented spelling 289,446 vs 3,828 |
| `napoles` | `nápoles` | 3,821 | accented spelling 27,250 vs 3,821 |
| `dusseldorf` | `düsseldorf` | 3,808 | accented spelling 20,078 vs 3,808 |
| `canton` | `cantón` | 3,675 | accented spelling 19,181 vs 3,675 |
| `taiwan` | `taiwán` | 3,232 | accented spelling 29,251 vs 3,232 |
| `lopez` | `lópez` | 3,135 | accented spelling 31,368 vs 3,135 |
| `garcia` | `garcía` | 3,096 | accented spelling 38,486 vs 3,096 |
| `todavia` | `todavía` | 3,086 | accented spelling 413,817 vs 3,086 |
| `linea` | `línea` | 3,074 | accented spelling 1,588,542 vs 3,074 |
| `malaga` | `málaga` | 3,047 | accented spelling 118,615 vs 3,047 |
| `bateria` | `batería` | 3,018 | accented spelling 309,928 vs 3,018 |
| `corazon` | `corazón` | 3,006 | accented spelling 654,493 vs 3,006 |
| `poliester` | `poliéster` | 2,986 | accented spelling 43,861 vs 2,986 |
| `area` | `área` | 2,917 | accented spelling 770,302 vs 2,917 |
| `coctel` | `cóctel` | 2,868 | accented spelling 28,613 vs 2,868 |
| `carbon` | `carbón` | 2,846 | accented spelling 49,369 vs 2,846 |
| `precision` | `precisión` | 2,834 | accented spelling 191,584 vs 2,834 |
| `oir` | `oír` | 2,816 | accented spelling 146,218 vs 2,816 |
| `andalucia` | `andalucía` | 2,763 | accented spelling 47,748 vs 2,763 |
| `fantasia` | `fantasía` | 2,724 | accented spelling 42,374 vs 2,724 |
| `descripcion` | `descripción` | 2,651 | accented spelling 643,262 vs 2,651 |
| `rodriguez` | `rodríguez` | 2,645 | accented spelling 27,267 vs 2,645 |
| `merida` | `mérida` | 2,629 | accented spelling 16,642 vs 2,629 |
| `sidney` | `sídney` | 2,592 | accented spelling 25,608 vs 2,592 |
| `martinez` | `martínez` | 2,588 | accented spelling 20,618 vs 2,588 |
| `ramon` | `ramón` | 2,471 | accented spelling 15,108 vs 2,471 |
| `mansion` | `mansión` | 2,455 | accented spelling 20,919 vs 2,455 |
| `construccion` | `construcción` | 2,447 | accented spelling 510,005 vs 2,447 |
| `genesis` | `génesis` | 2,422 | accented spelling 24,808 vs 2,422 |
| `pelicula` | `película` | 2,421 | accented spelling 383,192 vs 2,421 |
| `boton` | `botón` | 2,406 | accented spelling 435,876 vs 2,406 |
| `increible` | `increíble` | 2,366 | accented spelling 179,201 vs 2,366 |
| `perdida` | `pérdida` | 2,350 | accented spelling 340,080 vs 2,350 |
| `principe` | `príncipe` | 2,301 | accented spelling 64,583 vs 2,301 |
| `guias` | `guía` | 2,225 | accented spelling 55,698 vs 2,225 |
| `replica` | `réplica` | 2,217 | accented spelling 17,201 vs 2,217 |
| `division` | `división` | 2,210 | accented spelling 115,892 vs 2,210 |
| `paraiso` | `paraíso` | 2,191 | accented spelling 59,166 vs 2,191 |
| `electrico` | `eléctrico` | 2,183 | accented spelling 336,900 vs 2,183 |
| `juarez` | `juárez` | 2,174 | accented spelling 14,786 vs 2,174 |
| `item` | `ítem` | 2,166 | accented spelling 16,531 vs 2,166 |
| `habitat` | `hábitat` | 2,132 | accented spelling 31,306 vs 2,132 |
| `podria` | `poder` | 2,126 | accented spelling 337,741 vs 2,126 |
| `estacion` | `estación` | 2,103 | accented spelling 479,198 vs 2,103 |
| `estandar` | `estándar` | 2,042 | accented spelling 394,355 vs 2,042 |
| `opcion` | `opción` | 2,034 | accented spelling 919,323 vs 2,034 |
| `hare` | `hacer` | 1,996 | accented spelling 20,161 vs 1,996 |
| `monaco` | `mónaco` | 1,987 | accented spelling 12,428 vs 1,987 |
| `gomez` | `gómez` | 1,975 | accented spelling 15,028 vs 1,975 |
| `atico` | `ático` | 1,971 | accented spelling 34,145 vs 1,971 |
| `optima` | `óptimo` | 1,962 | accented spelling 46,107 vs 1,962 |
| `fotografia` | `fotografía` | 1,951 | accented spelling 193,996 vs 1,951 |
| `rincon` | `rincón` | 1,942 | accented spelling 56,757 vs 1,942 |
| `seran` | `ser` | 1,939 | accented spelling 184,889 vs 1,939 |
| `formula` | `fórmula` | 1,933 | accented spelling 85,892 vs 1,933 |
| `peninsula` | `península` | 1,915 | accented spelling 34,003 vs 1,915 |
| `salomon` | `salomón` | 1,904 | accented spelling 32,523 vs 1,904 |
| `gonzalez` | `gonzález` | 1,893 | accented spelling 27,160 vs 1,893 |
| `perez` | `pérez` | 1,782 | accented spelling 22,176 vs 1,782 |
| `jehova` | `jehová` | 1,781 | accented spelling 232,854 vs 1,781 |
| `relacion` | `relación` | 1,720 | accented spelling 851,322 vs 1,720 |
| `basico` | `básico` | 1,719 | accented spelling 250,148 vs 1,719 |
| `credito` | `crédito` | 1,719 | accented spelling 203,179 vs 1,719 |
| `aplicacion` | `aplicación` | 1,689 | accented spelling 1,253,516 vs 1,689 |
| `rapidamente` | `rápidamente` | 1,670 | accented spelling 302,953 vs 1,670 |
| `balcon` | `balcón` | 1,663 | accented spelling 149,008 vs 1,663 |
| `proximo` | `próximo` | 1,650 | accented spelling 409,143 vs 1,650 |
| `neon` | `neón` | 1,618 | accented spelling 8,293 vs 1,618 |
| `mexico` | `méxico` | 1,611 | accented spelling 469,335 vs 1,611 |
| `movil` | `móvil` | 1,595 | accented spelling 481,518 vs 1,595 |
| `dias` | `día` | 1,584 | accented spelling 906,920 vs 1,584 |
| `instalacion` | `instalación` | 1,568 | accented spelling 577,945 vs 1,568 |
| `espiritu` | `espíritu` | 1,567 | accented spelling 380,159 vs 1,567 |
| `distribucion` | `distribución` | 1,567 | accented spelling 252,410 vs 1,567 |
| `automaticamente` | `automáticamente` | 1,558 | accented spelling 245,755 vs 1,558 |
| `toner` | `tóner` | 1,547 | accented spelling 10,416 vs 1,547 |
| `mediterraneo` | `mediterráneo` | 1,536 | accented spelling 99,051 vs 1,536 |
| `pokemon` | `pokémon` | 1,535 | accented spelling 20,000 vs 1,535 |
| `grafico` | `gráfico` | 1,529 | accented spelling 191,138 vs 1,529 |
| `diaz` | `díaz` | 1,519 | accented spelling 13,774 vs 1,519 |
| `mandarin` | `mandarín` | 1,499 | accented spelling 8,247 vs 1,499 |
| `cache` | `caché` | 1,496 | accented spelling 23,394 vs 1,496 |
| `cristobal` | `cristóbal` | 1,489 | accented spelling 10,868 vs 1,489 |
| `plastico` | `plástico` | 1,461 | accented spelling 267,645 vs 1,461 |
| `bolivar` | `bolívar` | 1,460 | accented spelling 11,960 vs 1,460 |
| `sanchez` | `sánchez` | 1,455 | accented spelling 20,936 vs 1,455 |
| `francfort` | `fráncfort` | 1,455 | accented spelling 26,406 vs 1,455 |
| `frances` | `francés` | 1,428 | accented spelling 207,843 vs 1,428 |
| `turistico` | `turístico` | 1,412 | accented spelling 175,301 vs 1,412 |
| `miro` | `mirar` | 1,399 | accented spelling 15,145 vs 1,399 |
| `avila` | `ávila` | 1,384 | accented spelling 8,372 vs 1,384 |
| `tecnicos` | `técnico` | 1,372 | accented spelling 89,094 vs 1,372 |
| `historico` | `histórico` | 1,370 | accented spelling 274,088 vs 1,370 |
| `proximamente` | `próximamente` | 1,364 | accented spelling 11,861 vs 1,364 |
| `modem` | `módem` | 1,356 | accented spelling 10,921 vs 1,356 |
| `dali` | `dalí` | 1,340 | accented spelling 7,832 vs 1,340 |
| `terminos` | `término` | 1,332 | accented spelling 286,381 vs 1,332 |
| `aqui` | `aquí` | 1,328 | accented spelling 1,601,980 vs 1,328 |
| `sofa` | `sofá` | 1,310 | accented spelling 112,288 vs 1,310 |
| `opinion` | `opinión` | 1,307 | accented spelling 552,212 vs 1,307 |
| `educacion` | `educación` | 1,300 | accented spelling 467,490 vs 1,300 |
| `haiti` | `haití` | 1,286 | accented spelling 27,229 vs 1,286 |
| `sabado` | `sábado` | 1,274 | accented spelling 198,505 vs 1,274 |
| `judio` | `judío` | 1,269 | accented spelling 100,920 vs 1,269 |
| `calefaccion` | `calefacción` | 1,260 | accented spelling 198,477 vs 1,260 |
| `gestion` | `gestión` | 1,256 | accented spelling 644,421 vs 1,256 |
| `alvaro` | `álvaro` | 1,241 | accented spelling 8,302 vs 1,241 |
| `fabricacion` | `fabricación` | 1,235 | accented spelling 304,209 vs 1,235 |
| `reparacion` | `reparación` | 1,221 | accented spelling 138,418 vs 1,221 |
| `reir` | `reír` | 1,221 | accented spelling 19,363 vs 1,221 |
| `mazatlan` | `mazatlán` | 1,217 | accented spelling 8,338 vs 1,217 |
| `estanteria` | `estantería` | 1,212 | accented spelling 19,768 vs 1,212 |
| `produccion` | `producción` | 1,208 | accented spelling 691,482 vs 1,208 |
| `carton` | `cartón` | 1,205 | accented spelling 77,903 vs 1,205 |
| `tia` | `tía` | 1,195 | accented spelling 11,184 vs 1,195 |
| `situacion` | `situación` | 1,193 | accented spelling 505,942 vs 1,193 |
| `duo` | `dúo` | 1,190 | accented spelling 13,847 vs 1,190 |
| `analisis` | `análisis` | 1,181 | accented spelling 535,088 vs 1,181 |
| `oi` | `oír` | 1,167 | accented spelling 7,251 vs 1,167 |
| `tendra` | `tener` | 1,166 | accented spelling 150,288 vs 1,166 |
| `decoracion` | `decoración` | 1,153 | accented spelling 177,912 vs 1,153 |
| `turistica` | `turístico` | 1,147 | accented spelling 30,619 vs 1,147 |
| `especificamente` | `específicamente` | 1,143 | accented spelling 103,819 vs 1,143 |
| `aerolinea` | `aerolínea` | 1,137 | accented spelling 141,545 vs 1,137 |
| `razon` | `razón` | 1,134 | accented spelling 376,129 vs 1,134 |
| `portatil` | `portátil` | 1,131 | accented spelling 186,685 vs 1,131 |
| `pais` | `país` | 1,130 | accented spelling 1,485,108 vs 1,130 |
| `marmol` | `mármol` | 1,119 | accented spelling 52,149 vs 1,119 |
| `tomas` | `tomás` | 1,107 | accented spelling 17,162 vs 1,107 |
| `recien` | `recién` | 1,104 | accented spelling 138,984 vs 1,104 |
| `clasico` | `clásico` | 1,098 | accented spelling 174,919 vs 1,098 |
| `concepcion` | `concepción` | 1,095 | accented spelling 48,510 vs 1,095 |
| `informatica` | `informática` | 1,095 | accented spelling 52,293 vs 1,095 |
| `conexion` | `conexión` | 1,088 | accented spelling 613,859 vs 1,088 |
| `economia` | `economía` | 1,087 | accented spelling 277,833 vs 1,087 |
| `jimenez` | `jiménez` | 1,085 | accented spelling 8,372 vs 1,085 |
| `coleccion` | `colección` | 1,083 | accented spelling 344,338 vs 1,083 |
| `proposito` | `propósito` | 1,083 | accented spelling 239,588 vs 1,083 |
| `hernandez` | `hernández` | 1,082 | accented spelling 18,882 vs 1,082 |
| `satelite` | `satélite` | 1,079 | accented spelling 158,980 vs 1,079 |
| `fernandez` | `fernández` | 1,078 | accented spelling 18,642 vs 1,078 |
| `ceramica` | `cerámica` | 1,077 | accented spelling 71,598 vs 1,077 |
| `energia` | `energía` | 1,077 | accented spelling 756,842 vs 1,077 |
| `capitan` | `capitán` | 1,070 | accented spelling 46,662 vs 1,070 |
| `mato` | `matar` | 1,070 | accented spelling 11,058 vs 1,070 |
| `cadiz` | `cádiz` | 1,062 | accented spelling 19,748 vs 1,062 |
| `organo` | `órgano` | 1,062 | accented spelling 89,956 vs 1,062 |
| `presentacion` | `presentación` | 1,060 | accented spelling 263,702 vs 1,060 |
| `alegria` | `alegría` | 1,058 | accented spelling 100,638 vs 1,058 |
| `salmon` | `salmón` | 1,056 | accented spelling 17,311 vs 1,056 |
| `electrodomestico` | `electrodoméstico` | 1,055 | accented spelling 27,231 vs 1,055 |
| `jupiter` | `júpiter` | 1,045 | accented spelling 10,375 vs 1,045 |
| `ruben` | `rubén` | 1,041 | accented spelling 11,778 vs 1,041 |
| `raiz` | `raíz` | 1,024 | accented spelling 123,466 vs 1,024 |
| `tandem` | `tándem` | 1,023 | accented spelling 5,776 vs 1,023 |
| `dimension` | `dimensión` | 1,018 | accented spelling 119,476 vs 1,018 |
| `queria` | `querer` | 1,017 | accented spelling 60,453 vs 1,017 |
| `latex` | `látex` | 1,008 | accented spelling 13,638 vs 1,008 |
| `hector` | `héctor` | 998 | accented spelling 6,300 vs 998 |
| `electron` | `electrón` | 991 | accented spelling 8,716 vs 991 |
| `veronica` | `verónica` | 990 | accented spelling 6,049 vs 990 |
| `sera` | `ser` | 988 | accented spelling 566,379 vs 988 |
| `ramirez` | `ramírez` | 986 | accented spelling 9,446 vs 986 |
| `fatima` | `fátima` | 983 | accented spelling 9,440 vs 983 |
| `automatico` | `automático` | 983 | accented spelling 353,735 vs 983 |
| `cordon` | `cordón` | 982 | accented spelling 48,378 vs 982 |
| `habra` | `haber` | 982 | accented spelling 69,404 vs 982 |
| `mision` | `misión` | 975 | accented spelling 256,611 vs 975 |
| `estes` | `estar` | 971 | accented spelling 33,135 vs 971 |
| `visito` | `visitar` | 969 | accented spelling 10,359 vs 969 |
| `urbanizacion` | `urbanización` | 961 | accented spelling 51,170 vs 961 |
| `escuche` | `escuchar` | 958 | accented spelling 4,999 vs 958 |
| `tecnico` | `técnico` | 952 | accented spelling 455,499 vs 952 |
| `atletico` | `atlético` | 933 | accented spelling 16,133 vs 933 |
| `redireccion` | `redirección` | 933 | accented spelling 5,921 vs 933 |
| `saul` | `saúl` | 930 | accented spelling 34,834 vs 930 |
| `configuracion` | `configuración` | 929 | accented spelling 408,124 vs 929 |
| `revision` | `revisión` | 927 | accented spelling 171,750 vs 927 |
| `epoca` | `época` | 922 | accented spelling 203,983 vs 922 |
| `ingenieria` | `ingeniería` | 922 | accented spelling 165,788 vs 922 |
| `proxima` | `próximo` | 920 | accented spelling 71,925 vs 920 |
| `multiple` | `múltiple` | 920 | accented spelling 145,825 vs 920 |
| `asociacion` | `asociación` | 916 | accented spelling 279,561 vs 916 |
| `habitacion` | `habitación` | 915 | accented spelling 1,127,646 vs 915 |
| `categoria` | `categoría` | 912 | accented spelling 503,376 vs 912 |
| `podia` | `poder` | 912 | accented spelling 85,827 vs 912 |
| `basilica` | `basílica` | 910 | accented spelling 25,373 vs 910 |
| `aguila` | `águila` | 896 | accented spelling 15,372 vs 896 |
| `comunicacion` | `comunicación` | 893 | accented spelling 535,269 vs 893 |
| `lampara` | `lámpara` | 870 | accented spelling 120,331 vs 870 |
| `africa` | `áfrica` | 859 | accented spelling 139,210 vs 859 |
| `chavez` | `chávez` | 842 | accented spelling 17,902 vs 842 |
| `decision` | `decisión` | 840 | accented spelling 347,669 vs 840 |
| `elias` | `elías` | 837 | accented spelling 22,572 vs 837 |
| `comparacion` | `comparación` | 836 | accented spelling 240,152 vs 836 |
| `metropolis` | `metrópolis` | 831 | accented spelling 6,442 vs 831 |
| `identico` | `idéntico` | 831 | accented spelling 24,903 vs 831 |
| `asesoria` | `asesoría` | 827 | accented spelling 38,123 vs 827 |
| `oman` | `omán` | 821 | accented spelling 5,918 vs 821 |
| `salio` | `salir` | 819 | accented spelling 36,000 vs 819 |
| `estadia` | `estadía` | 812 | accented spelling 45,449 vs 812 |
| `conversion` | `conversión` | 810 | accented spelling 133,294 vs 810 |
| `valvula` | `válvula` | 810 | accented spelling 96,834 vs 810 |
| `rubi` | `rubí` | 804 | accented spelling 5,773 vs 804 |
| `estabamos` | `estar` | 801 | accented spelling 21,147 vs 801 |
| `baku` | `bakú` | 801 | accented spelling 6,418 vs 801 |
| `pregunto` | `preguntar` | 800 | accented spelling 28,835 vs 800 |
| `vivian` | `vivir` | 798 | accented spelling 9,323 vs 798 |
| `religion` | `religión` | 796 | accented spelling 111,127 vs 796 |
| `esten` | `estar` | 795 | accented spelling 106,423 vs 795 |
| `valparaiso` | `valparaíso` | 793 | accented spelling 6,908 vs 793 |
| `masia` | `masía` | 791 | accented spelling 5,114 vs 791 |
| `lavanderia` | `lavandería` | 789 | accented spelling 74,034 vs 789 |
| `centrico` | `céntrico` | 789 | accented spelling 40,959 vs 789 |
| `fantastico` | `fantástico` | 781 | accented spelling 136,929 vs 781 |
| `torreon` | `torreón` | 779 | accented spelling 4,891 vs 779 |
| `joaquin` | `joaquín` | 772 | accented spelling 10,018 vs 772 |
| `grafica` | `gráfica` | 771 | accented spelling 50,885 vs 771 |
| `oceania` | `oceanía` | 770 | accented spelling 12,142 vs 770 |
| `carpinteria` | `carpintería` | 770 | accented spelling 17,029 vs 770 |
| `rene` | `rené` | 769 | accented spelling 5,926 vs 769 |
| `oyo` | `oír` | 767 | accented spelling 10,299 vs 767 |
| `limon` | `limón` | 759 | accented spelling 46,073 vs 759 |
| `cafe` | `café` | 742 | accented spelling 269,909 vs 742 |
| `rustico` | `rústico` | 742 | accented spelling 23,452 vs 742 |
| `antiguedad` | `antigüedad` | 742 | accented spelling 40,923 vs 742 |
| `inversion` | `inversión` | 737 | accented spelling 281,233 vs 737 |
| `pakistan` | `pakistán` | 725 | accented spelling 31,523 vs 725 |
| `creacion` | `creación` | 723 | accented spelling 348,298 vs 723 |
| `sudan` | `sudán` | 719 | accented spelling 19,434 vs 719 |
| `haran` | `hacer` | 716 | accented spelling 31,935 vs 716 |
| `agricola` | `agrícola` | 715 | accented spelling 86,792 vs 715 |
| `simbolo` | `símbolo` | 715 | accented spelling 105,527 vs 715 |
| `joyeria` | `joyería` | 697 | accented spelling 77,085 vs 697 |
| `eliminacion` | `eliminación` | 697 | accented spelling 146,568 vs 697 |
| `esqui` | `esquí` | 695 | accented spelling 106,364 vs 695 |
| `debera` | `deber` | 695 | accented spelling 111,890 vs 695 |
| `vision` | `visión` | 693 | accented spelling 324,729 vs 693 |
| `sinai` | `sinaí` | 692 | accented spelling 9,193 vs 692 |
| `pajaro` | `pájaro` | 692 | accented spelling 37,199 vs 692 |
| `beisbol` | `béisbol` | 691 | accented spelling 30,030 vs 691 |
| `cajon` | `cajón` | 691 | accented spelling 31,097 vs 691 |
| `ayudo` | `ayudar` | 691 | accented spelling 22,162 vs 691 |
| `fundacion` | `fundación` | 689 | accented spelling 186,002 vs 689 |
| `quimica` | `química` | 689 | accented spelling 67,632 vs 689 |
| `suarez` | `suárez` | 688 | accented spelling 7,758 vs 688 |
| `edicion` | `edición` | 685 | accented spelling 251,810 vs 685 |
| `etcetera` | `etcétera` | 682 | accented spelling 272,824 vs 682 |
| `almacen` | `almacén` | 673 | accented spelling 75,639 vs 673 |
| `tanger` | `tánger` | 670 | accented spelling 6,730 vs 670 |
| `clinica` | `clínica` | 666 | accented spelling 109,423 vs 666 |
| `noto` | `notar` | 656 | accented spelling 3,413 vs 656 |
| `exodo` | `éxodo` | 655 | accented spelling 12,335 vs 655 |
| `parana` | `paraná` | 653 | accented spelling 4,712 vs 653 |
| `ocasion` | `ocasión` | 651 | accented spelling 231,887 vs 651 |
| `canaan` | `canaán` | 648 | accented spelling 10,890 vs 648 |
| `cirugia` | `cirugía` | 647 | accented spelling 187,533 vs 647 |
| `reune` | `reunir` | 643 | accented spelling 21,229 vs 643 |
| `musculo` | `músculo` | 641 | accented spelling 76,395 vs 641 |
| `amen` | `amén` | 638 | accented spelling 7,182 vs 638 |
| `dario` | `darío` | 637 | accented spelling 5,592 vs 637 |
| `consultoria` | `consultoría` | 635 | accented spelling 43,677 vs 635 |
| `tenian` | `tener` | 632 | accented spelling 66,555 vs 632 |
| `fisico` | `físico` | 630 | accented spelling 261,822 vs 630 |
| `metodo` | `método` | 630 | accented spelling 373,207 vs 630 |
| `oracion` | `oración` | 618 | accented spelling 147,980 vs 618 |
| `gaudi` | `gaudí` | 616 | accented spelling 13,466 vs 616 |
| `ines` | `inés` | 615 | accented spelling 3,150 vs 615 |
| `tomo` | `tomar` | 612 | accented spelling 51,359 vs 612 |
| `direccion` | `dirección` | 612 | accented spelling 858,020 vs 612 |
| `joas` | `joás` | 610 | accented spelling 4,630 vs 610 |
| `automatica` | `automático` | 610 | accented spelling 99,285 vs 610 |
| `osea` | `óseo` | 609 | accented spelling 8,029 vs 609 |
| `dare` | `dar` | 606 | accented spelling 12,800 vs 606 |
| `algodon` | `algodón` | 606 | accented spelling 146,803 vs 606 |
| `venia` | `venir` | 605 | accented spelling 9,799 vs 605 |
| `duracion` | `duración` | 605 | accented spelling 249,667 vs 605 |
| `maritimo` | `marítimo` | 604 | accented spelling 67,079 vs 604 |
| `cain` | `caín` | 604 | accented spelling 6,648 vs 604 |
| `barcelo` | `barceló` | 602 | accented spelling 5,168 vs 602 |
| `fantasias` | `fantasía` | 601 | accented spelling 7,256 vs 601 |
| `cañon` | `cañón` | 597 | accented spelling 39,968 vs 597 |
| `podrian` | `poder` | 596 | accented spelling 129,007 vs 596 |
| `politico` | `político` | 596 | accented spelling 287,485 vs 596 |
| `agustin` | `agustín` | 595 | accented spelling 11,452 vs 595 |
| `suspension` | `suspensión` | 595 | accented spelling 79,703 vs 595 |
| `mana` | `maná` | 594 | accented spelling 7,466 vs 594 |
| `recuperacion` | `recuperación` | 585 | accented spelling 174,576 vs 585 |
| `andres` | `andrés` | 584 | accented spelling 23,392 vs 584 |
| `huesped` | `huésped` | 582 | accented spelling 462,642 vs 582 |
| `termico` | `térmico` | 580 | accented spelling 71,142 vs 580 |
| `marques` | `marqués` | 579 | accented spelling 7,887 vs 579 |
| `sesion` | `sesión` | 575 | accented spelling 401,824 vs 575 |
| `causo` | `causar` | 571 | accented spelling 9,883 vs 571 |
| `alcala` | `alcalá` | 571 | accented spelling 11,398 vs 571 |
| `niger` | `níger` | 569 | accented spelling 5,912 vs 569 |
| `turisticas` | `turístico` | 568 | accented spelling 21,863 vs 568 |
| `situa` | `situar` | 568 | accented spelling 6,145 vs 568 |
| `declaracion` | `declaración` | 568 | accented spelling 295,793 vs 568 |
| `amon` | `amón` | 567 | accented spelling 5,942 vs 567 |
| `aleman` | `alemán` | 566 | accented spelling 226,784 vs 566 |
| `salon-comedor` | `salón-comedor` | 565 | accented spelling 26,849 vs 565 |
| `fluor` | `flúor` | 562 | accented spelling 4,988 vs 562 |
| `unico` | `único` | 562 | accented spelling 705,884 vs 562 |
| `recepcion` | `recepción` | 561 | accented spelling 208,309 vs 561 |
| `sotano` | `sótano` | 560 | accented spelling 26,077 vs 560 |
| `salvacion` | `salvación` | 558 | accented spelling 71,272 vs 558 |
| `judios` | `judío` | 554 | accented spelling 51,032 vs 554 |
| `belen` | `belén` | 554 | accented spelling 17,914 vs 554 |
| `nuñez` | `núñez` | 553 | accented spelling 4,398 vs 553 |
| `sonreir` | `sonreír` | 552 | accented spelling 24,108 vs 552 |
| `calida` | `cálido` | 551 | accented spelling 15,857 vs 551 |
| `cientifico` | `científico` | 542 | accented spelling 185,180 vs 542 |
| `expansion` | `expansión` | 542 | accented spelling 102,640 vs 542 |
| `comodas` | `cómodo` | 541 | accented spelling 22,716 vs 541 |
| `aragon` | `aragón` | 541 | accented spelling 11,672 vs 541 |
| `latinoamerica` | `latinoamérica` | 539 | accented spelling 48,348 vs 539 |
| `osmosis` | `ósmosis` | 538 | accented spelling 4,080 vs 538 |
| `excursion` | `excursión` | 530 | accented spelling 109,410 vs 530 |
| `gastronomia` | `gastronomía` | 530 | accented spelling 54,788 vs 530 |
| `deberian` | `deber` | 529 | accented spelling 53,815 vs 529 |
| `menton` | `mentón` | 528 | accented spelling 4,104 vs 528 |
| `libreria` | `librería` | 525 | accented spelling 25,100 vs 525 |
| `gijon` | `gijón` | 521 | accented spelling 9,004 vs 521 |
| `diametro` | `diámetro` | 521 | accented spelling 101,638 vs 521 |
| `sintoma` | `síntoma` | 518 | accented spelling 148,854 vs 518 |
| `tora` | `torá` | 515 | accented spelling 11,284 vs 515 |
| `belgica` | `bélgica` | 514 | accented spelling 50,330 vs 514 |
| `centrica` | `céntrico` | 514 | accented spelling 18,177 vs 514 |
| `tuberia` | `tubería` | 514 | accented spelling 64,488 vs 514 |
| `marti` | `martí` | 513 | accented spelling 6,996 vs 513 |
| `pergola` | `pérgola` | 512 | accented spelling 4,669 vs 512 |
| `noe` | `noé` | 511 | accented spelling 14,734 vs 511 |
| `alcazar` | `alcázar` | 510 | accented spelling 6,155 vs 510 |
| `muchisimas` | `mucho` | 508 | accented spelling 6,879 vs 508 |
| `hercules` | `hércules` | 508 | accented spelling 3,740 vs 508 |
| `dire` | `decir` | 506 | accented spelling 5,647 vs 506 |
| `benalmadena` | `benalmádena` | 506 | accented spelling 5,508 vs 506 |
| `localizacion` | `localización` | 506 | accented spelling 81,151 vs 506 |
| `inspiracion` | `inspiración` | 505 | accented spelling 69,220 vs 505 |
| `fundo` | `fundar` | 504 | accented spelling 12,303 vs 504 |
| `proteina` | `proteína` | 501 | accented spelling 88,567 vs 501 |
| `orientacion` | `orientación` | 501 | accented spelling 120,547 vs 501 |
| `acropolis` | `acrópolis` | 500 | accented spelling 4,904 vs 500 |
| `arabes` | `árabe` | 500 | accented spelling 13,850 vs 500 |
| `juda` | `judá` | 499 | accented spelling 66,918 vs 499 |
| `dominguez` | `domínguez` | 497 | accented spelling 3,668 vs 497 |
| `utopia` | `utopía` | 496 | accented spelling 5,408 vs 496 |
| `espectaculo` | `espectáculo` | 496 | accented spelling 88,671 vs 496 |
| `mojacar` | `mojácar` | 495 | accented spelling 3,754 vs 495 |
| `tripoli` | `trípoli` | 494 | accented spelling 3,394 vs 494 |
| `generacion` | `generación` | 492 | accented spelling 265,739 vs 492 |
| `manten` | `mantener` | 491 | accented spelling 17,793 vs 491 |
| `acne` | `acné` | 490 | accented spelling 28,078 vs 490 |
| `yucatan` | `yucatán` | 488 | accented spelling 9,346 vs 488 |
| `autobus` | `autobús` | 488 | accented spelling 364,028 vs 488 |
| `formacion` | `formación` | 486 | accented spelling 383,487 vs 486 |
| `japon` | `japón` | 482 | accented spelling 162,991 vs 482 |
| `precaucion` | `precaución` | 479 | accented spelling 47,015 vs 479 |
| `moises` | `moisés` | 479 | accented spelling 108,225 vs 479 |
| `mercancia` | `mercancía` | 477 | accented spelling 70,426 vs 477 |
| `bastion` | `bastión` | 477 | accented spelling 5,334 vs 477 |
| `mendez` | `méndez` | 475 | accented spelling 4,188 vs 475 |
| `evaluacion` | `evaluación` | 473 | accented spelling 281,196 vs 473 |
| `almuñecar` | `almuñécar` | 473 | accented spelling 2,560 vs 473 |
| `maiz` | `maíz` | 473 | accented spelling 51,845 vs 473 |
| `ebola` | `ébola` | 472 | accented spelling 10,200 vs 472 |
| `recibira` | `recibir` | 471 | accented spelling 37,748 vs 471 |
| `eleccion` | `elección` | 471 | accented spelling 246,668 vs 471 |
| `condicion` | `condición` | 470 | accented spelling 694,429 vs 470 |
| `teoria` | `teoría` | 469 | accented spelling 108,828 vs 469 |
| `periodico` | `periódico` | 468 | accented spelling 90,325 vs 468 |
| `jesus` | `jesús` | 468 | accented spelling 492,144 vs 468 |
| `bilingue` | `bilingüe` | 464 | accented spelling 17,080 vs 464 |
| `romantico` | `romántico` | 464 | accented spelling 68,660 vs 464 |
| `efectua` | `efectuar` | 462 | accented spelling 6,484 vs 462 |
| `varian` | `variar` | 462 | accented spelling 22,685 vs 462 |
| `contemporaneo` | `contemporáneo` | 458 | accented spelling 87,072 vs 458 |
| `hara` | `hacer` | 458 | accented spelling 86,205 vs 458 |
| `filosofia` | `filosofía` | 457 | accented spelling 77,812 vs 457 |
| `jerusalen` | `jerusalén` | 457 | accented spelling 105,090 vs 457 |
| `romantica` | `romántico` | 457 | accented spelling 13,850 vs 457 |
| `exito` | `éxito` | 457 | accented spelling 428,909 vs 457 |
| `daria` | `dar` | 456 | accented spelling 8,023 vs 456 |
| `microscopia` | `microscopía` | 456 | accented spelling 3,046 vs 456 |
| `comision` | `comisión` | 456 | accented spelling 292,477 vs 456 |
| `parr` | `párr` | 455 | accented spelling 2,440 vs 455 |
| `volo` | `volar` | 455 | accented spelling 2,499 vs 455 |
| `brujula` | `brújula` | 454 | accented spelling 9,089 vs 454 |
| `preparacion` | `preparación` | 452 | accented spelling 167,654 vs 452 |
| `nacion` | `nación` | 451 | accented spelling 162,513 vs 451 |
| `poesia` | `poesía` | 450 | accented spelling 24,717 vs 450 |
| `marquez` | `márquez` | 450 | accented spelling 7,604 vs 450 |
| `rapido` | `rápido` | 450 | accented spelling 1,002,554 vs 450 |
| `catalan` | `catalán` | 447 | accented spelling 34,288 vs 447 |
| `artesania` | `artesanía` | 446 | accented spelling 39,249 vs 446 |
| `bavaro` | `bávaro` | 446 | accented spelling 4,656 vs 446 |
| `introduccion` | `introducción` | 445 | accented spelling 147,652 vs 445 |
| `volcan` | `volcán` | 444 | accented spelling 33,872 vs 444 |
| `cacer` | `cácer` | 442 | accented spelling 3,685 vs 442 |
| `comite` | `comité` | 441 | accented spelling 182,783 vs 441 |
| `economica` | `económico` | 441 | accented spelling 94,926 vs 441 |
| `loteria` | `lotería` | 440 | accented spelling 33,851 vs 440 |
| `mahon` | `mahón` | 439 | accented spelling 5,530 vs 439 |
| `pantalon` | `pantalón` | 439 | accented spelling 69,192 vs 439 |
| `jaen` | `jaén` | 438 | accented spelling 8,900 vs 438 |
| `basquetbol` | `básquetbol` | 438 | accented spelling 2,398 vs 438 |
| `estetica` | `estético` | 434 | accented spelling 27,257 vs 434 |
| `talon` | `talón` | 433 | accented spelling 21,797 vs 433 |
| `fotografo` | `fotógrafo` | 432 | accented spelling 47,672 vs 432 |
| `poblacion` | `población` | 432 | accented spelling 365,017 vs 432 |
| `armonia` | `armonía` | 430 | accented spelling 49,715 vs 430 |
| `sabeis` | `saber` | 428 | accented spelling 11,553 vs 428 |
| `exposicion` | `exposición` | 426 | accented spelling 256,347 vs 426 |
| `tendran` | `tener` | 425 | accented spelling 61,218 vs 425 |
| `valentia` | `valentía` | 422 | accented spelling 14,051 vs 422 |
| `autovia` | `autovía` | 419 | accented spelling 6,970 vs 419 |
| `segun` | `según` | 419 | accented spelling 1,028,918 vs 419 |
| `frigorifico` | `frigorífico` | 417 | accented spelling 32,357 vs 417 |
| `pondran` | `poner` | 416 | accented spelling 4,133 vs 416 |
| `samana` | `samaná` | 416 | accented spelling 2,612 vs 416 |
| `diversion` | `diversión` | 413 | accented spelling 90,291 vs 413 |
| `argan` | `argán` | 413 | accented spelling 3,711 vs 413 |
| `fantastica` | `fantástico` | 412 | accented spelling 40,139 vs 412 |
| `basicamente` | `básicamente` | 411 | accented spelling 47,297 vs 411 |
| `sillon` | `sillón` | 410 | accented spelling 19,606 vs 410 |
| `respondio` | `responder` | 409 | accented spelling 49,198 vs 409 |
| `ambar` | `ámbar` | 408 | accented spelling 8,006 vs 408 |
| `noemi` | `noemí` | 408 | accented spelling 3,524 vs 408 |
| `conduccion` | `conducción` | 406 | accented spelling 76,059 vs 406 |
| `gondola` | `góndola` | 402 | accented spelling 3,706 vs 402 |
| `reproduccion` | `reproducción` | 402 | accented spelling 142,565 vs 402 |
| `versiculo` | `versículo` | 401 | accented spelling 25,513 vs 401 |
| `millon` | `millón` | 400 | accented spelling 446,210 vs 400 |
| `peticion` | `petición` | 398 | accented spelling 170,350 vs 398 |
| `galata` | `gálata` | 396 | accented spelling 2,397 vs 396 |
| `celula` | `célula` | 394 | accented spelling 136,886 vs 394 |
| `asuncion` | `asunción` | 394 | accented spelling 20,634 vs 394 |
| `decidi` | `decidir` | 393 | accented spelling 15,254 vs 393 |
| `navegacion` | `navegación` | 393 | accented spelling 211,288 vs 393 |
| `parametro#railway` | `parámetro` | 393 | accented spelling 88,663 vs 393 |
| `graficas` | `gráfico` | 392 | accented spelling 13,733 vs 392 |
| `regalia` | `regalía` | 392 | accented spelling 5,745 vs 392 |
| `iria` | `ir` | 391 | accented spelling 2,893 vs 391 |
| `teniamos` | `tener` | 390 | accented spelling 18,108 vs 390 |
| `quimico` | `químico` | 388 | accented spelling 96,219 vs 388 |
| `probe` | `probar` | 386 | accented spelling 2,201 vs 386 |
| `encontre` | `encontrar` | 386 | accented spelling 15,485 vs 386 |
| `podre` | `poder` | 386 | accented spelling 4,545 vs 386 |
| `soller` | `sóller` | 386 | accented spelling 3,804 vs 386 |
| `rapida` | `rápido` | 385 | accented spelling 188,115 vs 385 |
| `alava` | `álava` | 384 | accented spelling 4,788 vs 384 |
| `tension` | `tensión` | 384 | accented spelling 120,020 vs 384 |
| `belarus` | `belarús` | 384 | accented spelling 3,760 vs 384 |
| `reir#actual` | `reír` | 383 | accented spelling 19,363 vs 383 |
| `hamster` | `hámster` | 382 | accented spelling 2,532 vs 382 |
| `discipulo` | `discípulo` | 381 | accented spelling 59,084 vs 381 |
| `intencion` | `intención` | 380 | accented spelling 132,332 vs 380 |
| `ambito` | `ámbito` | 380 | accented spelling 177,823 vs 380 |
| `tipico` | `típico` | 380 | accented spelling 100,031 vs 380 |
| `calido` | `cálido` | 379 | accented spelling 80,649 vs 379 |
| `medula` | `médula` | 378 | accented spelling 4,222 vs 378 |
| `unicas` | `único` | 378 | accented spelling 32,316 vs 378 |
| `menus` | `menú` | 378 | accented spelling 17,372 vs 378 |
| `digito` | `dígito` | 377 | accented spelling 15,272 vs 377 |
| `perdon` | `perdón` | 375 | accented spelling 39,010 vs 375 |
| `sudamerica` | `sudamérica` | 374 | accented spelling 17,761 vs 374 |
| `xenon` | `xenón` | 374 | accented spelling 1,948 vs 374 |
| `lazaro` | `lázaro` | 373 | accented spelling 11,284 vs 373 |
| `lider` | `líder` | 373 | accented spelling 305,411 vs 373 |
| `simeon` | `simeón` | 372 | accented spelling 5,302 vs 372 |
| `pense` | `pensar` | 371 | accented spelling 19,680 vs 371 |
| `economicas` | `económico` | 369 | accented spelling 42,262 vs 369 |
| `lujan` | `luján` | 367 | accented spelling 1,964 vs 367 |
| `carcel` | `cárcel` | 366 | accented spelling 51,678 vs 366 |
| `vivi` | `vivir` | 365 | accented spelling 2,251 vs 365 |
| `colibri` | `colibrí` | 363 | accented spelling 2,445 vs 363 |
| `tradicion` | `tradición` | 362 | accented spelling 138,297 vs 362 |
| `musee` | `musée` | 362 | accented spelling 3,180 vs 362 |
| `celiaco` | `celíaco` | 362 | accented spelling 2,939 vs 362 |
| `iman` | `imán` | 361 | accented spelling 27,031 vs 361 |
| `castellon` | `castellón` | 361 | accented spelling 10,488 vs 361 |
| `deberan` | `deber` | 360 | accented spelling 47,672 vs 360 |
| `ramadan` | `ramadán` | 359 | accented spelling 4,360 vs 359 |
| `romani` | `romaní` | 358 | accented spelling 1,841 vs 358 |
| `regimen` | `régimen` | 358 | accented spelling 116,547 vs 358 |
| `violin` | `violín` | 356 | accented spelling 9,887 vs 356 |
| `pekin` | `pekín` | 356 | accented spelling 29,624 vs 356 |
| `invasion` | `invasión` | 356 | accented spelling 28,518 vs 356 |
| `bogota` | `bogotá` | 355 | accented spelling 81,998 vs 355 |
| `demoniaco` | `demoníaco` | 354 | accented spelling 2,995 vs 354 |
| `vertigo` | `vértigo` | 354 | accented spelling 5,603 vs 354 |
| `hindu` | `hindú` | 352 | accented spelling 9,373 vs 352 |
| `sabiduria` | `sabiduría` | 352 | accented spelling 81,708 vs 352 |
| `permitira` | `permitir` | 352 | accented spelling 64,859 vs 352 |
| `levanto` | `levantar` | 351 | accented spelling 8,839 vs 351 |
| `acido` | `ácido` | 351 | accented spelling 116,485 vs 351 |
| `boletin` | `boletín` | 351 | accented spelling 83,346 vs 351 |
| `manifesto` | `manifestar` | 349 | accented spelling 7,444 vs 349 |
| `adan` | `adán` | 349 | accented spelling 24,789 vs 349 |
| `badminton` | `bádminton` | 348 | accented spelling 2,654 vs 348 |
| `tropico` | `trópico` | 346 | accented spelling 3,798 vs 346 |
| `increiblemente` | `increíblemente` | 346 | accented spelling 33,550 vs 346 |
| `nestle` | `nestlé` | 346 | accented spelling 7,618 vs 346 |
| `fotografias` | `fotografía` | 345 | accented spelling 60,971 vs 345 |
| `nestor` | `néstor` | 345 | accented spelling 1,750 vs 345 |
| `aerolineas` | `aerolínea` | 342 | accented spelling 107,447 vs 342 |
| `indices` | `índice` | 340 | accented spelling 18,427 vs 340 |
| `lamparas` | `lámpara` | 340 | accented spelling 22,688 vs 340 |
| `quizas` | `quizás` | 339 | accented spelling 131,943 vs 339 |
| `lluis` | `lluís` | 338 | accented spelling 2,876 vs 338 |
| `hebron` | `hebrón` | 337 | accented spelling 6,340 vs 337 |
| `actualizacion` | `actualización` | 337 | accented spelling 281,039 vs 337 |
| `uzbekistan` | `uzbekistán` | 337 | accented spelling 7,132 vs 337 |
| `identificacion` | `identificación` | 336 | accented spelling 187,524 vs 336 |
| `accion` | `acción` | 335 | accented spelling 662,910 vs 335 |
| `valoracion` | `valoración` | 335 | accented spelling 95,580 vs 335 |
| `dara` | `dar` | 334 | accented spelling 54,046 vs 334 |
| `trebol` | `trébol` | 333 | accented spelling 4,194 vs 333 |
| `climax` | `clímax` | 333 | accented spelling 3,368 vs 333 |
| `lei` | `leer` | 333 | accented spelling 4,621 vs 333 |
| `grabacion` | `grabación` | 332 | accented spelling 94,267 vs 332 |
| `grua` | `grúa` | 331 | accented spelling 25,872 vs 331 |
| `pacifica` | `pacífico` | 330 | accented spelling 9,337 vs 330 |
| `guzman` | `guzmán` | 330 | accented spelling 8,195 vs 330 |
| `publicacion` | `publicación` | 330 | accented spelling 230,069 vs 330 |
| `devolucion` | `devolución` | 328 | accented spelling 84,394 vs 328 |
| `decia` | `decir` | 327 | accented spelling 31,742 vs 327 |
| `sebastien` | `sébastien` | 326 | accented spelling 2,178 vs 326 |
| `meson` | `mesón` | 326 | accented spelling 3,268 vs 326 |
| `tribulacion` | `tribulación` | 325 | accented spelling 12,202 vs 325 |
| `profecia` | `profecía` | 325 | accented spelling 23,283 vs 325 |
| `clasica` | `clásico` | 324 | accented spelling 28,931 vs 324 |
| `crater` | `cráter` | 321 | accented spelling 9,042 vs 321 |
| `areas` | `área` | 320 | accented spelling 182,352 vs 320 |
| `panaderia` | `panadería` | 318 | accented spelling 21,479 vs 318 |
| `acontecio` | `acontecer` | 317 | accented spelling 7,830 vs 317 |
| `basica` | `básico` | 316 | accented spelling 63,143 vs 316 |
| `baterias` | `batería` | 316 | accented spelling 42,835 vs 316 |
| `simultaneamente` | `simultáneamente` | 313 | accented spelling 35,851 vs 313 |
| `historica` | `histórico` | 309 | accented spelling 37,606 vs 309 |
| `subterraneo` | `subterráneo` | 308 | accented spelling 36,930 vs 308 |
| `ibamos` | `ir` | 307 | accented spelling 4,130 vs 307 |
| `tunez` | `túnez` | 307 | accented spelling 21,891 vs 307 |
| `difamacion` | `difamación` | 306 | accented spelling 5,616 vs 306 |
| `velez` | `vélez` | 306 | accented spelling 2,832 vs 306 |
| `moscu` | `moscú` | 305 | accented spelling 75,577 vs 305 |
| `peliculas` | `película` | 305 | accented spelling 98,386 vs 305 |
| `lapiz` | `lápiz` | 304 | accented spelling 39,799 vs 304 |
| `ecologico` | `ecológico` | 304 | accented spelling 70,437 vs 304 |
| `comodamente` | `cómodamente` | 303 | accented spelling 35,035 vs 303 |
| `sensacion` | `sensación` | 303 | accented spelling 161,644 vs 303 |
| `conversacion` | `conversación` | 301 | accented spelling 108,423 vs 301 |
| `comenzo` | `comenzar` | 301 | accented spelling 99,483 vs 301 |
| `delfin` | `delfín` | 300 | accented spelling 14,446 vs 300 |
| `cito` | `citar` | 299 | accented spelling 2,984 vs 299 |
| `bambu` | `bambú` | 299 | accented spelling 20,877 vs 299 |
| `acuatico` | `acuático` | 298 | accented spelling 51,720 vs 298 |
| `olimpico` | `olímpico` | 298 | accented spelling 22,798 vs 298 |
| `elaboracion` | `elaboración` | 297 | accented spelling 93,320 vs 297 |
| `habria` | `haber` | 297 | accented spelling 46,407 vs 297 |
| `malecon` | `malecón` | 297 | accented spelling 5,963 vs 297 |
| `turquia` | `turquía` | 296 | accented spelling 77,610 vs 296 |
| `cuestion` | `cuestión` | 296 | accented spelling 247,925 vs 296 |
| `conclusion` | `conclusión` | 295 | accented spelling 99,129 vs 295 |
| `podriamos` | `poder` | 295 | accented spelling 28,501 vs 295 |
| `simpatia` | `simpatía` | 292 | accented spelling 9,390 vs 292 |
| `piton` | `pitón` | 292 | accented spelling 1,780 vs 292 |
| `piston` | `pistón` | 291 | accented spelling 16,667 vs 291 |
| `aerobic` | `aeróbic` | 291 | accented spelling 1,648 vs 291 |
| `dracula` | `drácula` | 290 | accented spelling 2,502 vs 290 |
| `referendum` | `referéndum` | 290 | accented spelling 13,398 vs 290 |
| `vazquez` | `vázquez` | 289 | accented spelling 5,186 vs 289 |
| `porton` | `portón` | 289 | accented spelling 5,885 vs 289 |
| `psicologia` | `psicología` | 288 | accented spelling 38,217 vs 288 |
| `comunion` | `comunión` | 288 | accented spelling 44,274 vs 288 |
| `debil` | `débil` | 287 | accented spelling 61,545 vs 287 |
| `representacion` | `representación` | 285 | accented spelling 109,684 vs 285 |
| `apostol` | `apóstol` | 284 | accented spelling 45,687 vs 284 |
| `melon` | `melón` | 284 | accented spelling 5,778 vs 284 |
| `perimetro` | `perímetro` | 284 | accented spelling 12,855 vs 284 |
| `indigenas` | `indígena` | 283 | accented spelling 42,991 vs 283 |
| `humedo` | `húmedo` | 282 | accented spelling 57,194 vs 282 |
| `mecanico` | `mecánico` | 282 | accented spelling 97,217 vs 282 |
| `extraible` | `extraíble` | 279 | accented spelling 15,581 vs 279 |
| `verguenza` | `vergüenza` | 278 | accented spelling 21,913 vs 278 |
| `certificacion` | `certificación` | 278 | accented spelling 132,757 vs 278 |
| `utilizacion` | `utilización` | 278 | accented spelling 160,971 vs 278 |
| `merito` | `mérito` | 276 | accented spelling 17,338 vs 276 |
| `botanico` | `botánico` | 276 | accented spelling 21,828 vs 276 |
| `vitroceramica` | `vitrocerámica` | 276 | accented spelling 9,816 vs 276 |
| `explosion` | `explosión` | 275 | accented spelling 43,877 vs 275 |
| `espirita` | `espírita` | 275 | accented spelling 4,726 vs 275 |
| `nicaraguense` | `nicaragüense` | 275 | accented spelling 7,425 vs 275 |
| `contemporanea` | `contemporáneo` | 274 | accented spelling 17,058 vs 274 |
| `optico` | `óptico` | 273 | accented spelling 61,474 vs 273 |
| `estare` | `estar` | 273 | accented spelling 9,485 vs 273 |
| `celebracion` | `celebración` | 271 | accented spelling 100,820 vs 271 |
| `reduccion` | `reducción` | 270 | accented spelling 194,634 vs 270 |
| `conservacion` | `conservación` | 269 | accented spelling 106,080 vs 269 |
| `ilustracion` | `ilustración` | 269 | accented spelling 80,746 vs 269 |
| `planto` | `plantar` | 269 | accented spelling 1,756 vs 269 |
| `estais` | `estar` | 268 | accented spelling 12,116 vs 268 |
| `atlantica` | `atlántico` | 268 | accented spelling 3,184 vs 268 |
| `supervision` | `supervisión` | 268 | accented spelling 76,916 vs 268 |
| `recibio` | `recibir` | 266 | accented spelling 57,640 vs 266 |
| `prohiben` | `prohibir` | 266 | accented spelling 2,751 vs 266 |
| `humeda` | `húmedo` | 264 | accented spelling 8,903 vs 264 |
| `paramo` | `páramo` | 264 | accented spelling 3,982 vs 264 |
| `basicas` | `básico` | 262 | accented spelling 46,944 vs 262 |
| `tenes` | `tener` | 261 | accented spelling 2,638 vs 261 |
| `quorum` | `quórum` | 261 | accented spelling 4,474 vs 261 |
| `confia` | `confiar` | 260 | accented spelling 10,175 vs 260 |
| `comercializacion` | `comercialización` | 260 | accented spelling 63,117 vs 260 |
| `irun` | `irún` | 260 | accented spelling 1,598 vs 260 |
| `foton` | `fotón` | 260 | accented spelling 4,293 vs 260 |
| `leela` | `leer` | 260 | accented spelling 15,271 vs 260 |
| `satisfaccion` | `satisfacción` | 259 | accented spelling 102,379 vs 259 |
| `lesion` | `lesión` | 259 | accented spelling 132,422 vs 259 |
| `nutricion` | `nutrición` | 259 | accented spelling 74,224 vs 259 |
| `parecia` | `parecer` | 258 | accented spelling 32,684 vs 258 |
| `sandia` | `sandía` | 258 | accented spelling 4,959 vs 258 |
| `artistico` | `artístico` | 258 | accented spelling 77,322 vs 258 |
| `velazquez` | `velázquez` | 257 | accented spelling 4,634 vs 257 |
| `talisman` | `talismán` | 257 | accented spelling 1,821 vs 257 |
| `colaboracion` | `colaboración` | 257 | accented spelling 208,073 vs 257 |
| `poligono` | `polígono` | 257 | accented spelling 7,658 vs 257 |
| `recreacion` | `recreación` | 257 | accented spelling 20,601 vs 257 |
| `sindrome` | `síndrome` | 256 | accented spelling 64,896 vs 256 |
| `itza` | `itzá` | 256 | accented spelling 1,938 vs 256 |
| `algebra` | `álgebra` | 256 | accented spelling 2,800 vs 256 |
| `registrese` | `registrarse` | 255 | accented spelling 29,572 vs 255 |
| `nectar` | `néctar` | 254 | accented spelling 4,365 vs 254 |
| `turisticos` | `turístico` | 253 | accented spelling 33,998 vs 253 |
| `alhaurin` | `alhaurín` | 253 | accented spelling 1,676 vs 253 |
| `choco` | `chocar` | 252 | accented spelling 2,014 vs 252 |
| `hectarea` | `hectárea` | 252 | accented spelling 26,364 vs 252 |
| `jardineria` | `jardinería` | 251 | accented spelling 17,738 vs 251 |
| `ventilacion` | `ventilación` | 251 | accented spelling 47,392 vs 251 |
| `podran` | `poder` | 250 | accented spelling 121,198 vs 250 |
| `obtendra` | `obtener` | 250 | accented spelling 28,253 vs 250 |
| `setubal` | `setúbal` | 250 | accented spelling 1,286 vs 250 |
| `membresia` | `membresía` | 249 | accented spelling 30,283 vs 249 |
| `sere` | `ser` | 249 | accented spelling 8,874 vs 249 |
| `instruccion` | `instrucción` | 248 | accented spelling 511,549 vs 248 |
| `magico` | `mágico` | 248 | accented spelling 64,239 vs 248 |
| `inclusion` | `inclusión` | 248 | accented spelling 70,246 vs 248 |
| `vasquez` | `vásquez` | 248 | accented spelling 2,486 vs 248 |
| `peñiscola` | `peñíscola` | 247 | accented spelling 2,004 vs 247 |
| `biblico` | `bíblico` | 247 | accented spelling 23,419 vs 247 |
| `josue` | `josué` | 246 | accented spelling 26,481 vs 246 |
| `miercoles` | `miércoles` | 246 | accented spelling 156,373 vs 246 |
| `innovacion` | `innovación` | 245 | accented spelling 215,398 vs 245 |
| `cercania` | `cercanía` | 245 | accented spelling 24,714 vs 245 |
| `erotico` | `erótico` | 245 | accented spelling 15,824 vs 245 |
| `poliza` | `póliza` | 244 | accented spelling 34,152 vs 244 |
| `saenz` | `sáenz` | 244 | accented spelling 1,386 vs 244 |
| `reservacion` | `reservación` | 242 | accented spelling 43,520 vs 242 |
| `guie` | `guiar` | 242 | accented spelling 2,435 vs 242 |
| `baden-wurttemberg` | `baden-württemberg` | 241 | accented spelling 1,650 vs 241 |
| `cesareo` | `cesárea` | 241 | accented spelling 3,170 vs 241 |
| `podian` | `poder` | 241 | accented spelling 30,271 vs 241 |
| `mineria` | `minería` | 241 | accented spelling 46,809 vs 241 |
| `coccion` | `cocción` | 241 | accented spelling 27,749 vs 241 |
| `agata` | `ágata` | 240 | accented spelling 2,497 vs 240 |
| `medano` | `médano` | 240 | accented spelling 1,357 vs 240 |
| `benitez` | `benítez` | 239 | accented spelling 2,132 vs 239 |
| `aerea` | `aéreo` | 239 | accented spelling 26,255 vs 239 |
| `pidio` | `pedir` | 239 | accented spelling 28,451 vs 239 |
| `ciudadania` | `ciudadanía` | 239 | accented spelling 48,423 vs 239 |
| `stephane` | `stéphane` | 239 | accented spelling 1,542 vs 239 |
| `satanas` | `satanás` | 239 | accented spelling 37,881 vs 239 |
| `cancelacion` | `cancelación` | 238 | accented spelling 91,175 vs 238 |
| `catolicos` | `católico` | 237 | accented spelling 15,280 vs 237 |
| `boyaca` | `boyacá` | 237 | accented spelling 1,856 vs 237 |
| `ascension` | `ascensión` | 237 | accented spelling 13,340 vs 237 |
| `sudafrica` | `sudáfrica` | 237 | accented spelling 53,516 vs 237 |
| `serigrafia` | `serigrafía` | 237 | accented spelling 6,092 vs 237 |
| `confeso` | `confesar` | 236 | accented spelling 2,478 vs 236 |
| `operacion` | `operación` | 236 | accented spelling 365,297 vs 236 |
| `tendria` | `tener` | 236 | accented spelling 23,563 vs 236 |
| `categorias` | `categoría` | 236 | accented spelling 110,393 vs 236 |
| `hungria` | `hungría` | 234 | accented spelling 33,642 vs 234 |
| `animacion` | `animación` | 234 | accented spelling 62,008 vs 234 |
| `metalicas` | `metálico` | 234 | accented spelling 8,743 vs 234 |
| `acustico` | `acústico` | 234 | accented spelling 29,782 vs 234 |
| `inmigracion` | `inmigración` | 234 | accented spelling 72,994 vs 234 |
| `periodicamente` | `periódicamente` | 233 | accented spelling 65,029 vs 233 |
| `rehabilitacion` | `rehabilitación` | 233 | accented spelling 45,895 vs 233 |
| `michoacan` | `michoacán` | 233 | accented spelling 5,186 vs 233 |
| `atencion` | `atención` | 232 | accented spelling 698,751 vs 232 |
| `acrilico` | `acrílico` | 232 | accented spelling 36,190 vs 232 |
| `combine` | `combinar` | 232 | accented spelling 1,405 vs 232 |
| `adriatico` | `adriático` | 232 | accented spelling 4,924 vs 232 |
| `seul` | `seúl` | 232 | accented spelling 26,596 vs 232 |
| `jonatan` | `jonatán` | 232 | accented spelling 8,626 vs 232 |
| `aparecera` | `aparecer` | 231 | accented spelling 22,816 vs 231 |
| `anfitrion` | `anfitrión` | 231 | accented spelling 78,154 vs 231 |
| `higado` | `hígado` | 231 | accented spelling 66,556 vs 231 |
| `tunica` | `túnica` | 231 | accented spelling 9,030 vs 231 |
| `mormon` | `mormón` | 230 | accented spelling 9,189 vs 230 |
| `supresion` | `supresión` | 229 | accented spelling 26,153 vs 229 |
| `caserio` | `caserío` | 229 | accented spelling 3,990 vs 229 |
| `neumatico` | `neumático` | 228 | accented spelling 92,895 vs 228 |
| `incognito` | `incógnito` | 227 | accented spelling 3,087 vs 227 |
| `magnifica` | `magnífico` | 227 | accented spelling 25,921 vs 227 |
| `encantaria` | `encantar` | 227 | accented spelling 7,921 vs 227 |
| `mediterranea` | `mediterráneo` | 226 | accented spelling 21,746 vs 226 |
| `melodia` | `melodía` | 226 | accented spelling 17,075 vs 226 |
| `derribo` | `derribar` | 226 | accented spelling 1,686 vs 226 |
| `juridico` | `jurídico` | 225 | accented spelling 79,502 vs 225 |
| `jandia` | `jandía` | 225 | accented spelling 1,284 vs 225 |
| `lenceria` | `lencería` | 224 | accented spelling 8,071 vs 224 |
| `fijacion` | `fijación` | 224 | accented spelling 50,173 vs 224 |
| `helicoptero` | `helicóptero` | 223 | accented spelling 28,372 vs 223 |
| `documentacion` | `documentación` | 223 | accented spelling 106,608 vs 223 |
| `tecnologico` | `tecnológico` | 223 | accented spelling 113,644 vs 223 |
| `tartan` | `tartán` | 222 | accented spelling 1,271 vs 222 |
| `azucar` | `azúcar` | 222 | accented spelling 145,671 vs 222 |
| `ibañez` | `ibáñez` | 222 | accented spelling 1,854 vs 222 |
| `detras` | `detrás` | 221 | accented spelling 168,884 vs 221 |
| `matematica` | `matemática` | 221 | accented spelling 14,903 vs 221 |
| `condon` | `condón` | 221 | accented spelling 6,644 vs 221 |
| `compensacion` | `compensación` | 221 | accented spelling 73,689 vs 221 |
| `unica` | `único` | 221 | accented spelling 177,957 vs 221 |
| `microfono` | `micrófono` | 221 | accented spelling 45,804 vs 221 |
| `policiaco` | `policíaco` | 220 | accented spelling 2,086 vs 220 |
| `olvido` | `olvidar` | 220 | accented spelling 5,100 vs 220 |
| `isaias` | `isaías` | 220 | accented spelling 22,176 vs 220 |
| `restauracion` | `restauración` | 220 | accented spelling 66,027 vs 220 |
| `confirmacion` | `confirmación` | 220 | accented spelling 99,762 vs 220 |
| `imaginacion` | `imaginación` | 219 | accented spelling 44,116 vs 219 |
| `concentrate` | `concentrar` | 219 | accented spelling 1,454 vs 219 |
| `modificacion` | `modificación` | 219 | accented spelling 161,361 vs 219 |
| `varia` | `variar` | 219 | accented spelling 22,210 vs 219 |
| `sali` | `salir` | 219 | accented spelling 4,211 vs 219 |
| `cortesia` | `cortesía` | 219 | accented spelling 34,988 vs 219 |
| `jabon` | `jabón` | 219 | accented spelling 46,282 vs 219 |
| `divan` | `diván` | 219 | accented spelling 1,254 vs 219 |
| `aviles` | `avilés` | 218 | accented spelling 2,790 vs 218 |
| `fisicamente` | `físicamente` | 218 | accented spelling 26,286 vs 218 |
| `sabian` | `saber` | 218 | accented spelling 9,644 vs 218 |
| `multiples` | `múltiple` | 217 | accented spelling 117,679 vs 217 |
| `definicion` | `definición` | 217 | accented spelling 145,417 vs 217 |
| `riñon` | `riñón` | 217 | accented spelling 34,949 vs 217 |
| `piramide` | `pirámide` | 217 | accented spelling 19,869 vs 217 |
| `conoci` | `conocer` | 217 | accented spelling 8,991 vs 217 |
| `beltran` | `beltrán` | 217 | accented spelling 2,052 vs 217 |
| `geminis` | `géminis` | 217 | accented spelling 2,462 vs 217 |
| `chalten` | `chaltén` | 216 | accented spelling 1,540 vs 216 |
| `amenazo` | `amenazar` | 216 | accented spelling 2,493 vs 216 |
| `reflexion` | `reflexión` | 216 | accented spelling 61,869 vs 216 |
| `metalico` | `metálico` | 215 | accented spelling 52,557 vs 215 |
| `explicacion` | `explicación` | 215 | accented spelling 55,319 vs 215 |
| `sepulveda` | `sepúlveda` | 215 | accented spelling 1,154 vs 215 |
| `constitucion` | `constitución` | 214 | accented spelling 71,553 vs 214 |
| `bhutan` | `bhután` | 214 | accented spelling 1,150 vs 214 |
| `bartolome` | `bartolomé` | 213 | accented spelling 5,556 vs 213 |
| `jamon` | `jamón` | 213 | accented spelling 22,166 vs 213 |
| `prestamo` | `préstamo` | 212 | accented spelling 96,765 vs 212 |
| `toxico` | `tóxico` | 211 | accented spelling 30,802 vs 211 |
| `demas` | `demás` | 211 | accented spelling 339,455 vs 211 |
| `liberacion` | `liberación` | 210 | accented spelling 76,643 vs 210 |
| `atlantida` | `atlántida` | 210 | accented spelling 3,441 vs 210 |
| `magica` | `mágico` | 210 | accented spelling 13,321 vs 210 |
| `sabra` | `saber` | 210 | accented spelling 6,980 vs 210 |
| `capacitacion` | `capacitación` | 210 | accented spelling 108,996 vs 210 |
| `chillan` | `chillán` | 209 | accented spelling 1,142 vs 209 |
| `escaner` | `escáner` | 209 | accented spelling 36,012 vs 209 |
| `decidio` | `decidir` | 209 | accented spelling 35,073 vs 209 |
| `infusion` | `infusión` | 209 | accented spelling 16,818 vs 209 |
| `memorandum` | `memorándum` | 209 | accented spelling 3,977 vs 209 |
| `toracico` | `torácico` | 209 | accented spelling 5,172 vs 209 |
| `vivio` | `vivir` | 208 | accented spelling 16,223 vs 208 |
| `decimo` | `décimo` | 208 | accented spelling 23,047 vs 208 |
| `refrigeracion` | `refrigeración` | 207 | accented spelling 51,405 vs 207 |
| `proton` | `protón` | 207 | accented spelling 4,107 vs 207 |
| `multilingue` | `multilingüe` | 207 | accented spelling 18,363 vs 207 |
| `chiita` | `chiíta` | 207 | accented spelling 1,608 vs 207 |
| `mejia` | `mejía` | 207 | accented spelling 2,758 vs 207 |
| `clinico` | `clínico` | 206 | accented spelling 70,245 vs 206 |
| `mediodia` | `mediodía` | 206 | accented spelling 29,378 vs 206 |
| `consul` | `cónsul` | 206 | accented spelling 3,493 vs 206 |
| `planificacion` | `planificación` | 205 | accented spelling 123,347 vs 205 |
| `republica` | `república` | 205 | accented spelling 135,368 vs 205 |
| `util` | `útil` | 205 | accented spelling 307,922 vs 205 |
| `recaudo` | `recaudar` | 205 | accented spelling 1,460 vs 205 |
| `orgia` | `orgía` | 204 | accented spelling 3,649 vs 204 |
| `golan` | `golán` | 204 | accented spelling 1,228 vs 204 |
| `laser` | `láser` | 203 | accented spelling 119,211 vs 203 |
| `interpretacion` | `interpretación` | 203 | accented spelling 90,607 vs 203 |
| `resurreccion` | `resurrección` | 203 | accented spelling 41,028 vs 203 |
| `autorizacion` | `autorización` | 203 | accented spelling 102,346 vs 203 |
| `pave` | `pavé` | 202 | accented spelling 4,434 vs 202 |
| `artistica` | `artístico` | 202 | accented spelling 20,672 vs 202 |
| `hospederia` | `hospedería` | 201 | accented spelling 1,697 vs 201 |
| `balon` | `balón` | 201 | accented spelling 34,689 vs 201 |
| `civico` | `cívico` | 201 | accented spelling 11,611 vs 201 |
| `deberias` | `deber` | 201 | accented spelling 25,554 vs 201 |
| `instantaneamente` | `instantáneamente` | 201 | accented spelling 15,652 vs 201 |
| `tunel` | `túnel` | 201 | accented spelling 42,291 vs 201 |
| `inspeccion` | `inspección` | 201 | accented spelling 87,297 vs 201 |
| `proteccion` | `protección` | 201 | accented spelling 691,732 vs 201 |
| `alli` | `allí` | 200 | accented spelling 448,249 vs 200 |
| `energetico` | `energético` | 200 | accented spelling 97,036 vs 200 |
| `pedi` | `pedir` | 200 | accented spelling 4,910 vs 200 |
| `libano` | `líbano` | 199 | accented spelling 25,138 vs 199 |
| `automaticas` | `automático` | 199 | accented spelling 12,652 vs 199 |
| `homilia` | `homilía` | 199 | accented spelling 5,862 vs 199 |
| `aji` | `ají` | 198 | accented spelling 2,741 vs 198 |
| `decada` | `década` | 198 | accented spelling 166,119 vs 198 |
| `escribio` | `escribir` | 198 | accented spelling 44,630 vs 198 |
| `integramente` | `íntegramente` | 198 | accented spelling 11,340 vs 198 |
| `freir` | `freír` | 198 | accented spelling 13,678 vs 198 |
| `inscripcion` | `inscripción` | 198 | accented spelling 90,954 vs 198 |
| `tarzan` | `tarzán` | 198 | accented spelling 1,156 vs 198 |
| `nahuatl` | `náhuatl` | 198 | accented spelling 1,242 vs 198 |
| `jurgen` | `jürgen` | 197 | accented spelling 1,283 vs 197 |
| `suscribase` | `suscribirse` | 196 | accented spelling 19,408 vs 196 |
| `lexicon` | `lexicón` | 196 | accented spelling 1,420 vs 196 |
| `señorio` | `señorío` | 196 | accented spelling 3,707 vs 196 |
| `ejecucion` | `ejecución` | 196 | accented spelling 163,443 vs 196 |
| `rayon` | `rayón` | 195 | accented spelling 2,860 vs 195 |
| `alejandria` | `alejandría` | 195 | accented spelling 10,124 vs 195 |
| `biografia` | `biografía` | 195 | accented spelling 18,173 vs 195 |
| `estaria` | `estar` | 194 | accented spelling 19,104 vs 194 |
| `medicos` | `médico` | 194 | accented spelling 118,724 vs 194 |
| `comoda` | `cómodo` | 193 | accented spelling 70,880 vs 193 |
| `orquidea` | `orquídea` | 193 | accented spelling 5,924 vs 193 |
| `leccion` | `lección` | 192 | accented spelling 77,587 vs 192 |
| `provision` | `provisión` | 192 | accented spelling 30,799 vs 192 |
| `autonoma` | `autónomo` | 192 | accented spelling 18,560 vs 192 |
| `copan` | `copán` | 192 | accented spelling 1,432 vs 192 |
| `integracion` | `integración` | 192 | accented spelling 145,474 vs 192 |
| `centimetro` | `centímetro` | 191 | accented spelling 127,107 vs 191 |
| `liquidos` | `líquido` | 191 | accented spelling 29,797 vs 191 |
| `arnes` | `arnés` | 191 | accented spelling 12,567 vs 191 |
| `simpatico` | `simpático` | 191 | accented spelling 12,262 vs 191 |
| `agil` | `ágil` | 190 | accented spelling 22,868 vs 190 |
| `volvera` | `volver` | 190 | accented spelling 13,424 vs 190 |
| `cancion` | `canción` | 190 | accented spelling 183,152 vs 190 |
| `rapidos` | `rápido` | 190 | accented spelling 27,446 vs 190 |
| `evalua` | `evaluar` | 189 | accented spelling 10,180 vs 189 |
| `campeon` | `campeón` | 189 | accented spelling 51,955 vs 189 |
| `fria` | `frío` | 189 | accented spelling 33,626 vs 189 |
| `habiamos` | `haber` | 188 | accented spelling 13,106 vs 188 |
| `munchen` | `münchen` | 188 | accented spelling 2,526 vs 188 |
| `irani` | `iraní` | 188 | accented spelling 18,014 vs 188 |
| `computacion` | `computación` | 188 | accented spelling 26,991 vs 188 |
| `ramses` | `ramsés` | 188 | accented spelling 1,320 vs 188 |
| `prestacion` | `prestación` | 187 | accented spelling 93,807 vs 187 |
| `abadia` | `abadía` | 187 | accented spelling 11,512 vs 187 |
| `perigord` | `périgord` | 186 | accented spelling 1,100 vs 186 |
| `jeronimo` | `jerónimo` | 186 | accented spelling 3,907 vs 186 |
| `balsamo` | `bálsamo` | 186 | accented spelling 7,223 vs 186 |
| `patzcuaro` | `pátzcuaro` | 185 | accented spelling 1,326 vs 185 |
| `atitlan` | `atitlán` | 185 | accented spelling 1,522 vs 185 |
| `matias` | `matías` | 185 | accented spelling 3,654 vs 185 |
| `cafeteria` | `cafetería` | 185 | accented spelling 60,156 vs 185 |
| `harmonia` | `armonía` | 184 | accented spelling 1,052 vs 184 |
| `podrias` | `poder` | 184 | accented spelling 23,290 vs 184 |
| `pudieramos` | `poder` | 184 | accented spelling 3,935 vs 184 |
| `rapidas` | `rápido` | 183 | accented spelling 339,618 vs 183 |
| `informatico` | `informático` | 183 | accented spelling 53,975 vs 183 |
| `seccion` | `sección` | 183 | accented spelling 397,805 vs 183 |
| `buho` | `búho` | 183 | accented spelling 5,418 vs 183 |
| `obstaculo` | `obstáculo` | 182 | accented spelling 52,212 vs 182 |
| `participo` | `participar` | 182 | accented spelling 16,329 vs 182 |
| `junin` | `junín` | 182 | accented spelling 1,530 vs 182 |
| `generico` | `genérico` | 182 | accented spelling 36,410 vs 182 |
| `acepto` | `aceptar` | 182 | accented spelling 8,636 vs 182 |
| `sarten` | `sartén` | 180 | accented spelling 27,521 vs 180 |
| `menendez` | `menéndez` | 180 | accented spelling 2,798 vs 180 |
| `tendre` | `tener` | 180 | accented spelling 6,198 vs 180 |
| `haria` | `hacer` | 180 | accented spelling 16,841 vs 180 |
| `catolico` | `católico` | 179 | accented spelling 55,399 vs 179 |
| `estereo` | `estéreo` | 179 | accented spelling 21,207 vs 179 |
| `automovil` | `automóvil` | 178 | accented spelling 129,087 vs 178 |
| `septimo` | `séptimo` | 178 | accented spelling 44,928 vs 178 |
| `publique` | `publicar` | 178 | accented spelling 909 vs 178 |
| `clasificacion` | `clasificación` | 178 | accented spelling 128,017 vs 178 |
| `viver` | `víveres` | 178 | accented spelling 1,351 vs 178 |
| `instantanea` | `instantáneo` | 178 | accented spelling 17,072 vs 178 |
| `bendicion` | `bendición` | 177 | accented spelling 52,916 vs 177 |
| `exportacion` | `exportación` | 177 | accented spelling 113,512 vs 177 |
| `conto` | `contar` | 177 | accented spelling 18,335 vs 177 |
| `galactica` | `galáctico` | 177 | accented spelling 3,184 vs 177 |
| `formulas` | `fórmula` | 177 | accented spelling 10,500 vs 177 |
| `timon` | `timón` | 176 | accented spelling 5,630 vs 176 |
| `ilusion` | `ilusión` | 176 | accented spelling 35,672 vs 176 |
| `niquel` | `níquel` | 176 | accented spelling 16,444 vs 176 |
| `organico` | `orgánico` | 176 | accented spelling 82,827 vs 176 |
| `llameno` | `llamar` | 176 | accented spelling 1,123 vs 176 |
| `simpatica` | `simpático` | 176 | accented spelling 2,089 vs 176 |
| `iras` | `ir` | 176 | accented spelling 2,369 vs 176 |
| `sofa-cama` | `sofá-cama` | 175 | accented spelling 10,030 vs 175 |
| `electricos` | `eléctrico` | 175 | accented spelling 44,741 vs 175 |
| `evolucion` | `evolución` | 175 | accented spelling 166,433 vs 175 |
| `cotizacion` | `cotización` | 174 | accented spelling 55,171 vs 174 |
| `invitacion` | `invitación` | 174 | accented spelling 58,326 vs 174 |
| `ocurrio` | `ocurrir` | 173 | accented spelling 23,878 vs 173 |
| `implementacion` | `implementación` | 173 | accented spelling 130,671 vs 173 |
| `alimentacion` | `alimentación` | 173 | accented spelling 270,133 vs 173 |
| `importacion` | `importación` | 172 | accented spelling 69,939 vs 172 |
| `excepcion` | `excepción` | 172 | accented spelling 97,044 vs 172 |
| `fosforo` | `fósforo` | 172 | accented spelling 12,774 vs 172 |
| `estan` | `estar` | 172 | accented spelling 1,118,813 vs 172 |
| `parabola` | `parábola` | 172 | accented spelling 15,208 vs 172 |
| `extraido` | `extraer` | 172 | accented spelling 4,225 vs 172 |
| `colocacion` | `colocación` | 172 | accented spelling 46,692 vs 172 |
| `travesia` | `travesía` | 172 | accented spelling 22,522 vs 172 |
| `fotografico` | `fotográfico` | 172 | accented spelling 36,118 vs 172 |
| `imagenes` | `imagen` | 171 | accented spelling 358,179 vs 171 |
| `aspera` | `áspero` | 171 | accented spelling 1,759 vs 171 |
| `corporacion` | `corporación` | 170 | accented spelling 37,254 vs 170 |
| `hacian` | `hacer` | 170 | accented spelling 11,706 vs 170 |
| `federacion` | `federación` | 170 | accented spelling 57,697 vs 170 |
| `zocalo` | `zócalo` | 170 | accented spelling 11,132 vs 170 |
| `recibi` | `recibir` | 169 | accented spelling 8,849 vs 169 |
| `fantasticas` | `fantástico` | 169 | accented spelling 29,946 vs 169 |
| `cooperacion` | `cooperación` | 169 | accented spelling 158,735 vs 169 |
| `guarderia` | `guardería` | 169 | accented spelling 20,958 vs 169 |
| `sucedio` | `suceder` | 169 | accented spelling 20,526 vs 169 |
| `traduccion` | `traducción` | 169 | accented spelling 197,180 vs 169 |
| `vere` | `ver` | 169 | accented spelling 1,922 vs 169 |
| `lineas` | `línea` | 169 | accented spelling 130,182 vs 169 |
| `inyeccion` | `inyección` | 168 | accented spelling 98,543 vs 168 |
| `obligacion` | `obligación` | 168 | accented spelling 143,694 vs 168 |
| `tucan` | `tucán` | 168 | accented spelling 1,209 vs 168 |
| `fisicas` | `físico` | 168 | accented spelling 31,278 vs 168 |
| `consagracion` | `consagración` | 167 | accented spelling 8,205 vs 167 |
| `huracan` | `huracán` | 167 | accented spelling 29,598 vs 167 |
| `insolito` | `insólito` | 167 | accented spelling 4,848 vs 167 |
| `avion` | `avión` | 166 | accented spelling 528,178 vs 166 |
| `maestria` | `maestría` | 166 | accented spelling 35,524 vs 166 |
| `vendee` | `vendée` | 166 | accented spelling 1,470 vs 166 |
| `mijail` | `mijaíl` | 165 | accented spelling 894 vs 165 |
| `carre` | `carré` | 165 | accented spelling 986 vs 165 |
| `pate` | `paté` | 165 | accented spelling 1,573 vs 165 |
| `tranvia` | `tranvía` | 165 | accented spelling 23,161 vs 165 |
| `sabados` | `sábado` | 165 | accented spelling 12,018 vs 165 |
| `artico` | `ártico` | 165 | accented spelling 11,506 vs 165 |
| `tiber` | `tíber` | 164 | accented spelling 872 vs 164 |
| `hernan` | `hernán` | 164 | accented spelling 2,524 vs 164 |
| `tactil` | `táctil` | 164 | accented spelling 59,885 vs 164 |
| `gotico` | `gótico` | 164 | accented spelling 19,163 vs 164 |
| `peñon` | `peñón` | 163 | accented spelling 2,755 vs 163 |
| `sanlucar` | `sanlúcar` | 163 | accented spelling 2,136 vs 163 |
| `composicion` | `composición` | 162 | accented spelling 93,481 vs 162 |
| `institucion` | `institución` | 162 | accented spelling 174,230 vs 162 |
| `destruccion` | `destrucción` | 161 | accented spelling 70,630 vs 161 |
| `naci` | `nacer` | 161 | accented spelling 3,678 vs 161 |
| `torsion` | `torsión` | 161 | accented spelling 11,317 vs 161 |
| `opto` | `optar` | 161 | accented spelling 3,042 vs 161 |
| `haras` | `hacer` | 161 | accented spelling 10,527 vs 161 |
| `gabon` | `gabón` | 161 | accented spelling 3,244 vs 161 |
| `especimen` | `espécimen` | 161 | accented spelling 2,874 vs 161 |
| `galerias` | `galería` | 161 | accented spelling 18,113 vs 161 |
| `visualizacion` | `visualización` | 160 | accented spelling 81,940 vs 160 |
| `marron` | `marrón` | 160 | accented spelling 53,033 vs 160 |
| `vacia` | `vacío` | 160 | accented spelling 11,873 vs 160 |
| `limitacion` | `limitación` | 160 | accented spelling 100,744 vs 160 |
| `serguei` | `serguéi` | 160 | accented spelling 1,928 vs 160 |
| `angelico` | `angélico` | 160 | accented spelling 4,713 vs 160 |
| `calderon` | `calderón` | 159 | accented spelling 8,445 vs 159 |
| `parecio` | `parecer` | 159 | accented spelling 13,733 vs 159 |
| `guell` | `güell` | 159 | accented spelling 4,208 vs 159 |
| `auna` | `aunar` | 159 | accented spelling 1,802 vs 159 |
| `aleron` | `alerón` | 159 | accented spelling 2,355 vs 159 |
| `fermin` | `fermín` | 159 | accented spelling 1,844 vs 159 |
| `maori` | `maorí` | 158 | accented spelling 1,619 vs 158 |
| `huespedes` | `huésped` | 158 | accented spelling 425,782 vs 158 |
| `puntuacion` | `puntuación` | 158 | accented spelling 102,723 vs 158 |
| `engendro` | `engendrar` | 158 | accented spelling 2,899 vs 158 |
| `jardin` | `jardín` | 157 | accented spelling 434,506 vs 157 |
| `ningun` | `ninguno` | 157 | accented spelling 291,329 vs 157 |
| `estrategicamente` | `estratégicamente` | 157 | accented spelling 12,046 vs 157 |
| `civica` | `cívico` | 157 | accented spelling 2,838 vs 157 |
| `profesion` | `profesión` | 157 | accented spelling 51,529 vs 157 |
| `confusion` | `confusión` | 157 | accented spelling 37,966 vs 157 |
| `eslabon` | `eslabón` | 157 | accented spelling 6,916 vs 157 |
| `gosen` | `gosén` | 157 | accented spelling 1,196 vs 157 |
| `tintin` | `tintín` | 156 | accented spelling 1,131 vs 156 |
| `giron` | `girón` | 156 | accented spelling 1,388 vs 156 |
| `hermon` | `hermón` | 156 | accented spelling 948 vs 156 |
| `recibiran` | `recibir` | 156 | accented spelling 16,509 vs 156 |
| `mogan` | `mogán` | 156 | accented spelling 1,872 vs 156 |
| `ubicacion` | `ubicación` | 155 | accented spelling 674,329 vs 155 |
| `eligio` | `elegir` | 155 | accented spelling 9,316 vs 155 |
| `gines` | `ginés` | 155 | accented spelling 818 vs 155 |
| `prision` | `prisión` | 155 | accented spelling 66,168 vs 155 |
| `termometro` | `termómetro` | 155 | accented spelling 15,802 vs 155 |
| `notificacion` | `notificación` | 154 | accented spelling 172,773 vs 154 |
| `rabi` | `rabí` | 154 | accented spelling 3,165 vs 154 |
| `asiatico` | `asiático` | 154 | accented spelling 48,308 vs 154 |
| `arquitectonico` | `arquitectónico` | 154 | accented spelling 43,914 vs 154 |
| `propulsion` | `propulsión` | 154 | accented spelling 9,323 vs 154 |
| `financiacion` | `financiación` | 153 | accented spelling 82,302 vs 153 |
| `tengais` | `tener` | 152 | accented spelling 4,410 vs 152 |
| `norteamerica` | `norteamérica` | 152 | accented spelling 23,472 vs 152 |
| `ampliacion` | `ampliación` | 152 | accented spelling 64,986 vs 152 |
| `meditacion` | `meditación` | 152 | accented spelling 49,680 vs 152 |
| `enfasis` | `énfasis` | 152 | accented spelling 41,247 vs 152 |
| `volumenes` | `volumen` | 152 | accented spelling 19,279 vs 152 |
| `tiburon` | `tiburón` | 152 | accented spelling 15,160 vs 152 |
| `tuiteo` | `tuitear` | 152 | accented spelling 2,988 vs 152 |
| `enfermeria` | `enfermería` | 152 | accented spelling 30,835 vs 152 |
| `minusvalido` | `minusválido` | 151 | accented spelling 3,256 vs 151 |
| `gano` | `ganar` | 151 | accented spelling 29,736 vs 151 |
| `geiser` | `géiser` | 151 | accented spelling 881 vs 151 |
| `platano` | `plátano` | 151 | accented spelling 16,097 vs 151 |
| `pudin` | `pudín` | 150 | accented spelling 1,462 vs 150 |
| `atmosfera` | `atmósfera` | 150 | accented spelling 72,950 vs 150 |
| `tecnologica` | `tecnológico` | 150 | accented spelling 23,759 vs 150 |
| `idolo` | `ídolo` | 150 | accented spelling 13,742 vs 150 |
| `climatico` | `climático` | 150 | accented spelling 42,940 vs 150 |
| `queriamos` | `querer` | 150 | accented spelling 9,412 vs 150 |
| `dinamico` | `dinámico` | 149 | accented spelling 108,517 vs 149 |
| `aprendi` | `aprender` | 149 | accented spelling 7,831 vs 149 |
| `extraccion` | `extracción` | 148 | accented spelling 61,480 vs 148 |
| `quisieramos` | `querer` | 148 | accented spelling 2,717 vs 148 |
| `espia` | `espía` | 148 | accented spelling 10,615 vs 148 |
| `donacion` | `donación` | 148 | accented spelling 53,622 vs 148 |
| `centroamerica` | `centroamérica` | 147 | accented spelling 17,260 vs 147 |
| `portugues` | `portugués` | 147 | accented spelling 43,944 vs 147 |
| `sequia` | `sequía` | 147 | accented spelling 20,171 vs 147 |
| `moreton` | `moretón` | 147 | accented spelling 2,662 vs 147 |
| `depresion` | `depresión` | 147 | accented spelling 67,724 vs 147 |
| `academico` | `académico` | 146 | accented spelling 97,916 vs 146 |
| `afrodisiaco` | `afrodisíaco` | 146 | accented spelling 1,646 vs 146 |
| `mensajeria` | `mensajería` | 146 | accented spelling 40,242 vs 146 |
| `activacion` | `activación` | 145 | accented spelling 46,556 vs 145 |
| `pulpito` | `púlpito` | 145 | accented spelling 2,475 vs 145 |
| `perdio` | `perder` | 145 | accented spelling 17,969 vs 145 |
| `polimero` | `polímero` | 145 | accented spelling 17,875 vs 145 |
| `marcho` | `marchar` | 144 | accented spelling 1,062 vs 144 |
| `verificacion` | `verificación` | 143 | accented spelling 83,451 vs 143 |
| `chaman` | `chamán` | 143 | accented spelling 3,476 vs 143 |
| `relajacion` | `relajación` | 143 | accented spelling 44,295 vs 143 |
| `energetica` | `energético` | 143 | accented spelling 33,594 vs 143 |
| `cosmetico` | `cosmético` | 143 | accented spelling 41,405 vs 143 |
| `astrologia` | `astrología` | 143 | accented spelling 11,289 vs 143 |
| `preocupacion` | `preocupación` | 143 | accented spelling 106,948 vs 143 |
| `carroceria` | `carrocería` | 142 | accented spelling 36,972 vs 142 |
| `quirurgico` | `quirúrgico` | 142 | accented spelling 47,759 vs 142 |
| `pondra` | `poner` | 142 | accented spelling 15,968 vs 142 |
| `geometria` | `geometría` | 142 | accented spelling 23,536 vs 142 |
| `debora` | `débora` | 142 | accented spelling 1,284 vs 142 |
| `formaldehido` | `formaldehído` | 142 | accented spelling 2,856 vs 142 |
| `cupula` | `cúpula` | 142 | accented spelling 16,151 vs 142 |
| `separacion` | `separación` | 142 | accented spelling 56,577 vs 142 |
| `envianos` | `enviar` | 142 | accented spelling 6,783 vs 142 |
| `proteinas` | `proteína` | 142 | accented spelling 36,375 vs 142 |
| `aparecio` | `aparecer` | 141 | accented spelling 21,535 vs 141 |
| `colera` | `cólera#Masc` | 141 | accented spelling 10,600 vs 141 |
| `peco` | `pecar` | 141 | accented spelling 1,086 vs 141 |
| `mantendra` | `mantener` | 140 | accented spelling 13,006 vs 140 |
| `comodos` | `cómodo` | 140 | accented spelling 21,176 vs 140 |
| `odontologia` | `odontología` | 140 | accented spelling 12,428 vs 140 |
| `pucon` | `pucón` | 140 | accented spelling 2,196 vs 140 |
| `ecologica` | `ecológico` | 140 | accented spelling 16,949 vs 140 |
| `habil` | `hábil` | 140 | accented spelling 23,791 vs 140 |
| `aviñon` | `aviñón` | 140 | accented spelling 4,140 vs 140 |
| `reputacion` | `reputación` | 139 | accented spelling 64,789 vs 139 |
| `creyo` | `creer` | 139 | accented spelling 4,834 vs 139 |
| `velasquez` | `velásquez` | 139 | accented spelling 1,632 vs 139 |
| `reaccion` | `reacción` | 139 | accented spelling 110,678 vs 139 |
| `macias` | `macías` | 138 | accented spelling 968 vs 138 |
| `enos` | `enós` | 138 | accented spelling 834 vs 138 |
| `millan` | `millán` | 138 | accented spelling 1,180 vs 138 |
| `anibal` | `aníbal` | 138 | accented spelling 1,776 vs 138 |
| `indicacion` | `indicación` | 138 | accented spelling 83,996 vs 138 |
| `eurovision` | `eurovisión` | 138 | accented spelling 3,032 vs 138 |
| `parasito` | `parásito` | 137 | accented spelling 10,886 vs 137 |
| `dira` | `decir` | 137 | accented spelling 10,624 vs 137 |
| `exclusion` | `exclusión` | 137 | accented spelling 42,941 vs 137 |
| `bujia` | `bujía` | 137 | accented spelling 4,157 vs 137 |
| `evasion` | `evasión` | 137 | accented spelling 7,982 vs 137 |
| `aaiun` | `aaiún` | 137 | accented spelling 880 vs 137 |
| `garantias` | `garantía` | 137 | accented spelling 38,326 vs 137 |
| `vehiculos` | `vehículo` | 136 | accented spelling 129,328 vs 136 |
| `triada` | `tríada` | 136 | accented spelling 1,896 vs 136 |
| `cuadruple` | `cuádruple` | 136 | accented spelling 6,174 vs 136 |
| `arcangel` | `arcángel` | 136 | accented spelling 5,230 vs 136 |
| `parametro` | `parámetro` | 136 | accented spelling 88,663 vs 136 |
| `exotica` | `exótico` | 136 | accented spelling 2,910 vs 136 |
| `motivacion` | `motivación` | 136 | accented spelling 43,070 vs 136 |
| `mandara` | `mandar` | 136 | accented spelling 1,939 vs 136 |
| `confeccion` | `confección` | 136 | accented spelling 14,462 vs 136 |
| `erectil` | `eréctil` | 136 | accented spelling 11,743 vs 136 |
| `instantaneo` | `instantáneo` | 135 | accented spelling 52,539 vs 135 |
| `parrafo` | `párrafo` | 135 | accented spelling 87,678 vs 135 |
| `concentracion` | `concentración` | 135 | accented spelling 91,641 vs 135 |
| `enriquez` | `enríquez` | 135 | accented spelling 796 vs 135 |
| `fenomeno` | `fenómeno` | 135 | accented spelling 73,131 vs 135 |
| `elastico` | `elástico` | 134 | accented spelling 46,430 vs 134 |
| `ideo` | `idear` | 134 | accented spelling 873 vs 134 |
| `aereas` | `aéreo` | 134 | accented spelling 75,638 vs 134 |
| `jamas` | `jamás` | 134 | accented spelling 89,169 vs 134 |
| `chavon` | `chavón` | 134 | accented spelling 3,518 vs 134 |
| `protesis` | `prótesis` | 134 | accented spelling 15,338 vs 134 |
| `gimenez` | `giménez` | 134 | accented spelling 1,464 vs 134 |
| `oregano` | `orégano` | 133 | accented spelling 4,772 vs 133 |
| `erevan` | `ereván` | 133 | accented spelling 3,318 vs 133 |
| `aleacion` | `aleación` | 133 | accented spelling 125,990 vs 133 |
| `tapiceria` | `tapicería` | 133 | accented spelling 9,742 vs 133 |
| `timida` | `tímido` | 133 | accented spelling 2,062 vs 133 |
| `valdes` | `valdés` | 133 | accented spelling 3,196 vs 133 |
| `convencion` | `convención` | 133 | accented spelling 117,567 vs 133 |
| `interaccion` | `interacción` | 133 | accented spelling 97,808 vs 133 |
| `tetuan` | `tetuán` | 132 | accented spelling 1,974 vs 132 |
| `bailarin` | `bailarín` | 132 | accented spelling 13,432 vs 132 |
| `vivia` | `vivir` | 132 | accented spelling 12,079 vs 132 |
| `arqueologico` | `arqueológico` | 132 | accented spelling 32,517 vs 132 |
| `caratula` | `carátula` | 131 | accented spelling 2,508 vs 131 |
| `tacon` | `tacón` | 131 | accented spelling 19,234 vs 131 |
| `extrusion` | `extrusión` | 131 | accented spelling 12,969 vs 131 |
| `exotico` | `exótico` | 131 | accented spelling 20,501 vs 131 |
| `argon` | `argón` | 131 | accented spelling 2,100 vs 131 |
| `conocia` | `conocer` | 131 | accented spelling 11,749 vs 131 |
| `comi` | `comer` | 131 | accented spelling 1,634 vs 131 |
| `raco` | `racó` | 131 | accented spelling 730 vs 131 |
| `normandia` | `normandía` | 131 | accented spelling 7,430 vs 131 |
| `entrevisto` | `entrevistar` | 130 | accented spelling 1,923 vs 130 |
| `observacion` | `observación` | 130 | accented spelling 87,632 vs 130 |
| `graduacion` | `graduación` | 130 | accented spelling 21,226 vs 130 |
| `iluminacion` | `iluminación` | 130 | accented spelling 149,187 vs 130 |
| `transportacion` | `transportación` | 130 | accented spelling 7,410 vs 130 |
| `macae` | `macaé` | 130 | accented spelling 704 vs 130 |
| `paez` | `páez` | 130 | accented spelling 862 vs 130 |
| `penetracion` | `penetración` | 130 | accented spelling 22,404 vs 130 |
| `oce` | `océ` | 129 | accented spelling 1,024 vs 129 |
| `peonia` | `peonía` | 129 | accented spelling 1,482 vs 129 |
| `enseñe` | `enseñar` | 129 | accented spelling 1,253 vs 129 |
| `infeccion` | `infección` | 129 | accented spelling 177,586 vs 129 |
| `ubeda` | `úbeda` | 129 | accented spelling 1,176 vs 129 |
| `idoneo` | `idóneo` | 129 | accented spelling 26,290 vs 129 |
| `cojin` | `cojín` | 129 | accented spelling 23,362 vs 129 |
| `danes` | `danés` | 129 | accented spelling 15,178 vs 129 |
| `relajate` | `relajarse` | 128 | accented spelling 8,298 vs 128 |
| `leganes` | `leganés` | 128 | accented spelling 1,998 vs 128 |
| `deteccion` | `detección` | 128 | accented spelling 117,445 vs 128 |
| `oidme` | `oír` | 128 | accented spelling 728 vs 128 |
| `baston` | `bastón` | 128 | accented spelling 10,368 vs 128 |
| `estrategico` | `estratégico` | 128 | accented spelling 90,959 vs 128 |
| `permitio` | `permitir` | 128 | accented spelling 28,520 vs 128 |
| `colchon` | `colchón` | 128 | accented spelling 32,742 vs 128 |
| `doblo` | `doblar` | 128 | accented spelling 641 vs 128 |
| `efraim` | `efraím` | 128 | accented spelling 2,000 vs 128 |
| `salome` | `salomé` | 128 | accented spelling 1,448 vs 128 |
| `necesitabamos` | `necesitar` | 128 | accented spelling 5,047 vs 128 |
| `reposteria` | `repostería` | 128 | accented spelling 5,252 vs 128 |
| `exhorto` | `exhortar` | 127 | accented spelling 1,588 vs 127 |
| `nomada` | `nómada` | 127 | accented spelling 5,627 vs 127 |
| `abri` | `abrir` | 127 | accented spelling 2,052 vs 127 |
| `jazmin` | `jazmín` | 127 | accented spelling 3,993 vs 127 |
| `esau` | `esaú` | 127 | accented spelling 11,182 vs 127 |
| `anulacion` | `anulación` | 127 | accented spelling 12,641 vs 127 |
| `malvasia` | `malvasía` | 127 | accented spelling 689 vs 127 |
| `utero` | `útero` | 127 | accented spelling 27,887 vs 127 |
| `alce` | `alzar` | 127 | accented spelling 679 vs 127 |
| `segui` | `seguir` | 127 | accented spelling 3,024 vs 127 |
| `onis` | `onís` | 127 | accented spelling 1,246 vs 127 |
| `toxica` | `tóxico` | 126 | accented spelling 2,968 vs 126 |
| `graficos` | `gráfico` | 126 | accented spelling 64,378 vs 126 |
| `porcion` | `porción` | 126 | accented spelling 60,296 vs 126 |
| `podiamos` | `poder` | 126 | accented spelling 6,628 vs 126 |
| `caidas` | `caída` | 126 | accented spelling 12,073 vs 126 |
| `emocion` | `emoción` | 126 | accented spelling 79,995 vs 126 |
| `frio-calor` | `frío-calor` | 125 | accented spelling 964 vs 125 |
| `sintesis` | `síntesis` | 125 | accented spelling 37,923 vs 125 |
| `etiope` | `etíope` | 125 | accented spelling 3,949 vs 125 |
| `guarani` | `guaraní` | 125 | accented spelling 2,547 vs 125 |
| `calorias` | `caloría` | 125 | accented spelling 29,849 vs 125 |
| `saldra` | `salir` | 124 | accented spelling 9,663 vs 124 |
| `lipolisis` | `lipólisis` | 124 | accented spelling 1,014 vs 124 |
| `extraidos` | `extraer` | 124 | accented spelling 2,822 vs 124 |
| `imaginate` | `imaginarse` | 124 | accented spelling 4,348 vs 124 |
| `tematico` | `temático` | 124 | accented spelling 25,044 vs 124 |
| `transaccion` | `transacción` | 124 | accented spelling 102,416 vs 124 |
| `turo` | `turó` | 124 | accented spelling 764 vs 124 |
| `pixeles` | `píxel` | 124 | accented spelling 11,449 vs 124 |
| `deficit` | `déficit` | 123 | accented spelling 31,261 vs 123 |
| `economicamente` | `económicamente` | 123 | accented spelling 17,402 vs 123 |
| `sanguineo` | `sanguíneo` | 123 | accented spelling 43,409 vs 123 |
| `superheroe` | `superhéroe` | 123 | accented spelling 6,692 vs 123 |
| `tendras` | `tener` | 123 | accented spelling 88,252 vs 123 |
| `aisla` | `aislar` | 123 | accented spelling 1,160 vs 123 |
| `quindio` | `quindío` | 122 | accented spelling 1,039 vs 122 |
| `alarcon` | `alarcón` | 122 | accented spelling 3,076 vs 122 |
| `esperabamos` | `esperar` | 122 | accented spelling 3,241 vs 122 |
| `milimetro` | `milímetro` | 122 | accented spelling 244,222 vs 122 |
| `japones` | `japonés` | 122 | accented spelling 91,209 vs 122 |
| `piñon` | `piñón` | 122 | accented spelling 5,434 vs 122 |
| `interactuan` | `interactuar` | 122 | accented spelling 5,733 vs 122 |
| `posesion` | `posesión` | 122 | accented spelling 51,677 vs 122 |
| `coyoacan` | `coyoacán` | 122 | accented spelling 1,356 vs 122 |
| `querian` | `querer` | 121 | accented spelling 13,186 vs 121 |
| `torrejon` | `torrejón` | 121 | accented spelling 1,792 vs 121 |
| `reclamacion` | `reclamación` | 121 | accented spelling 65,074 vs 121 |
| `azoto` | `azotar` | 121 | accented spelling 997 vs 121 |
| `eter` | `éter` | 121 | accented spelling 4,161 vs 121 |
| `matara` | `matar` | 121 | accented spelling 1,665 vs 121 |
| `corrosion` | `corrosión` | 121 | accented spelling 33,274 vs 121 |
| `liston` | `listón` | 120 | accented spelling 4,211 vs 120 |
| `roldan` | `roldán` | 120 | accented spelling 1,056 vs 120 |
| `renovacion` | `renovación` | 120 | accented spelling 63,977 vs 120 |
| `magnetico` | `magnético` | 120 | accented spelling 51,424 vs 120 |
| `camaron` | `camarón` | 119 | accented spelling 12,706 vs 119 |
| `ficcion` | `ficción` | 119 | accented spelling 43,856 vs 119 |
| `transformacion` | `transformación` | 119 | accented spelling 103,568 vs 119 |
| `traera` | `traer` | 119 | accented spelling 7,699 vs 119 |
| `indice` | `índice` | 119 | accented spelling 233,494 vs 119 |
| `compas` | `compás` | 119 | accented spelling 7,147 vs 119 |
| `comprension` | `comprensión` | 119 | accented spelling 101,154 vs 119 |
| `hubieramos` | `haber` | 119 | accented spelling 3,693 vs 119 |
| `automatizacion` | `automatización` | 119 | accented spelling 58,363 vs 119 |
| `aprobacion` | `aprobación` | 119 | accented spelling 95,753 vs 119 |
| `geografia` | `geografía` | 118 | accented spelling 24,303 vs 118 |
| `lejia` | `lejía` | 118 | accented spelling 3,628 vs 118 |
| `botin` | `botín` | 118 | accented spelling 15,367 vs 118 |
| `montgo` | `montgó` | 118 | accented spelling 1,092 vs 118 |
| `contactano` | `contactar` | 118 | accented spelling 672 vs 118 |
| `sanson` | `sansón` | 118 | accented spelling 3,893 vs 118 |
| `amitie` | `amitié` | 118 | accented spelling 748 vs 118 |
| `kefir` | `kéfir` | 118 | accented spelling 1,187 vs 118 |
| `compro` | `comprar` | 117 | accented spelling 12,455 vs 117 |
| `dedicacion` | `dedicación` | 117 | accented spelling 35,493 vs 117 |
| `recomendacion` | `recomendación` | 117 | accented spelling 128,876 vs 117 |
| `volvere` | `volver` | 117 | accented spelling 4,964 vs 117 |
| `automoviles` | `automóvil` | 117 | accented spelling 42,940 vs 117 |
| `rubeola` | `rubéola` | 117 | accented spelling 2,046 vs 117 |
| `continuen` | `continuar` | 117 | accented spelling 3,801 vs 117 |
| `tematica` | `temática` | 117 | accented spelling 39,243 vs 117 |
| `abrio` | `abrir` | 116 | accented spelling 28,419 vs 116 |
| `projimo` | `prójimo` | 116 | accented spelling 23,782 vs 116 |
| `guio` | `guiar` | 116 | accented spelling 1,853 vs 116 |
| `sueter` | `suéter` | 116 | accented spelling 9,700 vs 116 |
| `electrolisis` | `electrólisis` | 116 | accented spelling 1,404 vs 116 |
| `bolson` | `bolsón` | 116 | accented spelling 1,381 vs 116 |
| `callejon` | `callejón` | 116 | accented spelling 11,374 vs 116 |
| `optimo` | `óptimo` | 116 | accented spelling 118,575 vs 116 |
| `telefonia` | `telefonía` | 116 | accented spelling 31,689 vs 116 |
| `maximalista` | `máximalista` | 116 | accented spelling 733 vs 116 |
| `faraon` | `faraón` | 116 | accented spelling 35,306 vs 116 |
| `mios` | `mío` | 115 | accented spelling 11,145 vs 115 |
| `psicologico` | `psicológico` | 115 | accented spelling 34,113 vs 115 |
| `metodologia` | `metodología` | 115 | accented spelling 74,729 vs 115 |
| `pasion` | `pasión` | 115 | accented spelling 104,519 vs 115 |
| `maniaco` | `maníaco` | 115 | accented spelling 1,516 vs 115 |
| `aviacion` | `aviación` | 115 | accented spelling 27,058 vs 115 |
| `cafes` | `café` | 115 | accented spelling 12,383 vs 115 |
| `transicion` | `transición` | 115 | accented spelling 83,030 vs 115 |
| `situan` | `situar` | 115 | accented spelling 1,437 vs 115 |
| `teheran` | `teherán` | 115 | accented spelling 15,320 vs 115 |
| `narcotico` | `narcótico` | 114 | accented spelling 4,070 vs 114 |
| `coordinacion` | `coordinación` | 114 | accented spelling 63,785 vs 114 |
| `tabernaculo` | `tabernáculo` | 114 | accented spelling 24,410 vs 114 |
| `gluteo` | `glúteo` | 114 | accented spelling 3,968 vs 114 |
| `oposicion` | `oposición` | 114 | accented spelling 85,166 vs 114 |
| `termica` | `térmico` | 113 | accented spelling 22,604 vs 113 |
| `futon` | `futón` | 113 | accented spelling 4,094 vs 113 |
| `encontra` | `encontrar` | 113 | accented spelling 1,580 vs 113 |
| `heroismo` | `heroísmo` | 113 | accented spelling 2,813 vs 113 |
| `contribucion` | `contribución` | 113 | accented spelling 81,197 vs 113 |
| `proximos` | `próximo` | 113 | accented spelling 86,049 vs 113 |
| `automata` | `autómata` | 113 | accented spelling 2,072 vs 113 |
| `basquet` | `básquet` | 113 | accented spelling 889 vs 113 |
| `maraton` | `maratón` | 112 | accented spelling 14,200 vs 112 |
| `vereis` | `ver` | 112 | accented spelling 3,781 vs 112 |
| `curcuma` | `cúrcuma` | 112 | accented spelling 4,844 vs 112 |
| `guillen` | `guillén` | 112 | accented spelling 1,150 vs 112 |
| `caiman` | `caimán` | 112 | accented spelling 11,165 vs 112 |
| `atomos` | `átomo` | 112 | accented spelling 5,987 vs 112 |
| `biologico` | `biológico` | 111 | accented spelling 48,102 vs 111 |
| `decian` | `decir` | 111 | accented spelling 12,975 vs 111 |
| `busquedas` | `búsqueda` | 111 | accented spelling 38,872 vs 111 |
| `moron` | `morón` | 111 | accented spelling 1,665 vs 111 |
| `pinguino` | `pingüino` | 111 | accented spelling 6,894 vs 111 |
| `colico` | `cólico` | 111 | accented spelling 3,090 vs 111 |
| `cehegin` | `cehegín` | 111 | accented spelling 914 vs 111 |
| `seguira` | `seguir` | 111 | accented spelling 20,247 vs 111 |
| `diafano` | `diáfano` | 110 | accented spelling 4,470 vs 110 |
| `sermon` | `sermón` | 110 | accented spelling 9,263 vs 110 |
| `alojate` | `alojarse` | 110 | accented spelling 9,776 vs 110 |
| `ocupacion` | `ocupación` | 110 | accented spelling 56,645 vs 110 |
| `estrategica` | `estratégico` | 110 | accented spelling 25,031 vs 110 |
| `explicitamente` | `explícitamente` | 110 | accented spelling 15,217 vs 110 |
| `perdida#Masc` | `pérdida` | 110 | accented spelling 340,080 vs 110 |
| `dolar` | `dólar` | 110 | accented spelling 194,260 vs 110 |
| `terminacion` | `terminación` | 110 | accented spelling 28,447 vs 110 |
| `erase` | `ser` | 110 | accented spelling 768 vs 110 |
| `mancora` | `máncora` | 110 | accented spelling 792 vs 110 |
| `nuvi` | `nüvi` | 110 | accented spelling 1,162 vs 110 |
| `acustica` | `acústico` | 110 | accented spelling 8,957 vs 110 |
| `vegetacion` | `vegetación` | 109 | accented spelling 36,100 vs 109 |
| `clarin` | `clarín` | 109 | accented spelling 1,678 vs 109 |
| `competicion` | `competición` | 109 | accented spelling 60,306 vs 109 |
| `tacita` | `tácito` | 109 | accented spelling 786 vs 109 |
| `juridica` | `jurídico` | 109 | accented spelling 24,713 vs 109 |
| `autonomia` | `autonomía` | 109 | accented spelling 39,874 vs 109 |
| `biogas` | `biogás` | 109 | accented spelling 5,413 vs 109 |
| `solia` | `soler` | 109 | accented spelling 13,872 vs 109 |
| `fallecio` | `fallecer` | 109 | accented spelling 7,885 vs 109 |
| `alcoholicas` | `alcohólico` | 108 | accented spelling 8,404 vs 108 |
| `legislacion` | `legislación` | 108 | accented spelling 131,432 vs 108 |
| `darsena` | `dársena` | 108 | accented spelling 970 vs 108 |
| `fronton` | `frontón` | 108 | accented spelling 1,589 vs 108 |
| `brigida` | `brígida` | 108 | accented spelling 873 vs 108 |
| `anonimo` | `anónimo` | 108 | accented spelling 50,753 vs 108 |
| `xel-ha` | `xel-há` | 108 | accented spelling 598 vs 108 |
| `sento` | `sentar` | 108 | accented spelling 1,254 vs 108 |
| `remodelacion` | `remodelación` | 108 | accented spelling 11,209 vs 108 |
| `natacion` | `natación` | 108 | accented spelling 28,564 vs 108 |
| `creia` | `creer` | 108 | accented spelling 12,027 vs 108 |
| `cañamo` | `cáñamo` | 108 | accented spelling 11,218 vs 108 |
| `congregacion` | `congregación` | 108 | accented spelling 42,708 vs 108 |
| `necesitais` | `necesitar` | 107 | accented spelling 1,406 vs 107 |
| `cafeina` | `cafeína` | 107 | accented spelling 21,303 vs 107 |
| `telefonicas` | `telefónico` | 107 | accented spelling 11,333 vs 107 |
| `galvez` | `gálvez` | 107 | accented spelling 1,402 vs 107 |
| `davila` | `dávila` | 107 | accented spelling 1,006 vs 107 |
| `elevacion` | `elevación` | 106 | accented spelling 60,791 vs 106 |
| `impresion` | `impresión` | 106 | accented spelling 259,589 vs 106 |
| `aceleracion` | `aceleración` | 106 | accented spelling 27,382 vs 106 |
| `societe` | `société` | 106 | accented spelling 860 vs 106 |
| `atras` | `atrás` | 106 | accented spelling 200,188 vs 106 |
| `pelicano` | `pelícano` | 106 | accented spelling 1,538 vs 106 |
| `chamartin` | `chamartín` | 106 | accented spelling 1,438 vs 106 |
| `limites` | `límite` | 106 | accented spelling 65,236 vs 106 |
| `camboriu` | `camboriú` | 106 | accented spelling 622 vs 106 |
| `examenes` | `examen` | 106 | accented spelling 38,813 vs 106 |
| `galvan` | `galván` | 106 | accented spelling 972 vs 106 |
| `tuyu` | `tuyú` | 106 | accented spelling 560 vs 106 |
| `muchisima` | `mucho` | 106 | accented spelling 2,341 vs 106 |
| `tarantula` | `tarántula` | 105 | accented spelling 674 vs 105 |
| `chandal` | `chándal` | 105 | accented spelling 2,423 vs 105 |
| `povoa` | `póvoa` | 105 | accented spelling 622 vs 105 |
| `boveda` | `bóveda` | 105 | accented spelling 12,613 vs 105 |
| `aparicion` | `aparición` | 105 | accented spelling 78,354 vs 105 |
| `recoleccion` | `recolección` | 105 | accented spelling 51,048 vs 105 |
| `hayais` | `haber` | 105 | accented spelling 2,650 vs 105 |
| `pondre` | `poner` | 105 | accented spelling 5,792 vs 105 |
| `kurdistan` | `kurdistán` | 105 | accented spelling 3,962 vs 105 |
| `albedrio` | `albedrío` | 105 | accented spelling 7,670 vs 105 |
| `acordeon` | `acordeón` | 105 | accented spelling 3,740 vs 105 |
| `dispersion` | `dispersión` | 104 | accented spelling 19,344 vs 104 |
| `funcion` | `función` | 104 | accented spelling 763,722 vs 104 |
| `mistico` | `místico` | 104 | accented spelling 12,353 vs 104 |
| `britanico` | `británico` | 104 | accented spelling 93,682 vs 104 |
| `zoologico` | `zoológico` | 104 | accented spelling 18,577 vs 104 |
| `cedula` | `cédula` | 104 | accented spelling 2,955 vs 104 |
| `incognita` | `incógnito` | 104 | accented spelling 667 vs 104 |
| `katmandu` | `katmandú` | 104 | accented spelling 5,998 vs 104 |
| `biologia` | `biología` | 104 | accented spelling 27,946 vs 104 |
| `cupon` | `cupón` | 104 | accented spelling 27,632 vs 104 |
| `sucedera` | `suceder` | 104 | accented spelling 6,411 vs 104 |
| `bejar` | `béjar` | 104 | accented spelling 1,160 vs 104 |
| `micrometro` | `micrómetro` | 103 | accented spelling 1,422 vs 103 |
| `raba` | `rabá` | 103 | accented spelling 856 vs 103 |
| `fabula` | `fábula` | 103 | accented spelling 3,131 vs 103 |
| `olimpica` | `olímpico` | 103 | accented spelling 3,702 vs 103 |
| `adquisicion` | `adquisición` | 103 | accented spelling 81,615 vs 103 |
| `andujar` | `andújar` | 103 | accented spelling 904 vs 103 |
| `gavilan` | `gavilán` | 103 | accented spelling 698 vs 103 |
| `estefania` | `estefanía` | 103 | accented spelling 586 vs 103 |
| `medicamente` | `médicamente` | 103 | accented spelling 3,188 vs 103 |
| `barcena` | `bárcena` | 103 | accented spelling 582 vs 103 |
| `adoracion` | `adoración` | 102 | accented spelling 24,653 vs 102 |
| `estetico` | `estético` | 102 | accented spelling 49,174 vs 102 |
| `baul` | `baúl` | 102 | accented spelling 3,851 vs 102 |
| `meti` | `meter` | 102 | accented spelling 569 vs 102 |
| `efrain` | `efraín` | 102 | accented spelling 8,736 vs 102 |
| `horoscopo` | `horóscopo` | 102 | accented spelling 8,823 vs 102 |
| `deberiamos` | `deber` | 102 | accented spelling 14,216 vs 102 |
| `lacteo` | `lácteo` | 102 | accented spelling 17,139 vs 102 |
| `disfruteis` | `disfrutar` | 102 | accented spelling 1,449 vs 102 |
| `respondera` | `responder` | 102 | accented spelling 6,147 vs 102 |
| `toxicas` | `tóxico` | 102 | accented spelling 4,291 vs 102 |
| `loule` | `loulé` | 102 | accented spelling 548 vs 102 |
| `proporcion` | `proporción` | 101 | accented spelling 67,771 vs 101 |
| `patron` | `patrón` | 101 | accented spelling 137,171 vs 101 |
| `manipulacion` | `manipulación` | 101 | accented spelling 47,488 vs 101 |
| `iberico` | `ibérico` | 101 | accented spelling 15,503 vs 101 |
| `lanzo` | `lanzar` | 101 | accented spelling 28,898 vs 101 |
| `registracion` | `registración` | 101 | accented spelling 4,433 vs 101 |
| `recobro` | `recobrar` | 101 | accented spelling 612 vs 101 |
| `recopilacion` | `recopilación` | 101 | accented spelling 43,763 vs 101 |
| `bermudez` | `bermúdez` | 101 | accented spelling 1,540 vs 101 |
| `goias` | `goiás` | 101 | accented spelling 874 vs 101 |
| `actuacion` | `actuación` | 101 | accented spelling 79,003 vs 101 |
| `descubri` | `descubrir` | 100 | accented spelling 6,984 vs 100 |
| `dirijase` | `dirigirse` | 100 | accented spelling 10,642 vs 100 |
| `adicion` | `adición` | 100 | accented spelling 39,425 vs 100 |
| `eucaristia` | `eucaristía` | 100 | accented spelling 20,423 vs 100 |
| `timido` | `tímido` | 100 | accented spelling 8,689 vs 100 |
| `prostata` | `próstata` | 100 | accented spelling 32,665 vs 100 |
| `esparrago` | `espárrago` | 99 | accented spelling 3,798 vs 99 |
| `abrira` | `abrir` | 99 | accented spelling 9,540 vs 99 |
| `cortazar` | `cortázar` | 99 | accented spelling 930 vs 99 |
| `retencion` | `retención` | 99 | accented spelling 54,178 vs 99 |
| `vias` | `vía` | 99 | accented spelling 42,004 vs 99 |
| `fertil` | `fértil` | 99 | accented spelling 12,001 vs 99 |
| `debi` | `deber` | 99 | accented spelling 952 vs 99 |
| `adaptacion` | `adaptación` | 99 | accented spelling 70,308 vs 99 |
| `intervencion` | `intervención` | 99 | accented spelling 122,853 vs 99 |
| `perfeccion` | `perfección` | 99 | accented spelling 65,697 vs 99 |
| `boqueron` | `boquerón` | 98 | accented spelling 866 vs 98 |
| `deberas` | `deber` | 98 | accented spelling 18,316 vs 98 |
| `competa` | `cómpeta` | 98 | accented spelling 1,326 vs 98 |
| `podra` | `poder` | 98 | accented spelling 262,962 vs 98 |
| `piramides` | `pirámide` | 98 | accented spelling 4,679 vs 98 |
| `policlinico` | `policlínico` | 98 | accented spelling 964 vs 98 |
| `septima` | `séptimo` | 98 | accented spelling 6,459 vs 98 |
| `turkmenistan` | `turkmenistán` | 98 | accented spelling 2,996 vs 98 |
| `existia` | `existir` | 98 | accented spelling 10,588 vs 98 |
| `rigido` | `rígido` | 98 | accented spelling 33,043 vs 98 |
| `ceramico` | `cerámico` | 98 | accented spelling 12,641 vs 98 |
| `galan` | `galán` | 98 | accented spelling 2,166 vs 98 |
| `redaccion` | `redacción` | 97 | accented spelling 37,855 vs 97 |
| `perdi` | `perder` | 97 | accented spelling 3,681 vs 97 |
| `orquideas` | `orquídea` | 97 | accented spelling 2,476 vs 97 |
| `tuvieramos` | `tener` | 97 | accented spelling 2,245 vs 97 |
| `haceis` | `hacer` | 97 | accented spelling 4,028 vs 97 |
| `cafarnaum` | `cafarnaúm` | 97 | accented spelling 812 vs 97 |
| `leidos` | `leer` | 97 | accented spelling 6,678 vs 97 |
| `proximas` | `próximo` | 97 | accented spelling 44,425 vs 97 |
| `corrupcion` | `corrupción` | 96 | accented spelling 60,777 vs 96 |
| `toco` | `tocar` | 96 | accented spelling 8,657 vs 96 |
| `tapon` | `tapón` | 96 | accented spelling 13,409 vs 96 |
| `anticipacion` | `anticipación` | 96 | accented spelling 66,333 vs 96 |
| `ojen` | `ojén` | 96 | accented spelling 512 vs 96 |
| `particion` | `partición` | 96 | accented spelling 26,563 vs 96 |
| `mastil` | `mástil` | 96 | accented spelling 10,986 vs 96 |
| `guarana` | `guaraná` | 96 | accented spelling 1,789 vs 96 |
| `mecanica` | `mecánico` | 96 | accented spelling 29,718 vs 96 |
| `combustion` | `combustión` | 96 | accented spelling 22,125 vs 96 |
| `ateismo` | `ateísmo` | 95 | accented spelling 2,262 vs 95 |
| `querubin` | `querubín` | 95 | accented spelling 4,879 vs 95 |
| `quintin` | `quintín` | 95 | accented spelling 622 vs 95 |
| `menciono` | `mencionar` | 95 | accented spelling 9,852 vs 95 |
| `natan` | `natán` | 95 | accented spelling 3,632 vs 95 |
| `tendreis` | `tener` | 95 | accented spelling 5,040 vs 95 |
| `cuauhtemoc` | `cuauhtémoc` | 95 | accented spelling 1,460 vs 95 |
| `jonico` | `jónico` | 95 | accented spelling 1,353 vs 95 |
| `etico` | `ético` | 95 | accented spelling 23,171 vs 95 |
| `escribi` | `escribir` | 95 | accented spelling 5,685 vs 95 |
| `afganistan` | `afganistán` | 95 | accented spelling 31,330 vs 95 |
| `celulas` | `célula` | 95 | accented spelling 105,312 vs 95 |
| `cronicas` | `crónica` | 94 | accented spelling 15,325 vs 94 |
| `respiracion` | `respiración` | 94 | accented spelling 42,876 vs 94 |
| `chiloe` | `chiloé` | 94 | accented spelling 1,582 vs 94 |
| `compresion` | `compresión` | 94 | accented spelling 47,898 vs 94 |
| `lesbico` | `lésbico` | 94 | accented spelling 1,946 vs 94 |
| `infografia` | `infografía` | 94 | accented spelling 9,961 vs 94 |
| `alumina` | `alúmina` | 94 | accented spelling 1,640 vs 94 |
| `curriculo` | `currículo` | 94 | accented spelling 12,407 vs 94 |
| `arabe` | `árabe` | 94 | accented spelling 67,600 vs 94 |
| `pilon` | `pilón` | 94 | accented spelling 1,047 vs 94 |
| `tachira` | `táchira` | 94 | accented spelling 902 vs 94 |
| `suscripcion` | `suscripción` | 93 | accented spelling 141,830 vs 93 |
| `futbolin` | `futbolín` | 93 | accented spelling 2,004 vs 93 |
| `bayamon` | `bayamón` | 93 | accented spelling 774 vs 93 |
| `hipodromo` | `hipódromo` | 93 | accented spelling 3,717 vs 93 |
| `hepatica` | `hepático` | 93 | accented spelling 7,424 vs 93 |
| `cantu` | `cantú` | 93 | accented spelling 466 vs 93 |
| `ecologia` | `ecología` | 93 | accented spelling 16,220 vs 93 |
| `bailen` | `bailén` | 93 | accented spelling 618 vs 93 |
| `didactico` | `didáctico` | 93 | accented spelling 15,274 vs 93 |
| `anonima` | `anónimo` | 93 | accented spelling 15,586 vs 93 |
| `intima` | `íntimo` | 93 | accented spelling 7,499 vs 93 |
| `vacias` | `vacío` | 93 | accented spelling 6,247 vs 93 |
| `paladin` | `paladín` | 93 | accented spelling 1,287 vs 93 |
| `politecnico` | `politécnico` | 93 | accented spelling 4,932 vs 93 |
| `revelacion` | `revelación` | 92 | accented spelling 42,062 vs 92 |
| `carrion` | `carrión` | 92 | accented spelling 1,690 vs 92 |
| `envios` | `envío` | 92 | accented spelling 37,458 vs 92 |
| `sintomas` | `síntoma` | 92 | accented spelling 124,477 vs 92 |
| `olvideis` | `olvidar` | 92 | accented spelling 1,394 vs 92 |
| `tipologia` | `tipología` | 92 | accented spelling 11,282 vs 92 |
| `absalon` | `absalón` | 92 | accented spelling 6,518 vs 92 |
| `hincapie` | `hincapié` | 92 | accented spelling 25,419 vs 92 |
| `glucagon` | `glucagón` | 91 | accented spelling 1,021 vs 91 |
| `anahuac` | `anáhuac` | 91 | accented spelling 792 vs 91 |
| `comence` | `comenzar` | 91 | accented spelling 9,454 vs 91 |
| `vestibulo` | `vestíbulo` | 91 | accented spelling 39,750 vs 91 |
| `metodos` | `método` | 91 | accented spelling 104,933 vs 91 |
| `lamina` | `lámina` | 91 | accented spelling 34,920 vs 91 |
| `emblematico` | `emblemático` | 91 | accented spelling 29,887 vs 91 |
| `circulacion` | `circulación` | 91 | accented spelling 68,044 vs 91 |
| `analogica` | `analógico` | 91 | accented spelling 4,500 vs 91 |
| `audifono` | `audífono` | 91 | accented spelling 15,514 vs 91 |
| `espectaculos` | `espectáculo` | 91 | accented spelling 23,910 vs 91 |
| `exhibicion` | `exhibición` | 90 | accented spelling 59,342 vs 90 |
| `nijar` | `níjar` | 90 | accented spelling 610 vs 90 |
| `exploracion` | `exploración` | 90 | accented spelling 58,812 vs 90 |
| `cervix` | `cérvix` | 90 | accented spelling 1,612 vs 90 |
| `israeli` | `israelí` | 90 | accented spelling 35,156 vs 90 |
| `cienaga` | `ciénaga` | 90 | accented spelling 1,436 vs 90 |
| `ganaderia` | `ganadería` | 90 | accented spelling 11,437 vs 90 |
| `biologica` | `biológico` | 90 | accented spelling 13,900 vs 90 |
| `sanacion` | `sanación` | 90 | accented spelling 22,997 vs 90 |
| `peten` | `petén` | 90 | accented spelling 1,100 vs 90 |
| `encia` | `encía` | 90 | accented spelling 12,298 vs 90 |
| `venian` | `venir` | 90 | accented spelling 5,668 vs 90 |
| `tipicas` | `típico` | 90 | accented spelling 9,925 vs 90 |
| `tripode` | `trípode` | 90 | accented spelling 9,160 vs 90 |
| `tipica` | `típico` | 89 | accented spelling 18,513 vs 89 |
| `tabula` | `tábula` | 89 | accented spelling 633 vs 89 |
| `yasuni` | `yasuní` | 89 | accented spelling 748 vs 89 |
| `actue` | `actuar` | 89 | accented spelling 5,213 vs 89 |
| `panoramico` | `panorámico` | 89 | accented spelling 40,702 vs 89 |
| `apareceran` | `aparecer` | 89 | accented spelling 8,442 vs 89 |
| `egoista` | `egoísta` | 89 | accented spelling 11,944 vs 89 |
| `persecucion` | `persecución` | 89 | accented spelling 30,064 vs 89 |
| `historicas` | `histórico` | 89 | accented spelling 13,561 vs 89 |
| `cantico` | `cántico` | 89 | accented spelling 4,858 vs 89 |
| `oira` | `oír` | 89 | accented spelling 1,594 vs 89 |
| `vudu` | `vudú` | 88 | accented spelling 1,149 vs 88 |
| `citrico` | `cítrico` | 88 | accented spelling 11,312 vs 88 |
| `mispa` | `mispá` | 88 | accented spelling 712 vs 88 |
| `panico` | `pánico` | 88 | accented spelling 19,971 vs 88 |
| `erroneo` | `erróneo` | 88 | accented spelling 18,164 vs 88 |
| `mazarron` | `mazarrón` | 88 | accented spelling 2,628 vs 88 |
| `lengueta` | `lengüeta` | 88 | accented spelling 6,213 vs 88 |
| `halcon` | `halcón` | 88 | accented spelling 5,871 vs 88 |
| `axarquia` | `axarquía` | 88 | accented spelling 1,013 vs 88 |
| `nacar` | `nácar` | 88 | accented spelling 2,061 vs 88 |
| `ademas` | `además` | 88 | accented spelling 1,504,690 vs 88 |
| `subscribete` | `suscribirse` | 88 | accented spelling 5,384 vs 88 |
| `champu` | `champú` | 88 | accented spelling 21,519 vs 88 |
| `anecdota` | `anécdota` | 87 | accented spelling 6,340 vs 87 |
| `crie` | `criar` | 87 | accented spelling 626 vs 87 |
| `cadi` | `cadí` | 87 | accented spelling 552 vs 87 |
| `artisticas` | `artístico` | 87 | accented spelling 11,219 vs 87 |
| `estara` | `estar` | 87 | accented spelling 108,576 vs 87 |
| `seguia` | `seguir` | 87 | accented spelling 11,526 vs 87 |
| `determinacion` | `determinación` | 87 | accented spelling 56,136 vs 87 |
| `calificacion` | `calificación` | 87 | accented spelling 87,318 vs 87 |
| `resolucion` | `resolución` | 87 | accented spelling 211,553 vs 87 |
| `peron` | `perón` | 87 | accented spelling 1,424 vs 87 |
| `odontologico` | `odontológico` | 87 | accented spelling 3,512 vs 87 |
| `subio` | `subir` | 87 | accented spelling 14,782 vs 87 |
| `ojala` | `ojalá` | 87 | accented spelling 12,513 vs 87 |
| `nurburgring` | `nürburgring` | 87 | accented spelling 740 vs 87 |
| `dominacion` | `dominación` | 87 | accented spelling 13,061 vs 87 |
| `heroina` | `heroína` | 86 | accented spelling 9,701 vs 86 |
| `purificacion` | `purificación` | 86 | accented spelling 18,886 vs 86 |
| `palamos` | `palamós` | 86 | accented spelling 1,694 vs 86 |
| `clitoris` | `clítoris` | 86 | accented spelling 5,764 vs 86 |
| `mataro` | `mataró` | 86 | accented spelling 2,882 vs 86 |
| `lerida` | `lérida` | 86 | accented spelling 1,382 vs 86 |
| `confio` | `confiar` | 86 | accented spelling 5,453 vs 86 |
| `cumplio` | `cumplir` | 86 | accented spelling 5,916 vs 86 |
| `cortes` | `cortés` | 86 | accented spelling 10,061 vs 86 |
| `carillon` | `carillón` | 86 | accented spelling 646 vs 86 |
| `difusion` | `difusión` | 86 | accented spelling 68,375 vs 86 |
| `cancerigenas` | `cancerígeno` | 85 | accented spelling 1,677 vs 85 |
| `lubricacion` | `lubricación` | 85 | accented spelling 17,934 vs 85 |
| `minimamente` | `mínimamente` | 85 | accented spelling 5,981 vs 85 |
| `abas` | `abás` | 85 | accented spelling 542 vs 85 |
| `codigos` | `código` | 85 | accented spelling 41,680 vs 85 |
| `caracteristico` | `característico` | 85 | accented spelling 24,087 vs 85 |
| `jurisdiccion` | `jurisdicción` | 85 | accented spelling 63,818 vs 85 |
| `mesia` | `mesías` | 85 | accented spelling 471 vs 85 |
| `biceps` | `bíceps` | 85 | accented spelling 2,023 vs 85 |
| `traian` | `traer` | 85 | accented spelling 1,546 vs 85 |
| `regulacion` | `regulación` | 85 | accented spelling 84,799 vs 85 |
| `antibiotico` | `antibiótico` | 85 | accented spelling 25,203 vs 85 |
| `tentacion` | `tentación` | 85 | accented spelling 21,176 vs 85 |
| `fanatico` | `fanático` | 85 | accented spelling 18,630 vs 85 |
| `rendon` | `rendón` | 85 | accented spelling 490 vs 85 |
| `navio` | `navío` | 85 | accented spelling 4,332 vs 85 |
| `contaminacion` | `contaminación` | 85 | accented spelling 89,919 vs 85 |
| `anfora` | `ánfora` | 85 | accented spelling 785 vs 85 |
| `chernobil` | `chernóbil` | 85 | accented spelling 978 vs 85 |
| `sumate` | `sumarse` | 84 | accented spelling 776 vs 84 |
| `enviame` | `enviar` | 84 | accented spelling 1,449 vs 84 |
| `ionica` | `iónico` | 84 | accented spelling 736 vs 84 |
| `serafin` | `serafín` | 84 | accented spelling 1,714 vs 84 |
| `griferia` | `grifería` | 84 | accented spelling 6,393 vs 84 |
| `consegui` | `conseguir` | 84 | accented spelling 3,694 vs 84 |
| `catedra` | `cátedra` | 84 | accented spelling 9,006 vs 84 |
| `afin` | `afín` | 84 | accented spelling 1,998 vs 84 |
| `tabu` | `tabú` | 84 | accented spelling 4,751 vs 84 |
| `chiriqui` | `chiriquí` | 84 | accented spelling 1,182 vs 84 |
| `elastica` | `elástico` | 83 | accented spelling 10,929 vs 83 |
| `climatizacion` | `climatización` | 83 | accented spelling 21,210 vs 83 |
| `veais` | `ver` | 83 | accented spelling 1,495 vs 83 |
| `quimicas` | `químico` | 83 | accented spelling 20,109 vs 83 |
| `erosion` | `erosión` | 83 | accented spelling 15,491 vs 83 |
| `eyaculacion` | `eyaculación` | 83 | accented spelling 6,767 vs 83 |
| `teologia` | `teología` | 83 | accented spelling 18,328 vs 83 |
| `planeacion` | `planeación` | 83 | accented spelling 11,394 vs 83 |
| `pichon` | `pichón` | 83 | accented spelling 1,164 vs 83 |
| `laban` | `labán` | 83 | accented spelling 6,050 vs 83 |
| `fueramos` | `ir` | 83 | accented spelling 1,849 vs 83 |
| `albumina` | `albúmina` | 83 | accented spelling 1,796 vs 83 |
| `serrania` | `serranía` | 83 | accented spelling 1,869 vs 83 |
| `gutierrez` | `gutiérrez` | 83 | accented spelling 12,360 vs 83 |
| `higienico` | `higiénico` | 83 | accented spelling 20,025 vs 83 |
| `chillon` | `chillón` | 82 | accented spelling 857 vs 82 |
| `platon` | `platón` | 82 | accented spelling 3,971 vs 82 |
| `expedicion` | `expedición` | 82 | accented spelling 33,806 vs 82 |
| `creeis` | `creer` | 82 | accented spelling 2,574 vs 82 |
| `encarnacion` | `encarnación` | 82 | accented spelling 14,349 vs 82 |
| `sauco` | `saúco` | 82 | accented spelling 871 vs 82 |
| `esteis` | `estar` | 82 | accented spelling 2,595 vs 82 |
| `ravena` | `rávena` | 82 | accented spelling 1,318 vs 82 |
| `orbita` | `órbita` | 82 | accented spelling 18,111 vs 82 |
| `escandalo` | `escándalo` | 82 | accented spelling 17,400 vs 82 |
| `autorizo` | `autorizar` | 82 | accented spelling 2,043 vs 82 |
| `vibracion` | `vibración` | 82 | accented spelling 44,252 vs 82 |
| `extraida` | `extraer` | 82 | accented spelling 2,075 vs 82 |
| `seais` | `ser` | 82 | accented spelling 4,772 vs 82 |
| `tripulacion` | `tripulación` | 82 | accented spelling 28,642 vs 82 |
| `laton` | `latón` | 82 | accented spelling 29,905 vs 82 |
| `florez` | `flórez` | 82 | accented spelling 586 vs 82 |
| `caqueta` | `caquetá` | 82 | accented spelling 674 vs 82 |
| `mecanicas` | `mecánico` | 82 | accented spelling 10,810 vs 82 |
| `najera` | `nájera` | 81 | accented spelling 802 vs 81 |
| `wurzburg` | `würzburg` | 81 | accented spelling 564 vs 81 |
| `submenu` | `submenú` | 81 | accented spelling 2,135 vs 81 |
| `paraiba` | `paraíba` | 81 | accented spelling 500 vs 81 |
| `promocion` | `promoción` | 81 | accented spelling 206,981 vs 81 |
| `historicamente` | `históricamente` | 81 | accented spelling 17,138 vs 81 |
| `manifestacion` | `manifestación` | 81 | accented spelling 56,647 vs 81 |
| `ammon` | `ammón` | 81 | accented spelling 1,948 vs 81 |
| `alcorcon` | `alcorcón` | 81 | accented spelling 1,628 vs 81 |
| `estevez` | `estévez` | 81 | accented spelling 636 vs 81 |
| `judaismo` | `judaísmo` | 81 | accented spelling 7,019 vs 81 |
| `aleksei` | `alekséi` | 81 | accented spelling 442 vs 81 |
| `vivira` | `vivir` | 81 | accented spelling 5,372 vs 81 |
| `negueb` | `négueb` | 81 | accented spelling 606 vs 81 |
| `mejoria` | `mejoría` | 81 | accented spelling 13,413 vs 81 |
| `alla` | `allá` | 81 | accented spelling 249,823 vs 81 |
| `melendez` | `meléndez` | 81 | accented spelling 962 vs 81 |
| `martir` | `mártir` | 81 | accented spelling 8,952 vs 81 |
| `murcielago` | `murciélago` | 81 | accented spelling 5,716 vs 81 |
| `afiliacion` | `afiliación` | 80 | accented spelling 22,392 vs 80 |
| `hipotesis` | `hipótesis` | 80 | accented spelling 29,643 vs 80 |
| `volveria` | `volver` | 80 | accented spelling 4,459 vs 80 |
| `taxon` | `taxón` | 80 | accented spelling 1,046 vs 80 |
| `henriquez` | `henríquez` | 80 | accented spelling 722 vs 80 |
| `atletica` | `atlético` | 80 | accented spelling 1,227 vs 80 |
| `en-linea` | `en línea` | 80 | accented spelling 859 vs 80 |
| `popurri` | `popurrí` | 80 | accented spelling 498 vs 80 |
| `ofreciendol` | `ofrecer` | 80 | accented spelling 1,920 vs 80 |
| `valida` | `válido` | 80 | accented spelling 27,445 vs 80 |
| `tepoztlan` | `tepoztlán` | 80 | accented spelling 674 vs 80 |
| `hipolito` | `hipólito` | 80 | accented spelling 852 vs 80 |
| `criquet` | `críquet` | 80 | accented spelling 1,794 vs 80 |
| `tampon` | `tampón` | 80 | accented spelling 4,128 vs 80 |
| `topico` | `tópico` | 80 | accented spelling 11,758 vs 80 |
| `atraido` | `atraer` | 79 | accented spelling 5,195 vs 79 |
| `benicarlo` | `benicarló` | 79 | accented spelling 1,254 vs 79 |
| `cocteles` | `cóctel` | 79 | accented spelling 10,793 vs 79 |
| `fistula` | `fístula` | 79 | accented spelling 2,307 vs 79 |
| `agradecele` | `agradecer` | 79 | accented spelling 900 vs 79 |
| `sarapiqui` | `sarapiquí` | 79 | accented spelling 424 vs 79 |
| `pildora` | `píldora` | 79 | accented spelling 32,214 vs 79 |
| `manabi` | `manabí` | 79 | accented spelling 1,924 vs 79 |
| `kurfurstendamm` | `kurfürstendamm` | 79 | accented spelling 1,138 vs 79 |
| `conyuge` | `cónyuge` | 78 | accented spelling 28,223 vs 78 |
| `explotacion` | `explotación` | 78 | accented spelling 112,285 vs 78 |
| `adis` | `adís` | 78 | accented spelling 7,150 vs 78 |
| `carpinterias` | `carpintería` | 78 | accented spelling 524 vs 78 |
| `establecio` | `establecer` | 78 | accented spelling 16,001 vs 78 |
| `etnico` | `étnico` | 78 | accented spelling 25,217 vs 78 |
| `medicion` | `medición` | 78 | accented spelling 140,869 vs 78 |
| `volveran` | `volver` | 78 | accented spelling 4,884 vs 78 |
| `nagueles` | `nagüeles` | 78 | accented spelling 524 vs 78 |
| `porcelanico` | `porcelánico` | 78 | accented spelling 3,236 vs 78 |
| `penedes` | `penedés` | 78 | accented spelling 720 vs 78 |
| `musulman` | `musulmán` | 78 | accented spelling 37,487 vs 78 |
| `atalia` | `atalía` | 78 | accented spelling 999 vs 78 |
| `omoplato` | `omóplato` | 78 | accented spelling 761 vs 78 |
| `caia` | `caer` | 77 | accented spelling 2,510 vs 77 |
| `nordico` | `nórdico` | 77 | accented spelling 8,719 vs 77 |
| `probo` | `probar` | 77 | accented spelling 3,161 vs 77 |
| `asesorias` | `asesoría` | 77 | accented spelling 1,579 vs 77 |
| `mamifero` | `mamífero` | 77 | accented spelling 8,986 vs 77 |
| `jalon` | `jalón` | 77 | accented spelling 1,352 vs 77 |
| `fragil` | `frágil` | 77 | accented spelling 18,534 vs 77 |
| `mostoles` | `móstoles` | 77 | accented spelling 1,412 vs 77 |
| `jugue` | `jugar` | 77 | accented spelling 934 vs 77 |
| `camerun` | `camerún` | 77 | accented spelling 8,958 vs 77 |
| `autoria` | `autoría` | 77 | accented spelling 8,958 vs 77 |
| `solucion` | `solución` | 77 | accented spelling 719,824 vs 77 |
| `pedasi` | `pedasí` | 77 | accented spelling 398 vs 77 |
| `anatomia` | `anatomía` | 77 | accented spelling 14,039 vs 77 |
| `craneo` | `cráneo` | 77 | accented spelling 17,722 vs 77 |
| `discrecion` | `discreción` | 77 | accented spelling 59,389 vs 77 |
| `programo` | `programar` | 77 | accented spelling 859 vs 77 |
| `prometio` | `prometer` | 77 | accented spelling 7,848 vs 77 |
| `tellez` | `téllez` | 76 | accented spelling 440 vs 76 |
| `osnabruck` | `osnabrück` | 76 | accented spelling 800 vs 76 |
| `gastronomico` | `gastronómico` | 76 | accented spelling 28,245 vs 76 |
| `patin` | `patín` | 76 | accented spelling 2,256 vs 76 |
| `capto` | `captar` | 76 | accented spelling 960 vs 76 |
| `champan` | `champán` | 76 | accented spelling 7,857 vs 76 |
| `neutron` | `neutrón` | 76 | accented spelling 2,599 vs 76 |
| `tesalonica` | `tesalónica` | 76 | accented spelling 3,696 vs 76 |
| `capitulos` | `capítulo` | 76 | accented spelling 12,839 vs 76 |
| `quejo` | `quejar` | 76 | accented spelling 1,091 vs 76 |
| `tactica` | `táctica` | 76 | accented spelling 15,376 vs 76 |
| `debeis` | `deber` | 76 | accented spelling 4,933 vs 76 |
| `etiopia` | `etiopía` | 76 | accented spelling 14,470 vs 76 |
| `expres` | `exprés` | 76 | accented spelling 11,527 vs 76 |
| `antelacion` | `antelación` | 76 | accented spelling 61,184 vs 76 |
| `barbaro` | `bárbaro` | 76 | accented spelling 4,017 vs 76 |
| `restriccion` | `restricción` | 76 | accented spelling 77,641 vs 76 |
| `conclave` | `cónclave` | 76 | accented spelling 2,196 vs 76 |
| `tarapaca` | `tarapacá` | 75 | accented spelling 748 vs 75 |
| `colageno` | `colágeno` | 75 | accented spelling 19,608 vs 75 |
| `aligator` | `aligátor` | 75 | accented spelling 491 vs 75 |
| `facturacion` | `facturación` | 75 | accented spelling 56,939 vs 75 |
| `egoismo` | `egoísmo` | 75 | accented spelling 11,738 vs 75 |
| `amazonico` | `amazónico` | 75 | accented spelling 5,296 vs 75 |
| `fluctuan` | `fluctuar` | 75 | accented spelling 536 vs 75 |
| `logistico` | `logístico` | 75 | accented spelling 18,314 vs 75 |
| `tipografia` | `tipografía` | 75 | accented spelling 8,304 vs 75 |
| `picon` | `picón` | 75 | accented spelling 442 vs 75 |
| `genetico` | `genético` | 75 | accented spelling 31,085 vs 75 |
| `antiguedades` | `antigüedad` | 75 | accented spelling 6,833 vs 75 |
| `maipu` | `maipú` | 75 | accented spelling 750 vs 75 |
| `sanguinea` | `sanguíneo` | 75 | accented spelling 8,508 vs 75 |
| `increibles` | `increíble` | 75 | accented spelling 36,032 vs 75 |
| `intimamente` | `íntimamente` | 74 | accented spelling 6,644 vs 74 |
| `sinfonia` | `sinfonía` | 74 | accented spelling 4,944 vs 74 |
| `magnetica` | `magnético` | 74 | accented spelling 13,706 vs 74 |
| `esteli` | `estelí` | 74 | accented spelling 912 vs 74 |
| `reves` | `revés` | 74 | accented spelling 17,308 vs 74 |
| `retractil` | `retráctil` | 74 | accented spelling 6,890 vs 74 |
| `ofrecera` | `ofrecer` | 74 | accented spelling 19,054 vs 74 |
| `jerarquia` | `jerarquía` | 74 | accented spelling 19,246 vs 74 |
| `adopcion` | `adopción` | 74 | accented spelling 61,083 vs 74 |
| `hipico` | `hípico` | 74 | accented spelling 1,518 vs 74 |
| `partia` | `partir` | 74 | accented spelling 692 vs 74 |
| `sorprendio` | `sorprender` | 74 | accented spelling 6,976 vs 74 |
| `simbolos` | `símbolo` | 73 | accented spelling 26,932 vs 73 |
| `pirolisis` | `pirólisis` | 73 | accented spelling 1,658 vs 73 |
| `marañon` | `marañón` | 73 | accented spelling 922 vs 73 |
| `versatil` | `versátil` | 73 | accented spelling 41,662 vs 73 |
| `inflacion` | `inflación` | 73 | accented spelling 33,468 vs 73 |
| `vibora` | `víbora` | 73 | accented spelling 2,209 vs 73 |
| `calidas` | `cálido` | 73 | accented spelling 5,463 vs 73 |
| `hagais` | `hacer` | 73 | accented spelling 3,163 vs 73 |
| `calcomania` | `calcomanía` | 73 | accented spelling 2,465 vs 73 |
| `admision` | `admisión` | 73 | accented spelling 38,929 vs 73 |
| `dandol` | `dar` | 73 | accented spelling 1,701 vs 73 |
| `mitico` | `mítico` | 73 | accented spelling 12,881 vs 73 |
| `liquidacion` | `liquidación` | 73 | accented spelling 19,674 vs 73 |
| `atun` | `atún` | 73 | accented spelling 12,234 vs 73 |
| `democratico` | `democrático` | 73 | accented spelling 45,088 vs 73 |
| `yazidi` | `yazidí` | 73 | accented spelling 369 vs 73 |
| `alienigena` | `alienígena` | 72 | accented spelling 8,139 vs 72 |
| `erronea` | `erróneo` | 72 | accented spelling 6,114 vs 72 |
| `estuvieramos` | `estar` | 72 | accented spelling 1,634 vs 72 |
| `edificacion` | `edificación` | 72 | accented spelling 21,741 vs 72 |
| `espatula` | `espátula` | 72 | accented spelling 5,585 vs 72 |
| `surgio` | `surgir` | 72 | accented spelling 13,014 vs 72 |
| `azaria` | `azaría` | 72 | accented spelling 1,496 vs 72 |
| `siguio` | `seguir` | 72 | accented spelling 19,789 vs 72 |
| `llamano` | `llamar` | 72 | accented spelling 1,172 vs 72 |
| `inscribete` | `inscribir` | 72 | accented spelling 19,296 vs 72 |
| `habran` | `haber` | 72 | accented spelling 7,153 vs 72 |
| `kluber` | `klüber` | 72 | accented spelling 432 vs 72 |
| `calendula` | `caléndula` | 72 | accented spelling 1,673 vs 72 |
| `correccion` | `corrección` | 72 | accented spelling 57,993 vs 72 |
| `cuadriceps` | `cuádriceps` | 72 | accented spelling 1,020 vs 72 |
| `estimulacion` | `estimulación` | 72 | accented spelling 19,229 vs 72 |
| `geografica` | `geográfico` | 72 | accented spelling 18,240 vs 72 |
| `periferico` | `periférico` | 72 | accented spelling 15,166 vs 72 |
| `oceanico` | `oceánico` | 72 | accented spelling 5,435 vs 72 |
| `bazan` | `bazán` | 72 | accented spelling 448 vs 72 |
| `mencion` | `mención` | 72 | accented spelling 25,982 vs 72 |
| `nescafe` | `nescafé` | 72 | accented spelling 820 vs 72 |
| `getsemani` | `getsemaní` | 72 | accented spelling 2,566 vs 72 |
| `traidos` | `traer` | 72 | accented spelling 2,061 vs 72 |
| `demostracion` | `demostración` | 72 | accented spelling 40,950 vs 72 |
| `ultimatum` | `ultimátum` | 72 | accented spelling 1,449 vs 72 |
| `tulipan` | `tulipán` | 71 | accented spelling 2,775 vs 71 |
| `creian` | `creer` | 71 | accented spelling 5,668 vs 71 |
| `herreria` | `herrería` | 71 | accented spelling 1,583 vs 71 |
| `dinastia` | `dinastía` | 71 | accented spelling 12,971 vs 71 |
| `soberania` | `soberanía` | 71 | accented spelling 25,760 vs 71 |
| `afan` | `afán` | 71 | accented spelling 9,018 vs 71 |
| `minimo` | `mínimo` | 71 | accented spelling 298,768 vs 71 |
| `crei` | `creer` | 71 | accented spelling 2,307 vs 71 |
| `eroticas` | `erótico` | 71 | accented spelling 1,655 vs 71 |
| `berlin-tegel` | `berlín-tegel` | 71 | accented spelling 1,558 vs 71 |
| `dramaticas` | `dramático` | 71 | accented spelling 1,788 vs 71 |
| `diocesis` | `diócesis` | 71 | accented spelling 23,663 vs 71 |
| `logico` | `lógico` | 71 | accented spelling 33,606 vs 71 |
| `britanica` | `británico` | 71 | accented spelling 22,903 vs 71 |
| `jerico` | `jericó` | 70 | accented spelling 7,722 vs 70 |
| `sirvio` | `servir` | 70 | accented spelling 10,987 vs 70 |
| `araucania` | `araucanía` | 70 | accented spelling 1,326 vs 70 |
| `dudeis` | `dudar` | 70 | accented spelling 1,015 vs 70 |
| `elegi` | `elegir` | 70 | accented spelling 4,930 vs 70 |
| `purpura` | `púrpura` | 70 | accented spelling 25,536 vs 70 |
| `querria` | `querer` | 70 | accented spelling 3,669 vs 70 |
| `plasticos` | `plástico` | 70 | accented spelling 19,557 vs 70 |
| `arcen` | `arcén` | 70 | accented spelling 541 vs 70 |
| `democratica` | `democrático` | 70 | accented spelling 15,309 vs 70 |
| `devocion` | `devoción` | 70 | accented spelling 17,836 vs 70 |
| `reconstruccion` | `reconstrucción` | 70 | accented spelling 38,569 vs 70 |
| `desearia` | `desear` | 70 | accented spelling 4,281 vs 70 |
| `predestino` | `predestinar` | 70 | accented spelling 390 vs 70 |
| `ataco` | `atacar` | 70 | accented spelling 4,201 vs 70 |
| `guaido` | `guaidó` | 70 | accented spelling 2,890 vs 70 |
| `buhler` | `bühler` | 70 | accented spelling 1,048 vs 70 |
| `compilacion` | `compilación` | 70 | accented spelling 15,469 vs 70 |
| `convertira` | `convertir` | 70 | accented spelling 10,522 vs 70 |
| `mandibula` | `mandíbula` | 70 | accented spelling 14,182 vs 70 |
| `patologia` | `patología` | 70 | accented spelling 20,898 vs 70 |
| `sarin` | `sarín` | 70 | accented spelling 574 vs 70 |
| `crecio` | `crecer` | 70 | accented spelling 14,422 vs 70 |
| `esteril` | `estéril` | 70 | accented spelling 11,485 vs 70 |
| `subtitulos` | `subtítulo` | 69 | accented spelling 9,249 vs 69 |
| `organica` | `orgánico` | 69 | accented spelling 23,141 vs 69 |
| `suni` | `suní` | 69 | accented spelling 898 vs 69 |
| `arbol` | `árbol` | 69 | accented spelling 189,711 vs 69 |
| `hialuronico` | `hialurónico` | 69 | accented spelling 8,108 vs 69 |
| `maximo` | `máximo` | 69 | accented spelling 515,774 vs 69 |
| `psicologo` | `psicólogo` | 69 | accented spelling 12,092 vs 69 |
| `filtracion` | `filtración` | 69 | accented spelling 24,776 vs 69 |
| `miquelon` | `miquelón` | 69 | accented spelling 1,134 vs 69 |
| `afirmacion` | `afirmación` | 69 | accented spelling 32,581 vs 69 |
| `disminucion` | `disminución` | 69 | accented spelling 64,301 vs 69 |
| `seguiran` | `seguir` | 69 | accented spelling 11,384 vs 69 |
| `iniciacion` | `iniciación` | 69 | accented spelling 16,689 vs 69 |
| `teofilo` | `teófilo` | 69 | accented spelling 962 vs 69 |
| `intimos` | `íntimo` | 68 | accented spelling 3,284 vs 68 |
| `remocion` | `remoción` | 68 | accented spelling 10,021 vs 68 |
| `sabras` | `saber` | 68 | accented spelling 23,826 vs 68 |
| `canonica` | `canónico` | 68 | accented spelling 1,139 vs 68 |
| `popocatepetl` | `popocatépetl` | 68 | accented spelling 348 vs 68 |
| `montgri` | `montgrí` | 68 | accented spelling 874 vs 68 |
| `fotografa` | `fotógrafa` | 68 | accented spelling 4,920 vs 68 |
| `padme` | `padmé` | 68 | accented spelling 626 vs 68 |
| `crimenes` | `crimen` | 68 | accented spelling 21,281 vs 68 |
| `utiles` | `útil` | 68 | accented spelling 61,734 vs 68 |
| `pakistani` | `pakistaní` | 68 | accented spelling 2,225 vs 68 |
| `garzon` | `garzón` | 68 | accented spelling 1,535 vs 68 |
| `yañez` | `yáñez` | 68 | accented spelling 392 vs 68 |
| `audioguia` | `audioguía` | 68 | accented spelling 3,100 vs 68 |
| `iliada` | `ilíada` | 68 | accented spelling 494 vs 68 |
| `conocio` | `conocer` | 68 | accented spelling 10,729 vs 68 |
| `ecija` | `écija` | 68 | accented spelling 748 vs 68 |
| `nepali` | `nepalí` | 68 | accented spelling 1,462 vs 68 |
| `dagon` | `dagón` | 68 | accented spelling 916 vs 68 |
| `heroe` | `héroe` | 68 | accented spelling 54,196 vs 68 |
| `curacion` | `curación` | 68 | accented spelling 33,648 vs 68 |
| `servira` | `servir` | 68 | accented spelling 10,033 vs 68 |
| `redencion` | `redención` | 67 | accented spelling 16,000 vs 67 |
| `contruccion` | `construcción` | 67 | accented spelling 468 vs 67 |
| `olia` | `oler` | 67 | accented spelling 976 vs 67 |
| `anomalia` | `anomalía` | 67 | accented spelling 14,371 vs 67 |
| `rogue#royal` | `rogar` | 67 | accented spelling 352 vs 67 |
| `refierase` | `referirse` | 67 | accented spelling 3,224 vs 67 |
| `rectangulo` | `rectángulo` | 67 | accented spelling 13,849 vs 67 |
| `sofreir` | `sofreír` | 67 | accented spelling 2,024 vs 67 |
| `escalon` | `escalón` | 67 | accented spelling 4,314 vs 67 |
| `efectue` | `efectuar` | 67 | accented spelling 2,686 vs 67 |
| `diafana` | `diáfano` | 67 | accented spelling 957 vs 67 |
| `coreografia` | `coreografía` | 67 | accented spelling 4,524 vs 67 |
| `videografo` | `videógrafo` | 67 | accented spelling 521 vs 67 |
| `permanecera` | `permanecer` | 67 | accented spelling 9,494 vs 67 |
| `mitica` | `mítico` | 67 | accented spelling 3,259 vs 67 |
| `dormi` | `dormir` | 67 | accented spelling 874 vs 67 |
| `calibracion` | `calibración` | 67 | accented spelling 23,537 vs 67 |
| `brocoli` | `brócoli` | 67 | accented spelling 6,486 vs 67 |
| `sabiamos` | `saber` | 67 | accented spelling 5,209 vs 67 |
| `pensabamos` | `pensar` | 67 | accented spelling 1,456 vs 67 |
| `pequeñin` | `pequeñín` | 67 | accented spelling 387 vs 67 |
| `pulmon` | `pulmón` | 67 | accented spelling 42,709 vs 67 |
| `contactenos` | `contactar` | 67 | accented spelling 17,614 vs 67 |
| `sabia` | `saber` | 66 | accented spelling 44,359 vs 66 |
| `penso` | `pensar` | 66 | accented spelling 11,665 vs 66 |
| `extasis` | `éxtasis` | 66 | accented spelling 6,662 vs 66 |
| `subscribase` | `suscribir` | 66 | accented spelling 372 vs 66 |
| `clasicas` | `clásico` | 66 | accented spelling 10,751 vs 66 |
| `petalo` | `pétalo` | 66 | accented spelling 5,586 vs 66 |
| `amsterdam-schiphol` | `ámsterdam-schiphol` | 66 | accented spelling 582 vs 66 |
| `pornografia` | `pornografía` | 66 | accented spelling 13,778 vs 66 |
| `minima` | `mínimo` | 66 | accented spelling 52,575 vs 66 |
| `cronografo` | `cronógrafo` | 66 | accented spelling 12,441 vs 66 |
| `emision` | `emisión` | 66 | accented spelling 112,868 vs 66 |
| `arevalo` | `arévalo` | 66 | accented spelling 1,040 vs 66 |
| `implantologia` | `implantología` | 66 | accented spelling 1,685 vs 66 |
| `bariatrica` | `bariátrico` | 66 | accented spelling 2,016 vs 66 |
| `descubrio` | `descubrir` | 66 | accented spelling 17,598 vs 66 |
| `exitos` | `éxito` | 66 | accented spelling 13,648 vs 66 |
| `incredulo` | `incrédulo` | 65 | accented spelling 4,697 vs 65 |
| `gascon` | `gascón` | 65 | accented spelling 506 vs 65 |
| `problematica` | `problemática` | 65 | accented spelling 18,753 vs 65 |
| `arrojo` | `arrojar` | 65 | accented spelling 3,676 vs 65 |
| `diplomatico` | `diplomático` | 65 | accented spelling 23,542 vs 65 |
| `percepcion` | `percepción` | 65 | accented spelling 61,074 vs 65 |
| `denominacion` | `denominación` | 65 | accented spelling 29,813 vs 65 |
| `depilacion` | `depilación` | 65 | accented spelling 8,472 vs 65 |
| `patina` | `pátina` | 65 | accented spelling 2,405 vs 65 |
| `unto` | `untar` | 65 | accented spelling 358 vs 65 |
| `romulo` | `rómulo` | 65 | accented spelling 982 vs 65 |
| `triatlon` | `triatlón` | 65 | accented spelling 6,782 vs 65 |
| `dedan` | `dedán` | 65 | accented spelling 344 vs 65 |
| `minimos` | `mínimo` | 65 | accented spelling 15,668 vs 65 |
| `deportacion` | `deportación` | 65 | accented spelling 14,517 vs 65 |
| `masturbacion` | `masturbación` | 65 | accented spelling 5,916 vs 65 |
| `unicamente` | `únicamente` | 65 | accented spelling 161,030 vs 65 |
| `administracion` | `administración` | 65 | accented spelling 326,961 vs 65 |
| `inmunologico` | `inmunológico` | 64 | accented spelling 23,266 vs 64 |
| `fundicion` | `fundición` | 64 | accented spelling 25,992 vs 64 |
| `estupido` | `estúpido` | 64 | accented spelling 8,811 vs 64 |
| `emulsion` | `emulsión` | 64 | accented spelling 4,313 vs 64 |
| `siriaco` | `siríaco` | 64 | accented spelling 365 vs 64 |
| `vagon` | `vagón` | 64 | accented spelling 6,629 vs 64 |
| `desinfeccion` | `desinfección` | 64 | accented spelling 12,197 vs 64 |
| `complexion` | `complexión` | 64 | accented spelling 1,319 vs 64 |
| `bovedas` | `bóveda` | 64 | accented spelling 2,525 vs 64 |
| `padron` | `padrón` | 64 | accented spelling 3,521 vs 64 |
| `obtencion` | `obtención` | 64 | accented spelling 46,856 vs 64 |
| `horreo` | `hórreo` | 64 | accented spelling 426 vs 64 |
| `taliban` | `talibán` | 64 | accented spelling 4,813 vs 64 |
| `rabida` | `rábida` | 64 | accented spelling 429 vs 64 |
| `fundacio` | `fundació` | 64 | accented spelling 4,360 vs 64 |
| `alcaldia` | `alcaldía` | 64 | accented spelling 7,674 vs 64 |
| `matematico` | `matemático` | 64 | accented spelling 15,379 vs 64 |
| `dramatico` | `dramático` | 64 | accented spelling 18,505 vs 64 |
| `sintonia` | `sintonía` | 64 | accented spelling 9,471 vs 64 |
| `manati` | `manatí` | 63 | accented spelling 1,146 vs 63 |
| `buzon` | `buzón` | 63 | accented spelling 22,926 vs 63 |
| `autentica` | `auténtico` | 63 | accented spelling 20,557 vs 63 |
| `lanus` | `lanús` | 63 | accented spelling 412 vs 63 |
| `estiercol` | `estiércol` | 63 | accented spelling 6,616 vs 63 |
| `intrusion` | `intrusión` | 63 | accented spelling 5,606 vs 63 |
| `agrupacion` | `agrupación` | 63 | accented spelling 18,950 vs 63 |
| `alergeno` | `alérgeno` | 63 | accented spelling 5,936 vs 63 |
| `adiccion` | `adicción` | 63 | accented spelling 21,488 vs 63 |
| `vocacion` | `vocación` | 63 | accented spelling 32,131 vs 63 |
| `empatia` | `empatía` | 63 | accented spelling 11,597 vs 63 |
| `efectuan` | `efectuar` | 63 | accented spelling 2,193 vs 63 |
| `benares` | `benarés` | 63 | accented spelling 664 vs 63 |
| `echeverria` | `echeverría` | 63 | accented spelling 858 vs 63 |
| `corcega` | `córcega` | 63 | accented spelling 4,994 vs 63 |
| `sahagun` | `sahagún` | 63 | accented spelling 692 vs 63 |
| `preinstalacion` | `preinstalación` | 63 | accented spelling 1,714 vs 63 |
| `filmacion` | `filmación` | 63 | accented spelling 6,509 vs 63 |
| `analogico` | `analógico` | 63 | accented spelling 22,561 vs 63 |
| `cigueña` | `cigüeña` | 63 | accented spelling 2,024 vs 63 |
| `detencion` | `detención` | 63 | accented spelling 46,981 vs 63 |
| `sentiras` | `sentir` | 63 | accented spelling 3,599 vs 63 |
| `sesamo` | `sésamo` | 63 | accented spelling 5,531 vs 63 |
| `sufrio` | `sufrir` | 63 | accented spelling 13,873 vs 63 |
| `jugueton` | `juguetón` | 63 | accented spelling 4,232 vs 63 |
| `confesion` | `confesión` | 63 | accented spelling 13,463 vs 63 |
| `quiropractico` | `quiropráctico` | 62 | accented spelling 6,197 vs 62 |
| `maracuya` | `maracuyá` | 62 | accented spelling 1,072 vs 62 |
| `agradeceria` | `agradecer` | 62 | accented spelling 690 vs 62 |
| `cesped` | `césped` | 62 | accented spelling 33,566 vs 62 |
| `almodovar` | `almodóvar` | 62 | accented spelling 1,492 vs 62 |
| `almaden` | `almadén` | 62 | accented spelling 334 vs 62 |
| `antartida` | `antártida` | 62 | accented spelling 7,887 vs 62 |
| `alaro` | `alaró` | 62 | accented spelling 748 vs 62 |
| `practicamente` | `prácticamente` | 62 | accented spelling 93,131 vs 62 |
| `recibire` | `recibir` | 62 | accented spelling 1,676 vs 62 |
| `pedagogia` | `pedagogía` | 62 | accented spelling 8,661 vs 62 |
| `erroneamente` | `erróneamente` | 62 | accented spelling 7,326 vs 62 |
| `perforacion` | `perforación` | 62 | accented spelling 44,660 vs 62 |
| `pabellon` | `pabellón` | 62 | accented spelling 28,307 vs 62 |
| `chacon` | `chacón` | 62 | accented spelling 1,349 vs 62 |
| `acequion` | `acequión` | 62 | accented spelling 338 vs 62 |
| `comun` | `común` | 62 | accented spelling 458,787 vs 62 |
| `tendrian` | `tener` | 62 | accented spelling 8,407 vs 62 |
| `bernabe` | `bernabé` | 61 | accented spelling 5,352 vs 61 |
| `rebelo` | `rebelar` | 61 | accented spelling 949 vs 61 |
| `barragan` | `barragán` | 61 | accented spelling 795 vs 61 |
| `bufalo` | `búfalo` | 61 | accented spelling 7,991 vs 61 |
| `epidemiologia` | `epidemiología` | 61 | accented spelling 4,781 vs 61 |
| `e-liquido` | `e-líquido` | 61 | accented spelling 1,184 vs 61 |
| `lactea` | `lácteo` | 61 | accented spelling 1,521 vs 61 |
| `tematicas` | `temática` | 61 | accented spelling 10,919 vs 61 |
| `caton` | `catón` | 61 | accented spelling 305 vs 61 |
| `agusti` | `agustí` | 61 | accented spelling 600 vs 61 |
| `estanterias` | `estantería` | 61 | accented spelling 6,714 vs 61 |
| `digestion` | `digestión` | 61 | accented spelling 16,313 vs 61 |
| `pare` | `parar` | 61 | accented spelling 351 vs 61 |
| `automovilistico` | `automovilístico` | 61 | accented spelling 11,554 vs 61 |
| `creiste` | `creer` | 61 | accented spelling 373 vs 61 |
| `inclinacion` | `inclinación` | 61 | accented spelling 26,099 vs 61 |
| `fotografos` | `fotógrafo` | 61 | accented spelling 12,804 vs 61 |
| `descubriras` | `descubrir` | 61 | accented spelling 5,373 vs 61 |
| `ayatola` | `ayatolá` | 61 | accented spelling 877 vs 61 |
| `evangelistico` | `evangelístico` | 61 | accented spelling 364 vs 61 |
| `glandula` | `glándula` | 61 | accented spelling 26,577 vs 61 |
| `caliz` | `cáliz` | 61 | accented spelling 6,911 vs 61 |
| `geografico` | `geográfico` | 60 | accented spelling 42,952 vs 60 |
| `permitia` | `permitir` | 60 | accented spelling 6,789 vs 60 |
| `anonimos` | `anónimo` | 60 | accented spelling 9,919 vs 60 |
| `tazon` | `tazón` | 60 | accented spelling 22,987 vs 60 |
| `matricula` | `matrícula` | 60 | accented spelling 24,045 vs 60 |
| `posicion` | `posición` | 60 | accented spelling 392,738 vs 60 |
| `median` | `medir` | 60 | accented spelling 337 vs 60 |
| `explique` | `explicar` | 60 | accented spelling 1,431 vs 60 |
| `topografia` | `topografía` | 60 | accented spelling 9,133 vs 60 |
| `guibea` | `guibeá` | 60 | accented spelling 1,072 vs 60 |
| `semisotano` | `semisótano` | 60 | accented spelling 1,010 vs 60 |
| `transeunte` | `transeúnte` | 60 | accented spelling 2,470 vs 60 |
| `academica` | `académico` | 60 | accented spelling 16,580 vs 60 |
| `diabetico` | `diabético` | 60 | accented spelling 10,042 vs 60 |
| `quedaria` | `quedar` | 60 | accented spelling 2,988 vs 60 |
| `marabu` | `marabú` | 60 | accented spelling 302 vs 60 |
| `aminoacido` | `aminoácido` | 60 | accented spelling 16,056 vs 60 |
| `autonomo` | `autónomo` | 60 | accented spelling 47,626 vs 60 |
| `laminas` | `lámina` | 60 | accented spelling 10,750 vs 60 |
| `bateo` | `batear` | 60 | accented spelling 661 vs 60 |
| `migracion` | `migración` | 60 | accented spelling 63,167 vs 60 |
| `negociacion` | `negociación` | 60 | accented spelling 77,892 vs 60 |
| `optimizacion` | `optimización` | 60 | accented spelling 55,766 vs 60 |
| `ahi` | `ahí` | 60 | accented spelling 179,322 vs 60 |
| `guilloche` | `guilloché` | 60 | accented spelling 321 vs 60 |
| `reunan` | `reunir` | 60 | accented spelling 1,264 vs 60 |
| `alcacer` | `alcácer` | 60 | accented spelling 362 vs 60 |
| `sustitucion` | `sustitución` | 59 | accented spelling 34,574 vs 59 |
| `protegera` | `proteger` | 59 | accented spelling 3,002 vs 59 |
| `valio` | `valer` | 59 | accented spelling 2,493 vs 59 |
| `cardiologia` | `cardiología` | 59 | accented spelling 6,760 vs 59 |
| `antologia` | `antología` | 59 | accented spelling 3,132 vs 59 |
| `albaicin` | `albaicín` | 59 | accented spelling 1,676 vs 59 |
| `psicologica` | `psicológico` | 59 | accented spelling 7,676 vs 59 |
| `aclaro` | `aclarar` | 59 | accented spelling 2,329 vs 59 |
| `olavarria` | `olavarría` | 59 | accented spelling 344 vs 59 |
| `tecnologicas` | `tecnológico` | 59 | accented spelling 16,903 vs 59 |
| `teleferico` | `teleférico` | 59 | accented spelling 9,257 vs 59 |
| `isotopo` | `isótopo` | 59 | accented spelling 1,917 vs 59 |
| `efren` | `efrén` | 59 | accented spelling 420 vs 59 |
| `perdera` | `perder` | 59 | accented spelling 5,008 vs 59 |
| `magicas` | `mágico` | 59 | accented spelling 5,473 vs 59 |
| `manutencion` | `manutención` | 59 | accented spelling 14,322 vs 59 |
| `mande` | `mandar` | 59 | accented spelling 1,659 vs 59 |
| `comparti` | `compartir` | 59 | accented spelling 1,121 vs 59 |
| `atraves` | `a través` | 59 | accented spelling 1,608 vs 59 |
| `orin` | `orín` | 59 | accented spelling 606 vs 59 |
| `aromatico` | `aromático` | 59 | accented spelling 11,877 vs 59 |
| `discriminacion` | `discriminación` | 58 | accented spelling 61,744 vs 58 |
| `piaui` | `piauí` | 58 | accented spelling 476 vs 58 |
| `vendre` | `venir` | 58 | accented spelling 1,169 vs 58 |
| `valia` | `valía` | 58 | accented spelling 5,395 vs 58 |
| `bengali` | `bengalí` | 58 | accented spelling 1,383 vs 58 |
| `recomendaria` | `recomendar` | 58 | accented spelling 11,361 vs 58 |
| `astronomia` | `astronomía` | 58 | accented spelling 11,243 vs 58 |
| `radon` | `radón` | 58 | accented spelling 2,608 vs 58 |
| `atomo` | `átomo` | 58 | accented spelling 13,590 vs 58 |
| `margenes` | `margen` | 58 | accented spelling 9,381 vs 58 |
| `variacion` | `variación` | 58 | accented spelling 59,972 vs 58 |
| `cuido` | `cuidar` | 58 | accented spelling 793 vs 58 |
| `tramites` | `trámite` | 58 | accented spelling 8,344 vs 58 |
| `lirico` | `lírico` | 58 | accented spelling 3,050 vs 58 |
| `macoris` | `macorís` | 58 | accented spelling 558 vs 58 |
| `conseguira` | `conseguir` | 58 | accented spelling 4,492 vs 58 |
| `oiste` | `oír` | 58 | accented spelling 712 vs 58 |
| `paseis` | `pasar` | 58 | accented spelling 782 vs 58 |
| `paysandu` | `paysandú` | 58 | accented spelling 668 vs 58 |
| `habias` | `haber` | 57 | accented spelling 4,221 vs 57 |
| `parecian` | `parecer` | 57 | accented spelling 7,708 vs 57 |
| `inalambrico` | `inalámbrico` | 57 | accented spelling 111,255 vs 57 |
| `maldicion` | `maldición` | 57 | accented spelling 17,551 vs 57 |
| `cartama` | `cártama` | 57 | accented spelling 330 vs 57 |
| `pediatria` | `pediatría` | 57 | accented spelling 6,653 vs 57 |
| `cardon` | `cardón` | 57 | accented spelling 531 vs 57 |
| `primogenito` | `primogénito` | 57 | accented spelling 12,596 vs 57 |
| `chicharo` | `chícharo` | 57 | accented spelling 566 vs 57 |
| `accio` | `acció` | 57 | accented spelling 376 vs 57 |
| `geograficas` | `geográfico` | 57 | accented spelling 10,393 vs 57 |
| `prohiban` | `prohibir` | 57 | accented spelling 479 vs 57 |
| `mas` | `más` | 57 | accented spelling 14,251,356 vs 57 |
| `juridicas` | `jurídico` | 57 | accented spelling 9,636 vs 57 |
| `pedira` | `pedir` | 57 | accented spelling 10,474 vs 57 |
| `arguineguin` | `arguineguín` | 57 | accented spelling 316 vs 57 |
| `betera` | `bétera` | 57 | accented spelling 418 vs 57 |
| `vastago` | `vástago` | 56 | accented spelling 7,746 vs 56 |
| `chavin` | `chavín` | 56 | accented spelling 508 vs 56 |
| `petropolis` | `petrópolis` | 56 | accented spelling 606 vs 56 |
| `aprenderas` | `aprender` | 56 | accented spelling 6,273 vs 56 |
| `ultimas` | `último` | 56 | accented spelling 114,638 vs 56 |
| `induccion` | `inducción` | 56 | accented spelling 20,618 vs 56 |
| `vinicola` | `vinícola` | 56 | accented spelling 5,563 vs 56 |
| `querais` | `querer` | 56 | accented spelling 1,698 vs 56 |
| `tuberias` | `tubería` | 56 | accented spelling 21,265 vs 56 |
| `demografica` | `demográfico` | 56 | accented spelling 7,332 vs 56 |
| `marroquineria` | `marroquinería` | 56 | accented spelling 1,745 vs 56 |
| `adhesion` | `adhesión` | 56 | accented spelling 31,036 vs 56 |
| `wurth` | `würth` | 56 | accented spelling 322 vs 56 |
| `mbappe` | `mbappé` | 56 | accented spelling 418 vs 56 |
| `codice` | `códice` | 56 | accented spelling 2,327 vs 56 |
| `estadistico` | `estadístico` | 56 | accented spelling 30,266 vs 56 |
| `canape` | `canapé` | 56 | accented spelling 1,088 vs 56 |
| `chamberi` | `chamberí` | 56 | accented spelling 1,266 vs 56 |
| `pompon` | `pompón` | 56 | accented spelling 1,672 vs 56 |
| `mencione` | `mencionar` | 55 | accented spelling 2,203 vs 55 |
| `reconciliacion` | `reconciliación` | 55 | accented spelling 22,523 vs 55 |
| `pres` | `prés` | 55 | accented spelling 390 vs 55 |
| `reservo` | `reservar` | 55 | accented spelling 762 vs 55 |
| `istan` | `istán` | 55 | accented spelling 520 vs 55 |
| `buble` | `bublé` | 55 | accented spelling 346 vs 55 |
| `tutankamon` | `tutankamón` | 55 | accented spelling 686 vs 55 |
| `dejeis` | `dejar` | 55 | accented spelling 1,398 vs 55 |
| `ximenez` | `ximénez` | 55 | accented spelling 518 vs 55 |
| `prevision` | `previsión` | 55 | accented spelling 133,467 vs 55 |
| `echo` | `echar` | 55 | accented spelling 5,568 vs 55 |
| `molecula` | `molécula` | 55 | accented spelling 19,084 vs 55 |
| `auditoria` | `auditoría` | 55 | accented spelling 57,020 vs 55 |
| `glutation` | `glutatión` | 55 | accented spelling 2,318 vs 55 |
| `esnorquel` | `esnórquel` | 55 | accented spelling 2,689 vs 55 |
| `dinamicas` | `dinámico` | 55 | accented spelling 12,960 vs 55 |
| `succion` | `succión` | 55 | accented spelling 16,401 vs 55 |
| `pluton` | `plutón` | 55 | accented spelling 4,229 vs 55 |
| `receto` | `recetar` | 55 | accented spelling 515 vs 55 |
| `conteste` | `contestar` | 55 | accented spelling 664 vs 55 |
| `cadaver` | `cadáver` | 55 | accented spelling 18,009 vs 55 |
| `bajio` | `bajío` | 54 | accented spelling 895 vs 54 |
| `microdermabrasion` | `microdermabrasión` | 54 | accented spelling 370 vs 54 |
| `estarian` | `estar` | 54 | accented spelling 7,121 vs 54 |
| `faberge` | `fabergé` | 54 | accented spelling 322 vs 54 |
| `vater` | `váter` | 54 | accented spelling 576 vs 54 |
| `gramatica` | `gramática` | 54 | accented spelling 14,808 vs 54 |
| `titulos` | `título` | 54 | accented spelling 39,664 vs 54 |
| `peñin` | `peñín` | 54 | accented spelling 412 vs 54 |
| `biotecnologia` | `biotecnología` | 54 | accented spelling 14,205 vs 54 |
| `reuna` | `reunir` | 54 | accented spelling 2,197 vs 54 |
| `naaman` | `naamán` | 54 | accented spelling 2,156 vs 54 |
| `poligrafo` | `polígrafo` | 54 | accented spelling 715 vs 54 |
| `electronicamente` | `electrónicamente` | 54 | accented spelling 11,880 vs 54 |
| `logre` | `lograr` | 54 | accented spelling 1,781 vs 54 |
| `geltru` | `geltrú` | 54 | accented spelling 926 vs 54 |
| `degustacion` | `degustación` | 54 | accented spelling 17,389 vs 54 |
| `escogi` | `escoger` | 54 | accented spelling 2,026 vs 54 |
| `aromaticas` | `aromático` | 54 | accented spelling 3,093 vs 54 |
| `galpon` | `galpón` | 54 | accented spelling 939 vs 54 |
| `rococo` | `rococó` | 54 | accented spelling 1,144 vs 54 |
| `votacion` | `votación` | 54 | accented spelling 40,120 vs 54 |
| `extraidas` | `extraer` | 54 | accented spelling 1,884 vs 54 |
| `insercion` | `inserción` | 54 | accented spelling 32,754 vs 54 |
| `mediacion` | `mediación` | 54 | accented spelling 21,628 vs 54 |
| `querias` | `querer` | 54 | accented spelling 3,026 vs 54 |
| `semaforo` | `semáforo` | 54 | accented spelling 8,875 vs 54 |
| `cardan` | `cardán` | 54 | accented spelling 1,660 vs 54 |
| `permitano` | `permitir` | 54 | accented spelling 1,066 vs 54 |
| `patagonica` | `patagónico` | 53 | accented spelling 618 vs 53 |
| `relajese` | `relajarse` | 53 | accented spelling 10,159 vs 53 |
| `tomare` | `tomar` | 53 | accented spelling 1,787 vs 53 |
| `humedos` | `húmedo` | 53 | accented spelling 5,588 vs 53 |
| `sujecion` | `sujeción` | 53 | accented spelling 36,731 vs 53 |
| `geometrico` | `geométrico` | 53 | accented spelling 15,443 vs 53 |
| `mitzva` | `mitzvá` | 53 | accented spelling 943 vs 53 |
| `exoticas` | `exótico` | 53 | accented spelling 5,030 vs 53 |
| `converti` | `convertir` | 53 | accented spelling 1,384 vs 53 |
| `expulsion` | `expulsión` | 53 | accented spelling 14,437 vs 53 |
| `discografia` | `discografía` | 53 | accented spelling 4,803 vs 53 |
| `irazu` | `irazú` | 53 | accented spelling 352 vs 53 |
| `autodromo` | `autódromo` | 53 | accented spelling 845 vs 53 |
| `zuñiga` | `zúñiga` | 53 | accented spelling 864 vs 53 |
| `rossello` | `rosselló` | 53 | accented spelling 1,622 vs 53 |
| `personalizalo` | `personalizar` | 53 | accented spelling 425 vs 53 |
| `antartica` | `antártico` | 53 | accented spelling 1,339 vs 53 |
| `torico` | `tórico` | 53 | accented spelling 1,325 vs 53 |
| `patagonico` | `patagónico` | 53 | accented spelling 2,605 vs 53 |
| `contratacion` | `contratación` | 53 | accented spelling 50,571 vs 53 |
| `civilizacion` | `civilización` | 53 | accented spelling 36,987 vs 53 |
| `irian` | `ir` | 53 | accented spelling 891 vs 53 |
| `bezier` | `bézier` | 53 | accented spelling 278 vs 53 |
| `creanme` | `creer` | 53 | accented spelling 1,446 vs 53 |
| `mojon` | `mojón` | 53 | accented spelling 534 vs 53 |
| `mandragora` | `mandrágora` | 53 | accented spelling 547 vs 53 |
| `ultimos` | `último` | 52 | accented spelling 258,181 vs 52 |
| `confiteria` | `confitería` | 52 | accented spelling 3,880 vs 52 |
| `rele` | `relé` | 52 | accented spelling 8,877 vs 52 |
| `traccion` | `tracción` | 52 | accented spelling 55,202 vs 52 |
| `menorquin` | `menorquín` | 52 | accented spelling 1,040 vs 52 |
| `obus` | `obús` | 52 | accented spelling 714 vs 52 |
| `associacio` | `associació` | 52 | accented spelling 662 vs 52 |
| `peloton` | `pelotón` | 52 | accented spelling 4,283 vs 52 |
| `cateter` | `catéter` | 52 | accented spelling 12,341 vs 52 |
| `momentaneamente` | `momentáneamente` | 52 | accented spelling 3,248 vs 52 |
| `torax` | `tórax` | 52 | accented spelling 8,220 vs 52 |
| `utilizo` | `utilizar` | 52 | accented spelling 19,487 vs 52 |
| `planifica` | `planificar` | 52 | accented spelling 3,468 vs 52 |
| `rompio` | `romper` | 52 | accented spelling 5,077 vs 52 |
| `dependera` | `depender` | 52 | accented spelling 12,305 vs 52 |
| `aspiracion` | `aspiración` | 52 | accented spelling 27,165 vs 52 |
| `aprendera` | `aprender` | 52 | accented spelling 8,232 vs 52 |
| `discusion` | `discusión` | 52 | accented spelling 99,647 vs 52 |
| `curico` | `curicó` | 52 | accented spelling 500 vs 52 |
| `latigo` | `látigo` | 52 | accented spelling 3,305 vs 52 |
| `finalizacion` | `finalización` | 52 | accented spelling 27,891 vs 52 |
| `perdidas` | `pérdida` | 52 | accented spelling 37,123 vs 52 |
| `congestion` | `congestión` | 51 | accented spelling 10,683 vs 51 |
| `trilogia` | `trilogía` | 51 | accented spelling 6,743 vs 51 |
| `encendera` | `encender` | 51 | accented spelling 642 vs 51 |
| `crepusculo` | `crepúsculo` | 51 | accented spelling 9,861 vs 51 |
| `repatriacion` | `repatriación` | 51 | accented spelling 3,833 vs 51 |
| `lavapies` | `lavapiés` | 51 | accented spelling 832 vs 51 |
| `ason` | `asón` | 51 | accented spelling 294 vs 51 |
| `repeticion` | `repetición` | 51 | accented spelling 24,859 vs 51 |
| `radiografia` | `radiografía` | 51 | accented spelling 15,258 vs 51 |
| `metropoli` | `metrópoli` | 51 | accented spelling 3,540 vs 51 |
| `comio` | `comer` | 51 | accented spelling 3,500 vs 51 |
| `boson` | `bosón` | 51 | accented spelling 1,290 vs 51 |
| `ofrecia` | `ofrecer` | 51 | accented spelling 4,692 vs 51 |
| `audicion` | `audición` | 51 | accented spelling 25,926 vs 51 |
| `varon` | `varón` | 51 | accented spelling 46,566 vs 51 |
| `poquer` | `póquer` | 51 | accented spelling 34,431 vs 51 |
| `trencadis` | `trencadís` | 51 | accented spelling 466 vs 51 |
| `transportin#Fem` | `transportín` | 51 | accented spelling 588 vs 51 |
| `visitame` | `visitar` | 51 | accented spelling 302 vs 51 |
| `tendon` | `tendón` | 51 | accented spelling 9,481 vs 51 |
| `cromatico` | `cromático` | 51 | accented spelling 10,025 vs 51 |
| `mashiaj` | `mashíaj` | 51 | accented spelling 474 vs 51 |
| `apendice` | `apéndice` | 51 | accented spelling 15,113 vs 51 |
| `abominacion` | `abominación` | 51 | accented spelling 8,520 vs 51 |
| `iconica` | `icónico` | 51 | accented spelling 3,366 vs 51 |
| `becquer` | `bécquer` | 51 | accented spelling 348 vs 51 |
| `anatomica` | `anatómico` | 51 | accented spelling 1,702 vs 51 |
| `alcoholico` | `alcohólico` | 51 | accented spelling 17,222 vs 51 |
| `monitorizacion` | `monitorización` | 51 | accented spelling 25,803 vs 51 |
| `neumaticos` | `neumático` | 51 | accented spelling 41,310 vs 51 |
| `maniqui` | `maniquí` | 50 | accented spelling 4,843 vs 50 |
| `leido` | `leer` | 50 | accented spelling 25,832 vs 50 |
| `revoco` | `revocar` | 50 | accented spelling 656 vs 50 |
| `tantrico` | `tántrico` | 50 | accented spelling 1,467 vs 50 |
| `placido` | `plácido` | 50 | accented spelling 2,270 vs 50 |
| `presion` | `presión` | 50 | accented spelling 318,929 vs 50 |
| `aprendio` | `aprender` | 50 | accented spelling 6,787 vs 50 |
| `interactua` | `interactuar` | 50 | accented spelling 4,766 vs 50 |
| `sonico` | `sónico` | 50 | accented spelling 2,006 vs 50 |
| `diaz-balart` | `díaz-balart` | 50 | accented spelling 284 vs 50 |
| `teorico` | `teórico` | 50 | accented spelling 35,118 vs 50 |
| `abrasion` | `abrasión` | 50 | accented spelling 13,000 vs 50 |
| `hidrogeno` | `hidrógeno` | 50 | accented spelling 23,657 vs 50 |
| `trevelez` | `trevélez` | 50 | accented spelling 256 vs 50 |
| `taull` | `taüll` | 50 | accented spelling 322 vs 50 |
| `agonia` | `agonía` | 50 | accented spelling 5,338 vs 50 |
| `donbas` | `donbás` | 50 | accented spelling 272 vs 50 |
| `quiros` | `quirós` | 50 | accented spelling 662 vs 50 |
| `triclosan` | `triclosán` | 50 | accented spelling 446 vs 50 |
| `sacatepequez` | `sacatepéquez` | 50 | accented spelling 644 vs 50 |
| `gamez` | `gámez` | 50 | accented spelling 374 vs 50 |
| `dwor` | `dwór` | 50 | accented spelling 254 vs 50 |
| `pade` | `pádel` | 50 | accented spelling 1,553 vs 50 |
| `estencil` | `esténcil` | 50 | accented spelling 258 vs 50 |
| `arida` | `árido` | 50 | accented spelling 796 vs 50 |
| `perdais` | `perder` | 50 | accented spelling 529 vs 50 |
| `atrevia` | `atreverse` | 50 | accented spelling 747 vs 50 |
| `resalto` | `resaltar` | 50 | accented spelling 2,673 vs 50 |
| `edredon` | `edredón` | 50 | accented spelling 8,973 vs 50 |
| `ultrasonico` | `ultrasónico` | 50 | accented spelling 13,337 vs 50 |
| `sereis` | `ser` | 49 | accented spelling 6,207 vs 49 |
| `martov` | `mártov` | 49 | accented spelling 332 vs 49 |
| `origenes` | `origen` | 49 | accented spelling 20,770 vs 49 |
| `jucar` | `júcar` | 49 | accented spelling 1,336 vs 49 |
| `identica` | `idéntico` | 49 | accented spelling 3,544 vs 49 |
| `consistia` | `consistir` | 49 | accented spelling 4,836 vs 49 |
| `antigeno` | `antígeno` | 49 | accented spelling 6,312 vs 49 |
| `señalizacion` | `señalización` | 49 | accented spelling 22,595 vs 49 |
| `pavon` | `pavón` | 49 | accented spelling 882 vs 49 |
| `diogenes` | `diógenes` | 49 | accented spelling 398 vs 49 |
| `datil` | `dátil` | 49 | accented spelling 1,509 vs 49 |
| `impio` | `impío` | 49 | accented spelling 11,815 vs 49 |
| `cilindrico` | `cilíndrico` | 49 | accented spelling 7,977 vs 49 |
| `estariamos` | `estar` | 49 | accented spelling 2,701 vs 49 |
| `riofrio` | `riofrío` | 49 | accented spelling 356 vs 49 |
| `dramaticamente` | `dramáticamente` | 49 | accented spelling 7,616 vs 49 |
| `trituracion` | `trituración` | 49 | accented spelling 5,617 vs 49 |
| `pelaez` | `peláez` | 49 | accented spelling 438 vs 49 |
| `jardi` | `jardí` | 49 | accented spelling 494 vs 49 |
| `granulo` | `gránulo` | 49 | accented spelling 3,809 vs 49 |
| `disfuncion` | `disfunción` | 49 | accented spelling 21,352 vs 49 |
| `climaticas` | `climático` | 49 | accented spelling 13,880 vs 49 |
| `macula` | `mácula` | 49 | accented spelling 2,437 vs 49 |
| `vayais` | `ir` | 49 | accented spelling 1,126 vs 49 |
| `drasticamente` | `drásticamente` | 49 | accented spelling 16,924 vs 49 |
| `saron` | `sarón` | 49 | accented spelling 558 vs 49 |
| `cartilago` | `cartílago` | 49 | accented spelling 8,238 vs 49 |
| `fotografie` | `fotografiar` | 49 | accented spelling 283 vs 49 |
| `receptaculo` | `receptáculo` | 49 | accented spelling 3,193 vs 49 |
| `tonico` | `tónico` | 49 | accented spelling 5,941 vs 49 |
| `amnon` | `amnón` | 49 | accented spelling 2,112 vs 49 |
| `traida` | `traer` | 49 | accented spelling 1,236 vs 49 |
| `construcion` | `construcción` | 49 | accented spelling 554 vs 49 |
| `inflamacion` | `inflamación` | 49 | accented spelling 56,480 vs 49 |
| `arqueologia` | `arqueología` | 49 | accented spelling 10,712 vs 49 |
| `armagedon` | `armagedón` | 48 | accented spelling 1,764 vs 48 |
| `bellisimo` | `bello` | 48 | accented spelling 2,170 vs 48 |
| `acumulacion` | `acumulación` | 48 | accented spelling 39,336 vs 48 |
| `afirmo` | `afirmar` | 48 | accented spelling 28,627 vs 48 |
| `rebajo` | `rebajar` | 48 | accented spelling 278 vs 48 |
| `salonica` | `salónica` | 48 | accented spelling 6,200 vs 48 |
| `contactandono` | `contactar` | 48 | accented spelling 1,279 vs 48 |
| `amplian` | `ampliar` | 48 | accented spelling 2,485 vs 48 |
| `interferon` | `interferón` | 48 | accented spelling 1,874 vs 48 |
| `humedas` | `húmedo` | 48 | accented spelling 5,200 vs 48 |
| `vendra` | `venir` | 48 | accented spelling 14,737 vs 48 |
| `liberate` | `liberar` | 48 | accented spelling 262 vs 48 |
| `necropolis` | `necrópolis` | 48 | accented spelling 2,496 vs 48 |
| `regua` | `régua` | 48 | accented spelling 300 vs 48 |
| `islamico` | `islámico` | 48 | accented spelling 21,282 vs 48 |
| `creci` | `crecer` | 48 | accented spelling 2,480 vs 48 |
| `vaqueria` | `vaquería` | 48 | accented spelling 288 vs 48 |
| `echevarria` | `echevarría` | 48 | accented spelling 606 vs 48 |
| `desesperacion` | `desesperación` | 48 | accented spelling 13,096 vs 48 |
| `codecs` | `códec` | 48 | accented spelling 2,042 vs 48 |
| `triptofano` | `triptófano` | 48 | accented spelling 1,626 vs 48 |
| `especificacion` | `especificación` | 48 | accented spelling 128,030 vs 48 |
| `cañeria` | `cañería` | 48 | accented spelling 1,923 vs 48 |
| `calidamente` | `cálidamente` | 48 | accented spelling 872 vs 48 |
| `ridiculo` | `ridículo` | 48 | accented spelling 8,646 vs 48 |
| `expiracion` | `expiración` | 48 | accented spelling 7,379 vs 48 |
| `evalue` | `evaluar` | 48 | accented spelling 3,172 vs 48 |
| `anabolico` | `anabólico` | 48 | accented spelling 28,181 vs 48 |
| `coalicion` | `coalición` | 48 | accented spelling 31,818 vs 48 |
| `canones` | `canon` | 48 | accented spelling 1,709 vs 48 |
| `emaus` | `emaús` | 48 | accented spelling 3,010 vs 48 |
| `ninfomana` | `ninfómana` | 48 | accented spelling 487 vs 48 |
| `servian` | `servir` | 48 | accented spelling 2,686 vs 48 |
| `guardela` | `guardar` | 48 | accented spelling 28,141 vs 48 |
| `tendriamos` | `tener` | 47 | accented spelling 3,197 vs 47 |
| `fogon` | `fogón` | 47 | accented spelling 5,252 vs 47 |
| `prohibicion` | `prohibición` | 47 | accented spelling 35,465 vs 47 |
| `subira` | `subir` | 47 | accented spelling 2,148 vs 47 |
| `lanjaron` | `lanjarón` | 47 | accented spelling 1,298 vs 47 |
| `hirio` | `herir` | 47 | accented spelling 4,874 vs 47 |
| `unicos` | `único` | 47 | accented spelling 36,352 vs 47 |
| `billon` | `billón` | 47 | accented spelling 16,869 vs 47 |
| `inmovil` | `inmóvil` | 47 | accented spelling 6,330 vs 47 |
| `taoista` | `taoísta` | 47 | accented spelling 816 vs 47 |
| `fiscalia` | `fiscalía` | 47 | accented spelling 15,226 vs 47 |
| `narracion` | `narración` | 47 | accented spelling 14,080 vs 47 |
| `imitacion` | `imitación` | 47 | accented spelling 19,831 vs 47 |
| `manases` | `manasés` | 47 | accented spelling 10,852 vs 47 |
| `espero` | `esperar` | 47 | accented spelling 2,446 vs 47 |
| `maimonides` | `maimónides` | 47 | accented spelling 418 vs 47 |
| `gedeon` | `gedeón` | 47 | accented spelling 5,154 vs 47 |
| `quimicos` | `químico` | 47 | accented spelling 47,008 vs 47 |
| `decadas` | `década` | 47 | accented spelling 46,691 vs 47 |
| `lucida` | `lúcido` | 47 | accented spelling 421 vs 47 |
| `nanometro` | `nanómetro` | 47 | accented spelling 8,480 vs 47 |
| `nordicas` | `nórdico` | 47 | accented spelling 527 vs 47 |
| `ecografia` | `ecografía` | 47 | accented spelling 10,479 vs 47 |
| `paradisiaca` | `paradisíaco` | 47 | accented spelling 870 vs 47 |
| `santafe` | `santafé` | 47 | accented spelling 292 vs 47 |
| `multifuncion` | `multifunción` | 47 | accented spelling 22,468 vs 47 |
| `avalos` | `ávalos` | 47 | accented spelling 262 vs 47 |
| `karoly` | `károly` | 47 | accented spelling 278 vs 47 |
| `fosil` | `fósil` | 47 | accented spelling 14,664 vs 47 |
| `tentaculo` | `tentáculo` | 47 | accented spelling 1,634 vs 47 |
| `arrayan` | `arrayán` | 47 | accented spelling 508 vs 47 |
| `parchis` | `parchís` | 47 | accented spelling 424 vs 47 |
| `democrata` | `demócrata` | 47 | accented spelling 24,894 vs 47 |
| `guixols` | `guíxols` | 47 | accented spelling 516 vs 47 |
| `ergonomico` | `ergonómico` | 47 | accented spelling 19,548 vs 47 |
| `femina` | `fémina` | 47 | accented spelling 540 vs 47 |
| `existian` | `existir` | 47 | accented spelling 5,623 vs 47 |
| `iglu` | `iglú` | 47 | accented spelling 973 vs 47 |
| `sabreis` | `saber` | 46 | accented spelling 2,154 vs 46 |
| `obsesion` | `obsesión` | 46 | accented spelling 9,734 vs 46 |
| `ponton` | `pontón` | 46 | accented spelling 1,967 vs 46 |
| `vacacion` | `vacaciones` | 46 | accented spelling 1,962 vs 46 |
| `proxima#cousin` | `próximo` | 46 | accented spelling 71,925 vs 46 |
| `demografico` | `demográfico` | 46 | accented spelling 19,394 vs 46 |
| `diplomaticas` | `diplomático` | 46 | accented spelling 5,211 vs 46 |
| `algun` | `alguno` | 46 | accented spelling 187,681 vs 46 |
| `loiza` | `loíza` | 46 | accented spelling 252 vs 46 |
| `interrupcion` | `interrupción` | 46 | accented spelling 47,476 vs 46 |
| `usti` | `ústí` | 46 | accented spelling 322 vs 46 |
| `demolicion` | `demolición` | 46 | accented spelling 7,931 vs 46 |
| `asia-pacifico` | `asia-pacífico` | 46 | accented spelling 4,902 vs 46 |
| `solidamente` | `sólidamente` | 46 | accented spelling 1,914 vs 46 |
| `indole` | `índole` | 46 | accented spelling 15,929 vs 46 |
| `ajimelec` | `ajimélec` | 46 | accented spelling 322 vs 46 |
| `ahogo` | `ahogarse` | 46 | accented spelling 528 vs 46 |
| `transgenero` | `transgénero` | 46 | accented spelling 7,241 vs 46 |
| `bantu` | `bantú` | 46 | accented spelling 299 vs 46 |
| `mames` | `mamés` | 46 | accented spelling 576 vs 46 |
| `felicitacion` | `felicitación` | 46 | accented spelling 13,604 vs 46 |
| `habrian` | `haber` | 46 | accented spelling 11,587 vs 46 |
| `pulpi` | `pulpí` | 46 | accented spelling 252 vs 46 |
| `technologia` | `tecnología` | 46 | accented spelling 470 vs 46 |
| `escorpion` | `escorpión` | 46 | accented spelling 4,863 vs 46 |
| `cadaques` | `cadaqués` | 46 | accented spelling 1,802 vs 46 |
| `tonala` | `tonalá` | 46 | accented spelling 394 vs 46 |
| `laud` | `laúd` | 46 | accented spelling 1,067 vs 46 |
| `antioco` | `antíoco` | 46 | accented spelling 1,096 vs 46 |
| `simil` | `símil` | 46 | accented spelling 1,061 vs 46 |
| `idem` | `ídem` | 46 | accented spelling 371 vs 46 |
| `alineacion` | `alineación` | 46 | accented spelling 23,440 vs 46 |
| `pelin` | `pelín` | 46 | accented spelling 572 vs 46 |
| `consiguio` | `conseguir` | 46 | accented spelling 15,018 vs 46 |
| `hidratacion` | `hidratación` | 46 | accented spelling 19,648 vs 46 |
| `dejaria` | `dejar` | 45 | accented spelling 3,047 vs 45 |
| `marroqui` | `marroquí` | 45 | accented spelling 14,271 vs 45 |
| `periodica` | `periódico` | 45 | accented spelling 7,325 vs 45 |
| `divulgacion` | `divulgación` | 45 | accented spelling 57,662 vs 45 |
| `hicieramos` | `hacer` | 45 | accented spelling 797 vs 45 |
| `dono` | `donar` | 45 | accented spelling 1,753 vs 45 |
| `iconico` | `icónico` | 45 | accented spelling 17,017 vs 45 |
| `globalizacion` | `globalización` | 45 | accented spelling 23,514 vs 45 |
| `floracion` | `floración` | 45 | accented spelling 17,594 vs 45 |
| `desaparecio` | `desaparecer` | 45 | accented spelling 6,246 vs 45 |
| `superacion` | `superación` | 45 | accented spelling 10,154 vs 45 |
| `chinchon` | `chinchón` | 45 | accented spelling 670 vs 45 |
| `narvaez` | `narváez` | 45 | accented spelling 610 vs 45 |
| `nitida` | `nítido` | 45 | accented spelling 3,865 vs 45 |
| `solto` | `soltar` | 45 | accented spelling 1,711 vs 45 |
| `comento` | `comentar` | 45 | accented spelling 17,334 vs 45 |
| `pasaria` | `pasar` | 45 | accented spelling 4,785 vs 45 |
| `admiracion` | `admiración` | 45 | accented spelling 10,637 vs 45 |
| `gaucin` | `gaucín` | 45 | accented spelling 432 vs 45 |
| `conviccion` | `convicción` | 45 | accented spelling 23,016 vs 45 |
| `jundiai` | `jundiaí` | 45 | accented spelling 354 vs 45 |
| `aereos` | `aéreo` | 45 | accented spelling 15,872 vs 45 |
| `maletin` | `maletín` | 45 | accented spelling 6,084 vs 45 |
| `alquezar` | `alquézar` | 45 | accented spelling 404 vs 45 |
| `acidos` | `ácido` | 45 | accented spelling 14,769 vs 45 |
| `malargue` | `malargüe` | 45 | accented spelling 304 vs 45 |
| `numeracion` | `numeración` | 45 | accented spelling 5,495 vs 45 |
| `melodias` | `melodía` | 45 | accented spelling 4,548 vs 45 |
| `traore` | `traoré` | 45 | accented spelling 322 vs 45 |
| `lios` | `lío` | 45 | accented spelling 548 vs 45 |
| `conocian` | `conocer` | 45 | accented spelling 4,219 vs 45 |
| `designo` | `designar` | 45 | accented spelling 1,910 vs 45 |
| `santillan` | `santillán` | 45 | accented spelling 396 vs 45 |
| `yemeni` | `yemení` | 45 | accented spelling 2,102 vs 45 |
| `inmersion` | `inmersión` | 45 | accented spelling 32,293 vs 45 |
| `morazan` | `morazán` | 45 | accented spelling 766 vs 45 |
| `aureo` | `áureo` | 45 | accented spelling 745 vs 45 |
| `asignacion` | `asignación` | 45 | accented spelling 45,681 vs 45 |
| `perello` | `perelló` | 45 | accented spelling 454 vs 45 |
| `tonteria` | `tontería` | 45 | accented spelling 4,796 vs 45 |
| `rosello` | `roselló` | 45 | accented spelling 288 vs 45 |
| `madian` | `madián` | 45 | accented spelling 3,836 vs 45 |
| `angiogenesis` | `angiogénesis` | 44 | accented spelling 834 vs 44 |
| `ortopedico` | `ortopédico` | 44 | accented spelling 5,717 vs 44 |
| `trifasico` | `trifásico` | 44 | accented spelling 4,620 vs 44 |
| `caldereria` | `calderería` | 44 | accented spelling 563 vs 44 |
| `mayoria` | `mayoría` | 44 | accented spelling 705,481 vs 44 |
| `pielago` | `piélago` | 44 | accented spelling 252 vs 44 |
| `elian` | `elián` | 44 | accented spelling 744 vs 44 |
| `fraccion` | `fracción` | 44 | accented spelling 23,930 vs 44 |
| `renteria` | `rentería` | 44 | accented spelling 468 vs 44 |
| `tajin` | `tajín` | 44 | accented spelling 336 vs 44 |
| `hipertension` | `hipertensión` | 44 | accented spelling 24,306 vs 44 |
| `rodano` | `ródano` | 44 | accented spelling 1,940 vs 44 |

### Dropped by 2+ flags: random sample of 0 of 0 in the window

| rank | lemma | flags |
|---:|---|---|

### Single flag, not yet reviewed: 0 (kept until reviewed)


Reviewed decisions applied in the window: 36,395 (keep 10,276, drop 26,119); review merges: 6,917.
