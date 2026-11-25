#!/usr/bin/python3
"""Module defining the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _check_int(name, value):
        """Raise TypeError if value is not an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        self._check_int("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        self._check_int("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x."""
        return self.__x

    @x.setter
    def x(self, value):
        self._check_int("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y."""
        return self.__y

    @y.setter
    def y(self, value):
        self._check_int("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with #, honoring x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes from args (ordered) or kwargs."""
        if args:
            names = ["id", "width", "height", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if key in ("id", "width", "height", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
