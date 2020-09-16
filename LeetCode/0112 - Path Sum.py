''' 
112. Path Sum
https://leetcode.com/problems/path-sum/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def hasPathSum(self, root: TreeNode, sum: int) -> bool:

    def dfs(node, running_sum):

        if not node:
            return False

        running_sum += node.val

        if node.left is None and node.right is None:
            return running_sum == sum

        return dfs(node.left, running_sum) or dfs(node.right, running_sum)

    return dfs(root, 0)
