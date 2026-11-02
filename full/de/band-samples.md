# de band samples: which words sit at each level

From the cleaned list as it would load (exclusion list, 1,311 merges, three review rounds plus the developer's rulings of
2026-11-02: the 12 places and 10 institutions kept, ordinals above 30 and abbreviations dropped). Not a snapshot. Corpus: **451,548,754 tokens** (HPLT v2 deu_Latn 445.4M, Tatoeba 6.1M). Glosses are a reviewer's; a bracket ([name], [English], [not a word: ...]) marks a
lemma it judged not a real word. Names such as Sophos or VLC near 30k are flagged lemmas the review window had not
reached yet (35 inside the 30k); they would go through review before a build. A re-check of hyphenated compounds and of keeps whose earlier examples came from a
minority form is running and may change a few entries.

## Frequency per million tokens at kept ranks

| kept rank | de lemma there | de f | de per million | es per million | ja per million |
|---:|---|---:|---:|---:|---:|
| 5,000 | Prävention | 6,036 | 13.37 | 12.48 | - |
| 10,000 | anknüpfen | 2,216 | 4.91 | 3.14 | - |
| 20,000 | Erdboden | 820 | 1.82 | 0.58 | - |
| 25,000 | pensionieren | 596 | 1.32 | 0.31 | 1.53 |
| 30,000 | unternehmensintern | 461 | 1.02 | 0.19 | 1.10 |

es: frozen 105.7M-token counts (full-es band report: f 332 / 62 / 33 / 20 at 10k / 20k / 25k / 30k). ja: 689.7M tokens (full-ja band report, f at kept positions ~25,000 and ~30,000; 5k-20k not given there). At 30k German sits at ~1.0 per million, close to Japanese (~1.1) and five times Spanish (~0.19): de and ja were counted from four to six times more text, so their 30k words are about as frequent in running text as es's ~8k.

## 25 random kept lemmas, 0-10k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 733 | obwohl | SCONJ | 57,021 | 126.28 | although |
| 905 | Freude | NOUN | 46,949 | 103.97 | joy |
| 1,087 | mobil | ADJ | 39,111 | 86.62 | mobile |
| 1,415 | Prozess | NOUN | 30,332 | 67.17 | process; trial |
| 1,993 | schwach | ADJ | 20,369 | 45.11 | weak |
| 2,612 | teils | ADV | 14,715 | 32.59 | partly |
| 3,051 | Parlament | NOUN | 12,027 | 26.63 | parliament |
| 3,159 | Fett | NOUN | 11,466 | 25.39 | fat |
| 3,265 | Umzug | NOUN | 11,002 | 24.37 | move (relocation) |
| 3,326 | allzu | ADV | 10,764 | 23.84 | all too |
| 5,308 | grösser | ADJ | 5,554 | 12.30 | bigger [Swiss spelling of größer] |
| 6,180 | am liebsten | X | 4,483 | 9.93 | preferably; most of all |
| 6,640 | Dass | SCONJ | 4,048 | 8.96 | that (conjunction) [capitalised form] |
| 6,676 | Flirt | NOUN | 4,022 | 8.91 | flirt |
| 6,794 | bezaubern | ADJ | 3,920 | 8.68 | enchanting [not a word: adjective form of verb bezaubern; should be bezaubernd] |
| 7,250 | stornieren | VERB | 3,568 | 7.90 | to cancel |
| 7,650 | Bann | NOUN | 3,287 | 7.28 | spell; ban |
| 8,210 | Sauberkeit | NOUN | 2,953 | 6.54 | cleanliness |
| 8,453 | Wechselwirkung | NOUN | 2,827 | 6.26 | interaction |
| 8,951 | Festland | NOUN | 2,593 | 5.74 | mainland |
| 9,163 | Mittagspause | NOUN | 2,509 | 5.56 | lunch break |
| 9,258 | hüpfen | VERB | 2,473 | 5.48 | to hop |
| 9,282 | Staatsanwalt | NOUN | 2,463 | 5.45 | public prosecutor |
| 9,707 | Fußballer | NOUN | 2,308 | 5.11 | footballer |
| 9,805 | vollautomatisch | ADJ | 2,275 | 5.04 | fully automatic |

