'''
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
'''

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
            i, j = 0, len(s)-1
            while i < j:
                temp = s[i]
                s[i]=s[j]
                s[j]=temp
                i+=1
                j-=1


if __name__ == '__main__':
    str=['h', 'e', 'l', 'l', 'o']
    Solution().reverseString(str)
    print(str)
