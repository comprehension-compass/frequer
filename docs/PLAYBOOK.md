# Playbook: building a learnable frequency list for a language

How a language's list is built, start to finish, so it can be repeated for es, de and ja and done for a new
language with every decision already settled. It is written for the **orchestrating agent** who runs the build
with the developer, not as a push-button script. The rulings it applies are in [DECISIONS.md](DECISIONS.md),
each with its date, rationale and where the code enforces it.

The chain this sits in:

1. **Lemmatiser release** (honeyeater-lemmatiser): annotate, train, score, package, upload, pin.
   [RELEASE-PLAYBOOK](https://github.com/comprehension-compass/honeyeater-lemmatiser/blob/main/docs/RELEASE-PLAYBOOK.md).
2. **Frequency list** (this repository): count large corpora through the production sentence stage with that
   release, clean the list, cut it, append place names. This playbook.
3. **Load and derive** (Honeyeater): load the snapshot, rebuild the defaults and everything derived from them,
   pre-generate. [docs/runbook/language-pipeline.md](https://github.com/comprehension-compass/honeyeater/blob/main/docs/runbook/language-pipeline.md).

## Principles

* **Code does the mechanics; judgement stays with agents and the developer.** Counting, convergence,
  distributed coordination, the heuristic flags and routing, merges, the number rule, appending names, builds
  and dry runs are commands. Every judgement is a person's or a reviewer's: the review rounds, triage, audits,
  the cutoff, place names and institutions, and every `# question`. Code routes items **to** judgement and
  records the outcome; it never replaces one.
* **The loaded list is the learnable set.** Anything on it is learnable by default; anything off it is ignored
  by the app. So junk on the list is a learner-facing bug, and a real word left off is too.
* **Look before moving on.** No stage proceeds until its outputs have been looked at: sample checks, and counts
  compared with expectations. Each section below says what to look at, what "looks wrong" means (with the real
  cases from the 2026-11-01 runs), and when to stop and ask the developer.
* **A rule is automated only once it has proved itself on reviewed data**, and is validated on a sample before
  it acts. On 2026-11-01: the ja diversity threshold was moved to 0.2 after a first run flagged 14,500 lemmas;
  an other-language rule that over-flagged real words was rejected; the proper-noun capitalisation rule was
  replaced by a band (drop >= 90 %, keep <= 20 %, review between) once its false drops were read.
* **Every automated drop is auditable and reversible** through the review file: a reviewed `keep` in
  `corpora/review/<lang>.tsv` outranks the proper-noun drop and vetoes an accent merge, and every drop is listed
  with its evidence in `<lang>.flags.tsv` and the report.
* **Rulings are recorded with their rationale**, in DECISIONS.md and the language's `full/<lang>/junk-review.md`,
  in the same commit as the change they cause. `# question` lines go to the developer; they are never settled
  silently.

`python -m frequer pipeline <lang> [--review-config <config.json>]` prints where a language stands: each stage
`done`, `next` or `waiting`, the next command, what to look at and when to ask. It is read-only and only checks
that files exist; reading them is still your job.

## Sessions and machines

The full runs used one **orchestrating session** (the build for one language), optional **part sessions**
(distributed counting) and headless `claude -p` reviewers launched from the orchestrator.

* **Pre-approve tools** when creating a session (`create_session` `extra_allowed_tools`): `Bash`, the remote
  session tools (`send_message`, `add_repo`), and running `claude`/`python`. On 2026-11-01 sessions stalled for
  hours on a permission prompt nobody saw.
* **Pin revisions by branch name or full SHA.** A short SHA as `source_revision` fails with `ref_not_found`.
* **Long processes need a watchdog.** Container restarts killed the de count, coordinator and convergence pusher
  three times; one outage lasted ~7 hours because the restart went unseen. After any restart, check `ps`, then
  restart the count (it resumes), the coordinator (with the new count PID) and any pusher. Run them from a frozen
  worktree, not a working tree another process edits, and push from a separate clone.
* **Kill exact PIDs.** `pkill -f <pattern>` matched the calling shell and killed it (exit 144).
* **Check reviewer output, not reviewer claims.** An agent reporting "done" may have stopped part-way (one
  screener stopped after 1,399 of 4,769 rows): the scripts refuse missing or extra lemmas; restart a fresh agent
  on the remainder only.

## 1. Corpus and manifest

`corpora/<lang>.yaml` holds everything per language as data (`frequer/config.py`): sources, hygiene, language
settings, the junk configuration and the observed token counts.

* **Licence rule: public domain, CC0 or CC BY only** (no SA, NC, ND). `frequer pipeline` checks every source's
  `licence`. Used so far: HPLT v2 cleaned (CC0), ParaCrawl release 9 (CC0), Tatoeba (CC BY 2.0 FR).
* **Tatoeba first.** Tatoeba is the closest thing to learner-level text; it is small, so it is counted whole,
  before the web (`first: true`, small `shard_chars` so the workers share it), and every checkpoint holds it.
* **Stride sampling across the whole file.** A web file's head is often one site's templates (the ParaCrawl
  en-es head is a flight-search site), so never cap a file without a `stride`: keep every n-th document so a run
  that stops early still samples the whole file. Size the stride for the token count you expect to stop at (es:
  stride 28 for ~150M tokens). Multi-URL sources round-robin, one shard per URL in turn.
* **More text later** without recounting: `stride_offsets` (disjoint passes over one file as virtual URLs; the es
  extension read offsets 0-9) or a second source with `skip_chars` (a deeper pass over files an earlier source
  capped; the de deep extension skipped each HPLT file's first 185M characters). Both keep shard names stable.
* **Pilot** (`frequer pilot <lang>`): a small slice through the same code. Look at characters per token, the
  language-ID drop rate, throughput, and the report's samples; size the full run from them.

Ask the developer before adding a source, raising a cap past the plan, or when a licence is unclear.

## 2. Counting

Count through **the runtime**: a clean, detached worktree of Honeyeater at the commit you record, its
`backend/.venv` interpreter, and the language's lemma wheel installed with `--no-deps` into a site directory
(README §Running it). Build the wheel byte-identically at the commit the release names: the wheel embeds the
git HEAD it was built at, so a build at a later docs commit has another sha256 (RELEASE-PLAYBOOK).

```bash
cd <honeyeater worktree>/backend
export PYTHONPATH=.:<frequer>:<wheel site> OMP_NUM_THREADS=1
.venv/bin/python -m frequer count <lang> --checkpoints --lemma-dir <site>/honeyeater_lemma_<lang> --wheel <wheel>
```

**Distributed counting** (README §Distributed counting) when one machine is too slow: `count --part i/N` counts
URLs `k % N == i`; part 0, the coordinator, also counts Tatoeba and the co-occurrence pass.

1. A setup branch `<lang>-shards-setup` holds the wheel(s), `SHA256SUMS` and, if the coordinator already counted
   shards, `skip/<lang>.txt` (their names; remote parts pass it as `count --skip-file` and cut past them).
2. Add the language to `scripts/remote-part.sh` (its wheel, sha256 and any extra model, as for de's spaCy model).
3. Start each part session with the tools pre-approved (above); each runs `scripts/remote-part.sh <lang> <i/N>
   <workers>`, which counts and runs `frequer ship` (counts files to `<lang>-shards-p<i>`, `DONE-p<i>` when its
   pass completes; a part that runs again withdraws a stale `DONE` marker).
4. The coordinator runs its part and `frequer coordinate <lang> --parts N --repo <scratch clone> --local-pid
   <count pid>`; it takes the checkpoints and pushes `<lang>-shards-stop` on convergence.

**Look at:** every shard header's lemma release and Honeyeater commit (the ja count first ran on a stale
lemmatiser commit and was restarted; the merge refuses mixed runtimes, but catch it early); throughput per worker
against the pilot (de went from 1.18k to 2.68k tokens/s with the batched stage); that every part and the
coordinator are alive after any restart; that `DONE` markers match what the parts actually finished.

**Restamping** a shard's runtime commit is allowed only after an equivalence proof that the two runtimes produce
identical output (es `full/es/runtime-equivalence.md`; de: 10,216 sentences identical). Record the old commit in
a top-level `restamped_from`, never inside `runtime`, and keep the files' mtimes (checkpoint order follows
arrival). Never restamp to paper over a real difference.

## 3. Convergence

Counting stops when the list is stable (README §Convergence checkpoints). After every shard, the shards so far
are merged, **filtered** (exclusions, proper-noun rule, junk rules: the list the snapshot will hold) and ranked.
**Stopping rule: three consecutive full-mix checkpoints with split-half disagreement <= 5 % at the top 20k and
<= 10 % at the top 50k.**

**Look at** `convergence.md`: the split-half columns falling, the mix `full`, and the **calibration table**
(each checkpoint's top N against the final list's). Two independent halves differ about twice as much as either
differs from the converged list; es measured 1.3-2.3x.

**Known floor: crawl grouping.** HPLT keeps a site's pages together, so its halves differ by site as well as by
sampling, and split-half has a floor. In ja the 50k split plateaued near 9.4-10 % from ~300M tokens while the
distance to the final list kept falling (3.0 %), and the calibration ratio rose from ~2 to 3+. If split-half
plateaus above the threshold, read the calibration table before counting more, and ask the developer whether to
extend or accept: a plateau with a falling distance-to-final is the floor, not instability. Results: es stopped
at 102.8M tokens (105.7M counted), de at 440M (451.5M), ja at 690M.

## 4. First build and the junk heuristics

```bash
.venv/bin/python -m frequer build <lang> --reference-root <honeyeater checkout with the current reference data>
manage.py load_lemmas <lang> --path out/<lang>/<lang>.json --dry-run      # in Honeyeater backend: 0 skipped
```

`--reference-root` is the Honeyeater checkout the app's reference data and checks come from (learnable names,
the number check), apart from the pinned runtime the counts were made with; the header records both.

The build applies, in order (`frequer/filters.py`): review splits and merges, accent merges, ranking, the
exclusion list (`corpora/exclude/<lang>.tsv`: English leakage, boilerplate, abbreviations, each reviewed; `keep-*`
rows protect established loans), the proper-noun rule, then the junk rules and routing (`frequer/junk.py`). The
rules flag with evidence; **2+ flags drop, 1 flag goes to review** within `review_top` (with `review_multi_flag`,
2+ flags in the window are reviewed too, so cut-off real words become merges, not drops).

| rule | flags | es | de | ja |
|---|---|---|---|---|
| `diversity` | concentrated in few documents for its frequency | 0.6 | 0.3 | 0.2 |
| `citation` | the lemma's spelling is never written | verbs exempt | on | verbs/adjectives exempt; token-separated forms read joined |
| `foreign` | wordfreq English much above the language | on | on | off (no Latin script) |
| `shape` | hyphen, digit, reduplication, fragment, length | `lnrdz` fragment finals | no finals; length 30 | one character only |
| proper nouns | | `propn_band`: capitalisation in running text, drop >= 90 %, keep <= 20 %, review between | `propn_usage`: every PROPN to review with its article/adjective share (all nouns are capitalised) | `propn_band` with Sudachi 固有名詞 subtags: 人名/組織名 + PROPN drop, 地名 pending names |
| accent merges | unaccented spelling into the accented lemma at 5x | strip accents, **ñ kept** | umlaut maps ü→u, ü→ue, ß→ss; **ß kept** as a letter; a dominant plain spelling (*bewusst*) never merges | off |
| number rule | Honeyeater's `number_is_learnable` says False: dropped | on | on | on |

**Diversity is a flag only, never a reordering**: the ranking stays raw frequency. The thresholds were
calibrated per language on samples (HPLT documents are long, so real words clump more than in es's
pseudo-documents).

**Look at** `report.md`: rule hits, the **rule-overlap matrix** (correlated flags such as foreign + shape +
proper noun on English acronyms are not independent evidence), the diversity calibration per frequency band, and
the samples per flag. **Looks wrong** (all seen on 2026-11-01): English leaking in as lemmas (`the`, `city`,
`airport`); common nouns the tagger called names (*kayak*, *palma*, 返品, *Hotel*); clipped lemmas (*jugabl*,
送 for 送る); spelled numbers (千九百九十八, *dreihundertsechzig*); Tatoeba-heavy real words in the diversity tail;
participles under citation; ñ stripped by an accent merge (*campana* → *campaña*). A false-positive class means a
rule fix, validated on a sample, before review starts. A new rule or threshold is a developer decision.

## 5. Review rounds

The review runner (`scripts/review/`, its README has the commands) is a tool you invoke and inspect, one step at
a time. Write a JSON config; the rules are versioned files in `scripts/review/prompts/<lang>/` (start a new
language from `prompts/TEMPLATE/`, and have the developer read the rules before the first round: they are
binding).

**The protocol** (developer ruling, 2026-11-01): every routed lemma gets **two independent reviewers** (the
cheaper model tier) who see the rules, the lemma's rank, frequency, POS, flags with evidence, written forms and up
to three example sentences in which the production lemmatiser filed it, and never each other's answers; **an
adjudicator** (the stronger tier) decides their disagreements. Decisions: `keep`, `drop`, `merge:<lemma>`,
`pending-names` (places), and the developer's `split:` for a broken lemma holding two words. Anything the rules
don't settle becomes a `# question` line for the developer.

A round: `route.py` → `examples.py` (check that ~85 %+ of lemmas got an example) → `review.py` (reviewers, then
it stops) → **your check**: read `agreed.tsv` (every merge, a sample of drops) and `accent-merges.txt` (a merge
can hide a second real word: es *comisaria*/*comisaría*, *clara*, *vaya*), write `queries.tsv` → `review.py
--adjudicate --queries` → `collect.py` → send the questions → `route.py` again. Drops pull new lemmas into the
window, so review with a margin (es reviewed to 31.5k for a 30k list) and repeat until nothing is pending.

**Look at:** the agreement rate (es and ja: ~95 %; much lower means the rules are unclear), the decision mix per
flag, the questions. **Stop and ask** on any new class of question; a ruling becomes an edit to the rules file,
a line in `junk-review.md` and DECISIONS.md, and a re-decision round (`collect.py --redecide`) for the affected
lemmas. Scale (es): 9 rounds, ~2-3k lemmas in the first, chunks of ~740 per reviewer.

## 6. Triage of unflagged lemmas

A blind sample found a few per cent junk among the lemmas no rule flagged, so they are screened too:
`screen.py` sends the unflagged keeps (no examples, batches of 250) to two screeners ("when in doubt, list it");
anything either lists goes through the full protocol with the unflagged rules (the lemmatiser's conventions
stand: function words, gendered nouns with their own entry, pronominal verbs). The release's own entries (units,
homograph keys, learnable names) are left out. es: 28,282 screened, 3,253 reviewed.

**Look at:** the suspect rate per band, and 30 suspects and 30 non-suspects by eye. If the screeners miss a class
of junk you can see, fix the screener prompt (a ruling) and rescreen.

## 7. Audit, the per-band report and the cutoff

* **Spot audit** (`audit.py`): random keeps and drops per band through the full protocol as an `audit-*` round.
  Never applied: it estimates the real-lemma share of the keeps and the false-drop share of the drops.
* **The per-band report** (`report.py` → `band-report.md`; bands 0-10k, 10-20k, 20-25k, 25-30k by default):
  actions per band, the real share among reviewed lemmas, rule hits, the audit estimates, 30 keeps at each band
  edge, 50 random drops, every merge, every question.
* **The developer picks the cutoff** from this report (es and ja: 30k; de pending). Record it as
  `language.top_n` and `language.cutoff` (the ruling) in the manifest. Extend deeper only if 25-30k still holds
  enough real lemmas. There is no separate depth band: the loaded list is the learnable set.

## 8. Place names and institutions

**Places** get `pending-names` in review, never a decision, until Honeyeater's reviewed learnable-names list
(`reference/learnable-names/<lang>.json`, Honeyeater PR #766) is final. That list is built and reviewed in
Honeyeater by its own two-reviewer protocol from CLDR and GeoNames (countries, continents, oceans, well-known
cities, US states with a target-language name, famous first-level divisions; same-spelled foreign places
ignored; bare forms added). Then set `names_final: true` and `append_learnable_names: true`, route and build with
`--reference-root` at a checkout holding the final list: a pending place in the list is kept, any other place is
dropped (`place-drop`), and listed names that rank below the cut are appended after it. Learnable status is a
union, so a listed name that is also a common word is kept. An interim list built before the names are final
uses `build --leave-out-pending-names`.

**Institutions** (ruling: famous institutions that aren't places are kept): screen the review and proper-noun
drops in the window with `screen.py --pool drops` and the institutions screen (positive selection: "be
generous"), then review the picks with `--decisions keep,drop` and apply with `--redecide`. es: 23,842 drops
screened, 754 picked, 158 kept. Other names drop: people, minor companies, brands, products.

## 9. Snapshot and load dry run

```bash
.venv/bin/python -m frequer build <lang> --reference-root <checkout>           # top_n + appended names
manage.py load_lemmas <lang> --path out/<lang>/<lang>.json --dry-run           # Honeyeater backend: 0 skipped
```

**Look at:** 0 skipped (skips came from merge targets that were missing, capitalised or multi-word, all fixed in
`junk.apply_merges`); entries = `top_n` plus the appended names; the header's hashes of the review file,
exclusion list and names list; the number check's source. Then commit the snapshot, report and review files on
the language's build branch, and hand over to Honeyeater's runbook (pin, load, rebuild the defaults, pre-generate).
**Combined deploy:** a change to the app's default-ignore rules ships in the same deploy as the new lists (PR #766
removes the proper-noun default rule, so it must not reach production ahead of the cleaned snapshots).

## 10. Failure modes we hit (2026-11-01/02)

| what happened | sign | what to do |
|---|---|---|
| Container restart killed count, coordinator, pusher | no new checkpoints; `ps` empty | restart count (resumes), coordinator with the new PID, pusher; keep a watchdog |
| Session stalled on a permission prompt | no progress for hours, no error | create sessions with `extra_allowed_tools`; check on parts |
| Stale `DONE-p<i>` after a part reran with a bigger manifest | coordinator ends early | `ship` withdraws it now; check markers against shard counts |
| Runtime restamp | merge refuses shards | only after an equivalence proof; `restamped_from` at top level; keep mtimes |
| Count on a stale lemmatiser commit | wrong release in shard headers | check headers before merging; recount |
| Wheel sha256 mismatch | the release's hash differs | build at the commit the release names (the wheel embeds HEAD) |
| `pkill -f` killed its own shell | exit 144 | kill exact PIDs |
| Working tree changed under a long run | odd failures mid-run | frozen worktree for runs, separate clone for pushes |
| Agent stopped part-way | missing rows | the scripts refuse gaps; rerun on the remainder only |
| Drop cascade | new pending lemmas after each round | review with a margin; repeat rounds |
| Loader skips | `load_lemmas --dry-run` skipped > 0 | fix merge targets (rename, fold case, compound) |
| Number rule needs a newer Honeyeater than the runtime | `number_is_learnable` missing | `--reference-root` at the newer checkout (it runs in a subprocess) |
| Split-half plateau | 50k split stuck near 10 % | read the calibration table: the crawl-grouping floor; ask the developer |

## 11. A new language, in short

1. Lemmatiser release pinned (RELEASE-PLAYBOOK). 2. Manifest with licence-clean sources, Tatoeba first, a stride;
pilot. 3. Junk configuration from the closest language above; validate every threshold on a sample. 4. Prompt
files from `prompts/TEMPLATE/`, read by the developer. 5. Count, converge, build, route, review rounds, triage,
audit, band report; the developer picks the cutoff. 6. Names final, final build, dry run, Honeyeater runbook.
Run `frequer pipeline <lang>` at every step.
