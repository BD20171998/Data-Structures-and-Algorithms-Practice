'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/
'''


def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])

    buckets = [[] for _ in range(m+n-1)]
    flat_ans = []

    for r in range(len(matrix)):

        for c in range(len(matrix[r])):

            buckets[r+c].append(matrix[r][c])

    for i in range(len(buckets)):

        if i % 2 == 0:
            buckets[i].reverse()

        flat_ans.extend(buckets[i])

    return flat_ans
