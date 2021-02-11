
'''
Linked List to Integer

Given a single linked list node, representing a binary number with 
most significant digits first, return it as an integer.
'''
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):

        binary = ""

        while node:

            binary += str(node.val)
            node = node.next

        return int(binary, 2)
