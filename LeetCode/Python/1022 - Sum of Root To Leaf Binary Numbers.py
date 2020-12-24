'''
1022. Sum of Root To Leaf Binary Numbers
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        total = 0

        def dfs(root, temp):

            nonlocal total

            if root is None:
                return

            temp.append(root.val)

            if root.left is None and root.right is None:
                total += int("".join(str(i) for i in temp), 2)

            dfs(root.left, temp)
            dfs(root.right, temp)

            temp.pop()

        dfs(root, [])

        return(total)