## 25 random kept lemmas, 10-20k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 10,063 | komplettieren | VERB | 2,198 | 4.87 | to complete |
| 10,328 | Limousine | NOUN | 2,125 | 4.71 | limousine; sedan |
| 11,144 | Medizinprodukt | NOUN | 1,907 | 4.22 | medical device |
| 11,208 | Heizkörper | NOUN | 1,889 | 4.18 | radiator |
| 11,623 | Versicherungsnehmer | NOUN | 1,799 | 3.98 | policyholder |
| 11,692 | Spoiler | NOUN | 1,782 | 3.95 | spoiler |
| 11,957 | Fachkräftemangel | NOUN | 1,723 | 3.82 | skilled-labour shortage |
| 12,038 | Typisch | NOUN | 1,704 | 3.77 | typical [capitalised, nominalised adjective] |
| 13,661 | Swimmingpool | NOUN | 1,423 | 3.15 | swimming pool |
| 14,693 | Vanillezucker | NOUN | 1,275 | 2.82 | vanilla sugar |
| 14,815 | Scannen | NOUN | 1,260 | 2.79 | scanning |
| 15,888 | Votum | NOUN | 1,138 | 2.52 | vote; verdict |
| 17,041 | Erziehungswissenschaft | NOUN | 1,031 | 2.28 | educational science |
| 17,149 | Konfigurator | NOUN | 1,022 | 2.26 | configurator |
| 17,473 | DVD-Player | PROPN | 995 | 2.20 | DVD player |
| 18,231 | prädestinieren | VERB | 938 | 2.08 | to predestine |
| 18,548 | Coronakrise | NOUN | 916 | 2.03 | coronavirus crisis |
| 18,624 | einbehalten | VERB | 910 | 2.02 | to withhold |
| 18,728 | Wickel | NOUN | 902 | 2.00 | compress; wrap |
| 18,889 | Steyr | NOUN | 892 | 1.98 | Steyr [name] |
| 18,929 | Seitenwechsel | NOUN | 890 | 1.97 | change of sides |
| 19,232 | ziel | ADJ | 871 | 1.93 | [not a word: truncated form of Ziel (goal) or ziel-] |
| 19,295 | Schattierung | NOUN | 866 | 1.92 | shading; nuance |
| 19,771 | Mrd | NOUN | 835 | 1.85 | billion (abbrev. Mrd.) |
| 19,837 | Zugänglichkeit | NOUN | 831 | 1.84 | accessibility |

## 25 random kept lemmas, 20-25k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 20,030 | WK | NOUN | 819 | 1.81 | [not a word: abbreviation WK, e.g. Weltkrieg / Wahlkreis] |
| 20,189 | Ausgeglichenheit | NOUN | 810 | 1.79 | balance; evenness |
| 20,716 | Einmischung | NOUN | 779 | 1.73 | interference |
| 20,766 | Meerjungfrau | NOUN | 776 | 1.72 | mermaid |
| 20,978 | Hefeteig | NOUN | 766 | 1.70 | yeast dough |
| 21,125 | Parship | NOUN | 758 | 1.68 | Parship [name] |
| 21,297 | Constantin | NOUN | 750 | 1.66 | Constantin [name] |
| 21,334 | wahrgenommen | ADJ | 749 | 1.66 | perceived |
| 21,881 | Nordlicht | NOUN | 722 | 1.60 | northern lights |
| 22,171 | Auffrischung | NOUN | 708 | 1.57 | refresher; refreshing |
| 22,195 | Petersen | NOUN | 707 | 1.57 | Petersen [name] |
| 22,224 | Kundenbedürfnis | NOUN | 706 | 1.56 | customer need |
| 22,235 | Ratenkauf | NOUN | 706 | 1.56 | instalment purchase |
| 22,463 | option | ADJ | 696 | 1.54 | [not a word: truncated form of optional / Option] |
| 22,640 | zischen | VERB | 688 | 1.52 | to hiss |
| 22,809 | Kleinod | NOUN | 680 | 1.51 | gem; treasure |
| 22,853 | abwählen | VERB | 679 | 1.50 | to deselect |
| 23,317 | Preisnachlass | NOUN | 658 | 1.46 | price reduction |
| 23,432 | unkritisch | ADJ | 654 | 1.45 | uncritical; unproblematic |
| 23,563 | Bauwirtschaft | NOUN | 648 | 1.44 | construction industry |
| 23,620 | Nachbargemeinde | NOUN | 646 | 1.43 | neighbouring municipality |
| 23,922 | innenliegend | ADJ | 634 | 1.40 | interior (lying inside) |
| 24,032 | Retina | PROPN | 630 | 1.40 | Retina [English/name: eye retina, Apple brand] |
| 24,325 | Entdecke | NOUN | 621 | 1.38 | [not a word: imperative form of entdecken (discover)] |
| 24,662 | Quinn | NOUN | 608 | 1.35 | Quinn [name] |

