'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
from typing import List
class Solution:
    def removeDuplicates(self,  nums: List[int]) -> int:
        solutionList = []
        k = 0
        for i in range(0, nums.__len__()):
            if i == 0:
                solutionList.append(nums[i])
                k+=1
                continue
            if(nums[i] != nums[i-1]):
                solutionList.append(nums[i])
                k+=1
            else:
                continue
        #print(f'solutionlist: {solutionList}')
        for i in range(0, solutionList.__len__()):
            nums[i]=solutionList[i]
        #print(f'i={i}')
        j = nums.__len__()
        while i < j-1:
            nums.pop()
            i+=1
        return k

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,2]
    print(solution.removeDuplicates(nums))
    print(nums)
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))
    print(nums)

