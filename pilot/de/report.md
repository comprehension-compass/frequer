# Review report: de (pilot)

- Ranking score: `frequency`; 129,167 candidate lemmas ranked.
- Tokens counted: 1,635,486 in 5,189 documents, 9 shards, 100 dispersion parts.
- Lemma release: `honeyeater_lemma_de` 0.0.1 (sha256 `1056c1b5bdc4adf5`); honeyeater `f4495a68bf53`; overrides sha256 `5e82271e87a53e65`.

## Corpus and hygiene

| source | shards | documents | lines kept | tokens | dropped by hygiene |
|---|---|---|---|---|---|
| hplt-v2-de | 8 | 4,473 | 59,414 | 1,386,834 | alpha 1,031, exact_dup 1,591, gap 1,062, langid 3,215, length 12,150, near_dup 658 |
| tatoeba-deu | 1 | 716 | 35,705 | 248,652 | alpha 1, gap 8, length 14, near_dup 72 |

## How the runtime decided the lemmas

Tokens by deciding layer: backend 24.0%, model 5.3%, table 70.7%.
Tokens the lemma step resolved to their host's lemma: 0. Sentences where an independent replay of the step disagreed with it: 0 of 161,257.

### Override file against the lemma step

The backend's lemma has the override file applied before the lemma step, but the step prefers its list for a form it knows. Of 243,317 tokens whose surface the override file names, the step emitted a different lemma for 2,994 (top 25 below, as counted in the 38 kept per shard).

| surface | override says | step emitted | tokens |
|---|---|---|---|
| `möchte` | `mögen` | `möchten` | 616 |
| `möchten` | `mögen` | `möchten` | 456 |
| `deutsche` | `Deutsche` | `deutsch` | 284 |
| `de` | `De` | `de` | 161 |
| `erster` | `erster` | `erste` | 158 |
| `lange` | `lange` | `lang` | 147 |
| `stand` | `stehen` | `Stand` | 142 |
| `anderer` | `anderer` | `ander` | 140 |
| `arbeiten` | `arbeiten` | `Arbeit` | 132 |
| `spielen` | `spielen` | `Spiel` | 121 |
| `sprachen` | `sprechen` | `Sprache` | 75 |
| `letzter` | `letzter` | `letzte` | 72 |
| `teil` | `Teil` | `teil` | 65 |
| `alter` | `Alter` | `alt` | 59 |
| `arbeiten` | `arbeiten` | `Arbeiten` | 44 |
| `lange` | `lange` | `Lange` | 39 |
| `gefahren` | `fahren` | `Gefahr` | 36 |
| `würde` | `werden` | `Würde` | 32 |
| `bin` | `sein` | `Bin` | 28 |
| `können` | `können` | `Können` | 22 |
| `glauben` | `glauben` | `Glaube` | 21 |
| `waren` | `sein` | `Ware` | 21 |
| `oder` | `oder` | `Oder` | 20 |
| `zweiter` | `zweiter` | `zweite` | 19 |
| `nächster` | `nächster` | `nächst` | 14 |

## Rank shifts against the live snapshot (`reference/lemmas/de.json`)

Live list 20,000 lemmas, this build 129,167; 19,013 shared. Spearman rank correlation on the shared lemmas 0.823; median rank ratio 1.31x.
Overlap of this build's top-k with the live top-k: top 1,000 87.6%, top 5,000 84.7%, top 20,000 72.9%.

### Biggest risers (rank improves)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `Alternativ` | 18734 | 2010 | -16,724 |
| `Bronchitis` | 19484 | 3704 | -15,780 |
| `Bestenlist` | 18713 | 3065 | -15,648 |
| `Daumen` | 19501 | 4572 | -14,929 |
| `Daten` | 18710 | 3883 | -14,827 |
| `Anhalt` | 19450 | 4690 | -14,760 |
| `Allen` | 18441 | 4064 | -14,377 |
| `Ihr` | 14082 | 42 | -14,040 |
| `Osaka` | 17079 | 3091 | -13,988 |
| `sogenannt` | 14915 | 928 | -13,987 |
| `Münchner` | 16894 | 3199 | -13,695 |
| `FOREVER` | 16993 | 3321 | -13,672 |
| `Mähroboter` | 16768 | 3142 | -13,626 |
| `Gong` | 18478 | 4882 | -13,596 |
| `verheiratet` | 15713 | 2141 | -13,572 |

