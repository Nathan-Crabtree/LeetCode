'''
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         dict = {}
#         words = s.split(' ')
#         #print("pattern: ", pattern)
#         #print ("words:", words)
#         #print(len(words))
#         #print(pattern  .__len__())
#         if len(words) != pattern.__len__():
#             return False
#         for i, char in enumerate(pattern):
#             if char not in dict:
#                 dict[char]= words[i]
#             #print('i == ',i)
#             #print('dict[char] == ', dict[char])
#             #print('words[i] == ', words[i])
#             if(dict[char]!=words[i]):
#                 return False
#         values = list(dict.values())
#         if len(values) == len(set(values)):
#             return True
#             #print("no duplicates")
#         else:
#             return False
#             #print("duplicates)
#         return True

#better solution
from itertools import zip_longest
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        print ("pattern set len: ", len(set(pattern)))
        print ("s set len: ", len(set(s)))
        print ("zip longest:")
        print(list(zip_longest(pattern,s)))
        print ("zip longest set len:")
        print(len(set(zip_longest(pattern, s))))
        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))

if __name__ == '__main__':
    print(Solution().wordPattern('abba', 'dog cat cat dog'))
    print(Solution().wordPattern('abba', 'dog cat cat fish'))
    print(Solution().wordPattern('aaaa', 'dog cat cat dog'))
    print(Solution().wordPattern('abba', 'dog dog dog dog'))



