'''
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniqueDict = {}
        if len(s) == 1:
            return 0
        for i in range(len(s)):
            print(f"s[{i}]", s[i])
            if (s[i] not in uniqueDict):
                uniqueDict[s[i]] = True
                #print(uniqueDict.keys())
                print(f"uniqueDict{s[i]}: True")
                for j in range(i+1, len(s)):
                    print("s[j]", s[j])
                    if(s[j]==s[i]):
                        print(f"uniqueDict{s[i]}: False")
                        uniqueDict[s[i]] = False
                        break
            if uniqueDict[s[i]] is True:
                return i
        return -1

if __name__ == '__main__':
    #print(Solution().firstUniqChar('leetcode'))
    #print(Solution().firstUniqChar('loveleetcode'))
    #print(Solution().firstUniqChar('z'))
    print(Solution().firstUniqChar("dddccdbba"))
