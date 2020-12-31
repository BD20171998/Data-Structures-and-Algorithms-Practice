/**
1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
*/

#include <numeric>

class Solution
{
public:
    int maxScore(vector<int> &cardPoints, int k)
    {

        int temp_sum, real_max;

        if (cardPoints.size() == k)
            return accumulate(cardPoints.begin(), cardPoints.end(), 0);

        temp_sum = accumulate(cardPoints.begin(), cardPoints.begin() + k, 0);
        real_max = temp_sum;

        for (int i = 0; i < k; i++)
        {
            temp_sum -= cardPoints[k - i - 1];
            temp_sum += cardPoints[cardPoints.size() - i - 1];
            real_max = max(temp_sum, real_max);
        }

        return real_max;
    }
};