/*
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
*/

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> mymap; 
        
        set<int> st1;
        set<int> st2;
        
        for (int i = 0; i<arr.size();i++)
        {
            if (mymap.find(arr[i]) == mymap.end())
                mymap[arr[i]]=1;
            
            else
                mymap[arr[i]]+=1;
        }
        
        
        for (const auto &e : mymap)
        {
            st1.insert(e.first);
            st2.insert(e.second);
        }
        
        if (st1.size()!=st2.size())
            return false;

        else
            return true;
    }
};