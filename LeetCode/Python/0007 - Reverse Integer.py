"""
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x: int) -> int:

        reverse_num = 0

        if x < 0:
            number_1 = number_2 = x* -1

        else:
            number_1 = number_2= x

        if number_1 % 10 == 0:

            number_1 = number_2 = number_1 //10

        length = 0

        while number_1 > 0:

            length = length +1 
            number_1 = number_1//10

        while number_2 > 0:

            reverse_num = reverse_num + 10**(length-1) * (number_2 % 10)

            number_2 = number_2 //10
            length = length -1


        if reverse_num < -2**31 or reverse_num> (2**31) -1:
           
            return 0

        elif x < 0:
            return reverse_num * -1

        else:
            return reverse_num