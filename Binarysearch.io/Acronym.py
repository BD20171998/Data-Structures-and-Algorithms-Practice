'''
Acronym

Given a string s representing a phrase, return its acronym. 
Acronyms should be capitalized and should not include the word "and".
'''


def solve(self, s):

    new = s.split(" ")

    return "".join(i[0].upper() for i in new if i != "and")
