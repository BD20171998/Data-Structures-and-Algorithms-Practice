'''
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

      
     
        best_sum = float('inf')
        
        l= 0

        for x, _ in enumerate(nums):

            l = x+1
            r = len(nums)-1

            while l < r:

                curr_sum = nums[x] + nums[l] + nums[r]

                if abs(curr_sum - target) <= abs(best_sum - target):
                    ans = best_sum = curr_sum

                if curr_sum > target:
                    r = r - 1

                elif curr_sum < target:
                    l = l + 1

                elif curr_sum == target:
                    return curr_sum


        return ans