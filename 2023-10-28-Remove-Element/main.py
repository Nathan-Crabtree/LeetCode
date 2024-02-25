'''
https://leetcode.com/problems/remove-element/
'''
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = 0
        while (i < nums.__len__()):
            if(nums[i] == val):
                nums.pop(i)
            else:
                i+=1;
                k+=1
        return k

if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    print(solution.removeElement(nums, val))
    print(f'nums={nums} val={val}')
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(solution.removeElement(nums, val))
    print(f'nums={nums} val={val}')

