'''
Furthest From Origin

You are given a string s 
where each character is "L" 
meaning you moved one unit left, 
"R" meaning you moved one unit right, 
or "?" meaning either "L" or "R".

Given you are at position 0, return 
the maximum possible distance you 
could be from 0 by replacing "?" 
with "L" or "R".
'''


class Solution:
    def solve(self, s):

        dist = 0
        move = 0
        for i in s:

            if i == 'L':
                dist -= 1

            elif i == 'R':
                dist += 1

            else:
                move += 1

        return abs(dist)+move
