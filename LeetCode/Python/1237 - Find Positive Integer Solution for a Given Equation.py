'''

'''
1237. Find Positive Integer Solution for a Given Equation
https: // leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/
'''

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    
    pairs = []
    
    def bin_search(x,l,r,z):
        mid = l + (r - l) // 2 #(y + x) // 2 
        
        if l>r:
            return 
        
        elif customfunction.f(x,mid) > z: 
            bin_search(x, l,mid-1, z) 

        elif customfunction.f(x,mid) < z: 
            bin_search(x,mid + 1, r, z) 

        else:
            pairs.append([x,mid])
            return
        
    for x in range(1,1002):
        l,r = 1, 1001
        bin_search(x,l,r,z)
            
    return pairs
