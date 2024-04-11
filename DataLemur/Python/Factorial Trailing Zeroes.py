'''
Factorial Trailing Zeroes
https://datalemur.com/questions/python-factorial-trailing-zeroes
'''

def trailing_zeroes(n):
    return -1


def facto(n):

    product = 1

    for i in range(n, 0, -1):
        product *= i

    return product


def trailing_zeroes(n):

    n_str = str(facto(n))[::-1]

    cnt = 0

    for char in n_str:
        if char == '0':
            cnt += 1
        else:
            return cnt

    return cnt