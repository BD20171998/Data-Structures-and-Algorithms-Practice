'''
https://projecteuler.net/problem=25
'''

# Crashed when helper function was embedded within current helper function (fib_length)


def fib_length(n):

   # get Fibonacci number - see CTCI by Laakmann-McDowell
    if n == 0:
        return n
    a = 0
    b = 1

    for i in range(2, n):

        new = a+b
        a = b
        b = new

    fib_num = a+b

    # get length of fibonacci number
    count = 0

    while fib_num > 0:
        count += 1

        fib_num //= 10

    return count


def calc_index(x):

    length = 0
    i = 0
    while length <= x:

        length = fib_length(i)

        if length == x:
            return i

        i += 1


print(calc_index(1000))
