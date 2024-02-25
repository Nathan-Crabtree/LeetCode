'''
NOT COMPLETE, INCORRECT, DOESN'T WORK!
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        solution = ''
        while i*-1 < a.__len__()-1 and i*-1 < b.__len__()-1:
            if(a[i] == '1' and b[i]=='1'):
                solution='10'+solution
            elif (a[i] == '1' and b[i]=='0') or (a[i] == '0' and b[i] =='1'):
                solution=solution+'1'
            else:
                solution = solution+'0'
            i -= 1
        return solution

if __name__ == '__main__':
    solution = Solution()
    print(solution.addBinary('11', '1'))
    print(solution.addBinary('1010', '1011'))
