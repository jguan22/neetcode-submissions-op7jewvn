class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        low = prices[0]
        max_profit = 0
        
        for i in range(n):
            if prices[i] < low:
                low = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - low)
        
        return max_profit