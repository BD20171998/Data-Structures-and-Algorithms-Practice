'''
Narcissistic number

Given an integer n, return whether it is equal to the sum of its own digits raised to the power of the number of digits.
'''


def solve(self, n):

    sum = 0
    length = 0
    temp = n

    while temp != 0:
        length += 1
        temp //= 10

    temp = n

    for i in range(length):
        sum += (temp % 10) ** length
        temp //= 10

    if sum == n:
        return True

    else:
        return False
