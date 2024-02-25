'''
https://leetcode.com/problems/reverse-bits/
Reverse bits of a given 32 bits unsigned integer.
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        binaryList = list(n)
        reversed = []
        for bit in binaryList:
            reversed = [bit]+reversed
        return(''.join(reversed))

if __name__ == '__main__':
    solution = Solution()
    #print(solution.reverseBits(12))
    print(solution.reverseBits(0b00000010100101000001111010011100))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
