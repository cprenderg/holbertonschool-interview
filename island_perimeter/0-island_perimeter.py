#!/usr/bin/python3
"""
Module that finds the perimeter of an island
"""


def island_perimeter(grid):
    """
    function that finds the perimeter of an island
    """

    perimeter = 0
    row = 0
    column = 0
    height = len(grid[row]) - 1
    width = len(grid) - 1

    while row < width:
        column = 0
        while column < height:
            if grid[row][column] == 1:
                # left
                if row == 0 or grid[row][column - 1] == 0:
                    perimeter += 1
                # right
                if row == width or grid[row][column + 1] == 0:
                    perimeter += 1
                # up
                if row == 0 or grid[row - 1][column] == 0:
                    perimeter += 1
                # down
                if row == height or grid[row + 1][column] == 0:
                    perimeter += 1
            column += 1
        row += 1
    return perimeter
