## Convergence

One row per counted shard: the shards counted so far, in the order they finished. Per band N: **chg** = share of the top N not in the previous checkpoint's top N; **shift** = median |rank shift| of the lemmas in both; **f@N** = raw frequency at rank N; **split** = split-half disagreement (1 - overlap of the top N ranked from half A against half B, shards dealt alternately within each source; a source with an odd count leaves its newest shard out). Stopping rule: 3 consecutive full-mix checkpoints with split <= 5% at 20k and <= 10% at 50k.

| tokens | per source | mix | 5k chg | 5k shift | f@5k | 5k split | 10k chg | 10k shift | f@10k | 10k split | 20k chg | 20k shift | f@20k | 20k split | 50k chg | 50k shift | f@50k | 50k split | stop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1,858,929 | hplt-v2-de 1,858,929 | web only | - | - | 28 | - | - | - | 12 | - | - | - | 5 | - | - | - | 2 | - | 0/3 |
| 3,228,275 | hplt-v2-de 3,228,275 | web only | 6.4% | 112 | 49 | 15.4% | 10.2% | 297 | 20 | 23.5% | 14.6% | 885 | 8 | 33.5% | 21.3% | 3,391 | 3 | 50.2% | 0/3 |
| 5,035,140 | hplt-v2-de 5,035,140 | web only | 6.2% | 128 | 75 | 15.4% | 8.4% | 302 | 30 | 23.5% | 12.2% | 782 | 12 | 33.5% | 17.6% | 3,269 | 4 | 50.2% | 0/3 |

Decision: **continue**.

