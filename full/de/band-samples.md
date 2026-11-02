# de band samples: which words sit at each level

From the cleaned list as it would load (exclusion list, 1,311 merges, three review rounds plus the developer's rulings of
2026-11-02: the 12 places and 10 institutions kept, ordinals above 30 and abbreviations dropped; round 4 re-judged 165 hyphenated compounds and re-checked 317
keeps). Not a snapshot. Corpus: **451,548,754 tokens** (HPLT v2 deu_Latn 445.4M, Tatoeba 6.1M). Glosses are a reviewer's; a bracket ([name], [English], [not a word: ...]) marks a
lemma it judged not a real word. Names such as Sophos or VLC near 30k are flagged lemmas the review window had not
reached yet (19 inside the 30k); they would go through review before a build.

## Frequency per million tokens at kept ranks

| kept rank | de lemma there | de f | de per million | es per million | ja per million |
|---:|---|---:|---:|---:|---:|
| 5,000 | befindlich | 6,035 | 13.37 | 12.48 | - |
| 10,000 | Jugendamt | 2,215 | 4.91 | 3.14 | - |
| 20,000 | Wegbegleiter | 821 | 1.82 | 0.58 | - |
| 25,000 | Zählung | 598 | 1.32 | 0.31 | 1.53 |
| 30,000 | Spaces | 462 | 1.02 | 0.19 | 1.10 |

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
| 5,308 | kraftvoll | ADJ | 5,552 | 12.30 | powerful, vigorous |
| 6,180 | Bodensee | PROPN | 4,481 | 9.92 | Lake Constance |
| 6,640 | Gift | NOUN | 4,048 | 8.96 | poison |
| 6,676 | lächerlich | ADJ | 4,022 | 8.91 | ridiculous |
| 6,794 | unerlässlich | ADJ | 3,920 | 8.68 | essential, indispensable |
| 7,250 | Aminosäure | NOUN | 3,567 | 7.90 | amino acid |
| 7,650 | Süßigkeit | NOUN | 3,287 | 7.28 | sweet, candy |
| 8,210 | Sauberkeit | NOUN | 2,953 | 6.54 | cleanliness |
| 8,453 | Wechselwirkung | NOUN | 2,827 | 6.26 | interaction |
| 8,951 | Festland | NOUN | 2,593 | 5.74 | mainland |
| 9,163 | interagieren | VERB | 2,509 | 5.56 | to interact |
| 9,258 | Einspruch | NOUN | 2,472 | 5.47 | objection |
| 9,282 | ergattern | VERB | 2,463 | 5.45 | to snag, to get hold of |
| 9,707 | frühstücken | VERB | 2,308 | 5.11 | to have breakfast |
| 9,805 | Befürchtung | NOUN | 2,274 | 5.04 | fear, apprehension |

## 25 random kept lemmas, 10-20k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 10,063 | mies | ADJ | 2,198 | 4.87 | lousy, rotten |
| 10,328 | app | ADJ | 2,125 | 4.71 | app [English] |
| 11,144 | Varize | NOUN | 1,907 | 4.22 | varicose vein |
| 11,208 | Sozialhilfe | NOUN | 1,889 | 4.18 | social welfare |
| 11,623 | Versicherungsnehmer | NOUN | 1,799 | 3.98 | policyholder |
| 11,692 | Basics | NOUN | 1,781 | 3.94 | basics [English] |
| 11,957 | dieMehr | NOUN | 1,723 | 3.82 | the more [not a word: article fused with Mehr] |
| 12,038 | e-mail | NOUN | 1,704 | 3.77 | email [English] |
| 13,661 | Swimmingpool | NOUN | 1,423 | 3.15 | swimming pool |
| 14,693 | Dow | NOUN | 1,275 | 2.82 | Dow (Jones index) [name] |
| 14,815 | Minijob | NOUN | 1,260 | 2.79 | mini job (low-paid part-time job) |
| 15,888 | Widerstandsfähigkeit | NOUN | 1,139 | 2.52 | resilience |
| 17,041 | Zustellbett | NOUN | 1,032 | 2.29 | extra bed, folding guest bed |
| 17,149 | Reihenhaus | NOUN | 1,023 | 2.27 | terraced house |
| 17,473 | angefertigt | ADJ | 996 | 2.21 | made, manufactured |
| 18,231 | vertagen | VERB | 939 | 2.08 | to adjourn, to postpone |
| 18,548 | Nut | NOUN | 917 | 2.03 | groove, slot |
| 18,624 | symptomatisch | ADJ | 911 | 2.02 | symptomatic |
| 18,728 | Baugebiet | NOUN | 902 | 2.00 | development area |
| 18,889 | verdampfen | VERB | 893 | 1.98 | to evaporate |
| 18,929 | Bewerbungsprozess | NOUN | 890 | 1.97 | job application process |
| 19,232 | Vergaser | NOUN | 871 | 1.93 | carburettor |
| 19,295 | WWW | PROPN | 867 | 1.92 | WWW [English] |
| 19,771 | ausspucken | VERB | 836 | 1.85 | to spit out |
| 19,837 | VA | NOUN | 832 | 1.84 | VA [name] |

