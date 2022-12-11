import stanza


def get_entities(text: str):
    nlp = stanza.Pipeline(lang='ru', processors='tokenize,ner')
    processed = nlp(text)
    entities = [[ent.text, ent.type] for ent in processed.ents]
    return entities
