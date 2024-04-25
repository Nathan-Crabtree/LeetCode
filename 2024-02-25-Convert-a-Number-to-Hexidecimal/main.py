#https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
# Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) -> str:
        #print('num = ', num)
        hex_string = '0123456789abcdef'
        if num == 0:
            return hex_string[0]
        # If the input number is negative, convert it to its corresponding positive value using two's complement
        if num < 0:
            num = (1 << 32) + num

        #print("num//16 = ", num//16)
        remainder = num % 16
        
        #print("remainder: ", remainder)
        #print("hex_string[remainder] = ", hex_string[remainder])
        hex_number = ''
        hex_number = hex_string[remainder] + hex_number
        #print("hex_number: ", hex_number)
        i = 0
        while num // 16 >= 1:
            num = num//16
            #print('Num = ', num)
            remainder = num % 16
            #print("Remainder: ", remainder)
            hex_number = hex_string[remainder] + hex_number
            #print("hex_number: ", hex_number)
        #print('')
        return hex_number



print(Solution().toHex(485))
print(Solution().toHex(48))
print(Solution().toHex(26))
print(Solution().toHex(-1))
print(Solution().toHex(0))