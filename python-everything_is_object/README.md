# Python - Everything is object

This project explores how Python treats everything as an object: identity vs.
equality, mutable vs. immutable types, aliasing, and how arguments are passed
to functions.

## Requirements

- Ubuntu 20.04 LTS, Python 3.8.5
- Code style: pycodestyle 2.7.*
- All Python files are executable and start with `#!/usr/bin/python3`
- All files end with a new line

## Files

| File | Description |
|------|-------------|
| `0-answer.txt` | Function to print the type of an object |
| `1-answer.txt` | Function to get an object's identifier |
| `2-answer.txt` - `5-answer.txt` | Do two variables point to the same object? |
| `6-answer.txt` - `13-answer.txt` | `==` vs. `is` with ints, strings and lists |
| `14-answer.txt` - `18-answer.txt` | Lists and integers, aliasing and function arguments |
| `19-copy_list.py` | Function that returns a copy of a list |
| `20-answer.txt` - `26-answer.txt` | Tuples and their identity |
| `27-answer.txt` - `28-answer.txt` | `a = a + [x]` vs. `a += [x]` and object identity |

## Usage

```
$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
new_list = copy_list(my_list)
print(new_list == my_list)
print(new_list is my_list)

$ ./19-main.py
True
False
```
