'''
https://leetcode.com/problems/isomorphic-strings/
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
'''

#doesn't work
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if(s.__len__() != t.__len__())
#             return False
#         seenS = []
#         seenT = []
#         for i in range (0, s.__len__()):
#             charS = s[i]
#             charT = t[i]
#             if(charS == charT)
#                 continue
#             for j in range(i, s.__len__()):
#                 if(s[j]==s[i]):
#                     if(t[j] == t[i]):
#                         continue
#
#             for j in range (0 , i):
#                 if(s[i]==s[j])
#                     seenS[i]+=1
#                 else:
#                     seenS[i]=1
#                 if (t[i] == t[j])
#                     seenT[i] += 1
#                 else:
#                     seenJ[i]=1
#         for i in range(0, seenS.__len__()):
#             if(seenS[i] != seenT[i])
#                 return False
#         return True

class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            print('IdxS:', idx)
            map1.append(s.index(idx))
        for idx in t:
            print('IdxT:', idx)

            map2.append(t.index(idx))
        print("map1:", map1)
        print("map2:", map2)

        if map1 == map2:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic('egg', 'add'))
    print(solution.isIsomorphic('foo', 'bar'))
    print(solution.isIsomorphic('paper', 'title'))