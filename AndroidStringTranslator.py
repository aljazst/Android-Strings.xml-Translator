import os
import argparse
from google.cloud import translate_v2 as translate
import xml.etree.ElementTree as ET

# Enter the path to your google cloud key
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\yourmom\Desktop\Python\AndroidTranslate\AndroidCloudTranslateKey.json"


def list_languages():
    """Lists all available languages."""

    translate_client = translate.Client()

    results = translate_client.get_languages()

    for language in results:
        print(u"{name} ({language})".format(**language))


def create_directory_if_not_exists(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    return os.path.abspath(os.getcwd()+"\\" + directory_name)


def translateFile():
    INPUT_FILE = input(
        "Enter the name of the input file: [default: strings.xml] ")
    if not INPUT_FILE:
        INPUT_FILE = "strings.xml"
        print(INPUT_FILE)

    INPUT_LANGUAGE = input("Enter source language: [default: sl] ")
    if not INPUT_LANGUAGE:
        INPUT_LANGUAGE = "sl"
        print(INPUT_LANGUAGE)

    OUTPUT_LANGUAGE = input("Enter output language: [default: en] ")
    if not OUTPUT_LANGUAGE:
        OUTPUT_LANGUAGE = "en"
        print(OUTPUT_LANGUAGE)

    out_file_name = "values-" + OUTPUT_LANGUAGE

    OUTFILE = create_directory_if_not_exists(out_file_name) + "\\strings.xml"

    translate_client = translate.Client()

    tree = ET.parse(INPUT_FILE)
    root = tree.getroot()

    print("\n\n=====================TRANSLATING=====================\n\n")
    print("\n\nTranslating from " + INPUT_LANGUAGE +
          " to " + OUTPUT_LANGUAGE+" ...\n\n")

    # strings
    for string in root.iter('string'):
        isTranslatable = string.get('translatable')
        if isTranslatable == 'false':
            continue
        string.text = str(translate_client.translate(
            string.text, target_language=OUTPUT_LANGUAGE).get("translatedText"))

    # string-array
    for string_array in root.findall('string-array'):
        isTranslatable = string_array.get('translatable')
        if isTranslatable == 'false':
            continue
        for item in string_array.findall('item'):
            item.text = str(translate_client.translate(
                item.text, target_language=OUTPUT_LANGUAGE).get("translatedText"))

   # plurals
    for plurals in root.findall('plurals'):
        isTranslatable = plurals.get('translatable')
        if isTranslatable == 'false':
            continue
        for item in plurals.findall('item'):
            item.text = str(translate_client.translate(
                item.text, target_language=OUTPUT_LANGUAGE).get("translatedText"))

    tree.write(OUTFILE, encoding='utf-8')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command")

    list_languages_parser = subparsers.add_parser(
        "list-languages", help=list_languages.__doc__)

    testing_parser = subparsers.add_parser(
        "translateFile", help=translateFile.__doc__)

    args = parser.parse_args()

    if args.command == "list-languages":
        list_languages()
    elif args.command == "translateFile":
        translateFile()
