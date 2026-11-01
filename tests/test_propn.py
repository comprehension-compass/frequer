import json
from pathlib import Path

from frequer import propn


def test_proper_nouns_drop_unless_learnable(tmp_path: Path) -> None:
    (tmp_path / "reference" / "learnable-names").mkdir(parents=True)
    (tmp_path / "reference" / "learnable-names" / "es.json").write_text(
        json.dumps({"schema_version": 1, "names": ["España", "Nueva York"]}), encoding="utf-8")
    names = propn.load(tmp_path, "es")
    rows = [("de", "ADP"), ("españa", "PROPN"), ("tom", "PROPN"), ("nueva york", "PROPN"), ("dios", "NOUN")]
    kept, dropped, learnable = propn.apply(rows, lambda r: r[0], lambda r: r[1], names,
                                           {r[0]: i for i, r in enumerate(rows, start=1)})
    assert [r[0] for r in kept] == ["de", "españa", "nueva york", "dios"]
    assert dropped == [(3, "tom")] and learnable == [(2, "españa"), (4, "nueva york")]
