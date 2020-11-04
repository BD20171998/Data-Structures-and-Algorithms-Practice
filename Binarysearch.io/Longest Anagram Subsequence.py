'''
Longest Anagram Subsequence

Given two lowercase alphabet strings a and b, 
return the length of the longest anagram subsequence.
'''


def solve(self, a, b):

    if a == "" and b == "":
        return 0

    set1 = set(a)
    set2 = set(b)
    count = 0

    store1 = {k: 0 for k in set1}
    store2 = {k: 0 for k in set2}

    for i in range(len(a)):
        if a[i] in set1:
            store1[a[i]] += 1

    for i in range(len(b)):
        if b[i] in set2:
            store2[b[i]] += 1

    for i in set1.intersection(set2):
        count += min(store1[i], store2[i])

    return count
