#!/usr/bin/python3

"""This module contains pascal_triangle() function"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
        n (Integer): Represents the row number of the triangle
    """

    if n <= 0:
        return []

    triangle = [[] for i in range(n)]
    triangle[0].append(1)

    for row in range(1, n):
        for column in range(row + 1):
            if column == 0 or column == row:
                triangle[row].append(1)
            else:
                triangle[row].append(
                    triangle[row - 1][column - 1] + triangle[row - 1][column]
                    )

    return triangle
