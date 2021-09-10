'''
1791. Find Center of Star Graph
https://leetcode.com/problems/find-center-of-star-graph/
'''


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        center = set()

        for edge in edges:
            if edge[0] in center:
                return edge[0]
            if edge[1] in center:
                return edge[1]

            center.add(edge[0])
            center.add(edge[1])
