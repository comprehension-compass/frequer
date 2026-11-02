"""Every learnable name gets an entry (developer ruling, 2026-11-02): the plan for the names after the cut.

Honeyeater's reviewed learnable-names list (``reference/learnable-names/<code>.json``) decides which place and
language names are learnable; the snapshot must give each one an entry, since the loaded list is the learnable
set. For every listed name not already on the list (after the ``top_n`` cut), in this order:

1. **Counted**: its counted row is appended, in rank order, whatever the filters did with it.
2. **Filed under another lemma**: a single-token name the release lemmatises to a different key (looked up
   through the runtime) is listed with that lemma: the lemma's row is appended (bare if uncounted) unless it is
   already on the list. A key the release never produces would never match a token in the reader.
3. **Uncounted single token**: appended bare (frequency 0, no forms), under the list's spelling (folded when the
   language folds case).
4. **Multiword, not emitted as a unit**: not appended (no token would ever carry it); written to
   ``learnable-multiword-names.tsv`` as input for the next lemma release's unit training.

The plan is pure (``plan``); the build applies it.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field


@dataclass
class NamePlan:
    #: counted keys to append, in the order given (rank order)
    counted: list[str] = field(default_factory=list)
    #: (name, the lemma the release files it under)
    filed: list[tuple[str, str]] = field(default_factory=list)
    #: keys to append bare (frequency 0): uncounted names and uncounted filed-under lemmas
    bare: list[str] = field(default_factory=list)
    #: multiword names the release does not emit as a unit
    multiword: list[str] = field(default_factory=list)

    def appended(self) -> list[str]:
        """Every key appended: counted rows first (rank order), then the bare entries. A filed-under lemma is in
        one of the two only when it was not already on the list."""
        return [*self.counted, *self.bare]


def plan(spellings: Mapping[str, str], on_list: Iterable[str], counted_in_rank_order: Iterable[str],
         lemma_of: Callable[[str], str | None], fold_case: bool) -> NamePlan:
    """``spellings``: case-folded name -> listed spelling; ``on_list``: the keys already chosen; ``lemma_of``:
    the counted key the runtime files a word under (None when it files none)."""
    out = NamePlan()
    listed = {k.split("#")[0].casefold() for k in on_list}
    counted = list(counted_in_rank_order)
    by_fold: dict[str, str] = {}
    for k in counted:
        by_fold.setdefault(k.split("#")[0].casefold(), k)
    for k in counted:  # 1. counted names, in rank order
        n = k.split("#")[0].casefold()
        if n in spellings and n not in listed:
            out.counted.append(k)
            listed.add(n)
    for n in sorted(spellings):
        if n in listed:
            continue
        name = spellings[n]
        if " " in name:  # 4. a multiword name no unit carries
            out.multiword.append(name)
            continue
        lemma = lemma_of(name)
        if lemma and lemma.split("#")[0].casefold() != n:  # 2. filed under another lemma
            out.filed.append((name, lemma))
            target = lemma.split("#")[0].casefold()
            if target not in listed:
                (out.counted if target in by_fold else out.bare).append(by_fold.get(target, lemma))
                listed.add(target)
            continue
        out.bare.append(name.lower() if fold_case else name)  # 3. uncounted single token
        listed.add(n)
    return out
