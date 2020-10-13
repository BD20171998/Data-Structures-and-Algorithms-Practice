/**
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
*/

class Solution
{
public:
    int findMinArrowShots(vector<vector<int>> &points)
    {

        int arrows = 0, max;

        if (points.size() <= 1)
            return points.size();

        vector<tuple<int, int>> v;

        if (points.size() > 1)
            arrows += 1;

        for (int i = 0; i < points.size(); i++)
            v.push_back(make_tuple(points[i][0], points[i][1]));

        sort(v.begin(), v.end());
        ​
            max = get<1>(v[0]);

        for (int i = 1; i < v.size(); i++)
        {

            if (get<0>(v[i]) > max)
            {
                max = get<1>(v[i]);
                arrows++;
            }
            ​ else max = min(max, get<1>(v[i]));
        }

        return arrows;
    }
};