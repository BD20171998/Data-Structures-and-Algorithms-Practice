'''
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
'''


class Solution:
    def numberToWords(self, num: int) -> str:

        def print_hundreds(n, p):

            single = ['Zero', 'One', 'Two', 'Three', 'Four',
                      'Five', 'Six', 'Seven', 'Eight', 'Nine',
                      'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
                      'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

            double = ['Twenty', 'Thirty', 'Forty',
                      'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

            triple = ['', 'Thousand', 'Million', 'Billion']

            if p > 0:
                thousands = " " + triple[p]

            else:
                thousands = ""

            temp = n
            number = []

            while temp > 0:
                number.insert(0, temp % 10)
                temp //= 10

            if n < 20:
                return "".join(single[n] + thousands)

            elif n > 19 and n <= 99:

                if number[1] == 0:
                    return "".join(double[number[0]-2] + thousands)

                else:
                    return "".join(double[number[0]-2]+" " + single[number[1]] + thousands)

            else:

                m = number[1]*10+number[2]

                if m == 0:
                    return "".join(single[number[0]] + " " + "Hundred" + thousands)

                elif m < 20:
                    return "".join(single[number[0]] + " " + "Hundred" + " "+single[m] + thousands)

                elif m > 19 and m <= 99:
                    if number[2] == 0:
                        return "".join(single[number[0]] + " "+"Hundred" + " "+double[number[1]-2] + thousands)
                    else:
                        return "".join(single[number[0]] + " "+"Hundred" + " "+double[number[1]-2] + " "+single[number[2]] + thousands)

        temp = num
        length = 0
        number = []
        word = []

        while temp > 0:
            length += 1
            number.insert(0, temp % 10)
            temp //= 10

        if num < 1000:
            return print_hundreds(num, 0)

        n = 0
        exp = 0
        i = length-1
        p = 0

        while i >= 0:

            n += number[i]*(10**exp)

            if exp == 2 or i == 0:
                if n == 0 and i > 0:
                    p += 1
                    i -= 1
                    exp = 0
                    continue

                word.append(print_hundreds(n, p))
                p += 1
                n = 0
                exp = 0
                i -= 1
                continue

            exp += 1
            i -= 1

        if num > 0 and "Zero" in word:
            word.remove("Zero")

        return " ".join(word[i] for i in range(len(word)-1, -1, -1))
