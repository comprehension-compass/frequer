# honeyeater-frequer

Builds the per-language **top-50k lemma frequency snapshots** that
[Honeyeater](https://github.com/amyandpotatoes/honeyeater) loads
(`reference/lemmas/<lang>.json`, `manage.py load_lemmas`). It is the 2025
Spanish-only `frequer` rewritten per `docs/plans/custom-lemmatisers-and-units.md`
§7 / §7.1 (the repository is to be renamed `honeyeater-frequer`).

Nothing here lemmatises on its own. Every sentence is counted through **the
runtime**: the production backend segments it, and the production sentence stage
(`nlp.sentence_stage.analyse_sentence`, the function the article pipeline runs)
tokenizes it, asks the language's `honeyeater-lemma-<lang>` release for a lemma and
UPOS per token and for its units, spells numbers out, and merges the units into
occurrences. frequer only hands the stage the release: where the app fetches the
pinned wheel from R2, frequer gives it a `SentenceLemmatiser` over a locally
installed wheel, so a release can be counted before it is pinned. A snapshot is
therefore the same lemma identity the article pipeline emits (the pinning contract
in `reference/lemmas/README.md`).

The same pass counts **co-occurrences** (lemma n-grams, verb pairs, marginals) and
scores them into a table the unit detector can read and a queue of associated
combinations the unit list lacks, for the next labelling pass (§Co-occurrence).

## Layout

```
corpora/<lang>.yaml   manifest: sources, licences, hygiene, checks, pilot caps, observed token counts
frequer/              the package (see below)
tests/                pytest: dispersion measures and the shard merge (the pure cores)
pilot/<lang>/         committed pilot reports (report.md, perf.json); no counts, no snapshots
legacy/               the 2025 scripts and data, kept for provenance
```

`legacy/` holds the original Spanish-only `frequer.py`, `frequer-post-processor.py`,
`create_model.py`, `nonlowerlemma.py` and the data directories `final-lists/`,
`frequer-output/`, `review-ouput/`. They are **kept for provenance, not run**:
Honeyeater's current `es` snapshot was rebuilt on 2026-10-06 from
`legacy/final-lists/en-es_paracrawl_lemmatized_freq_filtered_20250502_013410.json`
(`reference/lemmas/build_es_snapshot.py`). `notes.md` at the top level records the
original post-processing ideas the review report now carries on.

### Modules

| module | role |
| --- | --- |
| `config.py` | typed manifest (pydantic): per-language data, never code branches |
| `sources.py` | resumable HTTP stream, zstd/gzip/bz2, HPLT JSONL and TSV readers |
| `hygiene.py` | length/alpha/stripped-link `GAP`, exact + normalised-line dedup, py3langid |
| `shards.py` | cut a stream into fixed-size shards; done-markers; skip finished shards |
| `runtime.py` | load the backend and lemma release outside the app; run the sentence stage |
| `counting.py` | the worker: runtime -> per-shard counts file and co-occurrence file |
| `counts.py` | shard accumulator, file format, **merge** (pure) |
| `dispersion.py` | Gries' DP, Juilland's D, chance-corrected D (pure) |
| `ranking.py` | the configurable score |
| `merge.py` | two-pass merge of all shard files, consistency checks |
| `snapshot.py` | snapshot JSON (existing schema + provenance header) and dispersion sidecar |
| `checks.py`, `compare.py`, `report.py` | the review report |
| `cooc.py` | co-occurrence items per sentence, shard file, streaming merge (pure) |
| `assoc.py` | association measures (PMI, NPMI, signed G2, min over splits) and the scored table (pure) |
| `combos.py` | compaction, final merge, the shipped table, the unit-list comparison and the labelling queue |
| `run.py`, `build.py`, `cli.py`, `perf.py` | orchestration, build, commands, throughput table |
| `forms.py`, `forms_run.py`, `select.py` | the **form inventory** and candidate selection (below) |

## Running it

Run with the Honeyeater backend's interpreter, from `honeyeater/backend`, with
`PYTHONPATH=.` plus this repository and the directory holding the installed lemma
wheels:

Count through a **pinned checkout**, not a working tree another session may be editing: a
detached worktree at the commit to record (`git -C honeyeater worktree add --detach /tmp/he-<sha> <sha>`),
run with the main checkout's `backend/.venv` interpreter. The header records the commit and
refuses to merge shards counted at another one.

```bash
cd /path/to/honeyeater-worktree/backend
export PYTHONPATH=.:/path/to/frequer:/path/to/wheel-site
export OMP_NUM_THREADS=1                       # one core per worker
export FREQUER_DEPS=/path/to/extra-deps        # zstandard (required), wordfreq (optional)
uv pip install --python .venv/bin/python --target "$FREQUER_DEPS" zstandard wordfreq

# the lemma wheel: built by honeyeater-lemmatiser's model/package.py, installed with
uv pip install --python .venv/bin/python --target /path/to/wheel-site --no-deps honeyeater_lemma_es-<v>-py3-none-any.whl

python -m frequer pilot es --data-dir /big/disk --workers 3 \
    --lemma-dir /path/to/wheel-site/honeyeater_lemma_es --wheel honeyeater_lemma_es-<v>-py3-none-any.whl
python -m frequer count es --data-dir /big/disk --workers 8     # the full corpus, resumable
python -m frequer build es --data-dir /big/disk --out-dir out/es --score frequency   # --scope pilot labels a pilot build
python -m frequer sync-manifest es --counts-dir /big/disk/es/counts
```

```bash
python -m frequer forms es --data-dir /big/disk --tokens 50000000 --workers 2 --out-dir out/inventory
python -m frequer select es --forms out/inventory/forms-es.tsv --lookup lookup.json \
    --curated es-curated.tsv --case-fold --top 1000 --min-docs 5
```

`FREQUER_DEPS` is **appended** to `sys.path`, so it can never shadow a package the
backend pins. Dependencies beyond the backend venv: `zstandard` (HPLT is
`.jsonl.zst`) and, optionally, `wordfreq`. Without `wordfreq` the report says so and
skips that section and the English-leaning half of the foreign-word signal.

* `pilot` counts a small slice (the manifest's `pilot:` block: tens of millions of characters per
  source, a few HPLT URLs for de/ja), builds it, and writes `report.md` + `perf.json`.
  It never runs the full corpus.
* `count` is **resumable**: rerun the same command after a crash and finished shards (and
  URLs whose stream was fully cut) are skipped. Disk stays at a few shard files (about
  `workers + 1` cleaned shards of `shard_chars` raw characters each) however large the corpus.
* `build` merges, ranks, and writes `out/<lang>/<lang>.json` (the snapshot),
  `<lang>.dispersion.json.gz` (sidecar), `<lang>.cooc.tsv.gz` (the association table),
  `<lang>.cooc-queue.tsv` (the labelling queue), `report.md`, `perf.json`.

## What a build does

1. **Fetch.** Each URL is streamed (`Range`-resumable on a dropped connection),
   decompressed on the fly and never stored whole. HPLT shards are 50-70 GB, so a run reads
   the first `max_chars_per_url` characters of each of several URLs. The compressed bytes read
   are hashed; a stream read to the end is checked against the manifest's `sha256` where known.
2. **Hygiene**, per shard (so a shard depends only on its own input): length bounds, alphabetic
   ratio, the lemmatiser sampler's stripped-link `GAP`, exact duplicate lines, **near**-duplicates
   (a hashed line with case, digits and punctuation erased: HPLT's repeated boilerplate), then
   py3langid. HPLT lines are first restricted to the document's `seg_langs` of the target language.
   Every dropped line is counted by reason in the shard file.
3. **Shards.** A shard is a run of whole documents totalling at least `shard_chars` raw
   characters, so boundaries depend only on the stream. HPLT has real documents; Tatoeba and
   ParaCrawl are grouped into pseudo-documents of `pseudo_doc_lines` consecutive lines. Each
   document gets a *part*: `blake2b(doc id) mod parts` (100 by default), so parts are near
   equal-sized random samples of documents.
4. **Count** (worker processes, `spawn`; each loads the runtime once). Per shard: lemma ->
   frequency, document frequency, surface forms, POS votes, occurrence kinds, per-part counts
   (plus ja readings); every unit the release found; token and document totals, hygiene drops,
   per-stage seconds and peak RSS; and the shard's co-occurrence file. An occurrence whose
   lemma is `_` or `~`, or (for a word) fails the language's `lemma_pattern`, is not counted.
5. **Merge + rank.** Two passes so memory is bounded by the candidate set (`4 x top_n` lemmas),
   not by every type in the corpus. Shards counted under a different lemma release, fallback,
   honeyeater commit or hygiene configuration are refused.
6. **Snapshot.** Existing schema `{source, corpus, pos_tagger, top_n, lemmas}`; entry order is
   rank order. Header keys added: `lemma_release` (package, version, tree sha256, wheel sha256,
   theta), `honeyeater` (commit, dirty), `overrides`, `units`, `corpus_manifest`,
   `tokens`, `documents`, `ranking`, `frequer` (commit). The loader ignores unknown header and
   entry keys. Dispersion statistics are in the sidecar, not the snapshot.
7. **Co-occurrence**: merge, prune, score, ship the table and the queue (§Co-occurrence).
8. **Report**, see below.

### POS

`pos` is the per-lemma majority vote of the tag the sentence stage gives each occurrence: the
release's UPOS (the model tags every sentence, doc 06 §The lemma step), and `X` for a
multi-token unit, as the app's merged occurrence carries it.

### Japanese readings

`reading` / `reading_source` are derived as `build_ja_snapshot.py` does: the commonest
`LemmaCandidate.reading` the backend produced (its `choose_citation` selector), with the
candidate's `reading_source` emitted where it is not `dictionary`. A vote counts only when the
final lemma equals the backend candidate's lemma (a reading belongs to the lemma it was derived
for, not to an ending or a lemma only the model chose). A lemma with no vote is read by asking the
backend's own `lemma_citation` about the lemma itself.

### Ranking

`--score` picks the ordering; the default `frequency` is raw frequency, so output is comparable
with the live lists. Every score is computed for every candidate so the report can show how each
reorders the list.

| score | definition |
| --- | --- |
| `frequency` | source-weighted token count (weights default 1: a plain sum) |
| `document_frequency` | documents the lemma occurs in (contextual diversity) |
| `juilland_u` | `f x D` (Juilland's usage coefficient) |
| `juilland_u_corrected` | `f x D / E[D]`, see below |
| `dp_adjusted` | `f x (1 - DP_norm)` |
| `cd_blend` | `sqrt(f x document frequency)` |

Dispersion is over `parts` equal-size hash buckets of documents: **Gries' DP** (0 = even,
`DP_norm` rescales to [0,1]) and **Juilland's D** (`1 - V/sqrt(n-1)`, V the coefficient of
variation of per-part rates). Juilland's D is biased low for rare lemmas even when they are scattered
at random: `f` tokens placed uniformly over `n` equal parts give `E[D] = 1 - 1/sqrt(f)`, so
`juilland_d_corrected` divides by that and caps at 1. Without it a perfectly scattered lemma at
rank 40,000 (f = 50) is penalised ~14 % for sampling noise alone. `weight` per source in the
manifest scales that source's frequency in the score (the Tatoeba blend knob); the snapshot's
`frequency` stays the raw sum.

