'''
https://leetcode.com/problems/reverse-vowels-of-a-string/
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u',
and they can appear in both lower and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        i=0
        vowelIndices=[]
        while i < s.__len__():
            if s[i] in vowels:
                vowelIndices.append(i)
            i+=1
        i,j=0, vowelIndices.__len__()-1
        sList = list(s)
        while i < j:
            sList[vowelIndices[i]], sList[vowelIndices[j]] = sList[vowelIndices[j]], sList[vowelIndices[i]]
            i+=1
            j-=1
        return ''.join(sList)
if __name__ == '__main__':
    print(Solution().reverseVowels('leetcode'))