'''
Pairwise Linked List Swap

Given a singly linked list node, 
swap each pair of nodes and return the new head.
'''
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):
        if node is None:
            return None
        temp = node

        while temp.next:

            if temp.next.next is None:
                temp.next.val, temp.val = temp.val, temp.next.val
                break

            temp.next.val, temp.val = temp.val,  temp.next.val
            temp = temp.next.next
        return node
