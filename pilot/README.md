# Pilot, 2026-10-31: lemma release 1.4.0 with units

End-to-end run of `python -m frequer pilot <lang>` for es and de on about 7-8M tokens each:
counting, units, co-occurrence, merged table, ranking, report. Everything was counted through the
production sentence stage of a pinned honeyeater checkout (`0e1c3bbbd941`, detached worktree, clean)
with the `honeyeater-lemma-{es,de}` **1.4.0** wheels carrying the unit component:

| wheel | sha256 |
| --- | --- |
| `honeyeater_lemma_es-1.4.0-py3-none-any.whl` | `e0dc846f1c89040792f0e68326f7e430695da5d768403dc8545f4eaf97f5f6cb` |
| `honeyeater_lemma_de-1.4.0-py3-none-any.whl` | `0d68396e0babfa3d0ac30ef8c390bf7a7d7933324cf005787781b57bbf679790` |
| `honeyeater_lemma_ja-1.4.0-py3-none-any.whl` | `b634e14ea7c5eaf496a4e70b183e155b4488a457a05e305d49e024eac97bcc88` (throughput smoke only) |

Committed: `es/report.md`, `de/report.md` and their `perf.json`. The snapshots, sidecars,
co-occurrence tables and queues stay out of the repository (pilot-sized, and the web text behind
them is not ours to commit). The 2026-10-24 pilot (0.0.1 test wheels, no units) is in git history.

