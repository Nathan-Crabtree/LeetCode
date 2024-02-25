from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_customer_money = 0
        for customer in accounts:
            account_money_total = 0
            for account_money in customer:
                account_money_total += account_money
            if account_money_total > richest_customer_money:
                richest_customer_money = account_money_total 
        return richest_customer_money
        
if __name__ == "__main__":
    solution = Solution()
    accounts_list_2 = [[0,1,2],[3,4,5]]
    type(accounts_list_2)
    print(solution.maximumWealth(accounts = accounts_list_2))
    