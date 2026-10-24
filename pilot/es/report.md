# Review report: es (pilot)

- Ranking score: `frequency`; 66,916 candidate lemmas ranked.
- Tokens counted: 2,243,868 in 3,381 documents, 8 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_es` 0.0.1 (sha256 `165b1bf74ea54292`); honeyeater `f4495a68bf53`; overrides sha256 `bacb3760dd87f928`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| paracrawl-en-es | 7 | 2,589 | 99,390 | 1,974,498 | alpha 799, exact_dup 182, gap 728, langid 26,350, length 1,996, near_dup 5 |
| tatoeba-spa | 1 | 792 | 39,449 | 269,370 | alpha 3, gap 7, length 21, near_dup 120 |

## How the runtime decided the lemmas

Tokens by deciding layer: backend 18.2%, model 10.2%, table 71.7%.
Tokens the lemma step resolved to their host's lemma: 0. Sentences where an independent replay of the step disagreed with it: 0 of 145,921.

### Override file against the lemma step

The backend's lemma has the override file applied before the lemma step, but the step prefers its list for a form it knows. Of 348,678 tokens whose surface the override file names, the step emitted a different lemma for 7,969 (top 25 below, as counted in the 111 kept per shard).

| surface | override says | step emitted | tokens |
|---|---|---|---|
| `nos` | `nos` | `se` | 648 |
| `la` | `el` | `la` | 560 |
| `cuenta` | `cuenta` | `contar` | 512 |
| `los` | `el` | `los` | 434 |
| `estado` | `estado` | `estar` | 394 |
| `varias` | `vario` | `varios` | 336 |
| `muestra` | `muestra` | `mostrar` | 297 |
| `relacionados` | `relacionado` | `relacionar` | 280 |
| `falta` | `faltar` | `falta` | 279 |
| `ayuda` | `ayuda` | `ayudar` | 269 |
| `acondicionado` | `acondicionado` | `acondicionar` | 269 |
| `prácticas` | `práctica` | `práctico` | 169 |
| `mejora` | `mejora` | `mejorar` | 167 |
| `reglas` | `reglas` | `regla` | 146 |
| `dicha` | `dicha` | `dicho` | 142 |
| `ustedes` | `usted` | `ustedes` | 137 |
| `relacionadas` | `relacionado` | `relacionar` | 128 |
| `puesta` | `puesta` | `poner` | 127 |
| `las` | `el` | `las` | 116 |
| `aguas` | `aguas` | `agua` | 107 |
| `privado` | `privado` | `privar` | 97 |
| `relacionado` | `relacionado` | `relacionar` | 97 |
| `trabajo` | `trabajo` | `trabajar` | 90 |
| `juego` | `juego` | `jugar` | 89 |
| `cuadrados` | `cuadro` | `cuadrado` | 79 |

## Rank shifts against the live snapshot (`reference/lemmas/es.json`)

Live list 20,000 lemmas, this build 66,916; 19,361 shared. Spearman rank correlation on the shared lemmas 0.893; median rank ratio 1.19x.
Overlap of this build's top-k with the live top-k: top 1,000 90.5%, top 5,000 89.1%, top 20,000 81.8%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `acondicionar` | 18455 | 979 | -17,476 |
| `descanso` | 17625 | 2252 | -15,373 |
| `respaldo` | 18269 | 3442 | -14,827 |
| `torno` | 17613 | 2797 | -14,816 |
| `parto` | 17982 | 3323 | -14,659 |
| `adónde` | 15294 | 4808 | -10,486 |
| `tele` | 13853 | 3589 | -10,264 |
| `adecuar` | 13186 | 3142 | -10,044 |
| `fracaso` | 13578 | 3873 | -9,705 |
| `anoche` | 11693 | 2453 | -9,240 |
| `ken` | 11939 | 2867 | -9,072 |
| `nevar` | 12047 | 3194 | -8,853 |
| `enfadar` | 10986 | 2399 | -8,587 |
| `privar` | 10497 | 1945 | -8,552 |
| `incremento` | 11988 | 3566 | -8,422 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `ponerse` | 2137 | 56150 | +54,013 |
| `ponte` | 3426 | 56158 | +52,732 |
| `orlar` | 2655 | 54334 | +51,679 |
| `huevar` | 4037 | 45816 | +41,779 |
| `habano` | 3196 | 44657 | +41,461 |
| `darle` | 2317 | 38545 | +36,228 |
| `convertirse` | 2263 | 37599 | +35,336 |
| `darte` | 4768 | 38554 | +33,786 |
| `castrar` | 4982 | 35774 | +30,792 |
| `asegurarse` | 2744 | 32421 | +29,677 |
| `mantenerse` | 3347 | 26281 | +22,934 |
| `malasio` | 4644 | 26238 | +21,594 |
| `hondura` | 3735 | 25193 | +21,458 |
| `darse` | 3656 | 23414 | +19,758 |
| `abortar` | 3743 | 21378 | +17,635 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `esto` | - | 114 | - |
| `eso` | - | 219 | - |
| `varios` | - | 269 | - |
| `gracias` | - | 314 | - |
| `san` | - | 315 | - |
| `vacaciones` | - | 377 | - |
| `reserva` | - | 418 | - |
| `la` | - | 448 | - |
| `política` | - | 450 | - |
| `pasado` | - | 485 | - |
| `tema` | - | 525 | - |
| `debido` | - | 529 | - |
| `fuera` | - | 544 | - |
| `china` | - | 566 | - |
| `los` | - | 601 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `vario` | 265 | - | - |
| `relacionado` | 386 | 10899 | +10,513 |
| `acondicionado` | 836 | 7474 | +6,638 |
| `dicha` | 1152 | 12404 | +11,252 |
| `hacerlo` | 1220 | 16004 | +14,784 |
| `reglas` | 1354 | 6234 | +4,880 |
| `palmar` | 1362 | 6818 | +5,456 |
| `aguas` | 1570 | 7482 | +5,912 |
| `cabellar` | 1629 | 9167 | +7,538 |
| `puesta` | 1743 | 6409 | +4,666 |
| `alertar` | 1748 | 7486 | +5,738 |
| `entrevistar` | 1771 | 5166 | +3,395 |
| `st` | 1775 | 8574 | +6,799 |
| `ayudarte` | 1924 | - | - |
| `mozilla` | 1944 | 5469 | +3,525 |

## Ported frequer checks

### Form-ratio outliers (1)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 8 | `ser` | 37,049 | median form 12; `es` 16,807 (1401x) |

### Singular/plural mismatch (179)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 79 | `dos` | 2,210 | `do` lemmatises to `do` (rank 3,185) |
| 123 | `antes` | 1,536 | `ante` lemmatises to `ante` (rank 764) |
| 123 | `antes` | 1,536 | `ant` lemmatises to `ant` (rank 21,743) |
| 142 | `nos` | 1,392 | `no` lemmatises to `no` (rank 14) |
| 155 | `dios` | 1,327 | `dio` lemmatises to `dar` (rank 64) |
| 157 | `menos` | 1,320 | `meno` lemmatises to `meno` (rank 16,398) |
| 183 | `ellos` | 1,160 | `ello` lemmatises to `ello` (rank 719) |
| 197 | `tres` | 1,088 | `tr` lemmatises to `tr` (rank 21,016) |
| 240 | `mes` | 953 | `me` lemmatises to `me` (rank 35) |
| 267 | `les` | 863 | `le` lemmatises to `le` (rank 36) |
| 314 | `gracias` | 759 | `gracia` lemmatises to `gracia` (rank 2,694) |
| 377 | `vacaciones` | 655 | `vacacion` lemmatises to `vacacion` (rank 64,508) |
| 524 | `tras` | 492 | `tra` lemmatises to `tra` (rank 21,017) |
| 601 | `los` | 434 | `lo` lemmatises to `lo` (rank 23) |
| 609 | `cookies` | 425 | `cookie` lemmatises to `cookie` (rank 3,240) |
| 726 | `pues` | 359 | `pu` lemmatises to `pu` (rank 5,645) |
| 879 | `ambos` | 304 | `ambo` lemmatises to `ambo` (rank 31,348) |
| 936 | `seis` | 286 | `sei` lemmatises to `sei` (rank 28,429) |
| 1026 | `londres` | 261 | `londr` lemmatises to `londr` (rank 49,796) |
| 1051 | `ellas` | 253 | `ella` lemmatises to `ella` (rank 60) |
| 1101 | `windows` | 239 | `window` lemmatises to `window` (rank 21,268) |
| 1149 | `parís` | 229 | `parí` lemmatises to `parir` (rank 3,889) |
| 1302 | `gas` | 195 | `ga` lemmatises to `ga` (rank 13,916) |
| 1404 | `lunes` | 178 | `lune` lemmatises to `lune` (rank 50,025) |
| 1404 | `lunes` | 178 | `lun` lemmatises to `lun` (rank 11,610) |

_154 more not shown._

### Lemma consistency (233)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 94 | `trabajo` | 1,917 | alone, `trabajo` lemmatises to `trabajar` (rank 145) |
| 315 | `san` | 759 | alone, `san` lemmatises to `santo` (rank 517) |
| 370 | `lista` | 660 | alone, `lista` lemmatises to `listo` (rank 1,116) |
| 387 | `paso` | 645 | alone, `paso` lemmatises to `pasar` (rank 154) |
| 448 | `la` | 561 | alone, `la` lemmatises to `el` (rank 1) |
| 450 | `política` | 557 | alone, `política` lemmatises to `político` (rank 614) |
| 458 | `marca` | 551 | alone, `marca` lemmatises to `marcar` (rank 1,142) |
| 481 | `hecho` | 530 | alone, `hecho` lemmatises to `hacer` (rank 25) |
| 544 | `fuera` | 471 | alone, `fuera` lemmatises to `ser` (rank 8) |
| 566 | `china` | 456 | alone, `china` lemmatises to `chino` (rank 1,349) |
| 601 | `los` | 434 | alone, `los` lemmatises to `el` (rank 1) |
| 605 | `dicho` | 432 | alone, `dicho` lemmatises to `decir` (rank 43) |
| 656 | `adecuado` | 395 | alone, `adecuado` lemmatises to `adecuar` (rank 3,142) |
| 760 | `os` | 344 | alone, `os` lemmatises to `se` (rank 11) |
| 779 | `inicio` | 336 | alone, `inicio` lemmatises to `iniciar` (rank 684) |
| 907 | `vivo` | 295 | alone, `vivo` lemmatises to `vivir` (rank 190) |
| 1147 | `deseo` | 229 | alone, `deseo` lemmatises to `desear` (rank 299) |
| 1149 | `parís` | 229 | alone, `parís` lemmatises to `parir` (rank 3,889) |
| 1166 | `aumento` | 224 | alone, `aumento` lemmatises to `aumentar` (rank 463) |
| 1188 | `vino` | 219 | alone, `vino` lemmatises to `venir` (rank 153) |
| 1334 | `puesto` | 188 | alone, `puesto` lemmatises to `poner` (rank 112) |
| 1351 | `llamada` | 185 | alone, `llamada` lemmatises to `llamar` (rank 162) |
| 1412 | `aviso` | 176 | alone, `aviso` lemmatises to `avisar` (rank 3,051) |
| 1415 | `gasto` | 176 | alone, `gasto` lemmatises to `gastar` (rank 1,286) |
| 1463 | `pedido` | 169 | alone, `pedido` lemmatises to `pedir` (rank 308) |

_208 more not shown._

### Short lemmas (180)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 1 | `el` | 196,936 | `La` -> `el`, `los` -> `el`, `la` -> `el`, `el` -> `el`, `El` -> `el` |
| 2 | `de` | 185,565 | `de` -> `de`, `del` -> `de`, `Del` -> `de`, `De` -> `de`, `DE` -> `de` |
| 3 | `en` | 64,405 | `en` -> `en`, `En` -> `en`, `EN` -> `en` |
| 4 | `y` | 61,060 | `y` -> `y`, `Y` -> `y`, `e` -> `y` |
| 5 | `a` | 54,889 | `al` -> `a`, `a` -> `a`, `A` -> `a`, `Al` -> `a` |
| 11 | `se` | 22,011 | `se` -> `se`, `Se` -> `se`, `te` -> `te`, `Te` -> `te`, `Nos` -> `nos` |
| 12 | `su` | 20,150 | `su` -> `su`, `sus` -> `su`, `Su` -> `su`, `Sus` -> `su`, `SUS` -> `su` |
| 14 | `no` | 18,051 | `no` -> `no`, `No` -> `no`, `NO` -> `no`, `nos` -> `nos` |
| 21 | `o` | 11,094 | `o` -> `o`, `u` -> `o`, `O` -> `o` |
| 23 | `lo` | 8,659 | `lo` -> `lo`, `Lo` -> `lo`, `LO` -> `lo` |
| 26 | `tu` | 6,630 | `tus` -> `tu`, `tu` -> `tu`, `Tu` -> `tu`, `Tus` -> `tu`, `TU` -> `tu` |
| 27 | `si` | 6,165 | `Si` -> `si`, `si` -> `si`, `SI` -> `si` |
| 33 | `él` | 4,474 | `él` -> `él`, `Él` -> `él`, `El` -> `el`, `ÉL` -> `él` |
| 34 | `mi` | 4,374 | `mi` -> `mi`, `mis` -> `mi`, `Mi` -> `mi`, `Mis` -> `mi`, `MI` -> `mi` |
| 35 | `me` | 4,027 | `me` -> `me`, `Me` -> `me`, `ME` -> `me` |
| 36 | `le` | 4,023 | `le` -> `le`, `Le` -> `le`, `LE` -> `le`, `Les` -> `le`, `les` -> `les` |
| 38 | `ir` | 3,837 | `iba` -> `ir`, `va` -> `ir`, `van` -> `ir`, `íbamos` -> `ir`, `yendo` -> `ir` |
| 62 | `te` | 2,730 | `te` -> `te`, `Te` -> `te`, `TE` -> `te` |
| 80 | `ya` | 2,172 | `ya` -> `ya`, `Ya` -> `ya`, `YA` -> `ya` |
| 118 | `yo` | 1,564 | `yo` -> `yo`, `Yo` -> `yo`, `YO` -> `yo` |
| 217 | `ni` | 1,022 | `ni` -> `ni`, `Ni` -> `ni`, `NI` -> `ni` |
| 357 | `sí` | 681 | `sí` -> `sí`, `Sí` -> `sí`, `SÍ` -> `sí`, `si` -> `si` |
| 373 | `tú` | 657 | `tú` -> `tú`, `Tú` -> `tú` |
| 445 | `ti` | 562 | `ti` -> `ti`, `TI` -> `ti`, `Ti` -> `ti` |
| 448 | `la` | 561 | `la` -> `el`, `La` -> `el`, `las` -> `el` |

_155 more not shown._

### Case merges (0)

Non-lowercase lemmas, with the lowercase twin where one is listed.

_none_

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 732 (73.2%).

Ours only: `vuelo`, `hotel`, `habitación`, `archivo`, `barato`, `coche`, `diseño`, `alquiler`, `alojamiento`, `oferta`, `disponible`, `búsqueda`, `añadir`, `disfrutar`, `baño`, `comparar`, `proporcionar`, `electrónico`, `restaurante`, `visitar`, `san`, `correo`, `tratamiento`, `dispositivo`, `reservar`

wordfreq only: `ahí`, `argentino`, `d`, `listo`, `mierda`, `i`, `c`, `policía`, `juan`, `video`, `peor`, `voz`, `hola`, `militar`, `matar`, `cara`, `canción`, `capital`, `suerte`, `vuelta`, `resto`, `miedo`, `vos`, `ciudadano`, `josé`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 556 | `low` | 462 | wordfreq zipf en 5.3 vs es 3.6 |
| 563 | `cost` | 458 | wordfreq zipf en 5.2 vs es 3.3 |
| 609 | `cookies` | 425 | wordfreq zipf en 4.1 vs es 3.0 |
| 827 | `the` | 322 | wordfreq zipf en 7.7 vs es 5.4 |
| 1239 | `of` | 207 | wordfreq zipf en 7.4 vs es 5.1 |
| 1327 | `city` | 190 | wordfreq zipf en 5.6 vs es 4.3 |
| 1486 | `led` | 167 | wordfreq zipf en 5.1 vs es 3.7 |
| 1503 | `i` | 165 | wordfreq zipf en 7.1 vs es 5.4 |
| 1565 | `in` | 156 | wordfreq zipf en 7.3 vs es 5.1 |
| 1693 | `beach` | 140 | wordfreq zipf en 4.9 vs es 3.8 |
| 1792 | `new` | 130 | wordfreq zipf en 6.2 vs es 4.7 |
| 1887 | `show` | 122 | wordfreq zipf en 5.7 vs es 4.6 |
| 1912 | `and` | 120 | wordfreq zipf en 7.4 vs es 5.0 |
| 2031 | `home` | 113 | wordfreq zipf en 5.8 vs es 4.0 |
| 2172 | `resort` | 104 | wordfreq zipf en 4.4 vs es 3.3 |
| 2275 | `to` | 97 | wordfreq zipf en 7.4 vs es 4.9 |
| 2511 | `top` | 84 | wordfreq zipf en 5.6 vs es 4.4 |
| 2605 | `by` | 79 | wordfreq zipf en 6.7 vs es 4.5 |
| 2616 | `love` | 79 | wordfreq zipf en 5.8 vs es 4.3 |
| 2638 | `house` | 78 | wordfreq zipf en 5.7 vs es 4.2 |
| 2644 | `parking` | 78 | wordfreq zipf en 4.5 vs es 3.1 |
| 2649 | `set` | 78 | wordfreq zipf en 5.6 vs es 4.1 |
| 2685 | `bill` | 76 | wordfreq zipf en 5.2 vs es 4.1 |
| 2697 | `lake` | 76 | wordfreq zipf en 4.8 vs es 3.5 |
| 2813 | `island` | 71 | wordfreq zipf en 5.0 vs es 3.8 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 99 | `estado` | 1,789 | PROPN 54%, capitalised forms 66% |
| 155 | `dios` | 1,327 | PROPN 3%, capitalised forms 92% |
| 196 | `unido` | 1,090 | PROPN 94%, capitalised forms 94% |
| 315 | `san` | 759 | PROPN 100%, capitalised forms 100% |
| 436 | `españa` | 567 | PROPN 100%, capitalised forms 100% |
| 457 | `jetcost` | 551 | PROPN 100%, capitalised forms 100% |
| 459 | `consejo` | 550 | PROPN 50%, capitalised forms 48% |
| 517 | `santo` | 496 | PROPN 65%, capitalised forms 75% |
| 534 | `europeo` | 482 | PROPN 65%, capitalised forms 52% |
| 547 | `universidad` | 469 | PROPN 52%, capitalised forms 54% |
| 566 | `china` | 456 | PROPN 100%, capitalised forms 100% |
| 582 | `méxico` | 447 | PROPN 100%, capitalised forms 100% |
| 613 | `tripadvisor` | 420 | PROPN 96%, capitalised forms 100% |
| 631 | `jesús` | 407 | PROPN 97%, capitalised forms 100% |
| 643 | `puerto` | 400 | PROPN 57%, capitalised forms 51% |
| 696 | `york` | 372 | PROPN 100%, capitalised forms 100% |
| 713 | `europa` | 363 | PROPN 98%, capitalised forms 100% |
| 790 | `costa` | 333 | PROPN 58%, capitalised forms 62% |
| 792 | `google` | 333 | PROPN 100%, capitalised forms 99% |
| 805 | `tv` | 329 | PROPN 11%, capitalised forms 96% |
| 811 | `japón` | 327 | PROPN 98%, capitalised forms 100% |
| 827 | `the` | 322 | PROPN 98%, capitalised forms 81% |
| 829 | `barcelona` | 321 | PROPN 100%, capitalised forms 100% |
| 846 | `madrid` | 315 | PROPN 100%, capitalised forms 100% |
| 857 | `espíritu` | 311 | PROPN 52%, capitalised forms 48% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 98.8% | 0.997 |
| juilland_u | 99.4% | 1.000 |
| juilland_u_corrected | 99.4% | 1.000 |
| dp_adjusted | 98.7% | 0.998 |
| cd_blend | 98.9% | 0.999 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `únete` | 5019 | 4836 | -183 | 29 | 29 | 0.800 | 0.756 |
| `viviente` | 5126 | 4945 | -181 | 28 | 28 | 0.800 | 0.768 |
| `triunfo` | 5122 | 4944 | -178 | 28 | 28 | 0.820 | 0.739 |
| `triunfar` | 5011 | 4835 | -176 | 29 | 29 | 0.792 | 0.765 |
| `tornar` | 5008 | 4834 | -174 | 29 | 29 | 0.823 | 0.726 |
| `pseudo` | 4883 | 6921 | +2,038 | 30 | 15 | 0.738 | 0.871 |
| `pseudónimo` | 4781 | 6671 | +1,890 | 31 | 16 | 0.746 | 0.863 |
| `love` | 2616 | 4294 | +1,678 | 79 | 34 | 0.786 | 0.753 |
| `ascendente` | 3336 | 4946 | +1,610 | 54 | 27 | 0.776 | 0.737 |
| `remate` | 3736 | 5303 | +1,567 | 46 | 24 | 0.773 | 0.780 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `simulación` | 5112 | 4941 | -171 | 28 | 28 | 0.834 | 0.719 |
| `trasplante` | 5010 | 4846 | -164 | 29 | 28 | 0.836 | 0.714 |
| `monto` | 5088 | 4932 | -156 | 28 | 28 | 0.835 | 0.730 |
| `silencioso` | 5002 | 4853 | -149 | 29 | 29 | 0.833 | 0.715 |
| `thomas` | 5120 | 4972 | -148 | 28 | 27 | 0.825 | 0.721 |
| `parquet` | 4524 | 5282 | +758 | 34 | 24 | 0.608 | 0.780 |
| `fráncfort` | 4845 | 5197 | +352 | 30 | 23 | 0.708 | 0.800 |
| `dima` | 2982 | 3294 | +312 | 65 | 38 | 0.731 | 0.690 |
| `llama` | 4683 | 4984 | +301 | 32 | 25 | 0.718 | 0.766 |
| `fantasma` | 3718 | 4015 | +297 | 46 | 33 | 0.732 | 0.730 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `zorro` | 5018 | 4905 | -113 | 29 | 28 | 0.816 | 0.751 |
| `vicepresidente` | 5015 | 4904 | -111 | 29 | 27 | 0.815 | 0.738 |
| `trasplante` | 5010 | 4903 | -107 | 29 | 28 | 0.836 | 0.714 |
| `tornar` | 5008 | 4902 | -106 | 29 | 29 | 0.823 | 0.726 |
| `sumergir` | 5006 | 4900 | -106 | 29 | 29 | 0.821 | 0.742 |
| `parquet` | 4524 | 5388 | +864 | 34 | 24 | 0.608 | 0.780 |
| `fráncfort` | 4845 | 5247 | +402 | 30 | 23 | 0.708 | 0.800 |
| `llama` | 4683 | 5022 | +339 | 32 | 25 | 0.718 | 0.766 |
| `dima` | 2982 | 3311 | +329 | 65 | 38 | 0.731 | 0.690 |
| `fantasma` | 3718 | 4038 | +320 | 46 | 33 | 0.732 | 0.730 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `recargar` | 5213 | 4846 | -367 | 27 | 27 | 0.830 | 0.719 |
| `volcán` | 5237 | 4874 | -363 | 27 | 27 | 0.819 | 0.725 |
| `rosario` | 5351 | 4994 | -357 | 26 | 26 | 0.827 | 0.737 |
| `mark` | 5331 | 4983 | -348 | 26 | 26 | 0.826 | 0.735 |
| `hotelquickly` | 5312 | 4973 | -339 | 26 | 26 | 0.819 | 0.734 |
| `pseudo` | 4883 | 5999 | +1,116 | 30 | 15 | 0.738 | 0.871 |
| `pseudónimo` | 4781 | 5850 | +1,069 | 31 | 16 | 0.746 | 0.863 |
| `love` | 2616 | 3494 | +878 | 79 | 34 | 0.786 | 0.753 |
| `remate` | 3736 | 4405 | +669 | 46 | 24 | 0.773 | 0.780 |
| `model` | 4589 | 5199 | +610 | 33 | 20 | 0.767 | 0.817 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `únete` | 5019 | 4863 | -156 | 29 | 29 | 0.800 | 0.756 |
| `triunfar` | 5011 | 4862 | -149 | 29 | 29 | 0.792 | 0.765 |
| `tornar` | 5008 | 4861 | -147 | 29 | 29 | 0.823 | 0.726 |
| `sumergir` | 5006 | 4859 | -147 | 29 | 29 | 0.821 | 0.742 |
| `suscríbase` | 5007 | 4860 | -147 | 29 | 29 | 0.814 | 0.734 |
| `pseudo` | 4883 | 5905 | +1,022 | 30 | 15 | 0.738 | 0.871 |
| `pseudónimo` | 4781 | 5753 | +972 | 31 | 16 | 0.746 | 0.863 |
| `love` | 2616 | 3369 | +753 | 79 | 34 | 0.786 | 0.753 |
| `remate` | 3736 | 4484 | +748 | 46 | 24 | 0.773 | 0.780 |
| `ascendente` | 3336 | 4082 | +746 | 54 | 27 | 0.776 | 0.737 |

