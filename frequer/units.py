"""Hook for counting units (reflexive and separable verbs, set phrases) as themselves.

The unit component is not trained yet (plan custom-lemmatisers-and-units §3.6,
§10 D-5), so nothing here invents units. When it lands, implement
:class:`UnitCounter` over the sentence the runtime analysed and pass the
instance to :func:`frequer.counting.count_shard`; the shard files, the merge and
the sidecar already carry a ``units`` table of ``{unit: [frequency, documents]}``.
"""

from __future__ import annotations

from typing import Protocol

from frequer.runtime import AnalysedSentence


class UnitCounter(Protocol):
    def units(self, sentence: AnalysedSentence) -> list[str]:
        """Unit keys occurring in ``sentence`` (one entry per occurrence)."""
        ...


class NoUnits:
    """The default until the unit component exists: no units are counted."""

    def units(self, sentence: AnalysedSentence) -> list[str]:
        return []
