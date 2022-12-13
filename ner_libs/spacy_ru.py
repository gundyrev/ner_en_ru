from spacy import load


def get_entities(text: str):
    nlp = load('ru_core_news_sm')
    processed = nlp(text)
    entities = [[ent.text, ent.label_] for ent in processed.ents]
    return entities
