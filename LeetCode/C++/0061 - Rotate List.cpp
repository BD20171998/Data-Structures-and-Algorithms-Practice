/*
61. Rotate List
https://leetcode.com/problems/rotate-list/
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        
        if (!head || k ==0)
            return head;
        
        int counter=1;
        ListNode *node=head, *first, *second;
        
        while (node->next)
        {
            counter+=1;
            node = node->next;
        }
        
        k %= counter;
        
        if (k == 0)
            return head;
        
        second = head;
        first = head;
        
        for (int i=0;i < k; i++)
            second= second->next;
        
        while (second->next)
        {
            second= second->next;
            first = first->next;
        }
        
        second->next = head;
        head = first->next;
        first->next= NULL;
        
        return head;
     
    }
};