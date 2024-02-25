'''
https://leetcode.com/problems/single-number/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(0,nums.__len__()):
            #print("i=",i)
            #print("nums[i]=",nums[i])
            if(nums[i] in numsDict):
                numsDict[nums[i]]+=1
            else:
                numsDict[nums[i]]=1
            #print("numsDict[nums[i]]=", numsDict[nums[i]])

        for key in numsDict:
            if (numsDict[key] == 1):
                #print("key=", key)
                #print("numsDict[key] =", numsDict[key])
                return key

if __name__ == '__main__':
    solution=Solution()
    print(solution.singleNumber([2,2,1]))
    print("")
    print(solution.singleNumber([4,1,2,1,2]))
    print("")
    print(solution.singleNumber([1]))