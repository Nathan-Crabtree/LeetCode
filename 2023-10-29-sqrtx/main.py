'''
https://leetcode.com/problems/sqrtx/
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        previous_root = 0
        current_root = 1;
        while True:
            print("current_root:", current_root)
            print("previous_root:", previous_root)

            if(current_root * current_root > x):
                return previous_root
            else:
                previous_root = current_root
                current_root += 1

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(44))