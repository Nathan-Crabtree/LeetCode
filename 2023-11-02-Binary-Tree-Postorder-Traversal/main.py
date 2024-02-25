'''
https://leetcode.com/problems/binary-tree-postorder-traversal/
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]

if __name__ == '__main__':
    root, node1, node2, node3, node4 = TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(2)
    root.left= node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    solution = Solution()
    print(solution.postorderTraversal(root))