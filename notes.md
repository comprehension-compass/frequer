## Frequency to CEFR alignment
TOCFL and HSK lists suggest the following alignment:
A1 500
A2 1000
B1 2500
B2 5000
C1 8000
C2 ?

This also seems to line up with this paper: https://files.eric.ed.gov/fulltext/EJ887873.pdf

I received estimates around 5000 for my vocabulary in French and German: https://www.arealme.com/german-vocabulary-size-test/en/

Potentially need to make it lower if you're talking about the most frequent x words, as this is different to total vocabulary size.

Could also split as 500-1000-2000-4000-8000 so it's beautiful and even.

## Post-processing steps

Fully automated processing:
1. Frequency cut-off: There are millions of lemmas with very low occurence that are not useful for most processes, increase file size and slow processing -> remove lemmas below a frequency threshhold (min_freq)
2. Numbers and symbols: Many numbers and symbols appear as lemmas -> remove any lemmas that don't contain at least one letter
3. Capitalisation: Capitalised words are often not lemmatised by lemmatisers -> if a non-lowercase 'lemma' has a lowercase equivalent that occurs sufficiently often (more than min_freq times), then use that lemmatisation instead

Partially manual processing:
1. Lemmatisation mistakes: Occasional lemmatisation mistakes don't cause issues, but consistent mis-lemmatisation of a common forms does. For example, when a common noun is consistently mis-lemmatised as a conjugation of an uncommon verb.
    - Automatically highlight for review lemmas where any forms are more than 100x the median for that lemma (may not be appropriate for languages with little inflectional morphology), correct lemmatisation
    - Automatically highlight for review lemmas where the plural is under the lemma but not the singular, correct lemmatisation
    - Automatically highlight for review lemmas where the lemma itself has elsewhere been lemmatised to something else, correct lemmatisation
    - Automatically highlight for review lemmas that are one or two characters, check these are actually words, correct lemmatisation or mark as not for learning
    - Provide ordered list to an LLM for flagging and manually review
    - Manually check
2. Incorrect language: It is common for other languages, especiallly English to occur in the dataset. This is partially made up of genuine occurences in the foreign language, for example in proper nouns, but they should not be included in lists of words to learn for language learners so they should be marked as such.
    - LLM to mark these words as not for learning when adding definitions
    - Manual check
3. Proper nouns: Some proper nouns such as country names should be learned, some such as personal or brand names should not
    - Automatically highlight all non-lowercase lemmas for review
    - Provide list to an LLM for flagging and manually review
    - Manual check


## Spanish
### Tatoeba
Total processing time: 0:00:43
Statistics:
  Total words: 2980170
  Total sentences: 414491
  Unique lemmas before filtering: 52623
  Lemmas removed by frequency (min freq=3): 30298
  Lemmas removed by digit filtering: 218
  Lemmas removed by case check: 3565
  Total lemmas removed: 34081
  Final unique lemmas: 18542
Processing speed: 68690.33 words/sec, 9553.66 sentences/sec

Wordfreq Comparison:
  Common lemmas found: 634/1000, 1350/2000, 3380/5000

### Paracrawl
Total processing time: 4:06:12
Statistics:
  Total words: 4744276261
  Total sentences: 269394967
  Unique lemmas before filtering: 15872446
  Lemmas removed by frequency (min freq=50): 15278764
  Lemmas removed by digit filtering: 42884
  Lemmas removed by case check: 118257
  Total lemmas removed: 15439905
  Final unique lemmas: 432541
Processing speed: 321155.35 words/sec, 18236.21 sentences/sec

Wordfreq Comparison:
  Common lemmas found: 703/1000, 1494/2000, 3808/5000