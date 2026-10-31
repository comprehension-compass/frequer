# Review report: es (pilot)

- Ranking score: `frequency`; 141,164 candidate lemmas ranked.
- Tokens counted: 7,388,304 in 10,252 documents, 13 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_es` 1.4.0 (sha256 `0e8332b292b93e4e`); fallback `spacy-list`, units on; honeyeater `0e1c3bbbd941`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| paracrawl-en-es | 12 | 8,508 | 326,450 | 6,733,917 | alpha 2,702, exact_dup 818, gap 2,530, langid 86,346, length 6,514, near_dup 40 |
| tatoeba-spa | 1 | 1,744 | 86,798 | 654,387 | alpha 8, gap 16, length 71, near_dup 307 |

Japanese-style host tokens (an ending that took its host's lemma): 0. Occurrences not counted (punctuation, a lemma failing the language pattern): 110,070. Sentences: 435,871.

## Units

Counted occurrences by kind: compound 48,751 (0.66%), compound1 55,485 (0.75%), construction 147,498 (2.00%), phrase 132,853 (1.80%), word 7,003,717 (94.79%). A compound replaces its member words (a compound is a word); a phrase or construction counts next to its member words.

| unit type | distinct headwords found | occurrences found |
|---|---|---|
| compound | 2,987 | 111,706 |
| construction | 20 | 148,565 |
| phrase | 808 | 132,854 |

### Top compound units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `encontrarse` | 3,986 | 3,240 | 189 |
| `sitio web` | 2,671 | 2,087 | 287 |
| `Estados Unidos` | 2,271 | 1,927 | 360 |
| `internacional` | 2,048 | 1,752 | 261 |
| `por qué` | 1,776 | 1,502 | 484 |
| `correo electrónico` | 1,602 | 1,413 | 527 |
| `convertirse` | 1,553 | 1,417 | 2203 |
| `directamente` | 1,361 | 1,273 | 631 |
| `realmente` | 1,175 | 1,068 | 740 |
| `quedarse` | 1,150 | 994 | 837 |
| `simplemente` | 1,119 | 1,050 | 786 |
| `tratarse` | 1,114 | 1,035 | 2494 |
| `asegurarse` | 1,076 | 1,011 | 1560 |
| `especialmente` | 1,043 | 977 | 841 |
| `irse` | 1,022 | 874 | 865 |
| `actualmente` | 1,012 | 951 | 872 |
| `completamente` | 969 | 916 | 919 |
| `totalmente` | 955 | 892 | 937 |
| `sentirse` | 955 | 870 | 935 |
| `Nueva York` | 921 | 827 | 970 |
| `rápidamente` | 797 | 770 | 1105 |
| `ponerse` | 793 | 747 | 1253 |
| `solamente` | 757 | 720 | 1167 |
| `verse` | 737 | 690 | 1268 |
| `fácilmente` | 736 | 708 | 1200 |

### Top construction units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `poder + infinitivo` | 42,579 | 9,983 | 22 |
| `haber + participio` | 31,626 | 9,587 | 27 |
| `se + verbo (impersonal/pasiva)` | 27,947 | 9,102 | 30 |
| `ser + participio` | 15,194 | 7,577 | 37 |
| `estar + gerundio` | 11,550 | 6,758 | 46 |
| `tener que + infinitivo` | 4,126 | 3,286 | 162 |
| `al + infinitivo` | 4,000 | 3,202 | 176 |
| `ir a + infinitivo` | 3,327 | 2,580 | 220 |
| `seguir + gerundio` | 1,610 | 1,475 | 523 |
| `no … nada` | 1,310 | 1,138 | 658 |
| `volver a + infinitivo` | 1,030 | 942 | 857 |
| `comenzar a + infinitivo` | 902 | 854 | 988 |
| `empezar a + infinitivo` | 894 | 831 | 995 |
| `soler + infinitivo` | 845 | 790 | 1040 |
| `dejar de + infinitivo` | 790 | 740 | 1112 |
| `acabar de + infinitivo` | 517 | 459 | 1584 |
| `no … nadie` | 206 | 198 | 3209 |
| `lo + adjetivo` | 100 | 98 | 5065 |
| `hacer que + subjuntivo` | 9 | 9 | 20116 |
| `tener + N + años` | 3 | 3 | 41995 |

### Top phrase units

| headword | found | documents | snapshot rank |
|---|---|---|---|
| `después de` | 3,997 | 3,225 | 174 |
| `a través de` | 3,965 | 3,120 | 177 |
| `para que` | 3,703 | 3,016 | 195 |
| `antes de` | 2,894 | 2,489 | 265 |
| `cerca de` | 2,826 | 2,413 | 274 |
| `acerca de` | 2,658 | 2,240 | 289 |
| `sin embargo` | 2,418 | 2,114 | 328 |
| `así como` | 2,411 | 2,086 | 331 |
| `por favor` | 2,309 | 1,818 | 347 |
| `dentro de` | 2,165 | 1,865 | 376 |
| `por ejemplo` | 1,965 | 1,725 | 425 |
| `ya que` | 1,741 | 1,573 | 487 |
| `gracias a` | 1,405 | 1,284 | 610 |
| `así que` | 1,399 | 1,293 | 614 |
| `por lo que` | 1,359 | 1,251 | 633 |
| `en línea` | 1,333 | 1,193 | 643 |
| `convertirse en algo` | 1,240 | 1,154 | 699 |
| `además de` | 1,220 | 1,136 | 711 |
| `debido a` | 1,195 | 1,124 | 727 |
| `a partir de` | 1,169 | 1,075 | 741 |
| `alrededor de` | 1,154 | 1,076 | 755 |
| `a continuación` | 1,112 | 1,044 | 790 |
| `fuera de` | 1,083 | 1,004 | 812 |
| `contar con algo` | 1,000 | 941 | 882 |
| `mientras que` | 983 | 924 | 903 |

## Co-occurrence (association) table

7,163,012 tokens, 435,871 sentences. After merging and dropping items seen fewer than 5 times: 376,721 items (unigrams, UPOS votes, n-grams, pairs); 309,577 n-grams and pairs scored (n2 122,412, n3 130,028, n4 56,019, p2 1,118). Shipped: 195,099 rows, 3.3 MB gzipped (`es.cooc.tsv.gz`). Measures and the selection are in README §Co-occurrence.

### Labelling queue: top associated combinations not on the unit list

`es.cooc-queue.tsv` holds 2,000; the first 50 here.

| # | kind | keys | head | f | docs | PMI min | NPMI min | G2 min | extends listed |
|---|---|---|---|---|---|---|---|---|---|
| 1 | n | `mejor precio` |  | 4,226 | 3,307 | 7.71 | 0.72 | 40,268 |  |
| 2 | n | `low cost` |  | 1,519 | 1,393 | 12.18 | 1.00 | 28,444 |  |
| 3 | n | `respuesta rápido de personal` |  | 1,588 | 1,448 | 10.37 | 0.85 | 23,317 |  |
| 4 | n | `más barato` |  | 2,524 | 2,183 | 6.79 | 0.59 | 20,827 |  |
| 5 | n | `regular o vuelo low` |  | 1,203 | 1,130 | 11.77 | 0.94 | 20,546 |  |
| 6 | n | `pasaje aereo` |  | 1,192 | 627 | 12.01 | 0.96 | 20,487 |  |
| 7 | n | `buscar el mejor precio` |  | 1,520 | 1,393 | 9.51 | 0.78 | 20,224 |  |
| 8 | n | `no haber` |  | 5,125 | 3,991 | 3.95 | 0.38 | 19,462 |  |
| 9 | n | `continuar con la búsqueda` |  | 1,184 | 1,109 | 11.23 | 0.89 | 18,922 |  |
| 10 | n | `personal y los huésped` |  | 1,245 | 1,150 | 10.36 | 0.83 | 18,082 |  |
| 11 | n | `ser posible` |  | 2,861 | 2,449 | 5.30 | 0.47 | 17,801 |  |
| 12 | n | `buscador de vuelo` |  | 1,428 | 1,311 | 9.21 | 0.75 | 17,732 |  |
| 13 | n | `manual de instrucción` |  | 1,124 | 1,045 | 11.26 | 0.89 | 17,316 |  |
| 14 | n | `mejor precio en jetcost` |  | 1,372 | 1,276 | 8.92 | 0.72 | 17,106 |  |
| 15 | n | `vuelo regular o vuelo` |  | 1,203 | 1,130 | 9.35 | 0.75 | 15,738 |  |
| 16 | n | `precio para su vuelo` |  | 1,203 | 1,114 | 9.35 | 0.75 | 15,722 |  |
| 17 | n | `estar buscar el mejor` |  | 1,520 | 1,393 | 7.37 | 0.60 | 15,513 |  |
| 18 | n | `me gustar` |  | 1,473 | 1,125 | 8.19 | 0.67 | 14,717 |  |
| 19 | n | `alto calidad` |  | 1,389 | 1,268 | 8.50 | 0.69 | 14,425 |  |
| 20 | n | `vuelo low cost` |  | 1,208 | 1,135 | 9.02 | 0.72 | 14,265 |  |
| 21 | n | `estar buscar` |  | 2,174 | 1,937 | 5.82 | 0.50 | 14,188 |  |
| 22 | n | `que no` |  | 6,659 | 4,806 | 2.56 | 0.25 | 13,371 |  |
| 23 | n | `ser muy` |  | 2,817 | 2,411 | 4.24 | 0.37 | 12,143 |  |
| 24 | n | `tipo de` |  | 3,586 | 2,884 | 3.08 | 0.28 | 11,929 |  |
| 25 | n | `creer que` |  | 2,057 | 1,688 | 4.94 | 0.42 | 11,781 |  |
| 26 | n | `posible que no haber` |  | 1,186 | 1,111 | 7.31 | 0.58 | 11,777 |  |
| 27 | n | `para encontrar los vuelo` |  | 1,375 | 1,274 | 6.26 | 0.51 | 11,586 |  |
| 28 | n | `pronóstico de tiempo` |  | 886 | 839 | 9.19 | 0.71 | 10,843 |  |
| 29 | n | `querer continuar con` |  | 1,184 | 1,109 | 6.52 | 0.52 | 10,668 |  |
| 30 | n | `ser posible que` |  | 1,835 | 1,650 | 4.94 | 0.41 | 10,537 |  |
| 31 | n | `información sobre` |  | 1,509 | 1,376 | 6.24 | 0.51 | 10,461 |  |
| 32 | n | `relacionar con` |  | 1,412 | 1,273 | 5.96 | 0.48 | 10,182 |  |
| 33 | n | `decir que` |  | 2,882 | 2,389 | 3.63 | 0.32 | 9,950 |  |
| 34 | n | `ser posible que no` |  | 1,225 | 1,146 | 5.97 | 0.48 | 9,667 |  |
| 35 | n | `mejor precio para` |  | 1,683 | 1,526 | 4.99 | 0.41 | 9,145 |  |
| 36 | n | `que no haber resultado` |  | 1,185 | 1,109 | 5.56 | 0.44 | 8,997 |  |
| 37 | n | `a los mejor precio` |  | 1,505 | 1,393 | 4.90 | 0.40 | 8,769 |  |
| 38 | n | `billete avión` |  | 585 | 298 | 11.16 | 0.82 | 8,493 |  |
| 39 | n | `en vuelo regular` |  | 1,203 | 1,130 | 5.11 | 0.41 | 8,481 |  |
| 40 | n | `obtener respuesta rápido de` |  | 1,540 | 1,405 | 3.58 | 0.29 | 7,613 |  |
| 41 | n | `estar disponible` |  | 1,116 | 1,040 | 5.92 | 0.47 | 7,442 |  |
| 42 | n | `comparar tu pasaje aereo` |  | 551 | 540 | 10.30 | 0.75 | 7,197 |  |
| 43 | n | `política de privacidad` |  | 498 | 463 | 11.01 | 0.80 | 7,116 |  |
| 44 | n | `acceso a` |  | 1,474 | 1,309 | 4.41 | 0.36 | 7,081 |  |
| 45 | n | `cosa que hacer` |  | 792 | 749 | 7.26 | 0.55 | 6,987 |  |
| 46 | n | `alquiler de vacaciones` |  | 537 | 498 | 10.20 | 0.74 | 6,930 |  |
| 47 | n | `necesario para` |  | 1,252 | 1,159 | 5.01 | 0.40 | 6,846 |  |
| 48 | n | `dato personal` |  | 796 | 676 | 7.42 | 0.57 | 6,836 |  |
| 49 | n | `utilizar nuestro buscador de` |  | 1,361 | 1,260 | 3.58 | 0.29 | 6,738 |  |
| 50 | n | `más información` |  | 1,404 | 1,290 | 4.72 | 0.38 | 6,727 |  |

### Verb pairs in the queue

| keys | head | f | docs | PMI | NPMI | G2 |
|---|---|---|---|---|---|---|
| `reservar se` | `reservarse` | 382 | 370 | 6.27 | 0.44 | 2,643 |
| `visualizar se` | `visualizarse` | 103 | 101 | 7.42 | 0.46 | 904 |
| `proporcionar se` | `proporcionarse` | 146 | 145 | 4.43 | 0.28 | 626 |

## Rank shifts against the live snapshot (`reference/lemmas/es.json`)

Live list 20,000 lemmas, this build 141,164; 19,449 shared. Spearman rank correlation on the shared lemmas 0.902; median rank ratio 1.16x.
Overlap of this build's top-k with the live top-k: top 1,000 85.7%, top 5,000 84.1%, top 20,000 82.8%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 1219 | -17,236 |
| `diecinueve` | 18282 | 1463 | -16,819 |
| `descanso` | 17625 | 2561 | -15,064 |
| `dividirse` | 19076 | 4062 | -15,014 |
| `respaldo` | 18269 | 3429 | -14,840 |
| `torno` | 17613 | 2900 | -14,713 |
| `seiscientos` | 17737 | 3525 | -14,212 |
| `parto` | 17982 | 4241 | -13,741 |
| `diecisiete` | 14631 | 1212 | -13,419 |
| `empotrar` | 17238 | 4178 | -13,060 |
| `entregarse` | 17153 | 4158 | -12,995 |
| `quinientos` | 14749 | 1860 | -12,889 |
| `conforme` | 15056 | 2171 | -12,885 |
| `cuatrocientos` | 15401 | 2681 | -12,720 |
| `llamarse` | 14152 | 1794 | -12,358 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `veganas` | 4951 | 136498 | +131,547 |
| `pa` | 3676 | 114219 | +110,543 |
| `mas` | 757 | 105949 | +105,192 |
| `hondura` | 3735 | 94736 | +91,001 |
| `habano` | 3196 | 92814 | +89,618 |
| `brusela` | 2422 | 71652 | +69,230 |
| `capar` | 4795 | 73104 | +68,309 |
| `véase` | 3437 | 60100 | +56,663 |
| `jamar` | 3734 | 51387 | +47,653 |
| `barbar` | 3789 | 44604 | +40,815 |
| `paris` | 2969 | 40285 | +37,316 |
| `malasio` | 4644 | 39289 | +34,645 |
| `huevar` | 4037 | 38392 | +34,355 |
| `cintar` | 1929 | 36268 | +34,339 |
| `vacación` | 390 | 34465 | +34,075 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `la` | - | 2 | - |
| `los` | - | 8 | - |
| `un` | - | 11 | - |
| `las` | - | 13 | - |
| `una` | - | 14 | - |
| `poder + infinitivo` | - | 22 | - |
| `haber + participio` | - | 27 | - |
| `se + verbo (impersonal/pasiva)` | - | 30 | - |
| `ser + participio` | - | 37 | - |
| `estar + gerundio` | - | 46 | - |
| `parte#Fem` | - | 79 | - |
| `esto` | - | 114 | - |
| `tener que + infinitivo` | - | 162 | - |
| `después de` | - | 174 | - |
| `al + infinitivo` | - | 176 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `del` | 11 | - | - |
| `parte` | 59 | 12270 | +12,211 |
| `vario` | 265 | 9421 | +9,156 |
| `relacionado` | 386 | - | - |
| `vacación` | 390 | 34465 | +34,075 |
| `real` | 425 | 5565 | +5,140 |
| `cookies` | 565 | - | - |
| `aereos` | 595 | - | - |
| `u` | 628 | 5456 | +4,828 |
| `industriar` | 661 | - | - |
| `frente` | 673 | - | - |
| `mas` | 757 | 105949 | +105,192 |
| `acondicionado` | 836 | - | - |
| `corte` | 880 | 10576 | +9,696 |
| `armar` | 912 | 6544 | +5,632 |

