'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
https://leetcode.com/problems/two-sum/
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = list()
        for i in range(0, nums.__len__()):
            for j in range(i+1, nums.__len__()):
                if(nums[i] + nums[j] == target):
                    solution.append(i)
                    solution.append(j)
        return(solution)

if __name__ == '__main__':
    solution = Solution()
    solution2 = solution.twoSum([0,1,2,3,4,5,6,7,8,9], 9)
    [print(i) for i in solution2]


