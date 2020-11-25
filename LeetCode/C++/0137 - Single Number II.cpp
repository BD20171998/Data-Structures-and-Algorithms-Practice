/*
137. Single Number II
https://leetcode.com/problems/single-number-ii/
*/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        int ans=0;
        
        for(int j=0;j<32;j++)
        {
            int counter=0;
            for (int i=0;i <nums.size();i++)
            {
                int n = nums[i];
                counter+=(n >> j) & 1; 
                
            }
            if(counter%3 !=0)
                ans|= 1 << j;         
        }
        
        return ans;
    }
};