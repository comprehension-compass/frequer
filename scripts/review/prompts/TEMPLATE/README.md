# Prompt files for a new language

Copy this directory to `prompts/<code>/` and edit every `<...>` marker by hand: the language's name, its own
examples (from its first flagged round, not invented), and the sections that differ (a language without case has
no capitalisation evidence; a language without spaces has no hyphenated compounds; German capitalises every
noun). The texts are the binding es and ja rules (`../es/`, `../ja/`) with the cross-language developer rulings
folded in (`docs/DECISIONS.md`). The developer reads the new files before the first round runs: they are
binding rules, so a change is a ruling.

| file | used by | stage |
|---|---|---|
| `rules-flagged.md` | `review.py` (config `rules`) | flagged rounds |
| `rules-unflagged.md` | `review.py` (config `rules_unflagged`) | full review of screened suspects |
| `screener.md` | `screen.py` (config `screener`) | triage of unflagged keeps |
| `institutions-screen.md` | `screen.py --pool drops` (config `institutions_screen`) | institutions re-decision |
| `institutions-review.md` | `review.py --decisions keep,drop` | institutions re-decision |

The common wrappers (`../common/`) add the lemma entries and the answer format; the rules files hold only the
rules. Keep each rule with one or two real examples: reviewers follow examples more reliably than definitions.
