# Python - Test-driven development

Functions written with doctests (`tests/*.txt`) and unittests (`tests/*.py`).

Run the doctests and unittests from this directory:

```
python3 -m doctest -v ./tests/0-add_integer.txt
python3 -m unittest tests.6-max_integer_test
```

| File | Description |
| --- | --- |
| 0-add_integer.py | Adds two integers/floats |
| 2-matrix_divided.py | Divides all elements of a matrix |
| 3-say_my_name.py | Prints a name |
| 4-print_square.py | Prints a square with `#` |
| 5-text_indentation.py | Prints text with 2 new lines after `.`, `?`, `:` |
| 6-max_integer.py | Max integer of a list (given) |
| tests/6-max_integer_test.py | Unittests for `max_integer` |
