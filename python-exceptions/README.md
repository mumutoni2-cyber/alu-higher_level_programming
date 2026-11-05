# Python - Exceptions

This project explores handling and raising errors with `try` / `except` / `finally` and `raise` in Python 3.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/python3`
- Code follows the `pycodestyle` style (version 2.7.*)
- All files are executable
- No modules are imported

## Files

| File | Description |
| ---- | ----------- |
| `0-safe_print_list.py` | Prints `x` elements of a list and returns the number of elements printed. |
| `1-safe_print_integer.py` | Prints an integer with `"{:d}".format()` and returns whether it succeeded. |
| `2-safe_print_list_integers.py` | Prints the first `x` elements of a list, only integers, and returns the count printed. |
| `3-safe_print_division.py` | Divides 2 integers, prints the result in `finally`, and returns it (or `None`). |
| `4-list_division.py` | Divides 2 lists element by element, handling wrong type, division by 0, and out of range. |
| `5-raise_exception.py` | Raises a `TypeError`. |
| `6-raise_exception_msg.py` | Raises a `NameError` with a message. |