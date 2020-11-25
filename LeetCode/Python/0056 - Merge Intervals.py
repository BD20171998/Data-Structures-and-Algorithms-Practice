'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''


def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key=lambda x: x[0])

    new = [intervals[0]]

    for i in range(1, len(intervals)):

        if intervals[i][0] <= new[-1][1]:
            new[-1][1] = max(intervals[i][1], new[-1][1])

        else:
            new.append(intervals[i])

    return new
