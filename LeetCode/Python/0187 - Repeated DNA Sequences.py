'''
187 - Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/
'''


def findRepeatedDnaSequences(self, s: str) -> List[str]:
    result = set()
    ss = set()
    tail = 0
    for i in range(9, len(s)):
        if s[tail:i+1] in ss:
            result.add(s[tail:i+1])
        else:
            ss.add(s[tail:i+1])
        tail += 1
    return list(result)
