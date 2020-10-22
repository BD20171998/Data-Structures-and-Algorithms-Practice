'''
Sum of the digits

Given a positive integer num, return the sum of its digits.
Bonus: Can you do it without using strings?
'''

def solve(self, num):
        sum = 0
        
        while num >0:
            sum += num % 10
            num//=10
            
        return sum