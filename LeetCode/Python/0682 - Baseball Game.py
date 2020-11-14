'''
682. Baseball Game
https://leetcode.com/problems/baseball-game/
'''

def calPoints(self, ops: List[str]) -> int:
        
    record = []
    
    for i in range(len(ops)):
        
        if ops[i]=="C":
            record.pop()
            
        elif ops[i]=="D":
            record.append(record[-1]*2)
        
        elif ops[i]=="+":
            record.append(record[-2]+record[-1])
            
        else:
            record.append(int(ops[i]))
    return sum(record)