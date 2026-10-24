# Pilot, 2026-10-24

End-to-end run of `python -m frequer pilot <lang>` per language, on a small slice (never the full
corpus), counted through the production backends and the **test** lemma wheels
`honeyeater_lemma_{es,de,ja}-0.0.1` built from `honeyeater-lemmatiser` `model/releases/2026-10-24`
(honeyeater `f4495a68bf53`). The wheels are development builds, so ranks and lemma choices here
say nothing about the final lists; what the pilot tests is the pipeline and its cost.

Only the reports are committed (`<lang>/report.md`, `<lang>/perf.json`). The counts and the
snapshots stay out of the repository.

## Slice

| | es | de | ja |
| --- | --- | --- | --- |
| HPLT / ParaCrawl | first 14M chars of ParaCrawl en-es (es side) | first 9M chars of each of HPLT `deu_Latn` 10 and 11 | first 2M chars of each of HPLT `jpn_Jpan` 10 and 11 |
| Tatoeba | first 1.5M chars | first 1.5M chars | first 0.5M chars |
| shards (cleaned, ~2.5M / 2.5M / 1.2M raw chars) | 8 | 9 | 5 |
| tokens counted | 2,243,868 | 1,635,486 | 1,804,735 |
| documents | 3,381 | 5,189 | 2,498 |

Partial reads of an HPLT file are one crawl file deep (documents arrive grouped by WARC), which
is why two URLs are read; a full run should read many.

## Throughput (this container: 4 cores, 3 counting workers + the main process)

"tokens/s" is counted tokens divided by the core-seconds a stage spent, summed over all shards,
so it is a per-core rate and stages can be compared and added (1/total = sum of 1/stage).

| stage | es | de | ja |
| --- | ---: | ---: | ---: |
| fetch + decompress + parse (main) | 822k | 127k | 193k |
| hygiene filters (main) | 591k | 514k | 1,253k |
| py3langid (main) | 191k | 217k | 312k |
| read shard (worker) | 10.9M | 9.7M | 5.6M |
| backend segment | 66.6k | **2.0k** | 1,164k |
| backend tokenize | 115.8k | 47.7k | **13.5k** |
| backend lemma + overrides | 64.1k | 806k | 1,122k |
| lemma step (`LemmaRelease.lemmatise`, model where needed) | **9.9k** | 11.1k | **6.7k** |
| model POS on every 8th sentence | 61.5k | - | - |
| tally (count) | 258k | 184k | 145k |
| **worker total, per core** | **6.1k** | **1.6k** | **4.2k** |

* Where the time goes: es and ja are bound by the lemma step (the model runs for 10% / 26.5% of
  tokens: those the list does not settle); ja also by Sudachi tokenization; **de is bound by the
  backend's `segment`, which runs the full `de_core_news_sm` parse** (80% of worker time).
  Main-process work (fetch, hygiene, langid) is 2-6% of the worker cost and one core feeds many workers.
* Extrapolated to the plan's targets from these per-core rates: de 275M tokens ~ 48 core-hours, ja
  220M ~ 14, es 250M ~ 12. (Plan §7.1 estimated 65 / 12 / "a few hours".)
* Wall clock for the counting step at 3 workers: es 162 s, de 531 s, ja 198 s.

## Peak memory (RSS)

| process | es | de | ja |
| --- | ---: | ---: | ---: |
| counting worker (runtime loaded once, each shard) | 447 MB | 447 MB | 515 MB |
| main process (stream, hygiene, langid) | 149 MB | 150 MB | 148 MB |
| build (merge + rank + snapshot + report, incl. a runtime for the checks) | 694 MB | 898 MB | 730 MB |

The worker figure is flat in shard size (a shard's counters are about 100 MB). The build figure
grows with the candidate set (`4 x top_n` lemmas in full detail, plus one frequency counter over
every lemma type in pass one), so expect low single-digit GB at the target sizes, not these numbers.

## What the pilot found

* **The override file and the lemma step disagree** (new "Override file against the lemma step"
  section in each report). The backend's lemma has the override file applied, but the step takes its
  own list's lemma for any form it knows, so the override loses. es: 7,969 of 348,678 override-named
  tokens; de: 2,994 of 243,317, e.g. `möchte`/`möchten` -> override `mögen`, step `möchten`. The shards
  record the top conflicts; they are lemmatiser-list fixes, not frequer's to settle.
* **Japanese endings are counted for their host.** 150,961 of 1,804,735 ja tokens (8.4%) are
  resolved to their host's lemma (`<=`), and are counted into the host's frequency (config
  `host_tokens: count`, the literal reading of "count through the runtime"); the endings (`ます`, `た`,
  `て`) therefore do not rank as lemmas of their own. `host_tokens: skip` counts each word once.
  The effect on verbs' frequencies and on the ranking should be a developer decision.
* Dispersion works as intended at this scale: a name that occurs 96 times in a single document
  (`Kofahl`, de rank 1,542 by frequency) falls to rank ~36,700 by `document_frequency`. The scores
  barely move the top 1,000.
* es lines: 20% of ParaCrawl lines fail py3langid (mostly mis-aligned or mixed-language pairs).
