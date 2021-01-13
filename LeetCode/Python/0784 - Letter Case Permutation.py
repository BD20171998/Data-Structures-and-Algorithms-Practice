'''
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
'''


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        combinations = []

        def backtrack(i, mystring):

            if i == len(S):
                combinations.append("".join(mystring))
                return

            if mystring[i].islower() or mystring[i].isupper():
                mystring[i] = mystring[i].upper()
                backtrack(i+1, mystring)

                mystring[i] = mystring[i].lower()
                backtrack(i+1, mystring)

            else:
                backtrack(i+1, mystring)

        backtrack(0, list(S))

        return combinations
