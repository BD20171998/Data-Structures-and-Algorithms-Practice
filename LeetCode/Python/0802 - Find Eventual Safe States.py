'''
802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/
'''


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        nodes = {i: "x" for i in range(len(graph))}

        def dfs(i):

            nodes[i] = 'v'

            for j in graph[i]:

                if nodes[j] != 'x':

                    if nodes[j] != 's':
                        nodes[i] = 'u'
                        return False

                elif not dfs(j):
                    nodes[i] = 'u'
                    return False

            nodes[i] = 's'
            return True

        for i in range(len(graph)):

            if nodes[i] == 'x':
                dfs(i)

        return [i for i in nodes.keys() if nodes[i] == 's']
