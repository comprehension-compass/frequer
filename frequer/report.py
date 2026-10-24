"""Render the review report (markdown) for one build."""

from __future__ import annotations

import math
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from frequer.checks import Flag
from frequer.compare import AltRanking, LiveShift, Mover, WordfreqComparison
from frequer.merge import MergeResult
from frequer.ranking import Row

SHOW = 25


def _n(x: float, digits: int = 3) -> str:
    return "n/a" if math.isnan(x) else f"{x:.{digits}f}"


def _table(headers: Sequence[str], rows: Sequence[Sequence[object]]) -> list[str]:
    if not rows:
        return ["_none_", ""]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return [*lines, ""]


def _flags(title: str, why: str, flags: Sequence[Flag]) -> list[str]:
    out = [f"### {title} ({len(flags):,})", "", why, ""]
    out += _table(["rank", "lemma", "freq", "detail"],
                  [(f.rank, f"`{f.lemma}`", f"{f.frequency:,}", f.detail) for f in flags[:SHOW]])
    if len(flags) > SHOW:
        out += [f"_{len(flags) - SHOW:,} more not shown._", ""]
    return out


def _movers(ms: Sequence[Mover]) -> list[list[object]]:
    return [[f"`{m.lemma}`", m.old_rank or "-", m.new_rank or "-",
             f"{m.new_rank - m.old_rank:+,}" if m.old_rank and m.new_rank else "-"] for m in ms]


def _override_section(result: MergeResult) -> list[str]:
    """Where the override file and the lemma step disagree on a token."""
    conflicts = result.override_conflicts
    wrong = sum(conflicts.values())
    out = [
        "### Override file against the lemma step", "",
        f"The backend's lemma has the override file applied before the lemma step, but the step prefers "
        f"its list for a form it knows. Of {result.override_tokens:,} tokens whose surface the override file "
        f"names, the step emitted a different lemma for {wrong:,}"
        + (f" (top {min(len(conflicts), 25)} below, as counted in the {len(conflicts):,} kept per shard)." if conflicts else "."),
        "",
    ]
    rows = [(f"`{s}`", f"`{w}`", f"`{g}`", f"{n:,}") for (s, w, g), n in conflicts.most_common(25)]
    return out + _table(["surface", "override says", "step emitted", "tokens"], rows)


