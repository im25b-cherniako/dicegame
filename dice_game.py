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
    pass

main()