'''
https://leetcode.com/problems/is-subsequence/
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

#didn't work
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         sCopy = s
#         if s == t:
#             return True
#         for char in t:
#             if char in s:
#                 s=s.replace(char, '',1)
#                 t=t.replace(char, '', 1)
#         if t != sCopy:
#             return False
#         else:
#             return True

class Solution:
def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) > len(t): return False
    if len(s) == 0: return True
    subsequence = 0
    for i in range(0, len(t)):
        if subsequence <= len(s) - 1:
            print(s[subsequence])
            if s[subsequence] == t[i]:
                subsequence += 1
    return subsequence == len(s)

if __name__ == '__main__':
    print(Solution().isSubsequence('abc', 'ahbgdc'))
    print(Solution().isSubsequence('ab', 'baab'))