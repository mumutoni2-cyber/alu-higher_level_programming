#!/usr/bin/python3
"""Module 2-matrix_divided.
This module provides the function matrix_divided(matrix, div).
It divides every element of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.
    Return a new matrix with each element rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError(msg)
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(el / div, 2) + 0.0 for el in row] for row in matrix]
