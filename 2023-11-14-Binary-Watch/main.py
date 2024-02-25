'''
https://leetcode.com/problems/binary-watch/
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.
'''

from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def bit_counter(n):
            s = bin(n)[2:]
            temp = 0
            for i in s:
                if i == '1':
                    temp += 1
            return temp

        result = []

        for h in range(12):
            for m in range(60):
                if bit_counter(h) + bit_counter(m) == turnedOn:
                    result.append(f'{h}:{m:02}')

        return result

if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
