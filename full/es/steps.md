# es: the steps, in order (2026-11-01/02)

1. **Wheel.** Rebuilt `honeyeater_lemma_es-1.5.0` byte-identically (sha256 `89ddf9f6…`). The wheel embeds git
   HEAD, so build at `c8a4558` with `4f02f6b`'s files checked out (README §Rebuilding the wheel).
2. **Runtime.** Pinned honeyeater `44220fb`, a clean detached worktree.
3. **Corpus.** `corpora/es.yaml`: ParaCrawl r9 en-es Spanish side at stride 28 (20M-char shards) and Tatoeba
   spa whole, counted first (4M-char shards).
4. **Count.** `python -m frequer count es`: per-shard checkpoints with the split-half stop rule (3 full-mix
   checkpoints with ≤5 % at 20k and ≤10 % at 50k). It stopped at 102.8M tokens; the final counts are 105.7M
   (40 shards). These counts stay frozen in `data-base` for every build since.
5. **First build** (50k): snapshot, cooc table, queue, report. `load_lemmas --dry-run` reported 0 skipped.
6. **Exclusion list** (`corpora/exclude/es.tsv`): English, boilerplate, abbreviations, fragments, single letters
   and roman numerals, each reviewed (`exclusions.md`, `exclusions-review.tsv`); keep rows for established loans.
7. **Proper nouns.** First a case rule (capitalised in ≥50 % of running text, `corpora/case/es.tsv.gz` from
   `tally_es.py`). It was replaced by the junk rules' `propn_band` (≥90 % drop, ≤20 % keep, middle band
   reviewed).
8. **Cap.** The list was capped at 20k, then the developer chose 30k (review to 30k; the app default-ignores
   past 25k).
9. **Junk rules** (`frequer/junk.py`): diversity (clumping < 0.6), citation, foreign (wordfreq), shape,
   propn_band, and accent merges at ratio 5. Each rule was refined on its false positives (README §Junk).
10. **Flagged review, rounds 1-7.** Two reviewers and an adjudicator per round, 1,500 ranks past the cut. Later
    rounds covered the lemmas pulled in by drops, up to 31.5k. The lemmatiser fragments became merges
    (`review_multi_flag`).
11. **Distributed extension.** `count --part i/N` plus `ship`/`coordinate` through git branches. Each new
    checkpoint is judged on the filtered list (`full/es/convergence-ext.*`). The runtime was re-stamped to
    `c07c7015` after an equivalence proof (`runtime-equivalence.md`).
12. **Band report** (`band-report.md`): a blind sample of the unflagged keeps per band. It informed the 30k
    cutoff and showed residual junk in the unflagged keeps.
13. **Unflagged review.** Round 8 covered 0-10k and round 9 covered 10k-30k, each as triage, then the union of
    suspects, then the full review (`review/README.md`).
14. **Interim top-10k** (`snapshots/es-top10k.json`): round 8 applied and pending place names left out. Dry-run:
    0 skipped.
15. **Institutions** re-decision, under the developer ruling (`review/README.md`).
16. **Place names.** Re-decided against Honeyeater #766 `1bf77f0` (1,010 names), with the learnable names
    appended after the 30k cut.
17. **Developer rulings 2026-11-02**: split loans, *halar*/*hala*, interjections (`junk-review.md`).
18. **Final 30k build and dry-run**, then a rebuild once #766's number rule lands.
