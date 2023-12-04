import config
import os
from deep_translator import ChatGptTranslator

#Read a file in language X and translates it to Language Y
def translateFile(file,idiom):
    file_translate = os.getcwd() + '/Translate/' + file
    translated = ChatGptTranslator(api_key=config.OPENAI_API_KEY, target=idiom).translate_file(file_translate)
    file_name = os.path.splitext(file)[0]+'_translated.txt'
    file_path = os.getcwd() + '/Translate/Translated/' + file_name
    
    # Check if file already exists
    if os.path.exists(file_path):
        print('file already exists')
    else:
    # create a new file
        with open(file_path, 'w') as fp:
            fp.write(translated)
    
    return file_path


print(translateFile("README.md","pt"))