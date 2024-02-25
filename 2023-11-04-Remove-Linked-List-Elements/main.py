'''https://leetcode.com/problems/remove-linked-list-elements/
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        while head and head.val == val:
            head = head.next
        if not head:
            return None
        currentNode = head.next
        previousNode = head
        while(currentNode):
            if(currentNode.val == val):
                previousNode.next = currentNode.next
                currentNode = currentNode.next
                print("removing ", val)
                continue
            previousNode = currentNode
            currentNode = currentNode.next
        return head

if __name__ == '__main__':
    solution = Solution()
    root, node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5), ListNode(6)
    root.next=node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution.removeElements(root, 6)

    root, node1, node2, node3 = ListNode(7), ListNode(7), ListNode(7), ListNode(7)
    root.next=node1
    node1.next = node2
    node2.next = node3
    solution.removeElements(root, 7)
