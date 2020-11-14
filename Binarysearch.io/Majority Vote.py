'''
Majority Vote

You are given a list of integers nums containing n integers, where each number represents a vote to a candidate.
Return the id of the candidate that has > ⌊n/2⌋. If there's not a majority vote, return -1.
This should be done in O(1) space.
'''


def solve(self, nums):

    candidates = {i: 0 for i in set(nums)}

    for i in range(len(nums)):

        if nums[i] in candidates.keys():
            candidates[nums[i]] += 1

    most_votes = max(candidates.values())

    if most_votes > floor(len(nums)//2):
        return max(candidates, key=candidates.get)

    else:
        return -1
