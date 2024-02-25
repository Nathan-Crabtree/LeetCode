'''
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
'''

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #Do not return anything, modify nums in-place instead.
        i = 0
        len = nums.__len__()
        while i < len:
            print("i=",i)
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                print ("nums: ", nums)
                i -=1
                len -=1
            i+=1
    #Faster:
    # class Solution:
    #     def moveZeroes(self, nums: List[int]) -> None:
    #         """
    #         Do not return anything, modify nums in-place instead.
    #         """
    #         left = 0
    #         for right in range(len(nums)):
    #             if nums[right] != 0:
    #                 nums[right], nums[left] = nums[left], nums[right]
    #                 left += 1


if __name__ == '__main__':
    arr = [0,1,0,3,12]
    Solution().moveZeroes(arr)
    print (arr)
    arr = [0]
    Solution().moveZeroes(arr)
    print(arr)
    arr = [0, 0,1]
    Solution().moveZeroes(arr)
    print(arr)

