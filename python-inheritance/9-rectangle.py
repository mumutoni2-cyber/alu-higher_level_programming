#!/usr/bin/python3
"""Module that defines a full Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated private width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with a validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description string of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
