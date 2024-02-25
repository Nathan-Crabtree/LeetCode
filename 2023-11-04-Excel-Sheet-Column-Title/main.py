'''
https://leetcode.com/problems/excel-sheet-column-title/
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result.append(chr(65 + remainder))
        return ''.join(reversed(result))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution = Solution()
    print(solution.convertToTitle(1))
    print(solution.convertToTitle(28))
    print( solution.convertToTitle(701))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
