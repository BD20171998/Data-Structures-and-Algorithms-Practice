'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

    if matrix == [] or matrix == [[]]:
        return False

    if matrix[0][0] == target:
        return True

    low = 0
    high = len(matrix)-1

    while (high-low) > 1:
        mid = (high+low)//2

        if target > matrix[mid][0]:
            low = mid

        elif target < matrix[mid][0]:
            high = mid

        else:
            return True

    if target >= matrix[high][0]:
        row = high

    else:
        row = low

    low = 0
    high = len(matrix[row])-1

    while high-low > 1:

        mid = (high+low)//2

        if target > matrix[row][mid]:
            low = mid

        elif target < matrix[row][mid]:
            high = mid

        else:
            return True

    return target == matrix[row][low] or target == matrix[row][high]
