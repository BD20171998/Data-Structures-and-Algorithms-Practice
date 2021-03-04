'''
Tree Sum

Given a binary tree root, 
return the sum of all values 
in the tree.
'''


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):

        if root is None:
            return 0
        s = root.val

        def dfs(root):
            nonlocal s
            if root is None:
                return 0

            if root.left:
                s += root.left.val
                dfs(root.left)

            if root.right:
                s += root.right.val
                dfs(root.right)

        dfs(root)
        return s
