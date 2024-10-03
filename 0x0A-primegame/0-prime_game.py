#!/usr/bin/python3

"""This module contains isWinner() function"""


def isWinner(x, nums):
    """
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from the set
    The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
    Assuming Maria always goes first and both players play optimally,
    determine who the winner of each game is.

    Args:
        x: Is the number of rounds
        nums: Is an array of n

    Return: name of the player that won the most rounds
    """

    maria_turn = True
    ben_turn = False

    maria_wins = 0
    ben_wins = 0

    one_turn_arr = []
    cur_num = 0

    winner = ''

    for i in range(x):
        one_turn_arr = [r for r in range(1, nums[i] + 1)]

        turn_arr_len = len(one_turn_arr)
        for r in range(turn_arr_len):
            cur_num = one_turn_arr[r]
            for num in one_turn_arr[r + 1:]:
                if num % cur_num == 0 and cur_num * cur_num >= num:
                    if maria_turn:
                        maria_turn = False
                        ben_turn = True
                        maria_wins += 1
                        ben_wins = 0
                    elif ben_turn:
                        maria_turn = True
                        ben_turn = False
                        ben_wins += 1
                        maria_wins = 0

    if maria_wins > ben_wins:
        winner = 'Maria'
    elif maria_wins < ben_wins:
        winner = 'Ben'
    else:
        return None

    return winner
