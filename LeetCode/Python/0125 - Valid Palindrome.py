'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
'''


def isPalindrome(self, s: str) -> bool:

    count = 0

    letters = [i.lower() for i in s if i.isalnum()]

    new_s = "".join(letters)

    l = len(new_s)//2

    for i in range(l):

        if new_s[i] != new_s[len(new_s)-i-1]:
            count += 1

    if count > 0:
        return False

    else:
        return True
