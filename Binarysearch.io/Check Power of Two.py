'''
Check Power of Two

Given an integer n greater 
than or equal to 0, return 
whether it is a power of two.
'''


class Solution:
    def solve(self, n):

        if n == 0:
            return False

        if n == 1:
            return True
        x = 1
        y = 2
        while y <= n:
            y = 2**x
            if y == n:
                return True

            x += 1
        return False
