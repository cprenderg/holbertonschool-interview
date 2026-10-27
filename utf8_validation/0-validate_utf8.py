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

    # BINARY_MIN_ALL = 248
    # BINARY_MAX_ALL = 255
    # BINARY_MIN_0 = 128
    # BINARY_MAX_0 = 191

    CONTINUATION_BYTE_MIN = 128
    # CONTINUATION_BYTE_MAX = 191
    TWO_STARTER_MIN = 192
    # TWO_STARTER_MAX = 223
    THREE_STARTER_MIN = 224
    FOUR_STARTER_MIN = 240
    FOUR_STARTER_MAX = 247
    bytes_left = 0

    for number in data:
        if number > 255:
            number = number % 256
        if bytes_left == 0:
            if number >= CONTINUATION_BYTE_MIN and number < TWO_STARTER_MIN:
                return False
            if number >= TWO_STARTER_MIN and number < THREE_STARTER_MIN:
                bytes_left = 1
            if number >= THREE_STARTER_MIN and number < FOUR_STARTER_MIN:
                bytes_left = 2
            if number >= FOUR_STARTER_MIN and number < FOUR_STARTER_MAX:
                bytes_left = 3
        elif bytes_left:
            if number < CONTINUATION_BYTE_MIN or number >= TWO_STARTER_MIN:
                return False
            else:
                bytes_left -= 1

    if bytes_left:
        return False
    return True
