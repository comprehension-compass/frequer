# es review shard 23: report (round 18, cascade)

Branch `es-review-shard-23`, created from `origin/full-es` at `543d45d`. Since round 17 the only change to the
rules files is the diminutive call (580ac25), which the reviewers and adjudicator now had. I reused shard 19's
runtime, wheel and sample, copied into `$HOME/es-review-23`, and reran the setup script there for the config and
`routed.tsv`. All `review.py` lines passed `--rules` and `--decisions keep,drop,merge`. There were no failed
calls and nothing was rerun.

## Counts

| step | count |
|---|---|
| flagged queue (pending) | 182 |
| flagged with an example | 141 (77.5%: **under the ~85% mark**) |
| flagged reviewers agreed | 174 (drop 148, merge 20, keep 6); 8 sent to the adjudicator; 0 accent-only merges |
| flagged queried at the gate | 2 |
| flagged adjudicated (8 disagreements + 2 queries) | 10 (keep 2, drop 5, merge 3) |
| **flagged final** | **keep 7, drop 153, merge 22** |
| unflagged screened | 203 (1 batch, 0 failed) |
| suspects (either screener) | 112 (97 marked by both) |
| suspects with an example | 96 (85.7%) |
| unflagged reviewers agreed | 110 (drop 58, merge 36, keep 16); 2 sent to the adjudicator; 1 accent-only merge (alergía) |
| unflagged queried at the gate | 3 |
| unflagged adjudicated (2 disagreements + 3 queries) | 5 (keep 3, drop 1, merge 1) |
| **unflagged final** (suspects only; the 91 non-suspects stay keep) | **keep 19, drop 57, merge 36** |

## Gate

I read every agreed merge and keep in both rounds and all the agreed drops (lemma and reason). I checked forms
where a drop might hide a real word (vagos, mester, pijao, galano); each is mostly a name, with the real reading
a minority, so those decisions hold.

Flagged queries → adjudicator:
- cruzr (agreed merge:cruz; all 68 occurrences are capitalised "Cruz") → **drop** (surnames and places; merging
  would add name counts to cruz).
- cereso (agreed keep; CERESO, a Mexican prison type) → **keep** (an acronym used as an ordinary noun, like ONG).

Unflagged queries → adjudicator:
- bús (agreed merge:autobús) → **merge:bus** (a misspelling of bus, which has its own entry).
- recebar (agreed drop as Portuguese) → **keep**, with a split question recebo → recebo (jamón de recebo, gravel).
- jijiji (agreed drop as typed laughter; queried against the interjection rule) → **drop** (a repeated token, not
  a lexicalised interjection).

## Things for the coordinator

- Flagged example coverage is 77.5%, under the ~85% mark; unflagged is 85.7%.
- Diminutives: no diminutive-shaped lemma in this shard was decided as a diminutive. The only ones with that shape
  are humanita (Latin), nocilla (a brand used as a common noun) and pradillo (a name).
- Split-by-form question (ruling 2), which the coordinator writes: recebar (recebo, Recebo → recebo; recebe and
  receba are Portuguese and drop).
- Possible new classes of question:
  - typed laughter (jaja, jeje, jiji, jojo): always drop, or ever keep as an interjection?
  - whether all-caps headings count toward the one-third threshold (solidos, from RESIDUOS SOLIDOS);
  - a split loan whose other half isn't in the batch (cetera → etcétera; "et" would drop);
  - a broken lemma whose forms are all a capitalised name (cruzr): drop or merge into the common word.

## Every `# question` line

The question lines are in `s23-flagged/questions.txt` (21 lines) and `s23-unflagged/questions.txt` (17 lines),
reproduced below.

