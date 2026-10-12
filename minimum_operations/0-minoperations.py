#!/usr/bin/python3

""" Module finds the fewest number of operations needed
to result in n characters """


def minOperations(n):

    """ Function works under condition that you can only Copy All and Paste """

    if n <= 0:
        return 0

    if n == 2:
        return 2

    copied = 1
    ops = 1

    if n % 2 == 0:
        ops = minOperations(n/2)
        ops += 2
    else:
        i = n - 1
        while i != 0:
            if n % i == 0:
                k = n / i
                break
            i -= 1
        if i > 1:
            ops = minOperations(i)
            ops += int(k)
        else:
            return n

    return ops
