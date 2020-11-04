'''
Intervals Intersecting at Point

You are given a two-dimensional list of integers intervals and an integer point. Each element contains [start, end] represents an inclusive interval.
Return the number of intervals that are intersecting at point.
'''


def solve(self, intervals, point):
    count = 0

    for i in intervals:
        if point >= i[0] and point <= i[1]:
            count += 1

    return count
