from spacy import load


def get_entities(text: str):
    nlp = load('en_core_web_sm')
    processed = nlp(text)
    entities = [[ent.text, ent.label_] for ent in processed.ents]
    return entities
