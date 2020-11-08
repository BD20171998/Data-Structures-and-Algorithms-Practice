'''
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/
'''

from collections import defaultdict
from fractions import Fraction


def maxPoints(self, points: List[List[int]]) -> int:

    if len(points) == 0:
        return 0

    max_points = 0

    for i in range(len(points)):

        infinity = dups = 0
        slopes = defaultdict(int)

        for j in range(i+1, len(points)):

            if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                dups += 1

            elif points[j][0] == points[i][0]:
                infinity += 1

            else:
                slope = Fraction(points[j][1]-points[i]
                                 [1], points[j][0]-points[i][0])

                slope = (slope.numerator, slope.denominator)
                slopes[slope] += 1

        if len(slopes.values()) == 0:
            local_max = 0
        else:
            local_max = max(slopes.values())

        local_max = max(local_max, infinity)+1+dups

        if local_max > max_points:
            max_points = local_max

        return max_points
