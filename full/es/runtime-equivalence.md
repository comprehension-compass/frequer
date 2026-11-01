# Runtime equivalence: Honeyeater 44220fb vs c07c7015 (batched), es 1.5.0

The first 40 es shards (105,726,244 tokens) were counted through Honeyeater `44220fb` with frequer
`e3d5461`. The extension counts through the batched sentence stage, Honeyeater `c07c7015` with frequer
`full-es` after the uplift merge, about 2-3x faster per worker. frequer's merge refuses shards from
different runtimes, so the old shards could be re-stamped only once their counts were shown to be identical.

**Proof (2026-11-01).** The same sample was counted with both pairs, with the same wheel
(`honeyeater_lemma_es-1.5.0`, sha256 `89ddf9f6…`) and the same manifest settings: Tatoeba spa, first 3.0M raw
characters (564,229 tokens), and ParaCrawl at stride 28, first 3.0M kept characters (442,161 tokens).

| | old (44220fb) | new (c07c7015) |
| --- | ---: | ---: |
| Tatoeba shard, seconds | 349 | 111 |
| ParaCrawl shard, seconds | 153 | 84 |

Count files compared key by key: `lemmas` (every lemma's frequency, documents, forms, POS votes, parts,
kinds), `units`, `tokens`, `docs`, `lines`, `part_tokens`, `hygiene_dropped` and `config_hash` are
identical. The folded co-occurrence file body is byte-identical. Only `runtime.honeyeater_commit` and
the timing and peak-memory statistics differ.

**Re-stamp.** Each of the 40 counts files had `runtime.honeyeater_commit` set to
`c07c701585902f15fee2ef96a45893b1a5476940` and nothing else changed, apart from a top-level
`restamped_from` note. A rebuild from the re-stamped counts with the new runtime reproduces
`snapshots/es.json` entry for entry; only the provenance keys `source`, `honeyeater` and `frequer` differ.
