'''
46. Permutations
https://leetcode.com/problems/permutations/
'''


def permute(self, nums: List[int]) -> List[List[int]]:

    collections = []
    temp = []

    def dfs():

        if len(nums) == 0:
            collections.append(temp.copy())
            return

        for i in range(len(nums)):
            n = nums.pop(0)
            temp.append(n)
            dfs()

            n = temp.pop(-1)
            nums.append(n)

    dfs()

    return collections
