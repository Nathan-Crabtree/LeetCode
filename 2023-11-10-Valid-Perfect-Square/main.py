'''
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num==1:
            return True
        left, right = 0, num
        prevMid = -1
        mid = 0
        while left < right and prevMid != mid:
            prevMid = mid
            mid = (right+left)//2
            print ("MID:", mid)
            print('right:', right)
            print('left', left)
            if mid * mid > num:
                right = mid
            if mid * mid < num:
                left = mid
            if mid * mid == num:
                return True

        return False

if __name__ == '__main__':
    print(Solution().isPerfectSquare(14))