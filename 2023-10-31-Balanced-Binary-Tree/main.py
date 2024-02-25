'''
https://leetcode.com/problems/balanced-binary-tree/
Given a binary tree, determine if it is height-balanced
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        leftHeight = self.countHeight(root.left)
        rightHeight = self.countHeight(root.right)
        if(rightHeight - leftHeight > 1 or leftHeight - rightHeight > 1):
            return False
        else:
            return True

    def countHeight(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        #node = leaf
        if(root.left is None and root.right is None):
            return 1
        else:
            return 1 + max(self.countHeight(root.left), self.countHeight(root.right))

if __name__ == '__main__':
    solution=Solution()

    root, node1, node2, node3, node4 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    print(solution.isBalanced(root))

    root, node1, node2, node3, node4, node5, node6 = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(3), TreeNode(4), TreeNode(4)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5
    node3.right = node6
    print(solution.isBalanced(root))