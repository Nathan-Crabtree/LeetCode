'''
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while(head):
            vals.append(head.val)
            head = head.next
        if(len(vals)==1):
            return True
        i = 0
        j = len(vals)-1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    solution = Solution()
    head, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
    print(solution.isPalindrome(head))