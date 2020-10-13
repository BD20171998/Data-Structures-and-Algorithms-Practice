/**
148. Sort List
https://leetcode.com/problems/sort-list/
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
class Solution
{
public:
    ListNode *sort(ListNode *head, int length)
    {
        int i = 0;
        if (length == 1)
            return head;

        ListNode *sub_head1 = head, *sub_head2 = NULL;

        while (i < length / 2 - 1)
        {
            sub_head1 = sub_head1->next;
            i++;
        }

        sub_head2 = sub_head1->next;
        sub_head1->next = NULL;
        sub_head1 = head;

        sub_head1 = sort(sub_head1, length / 2);
        sub_head2 = sort(sub_head2, length - length / 2);

        return merge(sub_head1, sub_head2);
    }

public:
    ListNode *merge(ListNode *list1, ListNode *list2)
    {
        ListNode *merged_list, *merged_list_copy;

        if (list1->val < list2->val)
        {
            merged_list = list1;
            list1 = list1->next;
        }

        else
        {
            merged_list = list2;
            list2 = list2->next;
        }

        merged_list_copy = merged_list;

        while (list1 && list2)
        {
            if (list1->val < list2->val)
            {
                merged_list->next = list1;
                list1 = list1->next;
            }

            else
            {
                merged_list->next = list2;
                list2 = list2->next;
            }

            merged_list = merged_list->next;
        }

        if (!list1)
            merged_list->next = list2;

        else
            merged_list->next = list1;

        return merged_list_copy;
    }

public:
    ListNode *sortList(ListNode *head)
    {

        if (!head)
            return NULL;

        int length = 0;

        ListNode *temp = head;

        while (temp != NULL)
        {
            ++length;
            temp = temp->next;
        }

        return sort(head, length);
    }
};