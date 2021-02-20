'''
Base 3 to Integer

Given a string s representing 
a number in base 3 (consisting only of 0, 1, or 2), 
return its decimal integer equivalent. This should 
be implemented directly without using a built-in function.
'''


def solve(self, s):

    decimal = 0

    for i in range(len(s)):

        decimal += (ord(s[len(s)-1-i])-48) * (3**i)

    return decimal