### Biggest fallers (rank worsens)

| lemma | live rank | new rank | change |
|---|---|---|---|
| `weißen` | 1921 | 127628 | +125,707 |
| `wiener` | 2617 | 127789 | +125,172 |
| `ihnen` | 90 | 119746 | +119,656 |
| `kind` | 3802 | 120313 | +116,511 |
| `komm` | 4332 | 120508 | +116,176 |
| `höchst` | 4299 | 119696 | +115,397 |
| `gute` | 4050 | 118798 | +114,748 |
| `fünfter` | 3821 | 117944 | +114,123 |
| `en` | 2677 | 116723 | +114,046 |
| `berliner` | 1402 | 114800 | +113,398 |
| `am` | 318 | 113305 | +112,987 |
| `deinen` | 3718 | 115747 | +112,029 |
| `Wetten` | 4404 | 110249 | +105,845 |
| `This` | 3511 | 104012 | +100,501 |
| `Sami` | 3584 | 95974 | +92,390 |

### Newly in the top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `Sie` | - | 19 | - |
| `Ihr` | 14082 | 42 | -14,040 |
| `ander` | - | 66 | - |
| `erste` | - | 87 | - |
| `möchten` | 7136 | 102 | -7,034 |
| `letzte` | - | 142 | - |
| `nächst` | 8731 | 188 | -8,543 |
| `zweite` | - | 300 | - |
| `später` | - | 326 | - |
| `besonder` | 13451 | 412 | -13,039 |
| `Doktor` | 6875 | 423 | -6,452 |
| `früher` | 6068 | 510 | -5,558 |
| `bisschen` | 9541 | 745 | -8,796 |
| `dritte` | - | 774 | - |
| `de` | - | 874 | - |

### Dropped out of the live top 5,000

| lemma | live rank | new rank | change |
|---|---|---|---|
| `aller` | 53 | 7357 | +7,304 |
| `anderer` | 56 | 11807 | +11,751 |
| `alle` | 63 | 9007 | +8,944 |
| `mir` | 74 | - | - |
| `erster` | 86 | 29783 | +29,697 |
| `ihnen` | 90 | 119746 | +119,656 |
| `mich` | 104 | - | - |
| `dir` | 109 | - | - |
| `ihn` | 142 | - | - |
| `einiger` | 151 | 18156 | +18,005 |
| `euch` | 161 | - | - |
| `ihm` | 173 | - | - |
| `zweiter` | 277 | 12142 | +11,865 |
| `daß` | 286 | 29626 | +29,340 |
| `am` | 318 | 113305 | +112,987 |

## Ported frequer checks

### Form-ratio outliers (1)

A surface form far more frequent than the lemma's median form.

| rank | lemma | freq | detail |
|---|---|---|---|
| 40 | `wenn` | 4,422 | median form 3; `wenn` 4,418 (1473x) |

### Singular/plural mismatch (1,867)

Lemma looks like a plural whose stripped form maps to another listed lemma.

