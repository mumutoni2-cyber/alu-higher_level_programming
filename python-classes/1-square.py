#!/usr/bin/python3
"""Module that defines a class Square with a private size attribute."""


class Square:
    """Class that defines a square by its private size."""

    def __init__(self, size):
        """Initialize a new square with the given size, stored privately."""
        self.__size = size
