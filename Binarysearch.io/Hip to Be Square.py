'''
Hip to Be Square

Given a sorted list of integers, square the elements and give the output in sorted order.
'''

def solve(self, nums):
    
    return sorted([nums[i]**2 for i in range(len(nums))])

