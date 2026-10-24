"""honeyeater-frequer: top-N lemma frequency snapshots, counted through the runtime.

Run with the Honeyeater backend's interpreter from ``backend/`` with
``PYTHONPATH=.``. Dependencies the backend venv lacks (``zstandard``,
optionally ``wordfreq``) can live in a separate directory named by
``FREQUER_DEPS``; it is *appended* to ``sys.path`` so it can never shadow a
package the backend pins.
"""

from __future__ import annotations

import os
import sys

__version__ = "0.1.0"

for _dir in filter(None, os.environ.get("FREQUER_DEPS", "").split(os.pathsep)):
    if _dir not in sys.path:
        sys.path.append(_dir)
