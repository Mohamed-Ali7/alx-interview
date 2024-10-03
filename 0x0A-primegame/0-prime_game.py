#!/usr/bin/python3

"""This module contains isWinner() function"""


def list_filter(my_list):
    """Filter a list to make it only contains prime numbers"""

    primes = []

    for num in my_list:
        is_prime = True
        if num < 2:
            is_prime = False
        elif num == 2:
            primes.append(num)
        else:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)

    return primes


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
    if x <= 0:
        return None

    maria_total_wins = 0
    ben_total_wins = 0

    one_turn_arr = []

    winner = ''

    for i in range(x):
        one_turn_arr = [r for r in range(1, nums[i] + 1)]

        filtered_list = list_filter(one_turn_arr)

        filtered_list_len = len(filtered_list)

        if filtered_list_len % 2 == 0:
            ben_total_wins += 1
        else:
            maria_total_wins += 1

    if maria_total_wins > ben_total_wins:
        winner = 'Maria'
    elif maria_total_wins < ben_total_wins:
        winner = 'Ben'
    else:
        return None

    return winner
