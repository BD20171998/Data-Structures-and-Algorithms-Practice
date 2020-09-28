'''
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        ans = Node(0)
        workingAns = ans
        randomDict = {None: None}
        randomUpdateList = []

        while head:
            workingAns.next = Node(head.val, head.next, head.random)
            workingAns.next = Node(head.val, head.next, head.random)
            workingAns = workingAns.next
            randomDict[head] = workingAns

            if workingAns.random in randomDict:
                workingAns.random = randomDict[workingAns.random]
            else:
                randomUpdateList.append(workingAns)
            head = head.next

        while randomUpdateList != []:
            randomUpdateList[-1].random = randomDict[randomUpdateList[-1].random]
            randomUpdateList.pop()

        return ans.next
