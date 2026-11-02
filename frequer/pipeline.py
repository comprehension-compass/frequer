"""``frequer pipeline <lang>``: where a language's list build stands, stage by stage, and what to check next.

Read-only. It looks at the files each stage leaves behind, marks each stage ``done``, ``next`` or ``waiting``,
and for the next stage prints the command to run, what the orchestrating agent must look at before moving on,
and when to stop and ask the developer. It runs nothing and decides nothing: the counting, building and file
plumbing are commands; every judgement (reviews, audits, the cutoff, place names, rulings) stays with the
agents and the developer (docs/PLAYBOOK.md, one section per stage).

The one check it makes itself is the licence rule: every source in the manifest must be public domain, CC0 or
CC BY (no SA, NC or ND), or the first stage fails.
"""

from __future__ import annotations

import json
import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from frequer.config import Manifest

#: Public domain, CC0 or CC BY (any version, any port); never SA, NC or ND (docs/DECISIONS.md, corpus licences).
LICENCE_OK = re.compile(r"^(public-domain|CC0-\d+(\.\d+)?|CC-BY-\d+(\.\d+)?(-[A-Z]{2})?)$")


def licence_ok(licence: str) -> bool:
    return bool(LICENCE_OK.match(licence.strip()))


@dataclass(frozen=True)
class Paths:
    lang: str
    data: Path  # --data-dir/<lang>
    out: Path  # build output (out/<lang>)
    review: Path | None  # the review work directory (scripts/review config "work"), if one exists
    review_file: Path  # corpora/review/<lang>.tsv


@dataclass(frozen=True)
class Stage:
    key: str
    title: str
    done: Callable[[Manifest, Paths], bool]
    command: str
    look_at: str
    ask_when: str
    playbook: str


def _json(path: Path) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _pending(p: Paths) -> int | None:
    """Unreviewed ``pending`` lemmas in routed.tsv (None: not routed yet)."""
    if p.review is None or not (p.review / "routed.tsv").exists():
        return None
    with open(p.review / "routed.tsv", encoding="utf-8") as fp:
        return sum(1 for line in fp if not line.startswith("#") and line.rstrip("\n").split("\t")[2] == "pending")


def _rounds(p: Paths, prefix: str = "") -> list[Path]:
    if p.review is None:
        return []
    return [d for d in (p.review / "review").glob(f"{prefix}*") if (d / "decisions.tsv").exists()]


