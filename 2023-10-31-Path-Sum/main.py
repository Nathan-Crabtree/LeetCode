'''
https://leetcode.com/problems/path-sum/
Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        flag = False
        if not root:
            return flag
        return(self.calculatePathSum(root, targetSum, 0, flag))
    def calculatePathSum(self, node: Optional[TreeNode], targetSum: int, currentSum: int, flag: bool) -> bool:
        if(node is None):
            return False
        currentSum += node.val
        print("NODE.val: ", node.val, "CurrentSum:", currentSum)
        if(node.left is None and node.right is None):
            print('hi')
            if(currentSum == targetSum):
                print('hi2')
                return True
            else:
                print('hi3')
                return False
        if(flag):
            return flag
        if(node.left and node.right is None):
            return self.calculatePathSum(node.left, targetSum, currentSum, flag)
        if(node.right and node.left is None):
            print('bye')
            return self.calculatePathSum(node.right, targetSum, currentSum, flag)
        if(node.right and node.left):
            if(self.calculatePathSum(node.left, targetSum, currentSum, flag)):
                return True
            if(self.calculatePathSum(node.right, targetSum, currentSum, flag)):
                return True
        return False

if __name__ == '__main__':

    solution = Solution()

    root, node1, node2, node3, node4, node5, node6, node7, node8 = TreeNode(5), TreeNode(4), TreeNode(8), TreeNode(11), TreeNode(13),TreeNode(4),TreeNode(7),TreeNode(2),TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.right = node8

    print(solution.hasPathSum(root, 22))

    root, node1, node2 = TreeNode(1), TreeNode(2), TreeNode(3)
    root.left = node1
    root.right = node2
    print(solution.hasPathSum(root, 5))

    root, node1 = TreeNode(-2), TreeNode(-3)
    root.right = node1
    print(solution.hasPathSum(root, -5))
