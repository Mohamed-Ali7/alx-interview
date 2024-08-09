#!/usr/bin/python3
"""This module contains minOperations() function"""


def minOperations(n: int) -> int:
    """
    Ccalculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """

    next = 'H'
    body = 'H'
    op = 0
    while (len(body) < n):
        if n % len(body) == 0:
            op += 2
            next = body
            body += body
        else:
            op += 1
            body += next
    if len(body) != n:
        return 0
    return op
