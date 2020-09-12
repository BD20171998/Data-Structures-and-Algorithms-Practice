'''
Linked list delete last occurrence of value

Given a singly linked list node, and an integer target, 
delete the last occurrence of target  in node.
'''


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

def solve(self, node, target):
    # Write your code here
    head = node
    temp = node
    location = float('-inf')
    index = 0
    
    if node.val == target and node.next is None:
        return None
        
    while temp:
        if temp.val == target:
            location = index
            
        index+= 1
        temp = temp.next
    
    if location == float('-inf'):
        return node
    
    if location == 0:
        return node.next
    
    for i in range(location-1):
        node = node.next
    
    node.next = node.next.next
    
    return head