"""Command line: ``python -m frequer {count,build,pilot,sync-manifest} <lang>``."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date
from pathlib import Path

from frequer.build import BuildOptions, build_language
from frequer.config import Observed, load_manifest, write_observed
from frequer.counts import iter_counts, read_shard
from frequer.ranking import SCORES
from frequer.run import RunDirs, count_language
from frequer.shards import Limits


def _common(p: argparse.ArgumentParser) -> None:
    p.add_argument("lang")
    p.add_argument("--data-dir", type=Path, default=Path(os.environ.get("FREQUER_DATA", "data")))
    p.add_argument("--lemma-dir", type=Path, help="installed honeyeater_lemma_<lang> package dir")
    p.add_argument("--wheel", type=Path, help="the wheel file, to record its sha256")
    p.add_argument("--workers", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    p.add_argument("--sources", help="comma-separated source names")


def _build_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--score", default="frequency", choices=SCORES)
    p.add_argument("--top-n", type=int)
    p.add_argument("--candidates", type=int, help="lemmas kept in full detail (default 4 x top-n)")
    p.add_argument("--no-snapshot", action="store_true")


def _opts(args: argparse.Namespace, scope: str) -> BuildOptions:
    return BuildOptions(score=args.score, top_n=args.top_n, candidates=args.candidates, scope=scope,
                        lemma_dir=args.lemma_dir, wheel=args.wheel, write_snapshot=not args.no_snapshot)


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="frequer", description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("count", help="fetch, clean and count shards (resumable)")
    _common(c)
    c.add_argument("--shard-chars", type=int)
    c.add_argument("--max-chars", type=int, help="cap raw characters read per URL")
    c.add_argument("--max-urls", type=int)
    b = sub.add_parser("build", help="merge counts, rank, write snapshot, sidecar and report")
    _common(b)
    _build_args(b)
    b.add_argument("--out-dir", type=Path)
    b.add_argument("--scope", default="full", help="label recorded in the header and report (full, pilot)")
    pl = sub.add_parser("pilot", help="count a small slice per the manifest's pilot block, then build")
    _common(pl)
    _build_args(pl)
    pl.add_argument("--out-dir", type=Path, help="where report.md and perf.json go (default pilot/<lang>)")
    sm = sub.add_parser("sync-manifest", help="record observed token counts in the manifest")
    sm.add_argument("lang")
    sm.add_argument("--counts-dir", type=Path, required=True)
    sm.add_argument("--scope", default="full")
    args = parser.parse_args(argv)
    manifest = load_manifest(args.lang)
    names = args.sources.split(",") if getattr(args, "sources", None) else None

    if args.cmd == "count":
        dirs = RunDirs(args.data_dir / args.lang)
        summary = count_language(
            manifest, dirs, workers=args.workers, shard_chars=args.shard_chars, sources=names,
            limits=lambda _n: Limits(max_chars=args.max_chars, max_urls=args.max_urls),
            lemma_dir=args.lemma_dir, wheel=args.wheel,
        )
        print(json.dumps(summary, indent=1))
    elif args.cmd == "build":
        dirs = RunDirs(args.data_dir / args.lang)
        out = args.out_dir or Path("out") / args.lang
        print(json.dumps(build_language(manifest, dirs.counts, out, _opts(args, args.scope)), indent=1))
    elif args.cmd == "pilot":
        pilot = manifest.pilot
        dirs = RunDirs(args.data_dir / "pilot" / args.lang)
        summary = count_language(
            manifest, dirs, workers=args.workers, shard_chars=pilot.shard_chars, sources=names,
            limits=lambda n: Limits(max_chars=pilot.max_chars_per_url[n], max_urls=pilot.urls.get(n)),
            lemma_dir=args.lemma_dir, wheel=args.wheel,
        )
        out = args.out_dir or Path("pilot") / args.lang
        built = build_language(manifest, dirs.counts, out, _opts(args, "pilot"))
        built["count_wall_seconds"] = round(summary["wall_seconds"], 1)
        built["workers"] = summary["workers"]
        built["main_process_peak_rss_mb"] = round(summary["main_peak_rss_mb"])
        built["urls"] = summary["urls"]
        (out / "perf.json").write_text(json.dumps(built, indent=1), encoding="utf-8")
        print(json.dumps(built, indent=1))
    else:
        observed: dict[str, list[Observed]] = {k: list(v) for k, v in manifest.observed.items()}
        per_source: dict[str, dict[str, int]] = {}
        for source, path in iter_counts(args.counts_dir):
            shard = read_shard(path)
            t = per_source.setdefault(source, {"tokens": 0, "documents": 0, "shards": 0, "lines": 0})
            t["tokens"] += shard["tokens"]
            t["documents"] += shard["docs"]
            t["shards"] += 1
            t["lines"] += shard["lines"]
        for source, t in per_source.items():
            runs = [o for o in observed.get(source, []) if o.scope != args.scope]
            runs.append(Observed(scope=args.scope, date=date.today().isoformat(), partial=args.scope != "full", **t))
            observed[source] = runs
        write_observed(args.lang, observed)
