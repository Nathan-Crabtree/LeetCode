'''
https://leetcode.com/problems/binary-tree-paths/
Given the root of a binary tree, return all root-to-leaf paths in any order.
A leaf is a node with no children.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def __init__(self):
        self.res = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if root is None:
        #     return []
        # if root.left is None and root.right is None:
        #     return f"{root.val}"
        # if root.left and root.right:
        #     return [f"{root.val}->]+self.binaryTreePaths(root.left)], f"{root.val}->" + self.binaryTreePaths(root.right)]
        # if root.left:
        #     return [f"{root.val}->" + self.binaryTreePaths(root.left)]
        # if root.right:
        #     return [f"{root.val}->" + self.binaryTreePaths(root.right)]
        if not root:
            return [];
        if root.val:
            self.helper(root, '')
            return self.res

    def helper (self, node: Optional[TreeNode], arr):
        newarr = arr + str(node.val)
        if not node.left and not node.right:
            self.res.append(newarr);
            return
        else:
            newarr += "->"
            if node.left:
                self.helper(node.left, newarr)
            if node.right:
                self.helper(node.right, newarr)
        return

if __name__ == '__main__':
    root, node2, node3, node4 = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(5)
    root.left, root.right, node2.left = node2, node3, node4
    solution=Solution()
    print(solution.binaryTreePaths(root))