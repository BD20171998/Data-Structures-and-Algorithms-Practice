'''
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return
    
    stack = deque()
    cur = None
    stack.append(root)
    
    while len(stack)>0:
        root = stack.pop()
        
        if root.right:
            stack.append(root.right)
        
        if root.left:
            stack.append(root.left)
            
        if cur == None:
            cur =root
            
        else:
            cur.right = root
            cur = cur.right  
        
        root.left = None