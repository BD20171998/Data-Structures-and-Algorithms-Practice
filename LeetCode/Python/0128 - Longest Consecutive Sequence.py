'''
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        if len(nums) == 0:
            return 0
            
        if len(nums) == 1:
            return 1

        nums.sort()

        seq_len = 1
        temp_len = 1

        i = 1
       
        while i < len(nums):

            diff = abs(nums[i] - nums[i-1])

            if diff == 1:

                temp_len = temp_len + 1

              
            if diff == 0:

                i = i + 1
                continue

            if diff > 1:
                temp_len = 1
               
            seq_len = max(seq_len,temp_len)
            i = i + 1

        return seq_len