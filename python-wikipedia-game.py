# import modules
import wikipedia # Due to issue #107 (https://github.com/goldsmith/Wikipedia/issues/107), install: pip install --upgrade git+git://github.com/goldsmith/Wikipedia.git
import random

# game initialization 
def startGame():
    print("\n")
    print("\n~ WELCOME TO THE PYTHON WIKIPEDIA GAME ~\n")
    print("Objective: Navigate from the starting Wikipedia page to the target subject using only the links on each page. Fewer clicks and faster time will score the highest. Press ctrl+C to quit at any time.\n")

# get random Wikipedia subject & summary
def getSubject(): 
    subject = wikipedia.random()
    # try/catch for if there are multiple results for a subject. E.g. "United Theological College".
    try: 
        summary = wikipedia.summary(subject, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        num_options = len(e.options)
        option = random.randrange(num_options)
        summary = wikipedia.summary(e.options[option], sentences=1)
    chunk = {'subject': subject, 'summary': summary}
    return chunk

# get random starting and ending words
def setSubjects():
    start_subject = getSubject()
    target_subject = getSubject()
    print("* Starting Subject: %s - %s" % (start_subject["subject"], start_subject["summary"]))
    print("* Target Subject: %s - %s" % (target_subject["subject"], target_subject["summary"]))
    subjects = {"start": start_subject['subject'], "target": target_subject['subject']}
    return subjects

# Play game
startGame()
setSubjects()
