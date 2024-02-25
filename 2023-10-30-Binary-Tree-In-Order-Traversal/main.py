'''
https://leetcode.com/problems/binary-tree-inorder-traversal/
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l1, l2, l3, l4, l5 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)
    l4.left = l2
    l4.right = l5
    l2.left = l1
    l2.right = l3
    solution = Solution()
    print(solution.inorderTraversal(l4))