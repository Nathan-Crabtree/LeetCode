'''
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and q):
            if p.val != q.val:
                return False
            else:
                return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        elif (p and q is None):
            return False
        elif (p is None and q):
            return False
        else:
            return True


if __name__ == '__main__':
    solution=Solution()

    root1, root2, node2, node3 = TreeNode(1), TreeNode(1), TreeNode(2), TreeNode(3)
    root1.left = node2
    root1.right = node3
    root2.left = node2
    root2.right = node3
    print(solution.isSameTree(root1, root2))

    root1, root2, node2 = TreeNode(1), TreeNode(1), TreeNode(2)
    root1.left = node2
    root2.right = node2
    print(solution.isSameTree(root1, root2))

    root1, root2, node2, node3 = TreeNode(1), TreeNode(1), TreeNode(2), TreeNode(1)
    root1.left = node2
    root1.right = node3
    root2.left = node3
    root2.right = node2
    print(solution.isSameTree(root1, root2))