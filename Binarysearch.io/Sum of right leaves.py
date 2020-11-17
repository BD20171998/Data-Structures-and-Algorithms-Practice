'''
Sum of right leaves

Given a binary tree root, return the sum of all leaves that are right children.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(self, root):

    sum = 0

    def dfs(root, isRight):

        nonlocal sum

        if root is None:
            return

        dfs(root.left, False)

        dfs(root.right, True)

        if root.left is None and root.right is None and isRight:
            sum += root.val

    dfs(root, False)

    return sum
