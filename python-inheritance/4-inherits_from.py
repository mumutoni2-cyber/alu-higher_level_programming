#!/usr/bin/python3
"""Module that checks whether an object's class inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a strict subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