## 25 random kept lemmas, 25-30k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 25,379 | einsatzfähig | ADJ | 583 | 1.29 | ready for use; operational |
| 25,517 | Geldbuße | NOUN | 578 | 1.28 | fine |
| 25,753 | Reisedaten | NOUN | 570 | 1.26 | travel dates |
| 25,849 | Seniorenzentrum | NOUN | 567 | 1.26 | senior citizens' centre |
| 26,069 | po | PRON | 561 | 1.24 | [not a word: fragment, perhaps Latin/abbreviation] |
| 26,140 | Vorweg | NOUN | 559 | 1.24 | beforehand; in advance |
| 26,210 | ermäßigungen | NOUN | 557 | 1.23 | discounts [lowercase plural of Ermäßigung] |
| 26,314 | Informationszweck | NOUN | 553 | 1.22 | informational purpose |
| 26,336 | Konjunktiv | NOUN | 552 | 1.22 | subjunctive |
| 26,446 | Kletterwand | NOUN | 548 | 1.21 | climbing wall |
| 26,493 | flitzen | VERB | 547 | 1.21 | to dash |
| 26,522 | Vorlaufzeit | NOUN | 546 | 1.21 | lead time |
| 26,833 | zusammenfalten | VERB | 538 | 1.19 | to fold up |
| 27,102 | Wasseraufbereitung | NOUN | 530 | 1.17 | water treatment |
| 27,149 | Anmut | NOUN | 528 | 1.17 | grace; charm |
| 27,721 | buhlen | VERB | 514 | 1.14 | to woo |
| 27,742 | Jogge | NOUN | 513 | 1.14 | [not a word: broken form of Jogger or joggen; "Jogge"] |
| 28,048 | Bundesverdienstkreuz | NOUN | 505 | 1.12 | Federal Cross of Merit |
| 28,127 | position | ADJ | 504 | 1.12 | [not a word: truncated form of Position / positiv] |
| 28,618 | Azor | NOUN | 491 | 1.09 | Azor [name] |
| 28,756 | unfallfrei | ADJ | 489 | 1.08 | accident-free |
| 29,075 | Triathlet | NOUN | 481 | 1.07 | triathlete |
| 29,079 | Vorladung | NOUN | 481 | 1.07 | summons |
| 29,117 | Sperrfrist | NOUN | 480 | 1.06 | waiting period; blocking period |
| 29,983 | Zwischenmahlzeit | NOUN | 461 | 1.02 | snack between meals |

