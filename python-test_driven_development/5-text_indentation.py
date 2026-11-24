#!/usr/bin/python3
"""Module 5-text_indentation.
This module provides the function text_indentation(text).
It prints a text with two new lines after each '.', '?' and ':'.
"""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?' and ':'.
    Raise a TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
