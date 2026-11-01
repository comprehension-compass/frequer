# Rank samples, es (filtered ranking)

Developer request (2026-11-01): about 40 lemmas around each depth, to judge how deep the list needs to go. The ranking is the 105,726,244-token counts by raw frequency, after the exclusion list (`corpora/exclude/es.tsv`) and the proper-noun rule (dropped when capitalised in >= 50 % of running-text occurrences; learnable names kept). The first 50,000 are exactly `snapshots/es.json`. Ranks past 50,000 come from the full candidate ranking (200,000 candidates by frequency, 80,124 left after the filters; the candidate floor is frequency 3, so the 70k and 80k samples sit at that floor and their order there is arbitrary). POS is the majority UPOS. A multi-word unit (e.g. *sea como sea*) carries its own key.

## Around rank 20,000 (frequency 66)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 19,981 | extremeño | 66 | ADJ |
| 19,982 | fethiye | 66 | NOUN |
| 19,983 | funes | 66 | NOUN |
| 19,984 | gabardina | 66 | NOUN |
| 19,985 | garito | 66 | NOUN |
| 19,986 | gd | 66 | PROPN |
| 19,987 | glutamato | 66 | NOUN |
| 19,988 | grillar | 66 | NOUN |
| 19,989 | hacerlo | 66 | ADJ |
| 19,990 | hijoshijo | 66 | NOUN |
| 19,991 | histérico | 66 | ADJ |
| 19,992 | humanístico | 66 | ADJ |
| 19,993 | illustración | 66 | NOUN |
| 19,994 | imborrable | 66 | ADJ |
| 19,995 | imperecedero | 66 | ADJ |
| 19,996 | impregnación | 66 | NOUN |
| 19,997 | inconmensurable | 66 | ADJ |
| 19,998 | indigencia | 66 | NOUN |
| 19,999 | informador | 66 | NOUN |
| 20,000 | inmiscuir | 66 | VERB |
| 20,001 | insatisfactorio | 66 | ADJ |
| 20,002 | inusitado | 66 | ADJ |
| 20,003 | inviolable | 66 | ADJ |
| 20,004 | jugabl | 66 | ADJ |
| 20,005 | kanji | 66 | NOUN |
| 20,006 | lap | 66 | PROPN |
| 20,007 | linfa | 66 | NOUN |
| 20,008 | liofilizar | 66 | ADJ |
| 20,009 | macadamia | 66 | NOUN |
| 20,010 | manejabilidad | 66 | NOUN |
| 20,011 | manita | 66 | NOUN |
| 20,012 | medianamente | 66 | ADV |
| 20,013 | menos mal que | 66 | X |
| 20,014 | micronesia | 66 | PROPN |
| 20,015 | militarmente | 66 | ADV |
| 20,016 | motero | 66 | NOUN |
| 20,017 | neceser | 66 | NOUN |
| 20,018 | noronha | 66 | PROPN |
| 20,019 | notificarno | 66 | ADJ |
| 20,020 | obten | 66 | VERB |

## Around rank 30,000 (frequency 23)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 29,981 | rallycross | 23 | NOUN |
| 29,982 | ratonero | 23 | NOUN |
| 29,983 | razonabilidad | 23 | NOUN |
| 29,984 | reavivamiento | 23 | NOUN |
| 29,985 | recibio | 23 | VERB |
| 29,986 | reclinación | 23 | NOUN |
| 29,987 | recodar | 23 | NOUN |
| 29,988 | recopa | 23 | NOUN |
| 29,989 | redituable | 23 | ADJ |
| 29,990 | redon | 23 | PROPN |
| 29,991 | reflexividad | 23 | NOUN |
| 29,992 | reformatorio | 23 | NOUN |
| 29,993 | reguero | 23 | NOUN |
| 29,994 | reinterpretado | 23 | VERB |
| 29,995 | rellenador | 23 | NOUN |
| 29,996 | remiera | 23 | NOUN |
| 29,997 | representaciónes | 23 | NOUN |
| 29,998 | resaltante | 23 | ADJ |
| 29,999 | respetabilidad | 23 | NOUN |
| 30,000 | result | 23 | VERB |
| 30,001 | reversibilidad | 23 | NOUN |
| 30,002 | ricotta | 23 | NOUN |
| 30,003 | rinconcito | 23 | NOUN |
| 30,004 | rodal | 23 | ADJ |
| 30,005 | rompehielo | 23 | NOUN |
| 30,006 | rootkits | 23 | NOUN |
| 30,007 | sabiduria | 23 | NOUN |
| 30,008 | salinización | 23 | NOUN |
| 30,009 | salmonelosis | 23 | NOUN |
| 30,010 | salmorejo | 23 | NOUN |
| 30,011 | sarge | 23 | VERB |
| 30,012 | satanismo | 23 | NOUN |
| 30,013 | satsang | 23 | NOUN |
| 30,014 | sbt | 23 | PROPN |
| 30,015 | sección consular | 23 | ADJ |
| 30,016 | semicurado | 23 | ADJ |
| 30,017 | sequim | 23 | NOUN |
| 30,018 | servicio de parques nacionales | 23 | ADJ |
| 30,019 | setenil | 23 | ADJ |
| 30,020 | seudonimización | 23 | NOUN |

