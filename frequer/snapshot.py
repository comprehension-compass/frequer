"""Write the Honeyeater snapshot and its dispersion sidecar.

The snapshot keeps the schema ``reference/lemmas/<lang>.json`` already has
(``{source, corpus, pos_tagger, top_n, lemmas}``; each entry carries
``frequency``, ``log10_rate_per_billion``, ``pos``, the top folded ``forms`` and,
for Japanese, ``reading`` / ``reading_source``) plus header keys that record how
it was built. The loader ignores unknown header keys. Entry order is rank order.
Dispersion statistics live in the sidecar, never in the snapshot.
"""

from __future__ import annotations

import gzip
import json
import math
import subprocess
from collections import Counter
from collections.abc import Callable
from datetime import date
from pathlib import Path
from typing import Any

from frequer import __version__
from frequer.config import REPO_ROOT, Manifest
from frequer.counts import Merged
from frequer.merge import MergeResult
from frequer.ranking import SCORES, Row

#: ``citation(lemma, proper=..., forms=..., reading=...)`` -> object with ``.reading`` / ``.source``.
Citation = Callable[..., Any]
DEFAULT_SOURCE = "dictionary"


def frequer_commit() -> str:
    out = subprocess.run(["git", "-C", str(REPO_ROOT), "rev-parse", "HEAD"], capture_output=True, text=True)
    return out.stdout.strip() or "unknown"


def majority(counter: Counter[str], default: str = "") -> str:
    """Most common key; ties go to the alphabetically first so builds are stable."""
    if not counter:
        return default
    return min(counter.items(), key=lambda kv: (-kv[1], kv[0]))[0]


def top_forms(forms: Counter[str], n: int) -> dict[str, int]:
    return dict(sorted(forms.items(), key=lambda kv: (-kv[1], kv[0]))[:n])


def reading_for(row: Row, forms: dict[str, int], pos: str, citation: Citation) -> tuple[str, str]:
    """The lemma's hiragana reading and its source, derived as ``build_ja_snapshot.py`` does.

    The commonest reading the backend's candidate carried for a token whose lemma
    it agreed with; otherwise (a lemma only the model produced) the backend's
    own citation selector asked about the lemma itself.
    """
    stats = row.stats
    if stats.readings:
        reading = majority(stats.readings)
        return reading, stats.reading_source.get(reading, DEFAULT_SOURCE)
    cited = citation(row.lemma, proper=pos == "PROPN", forms=list(forms), reading="")
    return str(cited.reading), str(getattr(cited.source, "value", cited.source))


#: Occurrence kinds a snapshot entry names as ``unit`` (a one-token compound is a plain word entry).
UNIT_KINDS = ("compound", "phrase", "construction")


def unit_kind(kinds: Counter[str]) -> str:
    """The entry's unit type: its majority occurrence kind, where that is a unit."""
    kind = majority(kinds)
    return kind if kind in UNIT_KINDS else ""


def build_entries(
    ranked: list[Row], merged: Merged, manifest: Manifest, citation: Citation | None
) -> dict[str, dict[str, Any]]:
    cfg = manifest.language
    entries: dict[str, dict[str, Any]] = {}
    for row in ranked[: cfg.top_n]:
        stats = row.stats
        forms = top_forms(stats.forms, cfg.forms_kept)
        pos = majority(stats.pos, "X")
        entry: dict[str, Any] = {
            "frequency": stats.freq,
            "log10_rate_per_billion": round(math.log10(stats.freq * 1e9 / merged.tokens), 4),
            "pos": pos,
            "forms": forms,
        }
        kind = unit_kind(stats.kinds)
        if kind:
            entry["unit"] = kind
        if cfg.readings:
            assert citation is not None
            reading, source = reading_for(row, forms, pos, citation)
            entry["reading"] = reading
            if source != DEFAULT_SOURCE:
                entry["reading_source"] = source
        entries[row.lemma] = entry
    return entries


def header(result: MergeResult, manifest: Manifest, score: str, weights: dict[str, float], scope: str) -> dict[str, Any]:
    rt = result.runtime
    pos_tagger = (
        f"{rt['lemma_package']} {rt['lemma_version']} UPOS on every token, as the sentence stage "
        "assigns it (per-lemma majority; a multi-token unit is X)"
    )
    return {
        "source": (
            f"honeyeater-frequer {frequer_commit()[:12]} ({scope}): production {rt['tokenizer']} "
            f"backend through nlp.sentence_stage.analyse_sentence with {rt['lemma_package']} "
            f"{rt['lemma_version']} (fallback {rt['fallback']}, units {'on' if rt['units'] else 'off'})"
        ),
        "corpus": " + ".join(result.sources),
        "pos_tagger": pos_tagger,
        "built": date.today().isoformat(),
        "lemma_release": {
            "package": rt["lemma_package"], "version": rt["lemma_version"],
            "sha256": rt["lemma_sha256"], "wheel_sha256": rt["wheel_sha256"], "theta": rt["theta"],
        },
        "honeyeater": {"commit": rt["honeyeater_commit"], "dirty": rt["honeyeater_dirty"]},
        "overrides": (
            f"none applied to lemmas (a release language keeps only the desk's database rows, not "
            f"available offline); {rt['overrides_path']} sha256:{rt['overrides_sha256']} feeds the "
            f"backend fallback only"
        ),
        "units": {
            "counted": "a compound replaces its member words (a compound is a word); a phrase or "
                       "construction counts next to its member words",
            "entry_field": "unit (compound, phrase, construction) on multi-token unit entries",
        },
        "corpus_manifest": [
            {
                "name": name, "licence": manifest.source(name).licence, "urls": manifest.source(name).urls,
                "tokens": t.tokens, "documents": t.docs, "shards": t.shards, "lines": t.lines,
                "weight": weights.get(name, 1.0), "scope": scope,
            }
            for name, t in result.sources.items()
        ],
        "tokens": result.merged.tokens,
        "documents": result.merged.docs,
        "ranking": {"score": score, "source_weights": weights, "parts": manifest.parts},
        "frequer": {"version": __version__, "commit": frequer_commit()},
    }


def write_snapshot(path: Path, head: dict[str, Any], entries: dict[str, dict[str, Any]]) -> None:
    out = {**head, "top_n": len(entries), "lemmas": entries}
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fp:
        json.dump(out, fp, ensure_ascii=False, separators=(",", ":"))


def write_sidecar(path: Path, head: dict[str, Any], ranked: list[Row], merged: Merged, top_n: int) -> None:
    """Per-lemma dispersion statistics for the ranked lemmas, gzip JSON."""

    def num(x: float) -> float | None:
        return None if math.isnan(x) else round(x, 6)

    rows = [
        {
            "rank": i, "lemma": r.lemma, "frequency": r.stats.freq, "document_frequency": r.stats.df,
            "by_source": dict(r.stats.by_source), "parts_present": len(r.stats.parts),
            "dp": num(r.dp), "dp_norm": num(r.dp_norm), "juilland_d": num(r.juilland_d),
            "juilland_d_corrected": num(r.juilland_d_corrected),
            "scores": {name: round(r.scores[name], 4) for name in SCORES},
        }
        for i, r in enumerate(ranked[:top_n], start=1)
    ]
    body = {
        "header": head, "parts": merged.parts, "part_tokens": merged.part_tokens,
        "documents": merged.docs, "units": merged.units, "rows": rows,
    }
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=6) as fp:
        json.dump(body, fp, ensure_ascii=False, separators=(",", ":"))
