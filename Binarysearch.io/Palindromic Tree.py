'''
Palindromic Tree

Given a binary tree root where each 
node contains a digit from 0-9, return 
whether its in-order traversal is a 
palindrome.

Bonus: solve in O(h)
O(h) space where h is height of the tree.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):

        values = []

        def inorder(root):

            nonlocal values

            if root:

                inorder(root.left)

                values.append(root.val)

                inorder(root.right)

        inorder(root)

        for i in range(len(values)//2):

            if values[i] != values[len(values)-i-1]:
                return False

        return True