**Caution when ranking by anything but frequency:** Honeyeater's `lemma_loader._reconcile_overrides`
re-sorts entries by their summed `frequency` whenever an override file is non-empty, which would
silently undo a dispersion ranking. See the report's note in the pilot summary.

### The review report

`report.md` per build:

* **Rank shifts** against the live `reference/lemmas/<lang>.json`: overlaps, Spearman, biggest
  risers/fallers, what entered and left the top 5,000.
* **Ported frequer checks** (parameters in the manifest): form-ratio outliers, singular/plural
  mismatch, lemma-consistency, short lemmas, case merges. "Alone" checks ask the runtime to lemmatise
  a single word, so they are hints, not verdicts (the old script had the same property).
* **wordfreq comparison** (if installed): its top forms are lemmatised through the runtime, summed, and
  the top-1000 sets compared.
* **Foreign-word and proper-noun candidates.** Foreign: wordfreq English zipf well above the
  language's, or py3langid disagreeing with high confidence. Proper noun: PROPN majority vote, or
  almost always capitalised where forms keep their case.
* **Alternative scores**: overlap, Spearman, and the biggest risers/fallers against the default
  within the top 5,000.
* **Units**: occurrences by kind, unit types found, the top units of each type and their snapshot rank.
* **Co-occurrence**: table size, what was shipped, and the head of the labelling queue.

