# https://leetcode.com/problems/sum-of-left-leaves/description/
# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional 
class Solution:
    def __init__(self):
        self.sum = 0;
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft: bool) -> int:
        # print("root val: ", root.val)
        # print("sum: ", self.sum)
        # print("isLeft: ",isLeft)
        # print("")

        if root is None:
            return 0
        if root.left is None and root.right is None:
            if (isLeft):
                #print("IS LEFT LEAF")
                self.sum = self.sum + root.val
                return root.val
            else:
                return 0

        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)  
        
if __name__ == '__main__':
    root, node1, node2, node3, node4 = TreeNode(3), TreeNode(9),TreeNode(20),TreeNode(15),TreeNode(7)
    root.left, root.right = node1, node2
    node2.left, node2.right = node3,node4
    print(Solution().sumOfLeftLeaves(root, False))

    root = TreeNode(1)
    root.left, root.right = None, None
    print(Solution().sumOfLeftLeaves(root, True))