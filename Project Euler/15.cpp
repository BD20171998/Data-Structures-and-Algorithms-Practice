/**
https://projecteuler.net/problem=15
*/

#include <iostream>
#include <cstring>
using namespace std;

unsigned long helper(unsigned long int *dp, int r, int c, int n)
{

    if (r < 0 || c < 0)
        return 0;

    if (dp[c + r * n] < 1)
        dp[c + r * n] = helper(dp, r - 1, c, n) + helper(dp, r, c - 1, n);

    return dp[c + r * n];
}

unsigned long uniquePaths(int m, int n)
{

    unsigned long int dp[m][n];

    memset(dp, 0, m * n * 8);
    dp[0][0] = 1;

    helper((unsigned long int *)dp, m - 1, n - 1, n);

    return dp[m - 1][n - 1];
}

int main(void)
{
    cout << uniquePaths(21, 21);
}