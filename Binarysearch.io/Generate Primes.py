'''
Generate Primes

Given a number n, return 
a list of all prime numbers 
smaller than or equal to n 
in ascending order.
'''


class Solution:
    def solve(self, n):

        primes = []

        for i in range(2, n+1):

            for j in range(2, i+1):

                if i == j:
                    primes.append(j)

                elif i % j == 0:
                    break

        return primes
