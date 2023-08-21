'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''

import array as arr 



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dict = {num:target-num for num in nums}

        # [2,7,11,15]

        # [3,2,4] 6



        for i, num in enumerate(nums):

           if num_dict[num] in nums and nums.index(num_dict[num])!=  i:
               return[i,nums.index(num_dict[num])]

        



       
