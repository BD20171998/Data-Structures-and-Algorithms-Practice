'''
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''


def maxVowels(self, s: str, k: int) -> int:

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    counter = 0

    for j in range(len(s)):

        if j >= k:
            if s[j-k] in vowels:
                counter -= 1

        if s[j] in vowels:
            counter += 1

        vowel_count = max(counter, vowel_count)

    return vowel_count