| rank | lemma | freq | detail |
|---|---|---|---|
| 4 | `ein` | 39,731 | `ei` lemmatises to `ei` (rank 18,149) |
| 11 | `haben` | 16,682 | `hab` lemmatises to `hab` (rank 1,706) |
| 18 | `können` | 11,502 | `könn` lemmatises to `Könn` (rank 80,041) |
| 19 | `Sie` | 11,020 | `Si` lemmatises to `Si` (rank 21,303) |
| 27 | `oder` | 7,352 | `od` lemmatises to `od` (rank 47,521) |
| 28 | `als` | 6,998 | `al` lemmatises to `al` (rank 15,280) |
| 29 | `wie` | 6,674 | `wi` lemmatises to `wi` (rank 127,711) |
| 31 | `aus` | 6,237 | `au` lemmatises to `Au` (rank 9,252) |
| 32 | `dass` | 5,880 | `das` lemmatises to `der` (rank 1) |
| 37 | `unser` | 4,735 | `uns` lemmatises to `wir` (rank 21) |
| 39 | `mein` | 4,423 | `mei` lemmatises to `mei` (rank 121,591) |
| 40 | `wenn` | 4,422 | `wen` lemmatises to `wer` (rank 116) |
| 45 | `man` | 3,740 | `ma` lemmatises to `Ma` (rank 14,540) |
| 47 | `aber` | 3,579 | `ab` lemmatises to `ab` (rank 88) |
| 48 | `was` | 3,536 | `wa` lemmatises to `Wa` (rank 108,889) |
| 60 | `bis` | 2,954 | `bi` lemmatises to `Bi` (rank 13,894) |
| 61 | `kommen` | 2,948 | `komm` lemmatises to `komm` (rank 120,508) |
| 63 | `hier` | 2,721 | `hi` lemmatises to `hi` (rank 22,497) |
| 66 | `ander` | 2,586 | `and` lemmatises to `and` (rank 1,876) |
| 67 | `finden` | 2,431 | `find` lemmatises to `Find` (rank 34,867) |
| 69 | `immer` | 2,258 | `imm` lemmatises to `Imm` (rank 36,777) |
| 70 | `weiter` | 2,223 | `weit` lemmatises to `weit` (rank 338) |
| 71 | `dann` | 2,220 | `dan` lemmatises to `Dan` (rank 9,321) |
| 73 | `unter` | 2,078 | `unt` lemmatises to `Unt` (rank 106,134) |
| 74 | `sehen` | 2,035 | `seh` lemmatises to `seh` (rank 9,933) |

_1,842 more not shown._

### Lemma consistency (664)

Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).

| rank | lemma | freq | detail |
|---|---|---|---|
| 19 | `Sie` | 11,020 | alone, `Sie` lemmatises to `sie` (rank 20) |
| 30 | `ihr` | 6,528 | alone, `ihr` lemmatises to `sie` (rank 20) |
| 42 | `Ihr` | 4,057 | alone, `Ihr` lemmatises to `ihr` (rank 30) |
| 66 | `ander` | 2,586 | alone, `ander` lemmatises to `and` (rank 1,876) |
| 131 | `Frage` | 970 | alone, `Frage` lemmatises to `fragen` (rank 281) |
| 202 | `einer` | 680 | alone, `einer` lemmatises to `ein` (rank 4) |
| 333 | `Stelle` | 402 | alone, `Stelle` lemmatises to `stellen` (rank 117) |
| 357 | `euer` | 375 | alone, `euer` lemmatises to `eu` (rank 2,350) |
| 362 | `digital` | 373 | alone, `digital` lemmatises to `Digital` (rank 2,952) |
| 401 | `bestimmt` | 341 | alone, `bestimmt` lemmatises to `bestimmen` (rank 673) |
| 458 | `gesamt` | 299 | alone, `gesamt` lemmatises to `samen` (rank 47,855) |
| 459 | `App` | 297 | alone, `App` lemmatises to `app` (rank 6,607) |
| 509 | `personenbezogen` | 274 | alone, `personenbezogen` lemmatises to `Personenbezogen` (rank 90,231) |
| 620 | `Mm` | 236 | alone, `Mm` lemmatises to `mm` (rank 6,360) |
| 624 | `beliebt` | 235 | alone, `beliebt` lemmatises to `belieben` (rank 7,855) |
| 675 | `vergangen` | 220 | alone, `vergangen` lemmatises to `vergehen` (rank 2,669) |
| 716 | `Kauf` | 207 | alone, `Kauf` lemmatises to `kaufen` (rank 170) |
| 764 | `Suche` | 195 | alone, `Suche` lemmatises to `suchen` (rank 190) |
| 768 | `Morgen` | 194 | alone, `Morgen` lemmatises to `morgen` (rank 425) |
| 828 | `dich` | 180 | alone, `dich` lemmatises to `du` (rank 26) |
| 852 | `Essen` | 175 | alone, `Essen` lemmatises to `essen` (rank 272) |
| 871 | `weiß` | 171 | alone, `weiß` lemmatises to `wissen` (rank 101) |
| 894 | `meinen` | 166 | alone, `meinen` lemmatises to `mein` (rank 39) |
| 944 | `Training` | 158 | alone, `Training` lemmatises to `training` (rank 10,908) |
| 1032 | `Online` | 145 | alone, `Online` lemmatises to `online` (rank 387) |

_639 more not shown._

### Short lemmas (186)

Check these are real words.