## Around rank 40,000 (frequency 11)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 39,981 | facilitarl | 11 | ADJ |
| 39,982 | factoria | 11 | PROPN |
| 39,983 | faders | 11 | NOUN |
| 39,984 | failed | 11 | PROPN |
| 39,985 | fakes | 11 | NOUN |
| 39,986 | fanart | 11 | NOUN |
| 39,987 | fanfarronear | 11 | VERB |
| 39,988 | fanpage | 11 | NOUN |
| 39,989 | farmaceutico | 11 | ADJ |
| 39,990 | fatalista | 11 | NOUN |
| 39,991 | featur | 11 | NOUN |
| 39,992 | femdom | 11 | PROPN |
| 39,993 | ferratas | 11 | ADJ |
| 39,994 | ferrería | 11 | NOUN |
| 39,995 | fertil | 11 | ADJ |
| 39,996 | fetch | 11 | VERB |
| 39,997 | fibroid | 11 | NOUN |
| 39,998 | filabres | 11 | NOUN |
| 39,999 | filled | 11 | PROPN |
| 40,000 | flashcards | 11 | NOUN |
| 40,001 | flipante | 11 | ADJ |
| 40,002 | floema | 11 | NOUN |
| 40,003 | floorball | 11 | PROPN |
| 40,004 | fluidificar | 11 | ADJ |
| 40,005 | fluticasone | 11 | VERB |
| 40,006 | fluída | 11 | VERB |
| 40,007 | forfour | 11 | ADJ |
| 40,008 | fotografica | 11 | PROPN |
| 40,009 | frame-rate | 11 | NOUN |
| 40,010 | frecuencial | 11 | ADJ |
| 40,011 | frigorífico-nevera | 11 | NOUN |
| 40,012 | frisio | 11 | ADJ |
| 40,013 | frugalidad | 11 | NOUN |
| 40,014 | frutofruto | 11 | NOUN |
| 40,015 | fucks | 11 | ADJ |
| 40,016 | fuerte rojo | 11 | ADJ |
| 40,017 | fulguración | 11 | NOUN |
| 40,018 | fumeta | 11 | NOUN |
| 40,019 | fundante | 11 | ADV |
| 40,020 | fuí | 11 | VERB |

