# zh (Mandarin Chinese, Simplified) full run, 2026-11-06: the ordered steps

What was done, in order, so the run can be repeated. Commits are on `full-zh` (from `full-de`, plus uplift's
48df7d5 for multiword names in a language written without spaces). Calls and rulings: `junk-review.md`.

## 1. Runtime and wheel

1. Honeyeater pinned at `8bc18170` (main, 2026-11-07 07:40 +11: zh pins lemma release 1.6.4, `jieba-zh` with
   the 1.6.0 segmenter over jieba's tokens, the zh number speller) as a detached worktree; `uv sync` in `backend/`.
2. The zh 1.6.4 wheel is in R2 only, which needs credentials this session lacks, so it was rebuilt from
   honeyeater-lemmatiser at `fa4d132` with `model/package.py` exactly as `model/releases/1.6.4/WHEELS.md` says:
   sha256 `27abd5c0320580550aad309c25eab062f1f53dd15f6132650a454b7858d75f91`, identical to the pin. Installed
   with `--no-deps`; published for the remote parts on branch `zh-shards-setup` with `SHA256SUMS`.
3. The runtime checked by hand on test sentences: segmenter words, reading and sense keys (去#qù, 花#spend,
   了#le), 睡…觉 counted as the compound 睡觉, figures spelled (2025 → 二〇二五, 1,000 → 一千).

## 2. Manifest and hygiene (`corpora/zh.yaml`)

1. HPLT v2 `zho_Hans` cleaned, all 79 files of the map, 32M raw characters each (2 shards of 16M), and Tatoeba
   `cmn` whole, first. zh Wikinews left out (`junk-review.md`).
2. New hygiene options (frequer): `simplified_only` (a line OpenCC `t2s` changes is dropped; a document with
   >= 20 % Traditional lines is dropped whole) and `langid_aliases: [wuu]`. Both stay out of the shard config
   hash at their defaults, so es/de/ja shards keep their identity.
3. No `reference/lemma-overrides/zh.json` exists: the runtime header records `absent`.
4. Junk rules as ja (diversity 0.2, citation, shape with one-character lemmas, number rule), with
   `propn_evidence: tag`: every PROPN-majority lemma is reviewed. `review_top` 40,500 (the 40k cut with a margin).

## 3. Pilot (`pilot/zh/`)

2.9M tokens (4 HPLT shards of 1.5M characters, Tatoeba 1M characters): ~4.7 raw characters per counted token,
~2,700 tokens a second per worker (the sentence stage dominates); Tatoeba is 45 % Traditional (dropped).

## 4. Distributed count

6 parts (`count --part i/6`): this session part 0 (Tatoeba, co-occurrence, `frequer coordinate zh --parts 6`),
five child sessions parts 1-5 running `scripts/remote-part.sh zh i/6 4`, shipping to `zh-shards-p<i>`.

Two container restarts here and several in the part sessions; each part resumed itself (`remote-part.sh` is
resumable), and this session restarted part 0 and the coordinator. The 50k split-half plateaued near 6-8 % from
~400M tokens (the HPLT crawl-grouping floor ja met), then fell: **converged at 770,163,267 tokens** (3/3 full-mix
checkpoints; split-half 20k 4.7 %, 50k 5.9 %; `convergence.md`). Parts in flight were stopped; every shipped shard
was received (p1 16, p2 22, p3 26 + DONE, p4 21, p5 20, part 0 the rest).

## 5. Build

`frequer build zh` over all 120 shards: **818,629,336 tokens** in 1,049,585 documents (HPLT 818.3M, Tatoeba 0.35M);
192,409 candidate lemmas. Hygiene dropped 211,507 Traditional lines and 221,290 lines of Traditional documents
(`report.md`). Kept rank 40,000 = raw rank 44,739 (f 726, 0.89 per million).

## 6. Review (rounds 1-10; rulings and calls in `junk-review.md`)

Run in this session with the review runner (`claude -p` reviewers: two Sonnet reviewers, an Opus adjudicator), the
gate read by the coordinator between the stages each round. Started on the 462M-token checkpoint counts while the
parts finished (decisions are per lemma, so they carry over), then on the final counts:

1. Round 1: 5,835 flagged lemmas in the 40.5k window (96.5 % agreement; 213 adjudicated incl. 10 queries).
2. Screen: two screeners over the 34,440 unflagged keeps; the first screen over-listed compositional compounds,
   the screener was corrected (the release's word cut stands) and rerun: 7,530 suspects, reviewed as round 2 with
   the unflagged rules (2,046 adjudicated, 1,366 of them queried agreed drops decided before the calls).
3. Round 1r: 828 round-1 lemmas re-decided under calls 1-10 (112 changed).
4. Final counts: round 3 (887 flagged pending), round 4 (1,071 suspects among 3,116 keeps new to the window),
   round 5 (186 re-decided under calls 16-19), round 6/6x (cascade; degree adverb + adjective, call 22), rounds
   7-10 (the cascade to a clean window).
5. `corpora/review/zh.tsv`: every decision with its reason; nothing pending in the 40.5k window.

The reviewers' `# question` lines were settled as calls 1-24 under the standing delegation, on the established
rulings' pattern (cities and districts, suffixed place forms, brands and SOEs, people and canonical works,
offices, the release's word cut against its mis-cuts, number words, web-fiction vocabulary, newspapers, gambling
words). None raised a new class needing the developer.

## 7. Cutoff material

`scripts/review/report.py` (bands to 45k) → `band-report.md`; `band_samples.py --gloss --per-band 25 --cut 40000
--deeper 45000` → `band-samples.md`, with the frequency per million at kept ranks and the same positions in the
loaded es/de/ja snapshots added. No snapshot until the coordinator confirms the 40k cutoff.
