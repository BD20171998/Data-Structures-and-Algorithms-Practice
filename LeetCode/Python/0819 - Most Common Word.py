"""
819. Most Common Word
https://leetcode.com/problems/most-common-word/

"""

import re


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

    master_list = {}
     result = re.sub(r'\W+', ' ', paragraph).lower()
      cleaned = result.split()

       for word in cleaned:

            if word in banned:
                continue

            elif word not in master_list:
                master_list[word] = 0

            else:
                master_list[word] += 1

        return max(master_list, key=master_list.get)
