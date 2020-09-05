'''
N Lexicographic Integers
Given an integer n, return first n integers sorted in lexicographic order.
'''


class Solution:
    def solve(self, n):
        # Write your code here
        int_list = [str(i) for i in range(1, n+1)]
        int_lex_sort = []

        int_list.sort()

        for i in int_list:
            int_lex_sort.append(int(i))

        return int_lex_sort
