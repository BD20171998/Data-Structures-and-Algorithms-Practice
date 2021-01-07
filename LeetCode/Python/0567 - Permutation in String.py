'''
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/
'''
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        sum_1 = sum_2 = 0

        d1 = Counter(s1)
        d2 = defaultdict(int)

        for v in d1.values():
            sum_1 += v

        for i in range(len(s2)):

            if s2[i] in d1:

                d2[s2[i]] += 1

                if d1[s2[i]] >= d2[s2[i]]:
                    sum_2 += 1

            if (i - len(s1)) >= 0:
                if s2[i - len(s1)] in d1:
                    d2[s2[i - len(s1)]] -= 1

                    if d2[s2[i - len(s1)]] < d1[s2[i - len(s1)]]:
                        sum_2 -= 1

            if sum_1 == sum_2:

                return True

        return False
