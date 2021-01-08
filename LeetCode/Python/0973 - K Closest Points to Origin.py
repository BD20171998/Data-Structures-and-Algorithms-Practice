'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap=[]
        heapq.heapify(heap)
        
        for i in range(len(points)):
            
            euc_dist = sqrt(points[i][0]**2+points[i][1]**2)
            
            if len(heap)<K:
                heapq.heappush(heap, (-euc_dist, points[i]))
                         
            elif  heap[0][0]<(-euc_dist):
                heapq.heappushpop(heap, (-euc_dist, points[i]))
                               
        return [h[1] for h in heap]