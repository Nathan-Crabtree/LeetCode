'''
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle == haystack):
            return 0
        #print(f'haystack.__len__() = {haystack.__len__()}')
        #print(f'needle.__len__() = {needle.__len__()}')
        for i in range(0, haystack.__len__() - needle.__len__() + 1):
            #print(f'i={i}')
            solution_found = True
            j=0
            while solution_found and j in range(0, needle.__len__()):
                #print(f'j={j}')
                if(needle[j] != haystack[i+j]):
                    solution_found = False
                j+=1
            if solution_found:
                return i
        return -1




if __name__ == '__main__':
    solution = Solution()
    haystack = "abc"
    needle = "c"
    print(solution.strStr(haystack, needle))

    haystack = "sadbutsad"
    needle = "sad"
    print(solution.strStr(haystack, needle))

    haystack = "leetcode"
    needle = "leeto"
    print(solution.strStr(haystack, needle))

    haystack = "aspnetbeansddjdbeanerbeanfuckbeans"
    needle = "bean"
    print(solution.strStr(haystack, needle))
