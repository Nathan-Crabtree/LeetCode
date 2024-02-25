'''
https://leetcode.com/problems/binary-tree-preorder-traversal/
Given the root of a binary tree, return the preorder traversal of its nodes' values.
root, left, right
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        if root.left and root.right:
            return [root.val]+ self.preorderTraversal(root.left)+ self.preorderTraversal(root.right)
        if root.left:
            return [root.val] + self.preorderTraversal(root.left)
        if root.right:
            return [root.val] + self.preorderTraversal(root.right)

if __name__ == '__main__':
    root, node1, node2 = TreeNode(1), TreeNode(2), TreeNode(3)
    root.right = node1
    node1.left = node2
    solution = Solution()
    print(solution.preorderTraversal(root))
