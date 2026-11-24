#!/usr/bin/python3
"""Module 4-print_square.
This module provides the function print_square(size).
It prints a square made of the character #.
"""


def print_square(size):
    """Print a square of size size with the character #.
    Raise a TypeError if size is not an integer, or a ValueError if < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
