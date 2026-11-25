# python-almost_a_circle

A small Python project about classes, inheritance, JSON serialization and
unit testing. It models geometric shapes on top of a common `Base` class.

## Files

| File | Description |
| ---- | ----------- |
| `models/base.py` | `Base`: manages `id`; JSON helpers (`to_json_string`, `from_json_string`), `save_to_file`, `load_from_file`, `create` |
| `models/rectangle.py` | `Rectangle(Base)`: validated `width`, `height`, `x`, `y`; `area`, `display`, `update`, `to_dictionary`, `__str__` |
| `models/square.py` | `Square(Rectangle)`: `size` property, `update`, `to_dictionary`, `__str__` |
| `tests/test_models/` | `unittest` test suites for each class |

## Usage

```python
from models.rectangle import Rectangle
from models.square import Square

r = Rectangle(10, 2, 1, 9)
print(r)                       # [Rectangle] (1) 1/9 - 10/2
Rectangle.save_to_file([r])    # writes Rectangle.json
print(Rectangle.load_from_file())

s = Square(5, 1, 1)
s.update(size=7)
print(s.to_dictionary())
```

## Tests

Run all tests from this directory:

```
python3 -m unittest discover tests
```

Run a single file:

```
python3 -m unittest tests/test_models/test_base.py
```

Code follows PEP 8 (`pycodestyle`).
