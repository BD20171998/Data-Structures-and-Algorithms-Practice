'''
Equivalent Value and Frequency

Given a list of integers nums, return whether there's an integer whose frequency in the list is same as its value.
'''


def solve(self, nums):

    freq = {k: 0 for k in set(nums)}

    for num in nums:
        freq[num] += 1

    for num in nums:
        if num == freq[num]:
            return True

    return False
