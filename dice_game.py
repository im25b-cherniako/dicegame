import random

"""
Main function
"""

def inputs():
    """
    Function with programm inputs
    :return: number of players
    """
    while True:
        player_number = int(input('Geben Sie Anzahl Spieler ein (1-4) > '))
        if 4 >= player_number >= 1:
            return player_number
        else:
            print('Gib die Anzahl zwischen 1 und 4 an!')
            continue

def main():
    """
    Main func
    :return: None
    """
    inputs()
    decision()
    pass

def decision():
    """
    Asks the user if he wants to continue playing
    :param decision_answer:
    :return:
    """
    decision_answer = input('Wollen Sie weiterspielen? (JA/NEIN) \n')
    if decision_answer == 'JA':
        return True
    else:
        return False

main()