## 25 random kept lemmas, 20-25k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 20,030 | Corona-Zeit | NOUN | 819 | 1.81 | Covid era |
| 20,189 | Mechatroniker | NOUN | 811 | 1.80 | mechatronics technician |
| 20,716 | Brotzeit | NOUN | 780 | 1.73 | Bavarian snack break |
| 20,766 | Bergtour | NOUN | 777 | 1.72 | mountain hike |
| 20,978 | Stundenlohn | NOUN | 767 | 1.70 | hourly wage |
| 21,125 | Rattan | PROPN | 759 | 1.68 | rattan |
| 21,297 | Samt | NOUN | 751 | 1.66 | velvet |
| 21,334 | Antlitz | NOUN | 749 | 1.66 | countenance, face |
| 21,881 | Reiseroute | NOUN | 723 | 1.60 | itinerary |
| 22,171 | GE | NOUN | 709 | 1.57 | GE [name] |
| 22,195 | Hohn | NOUN | 708 | 1.57 | scorn, mockery |
| 22,224 | Verlobung | NOUN | 707 | 1.57 | engagement |
| 22,235 | Ausnahmeregelung | NOUN | 706 | 1.56 | exemption rule |
| 22,463 | gebieten | VERB | 697 | 1.54 | to command, to dictate |
| 22,640 | übermächtig | ADJ | 689 | 1.53 | overpowering |
| 22,809 | Liebende | NOUN | 681 | 1.51 | lovers |
| 22,853 | verschlüsselt | ADJ | 680 | 1.51 | encrypted |
| 23,317 | Verfehlung | NOUN | 659 | 1.46 | misdeed, offence |
| 23,432 | Cello | PROPN | 654 | 1.45 | cello |
| 23,563 | silberfarben | ADJ | 650 | 1.44 | silver-coloured |
| 23,620 | Steppe | NOUN | 647 | 1.43 | steppe |
| 23,922 | Musikunterricht | NOUN | 635 | 1.41 | music lessons |
| 24,032 | Umgebungstemperatur | NOUN | 631 | 1.40 | ambient temperature |
| 24,325 | Datentyp | NOUN | 622 | 1.38 | data type |
| 24,662 | Menschheitsgeschichte | NOUN | 609 | 1.35 | human history |

## 25 random kept lemmas, 25-30k

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 25,379 | Auffassungsgabe | NOUN | 584 | 1.29 | grasp, quickness of understanding |
| 25,517 | vater | ADJ | 580 | 1.28 | father [not a word: lowercase Vater] |
| 25,753 | Berufskraftfahrer | NOUN | 571 | 1.26 | professional driver |
| 25,849 | hammer | ADJ | 569 | 1.26 | hammer [not a word: lowercase Hammer] |
| 26,069 | Gesundheitsproblem | NOUN | 562 | 1.24 | health problem |
| 26,140 | Lymphdrainage | NOUN | 560 | 1.24 | lymphatic drainage |
| 26,210 | Präsidentschaftskandidat | NOUN | 558 | 1.24 | presidential candidate |
| 26,314 | drängend | ADJ | 555 | 1.23 | pressing, urgent |
| 26,336 | Innentür | NOUN | 554 | 1.23 | interior door |
| 26,446 | Lippenstifte | NOUN | 550 | 1.22 | lipsticks |
| 26,493 | geweiht | ADJ | 549 | 1.22 | consecrated |
| 26,522 | pack | VERB | 548 | 1.21 | pack [not a word: imperative stem or English] |
| 26,833 | Puzzles | NOUN | 539 | 1.19 | puzzles |
| 27,102 | Glitter | NOUN | 531 | 1.18 | glitter |
| 27,149 | Lieblingsrezept | NOUN | 530 | 1.17 | favourite recipe |
| 27,721 | Grundsteinlegung | NOUN | 515 | 1.14 | laying of the foundation stone |
| 27,742 | mondän | ADJ | 515 | 1.14 | chic, sophisticated |
| 28,048 | Monsieur | NOUN | 507 | 1.12 | Monsieur, Mr (French) |
| 28,127 | Geschenkpapier | NOUN | 505 | 1.12 | wrapping paper |
| 28,618 | Gruppenreisen | NOUN | 493 | 1.09 | group trips |
| 28,756 | Ohrhörer | NOUN | 490 | 1.09 | earphones |
| 29,075 | rlich | ADJ | 483 | 1.07 | -rlich [not a word: broken fragment] |
| 29,079 | zukunftsträchtig | ADJ | 483 | 1.07 | promising for the future |
| 29,117 | hauswirtschaftlich | ADJ | 482 | 1.07 | home economics (adj.) |
| 29,983 | Harms | PROPN | 462 | 1.02 | Harms [name] |

