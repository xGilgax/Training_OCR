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

    check_scores_file(path_to_score_folder, scores_file_name)

    with open(scores_file_name, 'rb') as scores_file:
        score_dict_reader = pickle.Unpickler(scores_file)
        score_dict = score_dict_reader.load()
        if isinstance(score_dict, dict):
            for key in score_dict.keys():
                if player_name == key:
                    return score_dict[player_name]

    with open(scores_file_name, 'wb') as scores_file:
        score_dict_writter = pickle.Pickler(scores_file)
        score_dict[player_name] = 0
        score_dict_writter.dump(score_dict)


    return score_dict[player_name]


def check_scores_file(path_to_score_folder, scores_file_name):
    os.chdir(path_to_score_folder)
    if not os.path.isfile(scores_file_name):
        with open(scores_file_name, 'wb') as scores_file:
            score_dict_writter = pickle.Pickler(scores_file)
            score_dict = {}
            score_dict_writter.dump(score_dict)
    return None


def set_player_score():
    return None


player_name = set_player_name()
print("Your name is: {}".format(player_name))

path_to_score = 'C:/Users/Cobra/PycharmProjects/Training_OCR/pendu'
scores_file_name = 'scores'

player_score = set_player(player_name, path_to_score, scores_file_name)

print(player_score)

with open(scores_file_name, 'rb') as scores_file:
    score_dict_reader = pickle.Unpickler(scores_file)
    score_dict = score_dict_reader.load()
    print(score_dict)