#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, operations[operator](a, b)))
