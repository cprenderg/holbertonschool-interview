#!/usr/bin/python3
"""
Checks if a dataset is represents valid UTF-8 encoding
"""


def validUTF8(data: list[int]):

    """
    Function the loops through a data set
    """

    # BINARY_MIN_ALL = 11111000
    # BINARY_MAX_ALL = 11111111
    # BINARY_MIN_0 = 10000000
    # BINARY_MAX_0 = 10111111

    BINARY_MIN_ALL = 248
    BINARY_MAX_ALL = 255
    BINARY_MIN_0 = 128
    BINARY_MAX_0 = 191

    for number in data:
        string = (chr(number).encode('utf-8'))

        if len(string) > 1 or len(string) == 0:
            for value in (string):
                bin_value = int(value)
                if bin_value >= BINARY_MIN_0 and bin_value <= BINARY_MAX_0:
                    return False
                if bin_value >= BINARY_MIN_ALL and bin_value <= BINARY_MAX_ALL:
                    return False

    return True
