# Review rules (the developer's; binding)

Honeyeater's Spanish frequency list (the top 20,000 lemmas a learner studies, counted from Spanish web text
and Tatoeba) is being cleaned. Each lemma below was flagged by an automatic heuristic. You decide what
happens to it. The flag says why it was sent; it is evidence, not a verdict.

**Decisions** (exactly one per lemma):
- `keep`: a real Spanish word (or an established loan) a learner would want on the list.
- `drop`: junk for a learner's list (see below).
- `merge:<lemma>`: a real word filed under a wrong or misspelt lemma, when the right Spanish lemma is
  obvious; give that lemma, written as Spanish writes it (e.g. `merge:indígena`, `merge:herpes`).

**Proper nouns** (flag `propn_band`):
- Countries, languages and major cities are learnable: `keep`.
- Other names drop: people, brands, companies, products, organisations, websites, smaller places.
- Common nouns stay: words the tagger mistook for names (kayak, rock, zoo, máster, hostel, safari, palma,
  cala, bingo, jaguar, margarita): `keep`.
- Acronyms: acronyms used as ordinary words in Spanish stay (IVA, ADN, ONG, PIB, VIH, PDF, TV, PC, USB, GPS,
  SMS, ONU): `keep`. Brand, company and organisation acronyms drop (HP, LG, IBM, BBC, FBI, DHL).
  Technical acronyms only specialists use (dll, ssl, xml, rgpd) drop: a learner would not study them.

**Foreign words** (flag `foreign`): drop English words that are not established in Spanish; keep loans
established enough that an English-speaking learner would want to know Spanish uses them (show, web, online,
marketing, chat, blog, email, low cost). Real Spanish words that look English stay (once, red, pie, sale).

**Shape** (flag `shape`): drop hyphenated web compounds (calidad-precio, salón-comedor), doubled words
(señorseñor) and fragments cut mid-word (jugabl). Keep established hyphenated words or loans (wi-fi, e-mail)
if a learner would study them.

**Citation** (flag `citation`, the lemma's spelling is never written as a word): usually a broken lemma.
`merge:` into the right lemma when it is obvious; otherwise `drop`.

**Low diversity** (flag `diversity`, concentrated in few documents): drop template or brand text; keep
real words.

When the rules don't settle a case, still decide, and add a line `# question <lemma>: <what is unclear>`.