| rank | lemma | freq | detail |
|---|---|---|---|
| 5 | `in` | 37,601 | `im` -> `in`, `in` -> `in`, `ins` -> `in`, `in-` -> `in` |
| 6 | `zu` | 26,890 | `zu` -> `zu`, `zur` -> `zu`, `zum` -> `zu`, `zu-` -> `zu` |
| 14 | `es` | 12,784 | `es` -> `es`, `’s` -> `es`, `s` -> `s`, `'s` -> `es` |
| 16 | `an` | 12,346 | `an` -> `an`, `am` -> `an`, `ans` -> `an`, `an-` -> `an`, `a` -> `an` |
| 23 | `er` | 9,488 | `er` -> `er`, `ihn` -> `er`, `ihm` -> `er`, `er-` -> `er` |
| 26 | `du` | 8,469 | `du` -> `du`, `dir` -> `du`, `dich` -> `du` |
| 33 | `um` | 5,777 | `um` -> `um`, `ums` -> `um`, `um-` -> `um` |
| 38 | `so` | 4,428 | `so` -> `so` |
| 76 | `da` | 2,007 | `da` -> `da`, `das` -> `der` |
| 88 | `ab` | 1,575 | `ab` -> `ab`, `ab-` -> `ab` |
| 113 | `ob` | 1,081 | `ob` -> `ob`, `obere` -> `ob` |
| 132 | `wo` | 961 | `wo` -> `wo` |
| 175 | `ja` | 764 | `ja` -> `ja`, `ja-` -> `ja` |
| 249 | `je` | 555 | `je` -> `je` |
| 450 | `B` | 303 | `b` -> `?`, `b.` -> `?` |
| 475 | `of` | 289 | `of` -> `of` |
| 620 | `Mm` | 236 | `mm` -> `Mm` |
| 623 | `x` | 236 | `x` -> `x` |
| 857 | `C` | 174 | `c` -> `C` |
| 874 | `de` | 170 | `de` -> `de`, `d’` -> `de` |
| 995 | `A` | 150 | `a` -> `an` |
| 1191 | `Öl` | 128 | `öle` -> `Öle`, `öl` -> `öl`, `ölen` -> `ölen`, `öls` -> `Öls` |
| 1258 | `g` | 120 | `g` -> `G`, `ges` -> `ges` |
| 1328 | `i` | 113 | `i` -> `i` |
| 1342 | `AG` | 111 | `ag` -> `AG` |

_161 more not shown._

### Case merges (1,649)

Non-lowercase lemmas, with the lowercase twin where one is listed.

| rank | lemma | freq | detail |
|---|---|---|---|
| 19 | `Sie` | 11,020 | lowercase `sie` is rank 20 (11,010): merge candidate |
| 42 | `Ihr` | 4,057 | lowercase `ihr` is rank 30 (6,528): merge candidate |
| 50 | `Jahr` | 3,477 | lowercase `jahr` is rank 46,966 (2): merge candidate |
| 79 | `Zeit` | 1,830 | lowercase `zeit` is rank 7,972 (13): merge candidate |
| 84 | `Kind` | 1,646 | lowercase `kind` is rank 120,313 (1): merge candidate |
| 107 | `Haus` | 1,169 | lowercase `haus` is rank 11,924 (8): merge candidate |
| 115 | `Uhr` | 1,069 | lowercase `uhr` is rank 125,772 (1): merge candidate |
| 126 | `Leben` | 998 | lowercase `leben` is rank 222 (628): merge candidate |
| 131 | `Frage` | 970 | lowercase `frage` is rank 117,743 (1): merge candidate |
| 136 | `Unternehmen` | 935 | lowercase `unternehmen` is rank 4,310 (28): merge candidate |
| 139 | `Buch` | 928 | lowercase `buch` is rank 22,248 (4): merge candidate |
| 144 | `Seite` | 899 | lowercase `seite` is rank 124,413 (1): merge candidate |
| 157 | `Arbeit` | 827 | lowercase `arbeit` is rank 5,818 (19): merge candidate |
| 159 | `Produkt` | 810 | lowercase `produkt` is rank 10,869 (9): merge candidate |
| 163 | `Information` | 802 | lowercase `information` is rank 11,944 (8): merge candidate |
| 164 | `Teil` | 799 | lowercase `teil` is rank 2,031 (71): merge candidate |
| 166 | `Geld` | 791 | lowercase `geld` is rank 8,425 (12): merge candidate |
| 174 | `Land` | 764 | lowercase `land` is rank 9,107 (11): merge candidate |
| 177 | `Welt` | 754 | lowercase `welt` is rank 127,638 (1): merge candidate |
| 181 | `Person` | 743 | lowercase `person` is rank 122,879 (1): merge candidate |
| 195 | `Stadt` | 703 | lowercase `stadt` is rank 9,160 (11): merge candidate |
| 197 | `Spiel` | 693 | lowercase `spiel` is rank 12,053 (8): merge candidate |
| 204 | `Bild` | 676 | lowercase `bild` is rank 10,721 (9): merge candidate |
| 211 | `Weg` | 650 | lowercase `weg` is rank 870 (171): merge candidate |
| 215 | `Preis` | 644 | lowercase `preis` is rank 13,559 (7): merge candidate |

