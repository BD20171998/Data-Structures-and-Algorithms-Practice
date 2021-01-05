/**
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
*/

/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
var uniquePathsWithObstacles = function(obstacleGrid) {
    if (obstacleGrid[0][0] === 1) return 0;
    let i = 0,
        j = 0;

    obstacleGrid[0][0] = 1;

    for (i = 0; i < obstacleGrid.length; i++)
        for (j = 0; j < obstacleGrid[i].length; j++) {
            if (obstacleGrid[i][j] === 1 && (i !== 0 || j !== 0)) {
                obstacleGrid[i][j] = 0;
                continue;
            } else {
                if (i > 0) obstacleGrid[i][j] += obstacleGrid[i - 1][j];

                if (j > 0) obstacleGrid[i][j] += obstacleGrid[i][j - 1];
            }
        }

    return obstacleGrid[i - 1][j - 1];
};