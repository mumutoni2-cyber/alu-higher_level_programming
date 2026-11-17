#!/usr/bin/python3
"""Module that defines a class Square that can print itself with #."""


class Square:
    """Class that defines a square by its private, validated size."""

    def __init__(self, size=0):
        """Initialize a square, validating size through the size setter."""
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating its type and value.

        Raises TypeError if value is not an integer and ValueError if
        value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size**2

    def my_print(self):
        """Print the square with the character #, or an empty line if 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
