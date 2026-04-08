class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = number of ways to decode at ith position
        # two possible ways to add: single digit(always valid), double(depending on i-1)
        # edge case
        if not s:
            return 0

        n = len(s)
        
        # dp[i] = ways to decode s[:i]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string
        
        for i in range(1, n + 1):
            # Single digit (if not '0')
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two digits (if valid and i >= 2)
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]