"""The app's number check, for the number rule (``JunkConfig.number_rule``).

frequer has no number definition of its own. It asks the Honeyeater checkout that holds the app's reference
data (the build's ``--reference-root``, by default the pinned runtime checkout) to classify every candidate
lemma, in one subprocess inside that checkout's ``backend``: ``lexicon.number_words.number_is_learnable(text,
language_code)`` where the checkout has it (Honeyeater PR #766), else the private helpers it replaced
(``lexicon.lemma_defaults._number_is_learnable`` plus the number-words list). ``True``: a learnable number;
``False``: a number the app ignores (dropped); ``None`` (absent from the result): not a number, so the list
decides (base words, counters and date forms: 百, 一つ, 二十日). A subprocess, because the reference checkout
can be newer than the pinned runtime the counts were made with.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from pathlib import Path

_SCRIPT = r"""
import json, logging, os, sys
logging.disable(logging.WARNING)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test")
import django
django.setup()
code, src, dst = sys.argv[1], sys.argv[2], sys.argv[3]
try:
    from lexicon.number_words import number_is_learnable
    def check(text):
        return number_is_learnable(text, code)
    how = "lexicon.number_words.number_is_learnable"
except ImportError:
    import lexicon.lemma_defaults as ld
    from lexicon.number_words import number_words
    words = number_words(code)
    def check(text):
        return True if text in words else ld._number_is_learnable(text)
    how = "lexicon.lemma_defaults._number_is_learnable"
out = {}
for text in json.load(open(src, encoding="utf-8")):
    verdict = check(text)
    if verdict is not None:
        out[text] = verdict
json.dump({"how": how, "verdicts": out}, open(dst, "w", encoding="utf-8"), ensure_ascii=False)
"""


def app_number_verdicts(texts: Iterable[str], code: str, root: Path) -> tuple[dict[str, bool], str]:
    """``{text: learnable}`` for every text the app calls a number, and which function decided."""
    backend = root / "backend"
    with tempfile.TemporaryDirectory() as tmp:
        src, dst = Path(tmp) / "in.json", Path(tmp) / "out.json"
        src.write_text(json.dumps(sorted(set(texts)), ensure_ascii=False), encoding="utf-8")
        env = {**os.environ, "PYTHONPATH": str(backend)}
        done = subprocess.run([sys.executable, "-c", _SCRIPT, code, str(src), str(dst)], cwd=backend, env=env,
                              capture_output=True, text=True)
        if done.returncode != 0:
            raise SystemExit(f"the app's number check failed in {backend}: {done.stderr[-2000:]}")
        body = json.loads(dst.read_text(encoding="utf-8"))
    return {k: bool(v) for k, v in body["verdicts"].items()}, str(body["how"])
