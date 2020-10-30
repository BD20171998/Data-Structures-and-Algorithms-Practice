'''
Home run

Given a non-negative integer n, return the length of the longest consecutive run of 1s in its binary representation.
'''


def solve(self, n):

    bin = "{0:b}".format(n)
    count = 0
    max = 0

    for i in range(len(bin)):

        if bin[i] == '1':
            count += 1
            if count > max:
                max = count

        else:
            count = 0

    return max
