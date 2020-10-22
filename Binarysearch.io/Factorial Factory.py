'''
Factorial Factory

Given an integer n less than or equal to 10, compute its factorial.
'''


def solve(self, n):

    def factorial(n):

        if n == 1 or n == 0:
            return 1

        return n * factorial(n-1)

    return factorial(n)
