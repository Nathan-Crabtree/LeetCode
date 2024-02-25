'''
https://leetcode.com/problems/plus-one/
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
'''
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits.__len__() == 1 and digits[0] == 9):
            digits[0]=1
            digits.append(0)
            return digits
        if(digits.__len__() == 1):
            digits[0]+=1
            return digits
        if(digits[-1] == 9):
            i = digits.__len__() - 1
            while (digits[i] == 9 and i >= 0):
                digits[i]=0
                i-=1
            if i == -1:
                digits.insert(0,1)
            else:
                digits[i]+=1
                print(digits)
            return digits
        else:
            digits[-1]+=1
            return digits

if __name__ == '__main__':
    solution = Solution()
    print(solution.plusOne([1,2,3]))
    print(solution.plusOne([4,3,2,1]))
    print(solution.plusOne([9]))
    print(solution.plusOne([9,9]))



