'''
Unique Occurrences

Given a list of integers nums, 
return whether the number of 
occurrences of every value in 
the array is unique.

Note: Numbers can be negative.
'''


def solve(self, nums):

    num_dict = {}

    for i in range(len(nums)):

        if nums[i] in num_dict:
            num_dict[nums[i]] += 1

        else:
            num_dict[nums[i]] = 1

    myset1 = num_dict.values()
    myset2 = set(num_dict.values())

    if len(myset1) == len(myset2):
        return True

    else:
        return False