Confirmed folds become list or override fixes in honeyeater-lemmatiser and a rebuild, never edits
to a snapshot.

### Units

Units count as themselves (plan §7, §10 D-5), following the app's own split between words and
combinations (plan §3.6):

* a **compound** is a word: one occurrence of its headword *replaces* its member words, as the
  sentence stage merges it (*me llamo* counts *llamarse*, not *llamar*; a one-token compound such
  as *irme* counts *irse*);
* a **phrase** or **construction** (a combination: not a word, counted apart in the app) counts
  *next to* its member words: *poder + infinitivo* gets its own count and rank while *poder*
  keeps every occurrence. Members keep the release's word lemma (a figure spelled out as the
  stage would).

A snapshot entry whose majority occurrence is a multi-token compound, phrase or construction
carries `"unit": "<type>"`. Unit headwords have spaces and slot labels (*tener que + infinitivo*),
and a homograph lemma keeps its key (`See#Fem`, the app's own inventory key); today's loader
`lemma_pattern` skips both, which is on the app-side list in `pilot/README.md`. The sidecar's
`units` table holds every unit the release found, claimed or not:
`{"<type>\t<headword>": [frequency, documents]}`.

## Co-occurrence

Counted in the counting pass (`frequer/cooc.py`), over the release's own word lemmas (a unit's
members keep their own lemmas, as in the text), each keyed as the unit detector keys a token
(`nlp.units.token_keys`: the lower-cased lemma; a Japanese ending with `host_keys` by its form),
with the homograph key off. Per sentence:

