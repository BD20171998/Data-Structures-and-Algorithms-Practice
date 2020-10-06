/*
657. Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin/
*/

class Solution {
public:
    bool judgeCircle(string moves) {
        int x=0, y=0;
        
        for(int i=0;i<moves.size();i++)
        {
            if (moves[i]=='L')
                x-=1;
            
            else if (moves[i]=='R')
                x+=1;
            
            else if (moves[i]=='D')
                y-=1;
            
            else
                y+=1;
        }
           
        if (x==0 && y==0)
            return true;
        
        else
            return false;
    }
};