## Around rank 50,000 (frequency 7)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 49,981 | roccia | 7 | NOUN |
| 49,982 | rodiado | 7 | ADJ |
| 49,983 | rodiano | 7 | NOUN |
| 49,984 | roll-off | 7 | PROPN |
| 49,985 | rollerball | 7 | PROPN |
| 49,986 | rolltube | 7 | VERB |
| 49,987 | romanticas | 7 | ADJ |
| 49,988 | romanza | 7 | NOUN |
| 49,989 | romesco | 7 | ADJ |
| 49,990 | ronroneo | 7 | NOUN |
| 49,991 | roode | 7 | NOUN |
| 49,992 | rooting | 7 | NOUN |
| 49,993 | rosegal | 7 | NOUN |
| 49,994 | rostizados | 7 | ADJ |
| 49,995 | roti | 7 | PROPN |
| 49,996 | rotoscopia | 7 | ADJ |
| 49,997 | rottentomatoes | 7 | NOUN |
| 49,998 | rougemont | 7 | NOUN |
| 49,999 | routeres | 7 | NOUN |
| 50,000 | rte-t | 7 | NOUN |
| 50,001 | rtsp | 7 | PROPN |
| 50,002 | rubble | 7 | ADJ |
| 50,003 | rudraksha | 7 | NOUN |
| 50,004 | ruffle | 7 | NOUN |
| 50,005 | ruivo | 7 | ADJ |
| 50,006 | rula | 7 | NOUN |
| 50,007 | rumiación | 7 | NOUN |
| 50,008 | ruxolitinib | 7 | NOUN |
| 50,009 | rxpense | 7 | NOUN |
| 50,010 | rydal | 7 | PROPN |
| 50,011 | sabalito | 7 | NOUN |
| 50,012 | sabanero | 7 | PROPN |
| 50,013 | saborizadas | 7 | ADJ |
| 50,014 | saborizados | 7 | ADJ |
| 50,015 | saciaos | 7 | VERB |
| 50,016 | sacrifícalo | 7 | VERB |
| 50,017 | sacúdanse | 7 | VERB |
| 50,018 | sadhus | 7 | NOUN |
| 50,019 | safeq | 7 | ADJ |
| 50,020 | safiro | 7 | PROPN |

## Around rank 60,000 (frequency 5)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 59,981 | transcluida | 5 | ADJ |
| 59,982 | transcripto | 5 | NOUN |
| 59,983 | transcriptoma | 5 | NOUN |
| 59,984 | transeje | 5 | VERB |
| 59,985 | transepidérmica | 5 | ADJ |
| 59,986 | transf | 5 | NOUN |
| 59,987 | transfiéralo | 5 | NOUN |
| 59,988 | transfiérelo | 5 | ADJ |
| 59,989 | transformacion | 5 | NOUN |
| 59,990 | transformista | 5 | ADJ |
| 59,991 | transgresivo | 5 | ADJ |
| 59,992 | transhistórico | 5 | ADJ |
| 59,993 | transilvano | 5 | ADJ |
| 59,994 | transitabilidad | 5 | NOUN |
| 59,995 | transitividad | 5 | NOUN |
| 59,996 | translucent | 5 | PROPN |
| 59,997 | transmi | 5 | NOUN |
| 59,998 | transnacionalismo | 5 | NOUN |
| 59,999 | transnacionalización | 5 | NOUN |
| 60,000 | transpondor | 5 | NOUN |
| 60,001 | transportecasa | 5 | NOUN |
| 60,002 | trapa | 5 | NOUN |
| 60,003 | trasdós | 5 | NOUN |
| 60,004 | trasladarno | 5 | ADJ |
| 60,005 | trasluchada | 5 | NOUN |
| 60,006 | trasluz | 5 | NOUN |
| 60,007 | trasporta | 5 | VERB |
| 60,008 | trasuntar | 5 | NOUN |
| 60,009 | tratador | 5 | NOUN |
| 60,010 | tratamientode | 5 | NOUN |
| 60,011 | travail | 5 | NOUN |
| 60,012 | travessa | 5 | NOUN |
| 60,013 | travoprost | 5 | NOUN |
| 60,014 | trazodone | 5 | VERB |
| 60,015 | trebuchet | 5 | NOUN |
| 60,016 | tregging | 5 | VERB |
| 60,017 | trendelenburg | 5 | PROPN |
| 60,018 | trenet | 5 | NOUN |
| 60,019 | triamcinolona | 5 | NOUN |
| 60,020 | triamterene | 5 | VERB |

