"""Shared configuration and file plumbing for the review scripts (README.md). Copies, merges and checks only:
every decision comes from a reviewer, the adjudicator or the developer.

One JSON config per language run, e.g. (paths are examples):

{"lang": "ja", "language_name": "Japanese", "work": "/scratch/jarev", "counts": "/data/ja/counts",
 "honeyeater": "/checkouts/he-pinned", "reference": "/checkouts/he-reference",
 "lemma_dir": "/site/honeyeater_lemma_ja", "wheel": "/wheels/honeyeater_lemma_ja-1.5.0-py3-none-any.whl",
 "window": 30000, "join": "", "sample": {"hplt-v2-ja": {"urls": [2, 6, 11, 16, 19], "max_chars": 25000000}},
 "rules": "prompts/ja/rules-flagged.md", "screener": "prompts/ja/screener.md",
 "reviewer_model": "sonnet", "adjudicator_model": "opus", "parallel": 6}

Relative prompt paths resolve against this directory. Models are ``claude`` CLI aliases (the cheaper tier for
screeners and reviewers, the stronger tier for adjudication).
"""

from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
PROMPTS = HERE / "prompts"
#: Every decision a reviewer may give (``merge`` stands for ``merge:<lemma>``); a round can narrow it (the
#: institutions review allows keep and drop only).
DECISIONS = ("keep", "drop", "pending-names", "merge")
#: The columns of a review queue (``examples.py`` writes it; ``review.py`` reads it).
QUEUE_COLUMNS = ("rank", "lemma", "freq", "pos", "forms", "flags", "action", "examples")
#: routed.tsv's columns (``route.py``).
ROUTED_COLUMNS = ("rank", "lemma", "action", "freq", "pos", "forms", "flags", "kept")
#: Actions that keep a lemma on the list.
KEPT = ("keep", "review-keep", "pending", "pending-names")


def load(path: str | Path) -> dict[str, Any]:
    cfg: dict[str, Any] = json.loads(Path(path).read_text(encoding="utf-8"))
    cfg.setdefault("window", 30000)
    cfg.setdefault("reviewer_model", "sonnet")
    cfg.setdefault("adjudicator_model", "opus")
    cfg.setdefault("parallel", 6)
    cfg.setdefault("language_name", cfg["lang"])
    cfg["work"] = Path(cfg["work"])
    for key in ("rules", "screener", "rules_unflagged", "institutions_screen", "institutions_review"):
        if key in cfg:
            cfg[key] = str(prompt_path(cfg[key]))
    (cfg["work"] / "cwd").mkdir(parents=True, exist_ok=True)  # an empty working directory for claude -p
    return cfg


def prompt_path(name: str | Path) -> Path:
    p = Path(name)
    return p if p.is_absolute() else HERE / p


def fill(template: str, values: Mapping[str, Any]) -> str:
    """``{name}`` placeholders in a prompt file; unknown placeholders are an error (a typo would go unseen)."""
    try:
        return template.format_map(dict(values))
    except KeyError as e:
        raise SystemExit(f"prompt placeholder {e} has no value") from e


def claude(cfg: dict[str, Any], model: str, prompt: str, path: Path, system: str | None = None) -> str:
    """One headless ``claude -p`` call, no tools, cached in ``path`` (a rerun skips finished calls).

    Run from an empty directory with no MCP servers and no tools, so a reviewer sees only the prompt. The
    calling session must be allowed to run ``claude`` without a prompt (PLAYBOOK §Sessions).
    """
    if path.exists() and path.stat().st_size:
        return path.read_text(encoding="utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", "--model", model, "--tools", "", "--strict-mcp-config", "--no-session-persistence"]
    if system:
        cmd += ["--system-prompt", system]
    err = ""
    for _ in range(3):
        out = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=cfg["work"] / "cwd",
                             timeout=1800)
        if out.returncode == 0 and out.stdout.strip():
            path.write_text(out.stdout, encoding="utf-8")
            return out.stdout
        err = out.stderr
    print(f"{path}: failed: {err[-300:]}", file=sys.stderr)
    return ""


# -- TSV files ----------------------------------------------------------------


def clean(text: Any) -> str:
    return str(text).replace("\t", " ").replace("\n", " ")


def read_tsv(path: Path, columns: Iterable[str]) -> list[dict[str, str]]:
    """Rows of a headed TSV (``#`` lines skipped), as dicts over ``columns`` (missing trailing fields: "")."""
    cols = tuple(columns)
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        f = line.split("\t")
        out.append({c: (f[i] if i < len(f) else "") for i, c in enumerate(cols)})
    return out


def write_tsv(path: Path, columns: Iterable[str], rows: Iterable[Mapping[str, Any]]) -> int:
    cols = tuple(columns)
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8") as fp:
        fp.write("# " + "\t".join(cols) + "\n")
        for r in rows:
            fp.write("\t".join(clean(r.get(c, "")) for c in cols) + "\n")
            n += 1
    return n


def routed_rows(cfg: dict[str, Any]) -> list[list[str]]:
    """``routed.tsv``: rank, lemma, action, freq, pos, forms (JSON), flags, kept position."""
    return [line.rstrip("\n").split("\t") for line in open(cfg["work"] / "routed.tsv", encoding="utf-8")
            if not line.startswith("#")]


def read_queue(path: Path) -> list[dict[str, Any]]:
    """A review queue: TSV (``QUEUE_COLUMNS``; forms as JSON, examples joined by `` || ``) or legacy JSONL."""
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in open(path, encoding="utf-8")]
    out = []
    for r in read_tsv(path, QUEUE_COLUMNS):
        out.append({"rank": int(r["rank"] or 0), "lemma": r["lemma"], "freq": int(r["freq"] or 0), "pos": r["pos"],
                    "forms": json.loads(r["forms"]) if r["forms"] else {}, "flags": r["flags"],
                    "action": r["action"], "examples": [e for e in r["examples"].split(" || ") if e]})
    return out


