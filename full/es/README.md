> **Current snapshot (2026-11-06): the 40k list (developer ruling), on the extended counts, 1,382,684,047 tokens**
> (ten stride-28 passes of ParaCrawl r9 plus Tatoeba; the split-half stop fired at 1.32B). `snapshots/es.json`:
> 40,000 reviewed lemmas + 63 learnable names after the cut (17 counted, 46 never counted with bare entries; 6 filed
> under another lemma are reported in the header; 183 multi-word names wait for lemma release 1.6,
> `learnable-multiword-names.tsv`). Review: rounds 1-22 (`junk-review.md`): every flagged lemma in the 40k window
> reviewed and every unflagged keep in 0-40k screened, with the boundary screened to 40.5k. Rulings: two developer
> sets, follow-ups, the 40k cut, and recorded coordinator calls. Learnable names and the number rule (23 dropped):
> Honeyeater #766 `9bbae4b`. Frequency at rank 1k / 5k / 10k / 20k / 30k / 40k: 164,582 / 17,323 / 4,332 / 718 /
> 187 / 66. `load_lemmas es --dry-run`: 40,063 ranked, 0 skipped, 1,707 unit headwords, 89 homograph keys
> [sha256 9e4bcb72a6a2]. Band samples: `band-samples.md`. The sections below describe earlier builds.

# Spanish full build, 2026-11-01: lemma release 1.5.0

The top-50k Spanish lemma snapshot is in `snapshots/es.json` (the loader's format, with the provenance
header). Everything was counted through the production sentence stage of a pinned honeyeater checkout
with the `honeyeater-lemma-es` **1.5.0** wheel. Counting stopped when the split-half convergence rule fired.

| | |
| --- | --- |
| honeyeater | `44220fb34e823d8cf6d8254195f5895ecf936c14` (main; pins es 1.5.0), detached worktree, clean |
| wheel | `honeyeater_lemma_es-1.5.0-py3-none-any.whl`, sha256 `89ddf9f6ebda6dc32a6ff156634030f228c855f00ecbc3d08b57935dba2a92e1` (= `reference/lemma-releases.json`) |
| corpus | ParaCrawl r9 en-es, Spanish side, stride 28 (35 shards of 20M raw chars); Tatoeba spa whole (5 shards of 4M), counted first |
| tokens | **105,726,244** (ParaCrawl 102,399,277, Tatoeba 3,326,967); 138,221 documents; 5,707,166 sentences |
| stop | split-half rule met at 102,801,568 tokens (3/3); the final list adds one shard that finished after that checkpoint |
| filters | `corpora/exclude/es.tsv`: 1,388 exclusions (English, boilerplate, abbreviations, fragments, single letters, roman numerals); 1,363 dropped from the top 50k. Then the proper-noun rule (capitalised in >= 50 % of running-text occurrences, `corpora/case/es.tsv.gz`): 19,506 dropped, 410 learnable names kept, and 1,768 PROPN-tagged common words kept (`exclusions.md`) |
| frequency at rank 1k / 5k / 10k / 20k / 50k | 12,582 / 1,318 / 334 / **66** / **7** (before the filters: 12,698 / 1,464 / 452 / 131 / 24); samples down to 80k in `rank-samples.md` |
| loader | `manage.py load_lemmas es --path snapshots/es.json --dry-run`: 50,000 ranked entries, 50,000 new, 0 demoted, **0 skipped**; 1,628 unit headwords, 97 homograph keys |
| machine | 4 cores: 3 counting workers plus the main process, ~2.8k tokens/s per worker, ~30M tokens/h, ~3.5 h of counting |

Files here: `report.md` (the review report with the convergence and calibration tables), `convergence.md` /
`.json` (one row per shard), `es.cooc.tsv.gz` (association table, 8.4 MB), `es.cooc-queue.tsv` (labelling
queue, 2,000 rows), `es.dispersion.json.gz` (dispersion sidecar), `perf.json` (throughput per stage), `exclusions.md` and `exclusions-review.tsv` (the exclusion review), `rank-samples.md` (lemmas around ranks 20k-80k).

## Rebuilding the wheel

