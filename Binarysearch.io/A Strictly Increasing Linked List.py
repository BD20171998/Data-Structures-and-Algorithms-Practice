'''
A Strictly Increasing Linked List

Given the head of a singly linked 
list head, return whether the values 
of the nodes are sorted in a strictly 
increasing order.
'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, head):

        if head.next is None:
            return True
        temp = head

        while temp.next is not None:

            if temp.next.val > temp.val:
                temp = temp.next

            else:
                return False

        return True
