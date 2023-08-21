"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        temp2 = headB
        
        seen =  set()
            
        
        while temp1 is not None:
            
            seen.add(temp1)
            temp1 = temp1.next

        while temp2 is not None:

            if temp2 in seen:
                return temp2
            else:

                temp2 = temp2.next

            
        return None