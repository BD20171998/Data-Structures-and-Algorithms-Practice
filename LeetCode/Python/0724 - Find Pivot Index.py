'''
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
    
        if len(nums) <1:
            return 0
        
        if sum(nums[1:]) == 0:
            return 0

        for i, ele in enumerate(nums):
            left = sum(nums[0:i])
            right = sum(nums[i+1:])

            if left == right:

                return i



        return -1