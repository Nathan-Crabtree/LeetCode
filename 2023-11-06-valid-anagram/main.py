'''
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(s.__len__() != t.__len__()):
            return False
        sDict = {}
        tDict = {}
        for c in s:
            if c not in sDict:
                sDict[c]=0
            sDict[c]+=1
        for c in t:
            if c not in tDict:
                tDict[c]=0
            tDict[c]+=1
        if sDict.keys() != tDict.keys():
            return False
        for key in sDict.keys():
            if(sDict[key] != tDict[key]):
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram('anagram', 'nagaram'))
    print(solution.isAnagram('rat', 'car'))
