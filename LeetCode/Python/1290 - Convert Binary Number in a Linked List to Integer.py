'''
1290. Convert Binary Number in a Linked List to Integer
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''

def getDecimalValue(self, head: ListNode) -> int:
        
        nodeList = []        
        ans = 0 

        while head:            
            nodeList.insert(0,head.val)
            head = head.next

        for i in range(len(nodeList)):
            if nodeList[i] == 1:
                ans += 2 ** i

        return ans