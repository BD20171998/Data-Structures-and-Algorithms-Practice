'''
Sibling Tree Value

You are given an integer k and a binary search tree root, 
where each node is either a leaf or contains 2 children.

Find the node containing the value k, and return its sibling's value.
'''

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def solve(self, root, k):

    queue = [root]

    while len(queue) > 0:

        size = len(queue)

        for i in range(size):

            curr = queue.pop(0)

            if curr.left is not None:
                queue.append(curr.left)

            if curr.right is not None:
                queue.append(curr.right)

            if curr.left:
                if curr.left.val == k and curr.right:
                    return curr.right.val

            if curr.right:
                if curr.right.val == k and curr.left:
                    return curr.left.val
