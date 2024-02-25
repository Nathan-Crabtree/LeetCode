'''
https://leetcode.com/problems/counting-bits/
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
'''
from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            print('i:', i)
            binary = format(i, 'b')
            count = 0
            for char in binary:
                if char == '1':
                    count+=1
            ans.append(count)
        return ans

if __name__ == '__main__':
    print(Solution().countBits(5))