'''
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
'''

class Solution:
    def reverseVowels(self, s: str) -> str:

      

        vowels = ['a', 'e', 'i', 'o', 'u', "A","E","I","O","U"]
        l = 0
        r = len(vowels) //2
       

        string = [char for char in s]

        l =0
        r = len(s) -1

        while l < r:

            if s[l] not in vowels:
                l = l+1

            if s[r] not in vowels:
                r = r - 1

            if s[l] in vowels and s[r] in vowels:

                string[l] = s[r]
                string[r] = s[l]

                l = l+1
                r = r -1

        return "".join(char for char in string)

        

