'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
'''

class Solution:
    def fib(self, n: int) -> int:
        memo =  [0, 1]+[0]*(n-1)

        def dfs(n):


            if memo[n] == 0 and n >1:
                memo[n] = dfs(n -1)+ dfs(n-2)
           

            return memo[n]

        return dfs(n)