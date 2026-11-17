#!/usr/bin/python3
"""Solve the N queens problem and print every solution."""

import sys


def solve(n, row, solution):
    """Place queens row by row with backtracking, printing each solution."""
    if row == n:
        print([[r, c] for r, c in enumerate(solution)])
        return
    for col in range(n):
        # a queen conflicts if it shares a column or a diagonal
        if all(col != c and abs(col - c) != row - r for r, c in enumerate(solution)):
            solution.append(col)
            solve(n, row + 1, solution)
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
    solve(n, 0, [])
