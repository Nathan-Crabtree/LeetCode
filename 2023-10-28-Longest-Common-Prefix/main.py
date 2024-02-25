'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
https://leetcode.com/problems/longest-common-prefix/
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #sort list of strings shortest to longest
        strs.sort(key=len)
        i = 0
        solution = ""
        for j in range(0, strs[0].__len__()):
            same = True
            for i in range(1, strs.__len__()):
                if(strs[i][j] != strs[0][j]):
                    same = False
            if(same):
                solution += strs[0][j]
        return solution

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
    print(solution.longestCommonPrefix(["dog","racecar","car"]))
    print(solution.longestCommonPrefix(["DDLLLDxx","DDLLLDyy","DDLLLDzz", "DDLLLDxx", "DDLLLDyy", "DDLLLDzz"]))


