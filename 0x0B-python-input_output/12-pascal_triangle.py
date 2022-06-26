#!/usr/bin/python3
"""
Module 12-Pascal's Triangle
Function that returns a list of lists
of integers representing the Pascal's Triangle of n
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists
    of integers representing the Pascal's Triangle of n
    Returns an empty list if n <= 0
    You can assume n will be always an integer
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for rows in range(n-1):
        triangle.append([a+b for a, b
                         in zip([0] + triangle[-1], triangle[-1] + [0])])
    return triangle
