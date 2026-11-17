#!/usr/bin/python3
"""Module that defines a class Square with a size and a position."""


class Square:
    """Class that defines a square by its private size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square, validating size and position via setters."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating it.

        Raises TypeError if value is not a tuple of 2 positive integers.
        """
        error = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(error)
        for coordinate in value:
            if type(coordinate) is not int or coordinate < 0:
                raise TypeError(error)
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size**2

    def my_print(self):
        """Print the square with #, offset by its position, or an empty line.

        An empty line is printed if size is 0. Lines are not filled with
        spaces when the vertical offset position[1] is greater than 0.
        """
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
