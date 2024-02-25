'''
https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
'''
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = self.generate(rowIndex+1)
        return rows[rowIndex]
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            #print(f'i={i}')
            row=[]
            row.append(1)
            #print('row:', row)
            #print ("rows[i-1].__len__()",rows[i-1].__len__())
            for j in range(0, rows[i-1].__len__()+1):
                #print('j=', j)
                if(j == 0):
                    row[j]=1
                    #print("appending:1 ")
                elif j == rows[i-1].__len__():
                    #print("appending 1")
                    row.append(1)
                else:
                    row.append(rows[i-1][j-1]+rows[i-1][j])
            #print(f"row: {row}\n")
            rows.append(row)
        return rows

if __name__ == '__main__':
    solution = Solution()
    row = solution.getRow(3)
    for num in row:
        print(f'{num},')