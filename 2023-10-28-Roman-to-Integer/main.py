'''
https://leetcode.com/problems/roman-to-integer/
Given a roman numeral, convert it to an integer.
'''

class Solution:
    numeralValues = {'I': 1, 'V': 5, 'X':10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    def romanToInt(self, s: str) -> int:
        sum = 0
        i = 0
        while i < s.__len__():
            if(i == s.__len__()-1):
                sum += self.numeralValues[s[i]]
                return sum
            if(s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')):
                sum += (self.numeralValues[s[i+1]] - self.numeralValues[s[i]])
                i+=2
                continue
            if(s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')):
                sum += (self.numeralValues[s[i+1]] - self.numeralValues[s[i]])
                i+=2
                continue
            if(s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M')):
                sum += (self.numeralValues[s[i+1]] - self.numeralValues[s[i]])
                i+=2
                continue
            sum += self.numeralValues[s[i]]
            i+=1
        return sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt(('CIV')))
    print(solution.romanToInt(('LVIII')))
    print(solution.romanToInt(('MCMXCIV')))
