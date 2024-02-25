'''
https://leetcode.com/problems/missing-number/
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, nums.__len__()+1):
            if i == nums.__len__():
                return i
            if nums[i] != i:
                return i

        
#Faster Solution:
# class Solution(object):
#     def missingNumber(self, nums):
#         return list(set(range(0,len(nums)+1)).difference(set(nums)))[0]

if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([3,0,1]))
    print(solution.missingNumber([0,1]))
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))