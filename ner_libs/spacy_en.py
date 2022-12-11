import spacy


def get_entities(text: str):
    nlp = spacy.load('en_core_web_sm')
    processed = nlp(text)
    entities = [[ent.text, ent.label_] for ent in processed.ents]
    return entities
