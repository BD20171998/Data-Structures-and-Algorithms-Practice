"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        temp = head 
        i = 0

        while temp:
            i = i+1
            temp = temp.next

        if i == 2:
            return head.next

        temp = head
        length = i//2
        
        while length>=1:
           
            length = length - 1
            temp = temp.next
            

        return temp