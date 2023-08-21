'''
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        i = 1

        while i < len(nums):

            if nums[i-1] == nums[i]:
                return True

            i = i + 1
        return False
       