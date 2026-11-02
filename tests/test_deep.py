"""A deeper pass (``skip_chars``) starts at exactly the document after an earlier capped pass's last one."""

from __future__ import annotations

import gzip
from pathlib import Path

from frequer.config import Hygiene, SourceConfig
from frequer.shards import Limits, produce_shards


def _classify(line: str) -> tuple[str, float]:
    return "de", 1.0


def _docs(job_paths: list[Path]) -> list[str]:
    out: list[str] = []
    for path in job_paths:
        with gzip.open(path, "rt", encoding="utf-8") as fp:
            out += [line.rstrip("\n").split("\t")[-1] for line in fp]
    return out


def _run(tmp: Path, name: str, url: str, cap: int | None, skip: int) -> list[str]:
    source = SourceConfig(name=name, kind="tsv", urls=[url], licence="x", column=0, pseudo_doc_lines=1,
                          shard_chars=100, max_chars_per_url=cap, skip_chars=skip)
    hygiene = Hygiene(min_chars=1, max_chars=1000, min_alpha_ratio=0.0, gap_filter=False, langid_min_prob=0.0)
    work, counts = tmp / name / "work", tmp / name / "counts"
    work.mkdir(parents=True)
    counts.mkdir()
    jobs = produce_shards(lang="de", source=source, hygiene=hygiene, parts=10, work_dir=work, counts_dir=counts,
                          limits=Limits(), classify=_classify, url_stats={})
    return _docs([job.path for job in jobs])


def test_deep_pass_continues_where_the_cap_stopped(tmp_path: Path) -> None:
    lines = [f"Satz Nummer {i} mit etwas Text" + "x" * (i % 7) for i in range(200)]
    corpus = tmp_path / "c.tsv"
    corpus.write_text("".join(f"{line}\n" for line in lines), encoding="utf-8")
    cap = 1500
    first = _run(tmp_path, "a", str(corpus), cap, 0)
    deep = _run(tmp_path, "b", str(corpus), None, cap)
    assert first and deep
    assert first + deep == lines  # no document read twice, none missed
