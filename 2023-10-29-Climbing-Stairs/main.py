'''
https://leetcode.com/problems/climbing-stairs/
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if(n==1 or n==0):
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(14))
