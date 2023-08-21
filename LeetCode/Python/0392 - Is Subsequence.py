'''
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
'''

lass Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s is "":
            return True

        if len(s) == 1 and len(t) ==1 and s == t:
            return True

        if len(s) == 1 and len(t) ==1 and s != t:
            return False

        counter = 0

        i = 0

        while i < len(t):

            if t[i] == s[counter]:

                if counter == len(s)-1:
                    return True
                else:
                    counter = counter + 1

            i = i+1

        return False