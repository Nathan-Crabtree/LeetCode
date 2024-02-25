'''
https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.'''


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for num in nums:
            if(num in numsDict):
                numsDict[num]+=1
            else:
                numsDict[num] = 1
            if(numsDict[num] > nums.__len__() /2):
                return num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement([3,2,3]))
    print(solution.majorityElement([2,2,1,1,1,2,2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
