'''
1528. Shuffle String
https://leetcode.com/problems/shuffle-string/
'''


def restoreString(self, s: str, indices: List[int]) -> str:

    #         temp = {indices[i]:s[i] for i in range(len(indices))for i in range(len(s))}
    #         temp2  = ""

    #         for i in range(len(indices)):

    #             temp2 += temp[i]
    #         return temp2

    temp = [""] * len(s)

    for i in range(len(s)):

        temp[indices[i]] = s[i]

    return "".join(temp)
