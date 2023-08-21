'''
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

      
        index_dict = {num:i for i, num in enumerate(numbers)}


        for i, num in enumerate(numbers):

            complement = target - num

            if complement in index_dict.keys():

                return [i+1, index_dict[complement]+1]