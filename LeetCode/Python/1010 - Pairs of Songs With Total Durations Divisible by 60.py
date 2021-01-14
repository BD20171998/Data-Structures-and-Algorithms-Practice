'''
1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        div_by_60 = [0 for i in range(60)]
        count = 0

        for i in range(len(time)):

            r = time[i] % 60
            if r == 0:
                count += div_by_60[0]

            else:
                count += div_by_60[60-r]

            div_by_60[r] += 1

        return count
