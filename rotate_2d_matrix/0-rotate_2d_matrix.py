#!/usr/bin/python3
"""
rotates a 2d matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):

    """
    mutates the given matrix by rotating 90 degree clockwise
    """

    side = len(matrix[0])
    rotate = []

    for i in range(side):
        rotate.append([])
        for j in range(side):
            rotate[i].append([])

    for i in range(side):
        for j in range(side):
            rotate[j][i] = matrix[- i - 1][j]

    for i in range(side):
        for j in range(side):
            matrix[i][j] = rotate[i][j]
