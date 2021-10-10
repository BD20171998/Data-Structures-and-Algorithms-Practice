'''
1971. Find if Path Exists in Graph
https://leetcode.com/problems/find-if-path-exists-in-graph/
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if edges==[]:
            return True
        nodes = {key:[] for key in range(n)}
        
        for edge in edges:

            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        queue=[start]
        seen = set()
        
        while len(queue)>0:
            
            temp=queue.pop(0)
            
            seen.add(temp)
            
            neighbors= nodes[temp]
            for child in neighbors:
                
                if child == end:
                    return True
                if child not in seen:
                    queue.append(child)
                    
        return False