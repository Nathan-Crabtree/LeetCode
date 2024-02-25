'''
https://leetcode.com/problems/ugly-number/
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
'''

#TOO SLOW
# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if abs(n) <= 1:
#             return True
#         if n < -1:
#             n = abs(n)
#
#         primes = []
#         for num in range(6, n):
#             prime = True
#             for i in range(2, num):
#                 if (num % i == 0):
#                     prime = False
#             if prime:
#                 primes.append(num)
#         for num in primes:
#             if n % num == 0:
#                 return False
#         return True

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(6))
    print(solution.isUgly(1))
    print(solution.isUgly(14))
    print(solution.isUgly(-4748))
