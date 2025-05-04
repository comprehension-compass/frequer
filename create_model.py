def create_model(lang):
    import spacy

    if lang == "es":    
        print("Intializing Spanish model with modified lookups...")
        nlp = spacy.blank(lang)
        nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
        nlp.initialize()
        # edit lookup table to correct
        lemmatizer = nlp.get_pipe('lemmatizer')
        lemma_lookup = lemmatizer.lookups.get_table('lemma_lookup')
        lemma_lookup["para"] = ["para"]
        lemma_lookup["línea"] = ["línea"]
        lemma_lookup["líneas"] = ["línea"]
        lemma_lookup["segundo"] = ["segundo"]
        lemma_lookup["segunda"] = ["segundo"]
        lemma_lookup["segundos"] = ["segundo"]
        lemma_lookup["segundas"] = ["segundo"]
        lemma_lookup["estrella"] = ["estrella"]
        lemma_lookup["estrellas"] = ["estrella"]
        lemma_lookup["hemos"] = ["haber"]
        lemma_lookup["colores"] = ["color"]
        lemma_lookup["sitio"] = ["sitio"]
        lemma_lookup["así"] = ["así"]
        lemma_lookup["cerca"] = ["cerca"]
        lemma_lookup["mano"] = ["mano"]
        lemma_lookup["largo"] = ["largo"]
        lemma_lookup["cinco"] = ["cinco"]
        lemma_lookup["madera"] = ["madera"]
        lemma_lookup["tales"] = ["tal"]
        lemma_lookup["viaje"] = ["viaje"]
        lemma_lookup["vuelo"] = ["vuelo"]
        lemma_lookup["nos"] = ["nos"]
        lemma_lookup["lo"] = ["lo"]
        lemma_lookup["los"] = ["el"]
        lemma_lookup["las"] = ["el"]
        lemma_lookup["la"] = ["el"]
        lemma_lookup["casa"] = ["casa"]
        lemma_lookup["os"] = ["os"]
        lemma_lookup["sis"] = ["sis"]
        lemma_lookup["uno"] = ["uno"]
        lemma_lookup["aes"] = ["aes"]
        lemma_lookup["sobre"] = ["sobre"]
        lemma_lookup["uso"] = ["uso"]
        lemma_lookup["como"] = ["como"]
        lemmatizer.cache = {}   

        return nlp