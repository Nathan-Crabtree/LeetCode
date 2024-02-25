'''
https://leetcode.com/problems/add-digits/
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''


class Solution:
    def addDigits(self, num: int) -> int:
        numStr = str(num)
        i = numStr.__len__() - 1
        while numStr.__len__() > 1:
            sum = 0
            i = 0
            while i < numStr.__len__():
                sum += int(numStr[i])
                i+=1
            i-=1
            numStr = str(sum)
        return int(numStr)

if __name__ == '__main__':
    solution=Solution()
    print(solution.addDigits(38))