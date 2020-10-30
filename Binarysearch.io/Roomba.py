'''
Roomba

A Roomba robot is currently sitting in a cartesian plane at (0, 0). You are given a list of its moves that it will make, containing NORTH, SOUTH, WEST, and EAST.
Return whether after its moves it will end up in the coordinate (x, y).
'''

def solve(self, moves, x, y):
        
        x_cor=0
        y_cor = 0
        for move in moves:
            
            if move == "NORTH":
                y_cor+=1
            elif move == "SOUTH":
                y_cor-=1
                
            elif move == "EAST":
                x_cor+=1
                
            else:
                x_cor-=1
                
        if x== x_cor and y ==y_cor:
            return True
        
        else:
            return False