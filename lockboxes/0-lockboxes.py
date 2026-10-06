#!/usr/bin/python3

"""
This module returns if a list of boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Function that returns if boxes can be unlocked
    """

    keys = [0]
    used_keys = []
    while len(keys) != 0:
        for key in keys:
            if key < len(boxes):
                for new_key in boxes[key]:
                    if new_key not in keys:
                        if new_key not in used_keys:
                            keys.append(new_key)
                used_keys.append(keys.pop(keys.index(key)))

    if len(used_keys) == len(boxes):
        return True
    return False