Machine: 4 cores shared with other jobs; 2 counting workers, plus the main process (stream,
hygiene, language ID: about 2 % of a core's worth of work per worker).

## Slice

| | es | de |
| --- | --- | --- |
| web | first 46M chars of ParaCrawl en-es (es side) | first 22M chars of each of HPLT v2 `deu_Latn` 10-13 |
| Tatoeba | first 3.5M chars | first 3.5M chars |
| tokens counted | 7,388,304 | 8,083,748 |
| documents / sentences | 10,252 / 435,871 | 25,910 / 750,866 |
| shards (4M raw chars) | 13 | 25 |
| count wall clock, 2 workers | 29.6 min | 78.6 min |

## Throughput, one core

Counted tokens per core-second of each stage, summed over every shard (so stages add as
1/total = sum of 1/stage).

| stage | es | de | ja (smoke, 0.5M tokens) |
| --- | ---: | ---: | ---: |
| fetch + decompress + parse (main) | 1,568k | 549k | 210k |
| hygiene (main) | 486k | 408k | 1,142k |
| py3langid (main) | 152k | 158k | 247k |
| backend `segment` | 60.7k | **1.9k** | 1,382k |
| sentence stage minus release (tokenize, candidates, numbers, unit merge) | 16.8k | 15.8k | 8.5k |
| release lemma + UPOS (model on every sentence) | **6.1k** | 4.2k | **5.6k** |
| release units (list candidates, spancat, parts list, splitter) | **6.7k** | 6.0k | 6.7k |
| tally | 145k | 121k | 132k |
| co-occurrence items + sorted write | 67k | 54k | 78k |
| **worker total** | **2.37k** | **0.96k** | **2.09k** |

* es and ja are bound by the release: the lemma model now runs on **every** sentence (the
  pipeline's `lemmatise_tagged`: the sentence stage needs every token's UPOS for the units), and
  the unit step costs as much again (the spancat scores every list candidate). The 2026-10-24
  pilot ran the model only on sentences the list could not settle (es 6.1k, ja 4.2k tokens/s).
  Tatoeba's short sentences run at about 1.5k tokens/s (per-sentence overhead).
* **German is still bound by the full `de_core_news_sm` parse in `segment`: 51 % of worker time.**
  The plan's "German drops the full parse" (2026-10-24) is not in this checkout:
  `GermanSpacyBackend.segment` still `nlp.pipe`s every sentence through the whole pipeline, and
  the backend's svp reattachment (`from_context`) still decides separable verbs where no release
  unit covers them. Measured on 1.5M chars of HPLT (one core): segment + tokenize as today 2,337
  tokens/s, the sentence split alone (`parser`, `tok2vec`, the units pipe) 8,181 tokens/s. With
  the parse dropped, German's worker total would be about **1.59k tokens/s** (1.65x).
* The co-occurrence pass costs 2-4 % of worker time. Worker peak RSS 1.0-1.1 GB (it creeps up
  shard by shard with spaCy's string stores; workers are now replaced every 12 shards).

## Top-50k shape against the live 20k snapshots

| | es | de |
| --- | --- | --- |
| frequency at rank 1k / 5k / 10k / 20k / 50k | 883 / 102 / 31 / 9 / 2 | 789 / 116 / 45 / 18 / 6 |
| live 20k lemmas in this top 20k / top 50k | 16,566 / 19,222 | 14,462 / 17,036 |
| top-k overlap with live, 1k / 5k / 20k | 85.7 / 84.1 / 82.8 % | 81.5 / 80.4 / 72.3 % |
| Spearman on shared lemmas | 0.902 | 0.820 |
| wordfreq top-1000 overlap | 69.6 % | 66.8 % |
| entries with `unit` (compound / phrase / construction) | 819 / 738 / 20 | 397 / 566 / 14 |
| homograph keys (`Tag#day`) / keys with spaces | 46 / 1,253 | 215 / 952 |
| snapshot size | 6.2 MB | 6.5 MB |

At 7-8M tokens the tail is noise by construction (rank 50,000 at 2-6 occurrences; the plan's
bar is about 100), and the pilot slices are the head of one file (ParaCrawl) or four (HPLT), so
template text and names crowd the tail (es: 45 % of entries PROPN). What the shape does show:

* **Units rank as themselves.** Constructions land high because they count next to their member
  words: *poder + infinitivo* es rank 22, *werden + Partizip II* de 18, *es gibt* 76, *sin
  embargo* 328; reflexive and separable compounds take their own ranks (*encontrarse* 189,
  *sich befinden* 306, *sich freuen* 621, *anbieten* 158).
* **German determiners are separate lemmas** in 1.4.0: *die*, *der*, *das*, *den*, *dem*, *des*,
  *eine*, *einen*, *einer*, *einem* all rank in the top 50 (the live list folds them under *der* /
  *ein*), and *Sie*/*sie*, *Ihr*/*ihr* stay apart. That is the release's lemma convention, so it is
  what the app files; worth confirming against the guide before the full count.
* German one-token compounds from the parts list and the splitter are 10.3 % of counted
  occurrences (103k distinct compound headwords found in 8M tokens), so the release's splitter
  quality now shapes the German tail directly (some splits look wrong: `Untersuchung`, `Schals`
  as compounds of themselves). The report's "Top compound units" table is the place to review it.

## Co-occurrence

| | es | de |
| --- | --- | --- |
| items in the running file (before pruning) | 7.7M (46 MB) | - |
| items at f >= 5 | 376,721 | 394,897 |
| scored: bigrams / trigrams / 4-grams / pairs | 122k / 130k / 56k / 1.1k | 150k / 86k / 20k / 7.2k |
| shipped (positive, p < 0.001, >= 3 docs) | 195,099 rows, 3.3 MB | 152,467 rows, 2.6 MB |

At full size the shipped table hits its 400,000-row cap (about 7 MB gzipped) and the cap picks the
strongest by `g2_min`.

**Queue examples** (top combinations not on the unit list). Beside real candidates the pilot
queues are full of the slices' templates: the head of ParaCrawl is one flight-search site
(*mejor precio en jetcost*, *vuelo regular o vuelo low cost*), the head of each HPLT file a few
shops and a film site (*film auf ihr merkliste*). Candidates of the kind the pass is for:

* es n-grams: *manual de instrucción*, *alto calidad*, *pronóstico de tiempo*, *política de
  privacidad*, *alquiler de vacaciones*, *acero inoxidable*, *me gustar* / *le gustar*, *creer
  que*, *ideal para*, *estar disponible*; pairs: *reservarse*, *visualizarse*.
* de n-grams: *rund um*, *bis hin zu*, *egal ob*, *art und weise*, *umgang mit*, *zugang zu*,
  *noch nie*, *z. b*, *per e-mail*; pairs: *sich machen*, *sich informieren*, *sich nehmen*,
  *sich auszeichnen* (verb + sich + particle), *sich holen*.

The unit-free pair count does its job: the es passive *se utiliza* / *se realiza* pairs, which
the release already files under *se + verbo (impersonal/pasiva)*, dropped out of the queue
(1,118 pairs scored, 3 queued). Particle pairs with an adverb (*hier finden* -> `hierfinden`)
still reach the de queue; the annotators judge them.

## Full-run plan

Targets from plan §7 and the manifests (`corpora/*.yaml`, set from this pilot's characters per
token):

| | source | tokens | worker rate | worker core-h | main + build core-h | total |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| es | whole ParaCrawl en-es at stride 14, + Tatoeba spa | ~300M | 2.52k (Tatoeba 1.5k) | 33 | 2 | **~35** |
| de | 17 HPLT shards x 185M chars, + Tatoeba deu | ~290M | 0.96k | 84 | 1.5 | **~86** |
| de, parse dropped | same | ~290M | ~1.59k | 51 | 1.5 | **~52** |
| ja | 21 HPLT shards x 27M chars, + Tatoeba jpn | ~225M | 2.09k (1.4.0; segmenter will change) | 30 | 1 | **~31** |

Total about 150 core-hours today, about 118 with German's parse dropped.

* **es** reads the whole 25 GB ParaCrawl file (streamed, never stored) keeping every 14th
  pseudo-document: the live snapshot counted the whole Spanish side (~4.8B tokens, rank 50,000 at
  ~1,400), so 1/14 of it puts rank 50,000 near 100, and the stride spreads it over every crawl
  instead of the head's one site.
* **Disk** per language: cleaned shards are deleted as they are counted; counts files plus the
  running co-occurrence file (est. ~1 GB for 300M tokens, from 46 MB at 7.2M growing sublinearly)
  and the merged file stay under ~3 GB. Fine on this machine's allowance one language at a time.
* **Memory**: 2 workers x ~1.2 GB at the full 20M-char shards, the build ~2-3 GB.

**Proposal.**

1. **es now, locally**, 2 workers: about 18 hours wall clock, resumable
   (`python -m frequer count es ...`, rerun after any interruption; then `build`). Nothing about
   the Spanish runtime is pending.
2. **de after the German parse drop lands in honeyeater** (plan §6). The drop changes German
   lemmas, not just speed (the svp reattachment goes with it and separable verbs come from units),
   so a de snapshot counted today would be counted again anyway. Then about 26 hours locally at 2
   workers.
3. **ja last**, after the segmenter ruling, with a fresh pilot to recalibrate `max_chars_per_url`
   and the rate; about 16 hours locally.

A throwaway Railway service (§7.1, doc 06) only buys wall clock: it is the same ~120-150
core-hours, needs an image with the backend, frequer and the wheels, and the outputs have to be
fetched back. If wall clock matters, one service per language with 8 vCPU and 7 workers would
take es ~5 h, de ~7 h (parse dropped), ja ~4.5 h; not created here. Locally the whole set is
about 2.5 days at 2 cores.

Two runtime changes would cut every language's cost and are honeyeater's to make (with the
release parity check): batching sentences through the release's spaCy pipeline and the spancat
(today one call per sentence, about 75 % of es worker time), and the German parse drop above.

## App-side changes for 50k ("assumes 20k", checked in `0e1c3bbbd941`)

From plan §7 and a grep of the checkout:

* `lexicon/levels.py` `RANKED_CEILING = 20_000`, used by `reviewapp/placement_runs.py` (window
  clamp `(RANKED_CEILING - 1) // WINDOW_WIDTH` and the literal `min(399, ...)` at line 509),
  `srs/placement_inference.py` (band edges), `lexicon/frequency_classes.py`
  (`LEMMA_CLASS_EDGES` ends at it: ranks 20k-50k would read `VERY_RARE`). Keep placement at 20k
  and rename the constant to say so (plan).
* `srs/estimator.py` line 262: band 6's edge `max(FREQUENCY_BAND_EDGES[-1] * 2, 20_000)`: must
  use the same ceiling, or advanced depth deflates.
* The article estimator's p90 lexical level and band guard (ranks 20-50k stop being
  unresolved): recalibrate. Ignore-by-default restamp after load (~30k more learnable words).
* **Loader** (`lexicon/lemma_loader.py`): `_filter_entries` applies the language
  `lemma_pattern`, which rejects every unit headword (spaces, `+`, `…`, slot labels: 1,253 es /
  952 de keys here) and every homograph key (`Tag#day`: 46 / 215); snapshot identity is the
  lemma text, so `See#Fem` needs `split_key` into `(lemma, homograph)` on load; `SnapshotEntry`
  ignores the new `unit` field (decide whether `Lemma` records it). The docstring's
  `"top_n": 20000` example.
* `extension_api/settings.py` `forms_cap = 20_000` (surface-form map entries per response): with
  50k lemmas the map can exceed it; check.
* Keep at 20k deliberately: `ai/settings.py` `ai_hq_sentence_clip_rank_ceiling` (definition
  sentence audio), the free lemma-clip carve-out, `warm_definitions`.
* Validation sets (German svp, Spanish clitics) against a rank-capped set; Japanese
  `DISTINCT_SPELLINGS` (坐る, 廻る ranked separately).
* Tests and docs pinning 20k: `lexicon/tests/test_committed_ja_lemma_readings.py` (`== 20000`),
  `feed/tests/test_bench.py` (`LEXICON = 20_000`), `lexicon/tests/test_levels.py`,
  `lexicon/tests/test_frequency_classes.py`, `srs/tests/test_placement_inference.py`
  (`raw == 20_000`), `nlp/tests/test_seed_demo.py` (comment), `nlp/backends/japanese_lemma.py`
  (comment), doc 06 (§One authoritative frequency snapshot says "top-20k" and more), 
  `reference/README.md`, `reference/lemmas/README.md`, the licence manifests; a decision-log
  amendment.
* Under a release the override file no longer applies to lemmas (only the desk's database rows
  do, which frequer cannot read offline); `lemma_loader._reconcile_overrides` re-sorts by summed
  frequency when overrides are non-empty, which would undo a dispersion ranking.