## Kept ranks 29,971-30,000 (consecutive)

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 29,971 | Betätige | NOUN | 462 | 1.02 | operate [not a word: truncated imperative or form of betätigen] |
| 29,972 | Blöd | NOUN | 462 | 1.02 | stupid [not a word: capitalised blöd] |
| 29,973 | Bombenangriff | NOUN | 462 | 1.02 | bombing raid |
| 29,974 | Brotaufstrich | NOUN | 462 | 1.02 | spread (for bread) |
| 29,975 | Buchverlag | NOUN | 462 | 1.02 | book publisher |
| 29,976 | Civic | PROPN | 462 | 1.02 | Civic [name] |
| 29,977 | Colitis | PROPN | 462 | 1.02 | colitis |
| 29,978 | Erlernte | NOUN | 462 | 1.02 | what has been learned |
| 29,979 | Fachwerk | NOUN | 462 | 1.02 | half-timbering |
| 29,980 | Frontkamera | NOUN | 462 | 1.02 | front camera |
| 29,981 | Fürbitte | NOUN | 462 | 1.02 | intercession, intercessory prayer |
| 29,982 | GBP | PROPN | 462 | 1.02 | GBP, pound sterling |
| 29,983 | Harms | PROPN | 462 | 1.02 | Harms [name] |
| 29,984 | Hausverbot | NOUN | 462 | 1.02 | ban from premises |
| 29,985 | Hussein | PROPN | 462 | 1.02 | Hussein [name] |
| 29,986 | Landesbetrieb | NOUN | 462 | 1.02 | state-owned enterprise |
| 29,987 | Lizenzgeber | NOUN | 462 | 1.02 | licensor |
| 29,988 | Locarno | NOUN | 462 | 1.02 | Locarno [name] |
| 29,989 | Luxor | PROPN | 462 | 1.02 | Luxor [name] |
| 29,990 | Lösegeld | NOUN | 462 | 1.02 | ransom |
| 29,991 | Megabyte | NOUN | 462 | 1.02 | megabyte |
| 29,992 | Monats-Bahn | NOUN | 462 | 1.02 | monthly rail pass |
| 29,993 | PSV | PROPN | 462 | 1.02 | PSV [name] |
| 29,994 | Paketversand | NOUN | 462 | 1.02 | parcel shipping |
| 29,995 | Pistenkilometer | NOUN | 462 | 1.02 | kilometres of ski slope |
| 29,996 | Polarisierung | NOUN | 462 | 1.02 | polarization |
| 29,997 | Presseartikel | NOUN | 462 | 1.02 | press article |
| 29,998 | STIHL | PROPN | 462 | 1.02 | STIHL [name] |
| 29,999 | Shenzhen | PROPN | 462 | 1.02 | Shenzhen [name] |
| 30,000 | Spaces | PROPN | 462 | 1.02 | Spaces [English] |

## 15 random kept lemmas, 30-35k (what a deeper cut would add)

| kept rank | lemma | POS | f | per million | gloss |
|---:|---|---|---:|---:|---|
| 30,305 | Landessportbund | NOUN | 456 | 1.01 | state sports federation |
| 32,337 | Migrationspolitik | NOUN | 422 | 0.93 | migration policy |
| 32,414 | Schiffer | PROPN | 421 | 0.93 | boatman, skipper |
| 32,861 | Vorredner | NOUN | 414 | 0.92 | previous speaker |
| 33,399 | knöchern | ADJ | 406 | 0.90 | bony |
| 33,546 | Bestückung | NOUN | 403 | 0.89 | equipping, stocking |
| 33,551 | Darstellerin | NOUN | 403 | 0.89 | actress, performer |
| 33,591 | gesundheit | ADJ | 403 | 0.89 | bless you (health) [not a word: lowercase Gesundheit] |
| 33,765 | Nennleistung | NOUN | 400 | 0.89 | rated power |
| 33,853 | abdunkeln | VERB | 399 | 0.88 | to darken, to dim |
| 33,969 | Löscharbeit | NOUN | 397 | 0.88 | firefighting work |
| 34,144 | Zahntechniker | NOUN | 395 | 0.87 | dental technician |
| 34,336 | Tischlampe | NOUN | 392 | 0.87 | table lamp |
| 34,452 | Noel | PROPN | 390 | 0.86 | Noel [name] |
| 34,510 | Luftpumpe | NOUN | 389 | 0.86 | air pump |
