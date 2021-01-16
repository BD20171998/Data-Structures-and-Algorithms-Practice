/*
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
*/

class Solution {
    public int hammingDistance(int x, int y) {
        
        int count =0;
        int xy = x^y;
        
        while (xy>0)
        // for (int i=0;i<32;i++)
        {
            if((xy&1)!=0)
                count++;
            
            xy>>=1;
        
        }
        return count;
    }
}