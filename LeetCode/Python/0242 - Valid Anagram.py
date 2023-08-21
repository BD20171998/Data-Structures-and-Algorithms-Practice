'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        a = [char for char in s]
        b = [char for char in t]

        a.sort()
        b.sort()
        i = 0
        while i < len(a):

            if a[i] != b[i]:
                return False

            i = i+1



        return True

        