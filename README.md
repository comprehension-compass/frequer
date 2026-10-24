# honeyeater-frequer

Builds the per-language **top-50k lemma frequency snapshots** that
[Honeyeater](https://github.com/amyandpotatoes/honeyeater) loads
(`reference/lemmas/<lang>.json`, `manage.py load_lemmas`). It is the 2025
Spanish-only `frequer` rewritten per `docs/plans/custom-lemmatisers-and-units.md`
§7 / §7.1 (the repository is to be renamed `honeyeater-frequer`).

Nothing here lemmatises on its own. Every token is counted through **the
runtime**: the production Honeyeater backend segments and tokenizes, and the
lemma is `LemmaRelease.lemmatise(words, spaces, backend_lemmas)` over the
installed `honeyeater-lemma-<lang>` wheel, with the backend's own lemma (override
file applied) as the fallback, exactly as the app does. A snapshot is therefore
the same lemma identity the article pipeline emits (the pinning contract in
`reference/lemmas/README.md`).

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
| `runtime.py` | load the backend, lemma release and override file outside the app |
| `counting.py` | the worker: runtime -> per-shard counts file |
| `counts.py` | shard accumulator, file format, **merge** (pure) |
| `dispersion.py` | Gries' DP, Juilland's D, chance-corrected D (pure) |
| `ranking.py` | the configurable score |
| `merge.py` | two-pass merge of all shard files, consistency checks |
| `snapshot.py` | snapshot JSON (existing schema + provenance header) and dispersion sidecar |
| `checks.py`, `compare.py`, `report.py` | the review report |
| `units.py` | the **unit-count hook** (nothing is invented; see below) |
| `run.py`, `build.py`, `cli.py`, `perf.py` | orchestration, build, commands, throughput table |

## Running it

Run with the Honeyeater backend's interpreter, from `honeyeater/backend`, with
`PYTHONPATH=.` plus this repository and the directory holding the installed lemma
wheels:

```bash
cd /path/to/honeyeater/backend
export PYTHONPATH=.:/path/to/frequer:/path/to/wheel-site
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

`FREQUER_DEPS` is **appended** to `sys.path`, so it can never shadow a package the
backend pins. Dependencies beyond the backend venv: `zstandard` (HPLT is
`.jsonl.zst`) and, optionally, `wordfreq`. Without `wordfreq` the report says so and
skips that section and the English-leaning half of the foreign-word signal.

* `pilot` counts a small slice (the manifest's `pilot:` block: a few million characters per
  source, two HPLT URLs for de/ja), builds it, and writes `report.md` + `perf.json`.
  It never runs the full corpus.
* `count` is **resumable**: rerun the same command after a crash and finished shards (and
  URLs whose stream was fully cut) are skipped. Disk stays at a few shard files (about
  `workers + 1` cleaned shards of `shard_chars` raw characters each) however large the corpus.
* `build` merges, ranks, and writes `out/<lang>/<lang>.json` (the snapshot),
  `<lang>.dispersion.json.gz` (sidecar), `report.md`, `perf.json`.

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
   frequency, document frequency, surface forms, POS votes, per-part counts (plus ja readings),
   token and document totals, hygiene drops, per-stage seconds and peak RSS. Tokens whose lemma
   is `_` or `~`, or fails the language's `lemma_pattern`, are not counted.
5. **Merge + rank.** Two passes so memory is bounded by the candidate set (`4 x top_n` lemmas),
   not by every type in the corpus. Shards counted under a different lemma release, override file,
   honeyeater commit or hygiene configuration are refused.
6. **Snapshot.** Existing schema `{source, corpus, pos_tagger, top_n, lemmas}`; entry order is
   rank order. Header keys added: `lemma_release` (package, version, tree sha256, wheel sha256,
   theta), `honeyeater` (commit, dirty), `overrides` (path + sha256), `corpus_manifest`,
   `tokens`, `documents`, `ranking`, `frequer` (commit). The loader ignores unknown header keys.
   Dispersion statistics are in the sidecar, not the snapshot.
7. **Report**, see below.

### POS

`pos` is the per-lemma majority vote. A backend that tags (de, ja) supplies the tag. `spacy-es`
is a blank pipeline with a lookup lemmatizer and tags nothing, so for languages with
`pos_source: model` the lemma model's own morphologizer tags every `pos_sample_every`-th sentence
(the vote is a sample; a rare lemma may get no vote and ships as `X`, which the loader already
treats as "unknown, upgrade on first sight"). This replaces the old GPL `es_core_news_md`
single-token tagging.

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
* Which layer (table / backend / model) decided the tokens, host-token counts, and a tripwire that
  replays the lemma step independently and counts sentences where it disagrees.

Confirmed folds become list or override fixes in honeyeater-lemmatiser and a rebuild, never edits
to a snapshot.

### Units

The unit component is not trained. `frequer/units.py` defines the `UnitCounter` protocol and the
default `NoUnits`; the shard files, merge and sidecar already carry a `units` table
(`{unit: [frequency, documents]}`). To count units, implement `UnitCounter` and pass it where
`counting.init_worker` builds `_STATE["units"]`.

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

Only the pure cores are tested: the dispersion measures (limits, a dense reference, chance level)
and the shard merge (any split of documents merges to the same totals). Type checks:
`mypy --strict` and `ruff check` over `frequer/` and `tests/`.