honeyeater-lemmatiser `model/package.py` writes `git rev-parse HEAD` into the wheel's `release.json`. The
1.5.0 es files were committed in `4f02f6b` *after* the wheel was built. So the command in the brief, run at
main (`4f02f6b`), gives `bf830b0c…`, not the pinned hash. Building with HEAD at `c8a4558` (the parent of the
release commit) and the working tree holding `4f02f6b`'s files reproduces `89ddf9f6…` byte for byte:

```bash
git -C honeyeater-lemmatiser worktree add --detach ../hl c8a4558
cd ../hl && git checkout 4f02f6b -- .
honeyeater/backend/.venv/bin/python model/package.py es model/releases/1.5.0/es 1.5.0 <out> \
    --unseen-default backend --rules name,clitic,guard --case-fold \
    --snapshot <honeyeater@44220fb>/reference/lemmas/es.json --units model/releases/1.5.0/units/es
```

## Decisions during the run

* **Stride 28, not 14.** ParaCrawl is one sequential stream, so a run the convergence rule stops early covers
  only the part of the file read so far. At stride 28 the whole file holds about 150M tokens, so a stop at
  100M has still sampled two-thirds of it. A stride-14 start was dropped after its first three shards.
* **Tatoeba first, in 4M-char shards** (manifest `first: true`), so every full-mix checkpoint holds it whole
  and the three workers share it.
* **Convergence spec** (frequer `b5f5634`): a checkpoint after every shard, and a stop after three consecutive
  full-mix checkpoints with split-half disagreement ≤ 5 % at top 20k and ≤ 10 % at top 50k.
* **Not switched to the batched runtime** (honeyeater `c07c7015`). The shards are stamped `44220fb`, so a
  re-stamp needed an equivalence proof first. The stop was then about two worker batches away, so the
  switch would have saved little. The whole list was counted under one runtime.

## Convergence at the stop (102.8M tokens)

| band | split-half disagreement | change vs previous checkpoint | median rank shift | f@N |
| --- | ---: | ---: | ---: | ---: |
| 5k | 1.4 % | 0.1 % | 3 | 1,424 |
| 10k | 2.5 % | 0.2 % | 8 | 439 |
| 20k | 4.3 % | 0.3 % | 25 | 128 |
| 50k | 9.5 % | 0.8 % | 126 | 24 |

Calibration (`report.md`): split-half disagreement runs about 1.3-2.3x a checkpoint's distance from the final
list, so the 50k band is probably within ~5 % of what more text would give.

## Review highlights

* Against the live 20k list (which still holds proper nouns): Spearman 0.931 on shared lemmas; top-k overlap 1k 87.4 %, 5k 83.1 %, 20k 67.1 %.
  wordfreq top-1000 overlap 68.5 %.
* **The tail is thin once proper nouns go.** Before the filters, PROPN was the majority tag of 28 % of the
  top 20k and 56 % of ranks 20k-50k. The proper-noun rule now drops most of them, and the list reaches about 20,900
  ranks deeper, so rank 20,000 sits at 66 occurrences and rank 50,000 at 7. The convergence check ran on the
  unfiltered list, so ranks 20k-50k are noisier than its 9.5 % says. A stable 50k of common vocabulary
  needs more text (the rest of the stride-28 pass, about 47M tokens, or a second offset pass).
* **Templates survive the stride.** The flight-search site in the head of ParaCrawl recurs throughout the
  file. The queue's head is *mejor precio (en jetcost)*, *pasaje aereo*, *vuelo low cost*, *buscador de
  vuelo*, *respuesta rápido de personal*. English leaked in as lemmas too (`the`, `city`, `beach`,
  `airport`, ...). The reviewed exclusion list now drops them (`exclusions.md`); established loans
  such as `cookie`, `resort`, `top`, `show`, `email` stay.
* Units rank as themselves: 1,628 unit entries in the top 50k (770 compound, 829 phrase, 29 construction).
* Checks flagged: form-ratio 220, singular/plural 99, lemma consistency 264, short lemmas 112, case merges 1.
* Language ID dropped 1.31M ParaCrawl lines (21 %), the same rate as the pilot. Hygiene is the pilot's.
