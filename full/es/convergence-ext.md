## Convergence

One row per counted shard: the shards counted so far, in the order they finished. Per band N: **chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement (1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each source; a source with an odd count leaves its newest shard out). Stopping rule: 3 consecutive full-mix checkpoints with split <= 5% at 20k and <= 10% at 50k.

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105,726,244 | paracrawl-en-es 102,399,277, tatoeba-spa 3,326,967 | full | - | - | 1,318 | 1.4% | - | - | 334 | 2.5% | - | - | 66 | 5.2% | - | - | 7 | 19.0% | 0/3 |
| 111,579,906 | paracrawl-en-es 108,252,939, tatoeba-spa 3,326,967 | full | 0.2% | 4 | 1,388 | 1.2% | 0.3% | 10 | 353 | 2.4% | 0.6% | 31 | 70 | 5.1% | 2.1% | 203 | 7 | 18.6% | 0/3 |
| 117,425,197 | paracrawl-en-es 114,098,230, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 1,464 | 1.2% | 0.2% | 10 | 371 | 2.4% | 0.5% | 30 | 73 | 5.0% | 2.0% | 193 | 7 | 18.1% | 0/3 |
| 225,662,453 | paracrawl-en-es 222,335,486, tatoeba-spa 3,326,967 | full | 0.6% | 16 | 2,792 | 1.0% | 0.9% | 35 | 712 | 1.6% | 1.9% | 97 | 141 | 3.9% | 6.7% | 493 | 14 | 13.5% | 0/3 |
| 266,630,143 | paracrawl-en-es 263,303,176, tatoeba-spa 3,326,967 | full | 0.3% | 5 | 3,309 | 0.9% | 0.3% | 12 | 842 | 1.6% | 0.8% | 37 | 167 | 3.5% | 2.7% | 209 | 16 | 12.5% | 0/3 |
| 301,747,992 | paracrawl-en-es 298,421,025, tatoeba-spa 3,326,967 | full | 0.1% | 4 | 3,746 | 0.8% | 0.3% | 9 | 952 | 1.5% | 0.6% | 30 | 189 | 3.4% | 2.1% | 170 | 18 | 12.1% | 0/3 |
| 1,068,227,088 | paracrawl-en-es 1,064,900,121, tatoeba-spa 3,326,967 | full | 0.4% | 11 | 13,246 | 0.4% | 0.6% | 26 | 3,363 | 0.7% | 1.6% | 71 | 666 | 1.9% | 5.7% | 378 | 64 | 7.0% | 1/3 |
| 1,194,027,333 | paracrawl-en-es 1,190,700,366, tatoeba-spa 3,326,967 | full | 0.1% | 2 | 14,799 | 0.4% | 0.1% | 5 | 3,761 | 0.8% | 0.3% | 14 | 744 | 1.9% | 1.1% | 82 | 72 | 6.7% | 2/3 |

Decision: **continue**.

