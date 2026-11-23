# python-inheritance

Exercises on Python inheritance, class introspection, and doctest-based testing.

## Requirements

- Python 3, scripts end with a new line and are executable
- Allowed editors: `vi`, `vim`, `emacs`
- No module imports (other than `__import__` of sibling files)
- Every module, class and function has a docstring
- Tests are text files in `tests/`, run with:

```bash
python3 -m doctest ./tests/*
```

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | `lookup(obj)`: returns the list of attributes and methods of an object |
| `1-my_list.py` | `MyList(list)` with `print_sorted()` that prints the list sorted ascending |
| `2-is_same_class.py` | `is_same_class(obj, a_class)`: True only if `obj` is exactly an instance of `a_class` |
| `3-is_kind_of_class.py` | `is_kind_of_class(obj, a_class)`: True if instance of, or inherited from, `a_class` |
| `4-inherits_from.py` | `inherits_from(obj, a_class)`: True only if `obj`'s class is a strict subclass of `a_class` |
| `5-base_geometry.py` | Empty `BaseGeometry` class |
| `6-base_geometry.py` | `BaseGeometry` with `area()` raising `Exception("area() is not implemented")` |
| `7-base_geometry.py` | Adds `integer_validator(name, value)` (`TypeError` / `ValueError`) |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` with private, validated `width` and `height` |
| `9-rectangle.py` | Full `Rectangle`: implements `area()` and `[Rectangle] <width>/<height>` string |
| `10-square.py` | `Square(Rectangle)` with private validated `size` and `area()` |
| `11-square.py` | `Square` printing as `[Square] <width>/<height>` |
| `tests/1-my_list.txt` | Doctests for `MyList` |
| `tests/7-base_geometry.txt` | Doctests for `BaseGeometry.integer_validator` |

## Example

```python
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)
print(s)         # [Square] 13/13
print(s.area())  # 169
```
