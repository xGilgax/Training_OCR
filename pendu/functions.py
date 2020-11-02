import os
import pickle

def scores():
    """
    Scores are saved as dictionaries with the name of the player as the key and the score as value
    Need to handle non existing file(need to create an empty dictionary) and the case where the player is not yet in the
    dictionary (need to create the key for the player and set his score to 0) .
    """
    return None

def set_player_name():
    """Ask the player his name"""
    try:
        player_name = str(input("Hello and welcome to LE PENDU! Who are you?"))
    except ValueError: #not very usefull here I guess
        print("I didn't catch your name, can you try again please?(only letters)")
        set_player_name()
    return player_name


def set_player(player_name, path_to_score_folder, scores_file_name):
    """Returns the player's actual score given his name. If it's a new player adds the player name to the players dict
    and set his score to 0"""
    check_scores_file(path_to_score_folder, scores_file_name)

    score_dict = read_scores_dict(scores_file_name)
    if isinstance(score_dict, dict):
        for key in score_dict.keys():
            if player_name == key:
                return score_dict[player_name]

    write_scores_dict(scores_file_name, player_name, 0, score_dict)

    return score_dict[player_name]


def check_scores_file(path_to_score_folder, scores_file_name):
    """Check the existence of the scores file and create an empty dictionary if the file is empty. If it doesn't exist
    creates it and creates en empty dictionary."""
    os.chdir(path_to_score_folder)
    if not os.path.isfile(scores_file_name):
        with open(scores_file_name, 'wb') as scores_file:
            score_dict_writter = pickle.Pickler(scores_file)
            score_dict = {}
            score_dict_writter.dump(score_dict)
    elif not os.stat(scores_file_name).st_size > 0:
        with open(scores_file_name, 'wb') as scores_file:
            score_dict_writter = pickle.Pickler(scores_file)
            score_dict = {}
            score_dict_writter.dump(score_dict)
    return None


def read_scores_dict(scores_file_name):
    """Read the scores dictionnary in the scores file"""
    with open(scores_file_name, 'rb') as scores_file:
        score_dict_reader = pickle.Unpickler(scores_file)
        score_dict = score_dict_reader.load()
    return score_dict


def write_scores_dict(scores_file_name, player_name, score, score_dict):
    """Write the score of a player in the scores dictionnary file"""
    with open(scores_file_name, 'wb') as scores_file:
        score_dict_writter = pickle.Pickler(scores_file)
        score_dict[player_name] = score
        score_dict_writter.dump(score_dict)
    return None


def set_player_score(player_name, score, scores_file_name):
    """Modify the score of a player (score is the score actualised)"""
    score_dict = read_scores_dict(scores_file_name)
    write_scores_dict(scores_file_name, player_name, score, score_dict)
    return None


def points_earned(word_lenght, tries_number):
    points = None
    return points


def pick_random_word(word_list):
    return None


def generate_hidden_word(word):
    hidden_word = None
    return hidden_word


def actualise_hidden_word(word):
    actualised_word = None
    return actualised_word


def check_win(hidden_word, word_to_find):
    win_status = None #Bool
    return win_status




path_to_score = 'C:/Users/Cobra/PycharmProjects/Training_OCR/pendu'
scores_file_name = 'scores'
word_list = {}

player_name = set_player_name()
print("Your name is: {}".format(player_name))

player_score = set_player(player_name, path_to_score, scores_file_name)

print(player_score)

with open(scores_file_name, 'rb') as scores_file:
    score_dict_reader = pickle.Unpickler(scores_file)
    score_dict = score_dict_reader.load()
    print(score_dict)


set_player_score('bobi', 2, scores_file_name)

with open(scores_file_name, 'rb') as scores_file:
    score_dict_reader = pickle.Unpickler(scores_file)
    score_dict = score_dict_reader.load()
    print(score_dict)