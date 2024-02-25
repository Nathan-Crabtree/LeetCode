'''
https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
'''

def guess(num: int) -> int:
    pick = 2
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0
class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        myGuess = (right + left+1)//2
        while right >= left:
            print("myGuess: ", myGuess)
            guessResult = guess(myGuess)
            print("Guess Result:", guessResult)
            if(guessResult ==1):
                left = myGuess
            if(guessResult==-1):
                right = myGuess
            if(guessResult == 0):
                return myGuess
            myGuess = (right+left+1)//2

if __name__ == '__main__':
    print(Solution().guessNumber(2))