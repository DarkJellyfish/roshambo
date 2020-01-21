import random
import time

RANDOM_NUMBER_TO_VALUE = {
    0: 'rock',
    1: 'paper',
    2: 'scissors',
    3: 'lizard',
    4: 'spock'
}

LETTER_TO_VALUE = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'l': 'lizard',
    'sp': 'spock'
}

WINNING_VALUE_TO_LOSING_VALUE = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['rock', 'scissors']
}

VALUE_PAIR_TO_SENTANCE = {
    ('spock', 'rock'): 'Spock vaporizes rock.',
    ('spock', 'scissors'): 'Spock smashes scissors.',
    ('lizard', 'spock'): 'Lizard poisons spock.',
    ('lizard', 'paper'): 'Lizard eats paper.',
    ('scissors', 'paper'): 'Scissors cuts paper.',
    ('scissors', 'lizard'): 'Scissors decapitates lizard.',
    ('paper', 'rock'): 'Paper covers rock.',
    ('paper', 'spock'): 'Paper disproves spock.',
    ('rock', 'lizard'): 'Rock crushes lizard.',
    ('rock', 'scissors'): 'Rock crushes scissors.'
}


def lets_play():
    """Main game funciton."""
    print('Welcome to rock paper scissors lizard spock.\n')
    user_name = input('What is your name?\n')

    keep_playing = 'y'
    computer_wins = 0
    player_wins = 0

    while keep_playing != 'n':
        random_number = random.randrange(0, 300) % 3

        player_throw = get_player_throw()

        player_value = LETTER_TO_VALUE[player_throw]
        print('\nPlayer: ', player_value)
        computer_value = RANDOM_NUMBER_TO_VALUE[random_number]
        print('Computer: ', computer_value)

        winner, winning_str = find_winner(computer_value, player_value)

        if winner == 'computer':
            print(winning_str, 'Computer wins.')
            computer_wins += 1
            keep_playing = continue_game()
        elif winner == 'player':
            print(winning_str, user_name, 'wins!')
            player_wins += 1
            keep_playing = continue_game()
        else:
            print('Tied game. Play again.\n')
            time.sleep(1)

    view_score = input('View score? ')
    if view_score == 'y':
        print('Player wins: ' + str(player_wins))
        print('Computer wins: ' + str(computer_wins))


def continue_game():
    print('Do you want to keep playing?\n')
    keep_playing = input('n for no, any other key for yes: ')
    return keep_playing


def get_player_throw():
    """Words and time to get the player's value."""
    wait_time = 1
    print('Ready to play rock paper scissors lizard spock?\n',
          'Enter r, p, s, l, sp.')
    print('3...')
    time.sleep(wait_time)
    print('2...')
    time.sleep(wait_time)
    print('1...')
    time.sleep(wait_time)
    print('\nShoot!')
    player_throw = input('r,p,s,l,sp: ')

    return player_throw


def find_winner(computer_value, player_value):
    """Finds the winner of the game from the winning value dictionary."""
    if computer_value in WINNING_VALUE_TO_LOSING_VALUE[player_value]:
        winning_str = VALUE_PAIR_TO_SENTANCE[(player_value, computer_value)]
        return 'player', winning_str
    elif player_value in WINNING_VALUE_TO_LOSING_VALUE[computer_value]:
        winning_str = VALUE_PAIR_TO_SENTANCE[(computer_value, player_value)]
        return 'computer', winning_str
    else:
        return 'tie', None


if __name__ == '__main__':
    lets_play()
