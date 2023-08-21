'''
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/
'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

      
        if len(nums) == 1:
            return nums[0]

        
        temp_sum = sum(nums[0:k]) 

        avg = temp_sum / k

        i = 1
        while i <= len(nums)-k:

            temp_sum  =  temp_sum - nums[i-1] + nums[i+k-1]
            temp_avg = temp_sum/k

            avg = max(temp_avg, avg)

            i = i+ 1


        return avg


