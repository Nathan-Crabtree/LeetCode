'''
https://leetcode.com/problems/invert-binary-tree/
Given the root of a binary tree, invert the tree, and return its root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root
        tempNode = None
        if root.left and root.right:
            print("hi")
            tempNode = root.left
            root.left = root.right
            root.right = tempNode
            self.invertTree(root.left)
            self.invertTree(root.right)
        elif root.right:
            print('Hi')
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        elif root.left:
            print('HI')
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        return root

if __name__ == '__main__':
    root, node2, node3, node4, node5, node6, node7 = TreeNode(4), TreeNode(2), TreeNode(1), TreeNode(3), TreeNode(7), TreeNode(6), TreeNode(8)
    root.left, root.right = node2, node5
    node2.left,node2.right = node3, node4
    node5.left, node5.right = node6,node7

    solution = Solution()
    solution.invertTree(root)