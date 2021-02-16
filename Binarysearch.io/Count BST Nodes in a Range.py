'''
Count BST Nodes in a Range

Given a binary search tree root, 
and integers lo and hi, return the 
count of all nodes in root whose values 
are between [lo, hi] (inclusive).
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root, lo, hi):

        count = 0

        def dfs(root, l, h):
            nonlocal count
            if root is None:
                return 0

            if root.val >= l and root.val <= h:
                count += 1

            dfs(root.left, l, h)
            dfs(root.right, l, h)

        dfs(root, lo, hi)
        return count
