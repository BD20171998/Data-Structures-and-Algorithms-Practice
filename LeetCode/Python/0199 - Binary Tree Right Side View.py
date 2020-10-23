'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return None
        
        result = []
        queue =[root]
        while len(queue) >0:
        
            size = len(queue)
            
            result.append(queue[-1].val)
            
            for i in range(size):
                current = queue.pop(0)

                if current.left:
                    queue.append(current.left)
        
                if current.right:
                    queue.append(current.right)
        
        return result