'''
342. Power of Four
https://leetcode.com/problems/power-of-four/
'''
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True

        if  n <= 0 or n % 4 != 0:
         
            return False

        if n == 4:
     
            return True
            
        return self.isPowerOfFour(n//4)