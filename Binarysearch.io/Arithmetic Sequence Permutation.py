'''
Arithmetic Sequence Permutation

Given a list of integers nums, return whether you can 
rearrange the order of nums such that the difference 
between every consecutive two numbers is the same.
'''


def solve(self, nums):
    nums.sort()

    diff = nums[1]-nums[0]
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] != diff:
            return False
    return True
