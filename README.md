# Translator script for Android Strings.xml

Android-Strings.xml-Translator is a Python script that uses the Google Cloud Translation API to translate a whole .xml file to the desired language.

## Documentation

[The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html)

[argsparse](https://docs.python.org/3/library/argparse.html)

[Google Cloud Translation API](https://cloud.google.com/translate/docs/basic/quickstart)

## Installation

Use the package manager pip to install the needed libraries.

```bash
pip install google-cloud-translate
```

## Setup

This script uses the Google Cloud API, so you will first of all need a google service account [Google Cloud](https://cloud.google.com/).
Make a project and go to API & Services > Credentials in the menu.
Under create credentials you will heve to make a service account and later add a key in json format in the service account details page.

After you have your json file containing the key you can add the file path to the script.

```python
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\yourmom\Desktop\Python\AndroidTranslate\APIKey.json" 
```

## Usage

Add the String.xml file to the same file as the script. 
You can run the script in the console.

To see all the supported language codes: 

```bash
python AndroidStringTranslator.py list-languages
```

To run the translator:

```bash
python AndroidStringTranslator.py translateFile
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