_1,624 more not shown._

### wordfreq comparison

Top 1000 lemmas shared with wordfreq's (its forms lemmatised through the runtime): 730 (73.0%).

Ours only: `Sie`, `Ihr`, `Frage`, `Datum`, `Teil`, `Welt`, `Weg`, `Bereich`, `Ende`, `beziehungsweise`, `Mal`, `außerdem`, `kostenlos`, `circa`, `Website`, `geeignet`, `heißen`, `Vorteil`, `Recht`, `Stelle`, `perfekt`, `Hund`, `Straße`, `Inhalt`, `Material`

wordfreq only: `hab`, `Weiss`, `s`, `enden`, `Weln`, `D`, `the`, `teil`, `grosse`, `grossen`, `i`, `stimmen`, `e`, `u`, `Heisst`, `Ne`, `Bzw`, `ne`, `ausserdem`, `halt`, `dank`, `h`, `us`, `EU`, `r`

## Foreign-word candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 34 | `all` | 5,508 | wordfreq zipf en 6.5 vs de 5.2 |
| 475 | `of` | 289 | wordfreq zipf en 7.4 vs de 5.5 |
| 879 | `her` | 168 | wordfreq zipf en 6.3 vs de 5.2 |
| 936 | `The` | 159 | wordfreq zipf en 7.7 vs de 5.6 |
| 995 | `A` | 150 | wordfreq zipf en 7.4 vs de 5.8 |
| 1025 | `See` | 146 | wordfreq zipf en 6.1 vs de 4.8 |
| 1067 | `Held` | 141 | wordfreq zipf en 5.2 vs de 4.2 |
| 1184 | `New` | 128 | wordfreq zipf en 6.2 vs de 5.1 |
| 1328 | `i` | 113 | wordfreq zipf en 7.1 vs de 5.5 |
| 1546 | `the` | 96 | wordfreq zipf en 7.7 vs de 5.6 |
| 1552 | `LED` | 95 | wordfreq zipf en 5.1 vs de 4.1 |
| 1651 | `national` | 89 | wordfreq zipf en 5.5 vs de 4.3 |
| 1679 | `Set` | 87 | wordfreq zipf en 5.6 vs de 4.3 |
| 1784 | `Business` | 82 | wordfreq zipf en 5.6 vs de 4.5 |
| 1876 | `and` | 78 | wordfreq zipf en 7.4 vs de 5.2 |
| 1893 | `Game` | 77 | wordfreq zipf en 5.7 vs de 4.4 |
| 2053 | `For` | 69 | wordfreq zipf en 7.0 vs de 4.9 |
| 2224 | `to` | 63 | wordfreq zipf en 7.4 vs de 5.2 |
| 2257 | `Finance` | 61 | wordfreq zipf en 4.7 vs de 3.4 |
| 2294 | `Office` | 60 | wordfreq zipf en 5.4 vs de 4.2 |
| 2377 | `No` | 58 | wordfreq zipf en 6.3 vs de 4.9 |
| 2451 | `Performance` | 56 | wordfreq zipf en 5.2 vs de 4.2 |
| 2459 | `WATCHES` | 56 | wordfreq zipf en 4.1 vs de 2.1 |
| 2515 | `Activity` | 54 | wordfreq zipf en 4.9 vs de 3.1 |
| 2569 | `Seat` | 53 | wordfreq zipf en 4.8 vs de 3.6 |

## Proper-noun candidates

