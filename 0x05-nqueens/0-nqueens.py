#!/usr/bin/python3

"""This module is to solve Chess Queen problem"""


import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def get_solutions(n):
    board = [-1] * n
    solutions = []
    solve_helper(board, 0, solutions)
    return solutions


def solve_helper(board, row, solutions):
    n = len(board)

    if row == n:
        solution = [[i, board[i]] for i in range(n)]
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_helper(board, row + 1, solutions)
            board[row] = -1


solutions = get_solutions(n)

for solution in solutions:
    print(solution)
