'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Given an integer array nums where the elements are sorted in ascending order, convert it to a
height-balanced binary search tree.
'''

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if not n:
            return None
        mid = (n-1)//2
        #print(f'n:{n}, mid:{mid}')
        root = TreeNode(nums[mid])
        #print(f"NODE: {root.val}")
        for num in nums:
            #print(f'num:{num}')
            pass
        if(nums.__len__() > 1):
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def printTree(self, root: Optional[TreeNode]):
        if(root.left is None and root.right is None):
            print(f'{root.val},')
            return
        elif (root.left and root.right is None):
            self.printTree(root.left)
        elif (root.right and root.left is None):
            self.printTree(root.right)
        elif (root.right and root.left):
            self.printTree(root.left)
            self.printTree(root.right)
        print(f'{root.val},')

if __name__ == '__main__':
    solution=Solution()
    root = solution.sortedArrayToBST([-10,-3,0,5,9])
    solution.printTree(root)