def render(
    *,
    lang: str,
    scope: str,
    head: dict[str, Any],
    result: MergeResult,
    ranked: Sequence[Row],
    shift: LiveShift | None,
    checks: dict[str, list[Flag]],
    wf: WordfreqComparison | None,
    wordfreq_note: str,
    foreign: Sequence[Flag],
    proper: Sequence[Flag],
    alts: Sequence[AltRanking],
    live_label: str,
) -> str:
    merged = result.merged
    rt = result.runtime
    out = [f"# Review report: {lang} ({scope})", ""]
    out += [
        f"- Ranking score: `{head['ranking']['score']}`; {len(ranked):,} candidate lemmas ranked.",
        f"- Tokens counted: {merged.tokens:,} in {merged.docs:,} documents, {merged.shards} shards, "
        f"{merged.parts} dispersion parts.",
        f"- Lemma release: `{rt['lemma_package']}` {rt['lemma_version']} (sha256 `{rt['lemma_sha256'][:16]}`); "
        f"honeyeater `{rt['honeyeater_commit'][:12]}`{' (dirty)' if rt['honeyeater_dirty'] else ''}; "
        f"overrides sha256 `{rt['overrides_sha256'][:16]}`.",
        "",
        "## Corpus and hygiene", "",
    ]
    out += _table(
        ["source", "shards", "documents", "lines kept", "tokens", "dropped by hygiene"],
        [(name, t.shards, f"{t.docs:,}", f"{t.lines:,}", f"{t.tokens:,}",
          ", ".join(f"{k} {v:,}" for k, v in sorted(t.dropped.items()))) for name, t in result.sources.items()],
    )
    prov = result.token_provenance
    total = sum(prov.values()) or 1
    out += [
        "## How the runtime decided the lemmas", "",
        "Tokens by deciding layer: " + ", ".join(f"{k} {v / total:.1%}" for k, v in sorted(prov.items())) + ".",
        f"Tokens the lemma step resolved to their host's lemma: {result.host_tokens:,}. "
        f"Sentences where an independent replay of the step disagreed with it: "
        f"{result.step_mismatch_sentences:,} of {result.sentences:,}.", "",
    ]

    out += _override_section(result)
    out += [f"## Rank shifts against {live_label}", ""]
    if shift is None:
        out += ["_No live snapshot to compare with._", ""]
    else:
        out += [
            f"Live list {shift.live_size:,} lemmas, this build {shift.new_size:,}; {shift.shared:,} shared. "
            f"Spearman rank correlation on the shared lemmas {_n(shift.spearman)}; median rank ratio "
            f"{_n(shift.median_log_ratio, 2)}x.",
            "Overlap of this build's top-k with the live top-k: "
            + ", ".join(f"top {k:,} {v:.1%}" for k, v in shift.overlap.items()) + ".", "",
            "### Biggest risers (rank improves)", "",
            *_table(["lemma", "live rank", "new rank", "change"], _movers(shift.up)),
            "### Biggest fallers (rank worsens)", "",
            *_table(["lemma", "live rank", "new rank", "change"], _movers(shift.down)),
            "### Newly in the top 5,000", "",
            *_table(["lemma", "live rank", "new rank", "change"], _movers(shift.new_in_top)),
            "### Dropped out of the live top 5,000", "",
            *_table(["lemma", "live rank", "new rank", "change"], _movers(shift.lost_from_top)),
        ]

    out += ["## Ported frequer checks", ""]
    out += _flags("Form-ratio outliers", "A surface form far more frequent than the lemma's median form.", checks["form_ratio"])
    out += _flags("Singular/plural mismatch", "Lemma looks like a plural whose stripped form maps to another listed lemma.", checks["plural"])
    out += _flags("Lemma consistency", "Lemma that, met alone, lemmatises to another listed lemma (single words, so a hint, not a verdict).", checks["consistency"])
    out += _flags("Short lemmas", "Check these are real words.", checks["short"])
    out += _flags("Case merges", "Non-lowercase lemmas, with the lowercase twin where one is listed.", checks["case"])

    out += ["### wordfreq comparison", ""]
    if wf is None:
        out += [wordfreq_note, ""]
    else:
        out += [f"Top {wf.top_n} lemmas shared with wordfreq's (its forms lemmatised through the runtime): "
                f"{wf.overlap} ({wf.overlap / wf.top_n:.1%}).", "",
                "Ours only: " + ", ".join(f"`{x}`" for x in wf.only_ours), "",
                "wordfreq only: " + ", ".join(f"`{x}`" for x in wf.only_wordfreq), ""]

    out += ["## Foreign-word candidates", ""]
    out += _table(["rank", "lemma", "freq", "signal"], [(f.rank, f"`{f.lemma}`", f"{f.frequency:,}", f.detail) for f in foreign[:SHOW]])
    out += ["## Proper-noun candidates", ""]
    out += _table(["rank", "lemma", "freq", "signal"], [(f.rank, f"`{f.lemma}`", f"{f.frequency:,}", f.detail) for f in proper[:SHOW]])

    out += ["## Alternative ranking scores", "",
            "How each score reorders the default's top 5,000. Dispersion is over hash buckets of documents; "
            "see README for the definitions. Rows are the biggest risers and fallers.", ""]
    out += _table(["score", "top-5k overlap", "Spearman"], [(a.score, f"{a.overlap_with_default:.1%}", _n(a.spearman)) for a in alts])
    for alt in alts:
        out += [f"### `{alt.score}`", ""]
        rows = [(f"`{r.lemma}`", old, new, f"{new - old:+,}", f"{r.stats.freq:,}", f"{r.stats.df:,}",
                 _n(r.juilland_d), _n(r.dp_norm)) for r, old, new in alt.risers + alt.fallers]
        out += _table(["lemma", "default rank", "this rank", "move", "freq", "docs", "Juilland D", "DP norm"], rows)
    return "\n".join(out) + "\n"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
