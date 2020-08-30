"""
1451. Rearrange Words in a Sentence
https://leetcode.com/problems/rearrange-words-in-a-sentence/
"""


def arrangeWords(self, text: str) -> str:

    final_string = " ".join(sorted(text.split(), key=len)).lower()

    return final_string.capitalize()
