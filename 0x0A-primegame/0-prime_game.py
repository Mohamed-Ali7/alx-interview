#!/usr/bin/python3

"""This module contains isWinner() function"""


def list_filter(my_list):
    """Filter a list to make it only contains prime numbers"""

    if not my_list:
        return []

    cur_num = my_list[0]
    cur_index = 0
    for num in my_list:
        if num % cur_num == 0 and num >= (cur_num * cur_num):
            del my_list[cur_index]

        cur_index += 1

    return my_list


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

    maria_wins = False
    ben_wins = False

    maria_total_wins = 0
    ben_total_wins = 0

    one_turn_arr = []

    winner = ''

    for i in range(x):
        one_turn_arr = [r for r in range(2, nums[i] + 1)]

        filtered_list = list_filter(one_turn_arr)

        for num in filtered_list:
            ben_wins = False
            maria_wins = False

            if maria_turn:
                maria_turn = False
                ben_turn = True
                maria_wins = True

            elif ben_turn:
                maria_turn = True
                ben_turn = False
                ben_wins = True

        if not filtered_list:
            maria_wins = False
            ben_wins = True

        if maria_wins:
            maria_total_wins += 1
        elif ben_wins:
            ben_total_wins += 1

    if maria_total_wins > ben_total_wins:
        winner = 'Maria'
    elif maria_total_wins < ben_total_wins:
        winner = 'Ben'
    else:
        return None

    return winner
