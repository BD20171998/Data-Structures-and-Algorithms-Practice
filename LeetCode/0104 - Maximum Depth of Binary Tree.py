'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def maxDepth(self, root: TreeNode) -> int:
    depth = 0

    if root is None:
        return depth

    def dfs(node, d):

        nonlocal depth

        if node.left is None and node.right is None:
            if d >= depth:
                depth = d
            return

        if node.left is not None:
            dfs(node.left, d + 1)

        if node.right is not None:
            dfs(node.right, d + 1)

    dfs(root, 1)

    return depth
