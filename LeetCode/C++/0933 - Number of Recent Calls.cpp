/*
933. Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/
*/

class RecentCounter
{

    int pl = 0;
    vector<int> pings;

public:
    RecentCounter()
    {
    }

    int ping(int t)
    {

        pings.push_back(t);
        int u = pings.size();
        int counter = 0;
        int lower = t - 3000;
        int upper = t;

        for (int index = 0; index < pings.size(); ++index)
        {
            if (lower > pings[pl])
                ++pl;
            else
                break;
        }

        for (int i = pl; i < pings.size(); ++i)
        {
            if (pings[i] >= lower && pings[i] <= upper)
                ++counter;
        }
        return counter;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */