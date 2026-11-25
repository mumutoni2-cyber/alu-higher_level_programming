#!/usr/bin/python3
"""Module defining the Base class."""
import csv
import json


class Base:
    """Base class managing id attribute for all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.

        Args:
            id (int): optional id; auto-incremented when None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string of list_objs to <Class name>.json."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        data = cls.to_json_string([o.to_dictionary() for o in list_objs])
        with open(filename, "w") as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by a JSON string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from <Class name>.json."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                data = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in data]

    @classmethod
    def _csv_fields(cls):
        """Return the ordered CSV field names for this class."""
        if cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
        return ["id", "width", "height", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write list_objs to <Class name>.csv (overwriting the file)."""
        if list_objs is None:
            list_objs = []
        fields = cls._csv_fields()
        with open(cls.__name__ + ".csv", "w", newline="") as f:
            writer = csv.writer(f)
            for obj in list_objs:
                d = obj.to_dictionary()
                writer.writerow([d[k] for k in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances loaded from <Class name>.csv."""
        fields = cls._csv_fields()
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as f:
                rows = [r for r in csv.reader(f) if r]
        except FileNotFoundError:
            return []
        return [cls.create(**dict(zip(fields, map(int, r)))) for r in rows]
