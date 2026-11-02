"""Re-stream a cleaned corpus sample (same hygiene and shard code as the count) for review examples.

    python sample.py <config.json>      (config "sample": {source: {"urls": [...], "max_chars": N}}; a
                                         source not named is read whole: the small first sources)
"""

from __future__ import annotations

import sys

from common import load

from frequer.config import load_manifest
from frequer.hygiene import make_classifier
from frequer.shards import Limits, produce_shards

cfg = load(sys.argv[1])
root = cfg["work"] / "sample"
m = load_manifest(cfg["lang"])
classify = make_classifier()
for src in m.sources:
    spec = cfg.get("sample", {}).get(src.name)
    if spec is None and not src.first:
        continue
    lim = Limits(max_chars=spec.get("max_chars"), url_indices=tuple(spec["urls"])) if spec else Limits()
    for job in produce_shards(lang=cfg["lang"], source=src, hygiene=m.hygiene_for(src), parts=m.parts,
                              work_dir=root / "work", counts_dir=root / "counts", limits=lim, classify=classify,
                              url_stats={}):
        print(job.path, job.lines, flush=True)
