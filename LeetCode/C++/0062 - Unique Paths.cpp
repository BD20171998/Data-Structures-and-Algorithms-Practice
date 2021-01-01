/**
62. Unique Paths
https://leetcode.com/problems/unique-paths/
*/

class Solution
{
public:
    int uniquePaths(int m, int n)
    {

        int dp[m][n];

        memset(dp, 0, m * n * 4);
        dp[0][0] = 1;

        helper((int *)dp, m - 1, n - 1, n);

        return dp[m - 1][n - 1];
    }

    int helper(int *dp, int r, int c, int n)
    {

        if (r < 0 || c < 0)

            return 0;
        if (dp[c + r * n] < 1)
            dp[c + r * n] = helper(dp, r - 1, c, n) + helper(dp, r, c - 1, n);

        return dp[c + r * n];
    }
};