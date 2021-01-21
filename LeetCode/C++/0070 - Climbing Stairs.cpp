/*
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
*/

class Solution {
public:
    
    int helper(int n,vector<int> &arr)
    {     
         if(n<0) return 0;
         if(arr[n]>0) return arr[n];
         if(n==0) return 1;
         arr[n]=helper(n-1,arr)+helper(n-2,arr);
        return arr[n];
    }
    
    int climbStairs(int n) {
        
        vector<int> arr(n+1,0);
        return helper(n,arr);
       
        
       
    }
};