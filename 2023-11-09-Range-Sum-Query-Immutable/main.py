'''
https://leetcode.com/problems/range-sum-query-immutable/
Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:
NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''
from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
            self.nums=nums
    def sumRange(self, left: int, right: int) -> int:
        sum=0
        for i in range(left,right+1):
            sum+=self.nums[i]
        return sum


if __name__ == '__main__':

    numArray=NumArray([-2,0,3,-5,2,-1])
    print(numArray.sumRange(0,2))
    print(numArray.sumRange(2,5))
    print(numArray.sumRange(0,5))