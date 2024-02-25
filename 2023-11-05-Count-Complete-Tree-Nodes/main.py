'''
https://leetcode.com/problems/count-complete-tree-nodes/
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return (1 + self.countNodes(root.left) + self.countNodes(root.right))


if __name__ == '__main__':
    solution = Solution()

    root,  node2, node3, node4,node5, node6 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    root.left, root.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left = node6

    print(solution.countNodes(root))