#!/usr/bin/python3

""" Module finds the fewest number of operations needed
to result in n characters """


def minOperations(n):

    """ Function works under condition that you can only Copy All and Paste """

    if n <= 1:
        return 0

    if n == 2:
        return 2

    copied = 1
    ops = 1

    if n % 2 == 0:
        ops = minOperations(n/2)
        ops += 2
    else:
        i = n // 2 + 1  # n is odd, so can't be divided by evens
        while i > 0:
            if n % i == 0:
                break
            i -= 2
        if i > 1:
            ops = minOperations(i)
            ops += n // i
        else:
            return n

    return int(ops)
