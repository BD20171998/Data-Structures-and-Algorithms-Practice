'''
Check if Number Is Perfect Square

Given an integer n, return whether 
n = k * k for some integer k.

This should be done without using 
built-in square root function.
'''


class Solution:
    def solve(self, n):

        if n == 0:
            return True
        low = 1
        high = n

        while low <= high:

            mid = low + (high-low)//2

            if mid*mid == n:
                return True
            elif mid*mid > n:
                high = mid - 1
            else:
                low = mid+1
        return False
