'''
Happy Numbers

Given an integer n, we apply this 
transformation until it becomes a 1: 
take each of the digits in n, square 
it, and then take their sum.

Return whether n will end up in 1 after the transformations.
'''

import math


class Solution:
    def solve(self, n):
        happy = []

        def transform(x):

            mysum = 0

            while x >= 1:

                mysum += ((x % 10)**2)

                x = math.floor(x/10)

            return mysum

        y = transform(n)
        happy.append(y)

        while y >= 1:

            y = transform(y)

            if y == 1:
                return True
            if y in happy:
                return False
            happy.append(y)

        return False
