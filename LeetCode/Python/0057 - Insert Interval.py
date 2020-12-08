'''
57. Insert Interval
https://leetcode.com/problems/insert-interval/
'''


def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    if len(intervals) == 0:
        return [newInterval]

    merged = newInterval
    new_merged = []

    flag = 0

    for i in range(len(intervals)):
        if merged[0] > intervals[i][1] or merged[1] < intervals[i][0]:
            new_merged.append(intervals[i])

        else:
            if merged[1] >= intervals[i][0]:
                if flag == 0:
                    merged[0] = min(merged[0], intervals[i][0])
                    merged[1] = max(merged[1], intervals[i][1])
                    new_merged.append(merged)
                    flag = 1

                if flag == 1:
                    new_merged.pop()
                    merged[0] = min(merged[0], intervals[i][0])
                    merged[1] = max(merged[1], intervals[i][1])
                    new_merged.append(merged)

    if flag == 1:
        return new_merged

    for i in range(len(new_merged)):
        if new_merged[i][0] > merged[0]:
            new_merged.insert(i, merged)
            return new_merged

    new_merged.append(merged)
    return new_merged
