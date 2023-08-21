'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [1]*len(nums)
        post = [1]*len(nums)
        
       
        for i in range(1,len(nums)):
        
            pre[i] = pre[i-1] * nums[i-1]
  
        for i in range(1,len(nums)):
        
            post[len(nums)-i-1] =  post[len(nums)-i]* nums[len(nums)-i]

    
        return [pre[i]*post[i] for i in range(len(nums))]