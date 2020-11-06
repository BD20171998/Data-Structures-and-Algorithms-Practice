'''
Uno Tree

Given a binary tree root, return whether all values in the tree are the same.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):

        def dfs(root, val):

            if root is None:
                return

            if root.val != val:
                return False

            left = dfs(root.left, val)
            right = dfs(root.right, val)

            if left is False or right is False:
                return False

            return True
        return dfs(root, root.val)
