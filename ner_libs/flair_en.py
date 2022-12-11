from flair.data import Sentence
from flair.models import SequenceTagger


def get_entities(text: str):
    sentence = Sentence(text)
    tagger = SequenceTagger.load('ner')
    tagger.predict(sentence)
    entities = [[entity.text, entity.tag] for entity in sentence.get_spans('ner')]
    return entities