| rank | lemma | freq | signal |
|---|---|---|---|
| 150 | `Deutschland` | 858 | PROPN 100%, capitalised forms 0% |
| 435 | `Berlin` | 314 | PROPN 100%, capitalised forms 0% |
| 475 | `of` | 289 | PROPN 92%, capitalised forms 0% |
| 501 | `Japan` | 278 | PROPN 100%, capitalised forms 0% |
| 571 | `München` | 250 | PROPN 100%, capitalised forms 0% |
| 621 | `Schweiz` | 236 | PROPN 100%, capitalised forms 0% |
| 631 | `Europa` | 232 | PROPN 100%, capitalised forms 0% |
| 698 | `Google` | 212 | PROPN 93%, capitalised forms 0% |
| 709 | `USA` | 209 | PROPN 100%, capitalised forms 0% |
| 715 | `Casino` | 207 | PROPN 94%, capitalised forms 0% |
| 753 | `Hamburg` | 199 | PROPN 100%, capitalised forms 0% |
| 781 | `Österreich` | 191 | PROPN 100%, capitalised forms 0% |
| 794 | `Cookies` | 187 | PROPN 76%, capitalised forms 0% |
| 819 | `Tom` | 182 | PROPN 94%, capitalised forms 0% |
| 857 | `C` | 174 | PROPN 86%, capitalised forms 0% |
| 874 | `de` | 170 | PROPN 92%, capitalised forms 0% |
| 916 | `Frankreich` | 162 | PROPN 99%, capitalised forms 0% |
| 936 | `The` | 159 | PROPN 99%, capitalised forms 0% |
| 1010 | `Daniel` | 148 | PROPN 97%, capitalised forms 0% |
| 1088 | `hallo` | 139 | PROPN 99%, capitalised forms 0% |
| 1103 | `Italien` | 137 | PROPN 100%, capitalised forms 0% |
| 1112 | `Zürich` | 137 | PROPN 99%, capitalised forms 0% |
| 1121 | `Köln` | 136 | PROPN 96%, capitalised forms 0% |
| 1129 | `Bad` | 135 | PROPN 70%, capitalised forms 0% |
| 1130 | `China` | 135 | PROPN 100%, capitalised forms 0% |

## Alternative ranking scores

How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; see README for the definitions. Rows are the biggest risers and fallers.

| score | top-5k overlap | Spearman |
|---|---|---|
| document_frequency | 90.6% | 0.928 |
| juilland_u | 94.9% | 0.972 |
| juilland_u_corrected | 94.5% | 0.969 |
| dp_adjusted | 94.0% | 0.965 |
| cd_blend | 94.0% | 0.965 |

### `document_frequency`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `zögern` | 6119 | 4775 | -1,344 | 18 | 18 | 0.769 | 0.838 |
| `wovon` | 6115 | 4774 | -1,341 | 18 | 18 | 0.769 | 0.834 |
| `wechselnd` | 6109 | 4773 | -1,336 | 18 | 18 | 0.737 | 0.857 |
| `unzureichend` | 6102 | 4772 | -1,330 | 18 | 18 | 0.759 | 0.827 |
| `soviel` | 6100 | 4771 | -1,329 | 18 | 18 | 0.764 | 0.831 |
| `Kofahl` | 1542 | 36748 | +35,206 | 96 | 1 | 0.000 | 0.997 |
| `Begrenzungskabel` | 2364 | 36749 | +34,385 | 58 | 1 | 0.000 | 0.993 |
| `THOMMEN` | 2457 | 36750 | +34,293 | 56 | 1 | 0.000 | 0.992 |
| `WATCHES` | 2459 | 36751 | +34,292 | 56 | 1 | 0.000 | 0.992 |
| `Activity` | 2515 | 36752 | +34,237 | 54 | 1 | 0.000 | 0.996 |

