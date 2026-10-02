class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 1

        while sell < len(prices): 
            if prices[buy] > prices[sell]:
                buy = sell
            else:
                cur_profit = prices[sell]-prices[buy]
                res = max(cur_profit, res)
            sell += 1
            
        return res