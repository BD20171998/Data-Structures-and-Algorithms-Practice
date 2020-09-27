/*
1051. Height Checker
https://leetcode.com/problems/height-checker/
*/

class Solution
{
public:
    int heightChecker(vector<int> &heights)
    {
        int move = 0;
        vector<int> vect2 = heights;

        sort(vect2.begin(), vect2.end());

        for (int i = 0; i < heights.size(); i++)
        {
            if (vect2[i] != heights[i])
                ++move;
        }

        return move;
    }
};