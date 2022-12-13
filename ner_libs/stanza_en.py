from stanza import Pipeline


def get_entities(text: str):
    nlp = Pipeline(lang='en', processors='tokenize,ner')
    processed = nlp(text)
    entities = [[ent.text, ent.type] for ent in processed.ents]
    return entities
