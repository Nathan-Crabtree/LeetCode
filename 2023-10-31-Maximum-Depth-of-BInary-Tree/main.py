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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        else:
            return (max(self.maxDepth(root.left), self.maxDepth(root.right))+1)

if __name__ == '__main__':
    solution=Solution()

    root1, node1, node2, node3, node4 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    root1.left = node1
    root1.right = node2
    node3.left = node3
    node3.right = node4
    print(solution.maxDepth(root1))