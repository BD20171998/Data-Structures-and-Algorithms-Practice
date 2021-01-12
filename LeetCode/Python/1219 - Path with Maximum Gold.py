'''
1219. Path with Maximum Gold
https://leetcode.com/problems/path-with-maximum-gold/
'''


def getMaximumGold(self, grid: List[List[int]]) -> int:

    max_gold = 0

    def backtrack(i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 0

        if grid[i][j] == 0:
            return 0

        restore = grid[i][j]
        grid[i][j] = 0

        temp_max = max(backtrack(i-1, j),
                       backtrack(i+1, j),
                       backtrack(i, j-1),
                       backtrack(i, j+1))

        grid[i][j] = restore

        return temp_max+grid[i][j]

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            max_gold = max(backtrack(i, j), max_gold)

    return max_gold
