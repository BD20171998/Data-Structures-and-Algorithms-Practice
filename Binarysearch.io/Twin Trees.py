'''
Twin Trees
Given two binary trees, root0 and root1, 
return whether their structure and values are equal.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root0, root1):
        # Write your code here

        def bfs(r1, r2):

            if r1 is None and r2 is None:
                return True

            if r1.val != r2.val:
                return False

            if r1.left and r2.left and r1.left.val != r2.left.val:
                return False

            if (r1.left and r2.left is None) or (r1.right and r2.right is None):
                return False

            if r1.right and r2.right and r1.right.val != r2.right.val:
                return False

            return bfs(r1.left, r2.left) and bfs(r1.right, r2.right)

        return bfs(root0, root1)
