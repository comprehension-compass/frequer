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

## 8. Cutoff, names export and the 40k snapshot (2026-11-07)

1. Developer (via the coordinator): cutoff 40,000 (`corpora/zh.yaml` `top_n: 40000`, `cutoff`).
2. `full/zh/learnable-names.tsv`: every kept PROPN-majority or name-reviewed lemma in the 40k, categorised by one
   Sonnet pass (country, region, city, district, geographic, landmark, holiday, era, platform, product, company,
   institution, media, disease, ethnic, astronomy, work, group, person; 3,882 ordinary words left out), for
   Honeyeater's `reference/learnable-names/zh.json`. Reading it found five round-1 person keeps made before call 4;
   call 25 (deities keep, people drop) and their re-decision.
3. Build at frequer `37710e0`, runtime Honeyeater 8bc1817 (the counts), `--reference-root` Honeyeater main
   `7cbedf1` (the number check): `snapshots/zh.json`, 40,000 entries, sha256
   `7c0748aebab25bcf2ac345071baddf959959d20320e2634286082ac973004c31`; report in `build-40k/`.
4. `manage.py load_lemmas zh --dry-run` from a migrated local database at Honeyeater `7cbedf1`:
   `zh (dry run): 40000 ranked entries — 0 existing rows re-ranked, 40000 new, 0 demoted, 0 skipped; 147 unit
   headwords, 222 homograph keys [sha256 7c0748aebab2]`. No learnable names are appended (Honeyeater has no zh names
   list yet).

## 9. Cut confirmation and the records (2026-11-07)

1. The band files regenerated from the final list (`band-report.md`, glossed `band-samples.md`: corpus, split-half
   and per-million tables, 25 glossed keeps per band to 45k, the last 60 before 40,000, the same positions in the
   loaded es/de/ja lists). The call-25 drops pulled 马扎 into the window; round 11 kept it; nothing pending. The
   top 40,000 equals `snapshots/zh.json` (sha256 `7c0748ae…`).
2. DECISIONS: zh Simplified-only, R12 names, people/deities (call 25), the release's word cut. README: zh.
3. Developer (via the coordinator): the 40k cut confirmed; the snapshot stands. **Open:** when Honeyeater #813
   (`reference/learnable-names/zh.json`, built from `learnable-names.tsv` plus CLDR language names) merges, rebuild
   with `append_learnable_names: true` and `--reference-root` at that commit, so every listed name not already on
   the list gets an entry (ruling 2026-11-02), dry-run, and send the new sha256.

## 10. Learnable names appended (2026-11-07)

Honeyeater #813 (merged `466ccb5`; main `9da747a`) added `reference/learnable-names/zh.json` (the places of
`learnable-names.tsv` plus the CLDR language names) and `reference/number-words/zh.json`. frequer `4d8fa19` turns on
`append_learnable_names` for zh and loads the names list in `propn_evidence: tag` mode (it did not before, so the
append would have added nothing). Rebuilt at frequer `4d8fa19` with `--reference-root` Honeyeater main `9da747a`:
the top 40,000 is unchanged under the new zh number rule; 69 names appended (18 counted below the cut, 51 uncounted
at frequency 0, mostly language names); 108 multiword names the release does not emit as a unit are not appended
and are listed in `learnable-multiword-names.tsv` (unit-training input). `snapshots/zh.json`: 40,069 entries,
sha256 `ba8d5325a1ed20c6cb8bc3206e9725dcbe0c02257f67ecebd44e0fc6266fe4ed`. `load_lemmas zh --dry-run` at `9da747a`:
`zh (dry run): 40069 ranked entries — 0 existing rows re-ranked, 40069 new, 0 demoted, 0 skipped; 147 unit
headwords, 222 homograph keys [sha256 ba8d5325a1ed]`.

## 11. Recount through the registry guard (Honeyeater #820, 2026-11-07)

#820 (head `259e4dd`, not merged at the time) makes the zh lemma step replace a model lemma whose key neither the
homograph registry nor training knows (入#jiàn, 卡#zhòng) with the form's commonest listed lemma, or the form. That
changes the runtime's per-token output, so the `8bc1817` shards could not be restamped: the same 120 shards were
recounted at `259e4dd` (skip list `zh-shards-setup:skip/zh2.txt`), 8 parts on branches `zh2-shards-p*`; this
machine's part 0 was killed by repeated container restarts after 7 of its 15 shards, and its last 8 were counted by
two further sessions (`zh2a`/`zh2b` skip lists, branches `zh2a-`/`zh2b-shards-p0`, without co-occurrence). frequer
`dcb22cd` hands the release the registry as `nlp.lemma_releases._lemmatiser` does (without it, registered keys
training never saw would fold too).

Build at frequer `dcb22cd`, runtime `259e4dd`, `--reference-root` Honeyeater main `7e4a448`: **818,620,585 tokens**
(8,751 fewer: tokens the guard maps to lemmas the pattern does not count); `snapshots/zh.json` 40,069 entries,
sha256 `f2d8fe9456a0c9f4d9c55c4e4e18ae5cadcb518ba685d6e1ff407e59d02bcc7b`; `load_lemmas zh --dry-run` at `7e4a448`:
40,069 new, 0 skipped; 147 unit headwords, 166 homograph keys (was 222). Against `ba8d5325`: 56 keyed entries gone
(入#jiàn, 卡#zhòng, 落#comp …), 56 entered at the tail (all inside the reviewed 40.5k window), no new entries in the
top 10k; 6,881 top-10k entries moved, 15 by 50 ranks or more (the gaining lemmas: 入#comp 428 → 334, 卡#kǎ 1,636 →
1,296, 落#là, 空#kōng, 背#bèi).

**Open:** 23 keys outside the registry remain (书面#noodle, 成功率#lǜ, 打卡#kǎ, 流云#cloud …). They are one-token
compounds (`compound1`) whose headword the unit splitter (`nlp/unit_splitter.py` `split`) builds as the modifier plus
the head part's *lemma*: 书面 → 书 + 面, 面's commonest lemma `面#noodle` → `书面#noodle`. The word stage itself
gives 书面. A fix there changes the runtime again (a recount).

**To recount again** (after the splitter fix; coordinator 2026-11-07: same build, registry check must pass): set
`HE_COMMIT` for zh in `scripts/remote-part.sh` to the fixed Honeyeater commit; count the same 120 shards with
`SKIP_NAME=zh2` (the 39 shards outside them, on `zh-shards-setup`) and a fresh `SHIP_PREFIX` (e.g. `zh3-shards-`),
8 parts (`count --part i/8`; part 0 also counts Tatoeba and, run locally, the co-occurrence pass); receive with
`frequer.transport.receive(..., prefix=...)` and check the counts directory holds exactly the 120 names; build with
`--reference-root` at Honeyeater main; dry-run; check that every `#` key in the snapshot is a `(lemma, key)` pair of
`lexicon.homographs.registered_keys("zh")`.
