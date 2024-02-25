'''
https://leetcode.com/problems/pascals-triangle/
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
'''
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for i in range(1, numRows):
            print(f'i={i}')
            row=[]
            row.append(1)
            print('row:', row)
            print ("rows[i-1].__len__()",rows[i-1].__len__())
            for j in range(0, rows[i-1].__len__()+1):
                print('j=', j)
                if(j == 0):
                    row[j]=1
                    print("appending:1 ")
                elif j == rows[i-1].__len__():
                    print("appending 1")
                    row.append(1)
                else:
                    row.append(rows[i-1][j-1]+rows[i-1][j])
            print(f"row: {row}\n")
            rows.append(row)
        return rows


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    rows = solution.generate(5)
    for row in rows:
        print(f'[')
        for num in row:
            print(f'{num},')
        print(f"]\n")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
