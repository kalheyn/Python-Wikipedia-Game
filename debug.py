import wikipedia
import random

def checkDisambiguation(subject):
    try: 
        summary = wikipedia.summary(subject, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        option = random.choice(e.options)
        summary = checkDisambiguation(option)
    return summary

print(checkDisambiguation('geore bush'))