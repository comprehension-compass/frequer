# German full run, 2026-11-01/02: the ordered steps

What was done, in order, so the run can be repeated for another language. Commits are on `full-de`.

## 1. Runtime and wheel

1. honeyeater pinned at `44883894` (PR #761 head: no dependency parse, spaCy `senter` splits sentences, de 1.5.1)
   as a detached worktree; `uv sync` in `backend/`; `de_core_news_sm` 3.8.0 installed from its GitHub wheel.
2. The de 1.5.1 wheel rebuilt from honeyeater-lemmatiser. `model/package.py` writes `git rev-parse HEAD` into
   `release.json`, so the build must run at the commit WHEELS.md names (`ceb2f99`), not at main (`5a5a9e9`, a
   docs commit): at main the sha256 was `6b924c2e...`; at `ceb2f99` it is `f14d4d64...` as pinned.
3. Wheel installed with `uv pip install --target <site> --no-deps`; frequer's extra deps (`zstandard`,
   `wordfreq`) into `FREQUER_DEPS`.

## 2. Counting

1. Manifest cap raised to 185M characters per URL (17 HPLT v2 deu_Latn files + Tatoeba deu first).
2. `count --checkpoints`, 3 workers on 4 cores. Convergence spec switched mid-start to the per-shard
   checkpoint / split-half rule (`b5f5634`); the count was restarted (no shard had finished).
3. **Batched runtime switch** (developer decision): honeyeater `c07c701` (batched sentence stage, proven
   identical on 10,216 de sentences). Drain without killing an in-flight shard: SIGSTOP the main `count` process
   (no new shards handed out), move the one queued shard's cleaned file aside (the worker that picks it fails at
   once, writing nothing), let the three running shards finish, then stop everything. 16 finished shards
   re-stamped `honeyeater_commit` 44883894 -> c07c701 (every other runtime field identical; mtimes kept so the
   checkpoint arrival order is unchanged): `restamp.json`. Throughput 1.18k -> 2.68k tokens/s per worker.
4. **Distributed counting** (developer decision): 5 parts (`count --part i/5`, URLs `k % 5 == i`); this session
   part 0 (with co-occurrence) and the coordinator (`frequer coordinate de --parts 5`); remote parts ran
   `scripts/remote-part.sh de i/5 4` from `full-de`. Setup branch `de-shards-setup`: the wheel, the spaCy model
   wheel (GitHub downloads may be blocked remotely), `SHA256SUMS`, and `skip/de.txt`, the shards already counted
   here, which remote parts pass as `count --skip-file` (cut past, never recounted).
5. **Deep extension** (developer decision, to ~450M tokens): the HPLT map lists only the 17 files already used,
   so a second source `hplt-v2-de-deep` reads the same files again from where the 185M cap stopped
   (`skip_chars: 185000000`, the cap's own stopping test, so it starts at exactly the next document; tested), cap
   110M. Same URL order, so each file stays with its part. A part that reruns withdraws its stale `DONE-p<i>`.
6. **Container restarts** killed the count, coordinator and convergence pusher three times (08:4x, 11:23, 12:51
   UTC). Each time: check `ps`, restart `count --part 0/5` (resumes: finished shards skipped, unfinished ones
   re-cut), restart `coordinate` with the new count pid, restart the pusher. One outage lasted ~7 hours because
   the restart notice was not seen until 19:37. Lesson: anything long-running needs an external watchdog, and
   `pkill -f <pattern>` must not match the shell running it.
7. Converged at checkpoint 27: 440,125,254 tokens (split-half 20k 4.3 %, 50k 6.8 %, 3/3). Three late shards
   fetched from the part branches before the build.

## 3. Build (`4fdc5a9`)

`build de` over all 274 shards: 451,548,754 tokens (hplt-v2-de 280.0M, deep 165.4M, Tatoeba 6.1M).
`load_lemmas de --dry-run`: 50,000 new, 0 skipped.

## 4. Cleaning pass

1. Merged `uplift` (exclusions, proper-noun rule, junk filter) and `full-es`'s junk follow-ups.
2. German junk configuration (`corpora/de.yaml` `junk:`): umlaut folds instead of the accent strip
   (`fold_maps`: ü->u and ü->ue, ß->ss; plus a guard so a dominant plain spelling such as *bewusst* never merges
   into the old *bewußt*); no capitalisation band; `propn_usage` instead (every PROPN-majority lemma to review
   with its share after *ein/kein* or an adjective); diversity threshold 0.3 (calibrated: below 0.3 is spam and
   templates, 0.3-0.6 mostly real words in HPLT's long documents); no fragment-final test; length limit 30.
3. Learnable place names: Honeyeater `reference/learnable-names/de.json` at `1bf77f0` (749 names). A listed name
   in the window is kept without review; any other place name drops.
4. Number rule: Honeyeater `lexicon.number_words.number_is_learnable(text, "de")` at `c48b853`, run in a separate
   process (the build runs at the counting commit `c07c701`, which predates it); a False verdict is recorded as a
   `drop` in `corpora/review/de.tsv`.
5. Review round 1 (`review/r1/`): 5,605 lemmas, two independent reviewers each, 188 disagreements adjudicated.
   Developer rulings applied: nationally famous institutions kept (Bundestag, ARD, ZDF, Deutsche Bahn); spelled
   numbers by the standing rule.
6. Round 2: the lemmas round 1's drops pulled into the 30k window (`review/r2/`).

## 5. 40k cleaning (2026-11-02), paused at the developer's request

Done and collected in `corpora/review/de.tsv`: shards r5a/r5b/r6a/r6b/r6c/r7 (8,870 lemmas), r8 (1,775 pending),
r8s (581 screener suspects), r8r (765 re-decisions under the second set of rulings). Rules: both sets of developer
rulings of 2026-11-02 are in `scripts/review/prompts/de/rules-*.md` and `full/de/junk-review.md`; names list and
number rule from Honeyeater #766 at 9bbae4b. After re-routing, kept rank 40,000 = raw rank 49,470 (f 261).

**On resume:** round 9 = the 543 pending flagged lemmas in the window plus the suspects of the third screen
(`screen40k-c`, kept positions 38,609-40,000, already screened). Run `examples.py` from the pinned Honeyeater
backend directory (it needs `config` on the path), then `review.py` (r9 flagged rules, r9s unflagged rules), gate,
`--adjudicate`, `collect.py`; route again; then `report.py` and `band_samples.py --gloss --cut 40000` with bands
0-10k/10-20k/20-25k/25-30k/30-35k/35-40k, copied to `full/de/band-report.md` and `band-samples.md`. No snapshot
until the developer confirms the 40k cutoff.
