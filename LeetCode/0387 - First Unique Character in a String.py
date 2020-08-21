'''
#387 - 
https://leetcode.com/problems/first-unique-character-in-a-string/
'''


def firstUniqChar(self, s: str) -> int:
    cache = {}

    for i in s:
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] += 1

    for j in range(len(s)):
        if cache[s[j]] == 1:
            return j

    return -1
