"""
1469. Find All The Lonely Nodes
https://leetcode.com/problems/find-all-the-lonely-nodes/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        
        def dfs(root):
            
            nonlocal result
          
            if root.left and root.right:
                dfs(root.left)
                dfs(root.right)
                return

            if root.left:
                result.append(root.left.val)
                dfs(root.left)
                
            if root.right:
                result.append(root.right.val)
                dfs(root.right)
            
        dfs(root)
        return result
            