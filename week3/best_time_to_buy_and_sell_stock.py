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
                       
    # some concept but shorter
    def maxProfit(self, prices):
        if not len(prices): return 0
        
        # pick a random or the first one
        buy_price = prices[0];
        profit = 0;
        # loop over each price
        for price in prices[1:]:
            # pricie - buy_price == the profit for this price
            # if current price is less then previouse price 
            # recored the min buyprice
            buy_price = min(buy_price, price);
            # recored if previous profit is larger than current profit
            profit = max(profit, price - buy_price);
        
        return profit; 
        
