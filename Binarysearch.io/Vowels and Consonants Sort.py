'''
Vowels and Consonants Sort

Given a lowercase alphabet string s, return a string with all the vowels of s in sorted order 
followed by all the consonants of s in sorted order.
Note: vowels are ["a", "e", "i", "o", "u"] and consonants are all other characters.
'''


def solve(self, s):

    vowels = ['a', 'e', 'i', 'o', 'u']

    ans = ""

    sorted_vowels = sorted([i for i in s if i in vowels])

    sorted_cons = sorted([i for i in s if i not in vowels])

    for i in sorted_vowels:
        ans += i

    for i in sorted_cons:
        ans += i

    return ans
