/*
1318. Minimum Flips to Make a OR b Equal to c
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/
*/

class Solution {
    public int minFlips(int a, int b, int c) {
        
        int count=0;
        
        for(int i=0;i<32;i++)
        {
            
            if((c&1) ==0)
            {
                if ((a & 1) !=0)
                    count+=1;
                
                if ((b & 1) !=0)
                    count+=1;
            }
            
            else if ((c&1) ==1)
            {
                if((a&1)==0 && (b&1)==0)
                    count+=1;
            }
            
            a>>=1;
            b>>=1;
            c>>=1;
            
        }
        return count;
    }
}