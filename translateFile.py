from googletrans import Translator

translator = Translator()

def doTranslate():
  with open("words.txt") as file:
    for word in file:
      print(word)
      translated = translator.translate(word, dest='en')
      print(translated.text)
doTranslate()