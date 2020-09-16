'''
1309. Decrypt String from Alphabet to Integer Mapping
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
'''


def freqAlphabets(self, s: str) -> str:
    alphabet = {v-96: chr(v) for v in range(97, 123)}
    decoded = ""
    i = 0

    while i < len(s):

        if i+2 < len(s) and s[i+2] == "#":
            temp = s[i] + s[i+1]
            decoded += alphabet[int(temp)]
            i += 3
        else:
            decoded += alphabet[int(s[i])]
            i += 1

    return decoded
