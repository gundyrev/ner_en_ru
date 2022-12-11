from natasha import Doc, Segmenter, NewsEmbedding, NewsNERTagger


def get_entities(text: str):
    segmenter = Segmenter()
    embedding = NewsEmbedding()
    ner_tagger = NewsNERTagger(embedding)
    processed = Doc(text)
    processed.segment(segmenter)
    processed.tag_ner(ner_tagger)
    entities = [[span.text, span.type] for span in processed.spans]
    return entities
