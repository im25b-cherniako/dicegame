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

def rules():
    print(
        '\n********************************************************************************************\n'
        'In diesem Spiel versucht jeder Spieler, so nah wie möglich an 21 Punkte zu kommen.\n'
        'Das Spiel ähnelt Blackjack, wird aber mit einem Würfel gespielt, der Zahlen von 1 bis 8 erzeugen kann.\n\n'
        
        '-----------------------------\n'
        '     SPIELABLAUF\n'
        '-----------------------------\n'
        '• Jeder Spieler startet eine Runde mit 0 Punkten.\n'
        '• Die Spieler sind der Reihe nach an der Reihe.\n'
        '• Wenn du an der Reihe bist, wirst du gefragt, ob du weiter würfeln möchtest.\n'
        '    - Antwortest du mit JA, wird eine Zahl zwischen 1 und 8 gewürfelt und zu deinem Punktestand addiert.\n'
        '    - Antwortest du mit NEIN, wird dein aktueller Punktestand gespeichert und du nimmst an dieser Runde nicht weiter teil.\n\n'
        
        'Die Runde endet, wenn alle Spieler entweder ausgestiegen sind oder über 21 Punkte gekommen sind.\n\n'
        
        '-----------------------------\n'
        '     RUNDENGEWINN\n'
        '-----------------------------\n'
        'Am Ende einer Runde wird der Spieler ermittelt, der am nächsten an 21 liegt.\n'
        'Dabei gilt:\n'
        '• Wer maximal 21 Punkte hat, ist im Vorteil.\n'
        '• Wer darüber liegt, kann trotzdem gewinnen, wenn die Differenz zu 21 die kleinste ist.\n\n'
        
        'Der Gewinner der Runde erhält 1 Punkt.\n'
        'Sobald ein Spieler 3 Punkte erreicht hat, gewinnt er das gesamte Spiel.\n'
        '********************************************************************************************\n'
    )


def welcome():
    """
    :return:
    """
    print('Willkommen zu unserem Würfelspiel, aka Blackjack!')
    explaination = input('Möchten Sie eine kurze Erklärung, wie Blackjack funktioniert? (JA/NEIN) > ')
    while explaination not in ('JA', 'NEIN', 'ja', 'nein'): #Wenn die Eingabe nicht den folgenden entspricht:
        print('Ungültige Eingabe!')
        explaination = input('Möchten Sie eine kurze Erklärung, wie Blackjack funktioniert? (JA/NEIN) > ')
    if explaination == 'JA' or explaination == 'ja':
        rules()
    else:
        print('****************************************************************************')


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


welcome()
players_number = inputs() # Speichert da die Spieleranzahl, weil in mehreren Funktionen verwendet wird

def dice():
    """
    Function to dice, generates a random integer from 1 to 8
    :return: int: dice number
    """
    dice_value = random.randrange(1,9)
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
