"""
Fr4nc3
This program implement a version of the game Mad Madder Libs
Set up the variables for the game Mad Madder Libs
"""

import random
import os
import os.path


def file_exist(file_path):
    """
    This method
    :param file_path:
    :return:
    True or False
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)


def create_resource_files(folder):
    """
    This method created the resources folder and resources csv if they don't exist
    :param folder:
    :return: void
    """
    nouns = ["psychic", "enthusiast", "singer", "destiny", "death", "potion",
             "poltergeist", "demon"]
    verbs = ["surround", "return", "medicate", "blindside", "flap", "trip", "snoop"]
    adjectives = ["sadistic", "wild", "domesticated", "abnormal", "medicated", "disrespectful", "impressive",
                  "crazy", "humorous"]
    sentences = ["Suddenly I saw a {adjective} {noun} {verb} in the zoo.",
                 "She {verb}s and Her {noun} were {adjective} at night.",
                 "I've known the {adjective} house for years. I {verb} all the way from {noun}",
                 "One Valentine's {noun} I {verb} when I looked in my {adjective} room and I ate chocolate",
                 "In a {adjective} day I verb} and I use my {noun}"]

    resources = {'nouns': nouns, 'verbs': verbs, 'adjectives': adjectives, 'sentences': sentences}
    if not os.path.exists(folder):  # if the folder doesn't exist create it
        os.makedirs(folder)

    for key, value in resources.items():
        file_path = os.path.join(folder, "{}.csv".format(key))
        if not file_exist(file_path):  # if the file doesn't exist create it
            with open(file_path, 'w') as f:  # always add files for the first time
                for item in value:
                    f.write("{}\n".format(item))


def play_game(**kwargs):
    """
    arguments:
        kwargs
    Return:
       Void
    """
    # Only 4 variables are expected
    min_value = kwargs.get('min_value', 0)
    max_value = kwargs.get('max_value', 0)
    recorded_sentences = kwargs.get('recorded_sentences', [])
    user_file = kwargs.get('user_file', '')
    if max_value == 0 or user_file == '':  # these are minimum values to start to play
        exit("missing parameters to play")

    is_keep_playing = None
    number_question = "Enter a number between {0} and {1}: ".format(min_value, max_value)
    play_question = "Play Again y or n: "
    while is_keep_playing != 'n':
        user_str_number = input(number_question)  # read data here
        try:
            user_number = isvalid(user_str_number)  #
        except:
            print("Sorry the value provided is not an integer.")
            user_number = None

        if user_number is not None:
            if user_number < min_value:
                print("Sorry the number provided is too small (lower than {})".format(min_value))
            elif user_number > max_value:
                print("Sorry the number provided is too big (greater than {})".format(max_value))
            else:
                # used the same random from my assignment 1
                sentence_idx = random.randint(0, min(user_number, len(SENTENCES) - 1))
                noun_idx = random.randint(0, min(user_number, len(NOUNS) - 1))
                verb_idx = random.randint(0, min(user_number, len(VERBS) - 1))
                adjective_idx = random.randint(0, min(user_number, len(ADJECTIVES) - 1))

                # generate the mad lib sentence
                sentence = SENTENCES[sentence_idx].format(
                    noun=NOUNS[noun_idx],
                    verb=VERBS[verb_idx],
                    adjective=ADJECTIVES[adjective_idx],
                )

                if sentence not in recorded_sentences:
                    save_new_sentence(len(recorded_sentences), sentence, user_file)  # save the new sentences
                    recorded_sentences.append(sentence)  # added to recorded sentences if the user continue playing
                else:
                    print("The generated sentence is already used, discarding it.")

                print("Your current madlib is:")

                for sentence in recorded_sentences:
                    print(sentence)

        is_keep_playing = None  # reset

        while 'y' != is_keep_playing and 'n' != is_keep_playing:
            is_keep_playing = input(play_question)  #
            try:
                is_keep_playing = is_keep_playing.strip().lower()  # it will work for y/n Y/N
            except:
                is_keep_playing = None

            if 'y' != is_keep_playing and 'n' != is_keep_playing:
                print("Sorry, I did not get that.")


def create_file_path(filename, folder="resources", prefix=""):
    """
    This method concatenate the file path using path.join
    :param filename:
    :param folder:
    :param prefix:
    :return:
    """
    return os.path.join(folder, "{prefix}{filename}.csv".format(filename=filename, prefix=prefix))


def save_new_sentence(index, sentence, file_path):
    """
    This method add the new sentence to the botton of the file
    the index is the len element of the list
    :param index:
    :param sentence:
    :param file_path:
    :return:
    """
    with open(file_path, "a") as file:  # append in the bottom of the file
        file.write("{sentence},{index}\n".format(sentence=sentence, index=index))


def load_csv_user_sentences(file_path):
    """
    This method load the user sentences
    :param file_path:
    :return: user sentences list
    """
    # print(file_path)
    temp_list = []
    if file_exist(file_path):
        with open(file_path) as f:
            for row in f.readlines():
                line = row.split(',')
                if len(line) == 2:
                    index = int(line[1].strip())
                    temp_list.insert(index, line[0].strip())  # this work even if the inser index exist
        return temp_list
    else:
        return []  # return empty list if file doesn't exist


def shuffle_list_simple(old_list):
    """
    This method shuffle a list without using random.shuffle()
    :param old_list:
    :return:
        tuple
    """
    return tuple(random.sample(old_list, len(old_list)))  # convert the shuffle list into an immutable list/tuple


def shuffle_list(old_list):
    """
    This method shuffle a list popping up a random index
    :param old_list:
    :return: tuple 
    """
    temp_list = []
    while len(old_list) != 0:  # run until no more element to pop up
        pop_index = random.randint(0, len(old_list) - 1)
        temp_list.append(old_list.pop(pop_index))
    return tuple(temp_list)  # convert the shuffle list into an immutable list or tuple


def isvalid(test):
    """
    isvalid is a method that return none or int if the string test is only digit
    because string.isidigit() anything like float, .0 -1 is not allowed
    arguments:
        test string
    Return:
      integer
    """
    return None if not test.isdigit() else int(test)  #


def load_csv_to_list(file_path):
    """
    This method load to a list the file
    :param file_path:
    :return:
    list
    """
    # print(file_path)
    count = 1
    temp_list = []
    if file_exist(file_path):
        with open(file_path) as f:
            for row in f.readlines():
                if count >= 10:  # avoid list larger than 10
                    break
                temp_list.append(row.strip())  # strip extra characters
                count += 1
        return temp_list
    else:
        return []  # return empty list if file doesn't exist


folder_name = "resources"  # predefined folder
create_resource_files(folder_name)
# load lists of words
SENTENCES = shuffle_list(load_csv_to_list(create_file_path("sentences", folder=folder_name)))
NOUNS = shuffle_list(load_csv_to_list(create_file_path("nouns", folder=folder_name)))
VERBS = shuffle_list(load_csv_to_list(create_file_path("verbs", folder=folder_name)))
ADJECTIVES = shuffle_list(load_csv_to_list(create_file_path("adjectives", folder=folder_name)))


# boundaries
MIN_VALUE = 0
MAX_VALUE = max(
    len(SENTENCES),
    len(NOUNS),
    len(VERBS),
    len(ADJECTIVES)
)

# this min_list is used to avoid empty list or tuple
min_list = min(
    len(SENTENCES),
    len(NOUNS),
    len(VERBS),
    len(ADJECTIVES)
)

if min_list == 0:
    exit("Missing content to continue running")  # die if any list is empty

username_question = "enter your Username: "
username = input(username_question)
while not username.isalnum():  # username must be alphanumeric no whitespaces or any other character
    print("The username needs to be alphanumeric (letters and numbers characters only)")
    username = input(username_question)

user_file_name = create_file_path(username, folder=folder_name, prefix="madlib_")
user_sentences = load_csv_user_sentences(user_file_name)

if len(user_sentences) == 0:
    print("Let start play {}!".format(username))
else:
    print("Welcome back {}!".format(username))

play_game(min_value=MIN_VALUE, max_value=MAX_VALUE, recorded_sentences=user_sentences, user_file=user_file_name)
print("Bye!")
