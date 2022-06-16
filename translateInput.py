from googletrans import Translator

translator = Translator()

translateInput = input("what do you want to be translated: ")
def Translate(word):
  translated = translator.translate(word, dest='en')
  print(translated.text)

Translate(translateInput)