class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currLow = float('inf')
        for price in prices:
            currLow = min(currLow, price)
            maxProfit = max(maxProfit, price - currLow)
        return maxProfit