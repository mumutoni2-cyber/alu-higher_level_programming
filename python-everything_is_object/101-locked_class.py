#!/usr/bin/python3
"""Module that defines the LockedClass class."""


class LockedClass:
    """Class that only allows the instance attribute first_name."""

    def __setattr__(self, name, value):
        """Prevent creating any instance attribute except first_name."""
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
