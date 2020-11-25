'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''


def maxProfit(self, prices: List[int]) -> int:

    lowest = float('inf')
    profit = 0

    for i in range(len(prices)):

        if prices[i] < lowest:
            lowest = prices[i]

        _profit = prices[i]-lowest
        if _profit > profit:
            profit = _profit

    return profit
