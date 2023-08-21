'''
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/
'''

def findCircleNum(self, isConnected: List[List[int]]) -> int:
    
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
               
                self.rank = [1] * size
                
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1
                
            def connected(self, x, y):
                return self.find(x) == self.find(y)
            
        provinces = 0
        uf = UnionFind(len(isConnected)+1)
        
        for i in range(len(isConnected)):
            
            for j in range(len(isConnected[i])-1):
               
                if i == j:
                    continue
                elif isConnected[i][j] ==1:
                    uf.union(i+1,j+1)

        for i in range(1,len(uf.root)):
            if i == uf.root[i]:
                provinces +=1

        return provinces
           