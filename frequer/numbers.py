"""The standing number rule: Honeyeater's ``lexicon.number_words.number_is_learnable`` decides number lemmas.

The function belongs to a Honeyeater checkout that may be newer than the pinned runtime (``FREQUER_REFERENCE_ROOT``),
so it runs in a subprocess with that checkout's ``backend/`` on the path: two versions of ``lexicon`` cannot share
one interpreter. ``True`` keeps (the curated number vocabulary), ``False`` drops (any other spelled number or
figure), ``None`` (not a number) leaves the lemma to the other rules.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

_SCRIPT = """
import json, sys
import django
django.setup()
from lexicon.number_words import number_is_learnable
lang = sys.argv[1]
lemmas = json.load(sys.stdin)
print("\\n" + json.dumps({t: number_is_learnable(t.split("#")[0], lang) for t in lemmas}))
"""


def verdicts(lemmas: Sequence[str], lang: str, honeyeater_root: Path) -> dict[str, bool | None]:
    env = {**os.environ, "PYTHONPATH": str(honeyeater_root / "backend"),
           "DJANGO_SETTINGS_MODULE": "config.settings.test"}
    proc = subprocess.run([sys.executable, "-c", _SCRIPT, lang], input=json.dumps(list(lemmas)), env=env,
                          capture_output=True, text=True, cwd=honeyeater_root / "backend")
    if proc.returncode:
        raise SystemExit(f"number rule failed in {honeyeater_root}:\n{proc.stderr[-2000:]}")
    out: dict[str, bool | None] = json.loads(proc.stdout.rstrip("\n").rsplit("\n", 1)[-1])
    return out
