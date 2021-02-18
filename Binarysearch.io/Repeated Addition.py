'''
Repeated Addition

Given a positive integer n, 
sum all of its digits to get 
a new number. Repeat this operation 
until it's less than 10.
'''


def solve(self, n):

    x = n

    def divider(x):
        mysum = 0
        while x > 0:
            mysum += x % 10
            x //= 10

        return mysum

    while n > 9:

        s = divider(n)

        n = s
        if n < 10:
            break
    return s
