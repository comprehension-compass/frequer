# Depth comparison, es (15k-30k)

From the frozen 105.7M-token counts through every current filter: the exclusion list, accent merges, the
junk rules and the review decisions from rounds 1-2. Reviewed to about rank 20k; past that, flagged lemmas
are unreviewed.

**Split halves.** The 40 shards dealt alternately into two halves of about 53M tokens each, each half ranked
through the same filters.

| depth | frequency | median documents (of 138k) | ranks within ±2√f | halves agree on top-N | median rank difference between halves (p90) | flagged, unreviewed nearby |
|---|---:|---:|---:|---:|---:|---:|
| 10k | 332 | 317 | 1,053 | 97.8 % | 346 (899) | 0 % |
| 15k | 129 | 123 | 2,153 | 96.6 % | 782 (1,948) | 0 % |
| 20k | 63 | 60 | 4,462 | 94.4 % | 1,631 (4,107) | 12 % |
| 25k | 38 | 37 | 7,815 | 92.6 % | 2,664 (6,900) | 28 % |
| 30k | 25 | 24 | 12,977 | 90.5 % | 3,995 (10,194) | 32 % |

Each half has half the text, so its rank differences overstate the full list's noise by about √2. Divide the
column by about 1.4 for the full 105.7M tokens.

Random samples (±1.5k around each depth; [P] = tagged PROPN):

- **15k**: inconsútil, horrorizar, metastásico, poncho, fichar, pomada, vagabundo, fundamentalista,
  surcoreano, compulsivo, península ibérica, comicios, carpiano, retablo, coproducción, decrecer,
  pronunciamiento, dramaturgo, psicológicamente, ánodo, flagelar, impune, likes, honorífico
- **20k**: middleware, preciollamada, descalificación, hostelero, planteo, circadiano, interracial,
  sobrealimentación, manopla, ocultamiento, pokédex, confitar, nausear, dressup [P], medline [P],
  vicerrector, alistarse, dsa [P], hula [P], osact [P], poma [P], paleontología, políglota, uniformar
- **25k**: horadar, irreconocible, arrimar, caricaturista, macaco, reasegurar, caracteristicas,
  fitoquímico, bajo llave, cuadratura, apalear, inapelable, montagne [P], agni [P], infrastructura,
  precancerosas, trole, allegro [P], carrizo, comar, manténganse, reprocesamiento, ens [P], pied [P]
- **30k**: itw [P], serp [P], tofino, desacoplamiento, magnánimo, ostensible, represor, disquera, embragar,
  moba [P], perdonador [P], almendralejo [P], anonimizar, multianual, neuropsicología, subdirección,
  cajetilla, clindamicina, enuresis, gib, puntapié, actuante, motonieve, rinconcito
