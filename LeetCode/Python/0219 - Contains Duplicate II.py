'''
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       
        if len(nums) == 1 and k >0:
            return False
        counts = {num:0 for num in nums}

        for num in nums:

            counts[num] = counts[num] +1

        l, r = 0, 1

        while l < len(nums) and r< len(nums):

            if counts[nums[l]] > 1:

                while nums[r] != nums[l] and r< len(nums)-1:

                    

                    r = r+1
                
                if abs(r-l) <= k and nums[r] == nums[l]:

                    return True

                else:
                    l = l+1
                    r = l+1
                   
            else:
                l = l+1
                r = l+1

        return False