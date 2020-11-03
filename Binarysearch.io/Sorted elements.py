'''
Sorted elements

Give a list of numbers nums, return the number of elements that are in the correct indices, if the list were to be sorted.
'''


def solve(self, nums):

    temp = sorted(nums)
    count = 0

    for i in range(len(nums)):

        if nums[i] == temp[i]:
            count += 1

    return count
