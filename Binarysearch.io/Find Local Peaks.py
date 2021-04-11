'''
Find Local Peaks

You are given a list of integers nums. 
Return the index of every peak in the 
list, sorted in ascending order. An 
index i is called a peak if

nums[i] > nums[i + 1] if i = 0
nums[i] > nums[i - 1] if i = n - 1
nums[i - 1] < nums[i] > nums[i + 1] otherwise

However, a list of length 1 is not considered a peak.
'''


class Solution:
    def solve(self, nums):
        indexes = []

        for i in range(1, len(nums)):

            if nums[0] > nums[1]:
                indexes.append(0)

            if nums[i] > nums[i-1] and i == len(nums)-1:

                indexes.append(i)
                break

            if nums[i-1] < nums[i] and nums[i] > nums[i + 1]:
                indexes.append(i)

        indexes.sort()

        return list(set(indexes))
