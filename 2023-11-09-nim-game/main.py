'''
https://leetcode.com/problems/nim-game/
You are playing the following Nim Game with your friend:
Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.
'''

# class Solution:
#     def __init__(self):
#         self.myTurn = True
#     def canWinNim(self, n: int) -> bool:
#         print("n=", n)
#         print("myTurn: ", self.myTurn)
#         if(n<=3):
#             if(self.myTurn):
#                 return True
#             else:
#                 return False
#         self.myTurn = not self.myTurn
#         if(self.canWinNim(n-3)):
#             return True
#         elif(self.canWinNim(n-2)):
#             return True
#         elif(self.canWinNim(n-1)):
#             return True
#         return False

#Best Solution:
class Solution:
    def canWinNim(self, n: int) -> bool:
        return bool(n % 4)

if __name__ == '__main__':
    # print(Solution().canWinNim(4))
    # print(Solution().canWinNim(1))
    # print(Solution().canWinNim(2))
    print(Solution().canWinNim(8))

