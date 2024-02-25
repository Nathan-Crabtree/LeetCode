'''
https://leetcode.com/problems/intersection-of-two-linked-lists/
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional

#TOO SLOW
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         aNodes = []
#         bNodes = []
#         currentNode = headA
#         while(currentNode):
#             aNodes.append(currentNode)
#             currentNode=currentNode.next
#         currentNode = headB
#         while (currentNode):
#             bNodes.append(currentNode)
#             currentNode = currentNode.next
#         for aNode in aNodes:
#             for bNode in bNodes:
#                 if aNode == bNode:
#                     return aNode

#ALSO TOO SLOW
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         nodes =[]
#
#         while(headA or headB):
#             if(headA == headB):
#                 return headA
#             for i in range(0, nodes.__len__()):
#                 if(nodes[i]==headA or nodes[i] == headB):
#                     return nodes[i]
#             if(headA):
#                 nodes.append(headA)
#                 headA = headA.next
#             if(headB):
#                 nodes.append(headB)
#                 headB = headB.next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        while headA:
            s.add(headA)
            headA=headA.next
        while headB:
            if headB in s:
                return headB
            headB=headB.next
        return None

if __name__ == '__main__':
    a1, a2 = ListNode(4), ListNode(1)
    b1, b2, b3 = ListNode(5), ListNode(6), ListNode(1)
    c1, c2, c3 = ListNode(8), ListNode(4), ListNode(5)
    a1.next = a2
    a2.next = c1
    b1.next = b2
    b2.next = b3
    b3.next = c1
    c1.next = c2
    c2.next = c3
    solution = Solution()
    print(solution.getIntersectionNode(a1, b1).val)