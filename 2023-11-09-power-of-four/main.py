'''
https://leetcode.com/problems/power-of-four/
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
'''


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while 4 ** i <= n:
            if 4 ** i == n:
                return True
            i+=1
        return False


if __name__ == '__main__':
    print(Solution().isPowerOfFour(16))
    print(Solution().isPowerOfFour(5))
    print(Solution().isPowerOfFour(1))
