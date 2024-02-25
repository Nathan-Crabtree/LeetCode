'''
https://leetcode.com/problems/first-bad-version/
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''


def isBadVersion(version: int) -> bool:
    if version >= 4:
        return True
    else:
        return False

# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#
#         firstBadVersion
#         previousN = n
#         previousRange = range(0,n)
#
#         while (isBadVersion(n//5)):
#             previousN = n
#             n = n//5
#         if n == previousN
#             return n
#         badRange = range(n, previousN)

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, ans = 1, n, -1

        while l <= r:
            mid = (l + r) >> 1
            if isBadVersion(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans



if __name__ == '__main__':
    solution = Solution()
    print(solution.firstBadVersion(5))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
