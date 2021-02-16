'''
Largest Number By Two Times

Given a list of integers nums, return whether the 
largest number is bigger than the second-largest 
number by more than two times.
'''


def solve(self, nums):

    nums.sort()

    if max(nums) > 2*nums[-2]:
        return True
    else:
        return False