### s23-flagged
```
# question auto-percepción: merge target autopercepción assumed to be the standard spelling
# question cereso: acronym used as a common noun in Mexico, but many examples are a specific prison number; kept as the generic word
# question cereso: mostly capitalised acronym (CERESO) for Mexican prisons; kept as acronym used as common noun, could be argued as institution names
# question cetera: "et" half is not in this batch; if "et" appears separately it should drop as the second half of the split
# question cetera: merged into etcétera, but it could also be treated as half of a split loan.
# question chorotega: the examples are mostly capitalised and refer to the people or a king, so the ethnonym ruling is applied loosely.
# question cruzr: no examples; Cruz is capitalised throughout, so it may be mostly the name (Santa Cruz) and drop could be right if the common-word reading is under a third
# question cruzr: the text is always Cruz, which is likely a surname or place name and not the verb cruzar; merged into cruz, but drop may be better.
# question diakonia: Could be a theological loan, but I merged it into the adapted diaconía.
# question ex-agente: merge target exagente assumed (RAE joins ex- to the word); confirm it is the intended lemma
# question ex-agente: the target "ex agente" assumes the usual separate-word spelling of ex; confirm
# question güira: only about 39% lowercase, the rest mostly place names; kept as the instrument
# question güira: the examples are place names; I kept it for the instrument or tree sense, which may be under a third of the occurrences
# question nocilla: brand used generically in Spain; kept, but the adapted spelling (nocilla) may be preferred over the capitalised brand
# question pijao: capitalised in 86% and tied to a named people (Nasa/Guambianos context); rules say lowercase ethnonyms keep, but mostly capitalised here so dropped.
# question pijao: ethnonym is capitalised in 86% of text and treated as a proper name; rules keep lowercase ethnonyms (hutíes) but this is mostly capitalised, so dropped.
# question portazgo: place-name use (Portazgo district, Posada) may be sizeable; kept as common word since 27% non-capitalised plus capitalised toll uses unclear
# question solidos: could be unaccented sólidos, but capitalised name use dominates, so dropped
# question vagos: Real plural of vago is possible, but the examples show the town name and all-caps spam, so I dropped it.
# question cruzr: a broken lemma whose surface forms are all capitalised names; is drop right, rather than merging into the real common word (cruz)?
# question solidos: do all-caps occurrences (likely headings such as RESIDUOS SOLIDOS) count toward the one-third real-reading threshold?
```

### s23-unflagged
```
# question bús: could instead merge into bus if that is the listed form; no examples shown, chose autobús as the fuller listed word.
# question coachee: coach is established, but coachee appears only in coaching jargon; dropped, could be argued as a loan.
# question coachee: coach is established, but coachee only appears in coaching jargon; dropped as not yet established
# question dextroanfetamina: borderline between common generic drug and specialist drug; kept as an adapted form.
# question dextroanfetamina: generic ADHD drug, borderline between common and specialist; kept as an adapted name
# question galano: galano is a real Spanish adjective (elegant), but the examples look like hotel/place names; dropped because the real reading seems under a third
# question galano: galano/galana is a real adjective (elegant), but most examples are the proper name Galana; dropped because the real reading is under a third.
# question jijiji: typed laughter is not covered by the interjection rule (vaya, hala, ojalá); dropped as a web-chat artefact
# question multiventana: a real Spanish tech term (Android "modo multiventana") but niche; dropped as doubtful
# question pizzicato: sample example is an agency name; kept for the musical term, but the real reading may be under a third of the examples
# question pizzicato: some examples are a company name; kept because the musical term is established in Spanish
# question recebar: recebar and recebo are real Spanish words (gravel), but the forms are mostly Portuguese-looking and no examples were available.
# question recebar: recebar is a real Spanish verb (to gravel), but the written forms and examples look mostly Portuguese; dropped as the minority reading
# question rotocultivo: capitalised product-listing only (probably from rotocultivador); no obvious merge target, so dropped
# question wayang: appears in Spanish cultural and UNESCO texts; dropped as not established for a general learner
# question jijiji: should typed laughter (jaja, jeje, jiji, jojo) ever be kept as interjections, or always dropped as repeated tokens?
# question recebar: split by form: recebo, Recebo -> recebo (noun: jamón de recebo, gravel/fill); recebe and receba are probably Portuguese, so drop those or leave them under recebar?
```
