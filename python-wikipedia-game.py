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
    target_choice = input("(Target Subject) Press ENTER for a random subject or type your choice here. (Tip: All roads lead to Philosophy.): ")
    print("")
    start_subject = getSubject(start_choice)
    print("(Start) %s: %s" % (start_subject["subject"].upper(), start_subject["summary"]))
    target_subject = getSubject(target_choice)
    print("(Target) %s: %s" % (target_subject["subject"].upper(), target_subject["summary"]))
    subjects = {"start": start_subject, "target": target_subject, 'current': start_subject}
    input("\nThe clock starts now. Press ENTER to begin!")
    return subjects

def initializePlayer(subjects):
    time = 0
    clicks = 0
    player_data = subjects
    player_data['time'] = time 
    player_data['clicks'] = clicks
    return player_data

def printHeader(player_data):
    divider_length = 100
    divider = '=' * divider_length
    print("")
    print(divider)
    print("%s clicks | %s seconds\n" % (player_data['clicks'], player_data['time']))
    print("Start: %s" % player_data['start']['subject'].upper())
    print("Target: %s" % player_data['target']['subject'].upper())
    print("Current: %s - %s\n" % (player_data['current']['subject'].upper(), player_data['current']['summary']))

def makeDecision(links):       
    choice = input("Enter the number of your selected link: ")
    # ensure choice is a valid number
    num_options = len(links)
    options = [*range(num_options)] # unpack the range argument into a list using *
    options = [str(option) for option in options] # use list comprehension to transform the list from ints to strings
    if choice not in options:
        choice = makeDecision(links)
    choice = int(choice)
    return choice

def updatePlayer(new_subject, player_data):
    player_data['clicks'] += 1
    player_data['current']['subject'] = new_subject
    player_data['current']['summary'] = wikipedia.summary(new_subject, sentences=1)
    return player_data
    
"""
Example of player_data object: 
    {'start': 
    {
    'subject': 'National Organic Standards Board', 
    'summary': 'The National Organic Standards Board is an advisory board that makes recommendations to the United States Secretary of Agriculture on organic food and products.'
    }, 
    'target': 
    {'subject': 'Wicked Willie', 
    'summary': 'Wicked Willie is a humorous British cartoon character, personified as a talking penis, created by Gray Jolliffe (illustrator) with Peter Mayle.'
    }, 
    'current': 
    {'subject': 'National Organic Standards Board', 
    'summary': 'The National Organic Standards Board is an advisory board that makes recommendations to the United States Secretary of Agriculture on organic food and products.'
    }, 
    'time': 0, 
    'clicks': 0 }
"""

def play(player_data):
    printHeader(player_data)
    current_subject = player_data['current']['subject']
    # display links on current subject's page
    page = wikipedia.WikipediaPage(current_subject)
    links = page.links
    for link in links: 
        option = links.index(link)
        print("%s. %s" % (option, link))
    print() 
    # set the selected link as the current subject
    choice = makeDecision(links)
    new_subject = links[choice]
    updatePlayer(new_subject, player_data)


# Play game
startGame()
subjects = setSubjects()
player_data = initializePlayer(subjects)
while not player_data['current'] == player_data['target']:
    play(player_data)
print("Done.")