'''
https://leetcode.com/problems/happy-number/
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''

class Solution:
    def get_digit(self, number, n):
        return number // 10 ** n % 10

    def isHappy(self, n: int) -> bool:
        digitCount = 0
        num = n
        while num != 0:
            num //= 10
            digitCount += 1
        print("digitCounT",digitCount)
        loops = 0
        num = n
        sum = 0
        while sum != 1 and loops < 100 :
            sum = 0
            digitCount = 0
            num2 = num
            while num2 != 0:
                num2 //= 10
                digitCount += 1
            print("digitCount", digitCount)
            for i in range (0, digitCount):
                digit=self.get_digit(num, i)
                sum += digit*digit
            num=sum
            print("sum: ", sum)
            loops+=1
        if(loops == 100):
            return False
        return True



if __name__ == '__main__':
    solution = Solution()
    #print(solution.isHappy(19))
    print(solution.isHappy(2))