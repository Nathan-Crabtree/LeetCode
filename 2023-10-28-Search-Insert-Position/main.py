'''
https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
'''
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range (0, nums.__len__()):
            if nums[i] >= target:
                return i
            if(i+1 > nums.__len__()-1):
                return i + 1
            if(nums[i+1] > target):
                return i+1



if __name__ == '__main__':
    solution = Solution();
    print(solution.searchInsert([1,3,5,6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1,3,5,6], 7))
