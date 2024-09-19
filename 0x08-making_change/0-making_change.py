#!/usr/bin/python3

"""This module contains makeChange() function"""


def makeChange(coins: list, total):
    """Returns fewest number of coins needed to meet total"""

    if total <= 0:
        return 0

    reminder = 0
    number_of_coins = 0

    coins.sort(reverse=True)

    for i in range(len(coins)):
        if coins[i] > total:
            continue

        reminder = total % coins[i]

        number_of_coins += total // coins[i]

        if reminder == 0:
            return number_of_coins

        for r in range(i + 1, len(coins)):
            if coins[r] > reminder:
                continue

            number_of_coins += reminder // coins[r]

            reminder = reminder % coins[r]

            if reminder == 0:
                return number_of_coins

    return -1
