'''
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/
'''

from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        nodes = defaultdict(list)
        
        for i in trust:
            nodes[i[0]].append(i[1])
    
       
        non_keys = [i for i in range(1, n+1) if i not in nodes.keys()]
        
        if len(non_keys)>1 or len(non_keys)==0:
            return -1
        
        for k,v in nodes.items():
            
            if non_keys[0] not in nodes[k]:
                return -1
                
        
        return non_keys[0]