#!/usr/bin/python3

"""This module contains isWinner() function"""


def list_filter(n):
    """Filter a list to make it only contains prime numbers"""

    primes = []
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)

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
    maria_total_wins = 0
    ben_total_wins = 0

    one_turn_arr = []

    winner = ''

    for num in nums:

        filtered_list = list_filter(num)

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
