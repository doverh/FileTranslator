import config
from deep_translator import ChatGptTranslator

#Read a file in language X and translates it to Language Y
#Reads a file   
def translateFile(file):
    translated = ChatGptTranslator(api_key=config.OPENAI_API_KEY, target='pt').translate_file(file)
    return translated

print(translateFile("text_translate.txt"))