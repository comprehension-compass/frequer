"""Shared configuration for the review scripts (README.md). One JSON file per language run, e.g.:

{"lang": "ja", "work": "/scratch/jarev", "counts": "/data/ja/counts",
 "honeyeater": "/checkouts/he-pinned", "reference": "/checkouts/he-reference",
 "lemma_dir": "/site/honeyeater_lemma_ja", "wheel": "/wheels/honeyeater_lemma_ja-1.5.0-py3-none-any.whl",
 "window": 30000, "join": "", "sample": {"hplt-v2-ja": {"urls": [2, 6, 11, 16, 19], "max_chars": 25000000}},
 "rules": "prompts/rules-ja.md", "screener": "prompts/screener-ja.md",
 "reviewer_model": "claude-sonnet-5", "adjudicator_model": "claude-opus-5", "parallel": 6}
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent


def load(path: str) -> dict[str, Any]:
    cfg: dict[str, Any] = json.loads(Path(path).read_text(encoding="utf-8"))
    cfg.setdefault("window", 30000)
    cfg.setdefault("reviewer_model", "claude-sonnet-5")
    cfg.setdefault("adjudicator_model", "claude-opus-5")
    cfg.setdefault("parallel", 6)
    cfg["work"] = Path(cfg["work"])
    for key in ("rules", "screener"):
        if key in cfg and not Path(cfg[key]).is_absolute():
            cfg[key] = str(HERE / cfg[key])
    (cfg["work"] / "cwd").mkdir(parents=True, exist_ok=True)  # an empty working directory for claude -p
    return cfg


def claude(cfg: dict[str, Any], model: str, prompt: str, path: Path, system: str | None = None) -> str:
    """One headless ``claude -p`` call, no tools, cached in ``path`` (a rerun skips finished calls)."""
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


def routed_rows(cfg: dict[str, Any]) -> list[list[str]]:
    """``routed.tsv``: rank, lemma, action, freq, pos, forms (JSON), flags, kept position."""
    return [line.rstrip("\n").split("\t") for line in open(cfg["work"] / "routed.tsv", encoding="utf-8")
            if not line.startswith("#")]
