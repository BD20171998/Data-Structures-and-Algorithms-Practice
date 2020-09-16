# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop


def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    
    new = root = ListNode()
    heap = []
    for i in range(len(lists)):
        node = lists[i]
        
        if node:
            heappush(heap, (node.val, i, node))
    
    while len(heap) > 0:
        temp = heappop(heap)
        new.next = temp[2]
        new = new.next
        
        if temp[2].next:
            heappush(heap, (temp[2].next.val,temp[1], temp[2].next))
                        
    return root.next