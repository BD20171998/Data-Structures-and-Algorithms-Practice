'''
78. Subsets
https://leetcode.com/problems/subsets/
'''


def subsets(self, nums: List[int]) -> List[List[int]]:
    power_set = []
    temp = []

    def backtrack(i, nums, temp, power_set):

        if len(temp) > len(nums):
            return

        power_set.append(temp.copy())

        for i in range(i, len(nums)):

            temp.append(nums[i])
            backtrack(i+1, nums, temp, power_set)
            temp.pop()

    backtrack(0, nums, temp, power_set)

    return power_set