### `juilland_u`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `ereignen` | 5598 | 4878 | -720 | 20 | 20 | 0.789 | 0.798 |
| `kleiden` | 5613 | 4915 | -698 | 20 | 19 | 0.780 | 0.804 |
| `derartig` | 5592 | 4904 | -688 | 20 | 19 | 0.781 | 0.818 |
| `verstellbar` | 5646 | 4970 | -676 | 20 | 18 | 0.769 | 0.827 |
| `nachvollziehbar` | 5623 | 4948 | -675 | 20 | 18 | 0.773 | 0.822 |
| `Begrenzungskabel` | 2364 | 46239 | +43,875 | 58 | 1 | 0.000 | 0.993 |
| `THOMMEN` | 2457 | 46240 | +43,783 | 56 | 1 | 0.000 | 0.992 |
| `WATCHES` | 2459 | 46241 | +43,782 | 56 | 1 | 0.000 | 0.992 |
| `Activity` | 2515 | 46242 | +43,727 | 54 | 1 | 0.000 | 0.996 |
| `Grill-und-co` | 2641 | 46243 | +43,602 | 51 | 1 | 0.000 | 0.996 |

### `juilland_u_corrected`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `kleiden` | 5613 | 4888 | -725 | 20 | 19 | 0.780 | 0.804 |
| `nachvollziehbar` | 5623 | 4907 | -716 | 20 | 18 | 0.773 | 0.822 |
| `verstellbar` | 5646 | 4932 | -714 | 20 | 18 | 0.769 | 0.827 |
| `ereignen` | 5598 | 4887 | -711 | 20 | 20 | 0.789 | 0.798 |
| `erstellt` | 5603 | 4892 | -711 | 20 | 19 | 0.776 | 0.820 |
| `Begrenzungskabel` | 2364 | 37937 | +35,573 | 58 | 1 | 0.000 | 0.993 |
| `THOMMEN` | 2457 | 37938 | +35,481 | 56 | 1 | 0.000 | 0.992 |
| `WATCHES` | 2459 | 37939 | +35,480 | 56 | 1 | 0.000 | 0.992 |
| `Activity` | 2515 | 37940 | +35,425 | 54 | 1 | 0.000 | 0.996 |
| `Grill-und-co` | 2641 | 37941 | +35,300 | 51 | 1 | 0.000 | 0.996 |

### `dp_adjusted`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `ansagen` | 5816 | 4668 | -1,148 | 19 | 19 | 0.781 | 0.793 |
| `zweit` | 5880 | 4753 | -1,127 | 19 | 19 | 0.774 | 0.804 |
| `wischen` | 6113 | 4987 | -1,126 | 18 | 16 | 0.730 | 0.815 |
| `nix` | 6088 | 4998 | -1,090 | 18 | 18 | 0.765 | 0.816 |
| `entziehen` | 5830 | 4750 | -1,080 | 19 | 19 | 0.762 | 0.803 |
| `Backmischung` | 4855 | 28109 | +23,254 | 23 | 1 | 0.000 | 0.998 |
| `Zofe` | 4515 | 25655 | +21,140 | 26 | 1 | 0.000 | 0.998 |
| `Onlinevorgang` | 4488 | 24479 | +19,991 | 26 | 1 | -0.000 | 0.998 |
| `Wickelbody` | 4388 | 23852 | +19,464 | 27 | 1 | 0.000 | 0.998 |
| `Wellnessreise` | 4626 | 23710 | +19,084 | 25 | 1 | -0.000 | 0.997 |

### `cd_blend`

| lemma | default rank | this rank | move | freq | docs | Juilland D | DP norm |
|---|---|---|---|---|---|---|---|
| `zweit` | 5880 | 4946 | -934 | 19 | 19 | 0.774 | 0.804 |
| `verschreiben` | 5871 | 4945 | -926 | 19 | 19 | 0.764 | 0.843 |
| `verschiedenst` | 5870 | 4944 | -926 | 19 | 19 | 0.759 | 0.839 |
| `strahlen` | 5863 | 4943 | -920 | 19 | 19 | 0.780 | 0.816 |
| `schweizerisch` | 5860 | 4942 | -918 | 19 | 19 | 0.789 | 0.822 |
| `ArbZG` | 4850 | 15150 | +10,300 | 23 | 1 | 0.000 | 0.996 |
| `Backmischung` | 4855 | 15151 | +10,296 | 23 | 1 | 0.000 | 0.998 |
| `Begrenzungsdraht` | 4860 | 15152 | +10,292 | 23 | 1 | 0.000 | 0.993 |
| `Gottschalk` | 4883 | 15153 | +10,270 | 23 | 1 | 0.000 | 0.993 |
| `Meeresaquaristik` | 4901 | 15154 | +10,253 | 23 | 1 | 0.000 | 0.996 |

