'''
1052 - Grumpy Bookstore Owner
https://leetcode.com/problems/grumpy-bookstore-owner/
'''


def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:

    base_line = 0
    temp_max = 0
    real_max = 0

    for j in range(len(customers)):

        if grumpy[j] == 0:
            base_line += customers[j]

        if grumpy[j] == 1:

            temp_max += customers[j]

        if j >= X and grumpy[j-X] == 1:
            temp_max -= customers[j-X]

        if temp_max > real_max:
            real_max = temp_max

    return base_line+real_max