def write_queue(path: Path, queue: Iterable[Mapping[str, Any]]) -> int:
    return write_tsv(path, QUEUE_COLUMNS, (
        {**q, "forms": json.dumps(q.get("forms", {}), ensure_ascii=False),
         "examples": " || ".join(clean(e) for e in q.get("examples", []))} for q in queue))


# -- decisions ------------------------------------------------------------------


def valid_decision(d: str, allowed: Iterable[str] = DECISIONS) -> bool:
    """One of ``allowed``, where ``merge`` admits ``merge:<lemma>`` (a target with no tab)."""
    allowed = tuple(allowed)
    if d.startswith("merge:"):
        return "merge" in allowed and len(d) > 6 and "\t" not in d
    return d != "merge" and d in allowed


def parse_answer(text: str, lemmas: set[str], allowed: Iterable[str] = DECISIONS
                 ) -> tuple[dict[str, tuple[str, str]], list[str]]:
    """A reviewer's answer: ``lemma<TAB>decision<TAB>reason`` lines for known lemmas, and ``# question`` lines.

    Anything else (a preamble, a table, an unknown lemma, an invalid decision) is ignored, so a lemma the answer
    mangles counts as missing and is asked again.
    """
    got: dict[str, tuple[str, str]] = {}
    questions: list[str] = []
    allowed = tuple(allowed)
    for raw in text.splitlines():
        line = raw.strip().strip("`")
        if line.startswith("# question"):
            questions.append(line)
            continue
        parts = line.split("\t")
        if len(parts) >= 2 and parts[0].strip() in lemmas and valid_decision(parts[1].strip(), allowed):
            got[parts[0].strip()] = (parts[1].strip(), parts[2].strip() if len(parts) > 2 else "")
    return got, questions


def agree(order: Iterable[str], a: Mapping[str, tuple[str, str]], b: Mapping[str, tuple[str, str]]
          ) -> tuple[dict[str, tuple[str, str]], list[str]]:
    """Agreed decisions (same decision, same merge target) and the lemmas for the adjudicator, in order."""
    agreed: dict[str, tuple[str, str]] = {}
    dis: list[str] = []
    for k in order:
        if k in a and k in b and a[k][0] == b[k][0]:
            agreed[k] = a[k]
        else:
            dis.append(k)
    return agreed, dis


def accent_only_merges(agreed: Mapping[str, tuple[str, str]]) -> list[str]:
    """Agreed merges whose source and target differ only by diacritics or case: the ones that can hide a second
    real word (es *comisaria* / *comisaría*, *secretaria* / *secretaría*). The coordinator reads these before
    adjudication (README §Sanity pass); this only lists them."""
    import unicodedata

    def plain(s: str) -> str:
        return "".join(c for c in unicodedata.normalize("NFD", s.casefold()) if unicodedata.category(c) != "Mn")

    return [k for k, (d, _r) in agreed.items() if d.startswith("merge:") and plain(d[6:]) == plain(k)]


def read_review_file(path: Path) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                f = line.split("\t")
                out[f[0]] = (f[1].strip() if len(f) > 1 else "", f[2].strip() if len(f) > 2 else "")
    return out


def apply_round(review_file: str, decided: Iterable[tuple[str, str, str]], label: str, redecide: bool
                ) -> tuple[str, Counter[str]]:
    """``review_file`` (the text of ``corpora/review/<lang>.tsv``) with one round's decisions applied.

    Append-only by default: a lemma that already has a line keeps it (an earlier decision stands; the round's
    differing decision is counted as ``conflict`` so the orchestrator sees it). With ``redecide`` (a round run
    under a new developer ruling) the line is replaced in place and the old decision kept in the reason.
    """
    lines = review_file.splitlines()
    where = {line.split("\t")[0]: i for i, line in enumerate(lines) if line.strip() and not line.startswith("#")}
    stats: Counter[str] = Counter()
    new: list[str] = []
    for lemma, decision, reason in decided:
        if not decision:
            raise SystemExit(f"{lemma}: undecided; finish the round (review.py --adjudicate) before applying it")
        row = f"{lemma}\t{decision}\t{clean(reason)}"
        if lemma in where:
            old = lines[where[lemma]].split("\t")
            if old[1].strip() == decision:
                stats["unchanged"] += 1
            elif redecide:
                lines[where[lemma]] = f"{row} (was {old[1].strip()}: {old[2].strip() if len(old) > 2 else ''})"
                stats["redecided"] += 1
            else:
                stats["conflict"] += 1
        else:
            new.append(row)
            where[lemma] = -1
            stats["added"] += 1
    if new:
        lines += [f"# {label}", *new]
    return "\n".join(lines) + "\n", stats


def learnable_names(cfg: Mapping[str, Any]) -> frozenset[str]:
    """The reference checkout's learnable-names list, case-folded (empty until it exists)."""
    path = Path(cfg.get("reference", cfg.get("honeyeater", "."))) / "reference" / "learnable-names" / \
        f"{cfg['lang']}.json"
    if not path.exists():
        return frozenset()
    return frozenset(n.casefold() for n in json.loads(path.read_text(encoding="utf-8"))["names"])


def release_entry(lemma: str, names: frozenset[str]) -> str | None:
    """Why a lemma is the release's own entry and not a screening candidate (es triage union), or None:
    a unit (multi-token key), a homograph key (``#``), or a learnable name."""
    if " " in lemma or "+" in lemma:
        return "unit"
    if "#" in lemma:
        return "homograph key"
    if lemma.casefold() in names:
        return "learnable name"
    return None
