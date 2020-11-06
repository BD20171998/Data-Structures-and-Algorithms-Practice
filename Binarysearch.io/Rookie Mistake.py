'''
Rookie Mistake

You’re given a string containing letters of three types, R, B, and ..
R represents your current position, B represents a blocked position, and . represents an empty position. In one step, you can move to any adjacent position to your current position, as long as it is empty. Can you reach either the leftmost position or the rightmost position?
Return true if you can reach either the leftmost or the rightmost position, or false if you cannot.
'''

def solve(self, s):
       
    left = True
    right = True
    
    string = s.split('R')

    for i in range(len(string[0])-1,-1,-1):
        if string[0][i]=='B':
            left= False
            
    for i in range(len(string[1])):
        if string[1][i]=='B':
            right= False
        
    return right or left