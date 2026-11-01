## Convergence

One row per counted shard: the shards counted so far, in the order they finished. Per band N: **chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement (1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each source; a source with an odd count leaves its newest shard out). Stopping rule: 3 consecutive full-mix checkpoints with split <= 5% at 20k and <= 10% at 50k.

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,858,929 | hplt-v2-de 1,858,929 | web only | - | - | 28 | - | - | - | 12 | - | - | - | 5 | - | - | - | 2 | - | 0/3 |
| 3,228,275 | hplt-v2-de 3,228,275 | web only | 6.4% | 112 | 49 | 15.4% | 10.2% | 297 | 20 | 23.5% | 14.6% | 885 | 8 | 33.5% | 21.3% | 3,391 | 3 | 50.2% | 0/3 |
| 5,035,140 | hplt-v2-de 5,035,140 | web only | 6.2% | 128 | 75 | 15.4% | 8.4% | 302 | 30 | 23.5% | 12.2% | 782 | 12 | 33.5% | 17.6% | 3,269 | 4 | 50.2% | 0/3 |
| 7,843,966 | hplt-v2-de 5,035,140, tatoeba-deu 2,808,826 | partial (lacks tatoeba-deu) | 11.1% | 398 | 103 | 15.4% | 10.2% | 687 | 40 | 23.5% | 10.1% | 1,278 | 15 | 33.5% | 9.5% | 3,267 | 5 | 50.2% | 0/3 |
| 11,145,054 | hplt-v2-de 5,035,140, tatoeba-deu 6,109,914 | full | 7.2% | 272 | 138 | 11.4% | 7.2% | 503 | 51 | 16.0% | 7.5% | 982 | 19 | 23.9% | 8.5% | 2,506 | 5 | 38.4% | 0/3 |
| 12,858,618 | hplt-v2-de 6,748,704, tatoeba-deu 6,109,914 | full | 3.0% | 104 | 165 | 10.2% | 3.5% | 203 | 61 | 13.8% | 5.1% | 433 | 23 | 20.8% | 8.0% | 1,692 | 7 | 34.0% | 0/3 |
| 14,661,404 | hplt-v2-de 8,551,490, tatoeba-deu 6,109,914 | full | 2.6% | 80 | 192 | 10.2% | 3.5% | 164 | 71 | 13.8% | 4.5% | 373 | 27 | 20.8% | 7.1% | 1,457 | 8 | 34.0% | 0/3 |
| 16,598,866 | hplt-v2-de 10,488,952, tatoeba-deu 6,109,914 | full | 2.4% | 69 | 223 | 9.0% | 3.0% | 152 | 83 | 13.2% | 4.1% | 349 | 32 | 19.3% | 6.5% | 1,294 | 9 | 30.8% | 0/3 |
| 18,137,485 | hplt-v2-de 12,027,571, tatoeba-deu 6,109,914 | full | 1.4% | 57 | 246 | 9.0% | 2.1% | 110 | 92 | 13.2% | 3.1% | 257 | 35 | 19.3% | 4.5% | 972 | 10 | 30.8% | 0/3 |

Decision: **continue**.

