"""The pipeline checklist: the licence rule and stage detection from the files stages leave behind."""

from __future__ import annotations

import json
from pathlib import Path

from frequer import pipeline
from frequer.config import load_manifest


def test_licence_rule_admits_public_domain_cc0_and_cc_by_only() -> None:
    for ok in ("CC0-1.0", "CC-BY-2.0-FR", "CC-BY-4.0", "public-domain"):
        assert pipeline.licence_ok(ok), ok
    for bad in ("CC-BY-SA-4.0", "CC-BY-NC-4.0", "CC-BY-ND-3.0", "proprietary", ""):
        assert not pipeline.licence_ok(bad), bad


def test_stages_follow_the_files(tmp_path: Path) -> None:
    m = load_manifest("de")  # no cutoff ruling yet
    paths = pipeline.Paths("de", tmp_path / "data" / "de", tmp_path / "out" / "de", tmp_path / "rev",
                           tmp_path / "review.tsv")
    status = {s.key: st for s, st in pipeline.evaluate(m, paths)}
    assert status["manifest"] == "done" and status["count"] == "next" and status["converge"] == "waiting"

    (paths.data / "counts").mkdir(parents=True)
    (paths.data / "counts" / "hplt.00.00000.tsv.gz").write_text("x")
    paths.out.mkdir(parents=True)
    (paths.out / "convergence.json").write_text(json.dumps({"decision": "stop"}))
    (paths.out / "report.md").write_text("x")
    (paths.out / "de.flags.tsv").write_text("x")
    assert paths.review is not None
    paths.review.mkdir()
    (paths.review / "routed.tsv").write_text("# head\n1\tHaus\tkeep\n2\tXyz\tpending\n")
    status = {s.key: st for s, st in pipeline.evaluate(m, paths)}
    assert [status[k] for k in ("count", "converge", "build", "route", "flagged")] == \
        ["done", "done", "done", "done", "next"]
    assert "1 lemmas are pending" in pipeline.render(m, paths)
