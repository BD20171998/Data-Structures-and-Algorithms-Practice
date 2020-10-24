'''
43. Multiply Strings
https://leetcode.com/problems/multiply-strings/
'''


def multiply(self, num1: str, num2: str) -> str:

    if int(num1) == 0 or int(num2) == 0:
        return "0"

    length = len(num1)+len(num2)

    number = [0 for i in range(length)]

    for i in range(len(num1)-1, -1, -1):

        for j in range(len(num2)-1, -1, -1):

            temp = (int(num1[i])*int(num2[j])) + number[i+j+1]
            number[i+j+1] = temp % 10
            number[i+j] += temp//10

    if number[0] == 0:
        number.pop(0)

    return "".join(str(i) for i in number)
