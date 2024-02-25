'''
https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while(list1 and list2):
            if(list1.val < list2.val):
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    input_list_1 = [1, 2, 4]
    input_list_2 = [1, 2, 4]
    nodes_1 = [ListNode(val=i) for i in input_list_1]
    nodes_2 = [ListNode(val=i) for i in input_list_2]
    for i in range(len(nodes_1) - 1):
        nodes_1[i].next = nodes_1[i + 1]
    for i in range(len(nodes_2) - 1):
        nodes_2[i].next = nodes_2[i + 1]

    solution_list_node = solution.mergeTwoLists(nodes_1[0], nodes_2[0])
    print(solution_list_node.val)
    while(solution_list_node.next):
        solution_list_node = solution_list_node.next
        print(solution_list_node.val)


