'''
Transpose of a Matrix

Given an integer square (n by n) matrix, return its transpose. 
A transpose of a matrix switches the row and column indices. 
That is, for every r and c, matrix[r][c] = matrix[c][r].
'''


def solve(self, matrix):
    matrix2 = []
    for i in range(len(matrix)):

        temp = []
        for j in range(len(matrix[i])):

            temp.append(matrix[j][i])

        matrix2.append(temp)

    return matrix2
