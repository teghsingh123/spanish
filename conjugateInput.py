from pydoc import doc
from numpy import conjugate
from unidecode import unidecode
import itertools

def doConjugate(pronoun,verb):
    if unidecode(verb).endswith("ar"):
        arDict = {"yo": "o", "tu": "as", "usted": "a", "él": "a", "ella": "a", "nosotros": "amos", "vosotros": "áis", "ustedes": "an", "ellos": "an", "ellas": "an"}
        verb = verb[:-2] + arDict[pronoun]
        return verb
    if unidecode(verb).endswith("er") or unidecode(verb).endswith("ir"):
        erDict = {"yo": "o", "tu": "es", "usteffdjfd": "e", "él": "e", "ella": "e", "nosotros": "emos", "vosotros": "éis", "ustedes": "en", "ellos": "en", "ellas": "en"}
        irDict = {"nosotros": "imos", "vosotros": "ís"}
        if (pronoun == "nosotros" or pronoun == "vosotros") and verb.endswith("ir"):
            verb = verb[:-2] + irDict[pronoun]
        else:
            verb = verb[:-2] + erDict[pronoun]
        return verb

verbInput = input("Enter your non-stemchanging verb: ")


prons = [k.strip() for k in open("pronouns.txt").readlines()]
for p in prons:
  conjugated = doConjugate(p,verbInput)
  print(conjugated)