STAGES: tuple[Stage, ...] = (
    Stage("manifest", "Manifest: sources, licences, hygiene, stride",
          lambda m, p: all(licence_ok(s.licence) for s in m.sources),
          "edit corpora/<lang>.yaml; frequer pilot <lang>",
          "every source public domain / CC0 / CC BY; Tatoeba first (first: true); a stride over the whole web file; "
          "the pilot report's characters per token and junk samples",
          "a source's licence is unclear, or the corpus needs a new kind of source", "§1 Corpus and manifest"),
    Stage("count", "Count through the runtime, with convergence checkpoints",
          lambda m, p: (p.data / "counts").is_dir() and any((p.data / "counts").glob("*.tsv*")),
          "frequer count <lang> --checkpoints [--part i/N] (distributed: scripts/remote-part.sh + frequer coordinate)",
          "the shard headers' lemma release and Honeyeater commit; per-shard throughput (perf.json); that the "
          "coordinator and every part are still alive after any container restart",
          "throughput or token counts are far off the pilot's, or the stamped release is not the one you pinned",
          "§2 Counting"),
    Stage("converge", "Convergence: 3 full-mix checkpoints within the thresholds",
          lambda m, p: _json(p.out / "convergence.json").get("decision") == "stop",
          "frequer checkpoint <lang> (the coordinator takes them as shards arrive)",
          "convergence.md: split-half distance at 20k (<=5%) and 50k (<=10%) on the filtered list, three in a row; "
          "the calibration table against the final list (a crawl-grouping floor)",
          "the distance plateaus above the threshold (a floor) or the corpus runs out first", "§3 Convergence"),
    Stage("build", "First build: snapshot, sidecar, report, flags",
          lambda m, p: (p.out / "report.md").exists() and (p.out / f"{p.lang}.flags.tsv").exists(),
          "frequer build <lang> --reference-root <honeyeater checkout>",
          "report.md: rule hits, the rule-overlap matrix, the diversity calibration, 50 samples per flag; "
          "load_lemmas --dry-run reports 0 skipped",
          "a rule flags far more than expected (validate it on a sample before it acts), or a new class of junk",
          "§4 Junk heuristics"),
    Stage("route", "Route: flags and actions for the review window",
          lambda m, p: _pending(p) is not None,
          "python scripts/review/route.py <config.json>",
          "the action counts in the window; read 20 lemmas of each action", "a drop action you cannot explain",
          "§5 Review"),
    Stage("flagged", "Flagged review rounds until nothing is pending",
          lambda m, p: _pending(p) == 0 and bool(_rounds(p, "round")),
          "examples.py -> review.py (stage 1) -> read agreed.tsv, accent-merges.txt -> review.py --adjudicate "
          "-> collect.py -> route.py; repeat",
          "agreement rate, a sample of agreed drops, every merge, the examples share, the questions",
          "always send the `# question` lines; stop on a new class of question", "§5 Review"),
    Stage("triage", "Triage of unflagged keeps, then the full protocol on suspects",
          lambda m, p: bool(_rounds(p, "triage")) or bool(_rounds(p, "unflagged")),
          "screen.py <config> triage -> examples.py --only-file --notes -> review.py --rules <unflagged rules>",
          "the suspect rate per band; read 30 suspects and 30 non-suspects", "the screeners miss a class of junk",
          "§6 Triage"),
    Stage("audit", "Spot audit and the per-band report",
          lambda m, p: p.review is not None and (p.review / "band-samples.md").exists() and bool(_rounds(p, "audit")),
          "audit.py -> examples.py --only-file -> review.py audit-<name> (+ --adjudicate) -> report.py; "
          "band_samples.py --compare <other configs> --gloss",
          "band-samples.md: words per band, just above the cut, what a deeper cut adds, across languages; "
          "band-report.md: audit estimates, drops, merges, questions",
          "always: the developer picks the cutoff from this report", "§7 Band report and cutoff"),
    Stage("cutoff", "Cutoff chosen by the developer, recorded in the manifest",
          lambda m, p: bool(m.language.cutoff),
          "set language.top_n and language.cutoff (the ruling: date, where recorded) in corpora/<lang>.yaml",
          "that top_n matches the ruling", "always (the developer's decision)", "§7 Band report and cutoff"),
    Stage("names", "Place names from the final learnable-names list",
          lambda m, p: m.language.junk.names_final and m.language.append_learnable_names,
          "names_final: true and append_learnable_names: true; route.py; build --reference-root <checkout with the list>",
          "pending-names resolved (kept if listed, dropped otherwise); the header's appended names count",
          "the list is not final yet (build an interim list with --leave-out-pending-names)", "§8 Place names"),
    Stage("snapshot", "Final snapshot and load dry run",
          lambda m, p: (p.out / f"{p.lang}.json").exists(),
          "frequer build <lang> --reference-root ...; manage.py load_lemmas <lang> --path out/<lang>/<lang>.json --dry-run",
          "0 skipped; entries = top_n + appended names; the header's review, exclusion and names hashes",
          "any skipped lemma; then hand over to Honeyeater (docs/runbook/language-pipeline.md)", "§9 Snapshot"),
)


def evaluate(manifest: Manifest, paths: Paths) -> list[tuple[Stage, str]]:
    """Each stage with ``done``, ``next`` (the first not done) or ``waiting``."""
    out: list[tuple[Stage, str]] = []
    nxt = False
    for stage in STAGES:
        ok = stage.done(manifest, paths)
        if ok and not nxt:
            out.append((stage, "done"))
        elif not nxt:
            out.append((stage, "next"))
            nxt = True
        else:
            out.append((stage, "done" if ok else "waiting"))
    return out


def render(manifest: Manifest, paths: Paths) -> str:
    bad = [f"{s.name}: {s.licence}" for s in manifest.sources if not licence_ok(s.licence)]
    lines = [f"frequer pipeline {paths.lang} (read-only; docs/PLAYBOOK.md)", ""]
    if bad:
        lines += ["LICENCE RULE: these sources are not public domain, CC0 or CC BY: " + "; ".join(bad), ""]
    pending = _pending(paths)
    for stage, status in evaluate(manifest, paths):
        mark = {"done": "[x]", "next": "[>]", "waiting": "[ ]"}[status]
        lines.append(f"{mark} {stage.title}  (PLAYBOOK {stage.playbook})")
        if status == "next":
            lines += [f"      run:      {stage.command}", f"      look at:  {stage.look_at}",
                      f"      ask the developer when: {stage.ask_when}"]
    if pending:
        lines += ["", f"{pending:,} lemmas are pending review in routed.tsv."]
    lines += ["", "A stage marked done only means its files exist: the orchestrator still reads its outputs "
                  "before moving on."]
    return "\n".join(lines)
