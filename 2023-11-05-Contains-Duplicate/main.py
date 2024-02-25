'''
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''


from typing import List
class Solution:

    #Too Slow
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     seen = []
    #     for i in range(0, nums.__len__()):
    #         if nums[i] in seen:
    #             return True
    #         seen.append(nums[i])
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        return(len(nums) != len(set(nums)))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    print(solution.containsDuplicate([1,2,3,1]))
    print(solution.containsDuplicate([1,2,3,4]))
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
