#!/usr/bin/python3
"""Module 3-say_my_name.
This module provides the function say_my_name(first_name, last_name="").
It prints a sentence with a first name and a last name.
"""


def say_my_name(first_name, last_name=""):
    """Print My name is <first name> <last name>.
    Raise a TypeError if a name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
