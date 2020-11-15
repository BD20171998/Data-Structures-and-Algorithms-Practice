'''
Palindromic Anagram

Given a string s, determine whether any permutation of it is a palindrome.
'''


def solve(self, s):

    temp = [i for i in s]

    letters = {i: 0 for i in set(temp)}
    count = 0

    for i in s:

        letters[i] += 1

    for i in letters.keys():
        if letters[i] % 2 != 0:
            count += 1
    if count > 1:
        return False

    else:
        return True
