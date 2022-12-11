from deeppavlov import build_model


def get_entities(text: str):
    ner_model = build_model('ner_rus_bert', download=True)
    processed = ner_model([text])
    entities = []
    for i in range(len(processed[0][0])):
        if processed[1][0][i] != 'O':
            entities.append([processed[0][0][i], processed[1][0][i]])
    return entities