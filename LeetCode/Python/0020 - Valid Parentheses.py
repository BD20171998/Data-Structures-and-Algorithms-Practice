"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/submissions/
"""


def isValid(self, s: str) -> bool:

    stack = []
    list_str = [i for i in s]

    for i in list_str:

        if i == "[":
            stack.append("]")

        elif i == "(":
            stack.append(")")

        elif i == "{":
            stack.append("}")

        elif stack == [] or stack.pop() != i:
            return False

    if len(stack) == 0:
        return True
