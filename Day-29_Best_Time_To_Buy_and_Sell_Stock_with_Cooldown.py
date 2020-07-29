'''
        Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]



'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dpsell_1 = 0
        dpbuy_1 = 0
        dpbuy_2 = 0
        for i in range(n-1, -1, -1):
            # if buy
            op1 = -prices[i] + dpsell_1
            op2 = dpbuy_1
            old_dpbuy_1 = dpbuy_1
            dpbuy_1 = max(op1, op2)

            op1 = prices[i] + dpbuy_2
            op2 = dpsell_1
            dpsell_1 = max(op1, op2)
            dpbuy_2 = old_dpbuy_1
        return dpbuy_1