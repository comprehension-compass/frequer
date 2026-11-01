import io

import pytest

from frequer.config import SourceConfig
from frequer.sources import iter_docs


def _source(**kw: object) -> SourceConfig:
    return SourceConfig.model_validate({"name": "pc", "kind": "tsv", "urls": ["u"], "licence": "CC0", "column": 1,
                                        "pseudo_doc_lines": 2, "stride": 3, **kw})


def test_stride_offsets_are_disjoint_virtual_urls() -> None:
    src = _source(stride_offsets=[0, 1, 2])
    assert src.virtual_urls() == [("u", 0), ("u", 1), ("u", 2)]
    data = b"".join(f"en{i}\tes{i}\n".encode() for i in range(12))
    seen = []
    for k, (_url, offset) in enumerate(src.virtual_urls()):
        docs = list(iter_docs(src, k, io.BytesIO(data), src.stride, offset))
        seen.append([line for d in docs for line in d.lines])
    # pseudo-documents of 2 lines, every 3rd from its offset: together each line once
    assert seen[0] == ["es0", "es1", "es6", "es7"] and seen[1] == ["es2", "es3", "es8", "es9"]
    assert sorted(x for s in seen for x in s) == sorted(f"es{i}" for i in range(12))
    assert _source().virtual_urls() == [("u", 0)]
    with pytest.raises(ValueError):
        _source(stride_offsets=[1, 2]).virtual_urls()
