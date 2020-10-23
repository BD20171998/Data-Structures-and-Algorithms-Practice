'''
Pigeonhole

You are given a list nums of length n + 1 picked from the range 1, 2, ..., n. By the pigeonhole principle, there must be a duplicate. Find and return it. There is guaranteed to be exactly one duplicate.
Bonus: Can you do this in linear time and constant space?
'''


def solve(self, nums):

    nums.sort()

    for i in range(len(nums)):

        if nums[i] == nums[i+1]:
            return nums[i]