## Around rank 70,000 (frequency 3)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 69,981 | asegorese | 3 | VERB |
| 69,982 | asegqrese | 3 | VERB |
| 69,983 | asegur | 3 | NOUN |
| 69,984 | aseguradoecha | 3 | VERB |
| 69,985 | asegúralo | 3 | ADJ |
| 69,986 | asesoraro | 3 | ADJ |
| 69,987 | asesoriamiento | 3 | NOUN |
| 69,988 | asesorándote | 3 | VERB |
| 69,989 | asfar | 3 | NOUN |
| 69,990 | asgardiana | 3 | ADJ |
| 69,991 | ashkenazí | 3 | NOUN |
| 69,992 | ashleyink | 3 | NUM |
| 69,993 | ashton-under-lyne | 3 | NOUN |
| 69,994 | asháninkas | 3 | ADJ |
| 69,995 | asiaticas | 3 | ADJ |
| 69,996 | asilvestrado | 3 | ADJ |
| 69,997 | asincronismo | 3 | NOUN |
| 69,998 | asincrónicamente | 3 | ADV |
| 69,999 | asistiva | 3 | ADJ |
| 70,000 | asistolia | 3 | NOUN |
| 70,001 | askalo | 3 | ADJ |
| 70,002 | asministrador | 3 | NOUN |
| 70,003 | asociable | 3 | ADJ |
| 70,004 | asociador | 3 | NOUN |
| 70,005 | asol | 3 | NOUN |
| 70,006 | asomarno | 3 | ADJ |
| 70,007 | asopao | 3 | NOUN |
| 70,008 | aspre | 3 | NOUN |
| 70,009 | assemblea | 3 | NOUN |
| 70,010 | assetsfx | 3 | PUNCT |
| 70,011 | associado | 3 | ADJ |
| 70,012 | assunto | 3 | NOUN |
| 70,013 | asterismo | 3 | NOUN |
| 70,014 | astillador | 3 | ADJ |
| 70,015 | astra-mental | 3 | ADJ |
| 70,016 | astracán | 3 | NOUN |
| 70,017 | astralinas | 3 | ADJ |
| 70,018 | astrobiólogo | 3 | NOUN |
| 70,019 | astrodinámica | 3 | NOUN |
| 70,020 | astrométricas | 3 | ADJ |

## Around rank 80,000 (frequency 3)

| rank | lemma | frequency | POS |
|---:|---|---:|---|
| 79,981 | xnet | 3 | NOUN |
| 79,982 | xoloitzcuintle | 3 | NOUN |
| 79,983 | xov | 3 | NUM |
| 79,984 | xpdl | 3 | NOUN |
| 79,985 | xpl | 3 | PROPN |
| 79,986 | xsane | 3 | NOUN |
| 79,987 | xstrain | 3 | NUM |
| 79,988 | xthree | 3 | VERB |
| 79,989 | xtremio | 3 | PUNCT |
| 79,990 | xuz | 3 | NUM |
| 79,991 | xvideoslive | 3 | NUM |
| 79,992 | xvii-xviii | 3 | NUM |
| 79,993 | yaba | 3 | VERB |
| 79,994 | yacaré | 3 | NOUN |
| 79,995 | yadunath | 3 | PROPN |
| 79,996 | yagé | 3 | VERB |
| 79,997 | yahudita | 3 | NOUN |
| 79,998 | yakutat | 3 | PROPN |
| 79,999 | yambú | 3 | ADJ |
| 80,000 | yanulación | 3 | NOUN |
| 80,001 | yapa | 3 | NOUN |
| 80,002 | yappx | 3 | NOUN |
| 80,003 | yardage | 3 | NOUN |
| 80,004 | yato | 3 | NOUN |
| 80,005 | yellow-paw | 3 | PROPN |
| 80,006 | yellowmark | 3 | ADV |
| 80,007 | yerbatero | 3 | ADJ |
| 80,008 | yesquero | 3 | NOUN |
| 80,009 | yestadio | 3 | NOUN |
| 80,010 | yevethano | 3 | ADJ |
| 80,011 | yeyunostomía | 3 | NOUN |
| 80,012 | yezidis | 3 | NOUN |
| 80,013 | ygg | 3 | PUNCT |
| 80,014 | yin-yang | 3 | PROPN |
| 80,015 | yina | 3 | NOUN |
| 80,016 | yisraelita | 3 | NOUN |
| 80,017 | yno | 3 | PRON |
| 80,018 | yo-tú | 3 | ADJ |
| 80,019 | yo-yo-yo | 3 | ADV |
| 80,020 | yodación | 3 | NOUN |
