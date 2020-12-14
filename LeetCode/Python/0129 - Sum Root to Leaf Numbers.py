'''
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        if root is None:
            return 0

        temp = []
        total_sum = 0

        def dfs(root):

            nonlocal total_sum, temp
            temp.append(root.val)

            if root.left is None and root.right is None:

                num = 0
                for i in range(len(temp)):
                    num += (10**(len(temp)-1-i))*temp[i]

                total_sum += num

                return

            if root.left:
                dfs(root.left)
                temp.pop()

            if root.right:
                dfs(root.right)
                temp.pop()

        dfs(root)

        return total_sum
