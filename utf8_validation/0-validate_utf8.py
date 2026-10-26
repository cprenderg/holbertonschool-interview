#!/usr/bin/python3
"""
Checks if a dataset is represents valid UTF-8 encoding
"""


def validUTF8(data: list[int]):

    """
    Function the loops through a data set
    """
    for number in data:
        if number > 255:
            return False
    return True
