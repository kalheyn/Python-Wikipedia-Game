import wikipedia
import random

try: 
    summary = wikipedia.summary("United Theological College", sentences=1)
except wikipedia.exceptions.DisambiguationError as e:
    num_options = len(e.options)
    option = random.randrange(num_options)
    summary = wikipedia.summary(e.options[option], sentences=1)

print(summary)