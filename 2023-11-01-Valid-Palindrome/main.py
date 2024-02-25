'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s=re.sub("[^A-Za-z0-9]+", "", s)
        print("s: ", s)
        i = 0
        j = len(s)-1
        while i < j:
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome(" "))