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

Decision: **continue**.

