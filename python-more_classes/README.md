# python-classes

This directory contains projects about Python classes and objects.

## Tasks

| File | Description |
| ---- | ----------- |
| `0-square.py` | Defines an empty class `Square` that represents a square. |
| `1-square.py` | Defines a class `Square` with a private instance attribute `size`, set at instantiation with no type or value verification. |
| `2-square.py` | Defines a class `Square` with a private `size` (default `0`) that raises `TypeError` if it is not an integer and `ValueError` if it is less than `0`. |
| `3-square.py` | Same as `2-square.py`, plus a public instance method `area()` that returns the current area of the square. |
| `4-square.py` | Same as `3-square.py`, but `size` is accessed through a property getter and a validating property setter. |
| `5-square.py` | Same as `4-square.py`, plus a public instance method `my_print()` that prints the square with the character `#` (an empty line if `size` is `0`). |
| `6-square.py` | Same as `5-square.py`, plus a private `position` tuple (validated property getter and setter) that offsets the square printed by `my_print()`. |
