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

Decision: **continue**.

