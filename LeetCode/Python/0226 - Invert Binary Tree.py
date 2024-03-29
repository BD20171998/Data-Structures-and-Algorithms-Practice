'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

   
        def dfs(root):
           
            if root is None:
                return

            

            temp = root.left
            root.left = root.right
            root.right = temp
                # return

          

            dfs(root.left)
            dfs(root.right)
          
            return root
        
        return dfs(root)