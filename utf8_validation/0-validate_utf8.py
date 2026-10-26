#!/usr/bin/python3
"""
Checks if a dataset is represents valid UTF-8 encoding
"""


def validUTF8(data: list[int]):

    """
    Function the loops through a data set
    """
    for number in data:
        string = (chr(number).encode('utf-8'))
        if len(string) > 1 or len(string) == 0:
            if len(string.decode('utf-8')) > 1 or len(string.decode('utf-8')) == 0:
                return False
    return True
