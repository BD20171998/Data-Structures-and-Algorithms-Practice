/*
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
*/

class Solution
{
public:
    vector<int> sortArrayByParity(vector<int> &A)
    {
        int size = A.size();

        vector<int> sorted;

        for (int i = 0; i < size; i++)
            if (A[i] % 2 == 0)
                sorted.push_back(A[i]);

        for (int i = 0; i < size; i++)
            if (A[i] % 2 != 0)
                sorted.push_back(A[i]);

        return sorted;
    }
};
