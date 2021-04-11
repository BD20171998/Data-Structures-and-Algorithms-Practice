'''
3-6-9

Given an integer n, 
return a list with each number 
from 1 to n, except if it's a 
multiple of 3 or has a 3, 6, or 9 
in the number, it should be the string "clap".

Note: return the number as a string.
'''


class Solution:
    def solve(self, n):

        lists = []

        for i in range(1, n+1):

            if i % 3 == 0:
                lists.append("clap")

            elif "3" in str(i):
                lists.append("clap")

            elif "6" in str(i):
                lists.append("clap")

            elif "9" in str(i):
                lists.append("clap")
            else:
                lists.append(str(i))

        return lists
