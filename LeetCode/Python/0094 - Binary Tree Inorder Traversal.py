'''
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return None

        nodes = []

        def inOrder(root):

            nonlocal nodes 

            if root is None:
                return

            inOrder(root.left)

            nodes.append(root.val)

            inOrder(root.right)

        inOrder(root)

        return nodes
