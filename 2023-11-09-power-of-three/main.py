'''
https://leetcode.com/problems/power-of-three/
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(n >= 1):
            if n==1:
                return True
            n=n/3
        return False
if __name__ == '__main__':
    print(Solution().isPowerOfThree(27))
    print(Solution().isPowerOfThree(0))
    print(Solution().isPowerOfThree(-1))

