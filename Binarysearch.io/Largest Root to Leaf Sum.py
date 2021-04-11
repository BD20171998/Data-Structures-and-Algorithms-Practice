'''
Largest Root to Leaf Sum

Given the root to a binary 
tree root, return the largest 
sum of any path that goes from 
the root to a leaf.
'''
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root):

        if root is None:
            return 0
        maximum = 0

        path = []

        def dfs(root):
            nonlocal path, maximum

            path.append(root.val)

            if root.left is None and root.right is None:
                print(path)
                if maximum <= sum(path):
                    maximum = sum(path)

                return

            if root.left:
                dfs(root.left)
                path.pop()

            if root.right:
                dfs(root.right)
                path.pop()

        dfs(root)
        return maximum
