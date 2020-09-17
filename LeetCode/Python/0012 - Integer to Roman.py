'''
12. Integer to Roman
https://leetcode.com/problems/integer-to-roman/
'''


def intToRoman(self, num: int) -> str:

    converted = ""
    while num > 0:

        if num >= 1000:
            converted += "M"
            num -= 1000

        elif num >= 900 and num < 1000:
            converted += "CM"
            num -= 900

        elif num >= 500 and num < 900:
            converted += "D"
            num -= 500

        elif num >= 400 and num < 500:
            converted += "CD"
            num -= 400

        elif num >= 100 and num < 400:
            converted += "C"
            num -= 100

        elif num >= 90 and num < 100:
            converted += "XC"
            num -= 90

        elif num >= 50 and num < 90:
            converted += "L"
            num -= 50

        elif num >= 40 and num < 50:
            converted += "XL"
            num -= 40

        elif num >= 10 and num < 40:
            converted += "X"
            num -= 10

        elif num >= 9 and num < 10:
            converted += "IX"
            num -= 9

        elif num >= 5 and num < 9:
            converted += "V"
            num -= 5

        elif num >= 4 and num < 5:
            converted += "IV"
            num -= 4

        else:
            converted += "I"
            num -= 1

    return converted
