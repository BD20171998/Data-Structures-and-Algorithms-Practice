'''
List Calculator

Given a list of integers nums, a string op representing either "+", "-", "/", or "*", and an integer val, perform the operation on every number in nums with val and return the result.
Note: "/" is integer division.
'''


def solve(self, nums, op, val):

    if op == "*":
        return [i*val for i in nums]

    elif op == "+":
        return [i+val for i in nums]

    elif op == "-":
        return [i-val for i in nums]

    else:
        return [i//val for i in nums]