## Ported frequer checks

### Form-ratio outliers (15)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 596,958 | median form 14; `de` 515,058 (36790x), `del` 75,281 (5377x) |
| 7 | `que` | 149,250 | median form 1; `que` 148,500 (148500x) |
| 9 | `ser` | 113,619 | median form 17; `es` 50,643 (2979x) |
| 10 | `para` | 89,993 | median form 5; `para` 82,622 (16524x), `Para` 7,095 (1419x) |
| 12 | `con` | 77,632 | median form 13; `con` 74,486 (5730x) |
| 20 | `haber` | 43,809 | median form 10; `ha` 12,055 (1206x) |
| 43 | `también` | 11,711 | median form 3.5; `también` 9,236 (2639x) |
| 73 | `vez` | 8,636 | median form 4.5; `vez` 6,109 (1358x) |
| 81 | `ofrecer` | 7,340 | median form 3; `ofrece` 3,128 (1043x) |
| 90 | `así` | 6,712 | median form 3.5; `así` 5,451 (1557x) |
| 147 | `cinco` | 4,393 | median form 2; `5` 3,020 (1510x) |
| 164 | `cuenta` | 4,104 | median form 3; `cuenta` 3,575 (1192x) |
| 207 | `tom` | 3,490 | median form 3; `Tom` 3,486 (1162x) |
| 323 | `embargo` | 2,433 | median form 2; `embargo` 2,428 (1214x) |
| 467 | `cocina` | 1,802 | median form 1; `cocina` 1,750 (1750x) |

