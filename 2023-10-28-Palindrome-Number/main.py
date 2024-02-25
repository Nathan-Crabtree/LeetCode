'''
Given an integer x, return true if x is a
palindrome, and false otherwise.
https://leetcode.com/problems/palindrome-number/description/
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        intString = str(x)
        #negative numbers can't be palindromes
        if(intString[0] == '-'):
            return False
        i = 0
        j = -1
        while i < (intString.__len__() / 2):
            if(intString[i] != intString[j]):
                return False
            i+=1
            j-=1
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    #print(solution.isPalindrome(-121))
    #print(solution.isPalindrome(11211))
    print(solution.isPalindrome(11221))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
