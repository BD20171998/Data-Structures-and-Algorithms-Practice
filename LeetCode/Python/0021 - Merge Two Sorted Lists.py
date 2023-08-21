'''
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      
        head = temp = ListNode(-1)
        
        while list1 and list2:

          
            if list1.val <= list2.val:

                temp.next = list1
               
                list1 = list1.next

            elif list1.val > list2.val:

                temp.next = list2
                list2 = list2.next

            temp = temp.next
        
        if list1 is not None:
           
            temp.next = list1

        elif list2 is not None:
          
            temp.next = list2
        return head.next