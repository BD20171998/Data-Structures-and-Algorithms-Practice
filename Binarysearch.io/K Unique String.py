'''
K Unique String

Given a string s of lowercase 
alphabet characters, and an 
integer k, return the minimum 
number of changes needed in the 
string (one change involves changing a 
single character to any other character) 
so that the resulting string has at most 
k distinct characters.
'''
from collections import Counter


class Solution:
    def solve(self, s, k):

        letters = {}

        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1

        h = Counter(letters)
        top = h.most_common(k)
        tops = {}

        for a, b in top:
            tops.setdefault(a, b)
        x = 0
        for key, val in letters.items():
            if key not in tops.keys():
                x += letters[key]

        return(x)
