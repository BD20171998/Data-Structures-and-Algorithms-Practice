'''
Odd number of digits

Given a list of positive integers nums, return the number of integers that 
have odd number of digits.
'''


def solve(self, nums):
    count = 0

    def divider(n):

        length = 0

        while n > 0:
            n //= 10
            length += 1

        return length

    for i in nums:
        if i < 10 and i % 2 != 0:
            count += 1

        else:
            temp = divider(i)

            if temp % 2 != 0:
                count += 1

    return count
