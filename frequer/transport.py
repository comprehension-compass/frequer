"""Distributed counting: ship finished shard counts through git, receive them centrally.

A run split over machines (``count --part i/N``) needs its shard files on one
machine for the checkpoints and the build. Each remote part pushes its counts
files (``<shard>.json.gz``, a few MB each; never the corpus text, never
credentials) to its own throwaway branch ``<prefix>p<i>`` of this repository, under
``shards/<lang>/``: one branch per part, so pushes never race. The coordinator
fetches every ``<prefix>p*`` branch, copies new files into its counts directory
(their arrival order is the checkpoint order), takes the checkpoints, and on
convergence pushes the branch ``<prefix>stop``, which tells every remote to stop.
A part that finishes its share pushes ``shards/<lang>/DONE-p<i>``. The branches
are deleted after the build (``frequer receive --cleanup``).

Co-occurrence files stay home: they are tens of MB per shard, so the table is
counted on the coordinator's own part only (remote parts run ``--no-cooc``).
"""

from __future__ import annotations

import os
import shutil
import signal
import subprocess
import time
from collections.abc import Callable
from pathlib import Path

from frequer.config import REPO_ROOT
from frequer.counts import read_shard

TRAILER = (
    "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n"
    "Claude-Session: https://claude.ai/code/session_01LCaNDxgx4QeyJKvxvbEYHU\n"
)


def git(repo: Path, *args: str, check: bool = True) -> str:
    out = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if check and out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {out.stderr.strip()}")
    return out.stdout.strip()


def origin_url() -> str:
    return git(REPO_ROOT, "remote", "get-url", "origin")


def remote_has(repo: Path, branch: str) -> bool:
    return bool(git(repo, "ls-remote", "--heads", "origin", branch, check=False))


def open_branch(repo: Path, branch: str, url: str) -> None:
    """A clone at ``repo`` on ``branch`` (created as an empty orphan when the remote lacks it)."""
    if not (repo / ".git").exists():
        repo.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--no-checkout", "--filter=blob:none", url, str(repo)], check=True,
                       capture_output=True)
    if remote_has(repo, branch):
        git(repo, "fetch", "origin", branch)
        git(repo, "checkout", "-B", branch, f"origin/{branch}")
    else:
        git(repo, "checkout", "--orphan", branch)
        git(repo, "rm", "-rf", "--cached", ".", check=False)
        for child in repo.iterdir():
            if child.name != ".git":
                shutil.rmtree(child) if child.is_dir() else child.unlink()
        git(repo, "commit", "--allow-empty", "-m", f"Shard counts for a distributed frequer run ({branch}){TRAILER}")
        push(repo, branch)


def push(repo: Path, branch: str, tries: int = 6) -> None:
    for attempt in range(tries):
        out = subprocess.run(["git", "-C", str(repo), "push", "-q", "origin", f"HEAD:refs/heads/{branch}"],
                             capture_output=True, text=True)
        if out.returncode == 0:
            return
        time.sleep(min(60, 5 * 2**attempt))
    raise RuntimeError(f"push to {branch} failed: {out.stderr.strip()}")


def ship_once(lang: str, counts_dir: Path, repo: Path, branch: str, part: int, done: bool) -> int:
    """Copy new counts files into the branch, commit and push; returns how many were new."""
    dest = repo / "shards" / lang
    dest.mkdir(parents=True, exist_ok=True)
    new = []
    for path in sorted(counts_dir.glob("*.json.gz")):
        target = dest / path.name
        if not target.exists():
            shutil.copy2(path, target)
            new.append(target)
    marker = dest / f"DONE-p{part}"
    if done and not marker.exists():
        marker.write_text("done\n", encoding="utf-8")
        new.append(marker)
    if new:
        git(repo, "add", *[str(p.relative_to(repo)) for p in new])
        git(repo, "commit", "-q", "-m", f"{lang} part {part}: {len(new)} shard file(s){TRAILER}")
        push(repo, branch)
    return len(new)


def ship(lang: str, counts_dir: Path, repo: Path, *, prefix: str, part: int, count_pid: int | None,
         interval: int = 120, log: Callable[[str], None] = print) -> None:
    """Ship until the count finishes (then mark the part done) or the coordinator says stop.

    The part is done only when its count exited normally: ``count`` writes ``run-<ts>.json``
    beside the counts directory at the end of a complete pass.
    """
    branch = f"{prefix}p{part}"
    open_branch(repo, branch, origin_url())
    stale = repo / "shards" / lang / f"DONE-p{part}"
    if stale.exists() and count_pid is not None and _alive(count_pid):
        # A rerun after the manifest grew (more URLs or sources): the part is not done any more.
        git(repo, "rm", "-q", str(stale.relative_to(repo)))
        git(repo, "commit", "-q", "-m", f"{lang} part {part}: running again{TRAILER}")
        push(repo, branch)
    started = time.time()
    while True:
        alive = count_pid is not None and _alive(count_pid)
        finished = not alive and any(p.stat().st_mtime >= started for p in counts_dir.parent.glob("run-*.json"))
        n = ship_once(lang, counts_dir, repo, branch, part, done=finished)
        if n:
            log(f"shipped {n} file(s) to {branch}")
        if remote_has(repo, f"{prefix}stop"):
            log("the coordinator says stop")
            if alive and count_pid is not None:
                os.killpg(os.getpgid(count_pid), signal.SIGTERM)
            return
        if count_pid is None or not alive:
            if not finished:
                log("the count exited without finishing its pass: rerun it (it resumes), then ship again")
            return
        time.sleep(interval)


