/**
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int high=matrix.size()-1, low=0, mid, row;
        
        if (matrix.size() <1)
            return false;
        
        else if (matrix[0].size() < 1)
            return false;
        
        while(low <= high)
        {
            mid = low + (high-low)/2;
            
            if (target< matrix[mid][0])
                high= mid-1;
                
            else if (target> matrix[mid][0])
                low= mid+1;
            
            else
                return true;   
        }
        
        if (matrix[mid][0]>target)
            mid--;
        
        if (mid< 0)
            return false;
        
        low = 0;
        high = matrix[mid].size()-1;
        row = mid;
        
        while(low <= high)
        {
            mid = low + (high-low)/2;
            
            if (target< matrix[row][mid])
                high= mid-1;
                
            else if (target> matrix[row][mid])
                low= mid+1;
            
            else
                return true;   
        }
        return false;
    }
};