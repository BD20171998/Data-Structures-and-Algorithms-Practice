'''
136. Single Number
https://leetcode.com/problems/single-number/
'''


def singleNumber(self, nums: List[int]) -> int:

    x = nums[0]

    for i in range(1, len(nums)):

        x = nums[i] ^ x

    return x
