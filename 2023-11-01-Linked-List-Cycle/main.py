'''
https://leetcode.com/problems/linked-list-cycle/
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        currentNode = head
        self.nodes = []
        while currentNode.next:
            for i in range(0, self.nodes.__len__()):
                if(currentNode.next == self.nodes[i]):
                    return True
            self.nodes.append(currentNode)
            currentNode = currentNode.next
        return False


if __name__ == '__main__':
    root, node1, node2, node3 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)

    root.next=node1
    node1.next=node2
    node2.next=node3
    node3.next=node1

    solution=Solution()
    print(solution.hasCycle(root))