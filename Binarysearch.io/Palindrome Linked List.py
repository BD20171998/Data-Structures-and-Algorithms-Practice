'''
Palindrome Linked List

Given a singly linked list 
node whose values are integers, 
determine whether the linked list 
forms a palindrome.
'''
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def solve(self, node):
        count = 0
        temp = node
        data = []

        while temp:
            data.append(temp.val)
            temp = temp.next

        for i in range(len(data)):
            if data[i] != data[len(data)-1-i]:
                count += 1

        if count >= 2:
            return False
        else:
            return True
