"""Report, header entry and sidecar for the junk-filter heuristics (``frequer/junk.py``)."""

from __future__ import annotations

import random
from collections import Counter
from pathlib import Path
from typing import Any

from frequer import junk
from frequer.config import Manifest
from frequer.filters import Filtered

KEPT = ("keep", "review-keep", "pending")


def window(flt: Filtered, top_n: int) -> list[junk.Routed]:
    """The routed lemmas up to the one that fills the ``top_n``-th kept place."""
    out: list[junk.Routed] = []
    kept = 0
    for r in flt.routed:
        out.append(r)
        kept += r.action in KEPT
        if kept >= top_n:
            break
    return out


def header_entry(manifest: Manifest, flt: Filtered, top_n: int, repo_root: Path) -> dict[str, Any]:
    jc = manifest.language.junk
    win = window(flt, top_n)
    return {
        "rules": list(jc.rules), "accent_ratio": jc.accent_ratio,
        "review": None if flt.review is None else {
            "file": str(flt.review.path.relative_to(repo_root)) if flt.review.path.is_relative_to(repo_root)
            else str(flt.review.path), "sha256": flt.review.sha256, "decisions": len(flt.review.decisions)},
        "merges": len(flt.merges),
        "actions_in_top_n": dict(Counter(r.action for r in win)),
        "hits_in_top_n": {rule: sum(1 for r in win if any(x == rule for x, _ in r.flags)) for rule in junk.RULES},
        "routing": "2+ flags dropped; 1 flag within review_top reviewed (corpora/review/<code>.tsv); proper nouns "
                   "capitalised in >= propn_drop of running text dropped alone; accent merges applied to the counts",
    }


def _fmt_flags(r: junk.Routed) -> str:
    return "; ".join(f"{rule}: {ev}" for rule, ev in r.flags)


def render(manifest: Manifest, flt: Filtered, top_n: int, sample: int = 50, seed: int = 20261101) -> list[str]:
    jc = manifest.language.junk
    flags = flt.flags or junk.Flags()
    win = window(flt, top_n)
    acts = Counter(r.action for r in win)
    lemmas = [r.lemma for r in win]
    ov = junk.overlap(flags, lemmas)
    out = ["## Junk-filter heuristics", "",
           f"Rules on: {', '.join(jc.rules) or 'none'}; accent merges at ratio {jc.accent_ratio}. Window: the "
           f"{len(win):,} ranked lemmas (after the exclusion list) that fill the top {top_n:,}. Actions: "
           + ", ".join(f"{k} {v:,}" for k, v in sorted(acts.items())) + ".", "",
           "### Hits and overlap (window)", "",
           "Diagonal: lemmas the rule flags; off-diagonal: lemmas both rules flag.", "",
           "| | " + " | ".join(junk.RULES) + " |", "|---|" + "---:|" * len(junk.RULES)]
    out += [f"| {a} | " + " | ".join(f"{ov[a][b]:,}" for b in junk.RULES) + " |" for a in junk.RULES]
    out += ["", f"Proper nouns dropped alone (capitalised in >= {jc.propn_drop:.0%} of running text): "
            f"{sum(1 for r in win if r.action == 'propn-drop'):,}.", ""]
    if flags.diversity_bands:
        hits = [r for r in win if any(x == "diversity" for x, _ in r.flags)]
        out += ["### Low diversity", "",
                f"Documents reached / documents expected at random, below {jc.diversity_max_clumping} "
                f"(frequency >= {jc.diversity_min_freq}): {len(hits):,} in the window. For comparison, each "
                "log2-frequency band's 2nd percentile: " + ", ".join(f"{b}: {t}" for b, t in sorted(
                    flags.diversity_bands.items(), key=lambda kv: int(kv[0].split("-")[0]))) + ".", "",
                "Examples: " + ", ".join(f"`{r.lemma}` ({r.rank})" for r in hits[:40]), ""]
    out += [f"### Accent merges ({len(flt.merges):,})", "",
            "| from | into | frequency moved | evidence |", "|---|---|---:|---|"]
    out += [f"| `{m.source}` | `{m.target}` | {m.source_freq:,} | {m.evidence} |" for m in flt.merges]
    drops = [r for r in win if r.action == "drop"]
    pick = random.Random(seed).sample(drops, min(sample, len(drops)))
    out += ["", f"### Dropped by 2+ flags: random sample of {len(pick)} of {len(drops):,} in the window", "",
            "| rank | lemma | flags |", "|---:|---|---|"]
    out += [f"| {r.rank} | `{r.lemma}` | {_fmt_flags(r)} |" for r in sorted(pick, key=lambda r: r.rank)]
    pending = [r for r in win if r.action == "pending"]
    out += ["", f"### Single flag, not yet reviewed: {len(pending):,} (kept until reviewed)", ""]
    if pending:
        out += ["| rank | lemma | flag |", "|---:|---|---|"]
        out += [f"| {r.rank} | `{r.lemma}` | {_fmt_flags(r)} |" for r in pending[:100]]
        if len(pending) > 100:
            out.append(f"\n_{len(pending) - 100:,} more in the flags sidecar._")
    reviewed = [r for r in win if r.action in ("review-keep", "review-drop")]
    out += ["", f"Reviewed decisions applied in the window: {len(reviewed):,} "
            f"(keep {sum(r.action == 'review-keep' for r in reviewed):,}, "
            f"drop {sum(r.action == 'review-drop' for r in reviewed):,}); review merges: "
            f"{sum(1 for m in flt.merges if m.evidence.startswith('review')):,}.", ""]
    return out


def write_flags(path: Path, flt: Filtered) -> None:
    """Every flagged or dropped lemma with its action and evidence, then every merge."""
    with path.open("w", encoding="utf-8") as fp:
        fp.write("# rank\tlemma\taction\tflags (rule: evidence; ...)\n")
        for r in flt.routed:
            if r.flags or r.action != "keep":
                ev = _fmt_flags(r) or (flt.flags.propn_drop.get(r.lemma, "") if flt.flags else "")
                fp.write(f"{r.rank}\t{r.lemma}\t{r.action}\t{ev}\n")
        for m in flt.merges:
            fp.write(f"-\t{m.source}\tmerged-into:{m.target}\t{m.evidence}\n")
