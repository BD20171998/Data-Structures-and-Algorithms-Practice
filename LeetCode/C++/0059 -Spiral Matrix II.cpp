/*
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
*/

class Solution
{
public:
    vector<vector<int>> generateMatrix(int n)
    {

        int i = 1, r1 = 0, r2 = n - 1, c1 = 0, c2 = n - 1;

        vector<vector<int>> matrix;

        vector<int> one_D_vector(n, 0);

        for (int i = 0; i < n; i++)
            matrix.push_back(one_D_vector);

        i = 1;

        while (r2 >= r1 && c2 >= c1)
        {
            for (int c = c1; c < c2 + 1; c++)
            {
                matrix[r1][c] = i;
                i += 1;
            }

            for (int r = r1 + 1; r < r2 + 1; r++)
            {
                matrix[r][c2] = i;
                i += 1;
            }

            for (int c = c2 - 1; c > c1 - 1; c--)
            {
                matrix[r2][c] = i;
                i += 1;
            }

            for (int r = r2 - 1; r > r1; r--)
            {
                matrix[r][c1] = i;
                i += 1;
            }

            r1 += 1;
            c1 += 1;
            r2 -= 1;
            c2 -= 1;
        }

        return matrix;
    }
};