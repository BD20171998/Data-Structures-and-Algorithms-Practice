'''
202. Happy Number
https://leetcode.com/problems/happy-number/
'''

    def isHappy(self, n: int) -> bool:
        
        def checker(y):
            new = 0
            
            while y !=0:
                
                new += (y%10)**2
                y//=10
                
            return new
        
        if n == 1:
            return True
        
        storage = [n]
        new = 0
        x = n
        
        while new !=1:
            
            new += checker(x)
               
            if new in storage:
                return False
                
            if new !=1:
                storage.append(new)
                x = new
                new = 0
            
        return True