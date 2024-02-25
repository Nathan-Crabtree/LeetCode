'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
DOESN'T WORK!!! CORRECT SOLUTION BUT INPUT OFF
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head



if __name__ == '__main__':
    solution=Solution()
    print(solution.deleteDuplicates([1,1,2]))
    print(solution.deleteDuplicates([1,1,2,3,3]))