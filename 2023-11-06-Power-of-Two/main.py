'''
https://leetcode.com/problems/power-of-two/
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        while n / 2 >= 1:
            if n / 2 == 1:
                return True
            n = n/2
        return False

#This works best:
        # def isPowerOfTwo(self, n: int) -> bool:
        #     if n <= 0:
        #         return False
        #     return math.log2(n) % 1 == 0

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPowerOfTwo(10))