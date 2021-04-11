'''
Binary Tree to Linked List

Given a binary tree root, 
convert it to a singly 
linked list using an inorder traversal.
'''
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, root):
        if root is None:
            return None
        q = []

        def dfs(root):
            nonlocal q
            if root is None:
                return

            dfs(root.left)

            q.append(root.val)

            dfs(root.right)

        dfs(root)

        node = temp = LLNode(q[0])
        for i in range(1, len(q)):

            temp.next = LLNode(q[i])
            temp = temp.next
        return node
