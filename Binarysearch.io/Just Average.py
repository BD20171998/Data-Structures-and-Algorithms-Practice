'''
Just Average

Given a list of integers nums and an integer k, return true if you 
can remove exactly one element from the list to make the average equal to exactly k.
'''


def solve(self, nums, k):

    if len(nums) == 2:
        if nums[0] == k or nums[1] == k:
            return True

        else:
            return False

    temp = nums[:]

    for i in range(len(nums)):

        temp.pop(i)

        avg = sum(temp)/(len(nums)-1)

        if avg == k:
            return True

        temp = nums[:]
    return False
