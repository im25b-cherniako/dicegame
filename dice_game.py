import random

"""
Main function
"""

def main():
    """
    Main func
    :return: None
    """
    print(game())


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
            print('Geben Sie die Anzahl zwischen 1 und 4 an!')
            continue


players_number = inputs() # Speichert da die Spieleranzahl, weil in mehreren Funktionen verwendet wird

def dice():
    """
    Function to dice, generates a random integer from 1 to 8
    :return: int: dice number
    """
    dice_value = random.randrange(1,8)
    return dice_value

def game_round():
    """
    Main function with game logic implemented
    :return: str: list of all players SCORE
    """
    player_scores = [] # Am Anfang immer so viele Nullen, wie es Spieler gibt
    end_scores = [] # Falls einer der Spieler aufhört zu spielen, speichert es seinen letzten Wert
    for i in range(players_number):
        player_scores.append(0)

    while not all(element > 21 for element in player_scores):
        for i in range(len(player_scores)):
            player_decision = decision(i + 1)
            if player_decision:
                dice_score = dice()
                player_scores[i] += dice_score
                print(f'Spieler {i + 1} hat {player_scores[i]} Punkte!')
                print(f'Die Ergebnisse sehen so aus: {player_scores}')
                if player_scores[i] == 21:
                    return player_scores + end_scores
            else:
                print(f'Spieler {i + 1} hat entschieden, das Spiel aufzuhören')
                end_scores.append(player_scores[i])
                player_scores.remove(player_scores[i])
                break  #
        continue       # Weil aus player_scores ein Element gelöscht wurde, muss die Iteration erneut gestartet werden
    return player_scores + end_scores

def game():
    """
    Function that summarises player scores and returning a winner name if his points equal 3
    :return: str: player x won
    """
    player_points = []
    for i in range(players_number):
        player_points.append(0)

    while not any(element == 3 for element in player_points):
        scores = game_round()
        lowest_difference = 21
        player_winning = -1

        for i in range(len(scores)):
            if scores[i] <= 21:
                if 21 - scores[i] < lowest_difference:
                    lowest_difference = 21 - scores[i]
                    player_winning = i
            else:
                if scores[i] - 21 < lowest_difference:
                    lowest_difference = scores[i] - 21
                    player_winning = i
        player_points[player_winning] += 1
        print(f'Spieler {player_winning + 1} hat {player_points[player_winning]} Punkten!')
        print(f'Die Spielergebnisse sehen so aus: {player_points}')

    return f'Spieler {player_points.index(max(player_points)) + 1} hat gewonnen! '



def decision(player):
    """
    Asks the user if he wants to continue playing
    :return: bool: True or False
    """
    while True:
        decision_answer = input(f'Spieler {player} wollen Sie weiterspielen? (JA/NEIN) \n')
        decision_answer = decision_answer.lower()

        if decision_answer == 'ja':
            return True
        elif decision_answer == 'nein':
            return False
        else:
            print('Geben Sie entweder "Ja" oder "Nein" ein')
            continue

main()