### Singular/plural mismatch (195)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `los` | 119,758 | `lo` lemmatises to `lo` (rank 31) |
| 13 | `las` | 73,213 | `la` lemmatises to `la` (rank 2) |
| 44 | `dos` | 11,585 | `do` lemmatises to `do` (rank 3,467) |
| 86 | `tres` | 7,033 | `tre` lemmatises to `tre` (rank 34,363) |
| 86 | `tres` | 7,033 | `tr` lemmatises to `tr` (rank 26,544) |
| 115 | `país` | 5,161 | `paí` lemmatises to `paí` (rank 115,408) |
| 133 | `nos` | 4,597 | `no` lemmatises to `no` (rank 17) |
| 136 | `antes` | 4,547 | `ante` lemmatises to `ante` (rank 778) |
| 136 | `antes` | 4,547 | `ant` lemmatises to `ant` (rank 43,773) |
| 167 | `dios` | 4,072 | `dio` lemmatises to `dar` (rank 71) |
| 182 | `menos` | 3,905 | `meno` lemmatises to `meno` (rank 15,243) |
| 193 | `ellos` | 3,744 | `ello` lemmatises to `ello` (rank 717) |
| 206 | `unos` | 3,509 | `uno` lemmatises to `uno` (rank 60) |
| 222 | `mientras` | 3,297 | `mientra` lemmatises to `mientra` (rank 107,772) |
| 256 | `les` | 2,985 | `le` lemmatises to `le` (rank 40) |
| 262 | `varios` | 2,911 | `vario` lemmatises to `vario` (rank 9,421) |
| 270 | `mes` | 2,851 | `me` lemmatises to `me` (rank 63) |
| 298 | `seis` | 2,612 | `sei` lemmatises to `sei` (rank 33,891) |
| 307 | `inglés` | 2,563 | `inglé` lemmatises to `inglé` (rank 96,867) |
| 367 | `gracias` | 2,231 | `gracia` lemmatises to `gracia` (rank 2,993) |
| 387 | `vacaciones` | 2,127 | `vacacion` lemmatises to `vacacion` (rank 59,626) |
| 580 | `tras` | 1,474 | `tra` lemmatises to `tra` (rank 29,726) |
| 803 | `pues` | 1,098 | `pue` lemmatises to `pue` (rank 40,761) |
| 803 | `pues` | 1,098 | `pu` lemmatises to `pu` (rank 6,356) |
| 820 | `ambos` | 1,074 | `ambo` lemmatises to `ambo` (rank 30,148) |

