'''
754. Reach a Number
https://leetcode.com/problems/reach-a-number/
'''

from math import sqrt, ceil


def reachNumber(self, target: int) -> int:

    n = 0
    temp_sum = 0
    target = abs(target)

    # -b+-b^2-4ac / 2a
    # 0 = n^2 + n -2x

    n = ceil((-1 + sqrt(1-4*1*-2*target))/2)

    temp_sum = (n*(n+1))/2

    if (temp_sum - target) % 2 == 0:
        return n

    elif (temp_sum + n+1 - target) % 2 == 0:
        return n+1

    else:
        return n+2