## Kept ranks 29,971-30,000 (consecutive)

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 29,971 | Sophos | PROPN | 461 | 1.02 | Sophos [name] |
| 29,972 | VLC | PROPN | 461 | 1.02 | VLC [name] |
| 29,973 | VR-Brille | NOUN | 461 | 1.02 | VR headset |
| 29,974 | Variabilität | NOUN | 461 | 1.02 | variability |
| 29,975 | Vermisste | NOUN | 461 | 1.02 | missing person |
| 29,976 | Verzweigung | NOUN | 461 | 1.02 | branching |
| 29,977 | Vordenker | NOUN | 461 | 1.02 | forward thinker; mastermind |
| 29,978 | Vorinstanz | NOUN | 461 | 1.02 | lower court |
| 29,979 | Wachsamkeit | NOUN | 461 | 1.02 | vigilance |
| 29,980 | Warburg | PROPN | 461 | 1.02 | Warburg [name] |
| 29,981 | Weltreligion | NOUN | 461 | 1.02 | world religion |
| 29,982 | Werbefläche | NOUN | 461 | 1.02 | advertising space |
| 29,983 | Zwischenmahlzeit | NOUN | 461 | 1.02 | snack between meals |
| 29,984 | alternate | ADJ | 461 | 1.02 | alternate [English] |
| 29,985 | altertümlich | ADJ | 461 | 1.02 | antiquated |
| 29,986 | aufstecken | VERB | 461 | 1.02 | to put up; to pin up |
| 29,987 | begrün | ADJ | 461 | 1.02 | [not a word: broken form of begrünen (to green)] |
| 29,988 | dramaturgisch | ADJ | 461 | 1.02 | dramaturgical |
| 29,989 | ersteinmal | ADV | 461 | 1.02 | first of all [misspelling of erst einmal] |
| 29,990 | europa | ADJ | 461 | 1.02 | [not a word: lowercase name Europa used as adjective] |
| 29,991 | fettreich | ADJ | 461 | 1.02 | rich in fat |
| 29,992 | frostfrei | ADJ | 461 | 1.02 | frost-free |
| 29,993 | hinlänglich | ADJ | 461 | 1.02 | sufficient |
| 29,994 | hinreißend | ADJ | 461 | 1.02 | captivating; ravishing |
| 29,995 | ibn | ADP | 461 | 1.02 | [not a word: Arabic "ibn" (son of), a name particle] |
| 29,996 | intakte | ADJ | 461 | 1.02 | intact [inflected form of intakt] |
| 29,997 | stülpen | VERB | 461 | 1.02 | to slip over; to put on |
| 29,998 | trau | VERB | 461 | 1.02 | [not a word: broken form of trauen or imperative of "trau"] |
| 29,999 | umspielen | VERB | 461 | 1.02 | to play around; to lap around |
| 30,000 | unternehmensintern | ADJ | 461 | 1.02 | internal to a company |

## 15 random kept lemmas, 30-35k (what a deeper cut would add)

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 30,305 | Zerstörer | NOUN | 455 | 1.01 | destroyer |
| 32,337 | Sherlock Holmes | PROPN | 421 | 0.93 | Sherlock Holmes [name] |
| 32,414 | Weinregion | NOUN | 420 | 0.93 | wine region |
| 32,861 | Brass | PROPN | 412 | 0.91 | Brass [name] |
| 33,399 | Ausritt | NOUN | 404 | 0.89 | ride out |
| 33,546 | Lesebrille | NOUN | 402 | 0.89 | reading glasses |
| 33,551 | Nachrichtensendung | NOUN | 402 | 0.89 | news broadcast |
| 33,591 | verifiziert | ADJ | 402 | 0.89 | verified |
| 33,765 | Sopran | PROPN | 399 | 0.88 | soprano |
| 33,853 | kanalisieren | VERB | 398 | 0.88 | to channel |
| 33,969 | Siegtreffer | NOUN | 396 | 0.88 | winning goal |
| 34,144 | wald | ADV | 394 | 0.87 | [not a word: Wald without capital, or fragment] |
| 34,336 | aufblähen | VERB | 391 | 0.87 | to bloat; to inflate |
| 34,452 | Weltregierung | NOUN | 389 | 0.86 | world government |
| 34,510 | Vocals | NOUN | 388 | 0.86 | vocals [English] |
