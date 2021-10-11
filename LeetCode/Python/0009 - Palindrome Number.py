'''
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        length = 0

        while temp > 0:

            temp //= 10
            length += 1

        i = 0
        temp = x

        while i < length//2:

            beginning = (temp % (10**(length-i))) // (10**(length-i-1))
            end = (temp//(10**i)) % 10

            if end != beginning:
                return False

            i += 1
        return True
