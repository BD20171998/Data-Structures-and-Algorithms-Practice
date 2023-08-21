'''
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
'''

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

       
        res = defaultdict(int)

        final_res = []

        for num in nums:
            res[num] = res[num] + 1

        res_sorted = sorted(res.items(), key=lambda x:x[1],reverse=True)
      
       
        for i in range(k):
           
            final_res.append(res_sorted[i][0])
        return final_res