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

Interim: Honeyeater #828 loaded this snapshot (`f2d8fe94`); 23 keys outside the registry remained (书面#noodle,
成功率#lǜ, 打卡#kǎ …), one-token compounds whose headword the unit splitter built as the modifier plus the head
part's *lemma* (书面 → 书 + 面#noodle). Honeyeater #829 fixed the splitter.

**Final recount at Honeyeater main `557148c`** (#820 guard + #829 splitter fix + #830, 2026-11-08): the same 120
shards; Tatoeba counted here with co-occurrence, the rest by nine sessions (parts 1-7 on `zh3-shards-p*`, part 0's
HPLT shards in two halves on `zh3a-`/`zh3b-shards-p0`, without co-occurrence), since container restarts kept killing
long counts here. The 23 compounds now count as bare words. Their bare keys had never been judged (the screener
leaves the release's keyed entries out), so they went through the protocol with the window's new entrants (rounds
12-15: 破处 drop, 用表 → 万用表, names, slurs and mis-cuts drop; the last keep to enter the margin, 铣刀, read by the
coordinator). Build at frequer `903dcc8`: **818,620,667 tokens**; `snapshots/zh.json` 40,069 entries, sha256
`b1a44d12dc10b33ce34f071994de5a9d3cdcb88071836a30f034e72451c10830`; **0 keys outside
`reference/homographs/zh.json`** (143 homograph keys, all registered); `load_lemmas zh --dry-run` at `557148c`:
`40069 ranked entries — 0 existing rows re-ranked, 40069 new, 0 demoted, 0 skipped; 147 unit headwords (12
constructions), 143 homograph keys [sha256 b1a44d12dc10]`. Kept rank 40,000: 币种 (f 724).

**To recount again** (after the splitter fix; coordinator 2026-11-07: same build, registry check must pass): set
`HE_COMMIT` for zh in `scripts/remote-part.sh` to the fixed Honeyeater commit; count the same 120 shards with
`SKIP_NAME=zh2` (the 39 shards outside them, on `zh-shards-setup`) and a fresh `SHIP_PREFIX` (e.g. `zh3-shards-`),
8 parts (`count --part i/8`; part 0 also counts Tatoeba and, run locally, the co-occurrence pass); receive with
`frequer.transport.receive(..., prefix=...)` and check the counts directory holds exactly the 120 names; build with
`--reference-root` at Honeyeater main; dry-run; check that every `#` key in the snapshot is a `(lemma, key)` pair of
`lexicon.homographs.registered_keys("zh")`.

## 12. Recount through zh lemma release 1.7.0 (2026-11-14, Honeyeater #886)

The 1.6.4 run reproduced with release 1.7.0 (Honeyeater #885: wheel sha256 `8adc0855…`, rebuilt byte for byte
from honeyeater-lemmatiser `92b8680` and added to `zh-shards-setup`), `HE_COMMIT` Honeyeater main `4cd1389` (#885
with its homograph registry). The same 120 shards: `SKIP_NAME=zh2`, prefix `zh4-shards-`, parts 1-7 remote,
part 0's HPLT in two halves (`zh3a`/`zh3b` skip lists, prefixes `zh4a-`/`zh4b-shards-`), Tatoeba counted here with
co-occurrence. The 2-hour background limit killed most remote parts once (each resumed); part 4's container
restarted before its last three shards (20.1, 28.1, 44.1) could finish, so they were counted here with the same
command (`--part 4/8 --no-cooc`, skip list zh2 plus part 4's shipped files). The counts directory holds exactly
the 1.6.4 run's 120 names. Tatoeba is the weekly export of 2026-11-14 (sha256 `262a48ca…`; 39,747 Traditional
lines dropped), so it differs from the 1.6.4 run's export.

Honeyeater main merged #893 and #897 (zh spelled-out number spans) after the counts began; the counts are at
`4cd1389`, before them (coordinator, 2026-11-14: no recount, number lemmas come from the number rule).

Review (config `/home/user/zhrev/config.json`, window 40,500; the example sample is HPLT files 2, 6, 11, 16, 19,
33, 47, 61 to 16M characters each plus Tatoeba, since the 1.6.4 sample settings were not recorded): routing found
1,308 flagged lemmas pending, 1,021 of them `propn_band` (1.7.0 tags many ordinary words PROPN: 布置, 密码, 损伤,
维生素; 626 were 1.6.4 keeps), and 2,432 keeps new to the window, many cut-off pieces of idioms and fixed terms
(起彼伏, 突如其, 恰到). Every one went through the protocol under the recorded rules; no rule changed. Rounds:

| round | lemmas | keep | drop | merge |
|---|---|---|---|---|
| 16 (flagged) | 1,308 | 869 | 424 | 15 |
| 16s (suspects among 2,432 new keeps) | 1,154 | 558 | 373 | 223 |
| 17 / 17s (cascade; 646 new keeps) | 152 / 198 | 80 / 112 | 71 / 63 | 1 / 23 |
| 18 / 18s (114 new keeps) | 31 / 36 | 18 / 19 | 13 / 12 | 0 / 5 |
| 19 / 19s (28 new keeps) | 5 / 6 | 3 / 4 | 2 / 2 | 0 |
| 20 | 0 | (3 new keeps, no suspects) | | |

Gate queries re-examined agreed rows against the calls (莫三比克 under call 15 keep; 山中 under the word-cut ruling
keep; 嗓 keep; 比高 drop under call 24; 瞒不过, 算不算, 订好, 那群 decided consistently with earlier rounds). The
adjudicators' questions are in `questions-lemma-1.7.0.txt`; the new classes for the developer: verb + potential
complement (斗不过, 瞒不过, 受得了) and verb + resultative 好/完/下 (call 6 names only 出/到/起, aspect particles
and 于; kept as the release's cut for now); Taiwan-transliteration place names (莫三比克 for 莫桑比克; kept);
level prefix + institution (市民政局; merged into 民政局 under call 24); demonstrative + measure (那群, 那伙;
dropped); reduplicated verbs (哄哄); city nicknames (蓉城); lower-tier leagues (英甲, 中甲).

Build at frequer `44c8be7`, `--reference-root` Honeyeater `4cd1389`: **818,671,745 tokens** in 1,049,587
documents; `snapshots/zh.json` 40,061 entries (40,000 + 61 appended learnable names), sha256
`eb33dc5e22eaecce684a1c0defe26b9e75c109e7b2dffec09eff187c90aa90c7`; **0 keys outside the registry** (171
homograph keys of 216 registered pairs); `load_lemmas zh --dry-run` at `4cd1389`: `40061 ranked entries — 0
existing rows re-ranked, 40061 new, 0 demoted, 0 skipped; 176 unit headwords (11 constructions), 171 homograph keys
[sha256 eb33dc5e22ea]`. Kept rank 40,000: 药箱 (f 679). Against `b1a44d12`: top-1,000 overlap 960, top-10,000
9,498, top-40,000 37,401; 2,602 entries in, 2,610 out. Release-side findings for the next zh release: the PROPN
over-tagging above; idioms cut into pieces; 莫 filed under the lemma 莫三比克 (22,302 of its 22,311 counts are
莫) and 瓦 under 瓦努阿图; common words the 1.7.0 cut no longer emits (各种, 还有, 看起来, 是不是, 便是).
