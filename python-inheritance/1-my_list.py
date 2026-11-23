#!/usr/bin/python3
"""Module that defines MyList, a list subclass with a sorted printer."""


class MyList(list):
    """A list subclass that can print itself in ascending sorted order."""

    def print_sorted(self):
        """Print the list sorted in ascending order without changing it."""
        print(sorted(self))
