#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            #print(i) 
            sub_max_profit = 0
            for j in range(i+1,len(prices)):
                #print ("    ",j)
                profit = prices[j] - prices[i]
                if profit > sub_max_profit:
                    #print("        new sub_max_profit found: ", profit, " prices[", i, "]: ", prices[i], " prices[", j, "]: ", prices[j])
                    sub_max_profit = profit
            if sub_max_profit > max_profit:
                max_profit = sub_max_profit
        return max_profit
    
if __name__ == "__main__":
    solution = Solution()
    print("Max Profit: ", solution.maxProfit([1,10,3,5,8,3,5,10,2,10,8,9,3,1]))
    print("Max Profit: ", solution.maxProfit([5,4,3,2,1,0]))
    print("Max Profit: ", solution.maxProfit([5,10,3,5,8,3,5,10,2,10,8,9,3,1]))
