#!/usr/bin/python3
"""
takes user input to check the N queens puzzle
"""

import sys


def create_board(n: int):
    """
    creates the board of size n
    """

    board = []
    x = 0
    for square in range(n):
        row = []
        for y in range(n):
            row.append([x, y])
        board.append(row)
        x += 1
    return board


def can_attack(queen, defender) -> bool:
    """
    checks if a square can be attacked by a queen
    """

    if queen is None:
        return True
    # horiztonal
    if queen[0] == defender[0]:
        return True
    # vertical
    if queen[1] == defender[1]:
        return True
    # diagonal down right
    if queen[0] - defender[0] == queen[1] - defender[1]:
        return True
    # diagonal up right
    if queen[0] - defender[0] == defender[1] - queen[1]:
        return True
    # diagonal down left
    if defender[0] - queen[0] == queen[1] - defender[1]:
        return True
    # diagonal up left
    if queen[0] - defender[0] == queen[1] - defender[1]:
        return True


def is_safe(queens, square):
    """
    checks if a square is safe
    """

    for queen in queens:
        if can_attack(queen, square):
            return False
    return True


def check_row(queens, board, n, row_num):
    """
    recursive function that returns a solution
    """

    solutions = []

    if len(queens) == n:
        return [queens]

    for square in board[row_num]:
        if is_safe(queens, square):
            temp = queens.copy()
            temp.append(square)
            temp = check_row(temp, board, n, row_num + 1)

            solutions.extend(temp)

    return solutions


def main(args):
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

    board = create_board(n)

    solutions = []
    queens = []

    for square in board[0]:
        queens.append(square)
        queens = check_row(queens, board, n, 1)
        if queens:
            solutions.extend(queens)
        queens = []

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main(sys.argv[1:])
