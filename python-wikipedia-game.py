# import modules
import wikipedia # Due to issue #107 (https://github.com/goldsmith/Wikipedia/issues/107), install: pip install --upgrade git+git://github.com/goldsmith/Wikipedia.git
import random

# game initialization 
def startGame():
    print(chr(27) + "[2J")
    print("\n~ WELCOME TO THE PYTHON WIKIPEDIA GAME ~\n")
    print("Objective: Navigate from the starting Wikipedia page to the target subject using only the links on each page. Fewest clicks and faster time will score the highest. Press ctrl+C to quit at any time.\n")
    input("Press ENTER to begin.")
    print("")

# recursive try/catch for if there are multiple results for a subject. E.g. "United Theological College".
def checkDisambiguation(subject):
    try: 
        summary = wikipedia.summary(subject, sentences=1)
    except wikipedia.exceptions.DisambiguationError as e:
        option = random.choice(e.options)
        summary = checkDisambiguation(option)
    return summary

# get random Wikipedia subject & summary
def getSubject(choice=""): 
    subject = ''
    if len(choice) == 0:
        subject = wikipedia.random()
    else: 
        subject = wikipedia.search(choice, results=1, suggestion=True)[0][0]
    summary = checkDisambiguation(subject)
    chunk = {'subject': subject, 'summary': summary}
    return chunk

# get random starting and ending words
def setSubjects():
    start_choice = input("(Starting Subject) Press ENTER for a random subject or type your choice here: ")
    target_choice = input("(Target Subject) Press ENTER for a random subject or type your choice here: ")
    print("")
    start_subject = getSubject(start_choice)
    print("(Start) %s: %s" % (start_subject["subject"].upper(), start_subject["summary"]))
    target_subject = getSubject(target_choice)
    print("(Target) %s: %s" % (target_subject["subject"].upper(), target_subject["summary"]))
    subjects = {"start": start_subject, "target": target_subject, 'current': start_subject}
    print("\nThe clock starts when you select your first link. Go!")
    return subjects

def printHeader(player_data):
    divider_length = 100
    divider = '=' * divider_length
    print("")
    print(divider)
    print("%s clicks | %s seconds" % (player_data['clicks'], player_data['time']))
    print("Start: %s" % player_data['start']['subject'].upper())
    print("Target: %s" % player_data['target']['subject'].upper())
    print("Current: %s - %s\n" % (player_data['current']['subject'].upper(), player_data['current']['summary']))

def play(player_data):
    time = 0
    clicks = 0
    player_data['time'] = time 
    player_data['clicks'] = clicks
    printHeader(player_data)

# Play game
startGame()
subjects = setSubjects()
play(subjects)