"""The app's number check, for the number rule (``JunkConfig.number_rule``).

frequer has no number definition of its own: it runs inside the pinned Honeyeater checkout and asks the app's
default-ignore classifier (``lexicon.lemma_defaults``), so the list drops exactly the spelled numbers the app
ignores. ``None``: not a number (a counter or date form such as 一つ, 二十日, a base word the app treats as
vocabulary); ``True``: a learnable number (a core number word up to 30, a single 漢数字 unit character);
``False``: a number the app ignores (千九百九十八).

Honeyeater PR #766 makes this one public function, ``number_is_learnable(text, language_code)``, which also reads
the per-language irregular forms (三百, 六百, 八百); until it lands, the private helpers it replaces are used.
"""

from __future__ import annotations

from collections.abc import Callable


def app_number_check(code: str) -> Callable[[str], bool | None]:
    from frequer.runtime import setup_django

    setup_django()
    import lexicon.lemma_defaults as ld

    public = getattr(ld, "number_is_learnable", None)
    if public is not None:
        return lambda text: public(text, code)
    from lexicon.number_words import number_words

    words = number_words(code)

    def check(text: str) -> bool | None:
        if text in words:  # LemmaFacts.is_number_word: a cardinal or ordinal word up to 30
            return True
        return ld._number_is_learnable(text)  # type: ignore[no-any-return]

    return check
