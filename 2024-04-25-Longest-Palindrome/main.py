#https://leetcode.com/problems/longest-palindrome/description/
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for letter in s:
            #print("LETTER ", letter)
            if letter not in letters.keys():
                letters[letter]=0
            letters[letter] += 1
            #print("letter: ", letter, " count: ", letters[letter])
        palindrome = ''
        sum = 0
        for letter in s:
            if(letters[letter]%2==0):
                sum += letters[letter]
                letters[letter]=0
            elif letters[letter] > 1:
                sum += letters[letter]-1
                letters[letter]=1
        sum_odds = 0
        for letter in letters.keys():
            if letters[letter]==1:
                sum_odds +=1
        if sum_odds > 0:
            sum += 1
        return sum


print(Solution().longestPalindrome('a'))
print(Solution().longestPalindrome('abccccdd'))