def _alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    return Path(f"/proc/{pid}").exists() and "zombie" not in Path(f"/proc/{pid}/status").read_text()


def receive(lang: str, counts_dir: Path, repo: Path, *, prefix: str) -> tuple[int, set[str]]:
    """Fetch every ``<prefix>p*`` branch and copy new shard files into ``counts_dir``.

    Returns the number of new files and the parts that marked themselves done.
    """
    if not (repo / ".git").exists():
        subprocess.run(["git", "clone", "--no-checkout", "--filter=blob:none", origin_url(), str(repo)],
                       check=True, capture_output=True)
    git(repo, "fetch", "-q", "--prune", "origin", f"+refs/heads/{prefix}p*:refs/remotes/origin/{prefix}p*")
    refs = git(repo, "for-each-ref", "--format=%(refname)", f"refs/remotes/origin/{prefix}p*").split()
    new, done = 0, set()
    counts_dir.mkdir(parents=True, exist_ok=True)
    for ref in refs:
        for path in git(repo, "ls-tree", "-r", "--name-only", ref, f"shards/{lang}/").split():
            name = Path(path).name
            if name.startswith("DONE-"):
                done.add(name.removeprefix("DONE-"))
                continue
            target = counts_dir / name
            if target.exists():
                continue
            tmp = counts_dir / (name + ".part")
            with tmp.open("wb") as fp:
                subprocess.run(["git", "-C", str(repo), "cat-file", "blob", f"{ref}:{path}"], stdout=fp, check=True)
            read_shard(tmp)  # a truncated or foreign file fails here, before it can be merged
            tmp.replace(target)
            new += 1
    return new, done


def signal_stop(repo: Path, prefix: str) -> None:
    """Push ``<prefix>stop`` (any commit): every remote ``ship`` loop stops its count."""
    refs = git(repo, "for-each-ref", "--format=%(refname)", f"refs/remotes/origin/{prefix}p*").split()
    if not refs:
        raise RuntimeError("no part branch to point the stop branch at")
    sha = git(repo, "rev-parse", refs[0])
    git(repo, "push", "-q", "origin", f"{sha}:refs/heads/{prefix}stop")


def cleanup(repo: Path, prefix: str) -> dict[str, list[str]]:
    """Delete every ``<prefix>*`` branch on the remote (after the build). Some git proxies refuse
    branch deletion; what could not be deleted is returned for a person to delete."""
    heads = git(repo, "ls-remote", "--heads", "origin", f"{prefix}*").split("\n")
    names = [line.split("refs/heads/", 1)[1] for line in heads if "refs/heads/" in line]
    out: dict[str, list[str]] = {"deleted": [], "refused": []}
    for name in names:
        ok = subprocess.run(["git", "-C", str(repo), "push", "-q", "origin", f":refs/heads/{name}"],
                            capture_output=True).returncode == 0
        out["deleted" if ok else "refused"].append(name)
    return out


def coordinate(lang: str, counts_dir: Path, repo: Path, *, prefix: str, parts: int, local_pid: int | None,
               checkpoint: Callable[[], str], interval: int = 180, log: Callable[[str], None] = print) -> str:
    """Receive, checkpoint, and stop everything on convergence; returns why it ended.

    ``checkpoint`` takes the due checkpoints and returns the decision (``stop`` or not).
    Ends when the run converged (``stop``), or when the local part has finished and every
    remote part has marked itself done (``exhausted``).
    """
    while True:
        new, done = receive(lang, counts_dir, repo, prefix=prefix)
        if new:
            log(f"received {new} shard file(s); remote parts done: {sorted(done) or 'none'}")
        decision = checkpoint()
        local_alive = local_pid is not None and _alive(local_pid)
        if decision == "stop":
            signal_stop(repo, prefix)
            if local_alive and local_pid is not None:
                os.killpg(os.getpgid(local_pid), signal.SIGTERM)
            log("converged: stop signalled to every part")
            return "stop"
        if not local_alive and done >= {f"p{i}" for i in range(1, parts)}:
            log("every part has finished its share")
            return "exhausted"
        time.sleep(interval)
