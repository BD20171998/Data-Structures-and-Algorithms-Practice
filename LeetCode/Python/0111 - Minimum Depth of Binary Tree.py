'''
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0

        queue = [root]
        depth = 0

        while len(queue) > 0:

            depth += 1
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if node.left is None and node.right is None:
                    return depth
