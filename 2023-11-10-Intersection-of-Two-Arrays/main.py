'''
https://leetcode.com/problems/intersection-of-two-arrays/
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
'''

from typing import List
#easy solution
# class Solution:
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         set1,set2 = set(nums1), set(nums2)
#         return set1.intersection(set2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num in nums1:
            if num in nums2:
                if num not in intersection:
                    intersection.append(num)
        return intersection

if __name__ == '__main__':
    print(Solution().intersection([1,2,2,1],[2,2]))
