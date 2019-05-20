"""
Time : O(n)
Space: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) <1:
            return 0
        min_price = prices[0]
        max_profit = 0        
        for price in prices:
            if price < min_price:
                min_price = price
                
            else:
                # diff between previous profit and current profit
                max_profit = max(max_profit, price - min_price)
            print(max_profit)
        return max_profit
                       