_170 more not shown._

### Lemma consistency (306)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 166 | `programa` | 4,074 | alone, `programa` lemmatises to `programar` (rank 1,977) |
| 330 | `pregunta` | 2,412 | alone, `pregunta` lemmatises to `preguntar` (rank 674) |
| 534 | `hecho` | 1,583 | alone, `hecho` lemmatises to `hacer` (rank 32) |
| 561 | `dicho` | 1,512 | alone, `dicho` lemmatises to `decir` (rank 51) |
| 571 | `china` | 1,486 | alone, `china` lemmatises to `chino` (rank 1,502) |
| 604 | `fuera` | 1,422 | alone, `fuera` lemmatises to `ser` (rank 9) |
| 659 | `presente` | 1,307 | alone, `presente` lemmatises to `presentar` (rank 308) |
| 661 | `abierto` | 1,304 | alone, `abierto` lemmatises to `abrir` (rank 327) |
| 722 | `visita` | 1,199 | alone, `visita` lemmatises to `visitar` (rank 353) |
| 736 | `compra` | 1,177 | alone, `compra` lemmatises to `comprar` (rank 198) |
| 818 | `causa` | 1,075 | alone, `causa` lemmatises to `causar` (rank 682) |
| 822 | `video` | 1,071 | alone, `video` lemmatises to `vídeo` (rank 754) |
| 941 | `carga` | 948 | alone, `carga` lemmatises to `cargar` (rank 1,505) |
| 986 | `pedido` | 908 | alone, `pedido` lemmatises to `pedir` (rank 429) |
| 1061 | `parís` | 832 | alone, `parís` lemmatises to `parir` (rank 10,896) |
| 1089 | `deseo` | 810 | alone, `deseo` lemmatises to `desear` (rank 306) |
| 1150 | `londres` | 765 | alone, `londres` lemmatises to `londr` (rank 52,591) |
| 1187 | `muestra` | 745 | alone, `muestra` lemmatises to `mostrar` (rank 204) |
| 1199 | `avanzado` | 738 | alone, `avanzado` lemmatises to `avanzar` (rank 1,953) |
| 1217 | `vino` | 724 | alone, `vino` lemmatises to `venir` (rank 208) |
| 1225 | `empleado` | 720 | alone, `empleado` lemmatises to `emplear` (rank 1,739) |
| 1252 | `llamada` | 691 | alone, `llamada` lemmatises to `llamar` (rank 214) |
| 1254 | `aumento` | 690 | alone, `aumento` lemmatises to `aumentar` (rank 455) |
| 1270 | `tejido` | 679 | alone, `tejido` lemmatises to `tejer` (rank 3,240) |
| 1307 | `windows` | 650 | alone, `windows` lemmatises to `window` (rank 16,071) |