| item | what |
| --- | --- |
| `n` | contiguous key n-grams, n = 2-4. Punctuation and keys with no letter (figures, symbols) are boundaries: never members, never crossed |
| `p` | verb pairs within a clause: exactly the release's off-list pair candidates (`nlp.unit_rules.open_spans`, source `pair`; the reflexive pronoun and particle settings are release data: es *se*, de *sich* and separated particles), with no boundary between the members. Key: the verb, then the rest in text order (`freuen sich`, `kommen an`) |
| `u`, `t` | every non-boundary key (the marginals) and its UPOS votes |

Each item gets a frequency and a document frequency. A shard writes its items sorted
(`<kind>\t<keys>\t<f>\t<d>` under a JSON meta line), so any number merge in one streaming pass in
constant memory. During `count`, finished shard files fold into one running `cooc-acc.gz` every
`compact_every` shards (it records the shards it holds, so a resumed run never adds one twice), and
disk holds one merged file plus a few shards. `build` merges the rest, drops items below
`min_count` (5; Evert 2005 §4.1 on the unreliability of scores for very low frequencies) and scores
every n-gram and pair (`frequer/assoc.py`) as a 2x2 contingency table: observed `O11`, the
frequencies `R1`, `C1` of its two sides (unigrams or shorter n-grams from the same pass), sample
size `N` (non-boundary tokens), `E11 = R1 C1 w / N` with window `w` = 1 for n-grams and the
pair window for verb pairs (Evert 2008).

| column | measure |
| --- | --- |
| `pmi` | pointwise mutual information, `log2 O11/E11` (Church & Hanks 1990); for n > 2 against independence of all n members |
| `pmi_min` | minimum PMI over the binary splits `w1..wk | wk+1..wn` (= `pmi` for two members): every split must be associated (the split view of n-gram association: da Silva & Lopes 1999; Pecina 2010 §3) |
| `npmi_min` | normalised PMI, `pmi / -log2(O11/N)` in [-1, 1] (Bouma 2009), minimum over the splits: bounded, so usable as a feature |
| `g2_min` | Dunning's (1993) log-likelihood ratio over the four cells, signed (negative when `O11 < E11`; Evert 2005 §3.1.4), minimum over the splits |

A two-member pair is the verb against its reflexive or particle; a three-member pair (verb,
reflexive, particle) is the (verb, particle) pair against the reflexive. PMI favours rare
combinations and G2 frequent ones; Pecina (2010) compares 82 measures for collocation extraction
and finds no single best, so the table carries both and the queue filters on one and ranks by the
other.

**Shipped table** `<lang>.cooc.tsv.gz`: a `# <JSON header>` line (provenance, totals, selection,
column meanings), then `kind, n, keys, f, d, pmi, pmi_min, npmi_min, g2_min, head` (`head`: for a
pair, the headword the release's rule gives it). Kept: positively associated items
(`g2_min >= 10.83`, p < 0.001 for one degree of freedom, and `pmi_min > 0`) seen in at least
`ship_min_docs` (3) documents, at most `ship_rows` (400,000) by `g2_min`; the detector reads a
missing combination as "no evidence of association".

**Labelling queue** `<lang>.cooc-queue.tsv`: the top `queue_rows` (2,000) shipped combinations the
release's unit list does not hold, ranked by `g2_min` among those with `npmi_min >= 0.25`.
"Listed" means: the key sequence is a list entry's fixed keys or a contiguous piece of one, or (a
pair) its headword is a unit-list or parts-list headword or its keys are an entry's in any order.
Also dropped: n-grams of function words only, n-grams opening or closing on a determiner or
conjunction (`queue_edge_ban`: *el mejor*, *tener uno* are fragments), an auxiliary with a reflexive
(the impersonal *se ha*), and an n-gram that is mostly (80 %) the inside of a longer queued one.
`extends_listed` names a listed unit the n-gram contains. Web text is not ours to commit, so the
queue only *finds* combinations; sentences for them come from the clean pools, as for forms.

