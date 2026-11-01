"""Command line: ``python -m frequer {count,build,pilot,sync-manifest,forms,select} <lang>``."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

from frequer import transport
from frequer.build import BuildOptions, build_language
from frequer.checkpoint import run_checkpoints
from frequer.config import Observed, load_manifest, write_observed
from frequer.counts import iter_counts, read_shard
from frequer.forms_run import run_forms
from frequer.ranking import SCORES
from frequer.run import RunDirs, count_language, parse_part
from frequer.select import run_select
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
    c.add_argument("--checkpoints", action="store_true",
                   help="take convergence checkpoints as shards finish and stop when the list has converged")
    c.add_argument("--out-dir", type=Path, help="where checkpoints go (default out/<lang>; give build the same)")
    c.add_argument("--part", help="i/N: count only part i of N (README §Distributed counting)")
    c.add_argument("--no-cooc", action="store_true", help="skip the co-occurrence pass (remote parts)")
    c.add_argument("--skip-file", type=Path,
                   help="counts file names finished elsewhere, one per line: cut past, never counted (remote parts)")
    ck = sub.add_parser("checkpoint", help="take the convergence checkpoints that are due; print the decision")
    _common(ck)
    ck.add_argument("--out-dir", type=Path)
    ck.add_argument("--no-snapshot", action="store_true", help="skip the latest checkpoint's snapshot")
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
    fm = sub.add_parser("forms", help="tokenizer-only form inventory: counts, documents, sites per form")
    fm.add_argument("lang")
    fm.add_argument("--data-dir", type=Path, default=Path(os.environ.get("FREQUER_DATA", "data")))
    fm.add_argument("--out-dir", type=Path, default=Path("out"))
    fm.add_argument("--tokens", type=int, default=50_000_000, help="word-token budget over all sources")
    fm.add_argument("--workers", type=int, default=2)
    fm.add_argument("--keep-shards", action="store_true", help="keep the cleaned shards after the merge")
    sl = sub.add_parser("select", help="rank the forms the labels lack into candidates-<lang>.tsv")
    sl.add_argument("lang")
    sl.add_argument("--forms", type=Path, required=True)
    sl.add_argument("--lookup", type=Path, required=True, help="the release's lookup.json")
    sl.add_argument("--curated", type=Path, help="curated TSV; first column is a listed form")
    sl.add_argument("--case-fold", action="store_true", help="also exclude capitalised forms whose lower case is listed")
    sl.add_argument("--top", type=int, default=1000)
    sl.add_argument("--min-docs", type=int, default=5)
    sl.add_argument("--out-dir", type=Path, help="default: next to --forms")
    sh = sub.add_parser("ship", help="push this part's finished shard counts to its git branch (remote parts)")
    sh.add_argument("lang")
    sh.add_argument("--data-dir", type=Path, default=Path(os.environ.get("FREQUER_DATA", "data")))
    sh.add_argument("--repo", type=Path, required=True, help="a scratch clone used for the shard branch")
    sh.add_argument("--part", required=True, help="i/N, as given to count")
    sh.add_argument("--prefix", help="branch prefix (default <lang>-shards-)")
    sh.add_argument("--count-pid", type=int, help="the count's pid (started with setsid); ship until it ends")
    sh.add_argument("--interval", type=int, default=120)
    co = sub.add_parser("coordinate", help="receive remote parts' shards, take checkpoints, stop on convergence")
    _common(co)
    co.add_argument("--repo", type=Path, required=True, help="a scratch clone used to fetch the shard branches")
    co.add_argument("--parts", type=int, required=True, help="N, as in --part i/N")
    co.add_argument("--prefix")
    co.add_argument("--out-dir", type=Path)
    co.add_argument("--local-pid", type=int, help="the local part's count pid (started with setsid)")
    co.add_argument("--interval", type=int, default=180)
    co.add_argument("--cleanup", action="store_true", help="delete the shard branches and exit (after the build)")
    args = parser.parse_args(argv)
    manifest = load_manifest(args.lang)
    names = args.sources.split(",") if getattr(args, "sources", None) else None

    if args.cmd == "forms":
        header = run_forms(manifest, data_dir=args.data_dir, out_dir=args.out_dir, tokens=args.tokens,
                           workers=args.workers, keep_shards=args.keep_shards)
        print(json.dumps({k: v for k, v in header.items() if k != "sources"}, indent=1))
    elif args.cmd == "select":
        if manifest.forms is None:
            raise SystemExit(f"{args.lang}: the manifest has no forms: block")
        stats = run_select(args.lang, forms=args.forms, lookup=args.lookup, curated=args.curated,
                           case_fold=args.case_fold, top=args.top, min_docs=args.min_docs,
                           script=manifest.forms.script, out_dir=args.out_dir or args.forms.parent)
        print(json.dumps(stats, indent=1))
    elif args.cmd == "count":
        dirs = RunDirs(args.data_dir / args.lang)
        skip = frozenset(
            line.strip() for line in args.skip_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        ) if args.skip_file else frozenset()
        if args.no_cooc:
            manifest = manifest.model_copy(update={"cooc": manifest.cooc.model_copy(update={"enabled": False})})
        summary = count_language(
            manifest, dirs, part=parse_part(args.part) if args.part else None, workers=args.workers, shard_chars=args.shard_chars, sources=names,
            limits=lambda n: Limits(max_chars=args.max_chars, max_urls=args.max_urls,
                                    stride=manifest.source(n).stride, skip=skip),
            lemma_dir=args.lemma_dir, wheel=args.wheel,
            checkpoints_out=(args.out_dir or Path("out") / args.lang) if args.checkpoints else None,
        )
        print(json.dumps(summary, indent=1))
    elif args.cmd == "ship":
        i, _n = parse_part(args.part)
        transport.ship(args.lang, args.data_dir / args.lang / "counts", args.repo,
                       prefix=args.prefix or f"{args.lang}-shards-", part=i, count_pid=args.count_pid,
                       interval=args.interval)
    elif args.cmd == "coordinate":
        prefix = args.prefix or f"{args.lang}-shards-"
        if args.cleanup:
            print(json.dumps(transport.cleanup(args.repo, prefix)))
            return
        out = args.out_dir or Path("out") / args.lang
        cmd = [sys.executable, "-m", "frequer", "checkpoint", args.lang, "--data-dir", str(args.data_dir),
               "--out-dir", str(out)]
        cmd += ["--lemma-dir", str(args.lemma_dir)] if args.lemma_dir else []
        cmd += ["--wheel", str(args.wheel)] if args.wheel else []

        def checkpoint() -> str:
            done = subprocess.run(cmd, capture_output=True, text=True)
            for line in done.stdout.splitlines():
                if line.startswith("checkpoint"):
                    print(line, flush=True)
            if done.returncode != 0:
                print(f"checkpoint failed: {done.stderr[-2000:]}", flush=True)
                return "continue"
            return str(json.loads(done.stdout.splitlines()[-1])["decision"])

        why = transport.coordinate(args.lang, args.data_dir / args.lang / "counts", args.repo, prefix=prefix,
                                   parts=args.parts, local_pid=args.local_pid, checkpoint=checkpoint,
                                   interval=args.interval, log=lambda m: print(m, flush=True))
        print(json.dumps({"ended": why}))
    elif args.cmd == "checkpoint":
        dirs = RunDirs(args.data_dir / args.lang)
        state = run_checkpoints(manifest, dirs.counts, args.out_dir or Path("out") / args.lang,
                                lemma_dir=args.lemma_dir, wheel=args.wheel, write_snapshot=not args.no_snapshot)
        print(json.dumps({"decision": state["decision"], "stopped_at": state.get("stopped_at"),
                          "checkpoints": len(state["checkpoints"])}))
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
