'''
Partition Tree

Given the root to a binary tree root, return a list of two numbers where the first 
number is the number of leaves in the tree and the second number is the number of 
internal (non-leaf) nodes.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):

        ans = [0, 0]

        def dfs(root):

            if root is None:
                return 0

            if root.left is None and root.right is None:
                ans[0] += 1
                return

            if root.left is not None or root.right is not None:
                ans[1] += 1

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans
