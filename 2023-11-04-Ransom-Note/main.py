'''
https://leetcode.com/problems/ransom-note/
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine:
                #print ('char:', char)
                magazine =magazine.replace(char, '', 1)
                #print("magazine", magazine)
            else:
                return False
        return True

if __name__ == '__main__':
    print(Solution().canConstruct('aa', 'ab'))