"""
# Fr4nc3
This program implement a version of the game Mad Libs
Set up the variables for the game Mad Libs
"""
import random

nouns = ["psychic", "enthusiast", "singer", "destiny", "death", "potion",
         "poltergeist", "demon"]
verbs = ["surround", "return", "medicate", "blindside", "flap", "trip", "snoop"]
adjectives = ["sadistic", "wild", "domesticated", "abnormal", "medicated", "disrespectful", "impressive",
              "crazy", "humorous"]
sentences = ["Suddenly, I saw a {2} {0} {1} in the zoo.",
             "She {1}s and Her {0} were {2} at night.",
             "I've known the {2} house for years. I {1} all the way from {0}",
             "One Valentine's {0}, I {1}, when I looked in my {2} room and I ate chocolate",
             "In a {2} day, I {1} and I use my {0}"]

recorder_sentences = []
play_question = "Play Again y or n:"
play = "y"  # start playing
size = 0  # minimum value to start to compare
my_lists = [nouns, verbs, adjectives, sentences]

for li in my_lists:  # get the size of the biggest list
    li_size = len(li)
    if li_size == 0:  # if any list is empty the rest of the code will fail
        exit("Missing content to continue running")
    elif li_size > size:
        size = li_size


def isvalid(test, max_size):
    """
    isvalid is a method that return true or false if the string test is only digit
    and 0<= test <= max_size
    because string.isidigit() anything like float, .0 -1 is not allowed
    arguments:
        test string
        max_size integer
    Return:
       True or False
    """
    valid_value = test.isdigit()
    return valid_value if not valid_value else int(test) <= max_size  # not necessary to check int(test) >= 0


number_question = "Enter a number between 0 and {0}: ".format(size)
while play == "y":
    played = input(number_question)

    while not isvalid(played, size):  # if the input is not invalid ask again!
        played = input(number_question)

    # min value between lower bound and the last element of the list
    num_played = int(played)  # convert the value to integer
    num_sentence = random.randint(0, min(num_played, len(sentences) - 1))
    num_noun = random.randint(0, min(num_played, len(nouns) - 1))
    num_verb = random.randint(0, min(num_played, len(verbs) - 1))
    num_adj = random.randint(0, min(num_played, len(adjectives) - 1))

    # sentences[num_sentence].format(noun, verb, adj)
    new_sentence = sentences[num_sentence].format(nouns[num_noun], verbs[num_verb], adjectives[num_adj])
    if new_sentence not in recorder_sentences:
        recorder_sentences.append(new_sentence)
    else:
        print("The MadLib sentence already exist!")

    print("These are the sentences generates so far:")
    for sentence in recorder_sentences:
        print(sentence)

    play = input(play_question)
    while play != "y" and play != "n":  # force to type y/n only
        play = input(play_question)
