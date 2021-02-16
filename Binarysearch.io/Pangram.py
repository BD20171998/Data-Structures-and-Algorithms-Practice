'''
Pangram

Given a string s, representing a sentence, 
return whether every letter (case-insensitive) 
of the alphabet is used at least once.
'''


def solve(self, s):
    alpha = {}

    for i in s:

        if i.lower() in alpha:
            alpha[i.lower()] += 1

        else:
            alpha[i.lower()] = 1

    for i in range(97, 123):

        if chr(i) not in alpha:
            return False

    return True