_281 more not shown._

### Short lemmas (184)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `de` | 596,958 | `de` -> `de`, `del` -> `de`, `Del` -> `de`, `De` -> `de`, `DE` -> `de` |
| 2 | `la` | 240,927 | `La` -> `la`, `la` -> `la`, `LA` -> `la` |
| 3 | `en` | 206,953 | `en` -> `en`, `En` -> `en`, `EN` -> `en` |
| 4 | `y` | 199,375 | `y` -> `y`, `Y` -> `y`, `e` -> `y`, `yes` -> `y` |
| 5 | `el` | 194,929 | `el` -> `el`, `El` -> `el`, `EL` -> `el` |
| 6 | `a` | 172,378 | `al` -> `a`, `a` -> `a`, `A` -> `a`, `Al` -> `a`, `AL` -> `a` |
| 11 | `un` | 78,639 | `un` -> `un`, `Un` -> `un`, `UN` -> `un` |
| 15 | `su` | 62,906 | `su` -> `su`, `sus` -> `su`, `Su` -> `su`, `Sus` -> `su`, `SUS` -> `su` |
| 17 | `no` | 54,251 | `no` -> `no`, `No` -> `no`, `NO` -> `no` |
| 19 | `se` | 44,995 | `se` -> `se`, `Se` -> `se`, `te` -> `te`, `SE` -> `se`, `me` -> `me` |
| 25 | `o` | 35,881 | `o` -> `o`, `ó` -> `o`, `u` -> `o`, `O` -> `o`, `o.` -> `?` |
| 31 | `lo` | 26,417 | `lo` -> `lo`, `Lo` -> `lo`, `LO` -> `lo`, `lA` -> `lo` |
| 33 | `tu` | 20,694 | `tus` -> `tu`, `tu` -> `tu`, `Tu` -> `tu`, `Tus` -> `tu`, `TU` -> `tu` |
| 35 | `si` | 19,497 | `Si` -> `si`, `si` -> `si`, `SI` -> `si`, `sis` -> `si` |
| 40 | `le` | 11,950 | `le` -> `le`, `Le` -> `le`, `LE` -> `le` |
| 42 | `mi` | 11,866 | `mi` -> `mi`, `mis` -> `mi`, `Mi` -> `mi`, `Mis` -> `mi`, `MI` -> `mi` |
| 58 | `él` | 10,482 | `él` -> `él`, `Él` -> `él`, `ÉL` -> `él` |
| 63 | `me` | 10,019 | `me` -> `me`, `Me` -> `me`, `ME` -> `me` |
| 67 | `ir` | 9,738 | `fuese` -> `ir`, `iba` -> `ir`, `va` -> `ir`, `van` -> `ir`, `íbamos` -> `ir` |
| 77 | `te` | 8,261 | `te` -> `te`, `Te` -> `te`, `TE` -> `te`, `tes` -> `te` |
| 91 | `ya` | 6,697 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya`, `-ya` -> `ya` |
| 121 | `yo` | 5,017 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo` |
| 233 | `ni` | 3,152 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni`, `ninos` -> `nino` |
| 404 | `sí` | 2,037 | `sí` -> `sí`, `Sí` -> `sí`, `SÍ` -> `sí`, `si` -> `si` |
| 436 | `tú` | 1,923 | `tú` -> `tú`, `Tú` -> `tú`, `TÚ` -> `tú` |

_159 more not shown._

### Case merges (2)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 3347 | `pendiente#Masc` | 194 | capitalised but mostly ADJ; no lowercase twin |
| 5049 | `editorial#Fem` | 100 | capitalised but mostly ADJ; no lowercase twin |

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 696 (69.6%).

