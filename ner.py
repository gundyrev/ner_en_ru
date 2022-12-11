import argparse
import ner_libs.deeppavlov_ru
import ner_libs.deeppavlov_en
import ner_libs.spacy_en
import ner_libs.spacy_ru
import ner_libs.flair_en
import ner_libs.stanza_en
import ner_libs.stanza_ru
import ner_libs.natasha_ru


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='the filename of the source text')
    parser.add_argument('--lib', required=True,
                        choices=['deeppavlov_en', 'deeppavlov_ru', 'spacy_en', 'spacy_ru', 'flair_en', 'stanza_en',
                                 'stanza_ru', 'natasha_ru'])
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    with open(args.filename, encoding='UTF-8') as file:
        text = file.read()
        entities = eval(f'ner_libs.{args.lib}.get_entities("""{text}""")')
        for entity in entities:
            print(f'{entity[0]} - {entity[1]}')
