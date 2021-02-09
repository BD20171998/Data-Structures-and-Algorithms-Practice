'''
https://binarysearch.com/problems/Longest-Alliteration
Longest Alliteration

Given a list of lowercase alphabet strings words, 
return the length of the longest contiguous sublist where all words 
share the same first letter.
'''


def solve(self, words):

    if words == []:
        return 0

    if len(words) == 1:
        return 1

    start = 0
    count = 1

    for i in range(1, len(words)):

        if words[i-1][0] == words[i][0]:
            count = max(count, i-start+1)

        else:
            start = i

    return count
