# python-if_else_loops_functions

Python exercises on conditions (`if`/`elif`/`else`), loops and functions, from the `alu-higher_level_programming` repository.

All scripts use `#!/usr/bin/python3`, import no modules (except the provided `*-main.py` test files, which use `__import__`), and are made executable with `chmod +x`.

## Files

| File | Description |
|------|-------------|
| `0-positive_or_negative.py` | Assigns a random number from -10 to 10 and prints whether it is positive, zero or negative. |
| `1-last_digit.py` | Assigns a random number from -10000 to 10000 and prints its last digit (negative for negative numbers), then whether that digit is greater than 5, is 0, or is less than 6 and not 0. |
| `2-print_alphabet.py` | Prints the lowercase alphabet on one line with no newline, using one loop and one `print`. |
| `3-print_alphabt.py` | Same as above, but skips the letters `q` and `e`. |
| `4-print_hexa.py` | Prints the numbers 0 to 98 in decimal and hexadecimal, for example `10 = 0xa`. |
| `5-print_comb2.py` | Prints the numbers 00 to 99 as two digits, separated by `, `, ending with a newline. |
| `6-print_comb3.py` | Prints every combination of two different digits in ascending order, listing each pair once (`01` but not `10`). |
| `7-islower.py` | `islower(c)`: returns `True` if the character is a lowercase letter, `False` otherwise, using `ord()`. |
| `8-uppercase.py` | `uppercase(str)`: prints a string in uppercase followed by a newline, without `str.upper()`. |
| `9-print_last_digit.py` | `print_last_digit(number)`: prints the last digit of a number and returns it. |
| `10-add.py` | `add(a, b)`: returns the sum of two integers. |
| `11-pow.py` | `pow(a, b)`: returns `a` to the power of `b`. |
| `12-fizzbuzz.py` | `fizzbuzz()`: prints 1 to 100, using `Fizz` for multiples of 3, `Buzz` for multiples of 5 and `FizzBuzz` for both. |

## Test files

`7-main.py` to `12-main.py` are small test scripts that import the matching function and print example results.

## Usage

```
chmod +x 0-positive_or_negative.py
./0-positive_or_negative.py
./7-main.py
```