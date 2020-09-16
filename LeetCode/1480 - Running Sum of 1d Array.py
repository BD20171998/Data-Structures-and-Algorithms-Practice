'''
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
'''

def runningSum(self, nums: List[int]) -> List[int]:
       
        return [sum(nums[:i+1]) for i in range(len(nums)) ]