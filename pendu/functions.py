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
        player_name = str(input("Hello and welcome to LE PENDU! Who are you?")).lower()
    except ValueError: #not very usefull here I guess
        print("I didn't catch your name, can you try again please?(only letters)")
        set_player_name()
    return player_name


def set_player(player_name, path_to_score):
    #refaire tout ça je ne pense pas que ce soit très ouf d'utiliser les exceptions comme ça. Il faut vérifier qu'un fichier contienne un objet avant d'essayer de le load.
    os.chdir(path_to_score)
    # with open('scores', 'wb') as scores_file:
    #     score_dict_writter = pickle.Pickler(scores_file)
    #     score_dict_writter.dump({player_name: 12})
    with open('scores', 'rb') as scores_file:
        score_dict_reader = pickle.Unpickler(scores_file)
        score_dict = score_dict_reader.load()
        try:
            score = score_dict[player_name]
        except KeyError:
            with open('scores', 'wb') as scores_file:
                score_dict_writter = pickle.Pickler(scores_file)
                score_dict[player_name] = 0
                score_dict_writter.dump(score_dict)
            score = set_player(player_name, path_to_score)

    return score


player_name = set_player_name()
print("Your name is: {}".format(player_name))

path_to_score = 'C:/Users/Cobra/PycharmProjects/Training_OCR/pendu'

player_score = set_player(player_name, path_to_score)

print(player_score)

with open('scores', 'rb') as scores_file:
    score_dict_reader = pickle.Unpickler(scores_file)
    score_dict = score_dict_reader.load()
    print(score_dict)