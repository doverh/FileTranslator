import config
import os
from deep_translator import ChatGptTranslator

#Read a file in language X and translates it to Language Y
def translateFile(file):
    translated = ChatGptTranslator(api_key=config.OPENAI_API_KEY, target='pt').translate_file(file)
    file_name = os.path.splitext(file)[0]+'_translated.txt'
    #print('File name: ', file_name)
    translated_file = open(file_name, 'w')
    translated_file.write(translated)
    return translated_file


print(translateFile("text_translate.txt"))