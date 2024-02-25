'''
https://leetcode.com/problems/merge-sorted-array/
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j=0
        nums3 = []
        while i < nums1.__len__() and j < nums2.__len__():
            if(nums1[i]<nums2[j] and nums1[i]!=0):
                nums3.append([nums1[i]])
                i+=1
            else:
                nums3.append([nums2[j]])
                j+=1
        while i < nums1.__len__():
            if nums1[i] != 0:
                nums3.append(nums1[i])
            i+=1
        while j < nums2.__len__():
            if nums2[j] != 0:
                nums3.append(nums2[j])
            j+=1
        k = 0
        while k < nums3.__len__():
            if k < nums1.__len__():
                nums1[k]=nums3[k]
            else:
                nums1.append(nums3[k])
            k+=1
        print("nums1:", nums1)


if __name__ == '__main__':
    solution = Solution()
    solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    solution.merge([1], 1, [], 0)
    solution.merge([], 0, [1], 1)


