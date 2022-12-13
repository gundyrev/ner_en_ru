import argparse
import nltk
from nltk.stem import PorterStemmer
from pymorphy2 import MorphAnalyzer
from razdel import tokenize


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, help='the filename of the source text')
    parser.add_argument('--lang', required=True,
                        choices=['ru', 'en'], help='language of the source text')
    parser.add_argument('--tokenize', action='store_true', help='tokenize text and print all tokens')
    parser.add_argument('--lemmatize', action='store_true', help='print lemmatized tokens')
    parser.add_argument('--pos', action='store_true',
                        help='print which parts of speech the tokens belong to')
    return parser.parse_args()


def print_tokens(_processed: list):
    for _token in _processed:
        print(_token)
    print('\n---------------------------------\n')


def print_lemmatized(_tokens: list, lang: str):
    if lang == 'ru':
        morph = MorphAnalyzer(lang=lang)
        for _token in _tokens:
            print(morph.parse(_token)[0].normal_form)
    elif lang == 'en':
        stemmer = PorterStemmer()
        for _token in _tokens:
            print(stemmer.stem(_token))
    print('\n---------------------------------\n')


def print_pos(_tokens: list, lang: str):
    if lang == 'ru':
        morph = MorphAnalyzer(lang=lang)
        for _token in _tokens:
            print(str(morph.parse(_token)[0].tag).split(',')[0])
    elif lang == 'en':
        tagged = nltk.pos_tag(_tokens)
        for tag in tagged:
            print(tag[1])
    print('\n---------------------------------\n')


if __name__ == "__main__":
    args = parse_args()
    with open(args.filename, encoding='UTF-8') as file:
        text = file.read()

        if args.lang == 'ru':
            tokens = [token.text for token in list(tokenize(text))]
        elif args.lang == 'en':
            nltk.download('averaged_perceptron_tagger')
            nltk.download('punkt')
            tokens = nltk.word_tokenize(text)

        if args.tokenize:
            print_tokens(tokens)

        if args.lemmatize:
            print_lemmatized(tokens, args.lang)

        if args.pos:
            print_pos(tokens, args.lang)