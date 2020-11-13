'''
Number of bits

Given an integer n greater than or equal to 0, return the number of 1 bits in n.
'''


def solve(self, n):
    z = bin(n)[2:]

      count = 0
       for i in z:
            if i == '1':
                count += 1
        return count
