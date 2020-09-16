'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


def removeDuplicates(self, nums: List[int]) -> int:

    i = 1

    while i < len(nums):

        if nums[i] == nums[i-1]:
            nums.pop(i-1)

        else:
            i += 1

    return len(nums)
