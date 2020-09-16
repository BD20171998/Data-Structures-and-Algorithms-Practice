'''
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        all_paths = []
        path = ""

        if root is None:
            return all_paths

        def dfs(node, path):
            nonlocal all_paths

            path += str(node.val)

            if node.left is None and node.right is None:
                all_paths.append(path)
                path = ""
                return

            if node.left is not None:

                dfs(node.left, path + "->")

            if node.right is not None:

                dfs(node.right, path + "->")

        dfs(root, "")

        return all_paths
