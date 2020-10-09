'''
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        tree = []

        def pre_order(root):

            if not root:
                return

            tree.append(root.val)

            pre_order(root.left)

            pre_order(root.right)

        pre_order(root)

        return json.dumps(tree)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        val_list = json.loads(data)

        def bst_insert(root, val):

            if root is None:
                return TreeNode(val)

            if val < root.val:
                root.left = bst_insert(root.left, val)

            if val > root.val:
                root.right = bst_insert(root.right, val)

            return root

        root = None

        for val in val_list:
            root = bst_insert(root, val)

        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
