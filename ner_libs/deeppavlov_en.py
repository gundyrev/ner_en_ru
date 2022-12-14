from deeppavlov import build_model


def get_entities(text: str):
    ner_model = build_model('ner_collection3_bert', download=True)
    processed = ner_model([text])
    entities = []
    for i, item in enumerate(processed[0][0]):
        if processed[1][0][i] != 'O':
            entities.append([item, processed[1][0][i]])
    return entities
