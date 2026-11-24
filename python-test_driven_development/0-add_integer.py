#!/usr/bin/python3
"""Module 0-add_integer.
This module provides the function add_integer(a, b=98).
It adds two integers or floats and returns the result as an integer.
Floats are cast to integers before the addition.
"""


def add_integer(a, b=98):
    """Add two integers.
    Raise a TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