References: S. Evert (2005), *The Statistics of Word Cooccurrences: Word Pairs and Collocations*,
PhD thesis, Stuttgart; S. Evert (2008), "Corpora and collocations", in *Corpus Linguistics: An
International Handbook*; P. Pecina (2010), "Lexical association measures and collocation
extraction", *Language Resources and Evaluation* 44; T. Dunning (1993), "Accurate methods for the
statistics of surprise and coincidence", *Computational Linguistics* 19(1); K. Church & P. Hanks
(1990), "Word association norms, mutual information, and lexicography", *Computational
Linguistics* 16(1); G. Bouma (2009), "Normalized (pointwise) mutual information in collocation
extraction", *GSCL*; J. da Silva & G. Lopes (1999), "A local maxima method and a fair dispersion
normalization for extracting multi-word units from corpora", *MOL 6*.

## Form inventory and candidate selection

`forms` is a tokenizer-only mode (no lemma step) that finds the most frequent surface forms the
lemmatiser's labels lack (`docs/plans/custom-lemmatisers-and-units.md` §7.1, "Next labelling pass").
The manifest's `forms:` block says how: the tokenizer (`spacy_blank` = `spacy.blank(code).tokenizer`,
or the Honeyeater `backend`, as for Japanese), the script, and per source a `share` of the token
budget, an optional `stride` and a calibrated `raw_chars_per_token`.

1. **Fetch.** One worker per source URL, through the same fetch, hygiene (py3langid runs **per line**)
   and shard code as `count`. HPLT is spread over *every* shard in the manifest's map, each read to a
   character cap derived from the budget (documents arrive grouped by crawl file, so many shallow
   reads beat one deep one). ParaCrawl and Tatoeba are read whole with a `stride` over their 50-line
   pseudo-documents, so the sample spans the file. Cleaned shards are kept (a few MB gzipped) until
   the merge; the raw stream is never stored.
2. **Repeated lines.** A line (normalised as in `hygiene.near_key`: case, digits, punctuation erased)
   seen in 3 or more different documents is dropped everywhere: menus, cookie banners, footers.
   Exact in bounded memory (two 64-bit words per line occurrence, sorted and de-duplicated).
3. **Tokenize** each shard minus those lines; a word token has at least one letter. Per form: total
   count, distinct documents, distinct sites (the HPLT URL host; for ParaCrawl and Tatoeba the
   pseudo-document, so there `sites == docs`). Resumable per shard.

`forms-<lang>.tsv` is `# <JSON header>`, then `form, count, docs, sites` by descending count. The
header records tokens read, per-source URLs and caps, the hygiene drops, and what the repeated-line
filter and language ID removed.

`select` writes `candidates-<lang>.tsv` (`rank, form, count, docs, sites, score`) and a
`candidates-<lang>.json` with the token mass each exclusion took and the top-N coverage. Excluded:
forms in `lookup.json` or the curated TSV (and, with `--case-fold`, capitalised variants of those);
the default-ignore classes by rule, using Honeyeater's own `lexicon.lemma_defaults` helpers
(not language, number, foreign script, acronym) plus URL and e-mail patterns; forms in fewer than
`--min-docs` documents or 3 sites. Score is `count * docs / (docs + 20)`.

## Manifests

`corpora/<lang>.yaml` holds the source URLs, licence, expected sha256 where known, hygiene bounds,
and `observed:` token counts (written by `sync-manifest`, scoped `pilot` or `full`). Licences were
checked against `reference/licenses/{es,de,ja}.md`:

| source | licence | obligation |
| --- | --- | --- |
| ParaCrawl en-es (es side) | CC0 | none |
| HPLT v2 `deu_Latn` / `jpn_Jpan` cleaned | CC0 | none |
| Tatoeba (spa, deu, jpn) | CC BY 2.0 FR (subset CC0) | attribute Tatoeba; recorded in each language's licence manifest |

Corpus text is never committed (`data/` is ignored).

## Tests

```bash
cd /path/to/frequer && /path/to/honeyeater/backend/.venv/bin/python -m pytest
```

Only the pure cores are tested: the dispersion measures (limits, a dense reference, chance level),
the shard merge (any split of documents merges to the same totals), the co-occurrence items
(boundaries, pair keys), their merge and compaction (no shard twice), the association measures
against a hand-worked table and the weakest split, and the inventory's repeated-line filter,
forms merge and selection exclusions. Type checks:
`mypy --strict` and `ruff check` over `frequer/` and `tests/`.
