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
