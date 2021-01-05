'''
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
'''


def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

    if obstacleGrid[0][0] == 1:
        return 0

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[i])):

            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = -1

            else:
                obstacleGrid[i][j] = None

    obstacleGrid[0][0] = 1

    def memo(i, j):

        if obstacleGrid[i][j] == -1:
            return 0

        if obstacleGrid[i][j] != None:
            return obstacleGrid[i][j]

        obstacleGrid[i][j] = 0

        if i > 0:
            obstacleGrid[i][j] += memo(i-1, j)

        if j > 0:
            obstacleGrid[i][j] += memo(i, j-1)

        return obstacleGrid[i][j]

    return memo(len(obstacleGrid)-1, len(obstacleGrid[0])-1)
