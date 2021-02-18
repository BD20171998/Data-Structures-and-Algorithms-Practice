'''
Kth Last Node of a Linked List

Given a singly linked list node, 
return the value of the kth last 
node (0-indexed). k is guaranteed 
not to be larger than the size of 
the linked list.

This should be done in 
O(1)space.
'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node, k):

        length = 0
        temp = node
        while temp.next is not None:
            length += 1
            temp = temp.next

        temp = node
        i = 0
        while i < length-k:
            temp = temp.next
            i += 1
        return temp.val
