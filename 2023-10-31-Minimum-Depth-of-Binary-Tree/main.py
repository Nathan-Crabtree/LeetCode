'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
'''
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.max = 100
        if(root is None):
            return 0
        if(root.left and root.right):
            return min(self.countMinHeight(root.left), self.countMinHeight(root.right))+1
        elif(root.left):
            return self.countMinHeight(root.left)+1
        elif(root.right):
            return self.countMinHeight(root.right)+1
        elif(root):
            return 1
    def countMinHeight(self, root: Optional[TreeNode]) ->int:
        if(root is None):
            return 0
        if(root.left and root.right):
            print("root: ", root.val, "root.left", root.left.val, "root.right", root.right.val)
            return min(self.countMinHeight(root.left) + 1, self.countMinHeight(root.right) + 1)
        elif root.left:
            print("root: ", root.val, "root.left", root.left.val)
            return self.countMinHeight(root.left) + 1
        elif root.right:
            print("root: ", root.val, "root.right", root.right.val)
            return self.countMinHeight(root.right) + 1
        else:
            print("leaf")
            return 1

if __name__ == '__main__':
    solution=Solution()

    root, node1, node2, node3, node4 = TreeNode(3), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    print(solution.minDepth(root))

    root, node1, node2, node3, node4 = TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(6)
    root.right = node1
    node1.right = node2
    node2.right = node3
    node3.right = node4
    print(solution.minDepth(root))