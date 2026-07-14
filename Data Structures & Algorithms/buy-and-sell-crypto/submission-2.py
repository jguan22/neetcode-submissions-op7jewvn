class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # not dp: can only buy and sell once
        # sliding window with greedy O(n)
        l = 0
        max_profit = 0

        for r in range(1, len(prices)):
            # find a smaller selling point, move left
            if prices[r] < prices[l]:
                l = r
            else:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
        
        return max_profit