Ours only: `poder + infinitivo`, `haber + participio`, `se + verbo (impersonal/pasiva)`, `ser + participio`, `estar + gerundio`, `vuelo`, `hotel`, `habitación`, `barato`, `archivo`, `tener que + infinitivo`, `después de`, `al + infinitivo`, `a través de`, `encontrarse`, `para que`, `tom`, `diseño`, `ir a + infinitivo`, `alojamiento`, `disponible`, `oferta`, `internacional`, `antes de`, `alquiler`

wordfreq only: `mal`, `dr`, `ahí`, `argentino`, `cero`, `unido`, `falta`, `mierda`, `i`, `c`, `orden#Fem`, `viejo`, `policía`, `elección`, `programar`, `juan`, `demás`, `peor`, `voz`, `hola`, `paz`, `militar`, `cargo`, `matar`, `cara`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 529 | `cookie` | 1,596 | wordfreq zipf en 4.1 vs es 3.0 |
| 550 | `low` | 1,543 | wordfreq zipf en 5.3 vs es 3.6 |
| 560 | `cost` | 1,522 | wordfreq zipf en 5.2 vs es 3.3 |
| 738 | `metro#metre` | 1,177 | wordfreq zipf en 3.6 vs es 1.6 |
| 792 | `the` | 1,112 | wordfreq zipf en 7.7 vs es 5.4 |
| 913 | `once` | 976 | wordfreq zipf en 5.5 vs es 4.4 |
| 1292 | `of` | 662 | wordfreq zipf en 7.4 vs es 5.1 |
| 1467 | `city` | 566 | wordfreq zipf en 5.6 vs es 4.3 |
| 1508 | `in` | 551 | wordfreq zipf en 7.3 vs es 5.1 |
| 1575 | `i` | 521 | wordfreq zipf en 7.1 vs es 5.4 |
| 1637 | `led` | 500 | wordfreq zipf en 5.1 vs es 3.7 |
| 1921 | `and` | 412 | wordfreq zipf en 7.4 vs es 5.0 |
| 1947 | `beach` | 407 | wordfreq zipf en 4.9 vs es 3.8 |
| 2036 | `new` | 388 | wordfreq zipf en 6.2 vs es 4.7 |
| 2053 | `resort` | 385 | wordfreq zipf en 4.4 vs es 3.3 |
| 2137 | `show` | 369 | wordfreq zipf en 5.7 vs es 4.6 |
| 2204 | `home` | 353 | wordfreq zipf en 5.8 vs es 4.0 |
| 2493 | `to` | 297 | wordfreq zipf en 7.4 vs es 4.9 |
| 2527 | `house` | 290 | wordfreq zipf en 5.7 vs es 4.2 |
| 2877 | `black` | 239 | wordfreq zipf en 5.5 vs es 4.3 |
| 2933 | `by` | 233 | wordfreq zipf en 6.7 vs es 4.5 |
| 2947 | `stock` | 232 | wordfreq zipf en 4.9 vs es 3.8 |
| 2953 | `top` | 231 | wordfreq zipf en 5.6 vs es 4.4 |
| 3006 | `real#royal` | 226 | wordfreq zipf en 4.8 vs es 3.7 |
| 3058 | `grand` | 219 | wordfreq zipf en 4.9 vs es 3.9 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 167 | `dios` | 4,072 | PROPN 0%, capitalised forms 94% |
| 207 | `tom` | 3,490 | PROPN 100%, capitalised forms 100% |
| 360 | `estados unidos` | 2,271 | PROPN 0%, capitalised forms 100% |
| 460 | `españa` | 1,836 | PROPN 100%, capitalised forms 100% |
| 498 | `jetcost` | 1,711 | PROPN 100%, capitalised forms 100% |
| 531 | `san` | 1,594 | PROPN 2%, capitalised forms 95% |
| 571 | `china` | 1,486 | PROPN 100%, capitalised forms 100% |
| 640 | `tripadvisor` | 1,337 | PROPN 100%, capitalised forms 100% |
| 655 | `jesús` | 1,314 | PROPN 100%, capitalised forms 100% |
| 730 | `europa` | 1,188 | PROPN 99%, capitalised forms 99% |
| 739 | `méxico` | 1,176 | PROPN 100%, capitalised forms 100% |
| 777 | `tv` | 1,132 | PROPN 4%, capitalised forms 97% |
| 792 | `the` | 1,112 | PROPN 97%, capitalised forms 78% |
| 892 | `barcelona` | 989 | PROPN 99%, capitalised forms 99% |
| 927 | `madrid` | 959 | PROPN 99%, capitalised forms 100% |
| 934 | `google` | 955 | PROPN 98%, capitalised forms 98% |
| 970 | `nueva york` | 921 | PROPN 100%, capitalised forms 100% |
| 978 | `mary` | 913 | PROPN 100%, capitalised forms 100% |
| 1061 | `parís` | 832 | PROPN 100%, capitalised forms 100% |
| 1134 | `japón` | 775 | PROPN 99%, capitalised forms 99% |
| 1138 | `israel` | 773 | PROPN 100%, capitalised forms 100% |
| 1150 | `londres` | 765 | PROPN 100%, capitalised forms 100% |
| 1204 | `francia` | 734 | PROPN 100%, capitalised forms 100% |
| 1240 | `cristo` | 705 | PROPN 99%, capitalised forms 100% |
| 1292 | `of` | 662 | PROPN 86%, capitalised forms 6% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 98.8% | 0.998 |
| juilland_u | 99.7% | 1.000 |
| juilland_u_corrected | 99.7% | 1.000 |
| dp_adjusted | 98.9% | 0.999 |
| cd_blend | 99.4% | 0.999 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `retener` | 4724 | 4553 | -171 | 112 | 112 | 0.900 | 0.374 |
| `sofisticado` | 4694 | 4525 | -169 | 113 | 113 | 0.905 | 0.373 |
| `supervivencia` | 4927 | 4759 | -168 | 105 | 105 | 0.894 | 0.419 |
| `súper` | 4670 | 4502 | -168 | 114 | 114 | 0.914 | 0.342 |
| `industry` | 4583 | 4420 | -163 | 117 | 117 | 0.914 | 0.341 |
| `love` | 3186 | 5209 | +2,023 | 208 | 90 | 0.862 | 0.530 |
| `ascendente` | 3702 | 5454 | +1,752 | 164 | 83 | 0.872 | 0.498 |
| `remate` | 4266 | 5981 | +1,715 | 131 | 71 | 0.881 | 0.489 |
| `tortuga` | 4566 | 5933 | +1,367 | 118 | 72 | 0.698 | 0.545 |
| `tiquete` | 2496 | 3765 | +1,269 | 296 | 150 | 0.913 | 0.347 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `síntesis` | 5034 | 4960 | -74 | 101 | 100 | 0.914 | 0.314 |
| `exquisito` | 4769 | 4698 | -71 | 110 | 109 | 0.921 | 0.285 |
| `materno` | 4914 | 4845 | -69 | 105 | 104 | 0.913 | 0.334 |
| `rendir` | 4823 | 4756 | -67 | 108 | 108 | 0.919 | 0.300 |
| `recomendable` | 4750 | 4684 | -66 | 111 | 110 | 0.917 | 0.324 |
| `torta` | 4382 | 5149 | +767 | 126 | 78 | 0.690 | 0.547 |
| `tortuga` | 4566 | 5300 | +734 | 118 | 72 | 0.698 | 0.545 |
| `helicóptero` | 4604 | 4996 | +392 | 116 | 94 | 0.786 | 0.429 |
| `desafortunado` | 4136 | 4330 | +194 | 137 | 117 | 0.846 | 0.410 |
| `love` | 3186 | 3346 | +160 | 208 | 90 | 0.862 | 0.530 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `sudáfrica` | 4511 | 4469 | -42 | 120 | 119 | 0.915 | 0.336 |
| `silencioso` | 4753 | 4713 | -40 | 111 | 108 | 0.915 | 0.330 |
| `refrigeración` | 4507 | 4467 | -40 | 120 | 111 | 0.909 | 0.373 |
| `terrestre` | 4754 | 4714 | -40 | 111 | 108 | 0.912 | 0.345 |
| `ronda` | 4508 | 4468 | -40 | 120 | 117 | 0.909 | 0.371 |
| `torta` | 4382 | 5173 | +791 | 126 | 78 | 0.690 | 0.547 |
| `tortuga` | 4566 | 5346 | +780 | 118 | 72 | 0.698 | 0.545 |
| `helicóptero` | 4604 | 5015 | +411 | 116 | 94 | 0.786 | 0.429 |
| `desafortunado` | 4136 | 4339 | +203 | 137 | 117 | 0.846 | 0.410 |
| `love` | 3186 | 3347 | +161 | 208 | 90 | 0.862 | 0.530 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `exquisito` | 4769 | 4390 | -379 | 110 | 109 | 0.921 | 0.285 |
| `rendir` | 4823 | 4470 | -353 | 108 | 108 | 0.919 | 0.300 |
| `síntesis` | 5034 | 4695 | -339 | 101 | 100 | 0.914 | 0.314 |
| `rasgo` | 5296 | 4962 | -334 | 93 | 92 | 0.911 | 0.330 |
| `parche` | 4970 | 4639 | -331 | 103 | 100 | 0.913 | 0.312 |
| `torta` | 4382 | 5164 | +782 | 126 | 78 | 0.690 | 0.547 |
| `tortuga` | 4566 | 5299 | +733 | 118 | 72 | 0.698 | 0.545 |
| `love` | 3186 | 3918 | +732 | 208 | 90 | 0.862 | 0.530 |
| `ascendente` | 3702 | 4276 | +574 | 164 | 83 | 0.872 | 0.498 |
| `remate` | 4266 | 4772 | +506 | 131 | 71 | 0.881 | 0.489 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `supervivencia` | 4927 | 4814 | -113 | 105 | 105 | 0.894 | 0.419 |
| `súper` | 4670 | 4564 | -106 | 114 | 114 | 0.914 | 0.342 |
| `resumir` | 4972 | 4871 | -101 | 103 | 103 | 0.886 | 0.441 |
| `retener` | 4724 | 4623 | -101 | 112 | 112 | 0.900 | 0.374 |
| `xix` | 4170 | 4069 | -101 | 136 | 136 | 0.911 | 0.355 |
| `love` | 3186 | 4059 | +873 | 208 | 90 | 0.862 | 0.530 |
| `remate` | 4266 | 5099 | +833 | 131 | 71 | 0.881 | 0.489 |
| `ascendente` | 3702 | 4495 | +793 | 164 | 83 | 0.872 | 0.498 |
| `tortuga` | 4566 | 5225 | +659 | 118 | 72 | 0.698 | 0.545 |
| `torta` | 4382 | 5002 | +620 | 126 | 78 | 0.690 | 0.547 |

