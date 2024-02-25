'''
https://leetcode.com/problems/length-of-last-word/
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        return(word_list[-1].__len__())

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord('Hello World'))
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))
    print(solution.lengthOfLastWord("luffy is still joyboy"))

