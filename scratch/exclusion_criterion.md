# Criterion (the developer's words; binding)

Honeyeater's Spanish frequency list (top 50,000 lemmas counted from Spanish web text and Tatoeba) is
being cleaned. **Remove English words and boilerplate, but don't remove words that are borrowed into
Spanish and adapted, to the point that an English-speaking learner would want to learn that they're
used in Spanish.**

- *show*, *web*, *online*, *marketing*, *chat*, *blog*, *email* are likely real Spanish loans: keep.
- *the*, *of*, *and*, *in*, *to*, *by*, *new*, *home*, *house*, *black*, *city* in running English
  template text are leakage: exclude.
- Borderline cases (*cookie*, *low cost*, *resort*, *top*, *beach*) need a real judgement on Spanish
  usage: *low cost* is established in Spain ("aerolínea low cost"); *beach* is not.
- Real Spanish words that happen to look English stay: *once* ("eleven"), *metro*, *led*, *real*,
  *final*, *son*, *come*, *fin*, *red*, *pie*, *mar*, *sale*, *dice*, etc.
- Boilerplate: website/template text that is not Spanish vocabulary a learner needs, e.g. the
  flight-search site's brand and template spellings such as *aereo* (unaccented, where the accented
  Spanish word *aéreo* exists) and other unaccented misspellings of an accented Spanish word.
- Proper nouns (names of people, places, brands) are NOT the target of this pass: the app ignores
  proper nouns by default. Mark a genuine proper noun `keep-spanish` with reason "proper noun".
  But an ordinary English word that the tagger mislabelled PROPN (e.g. *the*, *city*) is leakage.

Classes (exactly one per lemma):
- `exclude-english`  — an English word, not an established Spanish loan;
- `exclude-boilerplate` — website/template/brand text or a template misspelling;
- `keep-loan` — an English (or other) borrowing that is established in Spanish usage;
- `keep-spanish` — a Spanish word (including ones that look English), or a proper noun.

A homograph key such as `metro#metre` or `real#royal` is the Spanish lemma with a sense tag.
