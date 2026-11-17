#!/usr/bin/python3
"""Solve the N queens problem and print every solution."""

import sys


def is_safe(solution, col):
    """Return True if a queen in the next row at col is not attacked."""
    row = len(solution)
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == row - r:
            return False
    return True


def solve(n, solution):
    """Place queens row by row with backtracking, printing solutions."""
    if len(solution) == n:
        print([[r, c] for r, c in enumerate(solution)])
        return
    for col in range(n):
        if is_safe(solution, col):
            solution.append(col)
            solve(n, solution)
            solution.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, [])
