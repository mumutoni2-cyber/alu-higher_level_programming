#!/usr/bin/python3
"""Module defining the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes from args (ordered) or kwargs."""
        if args:
            names = ["id", "size", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                if key in ("id", "size", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
