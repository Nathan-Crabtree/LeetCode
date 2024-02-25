'''
https://leetcode.com/problems/reverse-linked-list/
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeStack = []
        print("forward:")
        while(head):
            nodeStack.append(head)
            print(head.val)
            head = head.next

        print("reverse:")
        head = nodeStack.pop()
        print(head.val)
        node = head
        while len(nodeStack) != 0:
            print("NodeVal:", node.val)
            node.next = nodeStack.pop()
            print("node.nextval:", node.next.val)
            node = node.next

        print("head: ", head.val)
        print("head.next: ", node.next.val)
        print("head.next.next: ", node.next.next.val)
        print("head.next.next.next: ", node.next.next.next.val)
        print("head.next.next.next.next: ", node.next.next.next.next.val)

        return head


if __name__ == '__main__':
    solution = Solution()
    root, node1, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
    root.next, node1.next, node2.next, node3.next = node1, node2, node3, node4
    solution.reverseList(root)
