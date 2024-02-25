
class Solution:
    def isSymmetric(self, node1: Optional[TreeNode], node2: Optional[TreeNode] ) -> bool:
        if(node1 is None and node2 is None):
            #print("case1")
            return True
        if(node1 and node2 is None):
            #print("case2")
            return False
        if(node1 is None and node2):
            #print("case3")
            return False
        #print(f'node1: {node1.val}, node2: {node2.val}')
        if(node1.val != node2.val):
            return False
        if node1.left and node2.right and (node1.left.val != node2.right.val):
            return False
        if node1.right and node2.left and (node1.right.val != node2.left.val):
            return False
        if(self.isSymmetric(node1.left, node2.right) and self.isSymmetric(node1.right, node2.left)):
            return True
        return False

if __name__ == '__main__':
    solution = Solution()

    root, node1, node2, node3, node4, node5, node6 = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(4),TreeNode(4), TreeNode(3)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    print(solution.isSymmetric(root.left, root.right))

    root, node1, node2, node3, node4, = TreeNode(1), TreeNode(2), TreeNode(2), TreeNode(3), TreeNode(3)
    root.left = node1
    root.right = node2
    node1.right = node3
    node2.right = node4
    print(solution.isSymmetric(root.left, root.right))
