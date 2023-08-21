'''
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       

        l, r = 0,0
        min_len = float('inf')
        running_sum = 0

        while r < len(nums):
             
            running_sum = nums[r] + running_sum

            while running_sum >= target:
            
               
                min_len = min(min_len, r-l+1)
                
                running_sum = running_sum - nums[l]
                l = l + 1
            r = r+1
       

        if min_len != float('inf'):
            return min_len
        else:
            return 0