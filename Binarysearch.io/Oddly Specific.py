'''
Oddly Specific

Given an integer n, return the sum of the first n positive odd integers.
'''


def solve(self, n):

    res = 0

    for i in range(1, 2*n):

        if i % 2 != 0:
            res += i

    return res
