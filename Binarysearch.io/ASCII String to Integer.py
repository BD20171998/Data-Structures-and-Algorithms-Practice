'''
ASCII String to Integer

You are given a string s containing digits from "0" to "9" 
and lowercase alphabet characters. Return the sum of the 
numbers found in s.
'''


def solve(self, s):
    mysum = 0
    temp = ""
    for i in range(len(s)):

        if ord(s[i]) < 48 or ord(s[i]) > 57:
            continue

        elif ord(s[i]) >= 48 and ord(s[i]) <= 57:

            temp += s[i]

            if i+1 == len(s) or ord(s[i+1]) < 48 or ord(s[i+1]) > 57:

                mysum += int(temp)
                temp = ""

    return mysum
