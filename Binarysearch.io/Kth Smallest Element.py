'''
Kth Smallest Element
Given a list of unsorted integers nums, and an integer k, 
return the kth (0-indexed) smallest element in the list.
'''


class Solution:
    def solve(self, nums, k):
        # Write your code here
        nums.sort()
        return nums[k]
