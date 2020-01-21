import random
import time

RANDOM_NUMBER_TO_VALUE = {
    0: 'rock',
    1: 'paper',
    2: 'scissors'
}

LETTER_TO_VALUE = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors'
}

WINNING_VALUE_TO_LOSING_VALUE = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}


def lets_play():
    """Main game funciton."""
    print('Welcome to rock paper scissors.\n\n')
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

        winner = find_winner(computer_value, player_value)

        if winner == 'computer':
            print(computer_value + ' beats ' +
                  player_value + '. Computer wins.')
            computer_wins += 1
            keep_playing = continue_game()
        elif winner == 'player':
            print(player_value + ' beats ' +
                  computer_value + '. ' + user_name + ' wins!')
            player_wins += 1
            keep_playing = continue_game()
        else:
            print('Tied game. Play again.\n')
            time.sleep(1)

    view_score = input('View score? ')
    if view_score == 'y':
        print('Computer wins: ' + str(computer_wins))
        print('Player wins: ' + str(player_wins))


def continue_game():
    print('Do you want to keep playing?\n')
    keep_playing = input('n for no, any other key for yes: ')
    return keep_playing


def get_player_throw():
    """Words and time to get the player's value."""
    wait_time = 1
    print('Ready to play rock paper scissors?\n',
          'Enter r, p, s.')
    print('Rock...')
    time.sleep(wait_time)
    print('Paper...')
    time.sleep(wait_time)
    print('Scissors...')
    time.sleep(wait_time)
    print('\nShoot!')
    player_throw = input('r,p,s: ')

    return player_throw


def find_winner(computer_value, player_value):
    """Finds the winner of the game from the winning value dictionary."""
    if WINNING_VALUE_TO_LOSING_VALUE[player_value] == computer_value:
        return 'player'
    elif WINNING_VALUE_TO_LOSING_VALUE[computer_value] == player_value:
        return 'computer'
    else:
        return 'tie'


if __name__ == '__main__':
    lets_play()
