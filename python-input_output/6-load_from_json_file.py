#!/usr/bin/python3
"""Module that defines a function creating an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the Python object stored as JSON in a text file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
