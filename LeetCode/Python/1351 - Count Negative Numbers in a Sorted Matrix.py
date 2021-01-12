'''
1351. Count Negative Numbers in a Sorted Matrix
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
'''


def countNegatives(self, grid: List[List[int]]) -> int:

    negatives = 0

    def bin_search(row, low, high):

        nonlocal negatives

        mid = low+(high-low)//2

        if low == high:
            negatives += len(row)-low
            return

        if row[mid] > -0.5:
            bin_search(row, mid+1, high)

        else:
            bin_search(row, low, mid)

    for i in range(len(grid)):

        if grid[i][0] < 0:
            negatives += len(grid[i])

        else:
            bin_search(grid[i], 0, len(grid[i]))

    return negatives
