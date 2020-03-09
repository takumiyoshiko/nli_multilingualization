# Imports the Google Cloud client library
from google.cloud import translate
import argparse
import os
import codecs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, type=str, help='path to input')
    parser.add_argument('--output', default=None, type=str, help='path to input')
    parser.add_argument('--target', required=True, type=str, help='path to input')
    args = parser.parse_args()

    # Instantiates a client
    translate_client = translate.Client()

    dic = {}
    # The text to translate
    with codecs.open(args.input, 'r', 'utf-8') as f:
        for text in f.readlines():
            translation = translate_client.translate(
            text,
            target_language=args.target)
            text.strip()
            translation['translatedText'].strip()
            if args.output:
                with open(args.output, "a") as out:
                    out.write(translation['translatedText'].encode('utf_8') + '\n')

if __name__ == '__main__':
    main()

