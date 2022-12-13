import argparse

from nltk.stem import PorterStemmer
from pymorphy2 import MorphAnalyzer
import nltk
from razdel import tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')


def parse_args():
    parser = argparse.ArgumentParser(description='text tokenizer')
    parser.add_argument('filename', type=str, help='the filename of the source text')
    parser.add_argument('--lang', required=True,
                        choices=['ru', 'en'])
    parser.add_argument('--lemmatized', action='store_true', help='also print the normal form of words')
    parser.add_argument('--pos', action='store_true',
                        help='also print which part of speech the words belong to')
    return parser.parse_args()


def print_tokens(_processed: list):
    for _token in _processed:
        print(_token)


def print_lemmatized(_tokens: list, lang: str):
    print('\n---------------------------------\n')
    if lang == 'ru':
        morph = MorphAnalyzer(lang=lang)
        for _token in _tokens:
            print(morph.parse(_token)[0].normal_form)
    elif lang == 'en':
        stemmer = PorterStemmer()
        for _token in _tokens:
            print(stemmer.stem(_token))


def print_pos(_tokens: list, lang: str):
    if lang == 'ru':
        morph = MorphAnalyzer(lang=lang)
        print('\n---------------------------------\n')
        for _token in _tokens:
            print(str(morph.parse(_token)[0].tag).split(',')[0])
    elif lang == 'en':
        tagged = nltk.pos_tag(_tokens)
        for tag in tagged:
            print(tag[1])


if __name__ == "__main__":
    args = parse_args()
    with open(args.filename, encoding='UTF-8') as file:
        text = file.read()

        if args.lang == 'ru':
            tokens = [token.text for token in list(tokenize(text))]
        elif args.lang == 'en':
            tokens = nltk.word_tokenize(text)

        print_tokens(tokens)

        if args.lemmatized:
            print_lemmatized(tokens, args.lang)

        if args.pos:
            print_pos(tokens, args.lang)