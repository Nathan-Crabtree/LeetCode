'''
https://leetcode.com/problems/excel-sheet-column-number/
Given a string columnTitle that represents the column title as appears in an Excel sheet,
return its corresponding column number.
'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        position = columnTitle.__len__();
        solution = 0
        for char in columnTitle:
            print ("position:", position)
            print(ord(char)-64)
            if(position >1):
                solution += (26 ** (position-1)) * (ord(char)-64)
            else:
                solution += (ord(char)-64)
            print("solution", solution)
            position -= 1
        return solution

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    print(solution.titleToNumber('A'))
    print(solution.titleToNumber('Z'))
    print(solution.titleToNumber('AA'))
    print(solution.titleToNumber('AB'))
    print("")
    print(solution.titleToNumber('ZY'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
