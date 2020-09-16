'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''


def letterCombinations(self, digits: str) -> List[str]:

    if digits == "":
        return []

    alpha_num = {0: "", 1: "", 2: "abc", 3: "def", 4: "ghi",
                 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

    master_list = []

    def dfs(prefix, i):

        if i == len(digits):
            master_list.append(prefix)
            return

        for letter in alpha_num[int(digits[i])]:
            dfs(prefix+letter, i+1)

    dfs("", 0)
    return master_list

#         non DFS method
#         queue = [""]
#         for digit in digits:
#             for _ in range(len(queue)):
#                 temp = queue.pop(0)
#                 for letter in alpha_num[int(digit)]:
#                     queue.append(temp+letter)
#         return queue
